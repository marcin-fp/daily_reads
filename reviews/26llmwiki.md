---
schema_version: 1
paper: slug:26llmwiki
title: "LLM Wiki"
authors:
  - Andrej Karpathy
publication:
  first_public_date: "2026-05"
  first_public_date_precision: month
  venue: "GitHub Gist"
  status: other
  reviewed_version: null
  reviewed_version_date: null
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-05-06/26llmwiki.md
raw: papers/raw/2026-05-06/26llmwiki.md
organizations: []
artifacts: []
facets:
  domains: [knowledge-management, human-computer-interaction]
  paper_type: [position]
  methods: [llm-wiki, markdown-based-memory, agent-skills]
  models: []
  benchmarks: []
assessment:
  extract_quality: good
  extract_limitations: []
  critical_flags: []
metadata_notes: "No author name appears in this document's own text; it is attributed to Andrej Karpathy solely on the strength of an already-reviewed paper in this corpus (reviews/26sciwiki.md, citing 'A. Karpathy, Llm wiki, https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (2026), gitHub Gist, accessed May 2026'), not on external prior knowledge. first_public_date likewise uses that citation's 'accessed May 2026' note as the only available anchor; the gist's own creation date is not stated in the extract. No organizations, funding, or institutional affiliation are named anywhere in the text."
---

Citation: Andrej Karpathy (attributed via citation in reviews/26sciwiki.md). LLM Wiki. GitHub Gist, 2026 (undated in source; cited elsewhere as accessed May 2026).

## What this paper is about

This is not a study; it is a short practitioner's note describing a personal workflow for using an LLM as a knowledge-base maintainer instead of a one-shot question-answering tool. The pitch: rather than uploading documents to a chatbot and letting it re-search them from scratch on every question (plain retrieval-augmented generation), have the LLM read each new source once, extract what matters, and fold it into a standing collection of markdown pages — a wiki — that it alone writes and keeps up to date. The human curates sources and asks questions; the LLM does the summarizing, cross-referencing, and bookkeeping. The document explicitly says it is describing a pattern to be handed to your own coding-agent LLM to instantiate, not a finished, evaluated system.

## Extended summary

The proposed architecture has three layers. Raw sources (articles, papers, images, data files) are immutable — the LLM reads but never edits them. The wiki is a directory of LLM-generated markdown pages (summaries, entity pages, concept pages, comparisons, an overview/synthesis) that the LLM owns entirely; the human reads it, the LLM writes it. The schema is a single configuration document (the author gives CLAUDE.md or AGENTS.md as examples) that tells the LLM how the wiki is organized and what workflows to follow for ingesting, querying, and maintaining it; the author describes this as co-evolving with use rather than being fixed up front.

Three operations are described. Ingest: a new source is dropped in and the LLM reads it, discusses key takeaways with the user, writes or updates a summary page, updates the index, touches related entity/concept pages (the author estimates a single source might touch 10-15 wiki pages), and appends a log entry; the author states a personal preference for ingesting sources one at a time with active supervision, while noting batch ingestion with less oversight is also possible. Query: the user asks a question, the LLM finds and reads relevant pages and synthesizes a cited answer in whatever output form fits (a markdown page, a comparison table, a slide deck, a chart, etc.); the author's stated key idea here is that a good answer should itself be filed back into the wiki as a new page rather than left to disappear in chat history, so that explorations compound the same way ingested sources do. Lint: periodically asking the LLM to health-check the wiki for contradictions between pages, claims made stale by newer sources, orphan pages with no inbound links, concepts mentioned but lacking their own page, missing cross-references, and data gaps that a web search could fill.

Two navigation files are recommended: an index.md that catalogs every wiki page with a one-line summary (read first when answering a query, before drilling into specific pages), and a chronological, append-only log.md recording ingests/queries/lint passes, with a suggested convention of a consistent per-entry prefix (e.g. `## [2026-04-02] ingest | Article Title`) so the log stays greppable with plain Unix tools. The author states, from personal experience, that this index-based navigation "works surprisingly well at moderate scale (~100 sources, ~hundreds of pages)" and can avoid the need for embedding-based RAG infrastructure at that scale; a third-party local search tool (qmd, combining BM25 and vector search with LLM re-ranking) is mentioned as an option once a wiki outgrows that scale. The document draws an explicit historical parallel to Vannevar Bush's 1945 Memex, framing this pattern as finally solving the maintenance-burden problem that made personal associative knowledge stores impractical for humans to sustain by hand. The document closes by stating plainly that it is "intentionally abstract," describes a pattern rather than an implementation, and expects the reader's own LLM agent to work out the specifics for their domain.

## Learnings

Two lightweight, human-readable files — a content-oriented index (one line per page) and a chronological, grep-friendly log — are proposed as sufficient navigation for an LLM-maintained knowledge base at "moderate scale" (on the order of 100 sources, hundreds of pages), without embedding-based retrieval. This is a concrete, checkable claim about where plain structured markdown can substitute for vector search, with an explicit (if informal) scale boundary attached, rather than a universal claim.

The proposed mechanism for how such a wiki actually grows richer over time is specific: not just "the LLM remembers things," but "a good answer to an ad hoc query gets filed back into the wiki as a new page," so that one-off analyses and comparisons become durable, citable artifacts instead of disappearing into chat history. This is a transferable design principle distinct from the general idea of persistent memory — it names the exact conversion step (query output to standing page) that makes the compounding actually happen.

## Verification

The document names a "Lint" operation as its verification-adjacent mechanism: periodically asking the LLM to check the wiki for contradictions between pages, claims made stale by newer sources, orphan pages, missing cross-references for mentioned-but-unlinked concepts, and data gaps. This is described only as a recommended practice, with no reported precision, coverage, or example of a caught error; the document does not discuss what happens when the lint pass itself is wrong (a false contradiction flag, a missed stale claim), nor any risk of errors compounding in the wiki over time. There is no other check, judge, or verification content in the document — sourcing, synthesis, and page-writing are all performed by the same LLM with no described independent check on any of it.

## Field context

This document is the direct precedent for the "LLM Wiki paradigm" that an already-reviewed paper in this corpus, [26sciwiki](26sciwiki.md) ("Beyond Retrieval: Compounding Scientific Extelligence with Artificial Intelligence Wikis"), explicitly cites and extends into a research-specific architecture (adding knowledge-graph framing, a formal three-layer/three-skill structure, and a discussion of governance and "epistemic contamination" risk that this original document does not raise at all). Both documents share the same core three-layer structure (immutable raw sources / LLM-maintained markdown layer / a schema or convention file) and the same operation names (this document's "Lint" becomes 26sciwiki's "Maintenance (Lint)"), which is a direct, verifiable lineage rather than a coincidental convergence, since 26sciwiki names this exact source. This document itself frames its own lineage as extending Vannevar Bush's 1945 Memex concept of a personally curated, associatively linked knowledge store, with the claim that the previously unsolved problem (who maintains the associative structure) is now addressed by having an LLM do the bookkeeping.

## Critical discussion

This is a personal-practice note, not a study, and it should be read as one: every claim about the pattern's benefits ("works surprisingly well," "the wiki stays maintained because the cost of maintenance is near zero," "LLMs don't get bored, don't forget to update a cross-reference") is presented as the author's first-person experience, with no comparison against plain RAG, no user study, no measurement of how often the wiki actually stays consistent as it grows, and no worked example of the Lint operation catching a real contradiction. That is a reasonable thing for a short idea-sharing gist to be — the document says outright that it is "intentionally abstract" and not an implementation — but it means none of its central claims should be read as validated, only as a plausible, specifically-described hypothesis about what might work.

The most consequential unaddressed risk is exactly the one the downstream 26sciwiki paper later named explicitly: errors, once written into a persistent wiki page, do not necessarily disappear the way a mistake in a single chat response would, and can be built upon by later ingests or queries. This document's confident framing ("LLMs don't get bored, don't forget to update a cross-reference") asserts reliability without engaging the possibility of the LLM confidently writing something wrong into a page and that error persisting or compounding — a gap that the paper it directly inspired felt was important enough to devote an entire section to. This is not a demonstrated failure of the pattern; it is an absence of any discussion of the failure mode in the document that proposes the pattern, which matters because the pattern's central selling point is durability across time.

The scale claim ("works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure") is stated as a specific, in-principle testable threshold, but no data or benchmark accompanies it; it is offered as personal experience rather than as a measured boundary, and the document does not say what breaks or how gracefully performance degrades past that scale, only gesturing at a third-party search tool as an eventual fallback.

What remains useful after these caveats: the architectural pattern itself (immutable sources, an LLM-owned markdown layer, a schema file, and named ingest/query/lint operations) is concretely specified enough to build and test, and the specific mechanism proposed for compounding value (filing good query answers back into the wiki as durable pages) is a clear, actionable design choice rather than a vague aspiration. Whether the pattern actually delivers the claimed low-maintenance-cost persistence, and how it behaves as errors accumulate or scale grows, remains untested by this document and is left entirely to the reader's own experience.

## Relevance to us

This document is the traceable origin of a pattern this repository itself already implements: an index.md-based catalog, a schema file (AGENTS.md) governing conventions, and immutable raw sources feeding an LLM-maintained layer of durable markdown (canonical papers, reviews, and lemmalog together playing the role this document assigns to "the wiki"). That is worth noting plainly now that both this document and its direct descendant ([26sciwiki](26sciwiki.md)) are in the corpus: the convergence noted in that earlier review is not an independent rediscovery of the same idea but a documented lineage from this exact source. As with that review, the useful takeaway here is not evidence that the pattern works — this document supplies none — but confirmation that the general shape of the problem (session-bound retrieval loses accumulated structure) and this specific shape of a solution (immutable sources, LLM-owned markdown, index plus log, periodic lint) are recognized and reused elsewhere, which is a weak but real form of face validity for the design choices this repo already makes, most concretely the choice to keep lemmalog's provenance and confidence grading (our own answer to the "who catches the LLM's mistake in the wiki" question this document leaves open) rather than trusting an unaudited accumulation of LLM-written pages.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| persistent LLM-maintained wiki | cross-document synthesis without re-derivation | improves | 0.3 | papers/canonical/2026-05-06/26llmwiki.md:L5 | Personal-experience claim contrasted with plain RAG; no comparison or measurement reported |
| index and log navigation files | need for embedding-based RAG at moderate scale | contradicts | 0.3 | papers/canonical/2026-05-06/26llmwiki.md:L21 | Author reports structured navigation (index.md, log.md) suffices at ~100 sources / hundreds of pages, without a benchmark |
| periodic LLM lint pass | wiki contradiction and staleness detection | implies | 0.25 | papers/canonical/2026-05-06/26llmwiki.md:L18 | Proposed maintenance mechanism; no reported precision, coverage, or worked example |
