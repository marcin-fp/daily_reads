#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "certifi>=2025.8.3",
#   "pymupdf4llm>=0.2.0",
# ]
# ///
"""Fetch an arXiv paper and create validated canonical Markdown.

Always converts the newest arXiv version of the given paper id.
Never aborts on a missing source: PDF -> LaTeX+Pandoc -> local raw dump.
Text only: figures are OCR'd into the text, no image files are kept.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import ssl
import subprocess
import sys
import tarfile
import tempfile
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

ARXIV_ID_RE = re.compile(
    r"(?:arxiv:|https?://(?:www\.)?arxiv\.org/(?:abs|pdf|html)/)?"
    r"(?P<base>\d{4}\.\d{4,5})(?P<version>v\d+)?(?:\.pdf)?$",
    re.IGNORECASE,
)
INPUT_RE = re.compile(
    r"(?<!\\)\\(?:input|include)(?![a-zA-Z@])\s*(?:\{([^}]+)\}|([^\s%]+))"
)
VERBATIM_RE = re.compile(
    r"\\begin\{(Verbatim|verbatim|lstlisting|minted|alltt)\*?\}.*?"
    r"\\end\{\1\*?\}",
    re.DOTALL,
)
COMMENT_RE = re.compile(r"(?<!\\)%.*")
IMAGE_LINK_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\([^)]*\)")
DOCUMENT_RE = re.compile(r"\\documentclass(?:\[[^\]]*\])?\{[^}]+\}")
TITLE_RE = re.compile(r"\\title(?:\[[^\]]*\])?\{(.+?)\}", re.DOTALL)
AUTHOR_RE = re.compile(r"\\author(?:\[[^\]]*\])?\{(.+?)\}", re.DOTALL)
TABLE_ENV_RE = re.compile(r"\\begin\{(?:longtable|tabular\*?|tabularx)\}")
MARKDOWN_TABLE_RE = re.compile(
    r"^\s*\|.*\|\s*\n\s*\|(?:\s*:?-+:?\s*\|)+\s*$", re.MULTILINE
)
TABLE_CAPTION_RE = re.compile(r"\bTable\s+\d+\s*:", re.IGNORECASE)


@dataclass(frozen=True)
class ArxivId:
    base: str
    version: str | None

    @property
    def full(self) -> str:
        return self.base + (self.version or "")


def parse_id(value: str) -> ArxivId:
    match = ARXIV_ID_RE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"Not a supported modern arXiv id or URL: {value}")
    return ArxivId(match.group("base"), match.group("version"))


def fetch(url: str, destination: Path) -> None:
    import certifi

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "daily-reads-canonicalizer/1.0 (paper archiving)"},
    )
    try:
        context = ssl.create_default_context(cafile=certifi.where())
        with urllib.request.urlopen(request, timeout=120, context=context) as response:
            destination.write_bytes(response.read())
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"Download failed ({error.code}): {url}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"Download failed: {url} ({error})") from error


def fetch_metadata(paper: ArxivId) -> dict[str, object]:
    """Fetch latest-version metadata. Query the unversioned id so arXiv returns HEAD."""
    with tempfile.NamedTemporaryFile(suffix=".xml") as tmp:
        fetch(
            f"https://export.arxiv.org/api/query?id_list={paper.base}",
            Path(tmp.name),
        )
        root = ET.fromstring(Path(tmp.name).read_bytes())
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entry = root.find("atom:entry", ns)
    if entry is None:
        raise RuntimeError(f"No metadata returned for {paper.base}")
    title = " ".join((entry.findtext("atom:title", default="", namespaces=ns)).split())
    authors = [
        " ".join((author.findtext("atom:name", default="", namespaces=ns)).split())
        for author in entry.findall("atom:author", ns)
    ]
    published = entry.findtext("atom:published", default="", namespaces=ns)
    atom_id = entry.findtext("atom:id", default="", namespaces=ns) or ""
    tail = atom_id.rstrip("/").split("/")[-1]
    parsed = ARXIV_ID_RE.fullmatch(tail)
    latest = parsed.group("version") if parsed else paper.version
    resolved = ArxivId(paper.base, latest)
    return {
        "id": f"arxiv:{paper.base}",
        "title": title or paper.base,
        "authors": [author for author in authors if author],
        "year": int(published[:4]) if published[:4].isdigit() else 2000 + int(paper.base[:2]),
        "version": resolved.version or "latest",
        "source_url": f"https://arxiv.org/abs/{resolved.full}",
        "resolved_id": resolved.full,
    }


def resolve_latest(paper: ArxivId) -> tuple[ArxivId, dict[str, object] | None, str | None]:
    """Ignore any requested vN and use the newest arXiv version."""
    try:
        metadata = fetch_metadata(paper)
    except (OSError, RuntimeError, ValueError, ET.ParseError, urllib.error.URLError) as error:
        return paper, None, f"metadata: {type(error).__name__}: {error}"
    version = metadata.get("version")
    if isinstance(version, str) and re.fullmatch(r"v\d+", version):
        return ArxivId(paper.base, version), metadata, None
    return paper, metadata, None


def safe_extract(archive: Path, destination: Path) -> None:
    with tarfile.open(archive, "r:*") as tar:
        root = destination.resolve()
        for member in tar.getmembers():
            target = (destination / member.name).resolve()
            if root != target and root not in target.parents:
                raise RuntimeError(f"Unsafe path in source archive: {member.name}")
            if member.issym() or member.islnk():
                raise RuntimeError(f"Links are not allowed in source archive: {member.name}")
        tar.extractall(destination, filter="data")


def decode_tex(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8", errors="replace")


def tex_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.tex") if path.is_file())


def choose_root(source_root: Path) -> Path:
    candidates = [
        path for path in tex_files(source_root) if DOCUMENT_RE.search(decode_tex(path))
    ]
    if not candidates:
        raise RuntimeError("No LaTeX file containing \\documentclass was found")

    def score(path: Path) -> tuple[int, int]:
        text = decode_tex(path)
        return (
            10 * len(INPUT_RE.findall(text))
            + 5 * text.count(r"\begin{document}")
            + len(text) // 10_000,
            -len(path.parts),
        )

    return max(candidates, key=score)


def resolve_include(parent: Path, source_root: Path, name: str) -> Path | None:
    name = name.strip()
    candidate = parent / name
    if not candidate.suffix:
        candidate = candidate.with_suffix(".tex")
    candidates = [candidate, source_root / candidate.name]
    for path in candidates:
        if path.is_file() and source_root.resolve() in path.resolve().parents:
            return path
    return None


def flatten_tex(root_file: Path, source_root: Path) -> tuple[str, list[str]]:
    """Inline input/include recursively and report unresolved includes."""
    active: set[Path] = set()
    unresolved: list[str] = []

    def inline(path: Path) -> str:
        resolved = path.resolve()
        if resolved in active:
            unresolved.append(f"cycle:{path.relative_to(source_root)}")
            return f"% circular include skipped: {path}\n"
        active.add(resolved)
        text = decode_tex(path)

        def replace(match: re.Match[str]) -> str:
            name = match.group(1) or match.group(2)
            child = resolve_include(path.parent, source_root, name)
            if child is None:
                unresolved.append(
                    f"{path.relative_to(source_root)} -> {name}"
                )
                return match.group(0)
            return (
                f"\n% BEGIN INLINED {child.relative_to(source_root)}\n"
                f"{inline(child)}"
                f"\n% END INLINED {child.relative_to(source_root)}\n"
            )

        flattened = INPUT_RE.sub(replace, text)
        active.remove(resolved)
        return flattened

    return inline(root_file), unresolved


def clean_latex_for_pandoc(text: str) -> str:
    # Common visual wrappers around tables confuse Pandoc but carry no content.
    text = re.sub(
        r"\\resizebox\s*\{[^{}]*\}\s*\{[^{}]*\}\s*\{"
        r"(\s*\\begin\{(?:tabular\*?|tabularx|longtable)\}.*?"
        r"\\end\{(?:tabular\*?|tabularx|longtable)\}\s*)\}",
        r"\1",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\\begin\{adjustbox\}\{[^}]*\}(.*?)\\end\{adjustbox\}",
        r"\1",
        text,
        flags=re.DOTALL,
    )
    return text


def strip_tex(value: str) -> str:
    value = re.sub(r"\\(?:thanks|footnote)\{.*?\}", "", value, flags=re.DOTALL)
    value = re.sub(r"\\(?:textbf|textit|emph|mathrm|mathbf)\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"\\\\", "; ", value)
    value = re.sub(r"\\[a-zA-Z@]+\*?(?:\[[^\]]*\])?", " ", value)
    value = value.replace("{", "").replace("}", "")
    return html.unescape(re.sub(r"\s+", " ", value)).strip(" ;")


def source_metadata(flattened: str, paper: ArxivId) -> dict[str, object]:
    title_match = TITLE_RE.search(flattened)
    author_match = AUTHOR_RE.search(flattened)
    authors: list[str] = []
    if author_match:
        authors = [
            part.strip()
            for part in re.split(r"\\and|;|\n", strip_tex(author_match.group(1)))
            if part.strip()
        ]
    year = 2000 + int(paper.base[:2])
    return {
        "id": f"arxiv:{paper.base}",
        "title": strip_tex(title_match.group(1)) if title_match else paper.full,
        "authors": authors,
        "year": year,
        "version": paper.version or "latest",
        "source_url": f"https://arxiv.org/abs/{paper.full}",
    }


def yaml_scalar(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def frontmatter(metadata: dict[str, object], repair: str) -> str:
    authors = metadata.get("authors") or []
    author_yaml = ", ".join(yaml_scalar(str(author)) for author in authors)
    lines = [
        "---",
        f"id: {metadata['id']}",
        f"title: {yaml_scalar(str(metadata['title']))}",
        f"authors: [{author_yaml}]",
        f"year: {metadata['year']}",
        f"version: {metadata['version']}",
        f"source_url: {metadata['source_url']}",
    ]
    if metadata.get("raw"):
        lines.append(f"raw: {metadata['raw']}")
    lines.extend([f"repair: {repair}", "---", ""])
    return "\n".join(lines)


def find_raw(repo_root: Path, paper: ArxivId) -> str | None:
    dashed = paper.base.replace(".", "-")
    patterns = (
        f"{paper.full.replace('.', '-')}-pdf.md",
        f"{dashed}v*-pdf.md",
        f"{dashed}-pdf.md",
    )
    for pattern in patterns:
        candidates = sorted((repo_root / "papers" / "raw").rglob(pattern))
        if candidates:
            return candidates[-1].relative_to(repo_root).as_posix()
    return None


def drop_images(markdown: str) -> str:
    """Canonical files are text only. Keep alt text/captions, drop image links."""

    def replace(match: re.Match[str]) -> str:
        alt = match.group("alt").strip()
        return f"*Figure: {alt}*" if alt else ""

    markdown = IMAGE_LINK_RE.sub(replace, markdown)
    return re.sub(r"\n{3,}", "\n\n", markdown)


def brace_repair_candidates(text: str) -> list[int]:
    """Guess how many closing braces a sloppy preamble/body left open."""
    probe = VERBATIM_RE.sub("", text)
    probe = COMMENT_RE.sub("", probe)
    probe = re.sub(r"\\[{}]", "", probe)
    depth = probe.count("{") - probe.count("}")
    candidates: list[int] = []
    for delta in range(4):
        for value in (depth - delta, depth + delta):
            if 0 < value <= 12 and value not in candidates:
                candidates.append(value)
    return candidates


def run_pandoc(pandoc: str, tex: Path, source_root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            pandoc,
            str(tex),
            "--from=latex",
            "--to=gfm+tex_math_dollars",
            "--wrap=none",
            f"--resource-path={source_root}",
        ],
        cwd=source_root,
        check=False,
        capture_output=True,
        text=True,
    )


def pandoc_markdown(
    pandoc: str, flattened: str, work: Path, source_root: Path
) -> tuple[str, str]:
    """Run Pandoc, retrying with balanced braces when the LaTeX leaves groups open."""
    tex = work / "flattened.tex"
    tex.write_text(flattened, encoding="utf-8")
    result = run_pandoc(pandoc, tex, source_root)
    if result.returncode == 0:
        return result.stdout, "arxiv-source+pandoc"

    for count in brace_repair_candidates(flattened):
        patched = flattened.replace(
            "\\end{document}", "}" * count + "\n\\end{document}", 1
        )
        tex.write_text(patched, encoding="utf-8")
        retry = run_pandoc(pandoc, tex, source_root)
        if retry.returncode == 0:
            return retry.stdout, f"arxiv-source+pandoc (closed {count} open brace groups)"

    message = (result.stderr or "").strip().splitlines()
    detail = " / ".join(message[-2:]) if message else f"exit {result.returncode}"
    raise RuntimeError(f"Pandoc could not parse the LaTeX source: {detail}")


def convert_source(
    paper: ArxivId,
    work: Path,
    output: Path,
    extra_metadata: dict[str, object] | None = None,
) -> dict[str, object]:
    pandoc = shutil.which("pandoc")
    if pandoc is None:
        raise RuntimeError(
            "Pandoc is not installed (optional source mode: brew install pandoc)"
        )
    archive = work / "source.tar"
    source_root = work / "source"
    source_root.mkdir(exist_ok=True)
    fetch(f"https://export.arxiv.org/e-print/{paper.base}", archive)
    safe_extract(archive, source_root)
    root_file = choose_root(source_root)
    flattened, unresolved = flatten_tex(root_file, source_root)
    flattened = clean_latex_for_pandoc(flattened)

    markdown, repair = pandoc_markdown(pandoc, flattened, work, source_root)
    markdown = drop_images(markdown)
    metadata = extra_metadata or source_metadata(flattened, paper)
    output.write_text(frontmatter(metadata, repair) + markdown, encoding="utf-8")
    return {
        "mode": "source",
        "root_tex": str(root_file.relative_to(source_root)),
        "unresolved_includes": unresolved,
        "source_table_environments": len(TABLE_ENV_RE.findall(flattened)),
        "markdown_tables": len(MARKDOWN_TABLE_RE.findall(markdown)),
    }


def convert_raw(
    paper: ArxivId,
    output: Path,
    raw_rel: str,
    repo_root: Path,
    metadata: dict[str, object] | None,
) -> dict[str, object]:
    body = (repo_root / raw_rel).read_text(encoding="utf-8", errors="replace")
    if body.startswith("---"):
        parts = body.split("---", 2)
        if len(parts) == 3:
            body = parts[2].lstrip("\n")
    meta = metadata or {
        "id": f"arxiv:{paper.base}",
        "title": paper.base,
        "authors": [],
        "year": 2000 + int(paper.base[:2]),
        "version": paper.version or "latest",
        "source_url": f"https://arxiv.org/abs/{paper.full}",
    }
    meta = {**meta, "raw": raw_rel}
    output.write_text(frontmatter(meta, "raw-fallback") + body, encoding="utf-8")
    return {
        "mode": "raw",
        "raw": raw_rel,
        "markdown_tables": len(MARKDOWN_TABLE_RE.findall(body)),
        "table_captions": len(TABLE_CAPTION_RE.findall(body)),
    }


def convert_pdf(
    paper: ArxivId,
    work: Path,
    output: Path,
    extra_metadata: dict[str, object] | None = None,
) -> dict[str, object]:
    pdf = work / f"{paper.full}.pdf"
    fetch(f"https://export.arxiv.org/pdf/{paper.base}", pdf)

    import pymupdf4llm

    # Figures are OCR'd into the text; no image files are written.
    markdown = pymupdf4llm.to_markdown(
        str(pdf),
        write_images=False,
        embed_images=False,
        table_strategy="lines_strict",
    )
    markdown = drop_images(markdown)
    metadata = extra_metadata or {
        "id": f"arxiv:{paper.base}",
        "title": paper.base,
        "authors": [],
        "year": 2000 + int(paper.base[:2]),
        "version": paper.version or "latest",
        "source_url": f"https://arxiv.org/abs/{paper.full}",
    }
    output.write_text(frontmatter(metadata, "pdf+pymupdf4llm") + markdown, encoding="utf-8")
    return {
        "mode": "pdf",
        "markdown_tables": len(MARKDOWN_TABLE_RE.findall(markdown)),
        "table_captions": len(TABLE_CAPTION_RE.findall(markdown)),
    }


def validate(output: Path, report: dict[str, object]) -> list[str]:
    text = output.read_text(encoding="utf-8")
    warnings: list[str] = []
    if len(text) < 5_000:
        warnings.append(f"output is suspiciously short ({len(text):,} characters)")
    source_tables = int(report.get("source_table_environments", 0))
    markdown_tables = int(report.get("markdown_tables", 0))
    table_captions = int(report.get("table_captions", 0))
    if source_tables and markdown_tables < source_tables:
        warnings.append(
            f"Pandoc emitted {markdown_tables} Markdown tables from "
            f"{source_tables} LaTeX table/tabular environments; inspect tables"
        )
    if table_captions > markdown_tables:
        warnings.append(
            f"found {table_captions} table captions but only "
            f"{markdown_tables} Markdown tables; inspect missing tables"
        )
    unresolved = report.get("unresolved_includes", [])
    if unresolved:
        warnings.append(f"{len(unresolved)} LaTeX includes were unresolved")
    if r"\begin{tabular" in text:
        warnings.append("raw tabular LaTeX remains in output")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Create canonical Markdown from the newest arXiv version. "
            "Falls back PDF -> LaTeX+Pandoc -> local raw dump; never crashes. "
            "The Markdown file is the only artifact."
        )
    )
    parser.add_argument("paper", help="arXiv id or abs/pdf/html URL (any version; latest is used)")
    parser.add_argument(
        "--mode", choices=("auto", "pdf", "source"), default="auto",
        help="auto tries PDF (with figure OCR), then LaTeX source, then the raw dump",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path("papers/canonical"),
    )
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    try:
        requested = parse_id(args.paper)
    except ValueError as error:
        parser.error(str(error))

    failures: list[str] = []
    paper, metadata, meta_error = resolve_latest(requested)
    if meta_error:
        failures.append(meta_error)
    if requested.version and paper.version and requested.version != paper.version:
        print(
            f"Using newest version {paper.full} (request was {requested.full})",
            file=sys.stderr,
        )

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{paper.base}.md"
    if output.exists() and not args.force:
        parser.error(f"{output} exists; pass --force to replace it")

    repo_root = Path(__file__).resolve().parent.parent
    raw = find_raw(repo_root, paper)
    report: dict[str, object] | None = None
    warnings: list[str] = []

    try:
        # Everything downloaded (PDF, LaTeX tarball, OCR images) lives here and
        # is deleted on exit; only the Markdown file survives.
        with tempfile.TemporaryDirectory(prefix=f"arxiv-{paper.full}-") as tmp:
            work = Path(tmp)
            if args.mode in ("auto", "pdf"):
                try:
                    report = convert_pdf(paper, work, output, extra_metadata=metadata)
                except Exception as error:  # noqa: BLE001 - conversion must fall through
                    failures.append(f"pdf: {type(error).__name__}: {error}")
            if report is None:
                try:
                    report = convert_source(paper, work, output, extra_metadata=metadata)
                except Exception as error:  # noqa: BLE001 - conversion must fall through
                    failures.append(f"source: {type(error).__name__}: {error}")
            if report is None and raw:
                try:
                    report = convert_raw(paper, output, raw, repo_root, metadata)
                    failures.append("used local raw dump because PDF and source failed")
                except Exception as error:  # noqa: BLE001 - last-resort dump
                    failures.append(f"raw: {type(error).__name__}: {error}")
            if report is None:
                print(
                    "No PDF, LaTeX source, or local raw dump could be converted.",
                    file=sys.stderr,
                )
                for failure in failures:
                    print(f"  {failure}", file=sys.stderr)
                return 1

            if raw and report.get("mode") != "raw":
                text = output.read_text(encoding="utf-8")
                if re.search(r"^raw:", text, re.MULTILINE) is None:
                    text = text.replace("\nrepair:", f"\nraw: {raw}\nrepair:", 1)
                    output.write_text(text, encoding="utf-8")
            warnings = validate(output, report)
    except Exception as error:  # noqa: BLE001 - never abort with a traceback
        print(f"Conversion failed without a usable file: {error}", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1

    print(f"Wrote {output}")
    print(f"Mode: {report['mode']} ({paper.full})")
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for failure in failures:
        print(f"FALLBACK: {failure}", file=sys.stderr)
    if report.get("mode") == "raw":
        return 3
    return 0 if not warnings else 2


if __name__ == "__main__":
    raise SystemExit(main())
