---
schema_version: 1
paper: slug:26matter
title: "A multimodal large language model for materials science"
authors:
  - Yingheng Tang
  - Wenbin Xu
  - Jie Cao
  - Weilu Gao
  - Steven Farrell
  - Benjamin Erichson
  - Michael W. Mahoney
  - Andy Nonaka
  - Zhi Jackie Yao
publication:
  first_public_date: "2026-04-24"
  first_public_date_precision: day
  venue: "Nature Machine Intelligence"
  status: journal
  reviewed_version: published
  reviewed_version_date: "2026-04-24"
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-05-06/26matter.md
raw: papers/raw/2026-05-06/26matter-pdf.md
source_url: https://doi.org/10.1038/s42256-026-01214-y
organizations:
  - name: Applied Mathematics and Computational Research Division, Lawrence Berkeley National Laboratory
    sector: government
    roles: [author_affiliation]
    authors: [Yingheng Tang, Andy Nonaka, Zhi Jackie Yao]
    grants: []
  - name: National Energy Research Scientific Computing Center, Lawrence Berkeley National Laboratory
    sector: government
    roles: [author_affiliation, compute_provider]
    authors: [Wenbin Xu, Steven Farrell]
    grants: ["NERSC GenAI award DDR-ERCAP0030541"]
  - name: NSF National AI Institute for Student-AI Teaming, University of Colorado at Boulder
    sector: academia
    roles: [author_affiliation]
    authors: [Jie Cao]
    grants: []
  - name: Department of Electrical and Computer Engineering, The University of Utah
    sector: academia
    roles: [author_affiliation]
    authors: [Weilu Gao]
    grants: []
  - name: Scientific Data Division, Lawrence Berkeley National Laboratory
    sector: government
    roles: [author_affiliation]
    authors: [Benjamin Erichson, Michael W. Mahoney]
    grants: []
  - name: International Computer Science Institute
    sector: nonprofit
    roles: [author_affiliation]
    authors: [Benjamin Erichson, Michael W. Mahoney]
    grants: []
  - name: Department of Statistics, University of California at Berkeley
    sector: academia
    roles: [author_affiliation]
    authors: [Michael W. Mahoney]
    grants: []
  - name: US Department of Energy, Office of Science
    sector: government
    roles: [funder]
    authors: [Yingheng Tang, Zhi Jackie Yao]
    grants: ["LAB-25-3560 (Transformational AI Model Consortium, ASCR)", "DE-AC02-05CH11231 (Lawrence Berkeley National Laboratory LDRD program)"]
  - name: National Science Foundation
    sector: government
    roles: [funder]
    authors: [Weilu Gao]
    grants: ["2235276"]
artifacts:
  - type: data
    url: https://doi.org/10.5281/zenodo.18735961
  - type: code
    url: https://doi.org/10.5281/zenodo.18735881
facets:
  domains: [materials-science, machine-learning, multimodal-learning]
  paper_type: [method, experiment, system]
  methods: [multimodal-llm, graph-neural-network, bridging-module, contrastive-learning, retrieval-augmented-generation, bootstrapped-pretraining]
  models: [Mistral-7B, CHGNet, MACE, Llama-3, DeepSeek-R1, Vicuna-7B, SchNet]
  benchmarks: [Materials-Project, MPtrj, GNoME]
assessment:
  extract_quality: partial
  extract_limitations: [figures-not-visually-assessed, table-extraction-damaged]
  critical_flags: [weak-baseline, missing-uncertainty]
metadata_notes: "Received 2025-04-04, Accepted 2026-03-06, Published online 2026-04-24 per the article header; first_public_date uses the publication date. Figure 5's per-model, per-task bar values (classification accuracy and RMSE across nine tasks and nine baseline/variant combinations) render in the extraction as a flat, unlabelled list of numbers that cannot be reliably re-associated with specific model/task pairs, so this review reports only the unambiguous prose-stated numbers (aggregate RAG improvement, latency, dataset sizes) rather than reconstructing the fine-grained table."
---

Citation: Yingheng Tang, Wenbin Xu, Jie Cao, Weilu Gao, Steven Farrell, Benjamin Erichson, Michael W. Mahoney, Andy Nonaka, and Zhi Jackie Yao. A multimodal large language model for materials science. Nature Machine Intelligence (2026). https://doi.org/10.1038/s42256-026-01214-y

## What this paper is about

Predicting a material's properties (does it conduct electricity, is it stable, what is its bandgap) usually means either running expensive quantum-chemistry simulations or training a graph-based machine-learning model that only speaks in numbers, not language. Meanwhile, general-purpose chatbots can discuss materials in plain English but cannot see a material's actual 3D atomic structure, so their quantitative predictions are unreliable. This paper introduces MatterChat, a system that connects a pretrained atomistic structure model (which reads a material's 3D atomic graph) to a pretrained language model (which reads and writes text), using a small trainable "bridge" module in between. The result is a single system a researcher can ask questions of in natural language ("what is the bandgap of this material?", "give me a synthesis protocol") while its answers are grounded in the material's actual atomic structure rather than in text alone.

## Extended summary

MatterChat has three components. A material processing branch encodes a crystal structure as an atomic graph and extracts embeddings using the frozen encoder of an existing pretrained universal machine-learned interatomic potential (MLIP) — either CHGNet or MACE-MP-0 (large), both trained by others on broad materials datasets and used here without further pretraining. A language processing branch is a frozen Mistral-7B LLM that turns the user's text prompt into embeddings. A bridge model, architecturally modeled on BLIP-2 (the vision-language bridging method), sits between them: 32 trainable query vectors alternate cross-attention (pulling structural features from the atom embeddings) and self-attention (refining those queries) across a multilayer transformer, then a linear projection maps the result into the LLM's embedding space. Only the bridge module is trained; both the structural encoder and the LLM stay frozen, which the authors argue keeps training cheap and lets components (encoder or LLM backbone) be swapped without retraining the rest — they report ablations across CHGNet vs MACE encoders and Mistral vs Llama 3 vs DeepSeek R1 backbones.

Training data comes from 142,899 relaxed crystal structures curated from the Materials Project Trajectory (MPtrj) dataset, each paired with a generated text dataset spanning 12 tasks: three descriptive tasks (chemical formula, space group, crystal system) and nine property-prediction tasks (metallicity, direct bandgap, stability, experimental observation, magnetic status, magnetic order, formation energy, energy above the hull, bandgap value). Training has two stages: a BLIP-2-style pretraining stage that aligns the frozen graph encoder with text using three combined losses (graph-text contrastive loss, graph-conditioned text-generation loss, graph-text matching loss) without the LLM attached, followed by instruction fine-tuning with the LLM attached, using a standard cross-entropy loss over all 12 tasks jointly. Training used AdamW (learning rate 2×10⁻⁴ in both stages, ~25 pretraining epochs and ~20 fine-tuning epochs), distributed across 32 A100 GPUs (4 per node × 8 nodes) for about 48 hours total. The evaluation set held out 14,290 samples (a 9:1 split).

On the nine property-prediction tasks, MatterChat is reported to consistently outperform open-source text-only LLM baselines (Vicuna-7B, Mistral-7B fine-tuned on serialized CIF-format text), specialized graph-based physical models (SchNet, CHGNet, MACE trained from scratch or fine-tuned) in classification accuracy, and to achieve the lowest RMSE among compared methods on the three numerical regression tasks (bandgap, formation energy, energy above the hull); pure LLMs were excluded from the regression comparison because of what the authors describe as their inherent limitations in quantitative precision. A five-fold cross-validation check is reported as consistent with the original train/test split, with a slight, unquantified drop attributed to reduced training data per fold. Adding a retrieval-augmented generation (RAG) step — retrieving the two nearest training-set neighbors by L2 embedding similarity and aggregating by majority vote (classification) or averaging (regression) — is reported to reduce regression RMSE by about 12% and improve classification accuracy by about 0.6%, at roughly 0.7% additional inference latency (headline figures throughout the paper are reported without RAG unless stated otherwise). On an external, out-of-distribution test set of roughly 15,000 materials from the GNoME database, the MACE-encoder variant of MatterChat is reported to transfer with the best accuracy among the compared configurations despite a reported distributional shift in the target properties relative to the training data, without additional fine-tuning.

A separate, more informal comparison (Fig. 2b) benchmarks MatterChat's formation-energy predictions against three commercial general-purpose chatbots — Gemini, GPT-4o, and DeepSeek — on newly discovered GNoME materials, reporting that MatterChat's predictions align more closely with ground-truth DFT values; the paper's abstract summarizes this broader comparison as "surpassing general-purpose LLMs such as GPT-4."

Beyond property prediction, the paper presents three worked case studies of "advanced scientific reasoning": for a metastable silicon phase (space group Cmcm), MatterChat both retrieves the correct properties and explains, in prose, why this phase is thermodynamically less stable than the standard diamond-cubic structure; for gallium nitride, it generates a step-by-step metal-organic chemical vapour deposition synthesis protocol (trimethylgallium and ammonia precursors, 800–1,000 °C growth window) that the authors say matches established literature methods; for yttrium iron garnet, it generates a solid-state-reaction synthesis protocol (3:5 Y₂O₃:Fe₂O₃ mixing ratio, ~5 °C/min thermal ramp) that the authors likewise describe as consistent with standard procedures. The authors describe this as a two-stage, task-agnostic process: structural attributes are extracted via the frozen encoder into a persistent "working memory," and the LLM then generates responses conditioned on that context, without any task-specific supervision for the synthesis-protocol generation itself.

An embedding-analysis section uses UMAP to visualize the bridge model's learned representations for silicon/carbon/silicon-carbide compounds (and, in supplementary material, several other material families), reporting that materials cluster by both structural similarity (computed via a SOAP/REMatch structural-similarity kernel) and formation energy, including a specific observed case where two structurally similar SiC polymorphs form separate embedding clusters that align with a formation-energy split rather than composition alone. A further attention analysis, examining which of the bridge model's 32 query vectors are most attended to by "stable"/"not" tokens across 20 stable and 20 unstable sampled materials, reports that certain query indices are more selectively activated for stable versus unstable materials, which the authors interpret as evidence the model maps linguistic concepts onto physically relevant structural features rather than "merely recalling data."

Authors' stated limitations, in their own "Limitation and future work" section: (1) MatterChat's task performance may reflect learned correlations rather than deep semantic grounding in the structural graph, limiting compositional reasoning about structure; (2) training relies on single-turn question-answer pairs and lacks multistep, cross-modal reasoning chains, which the authors flag as future work (multiturn dialogue, phased instruction tuning); (3) the frozen LLM backbone remains susceptible to hallucination where language priors override structural information, an issue RAG only partly mitigates. The paper separately reports, outside the formal limitations section, a "resolution gap": MatterChat retrieves discrete structural counts (e.g., 28 atoms per unit cell) accurately but is less accurate on continuous derived quantities such as volume and density, which the authors attribute to a general limitation of LLMs in high-precision zero-shot numerical regression.

## Learnings

A frozen, pretrained physics-domain encoder (a universal interatomic potential such as CHGNet or MACE) can be bridged into a frozen, pretrained general-purpose LLM through a small trainable module alone, without fine-tuning either endpoint, and the resulting system reportedly swaps cleanly between at least two structural encoders and three LLM backbones. This is a concrete, working instance of a "freeze both ends, train only the bridge" design for combining a physics-native representation with general language capability, at a fraction of the cost of training or fine-tuning either the encoder or the LLM.

A system can retrieve a precise discrete fact (atom count) correctly while still showing a measurable "resolution gap" on continuous numerical quantities derived from the same structure (volume, density). This is a specific, reproducible instance of a broader pattern worth watching for: LLM-adjacent systems seem to handle categorical or discrete retrieval more reliably than precise continuous-quantity regression, even when the discrete and continuous quantities come from the same underlying structural representation.

A cheap retrieval step — averaging or majority-voting over just the two nearest neighbors in embedding space from the training pool — produced a reported ~12% RMSE reduction on regression tasks for roughly 0.7% added latency. This is a low-cost way to buy robustness from an already-trained predictor, though as reported it is only evaluated in-distribution (the paper's out-of-distribution GNoME evaluation is not reported with RAG enabled), so it is unclear whether the same gain would hold on genuinely novel materials rather than ones with close neighbors in the training pool.

## Verification

The paper's quantitative claims are checked against deterministic, external ground truth rather than an LLM judge: property-prediction accuracy and RMSE are computed against density-functional-theory-derived values from the Materials Project and GNoME databases, which is a meaningfully stronger form of verification than LLM-as-judge scoring for the numerical tasks. A five-fold cross-validation check is reported as consistent with the main train/test split, though the specific per-fold numbers are not given in this extract. The qualitative "advanced scientific reasoning" claims (the silicon-stability rationale, the GaN and YIG synthesis protocols) are checked only informally, by the authors' own comparison to what they describe as established or landmark literature methods; no blinded expert review, no scoring rubric, and no systematic sample of synthesis-protocol generations (only three worked examples) are reported, so these case studies demonstrate plausibility rather than measured reliability. The embedding-clustering and attention-pattern analyses (UMAP visualization, query-activation patterns for stable versus unstable materials) are observational, correlational evidence for what the model's internal representations track; the paper does not report an interventional or ablation check (for example, knocking out the specific query indices it identifies as stability-relevant and confirming that predictions degrade) that would more directly support the causal interpretation given to these patterns.

## Field context

MatterChat's bridging architecture is explicitly modeled on BLIP-2 (vision-language bootstrapping with frozen encoders), transplanted from the vision-language setting into materials-graph-and-text. It builds on two existing pretrained universal machine-learned interatomic potentials, CHGNet and MACE-MP-0, using their encoders unmodified as structural feature extractors, and is trained and evaluated on the Materials Project / MPtrj dataset with an external out-of-distribution evaluation against GNoME (Google DeepMind's large-scale materials-discovery dataset). The authors position the work against a line of prior materials-specific LLM benchmarks (MatSci-NLP, MaScQA, HoneyBee, and others) that they characterize as relying primarily on text-serialized representations (chemical formulas, SMILES strings, CIF files) rather than full 3D graph structure, and argue this textual bottleneck is why those approaches underperform graph-based models on property prediction — a claim attributed to a cited comparison (ref. 40) rather than demonstrated fresh in this paper. None of MatterChat's specific precedents (BLIP-2, CHGNet, MACE, the cited materials-LLM benchmarks, or GNoME) are yet reviewed in this corpus, so this positioning reflects the authors' own framing rather than an independent check against another review here.

## Critical discussion

The paper's fairest and most informative comparison is the one buried in its ablations rather than foregrounded in its abstract: a Mistral-7B LLM fine-tuned on serialized CIF-format text, evaluated on the same nine property-prediction tasks as MatterChat. This is the correct apples-to-apples baseline for isolating what the graph-based structural bridge actually buys over a text-only LLM with the same backbone, and the paper reports it underperforms MatterChat, which is a legitimate, well-controlled result supporting the central architectural claim.

The abstract's higher-profile claim — "surpassing general-purpose LLMs such as GPT-4" — rests on a different and much less controlled comparison (Fig. 2b): commercial chatbots (Gemini, GPT-4o, DeepSeek) prompted to estimate formation energy for GNoME materials, apparently without being given the 3D atomic structure MatterChat has direct access to via its encoder. A model with no path to see the actual atomic geometry cannot be expected to match one that does, on a task where geometry is the determining factor; this is closer to demonstrating that structural information helps quantitative regression (already well established in the materials-ML literature the paper itself cites) than to demonstrating something specific about MatterChat's architecture. The comparison is also not the model named in the abstract: GPT-4o, not GPT-4, is what is actually benchmarked. Neither point undermines the paper's core architectural contribution, but the abstract's framing invites a reading (MatterChat's design beats frontier general-purpose LLMs at reasoning about materials) that the underlying experiment does not really test; the CIF-text-LLM ablation is the experiment that actually tests it, and it is reported with less prominence.

The interpretability analysis (embedding clustering by structural similarity and formation energy; specific bridge-module query indices linked to stability prediction) is presented with fairly strong causal-sounding language ("MatterChat does not merely recall data but effectively maps linguistic concepts onto physically relevant structural descriptors"), but the underlying evidence is observational: attention magnitude and cosine similarity correlate with known chemical/structural properties across a modest sample (24 materials for the similarity matrix; 20 stable and 20 unstable examples for the attention analysis). Correlation between attention weight and a downstream label is not the same as demonstrating that the identified indices causally drive the stability prediction; no ablation removing or perturbing those specific indices is reported to test whether predictions degrade accordingly. This is a common gap in neural-network interpretability claims generally, not a defect unique to this paper, but it means the stronger causal framing in the text outpaces what the reported analysis directly establishes.

Reported uncertainty is thin throughout: the headline classification-accuracy and RMSE comparisons across nine tasks and multiple baselines are given as point estimates without confidence intervals or per-fold variance, and the cross-validation check is described only qualitatively ("remained consistent") rather than with reported per-fold numbers in this extract. This makes it hard to judge how much of the reported gap between MatterChat and the next-best baseline (CHGNet fine-tuned, in most tasks) is a robust, large effect versus a narrower one that a confidence interval would reveal.

What remains well supported after these caveats: the core architectural claim — that bridging a frozen structural encoder to a frozen LLM via a lightweight trainable module outperforms a text-only LLM given the same backbone and task set, and is competitive with or better than specialized graph-based property predictors on the tasks tested — rests on the paper's own fair ablations and ground-truth-checked regression metrics, and is a reasonable, peer-reviewed result. What is less well supported, given the evidence available in this extract, is the stronger rhetorical claim that MatterChat demonstrates "advanced scientific reasoning" broadly or that it is meaningfully validated against frontier general-purpose LLMs specifically; both rest on a small number of qualitative case studies and an unequal, structure-blind-versus-structure-aware comparison rather than a systematic, ground-truth-checked evaluation of reasoning quality.

## Relevance to us

MatterChat is a working, peer-reviewed instance of the "physics-attuned replaceable backbone plus durable pipeline" pattern behind B02: freeze a domain-specific physics encoder and a general LLM, train only a small bridging module, and get a system that (per the ablations) beats a same-backbone text-only LLM at quantitative property prediction while remaining swappable across encoders (CHGNet, MACE) and LLM backbones (Mistral, Llama 3, DeepSeek R1). That swappability, achieved without retraining the frozen components, is a useful existence proof for the kind of modularity B02 assumes is achievable, even though the domain here (crystal structure property prediction) is narrower and better-suited to a single graph embedding than the wider var­iety of representations physics problems can demand.

The abstract-versus-ablation gap identified above is also a textbook instance of a pattern our own competitive-opening notes as endemic in this space: the flashier claim ("beats general-purpose LLMs") rests on a missing-baseline comparison (the commercial chatbots have no structural input at all), while the actually fair, budget-matched baseline (a same-backbone LLM given text-only structural input) is the one relegated to an ablation table. This is a concrete example to point to when we want to explain, with a citation rather than an abstraction, why B01's insistence on a strong, fair simple baseline matters: the paper's own honest ablation already makes its case; the less controlled comparison adds rhetorical force without adding evidence.

The self-reported "resolution gap" for continuous numerical properties (accurate atom counts, less accurate volume/density) is also worth flagging alongside a similar numeric-precision weakness noted in our review of the Natural Language Autoencoders work ([26nla](26nla.md)): two unrelated methods, in two different domains, both surface LLM-adjacent systems being reliable on discrete/categorical content and weaker on precise continuous quantities. That is not yet enough independent evidence to call this a well-established pattern, but it is a specific, recurring caution for any physics-facing system (ours included) that leans on an LLM component anywhere near a precision-sensitive continuous number.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| graph-based structural bridge embeddings | CIF-text-based LLM property prediction | improves | 0.8 | papers/canonical/2026-05-06/26matter.md:L958 | Fair same-backbone ablation: Mistral-7B fine-tuned on CIF text underperforms MatterChat with the same LLM backbone |
| MatterChat structural graph embeddings | material property prediction accuracy across nine tasks | improves | 0.75 | papers/canonical/2026-05-06/26matter.md:L316 | Outperforms open-source LLM and physical-model baselines on classification and regression, checked against DFT ground truth |
| MatterChat architecture | general-purpose LLMs without structural input | improves | 0.5 | papers/canonical/2026-05-06/26matter.md:L36 | Measured against Gemini, GPT-4o, DeepSeek, but those baselines are not given access to the 3D structure MatterChat's encoder reads |
| multimodal retrieval-augmented ensembling | regression RMSE | improves | 0.7 | papers/canonical/2026-05-06/26matter.md:L799 | ~12% RMSE reduction and ~0.6% accuracy gain at ~0.7% latency overhead, evaluated in-distribution only |
