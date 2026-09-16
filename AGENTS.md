# Daily reads — agent instructions

This repo is a personal paper corpus. Canonical Markdown is the readable source of truth. Reviews, graphify, and lemmalog all build from that.

## Skills

Canonical copies live in **`.agents/skills/`** (Cursor). Claude Code loads the same files via **`.claude/skills/`**, which is a symlink to that folder. Edit only `.agents/skills/`.

| Skill | Use when |
|-------|----------|
| `paper-review` | Reviewing a paper into `reviews/{id}.md` |
| `evidence-chains` | Typed claims, two-hop links, `why` trees |
| `graphify` | Concept map over `papers/canonical` only |
| `lemmalog` | Assert/query claims in the Datalog store |
| `grill-me` | Stress-testing a plan until it is agreed |
| `handoff` | Compacting this session for another agent |

## Pipeline

1. Raw dumps stay in `papers/raw/YYYY-MM-DD/`. Do not edit them.
2. Canonical files mirror the dump date: `papers/raw/2026-05-06/` → `papers/canonical/2026-05-06/`. Bulk: `uv run scripts/canonicalize_raw.py papers/raw`. Single paper: `uv run scripts/arxiv_to_md.py <arxiv-id> --output-dir papers/canonical/<dump-date>`. Filename is unversioned (`2605.26492.md`); version is frontmatter. One canonical file per id — a paper in a second dump stays where it already is. Skip existing unless `--force`.
3. Review with `paper-review` → `reviews/{id}.md`. Empty sections are allowed; do not force-fit FirstPrinciples or the approved bets.
4. Graphify **`papers/canonical` only** (whole tree, all date folders), `--directed`. Never scan the repo root.
5. Evidence chains go through lemmalog, not the agent's head.

Paper ids: `arxiv:YYMM.NNNNN` with no version in the id.

## Do not

- Commit conversion logs (`logs/`) or graphify HTML/cache.
- Overwrite canonical Markdown unless the user asks to regenerate.
- Treat a table-formatting warning as missing content until you compare with `papers/raw`.
