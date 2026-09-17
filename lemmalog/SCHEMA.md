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
| `paper --published_on--> YYYY-MM-DD` | Earliest public date at the precision stored in the review. |
| `paper --date_precision--> day` | `day` \| `month` \| `year` for `published_on`. |
| `paper --venue--> "…"` | Publication venue or `arXiv`. |
| `paper --authored_by--> "Person"` | An author named in the review metadata. |
| `"Person" --affiliated_with--> "Organization"` | Explicit author affiliation. |
| `paper --funded_by--> "Organization"` | Explicit financial support. |
| `paper --compute_provided_by--> "Organization"` | Explicit compute or API support. |
| `paper --data_provided_by--> "Organization"` | Explicit data support. |
| `paper --collaborated_with--> "Organization"` | Explicit institutional collaboration. |
| `paper --grant_id--> "Identifier"` | Grant identifier reported by the paper. |
| `paper --reviewed_in--> reviews/{id}.md` | Schema-v1 review that downstream synthesis may read. |
| `edge --source_paper--> paper` | Which paper asserted this edge. |
| `edge --from--> X` | Subject concept. |
| `edge --to--> Y` | Object concept. |
| `edge --kind--> implies` | `implies` \| `improves` \| `contradicts` \| `uses` \| `evaluates`. |
| `edge --located--> path:anchor` | Full-paper source anchor checked by paper-review. |
| `edge --reviewed_in--> reviews/{id}.md` | Review containing this extracted edge. |
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
published_on --describes--> earliest public date
date_precision --describes--> precision of published_on
venue --describes--> publication venue
authored_by --describes--> paper author
affiliated_with --describes--> explicit author affiliation
funded_by --describes--> explicit funding organization
grant_id --describes--> reported grant identifier
reviewed_in --describes--> schema-v1 review for downstream reading
source_paper --describes--> paper that asserted this edge
from --describes--> edge subject concept
to --describes--> edge object concept
kind --describes--> implies improves contradicts uses evaluates
located --describes--> space-free file anchor
implies --describes--> source supports destination
improves --describes--> source improves destination

arxiv:2606.18195 --title--> "d-OPSD for dLLMs"
arxiv:2606.18195 --year--> 2026
arxiv:2606.18195 --published_on--> 2026-06
arxiv:2606.18195 --date_precision--> month
arxiv:2606.18195 --reviewed_in--> reviews/2606.18195.md
e:2606.18195:suffix-teacher --source_paper--> arxiv:2606.18195
e:2606.18195:suffix-teacher --from--> "d-OPSD suffix teacher"
e:2606.18195:suffix-teacher --to--> "on-policy self distillation"
e:2606.18195:suffix-teacher --kind--> implies
e:2606.18195:suffix-teacher --located--> papers/canonical/2606.18195.md:Abstract
e:2606.18195:suffix-teacher --reviewed_in--> reviews/2606.18195.md
d-OPSD suffix teacher --implies[0.8]--> on-policy self distillation
```

## Derived (rules batch `evidence-chains`)

- `supported_by(X, Y, P)` — some edge from X to Y in paper P.
- `two_hop(X, Z, P1, P2)` — `X -implies-> Y -implies-> Z` with **different** papers P1 ≠ P2.
- `three_hop(X, W, P1, P2, P3)` — same idea, three papers. No unbounded `reaches`: confidence products get noisy.

Same-paper two-hops are omitted on purpose (not the interesting case).

## Discipline

1. Paper-review checks the canonical (or raw fallback) text and writes a schema-v1 review. Assert from that review; other skills do not reopen full papers.
2. Canonicalize names with `alias_of` instead of minting synonyms.
3. After `two_hop`, run `lemmalog_why` and read the linked reviews. Never invent the middle node. If a review does not preserve enough evidence to trust a weak hop, request a paper-review refresh rather than opening canonical or raw text in a synthesis workflow.
4. Wrong facts: `lemmalog_retract`. Changed titles/years: re-assert the same relation.
