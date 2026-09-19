---
schema_version: 1
paper: slug:26scales
title: "General scales unlock AI evaluation with explanatory and predictive power"
authors:
  - Lexin Zhou
  - Lorenzo Pacchiardi
  - Fernando Martínez-Plumed
  - Katherine M. Collins
  - Yael Moros-Daval
  - Seraphina Zhang
  - Qinlin Zhao
  - Yitian Huang
  - Luning Sun
  - Jonathan E. Prunty
  - Zongqian Li
  - Pablo Sánchez-García
  - Kexin Jiang-Chen
  - Pablo A. M. Casares
  - Jiyun Zu
  - John Burden
  - Behzad Mehrbakhsh
  - David Stillwell
  - Manuel Cebrian
  - Jindong Wang
  - Peter Henderson
  - Sherry Tongshuang Wu
  - Patrick C. Kyllonen
  - Lucy Cheke
  - Xing Xie
  - José Hernández-Orallo
publication:
  first_public_date: "2026-04-01"
  first_public_date_precision: day
  venue: Nature
  status: journal
  reviewed_version: published
  reviewed_version_date: "2026-04-01"
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-05-06/26scales.md
raw: papers/raw/2026-05-06/26scales-pdf.md
source_url: https://doi.org/10.1038/s41586-026-10303-2
organizations:
  - name: Princeton University
    sector: academia
    roles: [author_affiliation]
    authors: [Lexin Zhou, Peter Henderson]
    grants: []
  - name: Leverhulme Centre for the Future of Intelligence, University of Cambridge
    sector: academia
    roles: [author_affiliation]
    authors: [Lexin Zhou, Lorenzo Pacchiardi, Seraphina Zhang, Jonathan E. Prunty, John Burden, Lucy Cheke, José Hernández-Orallo]
    grants: []
  - name: Microsoft Research Asia
    sector: industry
    roles: [author_affiliation]
    authors: [Lexin Zhou, Qinlin Zhao, Yitian Huang, Xing Xie]
    grants: []
  - name: Valencian Research Institute for Artificial Intelligence (VRAIN), Universitat Politècnica de València
    sector: academia
    roles: [author_affiliation]
    authors: [Lexin Zhou, Fernando Martínez-Plumed, Yael Moros-Daval, Kexin Jiang-Chen, Pablo A. M. Casares, Behzad Mehrbakhsh, José Hernández-Orallo]
    grants: []
  - name: Department of Engineering, University of Cambridge
    sector: academia
    roles: [author_affiliation]
    authors: [Katherine M. Collins]
    grants: []
  - name: Department of Psychology, University of Cambridge
    sector: academia
    roles: [author_affiliation]
    authors: [Seraphina Zhang, Lucy Cheke]
    grants: []
  - name: The Psychometrics Centre, University of Cambridge
    sector: academia
    roles: [author_affiliation]
    authors: [Luning Sun, David Stillwell]
    grants: []
  - name: Department of Theoretical and Applied Linguistics, University of Cambridge
    sector: academia
    roles: [author_affiliation]
    authors: [Zongqian Li]
    grants: []
  - name: KU Leuven
    sector: academia
    roles: [author_affiliation]
    authors: [Pablo Sánchez-García]
    grants: []
  - name: Educational Testing Service
    sector: nonprofit
    roles: [author_affiliation]
    authors: [Jiyun Zu, Patrick C. Kyllonen]
    grants: []
  - name: Center for Automation and Robotics (CAR), Spanish National Research Council (CSIC-UPM)
    sector: government
    roles: [author_affiliation, funder]
    authors: [Manuel Cebrian]
    grants: []
  - name: William & Mary
    sector: academia
    roles: [author_affiliation]
    authors: [Jindong Wang]
    grants: []
  - name: Carnegie Mellon University
    sector: academia
    roles: [author_affiliation]
    authors: [Sherry Tongshuang Wu]
    grants: []
  - name: OpenAI
    sector: industry
    roles: [funder, compute_provider]
    authors: [José Hernández-Orallo]
    grants: ["AI Progress through the Lens of Predictable AI Ecosystems"]
  - name: Microsoft
    sector: industry
    roles: [funder, compute_provider]
    authors: []
    grants: ["Accelerate Foundation Models Research (AFMR)"]
  - name: DeepSeek
    sector: industry
    roles: [collaborator]
    authors: []
    grants: []
  - name: Meta
    sector: industry
    roles: [collaborator]
    authors: []
    grants: []
  - name: Google.org (via Silicon Valley Community Foundation, to Fundación General CSIC)
    sector: industry
    roles: [funder]
    authors: [Manuel Cebrian]
    grants: []
  - name: Coefficient Giving (formerly Open Philanthropy)
    sector: nonprofit
    roles: [funder]
    authors: []
    grants: ["Long-Term Future Scholarship"]
  - name: Spanish Government (MCIN/AEI)
    sector: government
    roles: [funder]
    authors: []
    grants: ["PID2023-150271NB-C21", "PID2021-122830OB-C42 (SFERA)", "PID2024-162030OB-100 (ROBIN)"]
  - name: Generalitat Valenciana
    sector: government
    roles: [funder]
    authors: []
    grants: ["CIPROM/2022/6 (FASSLOW)", "IDIFEDER/2021/05 (CLUSTERIA)", "CIACIF/2023/276"]
  - name: European Commission
    sector: government
    roles: [funder]
    authors: []
    grants: ["H2020-EU 952215 (TAILOR)", "ERDF", "NextGenerationEU"]
artifacts:
  - type: project
    url: https://kinds-of-intelligence-cfi.github.io/ADELE
facets:
  domains: [machine-learning, ai-evaluation, psychometrics]
  paper_type: [method, benchmark, analysis]
  methods: [rubric-based-annotation, llm-as-judge, item-response-theory, random-forest-assessor, fine-tuned-llm-assessor, logistic-curve-fitting]
  models: [GPT-4o, GPT-3.5-Turbo, Babbage-002, Davinci-002, OpenAI-o1, OpenAI-o1-mini, LLaMA-3.2, LLaMA-3.1-405B-Instruct, DeepSeek-R1-Distilled-Qwen, DeepSeek-V3, Claude-3.5-Sonnet]
  benchmarks: [ADeLe, GSM8K, OlymMATH, GPQA, MMLU-Pro, SciBench, ChemLLMBench]
assessment:
  extract_quality: good
  extract_limitations: [figures-not-visually-assessed]
  critical_flags: [same-family-judge]
metadata_notes: "Nature reports Received 2025-03-29, Accepted 2026-02-19, Published online 2026-04-01; first_public_date uses the publication date since no earlier preprint is referenced in the extract. Funding and support relationships are taken verbatim from the Acknowledgements and Competing interests statements; per-author grant attribution is not always explicit, so most funder entries list no authors."
---

Citation: Zhou, L. et al. General scales unlock AI evaluation with explanatory and predictive power. Nature (2026). https://doi.org/10.1038/s41586-026-10303-2

## What this paper is about

Benchmark accuracy numbers do not travel well: a score on one dataset rarely tells you how a model will do on the next one, and different benchmarks that claim to test the same thing ("reasoning") often disagree wildly. The authors build a fixed catalogue of 18 general cognitive "demand" scales (things like quantitative reasoning, metacognition, knowledge of natural sciences) plus a scale for how guessable a question is. Using rubrics that an LLM can apply automatically, they rate 16,108 task instances from 20 benchmarks on all 18 scales, and separately estimate each of 15 LLMs' ability on each scale. Comparing a benchmark's demand profile against a model's ability profile lets them explain why a benchmark is easy or hard for a given model, and predict success on brand-new tasks and benchmarks instance by instance, including out of distribution.

## Extended summary

The method has two independent halves. The demand side: 18 "DeLeAn" rubrics (11 "elemental" cognitive capabilities, 5 domain-knowledge dimensions, 2 "extraneous" difficulty inflators — Atypicality for contamination and Volume for task amalgamation — plus a separate Unguessability control for multiple-choice-style funnelling) each score an instance from 0 to 5+. GPT-4o ("gpt-4o-0513") applies the rubrics via chain-of-thought prompting at temperature 0. Five of the authors hand-annotated 900 instances and reached Delphi consensus; agreement between humans and GPT-4o averaged rWG = 0.86 across dimensions (range 0.75–0.94), and human-only pre-Delphi agreement was somewhat lower. Two smaller/open annotators (DeepSeek-V3, LLaMA-3.1-8B-Instruct) were also tried and gave similar but slightly weaker agreement (0.83 and 0.74) and predictive power.

The battery: 63 tasks from 20 benchmarks were drawn from ICML/NeurIPS/ICLR/ACL/EMNLP/NAACL 2024 papers with "bench" in the title, filtered to exclude benchmarks where GPT-4 already exceeds 75% accuracy. After removing instances flagged as low-quality, non-objective or ambiguous by an LLM quality check (16% of an initial 21,996-instance pool) and instances the annotator failed to score (0.9%), 18,291 instances remained. Grading of subject-model responses used two LLM judges, GPT-4o and Claude 3.5 Sonnet, on a 1–5 correctness scale; roughly 12% of instances where the two judges disagreed on the success/failure direction were dropped as "hard to verify," yielding the final 16,108-instance ADeLe v1.0 battery. A manual spot check on 100 sampled gradings found 98% agreement with the automated verdict.

The ability side: 15 LLMs (6 OpenAI, 5 Meta LLaMA, 4 DeepSeek-R1-Distilled-Qwen) are run on the battery. For each dimension, a "dominant slice" of instances (those where no other dimension's demand exceeds the level being studied) is used to fit a logistic subject characteristic curve; the level at 50% success probability is the model's ability on that dimension, and curves can extrapolate past level 5.

Headline results: (1) Demand profiles differ sharply across benchmarks (Fig. 2), and a sensitivity/specificity check (mean ≥ 2, s.d. ≥ 1.0 on the claimed dimension) finds that no benchmark in the sample of 20 hits high sensitivity and specificity together — e.g., SAT is saturated (low atypicality/high contamination), MedCalcBench is mostly an attention-and-scanning test rather than a medical-knowledge test (Table 2). (2) Ability profiles show knowledge dimensions scale mainly with model size, while quantitative/logical reasoning, metacognition and mind-modelling/social cognition are boosted by chain-of-thought/reasoning post-training (o1, DeepSeek-R1-Distilled) even at 7B scale, and parameter scaling shows diminishing returns at the top of the LLaMA and DeepSeek-Distilled families. (3) Demand-based random-forest assessors predict per-instance success with weighted AUROC ≈ 0.84 in-distribution, 0.81 with tasks held out, and 0.75 with entire benchmarks held out, versus 0.79/0.74 (task-OOD) and worse still (benchmark-OOD) for a GloVe-embedding RF and a fine-tuned LLaMA-3.1-8B classifier, at roughly six orders of magnitude less training compute (4 s versus ~300 GPU-hours). Average accuracy alone gives AUROC 0.5 by construction. The authors state limitations themselves: DeLeAn v1.0 has thin coverage of some dimensions (e.g., navigation) and no multimodal/agentic/robotic capabilities; very few level-5+ instances exist in the current battery; the choice of a 0–5+ range with a "1 in 10^(l-1)" calibration heuristic is a rule of thumb, not a per-dimension empirical calibration; and LLM-judge grading, while validated against human spot checks, may not transfer to more open-ended or agentic tasks.

## Learnings

Aggregate benchmark accuracy conflates a benchmark's difficulty distribution with a model's underlying ability: two "reasoning" benchmarks (OlymMATH Easy and GPQA) can rank a model in the opposite order from what their demand profiles predict, because GPQA carries knowledge demands beyond the formal-sciences dimension it advertises while OlymMATH Easy does not. A single percentage score cannot distinguish these cases; a demand profile can.

A cheap, interpretable classifier built only from 19 structured demand-annotation features (a random forest trained in about 4 seconds) matched or beat a fine-tuned 8B-parameter LLM classifier at predicting whether a given model would answer a given instance correctly, and degraded far less when the test distribution (new tasks, then new benchmarks) diverged from training. The gap between the two approaches widened, not narrowed, out of distribution — the opposite of what one might expect if the fine-tuned model were simply learning "harder" surface features.

Reasoning-oriented post-training (chain-of-thought, RL-style distillation) raises ability specifically on quantitative/logical reasoning, "identifying relevant information," and mind-modelling/social-cognition dimensions, sometimes down to 7B parameter scale, while knowledge dimensions stay tied mainly to raw parameter count. This is a case where two different training/scaling levers move genuinely separable capability axes, which a single aggregate score would blur into one number.

## Verification

Verification here means checking whether a subject model's answer is correct, not checking a derivation, so the paper's relevant content is grading methodology rather than physics-style step checking. Two LLM judges (GPT-4o and Claude 3.5 Sonnet) independently score each subject response 1 (surely incorrect) to 5 (surely correct) against the ground truth, given the same input; an instance is kept only if both judges agree in direction (both ≥4 or both ≤2), and the roughly 12% of instances where they disagree are discarded as "hard to verify" rather than forced into a label. The authors treat this abstention as protecting the predictive-power analysis from label noise, at the acknowledged cost of a possible selection bias in which instances remain. A human spot check of 100 sampled gradings found 98% agreement with the automated verdict, which is the paper's only direct precision estimate for the grading pipeline. Separately, the demand-annotation step (not answer grading) is checked against human Delphi-consensus labels via the rWG inter-rater statistic (average 0.86, one dimension as low as 0.75), which is a construct-validity check on the rubrics themselves rather than on any single answer.

## Field context

The paper sits in the psychometrics-for-AI line the senior author has worked in for years (item response theory applied to classifiers, "assessors" that predict instance-level success, and the group's own earlier occupational-task taxonomy, Tolan et al. 2021, which this work explicitly extends with knowledge and "extraneous" dimensions). It is explicitly framed against two alternatives: (a) plain benchmark aggregation, which the authors argue lacks construct validity and saturates; and (b) populational latent-variable methods (factor analysis, PCA, IRT) that the authors say are unstable because they depend on which benchmarks and models happen to be in the sample, citing a case where two contemporaneous factor-analysis papers on LLM capabilities (refs 16, 17) disagreed. The "non-populational, per-instance, absolute-scale" framing is the paper's central positioning claim relative to that older tradition. It also explicitly targets a live disagreement in the field ("LLMs can/can't reason") and offers demand-profile mismatch as the resolution mechanism, continuing the same author group's "Predictable AI" agenda (their own prior Nature and Artificial Intelligence papers, refs 6–7). This review corpus does not yet contain another paper directly engaging the same construct-validity or assessor-prediction claims, so no cross-review connection is drawn beyond noting the shared author lineage with the group's earlier reliability work.

## Critical discussion

The two headline claims rest on different kinds of evidence and hold up differently under scrutiny. The construct-validity finding (benchmarks lack sensitivity/specificity for what they claim to measure) is demonstrated with a transparent, if somewhat arbitrary, threshold (mean ≥ 2, s.d. ≥ 1.0) applied consistently across 20 benchmarks, and the qualitative pattern (SAT saturation from contamination, MedCalcBench measuring attention rather than medical knowledge) is concrete enough to be checked against Table 2 rather than taken on faith; a different threshold could shift which benchmarks pass, but is unlikely to reverse the overall conclusion that aggregation obscures multidimensional demand.

The predictive-power claim is the more rigorously supported one: it is measured with AUROC/ECE against held-out correctness labels under three increasingly strict distribution shifts, with a real (if modest) baseline — a fine-tuned LLaMA-3.1-8B and a GloVe-embedding random forest, not a crippled strawman — and the demand-based assessor's advantage grows rather than shrinks as the shift gets harder, which is the pattern you would want if the demand features are capturing something more structural than surface text statistics. Whether a fine-tuned 8B model is the strongest achievable black-box baseline is arguable (a larger fine-tuned model or a stronger sentence-embedding classifier might close some of the gap), so "superior to strong baselines" should be read as "superior to the baselines tested," not as an upper bound on what black-box methods could do.

The grading pipeline has a genuine same-family-judge exposure that the paper does not directly address: GPT-4o is both one of the 15 subject models being evaluated and one of the two judges grading all subjects' answers, including its own. The paper reports GPT-4o as "the most predictable LLM" (AUROC 0.882) but does not test whether GPT-4o's own outputs are graded more leniently or more predictably by GPT-4o-as-judge than by Claude 3.5 Sonnet alone. This is a plausible, not demonstrated, confound; the 98% human-agreement spot check is reassuring but was not broken out by which subject model was being graded. Relatedly, the Competing interests statement discloses that OpenAI, Microsoft and Google provided free API access/tokens for a subset of the evaluated model families, which is worth naming as a disclosed relationship even though the paper's competitors (DeepSeek, Meta) are still shown fairly, and the two headline effects (construct validity, OOD predictive power) don't obviously benefit from favoring any one vendor's models.

The absolute-scale claim — that a demand level of 6 represents literally double the "demand" of level 3 — is the most speculative part of the paper. It rests on a stated "rule of thumb" (roughly 1 in 10^(l−1) people solving a level-l item) calibrated from OECD education-attainment statistics for the five knowledge dimensions and then extended by assumption to the other 13 dimensions, which the authors themselves flag as needing "proper calibration" in future work. The commensurability across dimensions that makes profiles comparable (not just orderable) is therefore an assumption baked into the measurement instrument, not an independently verified property.

What remains supported after these caveats: common LLM benchmarks measure a narrower and more contaminated/confounded slice of their claimed construct than their aggregate scores suggest, and a cheap, interpretable, per-instance demand annotation predicts success better out of distribution than two reasonable black-box alternatives, at a fraction of the compute. The strong ratio-scale interpretation and exact cross-dimension commensurability are best read as a working hypothesis the authors are transparent about rather than an established result.

## Relevance to us

The size-versus-post-training split (knowledge ability tracks parameters; reasoning, metacognition and mind-modelling ability track chain-of-thought and inference compute) is direct evidence for one arm of Tension 1 (frontier backbone vs small specialized models): it suggests a physics-attuned backbone (B02) does not need to compete on raw scale for the capability axes that a research collaborator most needs — reasoning and self-monitoring — since those move with post-training and inference-time structure, not parameter count, even down to 7B in this data. That is encouraging for a small team but is measured on generic cognitive dimensions, not on physics-specific reasoning, so it is a hypothesis to test in-domain rather than a transferable result.

The demand-based assessor's core trick — decompose "did it succeed" into per-instance structured features and get a cheap, interpretable, more OOD-robust predictor than an expensive black-box model — is a candidate mechanism for B12 (graded physics-native verification stack) and for the "multidimensional non-saturating eval" item in our verification interests: instead of one pass/fail number, a physics-instance profile (what kind of reasoning, what domain knowledge, how atypical, how much is being asked at once) could explain and anticipate where our own verifier or backbone will fail, the same way DeLeAn explains benchmark-level failure here. The dimensions themselves (verbal, logical, metacognitive, knowledge-domain) are generic and would need physics-native replacements (family, regime, assumption load) rather than direct reuse, so this is a design pattern to borrow, not a tool to adopt.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| DeLeAn demand-profile analysis | benchmark construct validity | evaluates | 0.9 | papers/canonical/2026-05-06/26scales.md:L736 | Demand profiles reveal whether a benchmark is sensitive/specific to its claimed capability |
| demand-based RF assessor | out-of-distribution success prediction | improves | 0.85 | papers/canonical/2026-05-06/26scales.md:L837 | Demand features beat GloVe-embedding and fine-tuned-LLaMA assessors under task/benchmark OOD shift |
| aggregate benchmark accuracy | AI capability estimate | contradicts | 0.8 | papers/canonical/2026-05-06/26scales.md:L832 | Same nominal task type yields opposite model rankings once demand profiles differ |
| chain-of-thought/RL post-training | reasoning and metacognition ability scores | improves | 0.8 | papers/canonical/2026-05-06/26scales.md:L831 | o1 and DeepSeek-R1-Distilled show higher QL/MCr/MS ability than same-size non-reasoning models |
| dual LLM-judge grading (GPT-4o, Claude 3.5 Sonnet) | subject-response correctness labels | uses | 0.7 | papers/canonical/2026-05-06/26scales.md:L934 | Correctness set by judge agreement; disagreeing instances discarded rather than force-labelled |
