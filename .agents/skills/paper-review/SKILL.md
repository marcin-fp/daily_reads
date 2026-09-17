---
name: paper-review
description: Review a research paper into reviews/{id}.md with a plain-language brief, extended summary, reusable learnings, verification notes when present, lemmalog claims, and a grounded critical discussion. Use when asked to review, summarize, critique, or extract facts from a paper (PDF, MD, or arXiv id), including papers that mention verification, process rewards, or physics checking only in passing.
---

# Paper Review

## Quick start

Resolve via [`papers/index.md`](../../../papers/index.md): canonical MD first, else raw. Write `reviews/{id}.md` (id without version). Never write next to the dump.

Read [CONTEXT.md](CONTEXT.md), [TAXONOMY.md](TAXONOMY.md), [VERIFICATION.md](VERIFICATION.md), [STYLE.md](STYLE.md), and [CLAIMS.md](CLAIMS.md). Then draft. Do not force-fit our bets onto a paper that is not about them. Empty sections are correct when the paper does not earn them, except Discussion, which always scrutinizes the paper's own claims. Do not open other repo context folders while reviewing; those files are already distilled here.

## Workflow

### 1. Resolve and read

Canonical over raw. MD: Read. PDF: `pdftotext` or Read. If the extract is broken, say so (see repo README repair note) and review from what is usable.

### 2. Draft (length follows the paper)

Follow the template. Keep every heading. Write `None.` when a section has nothing real to say. Do not pad. Discussion is never `None.`: if the extract is usable, scrutinize the claims, even briefly.

- What this paper is about: scientists, not jargon-first. Problem, what they did, what they claim. Short.
- Extended summary: methods, setups, headline numbers, caveats that change the claim. Include details a later agent would otherwise re-read the PDF for. No fake precision.
- Learnings: reusable mechanisms or surprises, in the style of [STYLE.md](STYLE.md). `None.` if nothing transfers.
- Verification: what the paper actually says about checking claims, steps, traces, citations, or rewards. Central or satellite. `None.` if silent. See [VERIFICATION.md](VERIFICATION.md).
- Claims: lemmalog edges (the paper's stated relations, not your verdict). See [CLAIMS.md](CLAIMS.md). `None.` if empty.
- Discussion: two jobs. First, scrutinize the paper and the claims it makes. We are doing science, not repeating a pitch. If they compare against a weak or crippled baseline, note it. If they overclaim (headline stronger than the setup, on-distribution only sold as general, same-family LLM judge, contamination, unmeasured coverage, a mechanism that does not follow from the result), note it. Ground every objection in something the paper did or failed to do. Do not invent flaws to sound critical, and do not soften real ones to sound nice. Second, only if CONTEXT / TAXONOMY / VERIFICATION actually fire, say what it means for us. If the paper is irrelevant to us, one blunt sentence of relevance is enough; the scientific critique still happens. New bets or arcs are allowed; do not silently map them onto the nearest existing id.

Voice: [STYLE.md](STYLE.md).

### 3. Write files and memory

1. Save `reviews/{id}.md` with YAML `paper:` / `canonical:` / `raw:`.
2. Update `papers/index.md` to `reviewed`.
3. If Claims is non-empty and lemmalog MCP/`lemmalog-cli` exists, assert now ([`lemmalog/SCHEMA.md`](../../../lemmalog/SCHEMA.md)). If tools are missing, say so once. Skip assert on an empty Claims section.

## Output template

```
---
paper: arxiv:YYMM.NNNNN
canonical: papers/canonical/YYYY-MM-DD/YYMM.NNNNN.md
raw: papers/raw/YYYY-MM-DD/…
---

Citation: Author(s). Title. Venue, Year. URL

## What this paper is about

[Short. A physicist or CS colleague should get it without decoding slang.]

## Extended summary

[Details that matter. Caveats. Missing baselines if they matter.]

## Learnings

[None.  or a few short paragraphs, one finding each]

## Verification

[None.  or what they check, how, coverage/precision, who judges]

## Claims

[Table per CLAIMS.md, or: None.]

## Discussion

[Scrutinize the claims. Weak baselines, overclaims, circular eval, missing controls: name them if they are there. Then relevance to us only if earned.]
```
