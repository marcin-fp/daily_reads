---
schema_version: 1
paper: slug:23ppi
title: "Prediction-powered inference"
authors:
  - Anastasios N. Angelopoulos
  - Stephen Bates
  - Clara Fannjiang
  - Michael I. Jordan
  - Tijana Zrnic
publication:
  first_public_date: "2023-01-23"
  first_public_date_precision: day
  venue: Science
  status: journal
  reviewed_version: published
  reviewed_version_date: null
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-05-06/23ppi.md
raw: papers/raw/2026-05-06/23ppi-pdf.md
source_url: https://doi.org/10.1126/science.adi6000
organizations:
  - name: Department of Electrical Engineering and Computer Sciences, University of California, Berkeley
    sector: academia
    roles: [author_affiliation]
    authors: [Anastasios N. Angelopoulos, Stephen Bates, Clara Fannjiang, Michael I. Jordan, Tijana Zrnic]
    grants: []
  - name: Office of Naval Research
    sector: government
    roles: [funder]
    authors: [Michael I. Jordan]
    grants: ["N00014-21-1-2840"]
  - name: National Science Foundation
    sector: government
    roles: [funder]
    authors: [Anastasios N. Angelopoulos, Clara Fannjiang]
    grants: ["NSF Graduate Research Fellowship"]
artifacts:
  - type: code
    url: https://doi.org/10.5281/zenodo.8403931
  - type: data
    url: https://doi.org/10.5281/zenodo.8397451
facets:
  domains: [statistics, machine-learning, applied-science]
  paper_type: [method, theory, experiment]
  methods: [confidence-interval-construction, semi-supervised-inference, m-estimation, rectifier-correction]
  models: [AlphaFold, ResNet, gradient-boosted-trees, transformer-promoter-model]
  benchmarks: []
assessment:
  extract_quality: good
  extract_limitations: [figures-not-visually-assessed]
  critical_flags: []
metadata_notes: "First posted as arXiv:2301.09633 (submitted 2023-01-23); the Science version reviewed here was received 2023-05-07 and accepted 2023-10-05 per the article footer, published as Science 382, 669 (2023), DOI 10.1126/science.adi6000. The exact online-publication day for the Science version is not stated in the extract, so reviewed_version_date is left unset rather than guessed. This review is based on the main text and the excerpted portion of the Supplementary Materials covering the baseline comparisons and the 'Cases Where Prediction-Powered Inference is Underpowered' section; the full mathematical proofs and additional supplementary figures (S1-S6) were not read in full."
---

Citation: Angelopoulos, A. N., Bates, S., Fannjiang, C., Jordan, M. I., and Zrnic, T. Prediction-powered inference. Science 382, 669-674 (2023). https://doi.org/10.1126/science.adi6000

## What this paper is about

Scientists increasingly have access to two very different kinds of data: a small amount of gold-standard, expensively measured ground truth, and a large amount of cheap machine-learning predictions about the same kind of quantity. Naively trusting the predictions ("imputation") can silently produce wrong conclusions if the model is biased; ignoring the predictions and using only the gold-standard data ("classical" inference) is safe but wastes most of the available information. This paper introduces prediction-powered inference (PPI), a statistical recipe for combining the two that is provably guaranteed to give a valid confidence interval or p-value no matter how good or bad the machine-learning model is, while typically being narrower (more informative) than using the gold-standard data alone whenever the model is reasonably accurate and the pool of unlabeled, model-predicted data is large.

## Extended summary

The setup: a scientist wants a confidence interval for some estimand q (a mean, a median, a quantile, or a linear/logistic regression coefficient). They have a small labeled ("gold-standard") dataset of features and true outcomes, a much larger unlabeled dataset of features only, and predictions from a machine-learning model for both datasets. PPI proceeds in three steps. First, choose the estimand. Second, define a "measure of fit" (how consistent a candidate value of the estimand is with the imputed, model-predicted unlabeled data) and a "rectifier" — the difference between that same measure of fit computed on the labeled data using true outcomes versus using the model's predictions on that same labeled data. The rectifier is exactly zero if the model's predictions are perfect, and otherwise captures the model's bias for the quantity of interest. Third, combine the measure of fit (computed on the large imputed unlabeled set) with the rectifier (computed on the small labeled set) to construct the confidence interval; the paper proves this interval contains the true estimand with the target probability (e.g. 95%) for any machine-learning algorithm and any underlying data distribution, given only standard random-sampling assumptions. The same construction extends to a general "master protocol" for any estimand expressible as the minimizer of a convex objective, covering the specific cases (mean, median, quantile, OLS, logistic regression) as special instances, and further extends to two specific forms of distribution shift between the labeled and unlabeled data (covariate shift and label shift), with correspondingly adapted procedures and their own validity guarantees.

Seven real-data case studies (Fig. 2, rows A-G) demonstrate the method: (A) estimating the odds ratio between AlphaFold-predicted intrinsically disordered protein regions and post-translational modifications (10,803 gold-standard points; PPI required 316 labels to reject a null hypothesis at 95% confidence versus 799 for the classical approach); (B) estimating the fraction of Sloan Digital Sky Survey galaxies with spiral arms using Galaxy Zoo 2 citizen-science labels (1,364,122 points; 189 vs. 449 labels needed); (C) estimating quantiles of gene expression driven by yeast promoter sequences, using predictions from a transformer model from Vaishnav et al. (61,150 points; 764 vs. 900 labels); (D) estimating Amazon deforestation extent from satellite-imagery-based predictions against scarce field-visit labels (1,596 points; 21 vs. 35 labels); (E) estimating a logistic regression coefficient for income's effect on private health insurance uptake using US Census (Folktables) data and a gradient-boosted-tree predictor (378,817 points; 5,569 vs. 6,653 labels); (F) the same census data under an introduced covariate shift (reweighted sampling by sex), estimating an OLS coefficient for age's effect on income using the covariate-shift-robust variant (177 vs. 282 labels); and (G) counting plankton from a submersible flow-cytometry system across a year with a label-shift-robust variant, a case with no valid classical comparator since the classical approach does not apply under the label shift present in this dataset. Across all seven studies, the naive imputation approach failed to produce a confidence interval that covered the true (independently known, since all labels were actually available for evaluation purposes) value of the estimand, while both PPI and the classical approach were valid, with PPI consistently requiring substantially fewer gold-standard labels to reach the same statistical conclusion.

The Supplementary Materials report a further comparison against three existing baseline procedures for combining labeled and unlabeled data: post-prediction inference (Wang et al., 2020), which the authors state lacks a general theoretical guarantee and, in their tests, failed to achieve valid coverage under realistic conditions; semi-supervised mean estimation (Zhang and Bradic, 2022), whose formal guarantees are restricted to cross-fitted linear models and which the authors report provided little practical improvement over the classical interval in their experiments because of limited achievable variance reduction with linear models; and a conformal-prediction-based mean-estimation procedure, which is valid for arbitrary models and distributions but, in the authors' experiments, was extremely conservative, in some cases producing infinite-width intervals even without a Bonferroni correction. The paper explicitly and separately proves and empirically demonstrates (in the SM section "Cases Where Prediction-Powered Inference is Underpowered") that PPI provides no advantage over the classical approach when the machine-learning model is not accurate enough or when the unlabeled dataset is not sufficiently large relative to the labeled dataset — a limitation the main text states plainly rather than only in supplementary material. The Conclusions section separately flags handling more general (non-covariate/non-label) forms of distribution shift as open future work.

## Learnings

Separating "validity" from "power" is the paper's central methodological move, and it is a genuinely reusable framing beyond this specific statistical construction: a "rectifier," computed as the difference between a measure of fit evaluated on the small gold-standard sample using true outcomes versus using the machine-learning model's own predictions on that same sample, isolates exactly the model's bias for the population quantity of interest, and correcting for that bias (rather than trusting the model's raw predictions, or discarding them) is what lets an arbitrarily imperfect model still contribute information without threatening the validity of the final conclusion.

A single "master protocol" — any estimand expressible as the minimizer of a convex objective — subsumes what would otherwise be a family of special-cased tricks (one for means, one for quantiles, one for regression coefficients) into one general recipe with one proof of validity, which is a reusable pattern for building a broadly applicable statistical or verification tool: find the right general mathematical structure the target quantities share, prove the guarantee once at that level of generality, and let the specific cases fall out as instances rather than proving each separately.

A methods paper proactively proving and empirically demonstrating the specific conditions under which its own proposed method provides no benefit over the naive baseline (here: an inaccurate model, or too little unlabeled data relative to labeled data) is a disciplined and comparatively rare practice worth treating as a norm rather than an exception; it directly tells a prospective user when not to bother with the more complex method, which is more useful than a paper that reports only favorable comparisons.

## Verification

This paper's entire content is a verification framework in the sense our own standing interest tracks, applied to statistical estimation rather than to a physics derivation: the object being checked is whether a machine-learning system's predictions, in aggregate over a population, are biased for a specific quantity of interest, and the checking mechanism is a small gold-standard sample used to compute a "rectifier" that measures and corrects for that bias. Critically, the verdict-issuing mechanism is not a learned judge (LLM or otherwise) but a closed-form or convex-optimization-based statistical procedure with a formal, mathematically proven coverage guarantee (95% by construction, for any underlying data distribution and any machine-learning algorithm, given standard random-sampling assumptions) — the strongest form of verification this corpus has reviewed to date, since it is a proof rather than an empirical estimate of reliability. Coverage versus precision is the paper's explicit, central subject: validity (coverage) is unconditional on model quality, while precision (interval width, statistical power) depends on how accurate the model is and how much unlabeled data is available, and the paper proves and demonstrates the specific regime (weak model, small unlabeled pool) where precision gains vanish and PPI reduces to no better than the classical, labels-only approach. Two specific forms of a "the world's population is drifting" check (covariate shift, label shift) are handled with their own adapted procedures and guarantees, though the paper is explicit that more general or compound forms of distribution shift are not yet covered.

## Field context

The paper positions itself carefully against several distinct lines of prior work on combining labeled and unlabeled data: semi-supervised and high-dimensional estimation methods (cited broadly, e.g. Pepe 1992; Lafferty and Wasserman 2007; Zhang, Brown, and Cai 2019; Chakrabortty and collaborators; Zhang and Bradic 2022), which the authors say focus on efficiency in specific (often linear or low-dimensional) regimes rather than providing a general, assumption-light recipe for arbitrary convex-objective estimands; "post-prediction inference" (Wang, McCormick, and Leek, 2020), the most thematically similar prior method, which the authors argue lacks general validity guarantees and is shown, in this paper's own tests, to fail to cover under realistic conditions; and conformal prediction (Vovk, Gammerman, and Shafer), which the authors carefully distinguish on the grounds that it targets a per-instance prediction set for a single test point, not a population-level parameter such as a mean, and is mathematically a different tool applied to a different question, despite superficial similarity (both use a labeled dataset and a predictive model). None of these specific precedents are yet reviewed in this corpus. Separately, and not something this paper itself could report, a search for how this work has been received afterward found a substantial body of later papers extending it directly (works on statistical power analysis for PPI, generalizations to broader estimand classes and binary classifier evaluation, connections back to classical survey-sampling theory as a "difference estimator," and applications to AI evaluation and social science research), consistent with this paper having become a foundational reference point for combining ML predictions with scarce ground truth rather than a one-off result — noted here as an observation from this review's own search, not a claim the paper makes about itself.

## Critical discussion

As a work of statistical methodology backed by a formal proof of its central validity claim, this paper should be judged first on whether its assumptions match its demonstrations, and on that count it holds up well: the core guarantee requires only that the labeled and unlabeled datasets be randomly sampled from a common population, a standard and disclosed assumption, and the paper is explicit about the two specific, named forms of distribution shift it additionally handles (covariate shift, label shift) rather than implying it solves the general shift problem — the Conclusions section states plainly that more general or compound shifts remain open. This kind of honest scoping is exactly what should be expected of a methods paper and is worth crediting rather than treating as a gap to penalize.

The empirical demonstrations are genuinely diverse (seven case studies spanning proteomics, astronomy, genomics, remote sensing, two distinct census/econometrics applications, and ecology) and, unusually for this corpus, include real quantitative baseline comparisons against three specific competing methods (post-prediction inference, semi-supervised mean estimation, conformal-prediction-based intervals) run by the authors themselves rather than only cited, with each baseline's specific failure mode reported (no coverage guarantee and observed non-coverage; effectively no power gain; extreme, sometimes-infinite conservatism). This is a stronger standard of related-work engagement than most of the ML-agent papers reviewed elsewhere in this corpus.

One asymmetry worth naming precisely: of the seven case studies, six (A-F) include a full three-way comparison against both the classical and imputation baselines, while the seventh (G, plankton counting under label shift) has, by the paper's own statement, "no classical counterpart... because the data are collected under distribution shift," so its evidentiary contribution is narrower — it shows PPI covers the ground truth and imputation does not, but cannot show the labels-saved advantage over classical inference that anchors the paper's central practical pitch in the other six studies. This does not undermine the paper's claims about that case, but it means the label-shift demonstration is evidentially thinner than the others.

What remains fully supported: the central validity claim is a mathematical theorem, not an empirical estimate, so it does not carry the usual replication uncertainty of an empirical result; the claim that PPI is typically more informative (narrower intervals, fewer labels needed) than classical inference when the underlying model is reasonably good and unlabeled data is abundant is both proven in the relevant regime and demonstrated across six diverse real datasets with a real statistical comparator; and the claim that this advantage disappears with a weak model or too little unlabeled data is itself proven and empirically shown by the authors, not merely asserted as a caveat.

## Relevance to us

This paper is directly relevant to a specific, recurring shape of problem in our own verification interests: we often have (or could have) a large corpus of AI-generated or AI-scored physics claims, derivations, or property predictions, alongside a much smaller set of exactly-verified ground truth (solved analytically, cross-checked by a deterministic solver, or hand-verified). Prediction-powered inference is a rigorous, off-the-shelf recipe for exactly this situation: it gives a way to report a population-level quantity (for example, "the fraction of our verifier's flagged errors that are real" or "the average discrepancy between our physics-attuned backbone's predicted quantity and the true value") with a formally valid confidence interval that is honest about how little of the corpus was actually gold-standard-checked, rather than either trusting the AI-graded numbers wholesale (the "imputation" failure mode this paper repeatedly demonstrates) or discarding all the AI-graded data and reporting only on the tiny hand-checked subset. This maps directly onto our own stated preference (per our verification interest) for reporting error with explicit provenance and appropriately wide bounds rather than a single overconfident number, and it is a concrete, usable tool rather than only a philosophical alignment — if we ever need to report a calibrated estimate of a physics-native verifier's or backbone's true accuracy at scale, using a small hand-verified sample to correct a much larger AI-scored sample, this is the method to reach for rather than reinventing an ad hoc correction.

The paper's own discipline — proving and demonstrating exactly when its method does not help (a weak model, or too little unlabeled data relative to labeled data) — is also a template worth holding our own verification and evaluation write-ups to: stating the conditions under which a proposed check or metric provides no real benefit over a simpler baseline, rather than only reporting favorable comparisons, is the standard this paper meets and one we should aim to meet when reporting on our own physics-native verification mechanisms.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| prediction-powered confidence intervals | nominal coverage of the true estimand | implies | 0.9 | papers/canonical/2026-05-06/23ppi.md:L43 | Mathematically proven (Theorem S1) for any machine-learning algorithm and data distribution under standard sampling assumptions |
| imputation approach using raw ML predictions | valid confidence interval coverage | contradicts | 0.85 | papers/canonical/2026-05-06/23ppi.md:L95 | Imputation failed to cover the true estimand in every one of the seven real-data case studies reported |
| prediction-powered inference | classical labels-only inference statistical power | improves | 0.85 | papers/canonical/2026-05-06/23ppi.md:L117 | Consistently smaller confidence intervals and fewer labels needed to reject the null across six case studies with a classical comparator |
| prediction-powered inference | post-prediction inference (Wang et al. 2020) | improves | 0.6 | papers/canonical/2026-05-06/23ppi.md:L325 | Own SM comparison: baseline lacks a general validity guarantee and failed to cover under realistic tested conditions |
