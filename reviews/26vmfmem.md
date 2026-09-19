---
schema_version: 1
paper: slug:26vmfmem
title: "The von Mises–Fisher N-Gram Memory Module for O(1) Zero-Shot Fact Injection"
authors:
  - Not stated in source
publication:
  first_public_date: "2026"
  first_public_date_precision: year
  venue: unpublished
  status: other
  reviewed_version: null
  reviewed_version_date: null
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-05-06/26vmfmem.md
raw: papers/raw/2026-05-06/26vmfmem-pdf.md
organizations: []
artifacts: []
facets:
  domains: [machine-learning]
  paper_type: [theory, position]
  methods: [von-mises-fisher-distribution, hashed-n-gram-memory, spherical-linear-interpolation, model-editing]
  models: [DeepSeek Engram]
  benchmarks: []
assessment:
  extract_quality: good
  extract_limitations: [figures-not-visually-assessed, table-extraction-damaged]
  critical_flags: [overclaim, incomplete-reporting]
metadata_notes: "No author names, institutions, funding, venue, or submission status appear anywhere in the extract, and the raw dump matches the canonical text exactly, so this is not an omission from canonicalization. The document calls itself a 'research report' and its own Section 7 is a checklist of what would still be needed 'for acceptance at a top-tier machine learning conference,' i.e. it presents no experiments and does not claim to have been submitted or published anywhere. first_public_date is inferred only from its citations to three 2026 arXiv preprints (the corpus's YYMM id convention: refs [2], [3], [10] dated 2601–2602); the year is a lower-bound inference, not a stated date. The two comparison tables (mechanism-cost table after Section 5, evaluation-metric table before the Conclusion) render with columns and rows interleaved in the extraction and are reconstructed here by inference from context; the numbers themselves (e.g. '>95%', 'Zero') are quoted as they appear, uncited, in the source."
---

Citation: Unattributed. The von Mises–Fisher N-Gram Memory Module for O(1) Zero-Shot Fact Injection. Unpublished report, 2026 (undated). No source URL given in the extract.

## What this paper is about

This is a proposal, not a study: it argues that a language model's fast-changing factual memory (names, dates, current leadership, etc.) could be stored not as a single fixed vector per fact, as in a recent lookup-table memory design ("DeepSeek Engram"), but as a probability distribution on a sphere — a mean direction plus a "confidence" number. The pitch is that editing a fact would then reduce to overwriting the mean direction and cranking the confidence number to its maximum, with no retraining, no gradient updates, and (the document claims) no side effects on unrelated knowledge. The report works through the math of that idea, argues why it would be a meaningful advance over existing ways of editing model knowledge, lists ways the idea could fail, and closes with a checklist of the experiments a future version of this work would need in order to be publishable. No such experiments are run here.

## Extended summary

The report first restates, as background, a baseline it calls the "DeepSeek Engram" architecture (cited as an external 2026 arXiv preprint, ref [3], not itself in this corpus): selected Transformer layers hash canonicalized suffix n-grams through H independent hash functions into fixed-size lookup tables stored off-GPU, retrieve a static embedding per n-gram, and fuse it into the hidden state through a learned context-aware gate; a cited "Sparsity Allocation Law" recommends devoting 20–25% of a model's sparse parameter budget to this mechanism, and the residual stream is stabilized by projecting mixing matrices onto the Birkhoff polytope ("Manifold-Constrained Hyper-Connections", mHC).

The proposed extension replaces each table entry's single embedding with a von Mises–Fisher (vMF) distribution over the unit hypersphere, parameterized by a mean direction µ (‖µ‖=1) and a concentration κ ≥ 0 (κ→∞ concentrates all mass at µ; κ→0 is uniform). µ and κ would be learned during pretraining by maximum-likelihood estimation tied to the next-token objective. At inference, a retrieved (µ, κ) pair is compared against the current hidden state via a log-likelihood-derived gate scalar (a sigmoid of κ·(µᵀh) passed through a learned projection), and the memory is fused into the residual stream via Slerp (spherical linear interpolation) rather than additive injection, so the resulting hidden state stays on the sphere.

The central proposed capability is zero-shot fact injection: to change a fact, overwrite the hashed slot's µ with a target embedding µ⋆ and set κ to an artificially extreme maximum. The argument is that a maximal κ forces the gate scalar toward 1 regardless of context, so the Slerp fusion forcibly rotates the hidden state to µ⋆ — a database write standing in for gradient-based editing. This is contrasted with three families of existing model-editing methods (locate-and-edit methods like ROME/MEMIT, hypernetwork methods like MEND, and external-routing methods like SERAC/RAG), each characterized by the report as suffering catastrophic interference, prohibitive training cost, or context-window/latency overhead respectively; two summary tables assert that the proposed method dominates all three on update cost, sequential-edit reliability, context impact, and (in a second table) rewrite accuracy, portability, locality, sequential reliability, MMLU degradation, and inference latency. None of these numbers are attributed to an experiment, citation, or measurement protocol in the text; several (e.g. "∼100%", "Zero", "Negligible") appear to be assertions rather than reported results.

The report itself catalogs four failure modes for the design: (1) hash collisions between semantically unrelated n-grams pull a shared µ in conflicting directions during MLE training, driving κ toward zero and wasting that slot's capacity; (2) forcing κ to an artificial maximum during injection can override the context gate even when the surrounding text contradicts the injected fact ("Apple" the company vs. the fruit), producing fluent but incoherent "superficial mimicry"; (3) frequent n-grams cluster densely on the hypersphere while rare ones are diffuse, so an injected µ near a dense region can bleed into semantically adjacent concepts; (4) the mHC Birkhoff-polytope projection's non-negativity constraint can force mixing matrices toward the identity map, suppressing the very cross-stream routing the vMF rotation depends on. Section 7 then proposes mitigations (collision-free hashing via MPZCH or Cuckoo hashing, a less constrained "Spectral-Sphere-Constrained Hyper-Connections" alternative to mHC, learned/scheduled κ, Dirichlet priors over prototypes) and a experimental protocol a future version of the paper "must" run: CounterFact, ZsRE and a "QAEdit" benchmark tracking reliability/generalization/locality/portability as edits scale from 10 to 10,000, MMLU before/after editing to check for collateral damage, and replication of a cited Needle-in-a-Haystack improvement (84.2%→97.0%) attributed to the DeepSeek Engram baseline. All of this is framed as future work; none of it is executed in this document.

## Learnings

None. The document proposes a mechanism and reasons about it, but reports no experiment, measurement, or observation of its own; there is nothing here that has been demonstrated rather than argued.

## Verification

The report does not verify anything itself. Section 7.4 lays out what a verification protocol would need to look like — track Reliability, Generalization, Locality and Portability across CounterFact, ZsRE and a proposed QAEdit benchmark; require the reliability curve to stay flat as injected facts scale from 10 to 10,000 (contrasted with the "rapid exponential decay" the report attributes to ROME/MEMIT); check pre/post-edit MMLU for collateral damage; replicate a cited long-context NIAH improvement — but explicitly as a to-do list ("the paper must feature...", "must track...", "must replicate or exceed"), not as something performed. No judge, checker, or human evaluation is used anywhere in the document; the only place anything resembling "checking" occurs is the self-authored failure-mode analysis in Section 6, which is reasoned through rather than tested.

## Field context

The report positions itself as a direct extension of a cited external architecture, "DeepSeek Engram" (arXiv:2601.07372, not present in this corpus), adding a probabilistic layer on top of that design's deterministic hash-table memory, and separately draws on a cited "Spherical Steering" activation-rotation technique (arXiv:2602.08169) and a cited uncertainty-quantification paper using directional statistics (arXiv:2602.13264), plus the foundational vMF-distribution reference (Banerjee et al., JMLR 2005) and the original Product Key Memory paper (Lample et al., NeurIPS 2019). It explicitly contrasts itself with the locate-and-edit (ROME, MEMIT), hypernetwork (MEND), and external-routing (SERAC, RAG) lines of model-editing work. None of the papers this report builds on or contrasts itself against are yet reviewed in this corpus, so none of its characterizations of those methods (e.g., the specific reliability-decay behavior attributed to ROME/MEMIT, the NIAH numbers attributed to DeepSeek Engram) can be cross-checked against an independent review here; they are reported as this document's own account of secondary sources, not verified facts. The "DeepSeek Engram" baseline is treated throughout as an established, validated breakthrough rather than as a claim under its own scrutiny, which this report does not apply to its central citation the way it applies scrutiny (Section 6) to its own proposed extension.

## Critical discussion

The report's own internal structure undercuts its confident framing. The Abstract-level language ("unprecedented capacity," "instantaneous, gradient-free knowledge updates," a "profound structural innovation" that "renders gradient-based updates obsolete") is not supported by anything demonstrated in the text: there is no implementation, no dataset, no measured number anywhere in the document that was produced by running anything. The two comparison tables (mechanism-cost comparison after Section 5; evaluation-metric comparison before the Conclusion) present specific-looking entries — "∼100% (Deterministic Database Write)," "Zero (Fact perfectly localized)," "Negligible (O(1) latency increase)" — for the proposed method against ROME/MEMIT, MEND, SERAC and RAG, with no citation, benchmark, or method attached to any cell. This is the clearest instance of the overclaim flag: the tables have the visual form of reported results while containing none.

Section 6 of the same document then identifies four mechanisms that plausibly break exactly the claims made everywhere else: a forced maximum κ can override context and produce "Superficial Mimicry" (contradicting the "perfectly reliable" framing), hash collisions waste capacity and silently degrade untested slots, rare facts sit in low-confidence, high-interference regions of the hypersphere, and the cited stabilization mechanism (mHC/Birkhoff projection) can itself suppress the cross-stream routing the whole method depends on. None of these four risks are quantified — there is no estimate of collision rate at a realistic vocabulary/hash-table size, no case study of superficial mimicry, no measurement of how "geometric imbalance" actually degrades outputs — so the paper cannot say whether these are minor caveats or fatal flaws to the central claim. Because Section 6 is not connected to any experiment, it functions as a plausible risk list rather than a bounded characterization of failure rate, which is itself consistent with the rest of the document: reasoning stands in for measurement throughout.

The reliance on an external, unreviewed preprint (DeepSeek Engram) as settled ground truth is a second-order version of the same issue: specific numbers this report leans on for context (the 84.2%→97.0% NIAH improvement, the 20–25% Sparsity Allocation Law recommendation) are attributed to that other paper without this report subjecting them to the kind of scrutiny it applies to its own proposal, and this corpus has no independent review of that source to check the attribution against.

What remains defensible after these caveats: the mathematical exposition of the vMF distribution and its normalizing constant is a correct, properly cited restatement of standard directional statistics (Banerjee et al. 2005), and Slerp as a norm-preserving alternative to additive activation injection is a reasonable way to avoid the magnitude drift that plagues naive activation steering, which the report correctly identifies as a known problem. The self-authored failure-mode catalog in Section 6 is a genuinely useful list of concrete risks (collision-induced κ collapse, contextual override, minority-entity imbalance, mHC bottlenecking) for anyone who might actually build this kind of writable, probabilistic memory — as risks to test for, not as risks this document has ruled out.

## Relevance to us

The core idea here — a per-fact writable probabilistic memory, confidence-parameterized and editable by direct overwrite rather than gradient descent — is a close match to our own B22 (MF-Engram: writable probabilistic memory, frozen backbone) and to the "writable lookup memory vs RAG vs fine-tune" mechanism we already track. This document is not evidence for or against that bet; it contributes nothing measured. What it does offer, usable independent of its overclaiming, is a pre-built list of failure modes a physics-directed version of B22 would need to survive before we could trust it: hash-collision-driven confidence collapse for facts or relations that share a surface n-gram, a forced-confidence override mechanism silently defeating a context-aware gate exactly when context should matter most (the physics analogue of "Apple the company vs. the fruit" is a symbol or unit reused across different physical regimes), and confidence/geometry imbalance for rare, long-tail entries — which for us would mean rare notations, unusual conventions, or narrow sub-fields getting worse-calibrated confidence than common ones. These are hypotheses to design tests for if we build toward B22, not validated constraints.

The maximal-κ override described here is also worth contrasting with our own "knowledge dial" bet (B15: suppress recall, then verify): this design is architecturally the opposite move — force recall to maximum confidence with no verification step — and the paper's own Section 6 is effectively an unquantified argument for why that opposite move is risky. That contrast is a useful framing device, not a result to cite.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| vMF zero-shot database-write injection | sequential model-editing reliability | improves | 0.2 | papers/canonical/2026-05-06/26vmfmem.md:L144 | Comparison table asserts near-perfect reliability vs ROME/MEMIT/SERAC with no cited experiment or measurement method |
| vMF database-write fact injection | gradient-based model editing | improves | 0.15 | papers/canonical/2026-05-06/26vmfmem.md:L56 | Paper argues database-write editing supersedes gradient-based editing analytically; no implementation or test is reported |
