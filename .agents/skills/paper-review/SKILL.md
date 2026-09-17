---
name: paper-review
description: Produces a research-paper review in reviews/{id}.md with an accessible summary, reusable learnings, verification notes when present, lemmalog claims, a grounded critical discussion, and separate relevance to FirstPrinciples. Use when asked to review, summarize, critique, or extract facts from a paper (PDF, MD, or arXiv id), including papers that mention verification, process rewards, or physics checking only in passing.
disable-model-invocation: true
---

# Paper Review

## Quick start

Resolve via [`papers/index.md`](../../../papers/index.md): canonical MD first, else raw. Write `reviews/{id}.md` (id without version). Never write next to the dump.

Read [SCHEMA.md](SCHEMA.md), [CONTEXT.md](CONTEXT.md), [TAXONOMY.md](TAXONOMY.md), [VERIFICATION.md](VERIFICATION.md), [STYLE.md](STYLE.md), and [CLAIMS.md](CLAIMS.md). Then draft. Do not force-fit our bets onto a paper that is not about them. Do not open other repo context folders while reviewing; those files are already distilled here.

This review is the downstream source of truth. Later skills will not reopen the full paper, so preserve the publication metadata, decisive evidence, limitations, and field position they will need. It is still a briefing, not a second copy of the paper.

## Workflow

### 1. Resolve and read

Resolve through `papers/index.md`; canonical over raw. MD: Read. PDF: `pdftotext` or Read. The corpus is text-first: figures are not available for visual inspection, although captions or OCR text may have been extracted. Use that text when informative, but do not claim to have inspected a plot or diagram. If a result depends on an unavailable figure, say that it could not be assessed from the extract. If the extract is broken, say so (see repo README repair note) and review from what is usable.

Before drafting, fill the schema-v1 metadata:

1. Copy the title, authors, source URL, and reviewed version from canonical frontmatter when present.
2. Establish the earliest public date and the reviewed-version date from the paper landing page/API. Preserve month/year precision if an exact day is unavailable.
3. Extract explicit author affiliations, funders, grants, compute/data support, collaborators, and released artifacts from the author block and acknowledgments. Do not infer relationships.
4. Add compact facets and extract limitations. Add a critical flag only when Critical discussion explains it.

### 2. Draft (length follows the paper)

Follow the template. Keep every heading. Write `None.` when an optional section has nothing real to say. Do not pad. Critical discussion is required when the extract is usable; relevance to us is optional.

- What this paper is about: scientists, not jargon-first. Problem, what they did, what they claim. Short.
- Extended summary: methods, setups, headline numbers, and the authors' stated caveats. Include details a later agent would otherwise re-read the paper for. Report faithfully here; evaluate in Critical discussion. No fake precision.
- Learnings: reusable mechanisms or surprises, in the style of [STYLE.md](STYLE.md). `None.` if nothing transfers.
- Verification: what the paper actually says about checking claims, steps, traces, citations, or rewards. Central or satellite. `None.` if silent. See [VERIFICATION.md](VERIFICATION.md).
- Field context: neutrally place the paper in space and time. What line of work precedes it? What does it change? Which already-reviewed papers does it support, challenge, or extend? Separate the authors' positioning from your inference. `None.` only when the extract gives no defensible context.
- Critical discussion: scrutinize the paper and the claims it makes. We are doing science, not repeating a pitch. Ask whether the evidence supports the central claim, the comparison is fair, the evaluation measures the stated capability, and the result generalizes as far as claimed. Note weak baselines, missing controls, circular or same-family judging, contamination, unmeasured coverage, and mechanisms that do not follow from the result when they are present. Ground objections in a specific setup, result, table, reported comparison, or omission available in the text. Distinguish a demonstrated error from a limitation or an experiment that remains to be run. Missing evidence narrows a claim; it does not by itself prove the claim false. Do not invent faults to sound critical, but do not soften real ones. End with what remains supported after the caveats.
- Relevance to us: only if CONTEXT / TAXONOMY / VERIFICATION actually fire, explain what the paper changes, supports, or challenges for us. Name a bet only when it helps the reasoning. New bets or arcs are allowed; do not silently map them onto the nearest existing id. Write `None.` when the paper has no meaningful relevance.
- Claims: lemmalog edges (the paper's stated relations, not your verdict). See [CLAIMS.md](CLAIMS.md). `None.` if empty. Keep this machine-readable table last so it does not interrupt the review.

Voice: [STYLE.md](STYLE.md).

### 3. Write files and memory

1. Save `reviews/{id}.md` using [SCHEMA.md](SCHEMA.md).
2. Run `uv run .agents/skills/paper-review/scripts/validate_review.py reviews/{id}.md` and fix every error.
3. Update `papers/index.md` to `reviewed`.
4. If lemmalog MCP/`lemmalog-cli` exists, assert only the paper's `reviewed_in[1.0]` pointer and non-empty Claims ([`lemmalog/SCHEMA.md`](../../../lemmalog/SCHEMA.md)). Structural provenance is `[1.0]`; only the scientific relation carries the Claims-table confidence. If tools are missing, say so once. Empty Claims skip claim edges, not the review pointer. All other metadata stays in the review.

## Output template

Use the complete schema-v1 frontmatter from [SCHEMA.md](SCHEMA.md), followed by:

```
Citation: Author(s). Title. Venue, Year. URL

## What this paper is about

[Short. A physicist or CS colleague should get it without decoding slang.]

## Extended summary

[Methods, setups, headline numbers, and the authors' caveats. Reserve your evaluation for Critical discussion.]

## Learnings

[None.  or a few short paragraphs, one finding each]

## Verification

[None.  or what they check, how, coverage/precision, who judges]

## Field context

[Neutral field position, timeline, and connections to reviewed work]

## Critical discussion

[Does the evidence support the claims? Name weak baselines, overclaims, circular evaluation, and missing controls when present. State what remains supported.]

## Relevance to us

[None.  or what this changes, supports, or challenges for us]

## Claims

[Table per CLAIMS.md, or: None.]
```
