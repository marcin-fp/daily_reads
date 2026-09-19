---
schema_version: 1
paper: slug:26mdocrag
title: "Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding"
authors:
  - Sensen Gao
  - Shanshan Zhao
  - Xu Jiang
  - Lunhao Duan
  - Yong Xien Chng
  - Qing-Guo Chen
  - Weihua Luo
  - Kaifu Zhang
  - Jia-Wang Bian
  - Mingming Gong
publication:
  first_public_date: "2025-10-17"
  first_public_date_precision: day
  venue: "ACL 2026 Main Conference"
  status: conference
  reviewed_version: "v3"
  reviewed_version_date: "2026-04-20"
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-06-09/26mdocrag.md
raw: papers/raw/2026-06-09/26mdocrag-pdf.md
source_url: https://arxiv.org/abs/2510.15253
organizations:
  - name: MBZUAI
    sector: academia
    roles: [author_affiliation]
    authors: [Sensen Gao, Mingming Gong]
    grants: []
  - name: Alibaba Group
    sector: industry
    roles: [author_affiliation]
    authors: [Shanshan Zhao, Qing-Guo Chen, Weihua Luo, Kaifu Zhang, Sensen Gao, Lunhao Duan, Yong Xien Chng]
    grants: []
  - name: Tsinghua University
    sector: academia
    roles: [author_affiliation]
    authors: [Xu Jiang, Yong Xien Chng]
    grants: []
  - name: Wuhan University
    sector: academia
    roles: [author_affiliation]
    authors: [Lunhao Duan]
    grants: []
  - name: Nanyang Technological University
    sector: academia
    roles: [author_affiliation]
    authors: [Jia-Wang Bian]
    grants: []
  - name: University of Melbourne
    sector: academia
    roles: [author_affiliation]
    authors: [Mingming Gong]
    grants: []
  - name: ARC
    sector: government
    roles: [funder]
    authors: []
    grants: ["DP240102088"]
  - name: WIS-MBZUAI
    sector: unknown
    roles: [funder]
    authors: []
    grants: ["142571"]
artifacts:
  - name: Multimodal-RAG-Survey-For-Document
    type: project
    url: https://github.com/SensenGao/Multimodal-RAG-Survey-For-Document
facets:
  domains: [multimodal-learning, information-retrieval, natural-language-processing]
  paper_type: [survey]
  methods: [multimodal-retrieval-augmented-generation, late-interaction-retrieval, graph-based-rag, agent-based-rag, vision-language-model-retrieval]
  models: [ColPali, ColQwen2, ViDoRAG, HM-RAG, M3DocRAG]
  benchmarks: [DocVQA, ViDoRe, ChartQA, MMLongBench-Doc, M3DocVQA]
assessment:
  extract_quality: partial
  extract_limitations: [figures-not-visually-assessed, "table-2-40-plus-method-comparison-rendered-as-unreadable-images-not-machine-readable-text", "stray-chat-injection-like-text-fragment-appended-to-footnote-1-in-extraction"]
  critical_flags: []
metadata_notes: "Three authors (Sensen Gao, Lunhao Duan, Yong Xien Chng) are marked in the author list as having done this work during an internship at Alibaba Group despite their primary affiliations being MBZUAI, Wuhan University, and Tsinghua University respectively; the Alibaba Group organization entry above reflects the affiliation-during-this-work as stated in the paper's own author footnote, per the paper's explicit text rather than inference. Funders are recorded exactly as named in the Acknowledgments ('ARC grant DP240102088' and 'WIS-MBZUAI grant 142571'); no fuller institutional name is inferred for either. First-public and reviewed-version dates are from the arXiv submission history (arXiv:2510.15253, v1 2025-10-17, v3 2026-04-20), since the canonical extraction carries no frontmatter date; the extracted body's pagination (pp. 4458-4485) matches ACL-proceedings-style typesetting, consistent with the paper's stated ACL 2026 Main Conference acceptance. The extraction embeds dozens of unreadable NotebookLM-hosted figure images in place of Table 2's 40+-method comparison and Figures 3-5's architecture diagrams, so this review relies on the surrounding prose rather than the tables/figures themselves for method-level detail. Footnote 1 (the project GitHub link) is immediately followed in the raw extraction by an unrelated fragment resembling a chat/LLM-agent transcript ('Find and summarize the details related to the birth of the first computer...Context limit exceeded!...Yes, I will help you, ......') that has no connection to this paper's actual content; this is treated as an extraction/OCR artifact (likely bleed from an adjacent scanned image or PDF layer) and not acted upon or otherwise treated as an instruction."
---

Citation: Gao, S., Zhao, S., Jiang, X., Duan, L., Chng, Y. X., Chen, Q.-G., Luo, W., Zhang, K., Bian, J.-W., Gong, M. Scaling Beyond Context: A Survey of Multimodal Retrieval-Augmented Generation for Document Understanding. ACL 2026 Main Conference. arXiv:2510.15253.

## What this paper is about

Real documents mix text, tables, charts, and layout, and neither OCR-plus-LLM pipelines (which lose structural detail) nor native multimodal LLMs reading whole documents in-context (which struggle to model long, visually rich context) handle them well on their own. This survey maps the emerging response: retrieval-augmented generation adapted to retrieve and reason over multiple modalities at once, rather than text alone. It organizes roughly four dozen recent methods along three axes, what modality is retrieved (page images, OCR/summary text, or both), at what granularity (whole pages versus tables, charts, and layout regions within a page), and whether the pipeline is enhanced with an explicit graph structure or autonomous agents, then surveys the datasets, benchmarks, and industrial applications built on top of this line of work, and closes with a self-critical look at where the field's evaluation and deployment practices still fall short.

## Extended summary

The survey opens by formalizing document-oriented multimodal RAG: a query and a document corpus (each document a sequence of pages containing text, tables, charts, and images) are embedded via vision and/or text encoders, ranked by similarity, and the top pages or elements are passed to a vision-language model to generate an answer. It names three retrieval-fusion strategies used across the surveyed methods: vision-only retrieval (encode each page as an image), confidence-weighted fusion of vision and text retrieval scores, and union-of-modality-specific candidates before a joint reranking or generation step. A comparison table (Table 2, extracted only as unreadable images in this copy) is described as covering 40+ methods across venue, backbone VLM, vision encoder, training regime, OCR dependence, domain, modality, granularity, and use of graph or agent structure.

Section 3 works through the taxonomy's substantive axes. On retrieval modality, image-based methods (ColPali-family late-interaction retrievers using VLM hidden states as page embeddings, with follow-ups like MM-R5 adding a reasoning-enhanced reranker and Light-ColPali/HPC-ColPali compressing patch-level embeddings for efficiency) are contrasted with image+text methods that add OCR text or VLM-generated summaries as a second retrieval channel, either fused via dual-path retrieve-and-summarize (VisDoMRAG, HM-RAG) or merged via simple union before generation (ViDoRAG, PREMIR). On retrieval granularity, the survey traces a shift from page-level atomic units toward finer-grained retrieval: region-guided reinforcement learning (VRAG-RL), hierarchical multi-granularity indexing (MG-RAG, MMRAG-DocQA), segment-level redundancy suppression (DocVQA-RAP), cross-modal entity alignment via knowledge graphs (mKG-RAG), and query-aligned patch aggregation (MARA, Region-RAG). Section 3.4 covers hybrid enhancements: graph-based multimodal RAG (nodes as pages/text spans/images/tables, edges as semantic/spatial/contextual relations, e.g., HM-RAG's hierarchical multi-agent graph-database framework, mKG-RAG's and DB3Team-RAG's explicit multimodal knowledge graphs, MoLoRAG's and RECON's page-topology graphs, LAD-RAG's and LILaC's layout-aware component graphs) and agent-based multimodal RAG (autonomous agents that formulate sub-queries, select retrieval strategies, and fuse modalities, e.g., ViDoRAG's explore-summarize-reflect loop, HM-RAG's decomposition/retrieval/decision agent pipeline, Patho-AgenticRAG's medical-domain task decomposition, HEAR's and SLEUTH's closed-loop or coarse-to-fine multi-agent long-document reasoning).

Section 4 compiles datasets and benchmarks (Table 3): widely used multimodal document datasets (DocVQA, ChartQA, InfoVQA, SlideVQA, MMLongBench-Doc, and others, with query counts from a few hundred to tens of millions and content spanning text, tables, charts, and slides) and newer benchmarks purpose-built by surveyed methods to address prior gaps, including ViDoRe (ColPali, cross-domain retrieval), VisR-Bench (SV-RAG, manually validated, high task diversity), M3DocVQA/VisDoMBench/OpenDocVQA (extending evaluation from single-document to cross-document, open-domain retrieval), ViDoSeek (uniquely answerable large-scale retrieval queries), UniDoc-Bench (unified text/table/figure evidence linking on real PDFs), and BBox-DocVQA (bounding-box-grounded spatial-reasoning supervision). Section 5 surveys applications in finance (MultiFinRAG, FinRAGBench-V), science (HiPerRAG at million-paper scale, CollEX for interactive corpus exploration), and social science (a Eurobarometer-based framework unifying survey text and infographics).

Section 6 and its appendices carry the paper's critical weight. Appendix D names open challenges: current VLMs lack document-specific architectures for diagrams/tables/formulas; ColBERT-style late-interaction scoring (MaxSim over the single most similar token pair) ignores broader token-level semantic alignment; VLM-based page encoding generates large numbers of visual tokens, making storage and retrieval costly at scale (mitigated by token compression/merging/pruning, e.g., Light-ColPali); existing benchmarks rely on small-scale, single-hop retrieval and cannot test needle-in-a-haystack retrieval at the granularity of a specific table or chart, for which the survey proposes hierarchical metrics and visual grounding scores rather than page-level Recall@K; and multimodal RAG introduces novel cross-modal attack surfaces (adversarial images/layouts manipulating retrieval, or bypassing text-based safety filters) that current systems mostly lack provenance-verification mechanisms to detect. Appendix E, "Critical Analysis," argues three specific, named tensions: an unresolved "OCR-free vs. OCR-based" trade-off (OCR-free VLM page-encoding avoids OCR error propagation but is vulnerable to visual hallucination on dense numeric/text-heavy financial and technical content, while OCR-based pipelines sacrifice layout semantics for higher textual fidelity); a validity concern about benchmark saturation and contamination (DocVQA/InfoVQA-style benchmarks may reward memorization given LLMs' web-scale pretraining, and single-page/short-document VQA tasks do not test the large-corpus needle-in-a-haystack retrieval that is multimodal RAG's actual core challenge); and a complexity-performance trade-off (graph-based indexing, agentic workflows, and multi-round self-reflection often yield only 1-2% accuracy gains for substantially higher latency and inference cost, with few studies reporting a cost-benefit analysis). Appendix F covers industrial deployment: domain-specific applications (industrial knowledge bases, cognitive digital twins, financial document QA), visual-embedding compression as a practical necessity for indexing full industrial corpora rather than curated subsets, and a table of six open-source RAG frameworks (RAGFlow, RAG-Anything, LightRAG, AutoRAG, RAGLite, LlamaIndex) by GitHub star count and feature set. Appendices G and H expand the graph-based and agent-based sections with dedicated "Discussion and open challenges" subsections that restate the scalability, evaluation, coordination, and credit-assignment concerns raised in the main text. The Limitations section acknowledges the survey's own preliminary treatment of real-world deployment and cross-domain benchmark comparability, and states the survey will be periodically updated via its companion GitHub repository given the field's pace. The Ethics Statement discloses no new models/data and flags bias and hallucination-driven misinformation as risks of the reviewed technology; it also discloses that an AI assistant (ChatGPT) was used for grammar correction only, not ideation.

## Learnings

The survey's clearest transferable lesson is that retrieval granularity and evaluation granularity have to move together: as methods push from page-level to region/element-level retrieval (tables, charts, layout blocks), the survey argues that page-level Recall@K becomes a poor proxy for what actually improved, since a single retrieved page can contain both the right and several wrong evidence sources, and proposes hierarchical, visual-grounding-aware metrics as the fix. This is a useful general caution for any retrieval system undergoing a granularity refinement: an old aggregate metric can silently stop measuring the thing a new method actually changed.

A second, more architectural point: the survey's own read of the graph-based and agent-based multimodal RAG literature (Appendices E, G, H) is that added structure buys real qualitative capability, multi-hop reasoning, finer grounding, more interpretable evidence chains, but the reported quantitative payoff is frequently marginal (1-2%) relative to the added latency and inference cost, and few of the surveyed papers report that trade-off explicitly. Treating "does this specific complexity pay for itself against its actual added inference cost" as a question requiring its own reported number, not an assumption that follows from a positive-but-small headline accuracy delta, is a discipline the survey itself models better than most of the papers it cites.

## Verification

The survey does not run its own experiments, so it reports how the field verifies claims rather than performing verification itself. Standard practice across surveyed methods is automatic metric-based evaluation, retrieval Recall@K/ranking metrics for the retrieval stage and QA/generation metrics (exact match, F1, ANLS, BLEU/METEOR-style scores) for the answer stage, benchmarked against ground-truth QA pairs constructed for each dataset. The survey is explicit that this verification regime has real gaps: page-level Recall@K does not verify whether the correct fine-grained evidence (a specific table or chart) was actually retrieved, and near-universal reliance on now-saturating, potentially contaminated public benchmarks (DocVQA, InfoVQA) means high scores may reflect memorization rather than genuine document reasoning, a possibility the survey names but cannot itself rule out without training-data audits it does not perform. The security discussion (Appendix D) goes further, stating that most surveyed systems lack any cross-modal provenance-verification mechanism for retrieved evidence, which the survey frames as a live gap given multimodal RAG's exposure to adversarial-image and layout-manipulation attacks.

## Field context

This is a taxonomy paper positioned at the intersection of two established lines of work: document-image understanding (OCR-based pipelines, DocFormer-style layout-aware transformers) and general-purpose RAG, including the text-only graph-RAG lineage the survey itself traces in Appendix G (GraphRAG, LightRAG, HippoRAG-2) and the agent-based RAG lineage in Appendix H (MAIN-RAG, MA-RAG, MMOA-RAG). Its explicit contribution relative to prior surveys, including one it cites directly ("Ask in any modality," a broader multimodal-RAG survey), is narrowing scope specifically to document understanding and adding retrieval-granularity and hybrid graph/agent axes that the survey argues prior surveys under-cover. Within this corpus, its Appendix E critique that agentic and graph-based architectural complexity often buys only marginal accuracy for substantial added latency and cost is an independent, literature-wide echo of [26masat]'s controlled finding that multi-agent coordination's value is conditional and predictable mainly from single-agent task difficulty rather than assumed by default; the two use entirely different methods (a systematic empirical study versus a survey's qualitative synthesis of others' reported numbers) but converge on the same caution against assuming coordination overhead pays for itself. Its retrieval-granularity discussion, structure-aware indexing and retrieval improving precision over flat, undifferentiated retrieval, is a multimodal, page/element-level counterpart to [26intragt]'s single-document, section-aware retrieval agent for scientific papers, though 26intragt is text-only and evaluates a single method rather than surveying the field.

## Critical discussion

The survey's own Appendix E does a genuinely uncommon thing for the genre: it names specific, unresolved contradictions in the literature it surveys rather than only cataloguing progress. The OCR-free/OCR-based trade-off, the benchmark-saturation/contamination concern, and the complexity-performance mismatch for graph- and agent-based methods are each grounded in named methods and named benchmarks rather than left as generic caveats, which is a real strength relative to many taxonomy surveys that stop at "future work should address X." The result is a review that is unusually willing to state that a fashionable direction (agentic, graph-augmented multimodal RAG) may be under-delivering relative to its added cost, based on the aggregate pattern across the very methods the main text spends several pages describing favorably.

That said, three things limit how far this critical stance can be independently verified from the survey text alone. First, the survey's central empirical claims, that a given method "improves" over a baseline, that visual token compression is "near-optimal," that agentic gains are "1-2%", are second-hand: they are extracted from each surveyed paper's own reported comparison, and the survey does not re-run or independently re-verify any of them, so any weak baseline, favorable benchmark selection, or same-family judging bias present in an individual surveyed paper propagates unfiltered into this survey's synthesis. This is a structural limitation of the survey genre rather than a specific error, but it means the survey's own confident language ("collectively, these approaches illustrate...") should be read as a description of what the field claims, not as this survey's independent confirmation of it. Second, three of the ten authors did this work as Alibaba Group interns and two more are Alibaba-affiliated; Alibaba-associated methods (HM-RAG, appearing as a running example across the retrieval-modality, granularity, graph, and agent sections) are cited unusually often relative to a single method's actual footprint in the broader literature, which is worth noting as a potential, if likely unintentional, selection or framing bias in a self-authored taxonomy, though the survey does not claim HM-RAG is state-of-the-art and cites plenty of non-Alibaba methods just as favorably. Third, in an extremely fast-moving area (the survey's own Figure 1 cites rapid publication growth from 2024 to 2025), a survey with a v1 date of October 2025 and a v3 revision through April 2026 is already, by the nature of the field it describes, missing several months of newer methods by the time it reaches a reader; the survey addresses this directly and reasonably by committing to a periodically updated companion GitHub repository rather than treating the paper itself as a frozen final word, which is the right response given the constraint but does not change that a print reading of the taxonomy will age quickly.

What remains well supported: the three-axis taxonomy (modality, granularity, graph/agent enhancement) is a coherent and well-evidenced organizing structure for a genuinely fragmented literature, the dataset/benchmark compilation (Table 3) is a useful practical reference regardless of any individual method's reported numbers, and the survey's own critical-analysis appendix, precisely because it argues against the field's own momentum on evaluation validity and complexity-cost trade-offs, is more trustworthy than the main text's largely descriptive method summaries.

## Relevance to us

None.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| OCR-free page-image encoding | dense text retrieval reliability | contradicts | 0.55 | papers/canonical/2026-06-09/26mdocrag.md:L752 | Image-only VLM page encoding remains vulnerable to visual hallucination on dense, fine-grained text despite avoiding OCR error propagation |
| page level RecallK metric | fine grained evidence localization precision | contradicts | 0.6 | papers/canonical/2026-06-09/26mdocrag.md:L747 | A page can contain multiple independent information sources, so page-level recall does not verify whether the specific correct table or chart was retrieved |
| graph-based indexing and agentic workflows in multimodal RAG | computational overhead and inference latency disproportionate to reported accuracy gains | implies | 0.55 | papers/canonical/2026-06-09/26mdocrag.md:L755 | Surveyed graph- and agent-based methods often report only 1-2% accuracy gains despite significantly higher latency and cost, with little cost-benefit analysis |
| visual token compression and patch merging (e.g., Light-ColPali) | retrieval efficiency and feasibility of indexing full industrial document corpora | improves | 0.6 | papers/canonical/2026-06-09/26mdocrag.md:L771 | Compressing patch-level visual embeddings reduces GPU memory and vector-store size while retaining near-optimal retrieval quality, enabling indexing of complete industrial collections |
| web-scale LLM pretraining exposure to public benchmark data | validity of high scores on saturating benchmarks (DocVQA, InfoVQA) as evidence of genuine document reasoning | contradicts | 0.45 | papers/canonical/2026-06-09/26mdocrag.md:L753 | High scores may reflect memorization from contamination rather than reasoning, an unaddressed risk given LLMs' web-scale pretraining |
