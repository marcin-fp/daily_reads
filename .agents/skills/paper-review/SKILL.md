---
name: paper-review
description: Review a research paper into reviews/{id}.md with a plain-language brief, extended summary, learnings, lemmalog claims, and an honest discussion against FirstPrinciples context. Use when asked to review, summarize, or extract facts from a paper (PDF, MD, or arXiv id).
---

# Paper Review

## Quick start

Resolve via [`papers/index.md`](../../../papers/index.md): **canonical MD first**, else raw. Write `reviews/{id}.md` (id without version). Never write next to the dump.

Read [CONTEXT.md](CONTEXT.md) (authority: approved bets > personal perspective > IAIFI customer lens) and [TAXONOMY.md](TAXONOMY.md) (suggested questions, not labels). Then draft. **Do not force-fit.** Empty sections are correct when the paper does not earn them.

## Workflow

### 1. Resolve and read

Canonical over raw. MD: Read. PDF: `pdftotext` or Read. If the extract is broken, say so (see repo README repair note) and review from what is usable.

### 2. Draft (length follows the paper)

Follow the template below. Skip or write `None.` for any section with nothing real to say. Do not pad.

- **What this paper is about** — scientists, not ML-jargon-first. Problem, what they did, what they claim. Short.
- **Extended summary** — methods, setups, headline numbers, caveats that change the claim. Include details a later agent would otherwise re-read the PDF for. Still no fake precision.
- **Learnings** — surprising or reusable observations. Omit if none.
- **Claims** — lemmalog edges. See [CLAIMS.md](CLAIMS.md). **Empty table is allowed.**
- **Discussion** — only if CONTEXT/TAXONOMY actually fire: evidence for/against a tension; a possible mechanism for an approved bet; a customer (IAIFI) signal; or that **our framing is incomplete or wrong**. If the paper is irrelevant to us, one blunt sentence beats a strained paragraph. New bets/arcs are allowed; do not silently map them onto the nearest existing id.

Voice: first-person is fine; technically precise; no Slack hooks (“Interesting Paper!”).

### 3. Write files and memory

1. Save `reviews/{id}.md` with YAML `paper:` / `canonical:` / `raw:`.
2. Update `papers/index.md` to `reviewed`.
3. If Claims is non-empty and lemmalog MCP/`lemmalog-cli` exists, assert now ([`lemmalog/SCHEMA.md`](../../../lemmalog/SCHEMA.md)). If tools are missing, say so once. Skip assert on an empty Claims section.

## Output template

```
---
paper: arxiv:YYMM.NNNNN
canonical: papers/canonical/YYMM.NNNNN.md
raw: papers/raw/YYYY-MM-DD/…
---

Citation: Author(s). Title. Venue, Year. URL

## What this paper is about

[Short, no-jargon-first. Scientists in physics/CS should get it.]

## Extended summary

[Details that matter. Caveats. Missing baselines if they matter.]

## Learnings

[None.  — or a short list]

## Claims

[Table per CLAIMS.md, or: None.]

## Discussion

[None.  — or honest relevance / disagreement / new direction]
```
