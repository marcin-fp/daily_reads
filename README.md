# Daily reads

Store papers, write personal reviews, map concepts with graphify, and derive multi-paper evidence chains with lemmalog.

## Layout

| Path | Role |
|------|------|
| `papers/raw/YYYY-MM-DD/` | Immutable dumps (PDF/HTML extracts). Do not edit. |
| `papers/canonical/` | Repaired markdown. One file per paper. Graphify corpus. |
| `papers/index.md` | id, paths, status (`raw` / `canonical` / `reviewed`). |
| `reviews/` | One review per paper: `{id}.md` (no version in the filename). |
| `news/` `perspectives/` `trends/` | Later synthesis. Empty scaffolds for now. |
| `lemmalog/` | Claim schema and Datalog rules. |
| `graphify-out/` | Graph built from **`papers/canonical` only**. |

## Paper ids

- arXiv: `arxiv:YYMM.NNNNN` — **no version in the id**. Version lives in canonical frontmatter.
- Canonical filename: `YYMM.NNNNN.md` (example: `2606.18195.md`).
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

- `paper-review` — plain-language brief, extended summary, learnings, Claims, and honest contextual discussion; writes `reviews/{id}.md`.
- `evidence-chains` — extract/assert claims; query two-hop chains; discuss with `why` trees.
- `graphify` / `lemmalog` — as vendored.

## Generate canonical Markdown

The script always fetches the **newest arXiv version** of the paper id you pass (a `v1` raw dump still yields the latest PDF/source). Canonical filename is unversioned: `papers/canonical/2605.26492.md`; the version lives in frontmatter.

**The Markdown file is the only artifact.** Text only: figures are OCR'd into the text (Tesseract, via PyMuPDF), and the downloaded PDF, LaTeX tarball, and extracted images are deleted with the temp dir.

It never crashes. Fallback order:

1. PDF → PyMuPDF4LLM, with figure OCR and table extraction
2. LaTeX source + Pandoc, if Pandoc is on `PATH` (unbalanced brace groups are auto-repaired)
3. Local `papers/raw/**` dump (`repair: raw-fallback`)

If every path fails, it prints the failed attempts and exits `1` without a traceback.

```bash
uv run scripts/arxiv_to_md.py 2605.26492v1
```

Existing files are protected. Regenerate with `--force`. `--mode pdf` or `--mode source` picks a starting point but still falls through. Table warnings exit `2`; raw fallback exits `3`.
