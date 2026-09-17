# Review schema (version 1)

The review is the durable interface between a full paper and every later synthesis. Downstream skills read the review, not the canonical or raw paper. Keep the review compact enough to scan, but preserve the facts that would otherwise require reopening the source.

## Frontmatter

Use this shape. Quote every date so YAML does not convert it into a language-specific date object.

```yaml
---
schema_version: 1
paper: arxiv:YYMM.NNNNN
title: "Full title"
authors:
  - Full Name
publication:
  first_public_date: "YYYY-MM-DD"
  first_public_date_precision: day
  venue: arXiv
  status: preprint
  reviewed_version: v1
  reviewed_version_date: "YYYY-MM-DD"
reviewed_at: "YYYY-MM-DD"
canonical: papers/canonical/YYYY-MM-DD/YYMM.NNNNN.md
raw: papers/raw/YYYY-MM-DD/...
source_url: https://...
organizations:
  - name: Example University
    sector: academia
    roles: [author_affiliation]
    authors: [Full Name]
    grants: []
artifacts:
  - type: code
    url: https://...
facets:
  domains: [machine-learning]
  paper_type: [analysis]
  methods: [corpus-analysis]
  models: [Model Name]
  benchmarks: []
assessment:
  extract_quality: good
  extract_limitations: [figures-not-visually-assessed]
  critical_flags: []
metadata_notes: "Funding was not reported in the available text."
---
```

Required keys are `schema_version`, `paper`, `title`, `authors`, `publication`, `reviewed_at`, `canonical`, `raw`, `organizations`, `artifacts`, `facets`, and `assessment`. `source_url` and `metadata_notes` are optional.

### Dates

`first_public_date` is the earliest public date you can establish, normally the initial arXiv submission date or online publication date. `reviewed_version_date` is the date of the exact version reviewed when available. Use `day`, `month`, or `year` precision and preserve a partial value (`"2026-05"` or `"2026"`) instead of inventing a day. A dump date is already encoded in the canonical/raw paths; it is not a publication date.

For arXiv, use the source landing page or API metadata. For other papers, prefer the publisher's online-publication date. Record received and accepted dates only in `metadata_notes` when they help reconstruct a timeline.

### Organizations and support

Create one entry per explicitly named organization. `roles` may contain:

- `author_affiliation`
- `funder`
- `compute_provider`
- `data_provider`
- `collaborator`

`sector` is `academia`, `industry`, `government`, `nonprofit`, `other`, or `unknown`. Add the affected authors and grant identifiers when the paper states them. An industry affiliation, a grant, donated compute, and use of a commercial API are different relationships; record the correct role instead of collapsing them into a generic "company tie."

Do not infer affiliations or support from author names, email domains, prior knowledge, or citations. An empty funding role means "not reported or not recoverable," not "the work had no funding." Explain important uncertainty in `metadata_notes`.

### Artifacts

Artifact `type` is `code`, `data`, `model`, `benchmark`, `project`, or `other`. Include only artifacts produced or officially released by this work, not every dataset or model it used.

### Facets

Facets make later aggregation possible without turning the review into a taxonomy exercise.

- `domains`: broad scientific or technical areas.
- `paper_type`: one or more of `method`, `system`, `benchmark`, `analysis`, `theory`, `experiment`, `survey`, `position`, `case-study`, `dataset`, or `other`.
- `methods`: a few reusable method names.
- `models`: models evaluated, trained, or otherwise central to the work.
- `benchmarks`: benchmarks or evaluation datasets central to the results.

Use short, stable names and reuse names already present in reviews. Empty lists are correct. Do not tag every concept mentioned in related work.

### Assessment

`extract_quality` is `good`, `partial`, or `poor`. `extract_limitations` may include `figures-not-visually-assessed`, `figure-text-missing`, `table-extraction-damaged`, `equations-damaged`, `raw-fallback`, and a short free-form value when needed.

`critical_flags` are aggregation aids backed by the Critical discussion, not standalone verdicts. Allowed values:

- `weak-baseline`
- `missing-control`
- `same-family-judge`
- `circular-evaluation`
- `contamination-risk`
- `narrow-evaluation`
- `overclaim`
- `missing-uncertainty`
- `incomplete-reporting`

Use an empty list when none is earned. A missing experiment usually narrows a claim; it does not prove the claim false.

## Section order

Keep every heading in this order:

1. `## What this paper is about`
2. `## Extended summary`
3. `## Learnings`
4. `## Verification`
5. `## Field context`
6. `## Critical discussion`
7. `## Relevance to us`
8. `## Claims`

`Citation:` appears before the first heading. Learnings, Verification, Field context, Relevance to us, and Claims may contain `None.` Critical discussion is required when the paper extract is usable. Claims remains last and contains only relations asserted by the paper.

## Boundary between sections

- Extended summary reports methods, results, and author-stated caveats.
- Learnings contains short reusable findings, not a second summary.
- Verification records what the paper checks and how.
- Field context places the work neutrally in the research landscape: what preceded it, what it changes, and which reviewed work it connects to. Separate author positioning from reviewer inference.
- Critical discussion assesses whether the evidence supports the claims.
- Relevance to us applies the internal FirstPrinciples lens and may be `None.`
- Claims is the machine-readable paper-claim table.
