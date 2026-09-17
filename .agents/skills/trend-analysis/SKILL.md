---
name: trend-analysis
description: Produces dated competitive research landscape reports from review metadata, critical assessments, and cross-paper evidence. Use when asked what is changing in the field, what competitors or institutions are doing, where investment is accumulating, or where strategic niches remain.
disable-model-invocation: true
---

# Trend Analysis

Write a new snapshot to `trends/YYYY-MM-DD-<period-or-topic>.md`. Do not overwrite an older report. If the same date and slug already exist, add a version suffix.

Audience: product, go-to-market, research leads, and C-level readers. The report should be coherent and decision-useful, but "authoritative" means well-supported, not falsely certain.

## Source boundary

Allowed:

- schema-v1 `reviews/*.md` ([review contract](../paper-review/SCHEMA.md))
- `papers/index.md` for corpus and review-coverage counts
- lemmalog facts, aggregates, and `why` trees
- `reviews/graphify-out/` for candidate clusters
- earlier `trends/*.md` for deltas
- earlier `perspectives/*.md` as hypotheses, never as primary evidence

Never open `papers/canonical`, `papers/raw`, or the full-paper graph. Missing evidence becomes a Review gap for `paper-review`.

## Discipline

- Use `publication.first_public_date` for research timing. Use `reviewed_at` for pipeline coverage. Do not mistake dump date for publication date.
- Distinguish author affiliation, funding, donated compute/data, paid services, and collaboration. Do not translate all corporate mentions into sponsorship.
- The corpus is selected, not a representative sample of the literature. Paper counts describe this corpus unless an external denominator is present in a review.
- "Emerging", "growing", or "fading" requires at least two time windows and multiple reviewed papers. One paper is a signal, not a trend.
- Separate observation, interpretation, and recommendation. A repeated claim can still be repeatedly wrong.
- Aggregate critical flags only after reading their supporting Critical discussion.
- Do not require several papers before mentioning a scientific result. Label one-source results as reported or supported; use corroborated only for meaningfully independent evidence. Publication venue is context, not a correctness score.
- Read publication dates, titles, organizations, and funding from review frontmatter, not lemmalog.

## Workflow

1. Define the period/topic and locate the closest prior trend snapshot.
2. Report indexed, reviewed, in-period, and metadata-complete counts.
3. Aggregate publication dates, organizations/roles, facets, artifacts, Claims, Field context, and critical flags.
4. Compare with the prior window. Look for new entrants, repeated methods, releases, funding/compute patterns, benchmark movement, missing-baseline patterns, and topics with little credible work.
5. Use the reviews graph for candidate clusters and lemmalog for supported relationships. Label graph-derived cluster names as inferred.
6. Test the strongest competitive narrative against contrary reviews.
7. Write implications and niches separately from observations.

Use exact `lemmalog_query` calls for relations/aggregates and `lemmalog_why` for provenance. `lemmalog_context` is candidate discovery only. Never consume `store.snapshot` or an unfiltered `lemmalog_dump`.

## Output

```markdown
---
synthesis_schema_version: 1
type: competitive-research-landscape
title: "..."
generated_at: "YYYY-MM-DD"
period_start: "YYYY-MM-DD"
period_end: "YYYY-MM-DD"
source_reviews: []
previous_snapshot: null
coverage:
  indexed_papers: 0
  reviewed_papers: 0
  in_period_reviews: 0
  metadata_complete: 0
---

# Title

## Executive view
[The few changes decision-makers need to understand.]

## Scope and coverage
[Corpus selection, date basis, and what cannot be inferred.]

## Where activity is accumulating
[Methods, systems, institutions, support, and artifacts over time.]

## Competitive positions
[Who is doing what, with explicit organization roles and evidence.]

## Claims under pressure
[Repeated weak baselines, overclaims, verifier gaps, or contrary evidence.]

## Open niches
[Observed whitespace, why it may matter, and alternative explanations for the gap.]

## Implications
[Separate recommendations from factual trend statements.]

## Review gaps
[Missing or incomplete reviews that limit the report.]

## Sources
[Review paths, metadata facts, lemmalog queries/chains, prior snapshot.]
```

Prefer prose and a few compact lists. Use a table only when exact comparison is materially clearer. No press-release language or forced B-number tagging.
