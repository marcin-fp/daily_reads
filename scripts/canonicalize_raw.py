#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "certifi>=2025.8.3",
#   "pymupdf4llm>=0.2.0",
# ]
# ///
"""Walk a papers/raw dump and write canonical Markdown.

ArXiv files are converted with scripts/arxiv_to_md.py (newest version, auto
fallback). Non-arXiv dumps are copied as-is. Existing canonical files are
skipped unless --force is set.

Output mirrors the dump folders: papers/raw/2026-05-06/*.md becomes
papers/canonical/2026-05-06/*.md. A paper that appears in two dumps stays in the
folder where it landed first, so each id has exactly one canonical file.

Every job is appended to a JSONL log as it finishes, so an aborted run still
leaves a usable record. Re-run the problem papers with --retry-from LOG.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import signal
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from arxiv_to_md import ARXIV_ID_RE, ConversionResult, convert_paper

RAW_ARXIV_FILE = re.compile(
    r"^(?P<yyyy>\d{4})-(?P<nnnnn>\d{4,5})(?P<version>v\d+)?(?:-pdf)?\.md$"
)
RAW_DIR_NAME = "raw"


@dataclass
class Job:
    kind: str  # arxiv | copy
    label: str
    paper_id: str | None
    source: Path
    dest: Path


@dataclass
class Counts:
    scanned: int = 0
    jobs: int = 0
    skipped: int = 0
    duplicates: int = 0
    converted: int = 0
    copied: int = 0
    warnings: int = 0
    raw_fallback: int = 0
    failed: int = 0
    problems: list[str] = field(default_factory=list)


class RunLog:
    """Append-only JSONL log, flushed per record so aborted runs keep their data."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.handle = self.path.open("a", encoding="utf-8")

    def record(self, job: Job, result: ConversionResult, seconds: float) -> None:
        entry = {
            "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "id": job.label,
            "kind": job.kind,
            "status": result.status,
            "ok": result.ok,
            "arxiv_version": result.paper if job.kind == "arxiv" else None,
            "source": str(job.source),
            "output": str(result.output) if result.output else None,
            "warnings": result.warnings,
            "fallbacks": result.fallbacks,
            "error": result.error,
            "seconds": round(seconds, 2),
        }
        self.handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
        self.handle.flush()

    def close(self) -> None:
        self.handle.close()


def needs_attention(entry: dict[str, object]) -> str | None:
    """Classify a log entry as something worth retrying, or None if it is clean."""
    if not entry.get("ok"):
        return "failed"
    if entry.get("status") == "raw":
        return "raw-fallback"
    if entry.get("warnings"):
        return "warning"
    return None


def read_retry_ids(log_path: Path) -> dict[str, str]:
    """Latest reason per paper id from a previous log. Clean re-runs clear an id."""
    reasons: dict[str, str] = {}
    for line in log_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        paper_id = entry.get("id")
        if not isinstance(paper_id, str) or entry.get("status") == "skipped":
            continue
        reason = needs_attention(entry)
        if reason:
            reasons[paper_id] = reason
        else:
            reasons.pop(paper_id, None)
    return reasons


def discover_raw(raw_root: Path) -> list[Path]:
    return sorted(
        path
        for path in raw_root.rglob("*.md")
        if path.is_file() and not path.name.startswith(".")
    )


def parse_raw_arxiv(path: Path) -> tuple[str, str | None] | None:
    match = RAW_ARXIV_FILE.fullmatch(path.name)
    if not match:
        return None
    base = f"{match.group('yyyy')}.{match.group('nnnnn')}"
    if not ARXIV_ID_RE.fullmatch(base):
        return None
    return base, match.group("version")


def canonical_stem(path: Path) -> str:
    name = path.name
    if name.endswith("-pdf.md"):
        return name[: -len("-pdf.md")]
    return path.stem


def mirror_subdir(source: Path, raw_root: Path) -> Path:
    """Folder of a raw file relative to papers/raw, so canonical mirrors the dump dates.

    Anchored on the nearest ancestor named `raw` so that pointing the script at
    papers/raw or at papers/raw/2026-05-06 both yield canonical/2026-05-06/.
    """
    parts = source.parent.parts
    if RAW_DIR_NAME in parts:
        index = len(parts) - parts[::-1].index(RAW_DIR_NAME)
        return Path(*parts[index:])
    try:
        return source.parent.relative_to(raw_root)
    except ValueError:
        return Path()


def plan_jobs(raw_files: list[Path], output_dir: Path, raw_root: Path) -> list[Job]:
    arxiv_sources: dict[tuple[Path, str], Path] = {}
    jobs: list[Job] = []
    for path in raw_files:
        subdir = mirror_subdir(path, raw_root)
        dest_dir = output_dir / subdir if subdir.parts else output_dir
        parsed = parse_raw_arxiv(path)
        if parsed is None:
            stem = canonical_stem(path)
            jobs.append(Job("copy", stem, None, path, dest_dir / f"{stem}.md"))
            continue
        base, _version = parsed
        # Keep the last filename for this base (walk is sorted; later versions
        # typically sort after earlier ones). Conversion always fetches HEAD.
        arxiv_sources[(dest_dir, base)] = path
    for (dest_dir, base), source in arxiv_sources.items():
        jobs.append(Job("arxiv", base, base, source, dest_dir / f"{base}.md"))
    jobs.sort(key=lambda job: (job.kind != "arxiv", str(job.dest)))
    return jobs


def existing_canonical(output_dir: Path) -> dict[str, Path]:
    """Canonical stem -> file, so a paper already converted under one dump date is
    not converted again under another."""
    found: dict[str, Path] = {}
    for path in sorted(output_dir.rglob("*.md")):
        found.setdefault(path.stem, path)
    return found


def copy_as_is(job: Job) -> ConversionResult:
    job.dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(job.source, job.dest)
    return ConversionResult(
        ok=True,
        status="copied",
        paper=job.label,
        output=job.dest,
        warnings=[],
        fallbacks=[],
    )


def install_interrupt_handler() -> None:
    """The PDF/OCR stack resets SIGINT, so reinstate Ctrl-C as KeyboardInterrupt."""

    def handler(signum: int, frame: object) -> None:
        raise KeyboardInterrupt

    signal.signal(signal.SIGINT, handler)


def dest_label(dest: Path, output_dir: Path) -> str:
    try:
        return str(dest.relative_to(output_dir))
    except ValueError:
        return dest.name


def print_result(job: Job, result: ConversionResult, output_dir: Path) -> None:
    mark = {
        "skipped": "skip",
        "duplicate": "dup ",
        "copied": "copy",
        "pdf": "ok  ",
        "source": "ok  ",
        "raw": "raw ",
        "failed": "FAIL",
    }.get(result.status, result.status[:4])
    extra = ""
    if result.status == "duplicate" and result.output:
        extra = f" -> already at {dest_label(result.output, output_dir)}"
    elif result.status not in ("skipped", "copied") and result.paper:
        extra = f" [{result.paper}]"
    print(f"[{mark}] {dest_label(job.dest, output_dir)}{extra}")
    for warning in result.warnings:
        print(f"       WARNING: {warning}")
    for fallback in result.fallbacks:
        print(f"       FALLBACK: {fallback}")
    if result.error:
        print(f"       ERROR: {result.error}")
    sys.stdout.flush()


def summarize(counts: Counts, log_path: Path | None, interrupted: bool) -> int:
    print()
    print("=== canonicalize_raw ===")
    if interrupted:
        print("run was interrupted; counts cover completed jobs only")
    print(f"raw files scanned:     {counts.scanned}")
    print(f"unique papers:         {counts.jobs}")
    print(f"skipped (exists):      {counts.skipped}")
    print(f"skipped (other dump):  {counts.duplicates}")
    print(f"converted (arxiv):     {counts.converted}")
    print(f"copied (non-arxiv):    {counts.copied}")
    print(f"raw-dump fallback:     {counts.raw_fallback}")
    print(f"with warnings:         {counts.warnings}")
    print(f"failed:                {counts.failed}")
    if counts.problems:
        print()
        print("Problems:")
        by_kind: dict[str, list[str]] = defaultdict(list)
        for line in counts.problems:
            kind, _, rest = line.partition(": ")
            by_kind[kind].append(rest or line)
        for kind, items in by_kind.items():
            print(f"  {kind} ({len(items)})")
            for item in items:
                print(f"    - {item}")
    if log_path:
        print()
        print(f"Log: {log_path}")
        if counts.problems:
            print(
                "Retry the problem papers with: "
                f"uv run scripts/canonicalize_raw.py <raw> --retry-from {log_path} "
                "--mode source"
            )
    if interrupted:
        return 130
    return 1 if counts.failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Regenerate papers/canonical from a raw dump folder, mirroring the "
            "dump subfolders. ArXiv papers use auto conversion of the newest "
            "version; everything else is copied as-is. Papers already canonical "
            "(here or under another dump date) are skipped."
        )
    )
    parser.add_argument(
        "raw",
        type=Path,
        help="Raw dump folder (e.g. papers/raw or papers/raw/2026-06-09)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("papers/canonical"),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite existing canonical Markdown",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="plan the work without writing files",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="process at most N jobs (0 = no limit)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="seconds to wait between arXiv conversions (politeness)",
    )
    parser.add_argument(
        "--mode",
        choices=("auto", "pdf", "source"),
        default="auto",
    )
    parser.add_argument(
        "--log",
        type=Path,
        default=None,
        help="JSONL log path (default logs/canonicalize-<timestamp>.jsonl)",
    )
    parser.add_argument(
        "--retry-from",
        type=Path,
        default=None,
        help=(
            "only process papers that failed, fell back to raw, or warned in "
            "this earlier log; implies --force"
        ),
    )
    args = parser.parse_args()

    raw_root = args.raw.resolve()
    if not raw_root.is_dir():
        parser.error(f"not a directory: {raw_root}")

    retry_reasons: dict[str, str] = {}
    if args.retry_from:
        if not args.retry_from.is_file():
            parser.error(f"no such log: {args.retry_from}")
        retry_reasons = read_retry_ids(args.retry_from)
        if not retry_reasons:
            print(f"Nothing to retry in {args.retry_from}")
            return 0
        args.force = True

    repo_root = Path(__file__).resolve().parent.parent
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    raw_files = discover_raw(raw_root)
    jobs = plan_jobs(raw_files, output_dir, raw_root)
    existing = existing_canonical(output_dir)
    if retry_reasons:
        jobs = [job for job in jobs if job.label in retry_reasons]
        print(f"Retrying {len(jobs)} papers from {args.retry_from}")
        for job in jobs:
            print(f"  {retry_reasons[job.label]}: {job.label}")
        print()
    if args.limit:
        jobs = jobs[: args.limit]

    counts = Counts(scanned=len(raw_files), jobs=len(jobs))
    converted_so_far = 0
    interrupted = False

    install_interrupt_handler()

    log: RunLog | None = None
    if not args.dry_run:
        stamp = datetime.now(tz=None).astimezone().strftime("%Y%m%d-%H%M%S")
        log_path = args.log or repo_root / "logs" / f"canonicalize-{stamp}.jsonl"
        log = RunLog(log_path.resolve())
        print(f"Log: {log.path}")

    try:
        for job in jobs:
            elsewhere = existing.get(job.label)
            if elsewhere is not None and elsewhere != job.dest:
                result = ConversionResult(
                    ok=True,
                    status="duplicate",
                    paper=job.label,
                    output=elsewhere,
                    warnings=[],
                    fallbacks=[],
                )
                counts.duplicates += 1
                print_result(job, result, output_dir)
                if log:
                    log.record(job, result, 0.0)
                continue
            if job.dest.exists() and not args.force:
                result = ConversionResult(
                    ok=True,
                    status="skipped",
                    paper=job.label,
                    output=job.dest,
                    warnings=[],
                    fallbacks=[],
                )
                counts.skipped += 1
                print_result(job, result, output_dir)
                if log:
                    log.record(job, result, 0.0)
                continue
            if args.dry_run:
                action = "copy" if job.kind == "copy" else "arxiv"
                existing[job.label] = job.dest
                print(
                    f"[plan] {action} {job.source.name} -> "
                    f"{dest_label(job.dest, output_dir)}"
                )
                continue

            started = time.monotonic()
            if job.kind == "copy":
                try:
                    result = copy_as_is(job)
                    counts.copied += 1
                except OSError as error:
                    result = ConversionResult(
                        ok=False,
                        status="failed",
                        paper=job.label,
                        output=None,
                        warnings=[],
                        fallbacks=[],
                        error=str(error),
                    )
                    counts.failed += 1
                    counts.problems.append(f"failed: {job.label}: {error}")
                if result.ok:
                    existing[job.label] = job.dest
                print_result(job, result, output_dir)
                if log:
                    log.record(job, result, time.monotonic() - started)
                continue

            if converted_so_far and args.delay > 0:
                time.sleep(args.delay)
            started = time.monotonic()
            result = convert_paper(
                job.paper_id or job.label,
                job.dest.parent,
                mode=args.mode,
                force=args.force,
                repo_root=repo_root,
            )
            converted_so_far += 1
            if result.ok and result.output:
                existing[job.label] = result.output
            print_result(job, result, output_dir)
            if log:
                log.record(job, result, time.monotonic() - started)
            if result.status == "skipped":
                counts.skipped += 1
            elif not result.ok:
                counts.failed += 1
                counts.problems.append(
                    f"failed: {job.label}: {result.error or 'unknown error'}"
                )
            else:
                counts.converted += 1
                if result.status == "raw":
                    counts.raw_fallback += 1
                    counts.problems.append(
                        f"raw-fallback: {job.label} ({result.paper})"
                    )
                if result.warnings:
                    counts.warnings += 1
                    for warning in result.warnings:
                        counts.problems.append(f"warning: {job.label}: {warning}")
                for fallback in result.fallbacks:
                    if fallback.startswith("used newest version"):
                        continue
                    counts.problems.append(f"fallback: {job.label}: {fallback}")
    except KeyboardInterrupt:
        interrupted = True
        print("\nInterrupted.", file=sys.stderr)
    finally:
        if log:
            log.close()

    if args.dry_run:
        print()
        print("(dry run — no files written)")
    return summarize(counts, log.path if log else None, interrupted)


if __name__ == "__main__":
    raise SystemExit(main())
