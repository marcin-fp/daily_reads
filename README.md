# Daily reads

Store papers, write personal reviews, map concepts with graphify, and derive multi-paper evidence chains with lemmalog.

## Layout

| Path | Role |
|------|------|
| `papers/raw/YYYY-MM-DD/` | Immutable dumps (PDF/HTML extracts). Do not edit. |
| `papers/canonical/YYYY-MM-DD/` | Repaired markdown, one folder per dump date mirroring `papers/raw/`. One file per paper. Graphify corpus. |
| `papers/index.md` | id, paths, status (`raw` / `canonical` / `reviewed`). |
| `reviews/` | One review per paper: `{id}.md` (no version in the filename). |
| `news/` `perspectives/` `trends/` | Later synthesis. Empty scaffolds for now. |
| `lemmalog/` | Claim schema and Datalog rules. |
| `graphify-out/` | Graph built from **`papers/canonical` only**. |

## Paper ids

- arXiv: `arxiv:YYMM.NNNNN` — **no version in the id**. Version lives in canonical frontmatter.
- Canonical filename: `YYMM.NNNNN.md` under the dump date folder (example: `papers/canonical/2026-06-09/2606.18195.md`). One canonical file per id, in the folder of the dump that first brought it in.
- Other venues: `doi:…` or `slug:short-name`.

## Pipeline

1. Drop a dump into `papers/raw/YYYY-MM-DD/` and add a row to `papers/index.md` (`status: raw`).
2. Generate canonical Markdown with `scripts/arxiv_to_md.py` (below). Set `status: canonical`. Raw-only papers stay **off** the graphify corpus.
3. Review with the `paper-review` skill → `reviews/{id}.md` plus a **Claims** block. Assert claims to lemmalog when MCP/CLI is available.
4. Rebuild the concept map: graphify `papers/canonical` with `--directed`; later `--update`.
5. Find cross-paper chains with the `evidence-chains` skill (`two_hop`, then `lemmalog_why`). Do not close chains in the agent’s head.

## Graphify runbook

Scan root is **`papers/canonical`**, never the repo root (skills and reviews would pollute the graph). Outputs stay in repo-root `graphify-out/`. Point `.graphify_root` at the canonical folder:

```bash
mkdir -p graphify-out
echo "$(cd papers/canonical && pwd)" > graphify-out/.graphify_root
```

Then follow `.agents/skills/graphify/SKILL.md` with `INPUT_PATH=papers/canonical` and **`--directed`**. After new canonical files, use `--update`. Keep `graph.json` and `GRAPH_REPORT.md`; HTML and cache files are gitignored.

Graphify is the concept map (communities, surprising bridges, `query` / `path`). It is **not** the evidence-chain store. Promote a path into lemmalog only after checking the papers.

## Lemmalog

Schema: [`lemmalog/SCHEMA.md`](lemmalog/SCHEMA.md). Rules: [`lemmalog/rules/evidence-chains.dl`](lemmalog/rules/evidence-chains.dl). Skill: `.agents/skills/evidence-chains`.

## Skills

Canonical copies live in `.agents/skills/` (Cursor). Claude Code loads the same files through `.claude/skills/` (a symlink). Edit only `.agents/skills/`. Project instructions: `AGENTS.md` (Cursor) and `CLAUDE.md` (Claude Code; it includes `AGENTS.md`).

- `paper-review` — plain-language brief, extended summary, learnings, Claims, and honest contextual discussion; writes `reviews/{id}.md`.
- `evidence-chains` — extract/assert claims; query two-hop chains; discuss with `why` trees.
- `graphify` / `lemmalog` — as vendored.

## Generate canonical Markdown

The script always fetches the **newest arXiv version** of the paper id you pass (a `v1` raw dump still yields the latest PDF/source). Canonical filename is unversioned: `papers/canonical/2026-06-09/2605.26492.md`; the version lives in frontmatter. `arxiv_to_md.py` writes wherever `--output-dir` points, so pass the dump folder when converting by hand.

**The Markdown file is the only artifact.** Text only: figures are OCR'd into the text (Tesseract, via PyMuPDF), and the downloaded PDF, LaTeX tarball, and extracted images are deleted with the temp dir.

It never crashes. Fallback order:

1. PDF → PyMuPDF4LLM, with figure OCR and table extraction
2. LaTeX source + Pandoc, if Pandoc is on `PATH` (unbalanced brace groups are auto-repaired)
3. Local `papers/raw/**` dump (`repair: raw-fallback`)

If every path fails, it prints the failed attempts and exits `1` without a traceback.

```bash
uv run scripts/arxiv_to_md.py 2605.26492v1 --output-dir papers/canonical/2026-06-09
```

Existing files are protected. Regenerate with `--force`. `--mode pdf` or `--mode source` picks a starting point but still falls through. Table warnings exit `2`; raw fallback exits `3`.

Bulk conversion from a raw dump. Output mirrors the dump folders, so `papers/raw/2026-05-06/*` lands in `papers/canonical/2026-05-06/`, and papers that already have a canonical file are skipped:

```bash
uv run scripts/canonicalize_raw.py papers/raw
uv run scripts/canonicalize_raw.py papers/raw/2026-05-06 --dry-run
```

Pointing the script at `papers/raw` or at a single date folder gives the same destinations — the mirror is anchored on `papers/raw`, not on the argument.

ArXiv dumps are converted with auto mode against the newest version. Non-arXiv dumps are copied as-is. A paper that appears in two dumps keeps its first canonical file and is reported as `skipped (other dump)`, so every id has exactly one canonical copy. The summary at the end lists successes, skips, raw fallbacks, table warnings, and failures. `--force` overwrites; `--limit N` processes a prefix; `--delay` (default 1s) spaces arXiv fetches.

Every job is appended to `logs/canonicalize-<timestamp>.jsonl` (gitignored) as it finishes, flushed per line, so an aborted run keeps its record. Ctrl-C summarizes what completed and exits `130`. Re-run just the problem papers — failures, raw fallbacks, and table warnings — against that log:

```bash
uv run scripts/canonicalize_raw.py papers/raw --retry-from logs/canonicalize-20260916-124500.jsonl --mode source
```

`--retry-from` implies `--force`, and a clean result in a later log entry clears an id from the retry set.
