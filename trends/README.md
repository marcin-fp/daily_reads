# Trends

Competitive research landscape reports for product, go-to-market, research leads, and C-level readers. They describe what is moving, who is doing it, what support and artifacts surround it, and where credible niches remain.

Invoke the `trend-analysis` skill explicitly. It writes:

```text
trends/YYYY-MM-DD-<period-or-topic>.md
```

Reports are immutable snapshots. Add a version suffix rather than overwriting one.

## Inputs

- schema-v1 review metadata and prose
- lemmalog facts/aggregates and `why` trees
- the reviews graph for candidate clusters
- prior trend snapshots for deltas
- prior perspectives as hypotheses, not primary evidence
- `papers/index.md` for corpus/review coverage

Do not read canonical/raw papers or use the full-paper graph. Missing evidence is a review gap for `paper-review`.

## Standard

Use paper first-public dates for research timing and review dates for pipeline coverage. Keep affiliations, grants, donated resources, paid services, and collaborations distinct. Separate observed facts, interpretation, and recommendation.

The corpus is selected rather than statistically representative. Counts describe this corpus unless a reviewed source provides an external denominator. Terms such as "growing" or "fading" require multiple reviewed papers and at least two time windows.
