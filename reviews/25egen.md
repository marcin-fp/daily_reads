---
schema_version: 1
paper: slug:25egen
title: "E-Gen: Leveraging E-Graphs to Improve Continuous Representations of Symbolic Expressions"
authors:
  - Hongbo Zheng
  - Suyuan Wang
  - Neeraj Gangwar
  - Nickvash Kani
publication:
  first_public_date: "2025-01"
  first_public_date_precision: month
  venue: "NAACL 2025 (Long Papers)"
  status: conference
  reviewed_version: "NAACL 2025 camera-ready"
  reviewed_version_date: null
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-05-06/25egen.md
raw: papers/raw/2026-05-06/25egen-pdf.md
source_url: https://aclanthology.org/2025.naacl-long.590/
organizations:
  - name: University of Illinois at Urbana-Champaign
    sector: academia
    roles: [author_affiliation]
    authors: [Hongbo Zheng, Suyuan Wang, Neeraj Gangwar, Nickvash Kani]
    grants: []
  - name: National Center for Supercomputing Applications (NCSA)
    sector: nonprofit
    roles: [compute_provider]
    authors: []
    grants: []
artifacts:
  - type: code
    url: https://github.com/MLPgroup/E-Gen
  - type: data
    url: https://github.com/MLPgroup/E-Gen
facets:
  domains: [machine-learning, natural-language-processing, mathematics]
  paper_type: [method, experiment]
  methods: [e-graph-based-data-generation, contrastive-learning, seq2seq, embedding-algebra, k-means-clustering]
  models: [GPT-4o]
  benchmarks: []
assessment:
  extract_quality: good
  extract_limitations: [figures-not-visually-assessed]
  critical_flags: [weak-baseline, missing-uncertainty]
metadata_notes: "arXiv:2501.14951 (month precision from the YYMM id; exact day not independently confirmed). Published as NAACL 2025 Long Papers, pages 11772-11788 (aclanthology.org/2025.naacl-long.590), conference held 2025-04-29 to 2025-05-04 in Albuquerque; exact camera-ready date not stated in the extract. No external grant is named; acknowledgments thank the University of Illinois for institutional support and NCSA for compute access only."
---

Citation: Zheng, H., Wang, S., Gangwar, N., and Kani, N. E-Gen: Leveraging E-Graphs to Improve Continuous Representations of Symbolic Expressions. In Proceedings of NAACL 2025 (Long Papers), pages 11772-11788. https://aclanthology.org/2025.naacl-long.590/

## What this paper is about

Teaching a model to recognize when two differently-written math expressions mean the same thing (e.g. `sin(x)` and `-sin(-x)`) requires training data with many rewrites per expression, not just one or two. Prior synthetic datasets, built by running a computer-algebra system's simplifier, mostly produce single pairs (an expression and its simplest form), which is a weak training signal. This paper introduces E-Gen, a method that instead uses an e-graph — a data structure from the compiler-optimization world for representing all ways a term can be rewritten — to systematically generate large clusters of many mutually equivalent expressions per starting expression. The authors train small transformer-based embedding models on this richer data and show they substantially outperform both a prior SymPy-based approach and GPT-4o on several tasks, including detecting errors in step-by-step math derivations.

## Extended summary

The corpus starts from about 5,000 hand-templated initial expressions covering arithmetic, trigonometric, hyperbolic, logarithmic/exponential, and their inverse operators (34 operators total). Each is fed through E-Gen, which applies roughly 800 mathematical rewrite rules via e-graph saturation: an e-graph groups equivalent sub-terms into "e-classes," and repeatedly applying rules (e.g. `(x+y)-z → x+(y-z)`, `x-x → 0`) either adds new equivalent forms to an e-class or merges e-classes, until no more rules apply. The saturated e-graph is then converted into a context-free grammar, from which a recursive algorithm extracts concrete equivalent expressions (capped at 25 tokens and 600 seconds of generation time per initial expression) to form clusters. This yields an average cluster size of 102 equivalent expressions per starting expression, versus 2 (i.e., pairs) for the prior SymPy-based "Equivalent Expressions Dataset" (EED) from the same lab's earlier SEMEMB work — with more operators (34 vs 24) and a comparable average sequence length. The resulting corpus totals about 55 million equivalent-expression pairs and 50 million contrastive triplets for training, with an 8,077-expression held-out validation/test set across 279 clusters.

Two embedding approaches are trained on this data, both using a transformer encoder over expressions in prefix notation: a seq2seq model, trained to generate one equivalent expression given another (following the same objective as the prior SEMEMB work); and a contrastive-learning model, trained with an InfoNCE-style loss on (anchor, equivalent, non-equivalent) triplets to pull equivalent expressions together and push non-equivalent ones apart in embedding space, with two pooling variants (mean and max over the final encoder layer) trained separately.

Four evaluations compare these models against the prior SEMEMB baseline (trained on the SymPy-based EED corpus) and, for two tasks, against GPT-4o. (1) K-means clustering of the 8,077-expression test set into its 279 ground-truth clusters: the E-Gen-trained models reach 96.7-97.6% accuracy versus 37.7% for SEMEMB. (2) A "semantic understanding beyond syntactic similarity" task, where a model must pick the true semantic equivalent of a query expression from among 7 candidates, 6 of which are syntactically similar decoys: the seq2seq model reaches 76.4% versus 28.6% for SEMEMB (contrastive variants score 48-50%, lower than seq2seq on this specific task). (3) Mistake detection in step-by-step derivations: SymPy-generated derivations (18,462 total steps, 2,974 containing an introduced error) are classified step-by-step as "mistake" or "no mistake" using a per-model cosine-similarity threshold between consecutive steps' embeddings, computed once from correct-step similarities in the training set (Algorithm 1: the average, across training derivations, of each derivation's minimum correct-step cosine similarity). The E-Gen-trained models reach F1 of 77-78% on the "mistake" class versus 53.6% for SEMEMB, with similarly-high "no mistake" F1 (89-96% across models). (4) "Embedding algebra": analogy-style reasoning (given x1, y1, x2, predict y2 via `f(y2) ≈ -f(x1)+f(y1)+f(x2)` in embedding space) evaluated on 584 manually constructed analogies drawn from the E-Gen corpus; the seq2seq model reaches 70.4% accuracy, ahead of the contrastive variants (50.3-64.7%) and SEMEMB (54.9%).

A separate comparison pits the seq2seq model directly against GPT-4o (prompted, not via its own embeddings) on two of these tasks. For mistake detection, a smaller subsample (322 steps, 50 of them mistakes) is used; GPT-4o is first shown an example derivation and given corrective feedback if it fails to identify the mistake, "until it correctly understands the task," before being tested on the sampled steps. GPT-4o reaches 92.2% F1 on "no mistake" but only 61.1% F1 on "mistake" (versus 94.8%/78.5% for the seq2seq model on the full test set), with the authors attributing this to a high false-positive rate: GPT-4o tends to flag mathematically valid but syntactically different rewrites as errors, and conversely sometimes accepts genuinely invalid operator substitutions. For embedding algebra, GPT-4o (again shown one example before testing) reaches 39.6% accuracy, below every embedding model tested including SEMEMB (54.9%); worked examples show GPT-4o sometimes imitating the surface structure of the analogy's second term rather than applying the correct mathematical transformation (e.g., predicting `csc(x-π/2)` instead of `csc(x+π/2)`).

The paper's stated limitations: the operator set, while broader than prior work, is narrower than what appears in real published mathematical text (the authors cite ArXMLiv and ARQMath as examples of richer real-world corpora); the recursive grammar-enumeration procedure used to extract expressions from the saturated e-graph is simple and could be made more efficient (e.g., via Earley-algorithm-based techniques) to scale to more complex or higher-arity operators; variable characteristics such as dimensionality, phase, or bounds are not encoded and are noted as an open direction; and integrating these purely symbolic embeddings with natural-language embeddings for mixed math-plus-text retrieval (as needed for tasks like ARQMath) remains unaddressed.

## Learnings

A deterministic, cheap cosine-similarity threshold — computed once from training-set statistics, with no LLM judge or learned classifier involved at inference time — substantially outperformed a frontier LLM (GPT-4o) prompted to classify the same kind of error: F1 on the "mistake" class was 77-78% for the trained embedding models versus 61.1% for GPT-4o (on a smaller subsample), with GPT-4o's errors concentrated in false positives on mathematically valid but syntactically unusual rewrites. This is a concrete instance of a simple, non-judge-based geometric check beating a general-purpose LLM's judgment at a narrow verification task.

Changing only the training-data generation method, while holding the downstream model architecture fixed, produced an unusually large single-lever effect: switching from a SymPy-simplification-based corpus (average cluster size 2) to an e-graph-saturation-based corpus (average cluster size 102) took clustering accuracy from 37.7% to 96.7-97.6% on the same task and architecture. Cluster size and diversity of the training data, not the embedding model itself, appears to be the dominant factor here.

Contrastive learning's training objective is a closer conceptual match to a clustering evaluation (pull equivalents together, push non-equivalents apart) than sequence-to-sequence generation is, yet the simpler seq2seq model generalized better to an analogy-style "embedding algebra" reasoning task (70.4% versus 50.3-64.7% for the contrastive variants). The training objective best suited to one evaluation is not automatically the one that transfers best to a structurally related but distinct evaluation.

## Verification

Mistake detection in symbolic derivations is this paper's own verification mechanism, and it is deterministic and non-LLM-judge-based: a fixed cosine-similarity threshold between consecutive derivation-step embeddings, calibrated once (Algorithm 1) from the minimum correct-step similarity observed across training derivations, then applied unchanged at test time. This gives full coverage (every step in the 18,462-step test set is classified) with a stated, reproducible calibration procedure, and the paper reports per-class precision/recall/F1 rather than a single aggregate accuracy, which is appropriate given the "mistake" class is a minority (2,974 of 18,462 steps, about 16%). The comparison against an LLM-judge-style approach (GPT-4o prompted directly to classify mistakes) is informative but should be read cautiously: it uses a much smaller sample (322 of 18,462 steps, with only 50 mistakes) with no reported confidence interval or variance, and GPT-4o was given an example derivation and iterative corrective feedback before testing, a calibration step not clearly matched by any analogous adjustment on the embedding-model side (whose threshold is fixed by a training-set statistic, not tuned interactively against test-adjacent feedback).

## Field context

E-Gen is explicitly built as a direct successor to the same research group's prior SEMEMB model and its SymPy-generated "Equivalent Expressions Dataset" (Gangwar and Kani, 2023), replacing SymPy's single-simplification-per-expression generation with e-graph saturation to produce much larger equivalence clusters. It positions itself against EQNET (Allamanis et al., 2017, TreeNN-based, limited to arithmetic/boolean expressions) and against text-context-based mathematical embedding approaches (Krstovski and Blei, 2018; MathBERT) that the authors argue cannot process pure symbolic content lacking surrounding prose. It also cites Lample and Charton's (2019) sequence-to-sequence approach to symbolic mathematics as a methodological precedent for using prefix notation with transformer encoders. None of these specific precedents are yet reviewed in this corpus.

## Critical discussion

The core comparison against the prior SEMEMB baseline is well-controlled: same downstream architecture family, same evaluation tasks and test set, with the only stated difference being the training corpus's generation method (SymPy simplification versus e-graph saturation), which makes the large accuracy gaps reported (e.g., 97% vs 38% on clustering) reasonably attributable to the data-generation change the paper is proposing.

The GPT-4o comparisons are the weaker part of the evidence, for three specific, related reasons. First, GPT-4o was shown a worked example and given corrective feedback "until it correctly understands the task" before being tested, while the embedding models' calibration (the mistake-detection threshold) comes from a fixed training-set statistic with no comparable test-adjacent tuning; this is an asymmetry in how much task-specific adaptation each system received immediately before scoring. Second, the mistake-detection comparison against GPT-4o uses a subsample of only 322 steps with 50 mistakes, roughly 1.7% of the full 18,462-step test set used for the embedding models, and no confidence interval is reported for GPT-4o's precision/recall/F1 despite this small base rate of positive cases — a meaningfully less statistically powered comparison than the embedding-model results it sits beside in the same table. Third, the exact prompting protocol given to GPT-4o (whether chain-of-thought reasoning was elicited, how many worked examples were shown, whether the model saw the full derivation context or only consecutive step pairs) is not fully specified in this extract, which limits how precisely the comparison's fairness can be assessed. None of this means the qualitative conclusion (small, specialized embeddings beat a general-purpose LLM at this narrow symbolic-equivalence task) is wrong — it is a reasonable and unsurprising result given the task's structure — but the specific magnitude of GPT-4o's reported shortfall should be read with the small-sample and coaching caveats in mind rather than taken as a precise, low-variance estimate.

A further point worth naming precisely: the paper's "mistake detection" task is described as out-of-distribution, but the underlying expressions used to build its derivations are still drawn from the E-Gen corpus itself ("step-by-step mathematical derivations are generated for each expression in the E-Gen corpus"). The out-of-distribution claim is accurate with respect to task format (derivation-error classification versus equivalence clustering/retrieval) but not with respect to the underlying expression distribution or notation, which remains the same synthetic, template-and-rule-generated domain used for training. This narrows, without invalidating, how far the generalization claim should be read: it is evidence the embeddings transfer across task formats within this synthetic domain, not evidence they transfer to genuinely novel mathematical content or real-world notation, a gap the authors' own Limitations section acknowledges in different terms (extending to real-world corpora like ArXMLiv and ARQMath is listed as future work).

What remains well supported after these caveats: e-graph-based corpus generation produces measurably richer training signal than a prior SymPy-based approach on the same architecture and evaluation suite, and small, task-specific embedding models trained on that signal outperform a general-purpose frontier LLM on narrow symbolic-equivalence and error-detection tasks within the paper's synthetic domain. Whether this specific implementation (this operator set, this rule set, this test distribution) generalizes to messier, real-world mathematical notation of the kind that appears in scientific papers is not yet demonstrated by this paper's own evidence.

## Relevance to us

This paper is a concrete, mostly well-controlled existence proof for our B03 bet (math-function embeddings for retrieval, comparison, context): a small, purpose-built transformer encoder trained on systematically-generated equivalence data outperforms a frontier general-purpose LLM at recognizing when two differently-written expressions mean the same thing, and at flagging erroneous steps in a derivation, using only a cheap, deterministic cosine-similarity check rather than any LLM judgment. The mistake-detection mechanism specifically — a fixed similarity threshold calibrated once from correct-step statistics, applied step-by-step through a derivation — is a low-cost, non-LLM-judge verification building block directly relevant to our PVRE-line interest in deterministic step checking (VERIFICATION.md); it is worth remembering as a candidate cheap first-pass filter (flagging candidate error locations for a more expensive check to examine) rather than a complete verifier, since it is evaluated here only on clean synthetic symbolic-calculus derivations, not on physics derivations carrying units, dimensional structure, or physical assumptions.

The corpus-generation method itself (e-graph saturation over a rule set, producing large equivalence clusters rather than single simplified forms) is a transferable data-engineering technique worth considering if we ever build a physics-specific analogue of B03/B04: the paper's own before/after comparison suggests that the size and diversity of equivalence clusters, more than the embedding architecture, was the dominant factor behind its accuracy gains, which argues for investing generation effort in maximizing rewrite diversity per seed expression rather than assuming a better encoder alone would close the gap. The caveat that this paper's "out-of-distribution" evaluation stays within its own synthetic expression distribution is directly relevant to how we would need to validate an analogous physics tool: genuine generalization to real derivations from papers or textbooks, not just a different task format over the same synthetic rule set, would need to be demonstrated before trusting this class of method for physics verification.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| e-graph-generated cluster corpus | SymPy-generated pairwise equivalence dataset | improves | 0.85 | papers/canonical/2026-05-06/25egen.md:L315 | Same downstream architecture reaches 97% vs 38% clustering accuracy depending only on training corpus |
| cosine-similarity threshold mistake detector | GPT-4o prompted mistake detection | improves | 0.6 | papers/canonical/2026-05-06/25egen.md:L427 | 77-78% vs 61.1% F1 on the mistake class, but GPT-4o evaluated on a much smaller, uncalibrated-comparison subsample |
| seq2seq embedding trained on E-Gen | GPT-4o embedding-algebra reasoning | improves | 0.55 | papers/canonical/2026-05-06/25egen.md:L433 | 70.4% vs 39.6% accuracy; GPT-4o's exact prompting/reasoning protocol not fully specified |
| large equivalence cluster size | semantic-vs-syntactic discrimination accuracy | improves | 0.75 | papers/canonical/2026-05-06/25egen.md:L338 | E-Gen-trained models reach 48-76% vs 28.6% for the prior pairwise-only SEMEMB corpus |
