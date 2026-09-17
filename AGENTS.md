# Daily reads — agent instructions

This repo is a personal paper corpus. Canonical Markdown is the readable source of truth. Reviews, graphify, and lemmalog all build from that.

## Skills

Canonical copies live in **`.agents/skills/`** (Cursor). Claude Code loads the same files via **`.claude/skills/`**, which is a symlink to that folder. Edit only `.agents/skills/`.

| Skill | Use when |
|-------|----------|
| `paper-review` | Reviewing a paper into `reviews/{id}.md` |
| `evidence-chains` | Typed claims, two-hop links, `why` trees |
| `learning-synthesis` | Dated cross-paper learnings |
| `perspectives` | Dated, argued views for researchers |
| `trend-analysis` | Competitive research landscape for product/GTM/leads |
| `news-article` | One analytical article centered on a reviewed paper |
| `graphify` | Concept map; one graph per corpus folder (`papers/canonical/graphify-out`, later `reviews/graphify-out`) |
| `lemmalog` | Assert/query claims in the Datalog store |
| `grill-me` | Stress-testing a plan until it is agreed |
| `handoff` | Compacting this session for another agent |

## Pipeline

1. Raw dumps stay in `papers/raw/YYYY-MM-DD/`. Do not edit them.
2. Canonical files mirror the dump date: `papers/raw/2026-05-06/` → `papers/canonical/2026-05-06/`. Bulk: `uv run scripts/canonicalize_raw.py papers/raw`. Single paper: `uv run scripts/arxiv_to_md.py <arxiv-id> --output-dir papers/canonical/<dump-date>`. Filename is unversioned (`2605.26492.md`); version is frontmatter. One canonical file per id — a paper in a second dump stays where it already is. Skip existing unless `--force`.
3. `paper-review` is the only skill that reads canonical/raw full papers. It writes and validates schema-v1 `reviews/{id}.md`. Empty optional sections are allowed; do not force-fit FirstPrinciples or the approved bets. Critical discussion is required.
4. All synthesis (`evidence-chains`, `learning-synthesis`, `perspectives`, `trend-analysis`, `news-article`) reads reviews, lemmalog, prior snapshots, `papers/index.md` for counts, and the reviews graph only. Never reopen canonical/raw papers or use the full-paper graph as synthesis evidence. Missing evidence becomes a review gap routed back through `paper-review`.
5. Graphify lives **next to the corpus**, not at the repo root. Papers: `graphify extract papers/canonical --backend bedrock --directed` → `papers/canonical/graphify-out/`. Reviews: a separate `graphify extract reviews ...` → `reviews/graphify-out/`. Never scan the repo root.
6. Evidence chains go through lemmalog, not the agent's head. Lemmalog stores scientific relations/provenance plus one `reviewed_in` pointer per paper; all publication and landscape metadata stays in reviews. A graph path or `lemmalog_context` result is a candidate. Confirm with exact `lemmalog_query` and `why`; never consume `store.snapshot` or an unfiltered dump as research context.
7. Higher-level outputs are immutable dated Markdown snapshots under `learnings/`, `perspectives/`, `trends/`, and `news/`. Do not overwrite prior analyses; add a version suffix if needed.

Evidence has graded support, not a minimum-paper gate. A single paper may report or support a scoped claim. Use corroborated only for meaningfully independent sources and well-established only for diverse evidence without a strong unresolved contradiction. Peer review is context, not a correctness multiplier.

Paper ids: `arxiv:YYMM.NNNNN` with no version in the id.

## Do not

- Commit conversion logs (`logs/`) or machine-local graphify files (`.graphify_python`, `.graphify_root`, dated snapshot folders). Do track `graph.json`, `GRAPH_REPORT.md`, `graph.html`, `cache/`, labels, and analysis.
- Overwrite canonical Markdown unless the user asks to regenerate.
- Treat a table-formatting warning as missing content until you compare with `papers/raw`.
- Infer affiliations, funders, grants, or corporate support from names or prior knowledge. Record only relationships explicit in the paper/review.
- Treat counts in this selected corpus as prevalence in the whole research field.
