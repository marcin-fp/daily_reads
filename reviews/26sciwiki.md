---
schema_version: 1
paper: slug:26sciwiki
title: "Beyond Retrieval: Compounding Scientific Extelligence with Artificial Intelligence Wikis"
authors:
  - Luiz E. F. C. Lopes
  - Pedro H. M. Zanineli
  - Bruno Focassio
  - Gabriel R. Schleder
publication:
  first_public_date: "2026-05"
  first_public_date_precision: month
  venue: arXiv
  status: preprint
  reviewed_version: null
  reviewed_version_date: null
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-05-06/26sciwiki.md
raw: papers/raw/2026-05-06/26sciwiki-pdf.md
organizations:
  - name: Brazilian Nanotechnology National Laboratory (LNNano/CNPEM)
    sector: government
    roles: [author_affiliation]
    authors: [Luiz E. F. C. Lopes, Pedro H. M. Zanineli, Bruno Focassio, Gabriel R. Schleder]
    grants: []
  - name: Universidade Federal do ABC (UFABC)
    sector: academia
    roles: [author_affiliation]
    authors: [Pedro H. M. Zanineli, Gabriel R. Schleder]
    grants: []
  - name: CNPq (Conselho Nacional de Desenvolvimento Científico e Tecnológico)
    sector: government
    roles: [funder]
    authors: []
    grants: ["422069/2023-0", "313301/2025-5", "371610/2023-0 (INCT Materials Informatics)"]
  - name: FAPESP (Fundação de Amparo à Pesquisa do Estado de São Paulo)
    sector: government
    roles: [funder]
    authors: []
    grants: ["2024/22392-2", "2024/00989-7", "2023/13081-0"]
artifacts:
  - type: code
    url: https://github.com/cnpem/sci-ai-wiki
facets:
  domains: [ai-for-science, knowledge-management, human-computer-interaction]
  paper_type: [position, system]
  methods: [llm-wiki, knowledge-graph, agent-skills, markdown-based-memory]
  models: []
  benchmarks: []
assessment:
  extract_quality: good
  extract_limitations: [figures-not-visually-assessed]
  critical_flags: []
metadata_notes: "No arXiv identifier or explicit venue self-reference appears in the extract; a web search for the title corroborates that this is a preprint dated May 2026 (consistent with the 2026-05-06 dump folder) but did not surface an exact arXiv id or day-level date, so first_public_date uses month precision. No submission venue beyond preprint status could be confirmed."
---

Citation: Luiz E. F. C. Lopes, Pedro H. M. Zanineli, Bruno Focassio, and Gabriel R. Schleder. Beyond Retrieval: Compounding Scientific Extelligence with Artificial Intelligence Wikis. Preprint, 2026.

## What this paper is about

Chatbots and retrieval-augmented systems answer a question well but then throw away everything they figured out in the process. The next session starts from zero, so a researcher who used an LLM to work through a literature question in March has to re-explain the same context in July. This short position paper argues that the real bottleneck in AI-assisted science is not retrieval quality or context-window size but the lack of a persistent, structured memory that survives across sessions. It proposes and releases an architecture, the "SciAI Wiki," in which an LLM-driven agent incrementally builds and maintains an interlinked markdown knowledge base from a researcher's papers, notes, and data, instead of reconstructing context from scratch at every query.

## Extended summary

The argument opens by characterizing current AI-assisted science as "retrieval-centric and session-bound": Retrieval-Augmented Generation (RAG) and similar pipelines retrieve relevant chunks at query time, generate a transient response, and discard the intermediate structure of the interaction, so relationships between a method introduced in one paper and a contradictory result found months later are never preserved as an explicit, evolving object. The paper contrasts two existing agentic approaches from the literature as illustrating the same underlying problem from opposite ends of an autonomy spectrum: Agent Laboratory, a human-in-the-loop research co-pilot, and The AI Scientist, a highly autonomous end-to-end research system whose own reported failure modes include methodological fragility, incorrect implementations, and citation hallucinations (the paper cites The AI Scientist's 2026 Nature publication for this). Both, the authors argue, share a continuity problem rather than a generation problem.

The proposed SciAI Wiki extends an existing "LLM Wiki" paradigm (attributed to a 2026 GitHub gist by Andrej Karpathy) into a research-specific architecture with three layers: (1) immutable raw sources (papers, datasets, lab records, repositories), (2) an LLM-maintained markdown wiki layer of interconnected, type-specific pages (concepts, methods, authors) with explicit cross-links, and (3) a schema layer defining data structures, conventions, and workflows, itself expressed as markdown and editable instruction files (the paper gives AGENTS.md as an example). On top of these layers, three core "skills" operate: Ingestion (turning raw sources into structured, provenance-preserving representations), Query (multi-depth reasoning over the accumulated structure, e.g. connecting a method to a later experimental result), and Maintenance/Lint (auditing the repository for broken links, orphan pages, schema violations, stale claims, and contradictions between ingested papers), plus user-defined task skills such as an automated literature-review-writing skill. The authors frame this as "harness engineering" (citing a 2026 review of memory/skills/protocol externalization in LLM agents) rather than a new model architecture: the innovation is in the externalized, inspectable, model-agnostic protocol and file structure, not in the underlying LLM.

The paper situates this lineage against older external-memory visions (Vannevar Bush's 1945 Memex, the Zettelkasten note-taking method) and the concept of "extelligence" (externalized cultural/cognitive knowledge, Stewart & Cohen 1997), and against a more recent, closely related paradigm the authors call "vibe researching" (a 2026 preprint proposing a "cognitive delegation boundary" where the researcher retains tacit judgment while delegating codifiable tasks). As indirect quantitative support for structured-over-chunk retrieval generally, the paper cites an external benchmark result (not run by these authors) reporting that graph-based, pre-structured retrieval systems outperform chunk-based RAG on multihop reasoning tasks while using fewer retrieved tokens.

Section V ("Limitations and Governance") is the paper's most self-critical section: persistent memory, unlike a stateless chat session, lets errors "accumulate and recursively influence future reasoning" — hallucinated links, unsupported syntheses, or outdated claims can become embedded in the structure itself, a failure mode the authors call "epistemic contamination." They further note that scientific disagreement often reflects differing methodology or instrumentation rather than a simple factual conflict, so a persistent-memory system must track provenance, uncertainty, and versioning, and support human verification, rather than treating everything it accumulates as reliable. The paper concludes that governance (maintenance protocols, structured auditing, verification loops) is as important as retrieval quality for determining whether such a system amplifies understanding or accumulates noise. The paper's code, prompts, schemas, and agent-skill definitions are released at github.com/cnpem/sci-ai-wiki.

## Learnings

Persistent memory reframes error handling from a per-session problem into a compounding one: a stateless chatbot's mistake disappears when the session ends, but the same mistake embedded into a standing markdown knowledge base can be retrieved and built upon indefinitely. The paper's practical implication is that a maintenance/audit loop is not an optional add-on to a memory system but the mechanism that determines whether accumulation helps or actively degrades reliability over time — the audit skill's own error rate becomes as consequential as the ingestion skill's.

The proposed three-layer split (immutable raw sources / LLM-maintained markdown layer / schema-and-convention layer) plus a three-skill loop (ingest, query, maintain) is a concrete, minimal architectural pattern for durable AI memory that is largely orthogonal to which underlying LLM or vector store is used — its distinguishing feature versus GraphRAG-style approaches is writing out durable, human-readable, versionable artifacts rather than reconstructing structure at query time from embeddings alone.

## Verification

The paper names a specific verification-adjacent mechanism — the "Maintenance (Lint)" skill — described as performing continuous "structural and semantic audit": detecting broken links, orphan pages, and schema violations (structural) and stale claims or contradictory assertions between ingested papers (semantic), aiming at "graph coherence and logical consistency." This is architecturally central to the proposal (it is one of the three core skills), but the paper reports no coverage, precision, or false-positive/false-negative rate for this audit process, no worked example of a contradiction it actually caught, and no comparison against a simpler check (e.g., a plain broken-link linter). It is presented as a designed capability of the released system, not as a measured one in this paper.

## Field context

The paper positions itself as extending a specific named precedent, the "LLM Wiki" paradigm from a 2026 Andrej Karpathy GitHub gist, into a research-specific instantiation, and explicitly contrasts itself with two existing agentic-science systems (Agent Laboratory's human-in-the-loop co-pilot design; The AI Scientist's fully autonomous pipeline, now published in Nature per the paper's own citation) by arguing both illustrate a shared continuity gap rather than a generation-quality gap. It draws its retrieval baseline from the RAG literature (Lewis et al. 2020) and GraphRAG (Edge et al., "From local to global"), and situates the broader idea within a decades-old tradition of external cognitive scaffolding (Bush's Memex, Zettelkasten, the "extelligence" concept) and a very recent, closely related "vibe researching" framing (2026) that separates tacit human judgment from delegable, codifiable work. None of these specific cited works — the LLM Wiki gist, Agent Laboratory, The AI Scientist, GraphRAG, the vibe-researching preprint, or the cited knowledge-graph benchmark — are yet reviewed in this corpus, so this field positioning reflects the authors' own account rather than something checked against an independent review here.

## Critical discussion

This is a position and architecture paper, not an empirical one, and it should be read as such: the central diagnostic claim (session-bound retrieval systems force "repetitive cycles of rediscovery") is argued from citation and characterization of other systems' known limitations rather than measured directly, and the proposed SciAI Wiki itself is not evaluated anywhere in the paper — there is no case study of a real multi-month research project run through the released repository, no measurement of whether rediscovery cycles actually shrink, and no comparison of the wiki's outputs against a plain RAG or GraphRAG baseline on any concrete task. The one piece of quantitative evidence offered (graph-based retrieval beating chunk-based RAG on multihop reasoning) is an external benchmark result about knowledge-graph retrieval systems in general, not a measurement of this specific ingestion/query/maintenance architecture, so it supports the general direction (structure beats flat chunks for multihop tasks) without validating the paper's own added design choices.

The paper's own Section V is unusually candid for a proposal of this kind: it names "epistemic contamination" — hallucinated links, unsupported syntheses, or outdated claims becoming permanently embedded and recursively reused — as a first-order risk of exactly the system being proposed, and correctly frames governance and auditing as being as important as retrieval quality. That said, the paper's response to its own risk stays at the level of design requirements (provenance, uncertainty tracking, versioning, human verification, a maintenance/lint skill) rather than demonstrated mitigations; nothing in the text shows the maintenance skill actually catching a real contradiction, nor characterizes how often it would miss one. Given that the paper's central selling point is durability (facts persist and compound across sessions), the absence of any measured error/audit rate is the most consequential gap in the argument, more so than it would be for a paper proposing an ephemeral, per-session tool.

Unlike architecture proposals that pair confident claims with fabricated-looking comparison tables, this paper is careful to hedge appropriately ("we argue," "may," "increasingly") and to release an inspectable, testable implementation rather than only prose, which makes its claims falsifiable in a way a number-free rhetorical pitch would not be. What remains supported after these caveats: the diagnosis of a real, well-documented limitation in current retrieval-centric AI-assisted science (context and intermediate reasoning discarded between sessions) is reasonable and consistent with independently reported failure modes of the two contrasting systems it cites. What is not yet supported is any claim that this specific three-layer, three-skill design measurably reduces rediscovery, reliably catches contradictions, or outperforms simpler alternatives on a concrete research task — those remain proposed capabilities of a released but unevaluated system.

## Relevance to us

This paper is close to a design justification for the pattern this repository already implements: an AGENTS.md-governed markdown memory (canonical papers → reviews as durable summaries → lemmalog as a typed-relation store → graphify as a concept map), with explicit ingestion (paper-review), query (synthesis skills reading reviews and lemmalog), and maintenance (validate_review.py, lemmalog provenance and retraction) roles matching the paper's three-skill split almost exactly. That convergence is worth noting as independent validation of the general pattern (persistent, inspectable, model-agnostic markdown memory beats session-bound retrieval for continuity), directly relevant to B09 (long-lived inspectable research runtime) and B08 (whole-literature reasoning), and to the "wiki as lab notebook vs silent backstage" framing in our own long-lived-sessions arc.

The paper's self-identified "epistemic contamination" risk is also a fair description of exactly the failure mode our own repo rules are built to resist: AGENTS.md's requirement that synthesis skills never reopen full papers and never consume lemmalog's `store.snapshot` or an unfiltered dump as research context, that claims carry graded confidence rather than being treated as uniformly reliable, and that `lemmalog_why` be checked before trusting a derived two-hop chain, are concrete answers to the same problem this paper names only at the requirements level ("must prioritise provenance, uncertainty tracking, versioning, and human verification"). This paper does not itself supply those mechanisms or evidence that they work; it is useful here mainly as confirmation that the general problem and the general shape of a solution are recognized elsewhere, not as evidence about whether any particular governance mechanism (ours or theirs) actually prevents contamination in practice. It says nothing about the physics-specific extensions (family/regime tracking, graded verification, assumption ledgers) that would differentiate a science-general wiki from what B12/B13 would need.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| session-bound retrieval-centric AI systems | repetitive rediscovery of insights | implies | 0.5 | papers/canonical/2026-05-06/26sciwiki.md:L14 | Argued diagnosis from characterization of existing systems, not measured by this paper |
| graph-based pre-structured knowledge retrieval | multihop reasoning performance over chunk-based RAG | improves | 0.4 | papers/canonical/2026-05-06/26sciwiki.md:L126 | Cites an external benchmark result, not the authors' own experiment on this architecture |
| persistent scientific memory without governance | epistemic contamination risk | implies | 0.6 | papers/canonical/2026-05-06/26sciwiki.md:L147 | Errors in a persistent structure can recursively compound rather than disappear between sessions |
| SciAI Wiki ingestion/query/maintenance skills | durable structured scientific knowledge across sessions | implies | 0.4 | papers/canonical/2026-05-06/26sciwiki.md:L136 | Central architecture proposal; released as code but not evaluated in this paper |
