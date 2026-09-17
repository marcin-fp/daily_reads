---
name: news-article
description: Produces a dated analytical news article centered on one reviewed paper, placing it in scientific and competitive context rather than repeating its abstract. Use when asked to turn a paper review into a news story for colleagues or a broader technically informed audience.
disable-model-invocation: true
---

# News Article

Write one article to `news/YYYY-MM-DD-<paper-slug>.md`, using the paper's first-public date. Do not overwrite an older article; add a version suffix when revising on the same date.

Audience: technically informed readers who want to know what this paper changes and where it belongs in the field. The voice is that of an informed scientist, not a press office.

## Source boundary

Allowed:

- the schema-v1 review of the central paper ([review contract](../paper-review/SCHEMA.md))
- other schema-v1 reviews for field context
- `papers/index.md` for review status only
- lemmalog claims and `why` trees
- `reviews/graphify-out/` for candidate connections
- earlier news, perspectives, trends, and learnings as leads, not primary evidence

The central paper must be reviewed. Never open `papers/canonical`, `papers/raw`, or the full-paper graph. Do not report a graph connection until reviews or lemmalog support it. If the article needs a fact missing from the review, list the gap and request `paper-review`; do not quietly fill it from the full paper.

## Workflow

1. Read the central review completely, including metadata, Field context, Critical discussion, and Relevance to us.
2. Decide the story before the headline: what changed, what surprising mechanism or tension it exposes, or why the result matters now.
3. Find a small number of related reviewed papers through Claims, lemmalog, or the reviews graph. Verify derived chains with `lemmalog_why`.
4. Reconstruct the timeline from review publication metadata. Do not use dump/review date as the paper's publication date.
5. Write the result and its limits together. Preserve the difference between what the authors showed, what they proposed, and your interpretation.
6. Explain community significance first. Add FirstPrinciples relevance only when it improves the story and can be stated without turning the article into an internal memo.
7. Finish with review-backed sources and any review gaps.

If no reviewed connection exists yet, write a focused article from the central review. Do not invent a lineage to make the piece look more informed.

Use graded evidence language. One paper may report or support a result; independent agreement may corroborate it; well-established requires diverse evidence and no strong unresolved contradiction. Mention peer review when relevant to the story, but do not use venue prestige as a substitute for evaluating the particular claim.

Use exact `lemmalog_query` calls and `lemmalog_why` for relationships. `lemmalog_context` is candidate discovery only. Never consume `store.snapshot` or an unfiltered `lemmalog_dump`.

## Output

```markdown
---
synthesis_schema_version: 1
type: news-article
title: "..."
central_paper: arxiv:YYMM.NNNNN
paper_first_public_date: "YYYY-MM-DD"
generated_at: "YYYY-MM-DD"
source_reviews: [arxiv:YYMM.NNNNN]
lemmalog_queries: []
---

# Informative headline

[One- or two-sentence standfirst: the result and why it matters.]

[A strong lead organized around the scientific issue, not \"A new paper reports...\"]

[What the paper actually did and found, in accessible but precise language.]

[Where it sits in the field and in time, using reviewed connections.]

[What the evidence does not establish and what experiment or observation comes next.]

[What it means to the community and, only if earned, to us.]

## Review gaps
[None. or facts/connections that require a refreshed review.]

## Sources
[Central and related review paths; lemmalog chains used.]
```

Avoid hype ("breakthrough", "revolutionary") unless the evidence and field response justify it. Do not write a section-by-section summary, use em dashes, or lead each paragraph with a bold slogan.
