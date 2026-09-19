---
schema_version: 1
paper: slug:24semant
title: "Detecting hallucinations in large language models using semantic entropy"
authors:
  - Sebastian Farquhar
  - Jannik Kossen
  - Lorenz Kuhn
  - Yarin Gal
publication:
  first_public_date: "2024-06-19"
  first_public_date_precision: day
  venue: "Nature"
  status: journal
  reviewed_version: null
  reviewed_version_date: "2024-06-19"
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-06-09/24semant.md
raw: papers/raw/2026-06-09/24semant-pdf.md
source_url: https://doi.org/10.1038/s41586-024-07421-0
organizations:
  - name: University of Oxford
    sector: academia
    roles: [author_affiliation]
    authors: [Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, Yarin Gal]
    grants: []
  - name: UK Research and Innovation
    sector: government
    roles: [funder]
    authors: [Yarin Gal]
    grants: ["EP/V030302/1"]
  - name: The Alan Turing Institute
    sector: nonprofit
    roles: [funder]
    authors: [Yarin Gal]
    grants: []
artifacts:
  - type: code
    url: https://github.com/jlko/semantic_uncertainty
  - type: code
    url: https://github.com/jlko/long_hallucinations
  - type: data
    url: https://github.com/jlko/long_hallucinations
facets:
  domains: [machine-learning, natural-language-processing]
  paper_type: [method, experiment]
  methods: [semantic-entropy, bidirectional-entailment-clustering, llm-as-judge, p-true, embedding-regression]
  models: [LLaMA-2-Chat, Falcon-Instruct, Mistral-7B-Instruct, GPT-4, GPT-3.5]
  benchmarks: [TriviaQA, SQuAD, BioASQ, NQ-Open, SVAMP, FactualBio]
assessment:
  extract_quality: partial
  extract_limitations: [figures-not-visually-assessed, equations-damaged]
  critical_flags: [narrow-evaluation, missing-uncertainty]
metadata_notes: "Received 2023-07-17, accepted 2024-04-12, published online 2024-06-19 (Open Access); first_public_date uses the online-publication date since no separate preprint is referenced in the text. The Competing interests statement notes S. Farquhar is now at Google DeepMind and L. Kuhn at OpenAI, but states the paper was written under their University of Oxford affiliation; per the no-inference policy, no organization entry is created for those current employers since the work itself is not attributed to them. Funding is stated only for Y. Gal (a Turing AI Fellowship via UKRI, delivered by the Alan Turing Institute); no funding is stated for the other three authors. Equations in the extracted Methods section are visibly mangled by PDF-to-text conversion; the prose description of the entropy estimator and its discrete variant was used instead of relying on the damaged formula rendering."
---

Citation: Farquhar, S., Kossen, J., Kuhn, L., and Gal, Y. Detecting hallucinations in large language models using semantic entropy. Nature 630, 625–630 (2024).

## What this paper is about

Language models sometimes state wrong things fluently and confidently. This paper targets a specific slice of that problem: "confabulations," meaning answers that are not just wrong but arbitrary, in the sense that a different random seed could have produced a different, equally confident answer. The authors propose detecting confabulations by measuring uncertainty over the meaning of a model's answers rather than over their exact wording, since a model can express one stable idea in many different sentences. Their method, semantic entropy, requires no labeled training data and no knowledge of the task in advance, and it improves question-answering accuracy simply by letting a system decline to answer the questions it is most likely to confabulate on.

## Extended summary

The method proceeds in three steps. First, sample several answers (M generations, temperature 1, nucleus and top-K sampling) from the model for a given question. Second, cluster those answers into groups that mean the same thing, using bidirectional entailment: two answers are considered semantically equivalent if each entails the other, checked either with an instruction-tuned LLM (the authors settle on GPT-3.5-Turbo after evaluating alternatives) or with a lightweight fine-tuned entailment model (DeBERTa-large-MNLI, 1.5B parameters). Third, estimate the entropy of the resulting distribution over meaning-clusters rather than over token sequences. When token probabilities are unavailable, a "discrete" variant approximates cluster probabilities from the fraction of sampled generations landing in each cluster instead, which the authors needed for GPT-4 experiments since GPT-4 did not expose output probabilities at the time of writing.

The main evaluation covers five free-form question-answering and math datasets (TriviaQA, SQuAD 1.1, BioASQ, NQ-Open, SVAMP), each sampled to 400 train and 400 test examples, with context passages deliberately withheld to make the tasks hard enough to induce confabulations (accuracy is otherwise too high to study the phenomenon). Models tested are LLaMA 2 Chat (7B, 13B, 70B), Falcon Instruct (7B, 40B), and Mistral 7B Instruct, giving 30 model-dataset combinations. Two metrics are used: AUROC for predicting whether a given answer is wrong, and a new metric, AURAC, the area under the curve of "rejection accuracy" (the accuracy of the model's remaining answers as increasingly many high-uncertainty questions are refused). Ground truth for whether a generated sentence-length answer is correct is established automatically by prompting GPT-4 to judge semantic match against the reference answer, a choice justified by the poor fit of exact-match scoring to long free-form answers and checked, per the authors, against human judgment in the supplementary material (not detailed in the extracted main text). Averaged across all 30 combinations, semantic entropy reaches an AUROC of 0.790, its discrete (probability-free) variant performs similarly, and both outperform naive token-level entropy (0.691), the P(True) self-report baseline (Kadavath et al., 2022; 0.698), and a supervised embedding-regression classifier trained on the model's final hidden states (0.687 in-distribution, worse out-of-distribution). Semantic entropy's AUROC stays in a comparatively tight 0.78-0.81 band across all three model families and scales tested, while P(True) is reported to improve with model scale without closing the gap. Table 1 walks through four qualitative examples: one where naive entropy is misled by lexical variation that semantic entropy correctly treats as one meaning, one where both methods agree an answer is a confabulation, one where both agree it is not, and one explicit failure case where semantic entropy's clustering was "erroneously high" because it separated a specific-date answer from an equivalent year-only answer.

A second experiment extends the method to paragraph-length text using a new dataset, FactualBio: 21 GPT-4-generated biographies of moderately notable individuals, decomposed into 150 individually human-labeled factual claims (45 incorrect). Because directly resampling whole sentences conflates uncertainty about content with unrelated variation in narrative structure, the authors instead decompose each biography into factual claims, auto-generate clarifying questions that each claim might answer, resample three new answers per question (six questions per claim, using two rounds of three), and average the discrete semantic entropy over those questions. Discrete semantic entropy is compared against a simple GPT-4 "self-check" baseline (asking the model directly whether a statement is likely true) and an adapted, Monte Carlo-estimated P(True) variant, and it outperforms both on AUROC and AURAC, with P(True) gaining only a narrow edge in rejection accuracy once the most uncertain 20% of claims have already been excluded.

## Learnings

Clustering generations by whether they entail each other, rather than treating every distinct token sequence as a separate outcome, removes the specific confound where multiple correct phrasings of one answer inflate naive uncertainty estimates. This lets an unsupervised, no-training entropy measure outperform both a classifier trained on the model's own hidden states and an in-context "ask the model how confident it is" baseline, without needing any labeled confabulation examples to get there.

A supervised hallucination-detection classifier trained on model hidden states (embedding regression here) performs well in-distribution but degrades once it is deployed on a dataset different from the one it was trained on, which is precisely the situation in which reliable uncertainty matters most; any claim of a hallucination detector's generality should be checked specifically against this off-distribution case, not only against in-distribution accuracy.

Asking a model to self-report whether its own answer is likely true (P(True)) gets closer to the performance of an externally computed, meaning-level entropy measure as model scale increases, but even the largest models tested here (up to 70B) still trail it; scale narrows the gap between what a model can articulate about its own uncertainty and what an external statistical measure extracts from the same set of generations, but does not close it.

## Verification

This paper is centrally about verification in the sense of estimating, without ground truth at inference time, whether a generated claim is likely to be reliable. The check is a statistical one, not a deterministic or symbolic oracle: it resamples answers, clusters them by meaning via a separate entailment model, and reports the entropy of that meaning distribution as the uncertainty signal, so the "verdict" is a graded score rather than a pass/fail label, and no abstention criterion is fixed a priori (the AURAC metric instead sweeps over rejection thresholds). Coverage is a stated strength: the method needs no task-specific training data and no prior knowledge of the domain, in explicit contrast to the supervised embedding-regression baseline, which needs matched-distribution training data to perform well. Precision is reported at 0.790 average AUROC across 30 model-dataset combinations, held in an unusually stable 0.78-0.81 band across three different model families and parameter scales from 7B to 70B, though the paper does not report per-combination confidence intervals, resting the generalization claim on cross-combination consistency rather than statistical uncertainty bounds. Ground truth for correctness itself is judged automatically by GPT-4 for the sentence-length experiments (validated against human raters per the paper's own statement, though the agreement figures are in supplementary material not present in the extracted text) and by direct human labeling for the 150 FactualBio claims. The paper draws an explicit, disciplined scope boundary around what its check does and does not cover: it is designed to catch confabulations specifically, defined as arbitrary and seed-sensitive errors, and the authors explicitly state it does not address hallucinations from other mechanisms, such as models being consistently wrong because of erroneous training data, or being confidently misleading by design.

## Field context

This work formalizes and substantially extends the same group's earlier "semantic uncertainty" idea (Kuhn, Gal, and colleagues, cited in the paper's own references) into a broader, more heavily validated confabulation-detection method, and it is one of the most widely cited demonstrations that meaning-level rather than token-level uncertainty estimation is a practical route to hallucination detection in free-form generation. It explicitly positions itself against P(True) (Kadavath et al., 2022, "Language models (mostly) know what they know") as its main in-context self-knowledge baseline and against supervised classifier probes as its main trained baseline, arguing in the Discussion that its results suggest models are, in a specific sense, better at "knowing what they don't know" than the P(True) framing implied, since an external statistical measure over the same generations extracts more signal than the model's own verbalized confidence does. Within this corpus, it sits alongside the review of 24selfcor and 2604.27251 as another instance of the recurring finding that a model's own self-report (whether about correctness after self-correction, about reasoning-type compliance, or about answer confidence) is a weaker signal than an externally grounded check computed from the model's behavior rather than solicited from its self-description. The paper's own Discussion also draws a direct, explicit line toward AI-safety-via-debate and scalable oversight, framing meaning-level cross-examination as a natural extension of the same idea to adversarial or multi-turn settings.

## Critical discussion

The central comparison, semantic entropy against naive token-level entropy on the same generations, is a clean ablation that isolates exactly the mechanism the paper claims matters (clustering by meaning rather than counting distinct strings), and the result is replicated across three model families spanning a 10x parameter range and five separate datasets, with AUROC staying inside a tight 0.78-0.81 band throughout. That breadth and stability is a genuine strength for an unsupervised method making a generalization claim.

Several aspects of the evaluation design are worth naming plainly rather than taken at face value from the headline numbers. Context passages are withheld from every one of the five QA datasets specifically to induce confabulations, a disclosed and reasoned choice (accuracy is otherwise too high to study the phenomenon) but one that means the reported detection numbers describe a closed-book regime deliberately made harder than a retrieval-augmented deployment would be, so the AUROC/AURAC figures should be read as characterizing detection performance under induced difficulty rather than under typical production conditions. The paper explicitly declines to report standard errors on its headline averaged AUROC and AURAC values, reasoning that consistency of the ranking across datasets is a stronger signal here than per-run variance; that is a defensible, stated methodological position, but it leaves no way for the reader to judge whether the narrower gaps in the comparison, for instance P(True) at 0.698 against embedding regression at 0.687, are meaningfully different from sampling noise. The FactualBio extension to paragraph-length text is considerably narrower than the main result: 21 individuals, 150 hand-labeled claims, a single generator model (GPT-4), and a multi-step LLM-mediated pipeline (claim decomposition, question generation, resampling) whose own error the authors candidly flag as "the main source of errors in the procedure," since the auto-generated clarifying questions are not always well targeted. This is a genuine limitation of the more ambitious extension that the authors state themselves rather than one uncovered by scrutiny, and it means the paragraph-length result should be read as a promising proof of concept on one model and one small hand-labeled dataset rather than as generalization evidence on the same footing as the five-dataset sentence-length result. Table 1's fourth example is a useful, self-reported failure case in its own right: the clustering step's notion of "same meaning" is itself a modeling choice (here, treating a specific date and an equivalent year-only answer as different clusters) that can misfire relative to what a reader would actually consider the same answer in context.

What remains well supported after these caveats: across a genuinely broad sweep of models, scales, and datasets, computing entropy over clustered meaning rather than raw token sequences captures a real and previously underexploited signal for confabulation, reliably beating a naive entropy baseline and two supervised or in-context alternatives without any labeled training data, and the authors are explicit and disciplined about the boundary of what the method claims to detect, rather than overselling it as a general hallucination fix.

## Relevance to us

This connects directly to the uncertainty-engine strand of our verification programme: a coverage-general, training-free signal for "how much does this vary across resampling, at the level of meaning rather than surface form" is a concrete instance of the kind of typed uncertainty (random vs. structural, rather than a single opaque confidence number) that future users have asked for. A physics derivation can likewise be phrased many equivalent ways (different but algebraically identical rearrangements, different unit conventions, different variable names) without being unstable in the sense that matters, so an analogous "cluster by content equivalence, not surface form, before measuring variability" strategy is a plausible template for distinguishing a genuinely underdetermined or confabulated derivation step from harmless notational variation. The equivalence relation itself would need to change, however: natural-language bidirectional entailment is a soft, model-judged relation, whereas physics offers harder, checkable equivalence criteria (dimensional consistency, algebraic identity under substitution, numerical agreement within tolerance), so a physics-native version of this method would likely replace the entailment-clustering step with a deterministic or symbolic equivalence check rather than reuse an LLM or NLI model to decide what counts as "the same derivation." The paper's finding that self-reported confidence (P(True)) trails an externally computed signal even as models scale reinforces our existing design instinct, echoed in VERIFICATION.md, that a model's own verbalized confidence should not be the primary trust signal in a verification stack; resampling-and-cluster approaches are one concrete mechanism worth prototyping for separating physically meaningful entropy (a genuinely underdetermined regime or assumption) from confabulation-like instability in a derivation.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| clustering generations by bidirectional entailment before entropy | confabulation detection AUROC versus naive token entropy | improves | 0.85 | papers/canonical/2026-06-09/24semant.md:L108 | Semantic entropy averages 0.790 AUROC versus 0.691 for naive entropy across 30 model-dataset combinations |
| semantic entropy | out of distribution embedding regression baseline | improves | 0.75 | papers/canonical/2026-06-09/24semant.md:L107 | Embedding regression degrades under distribution shift while semantic entropy does not rely on matched training data |
| semantic entropy | p true self knowledge baseline | improves | 0.7 | papers/canonical/2026-06-09/24semant.md:L108 | Semantic entropy reaches 0.790 AUROC against 0.698 for P(True), which trails even as it improves with model scale |
| discrete semantic entropy on biographies | GPT-4 self check and p true baselines | improves | 0.7 | papers/canonical/2026-06-09/24semant.md:L185 | Discrete semantic entropy exceeds both baselines on AUROC and AURAC for FactualBio claim detection |
