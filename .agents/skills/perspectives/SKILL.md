---
name: perspectives
description: Produces dated, evidence-backed perspective essays from paper reviews and lemmalog chains for internal researchers. Use when asked to develop or update a perspective, tension, research arc, or argued view of the field.
disable-model-invocation: true
---

# Perspectives

Write a new snapshot to `perspectives/YYYY-MM-DD-<topic-slug>.md`. Do not overwrite an older perspective. If the same date and slug already exist, add `-v2`, `-v3`, and so on.

Audience: fellow researchers. A perspective is an argued, provisional view meant to provoke better scientific and strategic discussion. It is not a competitive-intelligence briefing and not a list of papers.

## Source boundary

Allowed:

- schema-v1 `reviews/*.md` ([review contract](../paper-review/SCHEMA.md))
- `papers/index.md` for coverage/status counts only
- lemmalog queries and `why` trees
- `reviews/graphify-out/` when it exists, for candidate connections
- earlier `perspectives/*.md`, as prior views to test rather than evidence

Never open `papers/canonical`, `papers/raw`, or `papers/canonical/graphify-out`. Graphify suggests connections; reviews and lemmalog support them. If a required fact is absent from a review, list the paper under Review gaps and request a `paper-review` refresh. Do not silently recover the fact from the full paper.

## Workflow

1. Define one question, tension, or thesis. Do not attempt a perspective on the whole field at once.
2. Read the latest perspective on that topic, if one exists. Extract what it claimed and what evidence would change it.
3. Count total and reviewed papers in scope. Select reviews by publication date, facets, Claims, Field context, and Critical discussion.
4. Query lemmalog for direct support, contradiction, and two/three-hop candidates. Run `lemmalog_why` before using a derived chain. If lemmalog is unavailable, use direct review-backed comparisons only and say so.
5. Use the reviews graph only to find candidates you did not think to query. A graph node or path is never evidence by itself.
6. Draft an argument, not a catalog. Represent the strongest counterevidence and distinguish paper results, reviewer assessments, and your synthesis.
7. State what changed from the previous snapshot, what remains unresolved, and which observations would reverse the view.
8. Write the source manifest and review gaps.

With fewer than five relevant reviews, label the result `exploratory` in frontmatter and avoid field-wide conclusions.

There is no minimum source count for using evidence. Mark a single source as reported or supported; reserve corroborated for meaningfully independent sources, well-established for diverse evidence without a strong unresolved contradiction, and contested for credible conflict. Shared authors, datasets, model families, or judges reduce independence. Peer review informs the assessment but never substitutes for examining the claim.

Use exact `lemmalog_query` calls and `lemmalog_why` for conclusions. `lemmalog_context` is candidate discovery only. Never consume `store.snapshot` or an unfiltered `lemmalog_dump`.

## Output

```markdown
---
synthesis_schema_version: 1
type: perspective
title: "..."
status: exploratory | developed
generated_at: "YYYY-MM-DD"
review_cutoff: "YYYY-MM-DD"
source_reviews: [arxiv:YYMM.NNNNN]
previous_snapshot: null
lemmalog_queries: []
coverage:
  indexed_papers: 0
  reviewed_papers: 0
  relevant_reviews: 0
---

# Title

## Thesis
[The position in a few clear paragraphs.]

## What changed
[How new evidence changed, strengthened, or weakened the prior view.]

## Evidence and counterevidence
[Cross-paper argument. Cite review paths/paper ids; derived chains require why.]

## Tensions and objections
[The strongest alternative reading and what it explains better.]

## Implications
[Research/product implications only to the extent supported.]

## Open questions
[What evidence would decide the remaining uncertainty.]

## Review gaps
[None. or paper ids whose reviews need more evidence.]

## Sources
[Review paths and lemmalog claims/chains actually used.]
```

Write in the same scientific, accessible voice as the reviews. Do not use em dashes, hype, or bold-led bullet lists.
