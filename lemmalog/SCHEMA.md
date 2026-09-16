# Lemmalog schema for papers

Typed claims live here. Graphify is a concept map; it does not store provenance or proof trees.

Install [`rules/evidence-chains.dl`](rules/evidence-chains.dl) once as batch `evidence-chains`. Assert `describes` lines on first use. Query with `lemmalog_query`; trust derived facts only after `lemmalog_why`.

## Entity names

- Papers: `arxiv:2606.18195` (no version). Quote in rules: `"arxiv:2606.18195"`.
- Concepts: ≤8 words, natural language, quoted. Alias variants: `local --alias_of[conf]--> canonical`.
- Edges: `e:{paper-id}:{short}` with no spaces, e.g. `e:2606.18195:dopsd-sample-eff`.
- `located` objects: space-free, `papers/canonical/2606.18195.md:Abstract` or `…md:L42`.

Confidence: verified quotes `[1.0]`; fair paraphrases `[0.7]`–`[0.9]`; interpretive `[0.4]`–`[0.6]`. Untagged defaults to 0.9 and decays down the proof chain.

## Relations

Assert `Relation --describes--> "one-line meaning"` the first time you use a relation.

| Triple | Meaning |
|--------|---------|
| `paper --title--> "…"` | Display title (≤8 words: shorten; full title can live in the review). |
| `paper --year--> YYYY` | Bare year. |
| `edge --source_paper--> paper` | Which paper asserted this edge. |
| `edge --from--> X` | Subject concept. |
| `edge --to--> Y` | Object concept. |
| `edge --kind--> implies` | `implies` \| `improves` \| `contradicts` \| `uses` \| `evaluates`. |
| `edge --located--> path:anchor` | Where to re-read. |
| `X --implies[c]--> Y` | Closable graph for `kind=implies` (same for other kinds as named rels). |
| `X --improves[c]--> Y` | Same pattern. |
| `X --contradicts[c]--> Y` | Same pattern. |
| `X --uses[c]--> Y` | Same pattern. |
| `X --evaluates[c]--> Y` | Same pattern. |
| `local --alias_of[c]--> canonical` | Vocabulary merge. |

Reify **every** closable triple as an `edge` so `supported_by` can name the paper. Do not assert `X --implies--> Y` without a matching edge.

## Example (one paper, two claims)

```text
title --describes--> paper display title
year --describes--> publication year
source_paper --describes--> paper that asserted this edge
from --describes--> edge subject concept
to --describes--> edge object concept
kind --describes--> implies improves contradicts uses evaluates
located --describes--> space-free file anchor
implies --describes--> source supports destination
improves --describes--> source improves destination

arxiv:2606.18195 --title--> "d-OPSD for dLLMs"
arxiv:2606.18195 --year--> 2026
e:2606.18195:suffix-teacher --source_paper--> arxiv:2606.18195
e:2606.18195:suffix-teacher --from--> "d-OPSD suffix teacher"
e:2606.18195:suffix-teacher --to--> "on-policy self distillation"
e:2606.18195:suffix-teacher --kind--> implies
e:2606.18195:suffix-teacher --located--> papers/canonical/2606.18195.md:Abstract
d-OPSD suffix teacher --implies[0.8]--> on-policy self distillation
```

## Derived (rules batch `evidence-chains`)

- `supported_by(X, Y, P)` — some edge from X to Y in paper P.
- `two_hop(X, Z, P1, P2)` — `X -implies-> Y -implies-> Z` with **different** papers P1 ≠ P2.
- `three_hop(X, W, P1, P2, P3)` — same idea, three papers. No unbounded `reaches`: confidence products get noisy.

Same-paper two-hops are omitted on purpose (not the interesting case).

## Discipline

1. Assert only what you checked in canonical (or raw fallback) text.
2. Canonicalize names with `alias_of` instead of minting synonyms.
3. After `two_hop`, run `lemmalog_why`, re-read the weakest `located` anchors, then discuss. Never invent the middle node.
4. Wrong facts: `lemmalog_retract`. Changed titles/years: re-assert the same relation.
