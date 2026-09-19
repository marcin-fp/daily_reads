---
schema_version: 1
paper: slug:25mcrit
title: "Training Language Models to Critique With Multi-agent Feedback"
authors:
  - Tian Lan
  - Wenwei Zhang
  - Chengqi Lyu
  - Shuaibin Li
  - Chen Xu
  - Heyan Huang
  - Dahua Lin
  - Xian-Ling Mao
  - Kai Chen
publication:
  first_public_date: "2024-10-20"
  first_public_date_precision: day
  venue: "Findings of EMNLP 2025"
  status: conference
  reviewed_version: v1
  reviewed_version_date: "2024-10-20"
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-06-09/25mcrit.md
raw: papers/raw/2026-06-09/25mcrit-pdf.md
source_url: https://arxiv.org/abs/2410.15287
organizations:
  - name: Beijing Institute of Technology
    sector: academia
    roles: [author_affiliation]
    authors: [Tian Lan, Heyan Huang, Xian-Ling Mao, Chen Xu]
    grants: []
  - name: Shanghai AI Laboratory
    sector: nonprofit
    roles: [author_affiliation]
    authors: [Wenwei Zhang, Chengqi Lyu, Shuaibin Li, Dahua Lin, Kai Chen]
    grants: []
  - name: The Chinese University of Hong Kong (MMLab)
    sector: academia
    roles: [author_affiliation]
    authors: [Dahua Lin]
    grants: []
  - name: CPII under InnoHK
    sector: nonprofit
    roles: [author_affiliation]
    authors: [Dahua Lin]
    grants: []
  - name: National Natural Science Foundation of China
    sector: government
    roles: [funder]
    authors: []
    grants: ["62402043", "62172039", "62302040", "U21B2009", "62276110"]
  - name: China Postdoctoral Science Foundation
    sector: government
    roles: [funder]
    authors: []
    grants: ["2022TQ0033"]
  - name: Beijing Institute of Technology Research Fund Program for Young Scholars
    sector: academia
    roles: [funder]
    authors: []
    grants: []
artifacts:
  - type: code
    url: https://github.com/gmftbyGMFTBY/MultiCritique
  - type: data
    url: https://github.com/gmftbyGMFTBY/MultiCritique
facets:
  domains: [machine-learning, natural-language-processing]
  paper_type: [method, dataset, experiment]
  methods: [multi-agent-critique-aggregation, meta-critique, reinforcement-learning-from-ai-feedback, supervised-fine-tuning, ppo]
  models: [GPT-4, GPT-3.5-Turbo, Claude-1-instant, Qwen-1.5-72B-Chat, Qwen2-72B-Instruct, InternLM2-7B-Chat-SFT, InternLM2-20B-Chat, Llama3-70B-Instruct, Llama3-8B-Instruct]
  benchmarks: [CRITICEVAL, CRITICBENCH]
assessment:
  extract_quality: partial
  extract_limitations: [figures-not-visually-assessed, figure-text-missing]
  critical_flags: [same-family-judge, missing-uncertainty]
metadata_notes: "Confirmed via web search and arXiv (2410.15287, v1 only, submitted 2024-10-20) to be accepted to Findings of EMNLP 2025 (ACL Anthology 2025.findings-emnlp.78); the extracted canonical text is the camera-ready proceedings version. Funding grants (NSFC, China Postdoctoral Science Foundation, BIT Young Scholars fund) are stated for the author group collectively without naming which specific authors each grant covers, so no per-author attribution is recorded. Shanghai AI Laboratory and CPII under InnoHK are classified as nonprofit research institutes rather than industry or government, consistent with their public description as state- or government-initiative-funded, non-commercial research organizations; this is a judgment call noted for transparency. The early pages of the canonical extraction (Figure 1's pipeline diagram) contain a long run of unreadable image placeholders and fragmentary OCR text (e.g. isolated tokens like 'Rev', 'ACU with Label') that were not usable and are disregarded in this review; the Method, Results, and Limitations sections extracted cleanly."
---

Citation: Lan, T., Zhang, W., Lyu, C., Li, S., Xu, C., Huang, H., Lin, D., Mao, X.-L., and Chen, K. Training Language Models to Critique With Multi-agent Feedback. Findings of the Association for Computational Linguistics: EMNLP 2025.

## What this paper is about

Teaching a language model to critique, that is, to find and explain flaws in a response, usually means training it on critiques written by one strong "teacher" model such as GPT-4. But a single model's critiques inherit that model's own blind spots, and fine-tuning on them can bake those blind spots into the student. This paper asks whether getting several different models to critique the same response, and then having a judging step reconcile their disagreements, produces better training data than trusting one model's critique outright, without requiring the far more expensive alternative of human-annotated critiques. The resulting method, MultiCritique, is used to build both a supervised fine-tuning dataset and a reinforcement-learning preference dataset, and a 7B model trained on them is reported to match or approach much larger models on two critique benchmarks.

## Extended summary

The pipeline starts from 10.7K diverse queries drawn from alignment, math, coding, and existing critique datasets, each paired with three responses of low, medium, and high quality sampled from eleven different LLMs and coarsely scored by a reward model, giving 32.1K query-response pairs. For each pair, GPT-4 is prompted to generate three "crucial information" fields meant to make the critique task itself easier and more consistent: a task description, a customized two-tier evaluation criteria structure, and a reference response that would satisfy those criteria.

The MultiCritique-SFT stage then has four different LLMs (GPT-4, Claude-1-instant, Qwen-1.5-72B-Chat, and InternLM2-20B-Chat) independently critique each response, both sentence-by-sentence and across sentences, producing structured "Analytical Critique Units" (ACUs) that each name a location, a description of the flaw, a revision suggestion, a criteria type, and a severity rating. Rather than letting the four models debate each other directly, which the authors report reduces critique diversity in their preliminary tests, a separate meta-critique step has GPT-4 classify each ACU, one at a time, into one of seven human-defined quality categories with associated severity scores, using the other models' critiques only as context. GPT-4 then aggregates the highest-quality ACUs across all four models' critiques into one final, comprehensive critique, discarding or correcting the ones flagged as flawed. This produces the 32.1K-sample MultiCritiqueDataset-SFT, and the authors report (Table 1) that critiques from this aggregation process contain more distinct critique units and cover more evaluation-criteria aspects than a critique from any single one of the four contributing models alone.

The MultiCritique-RL stage constructs preference pairs from the same underlying critiques: for each query-response pair, a "chosen" and "rejected" critique are identified from the meta-critique severity scores. Because the authors' own prior work found meta-critique judgments themselves to be noisy, an additional step, Multi-Agent-Revision-Validating (MARV), is used to filter these pairs: four independent 7B LLMs each revise the response according to a given critique, eight times each (32 revisions total), those revisions are scored by a reward model, and a preference pair is kept only if the chosen critique's revisions score higher on average than the rejected critique's revisions. This yields a 19.7K-sample preference dataset, MultiCritiqueDataset-RL, used to train a reward model (via a focal ranking loss) and then fine-tune the SFT model with PPO.

Experiments fine-tune 7B-8B open models (InternLM2-7B-Chat-SFT as the primary reported model, with Llama3 and Qwen2.5 results in an appendix) and evaluate on CRITICEVAL (nine tasks spanning alignment, general NLP, and reasoning, scored on objective feedback correlation with humans, GPT-4-judged subjective feedback quality, objective revision pass rate, and GPT-4-judged subjective revision quality) and CriticBench (3,825 items across five reasoning task types, scored by F1 for correctly identifying whether an evaluated response is right or wrong). SFT and RL fine-tuning on MultiCritiqueDataset yield absolute gains of 19.8 and 6.3 percentage points respectively on CRITICEVAL's subjective feedback metric over the InternLM2-7B-Chat-SFT base model, and the RL-stage model reaches 75.66% F1 on CriticBench, close to GPT-4-Turbo's 78.75% and above the 70B open models tested (Qwen2-72B-Instruct 75.86%, Llama3-70B-Instruct 76.80%), though the authors note CriticBench's difficulty means even GPT-4-Turbo is well short of a ceiling. Against three baseline critique datasets built from single-model (GPT-4) critiques (Auto-J, UltraFeedback, Feedback-Collection), MultiCritiqueDataset-SFT gives average gains of 21.48% and 22.50% on CRITICEVAL and CriticBench respectively, and a model trained on only 3K MultiCritique samples matches baselines trained on 100K-257K samples from those other datasets, a reported 2.15-4.22x data-efficiency improvement, estimated by the authors to correspond to roughly $890 of GPT-4 API cost versus $1,915-$3,758 for the larger baseline datasets.

Ablations isolate specific components. Fine-tuning on critiques from any single one of the four contributing models underperforms the full meta-critique-aggregated dataset (Table 5), with GPT-4 alone the strongest single source and Claude-1-instant the weakest. Removing any of the three "crucial information" fields degrades most CRITICEVAL metrics, except that removing the evaluation criteria specifically improves the subjective revision score, which the authors flag as an unexplained side effect for future investigation (Table 6). Removing MARV from the RL pipeline causes the resulting model's subjective feedback score to fall below even the SFT-only baseline (4.84 versus 5.71), despite additional RL training, which the authors read as evidence that MARV, not the RL stage by itself, is what stabilizes RL fine-tuning by filtering out noisy preference pairs (Table 7). Separately, integrating the SFT dataset into general instruction-tuning is reported to improve average general-benchmark performance (for example, a 9.43% average gain on AlpacaEval and Alpaca Hard), and removing math and coding examples from training still yields a model that closely matches full-dataset performance on those held-out task types (88.44% versus 88.56% on math, Table 9), which the authors present as evidence of generalization to unseen tasks.

A late "Limitations" section (unusually substantive for this section) reports that the four critique-generating models were chosen for capability as of April 2024 and may already be dated; that MARV's reward model (InternLM2-20B-reward) is a single point of potential failure whose accuracy may vary by task; that preliminary tests applying MultiCritique to a much stronger 72B backbone (Qwen2.5-72B-Instruct, which the authors note already exceeds GPT-4 on both benchmarks) showed limited gains; and that the severity-score component, though not the paper's main focus, was checked against human judgment on a sample of 200 instances by three independent annotators, finding 0.7717 agreement (against a 0.25 random baseline), 0.8593 internal consistency across 64 repeated LLM samplings, and 0.7812 inter-model agreement among the four critique-generating LLMs.

## Learnings

Classifying each atomic unit of a critique into a discrete quality category via a separate meta-critique step, rather than letting several models debate a response directly, appears to preserve more critique diversity: the authors report that direct multi-agent debate reduced diversity in their preliminary tests, while judging each critique unit independently, using the other models' critiques only as context rather than as something to converge with, avoided that collapse. This is a specific, checkable design choice, not a debate mechanism, worth distinguishing from other multi-agent frameworks that do rely on iterative back-and-forth.

Validating a preference judgment by its downstream consequence, rather than trusting the judgment directly, produced a measurable stability gain here: rather than trusting the meta-critique severity score alone to build RL preference pairs, the pipeline additionally checks whether the "better" critique actually leads to better revisions when several models act on it, and removing that downstream check caused the RL-trained model's critique quality to fall below the pre-RL baseline despite additional training. A judgment that is merely self-consistent is not the same as a judgment that is useful when acted on, and this paper offers a concrete instance where testing the latter, not the former, kept a preference-learning pipeline from degrading.

Data efficiency in fine-tuning can come from how a training set is constructed rather than from its size: a training set built by aggregating and filtering multiple models' outputs through an explicit quality-classification step reportedly matched datasets 30-80 times larger built from a single teacher model's uncorrected output. This does not establish that aggregation alone (versus other factors, such as the shared query curation and "crucial information" scaffolding used across every variant of the dataset in this paper) is the specific driver of that efficiency, since the paper does not report a size-matched comparison isolating aggregation from those other shared components.

## Verification

Verification in this paper takes the form of a specific, learned reward signal rather than a deterministic check, but the paper's own design choices show real awareness of the risks of trusting a judge's stated confidence directly. The meta-critique step, in which GPT-4 classifies each critique unit into a human-defined quality category, is itself acknowledged by the authors (citing their own prior work) to be noisy and more difficult than critiquing a response in the first place, which motivates MARV: rather than trusting that classification as the final word on which of two critiques is better, the pipeline tests each critique's downstream effect, having several independent models revise a response according to it and scoring the resulting revisions with a reward model, and keeps a preference pair only when the intended "better" critique actually produces better revisions on average. This is an outcome-validated check rather than a purely judgment-based one, and its removal is shown to cause a specific, measured regression (Table 7). A narrower, explicitly labeled preliminary check is also reported for the severity-scoring component specifically: three human annotators independently rated 200 sampled instances, finding moderate-to-strong agreement (0.7717) against a stated random baseline of 0.25, alongside separately reported internal consistency (0.8593 across 64 repeated LLM samplings) and inter-model agreement (0.7812) statistics. The paper leans on an external source, the CRITICEVAL benchmark's own prior validation, for its claim that GPT-4's subjective judgments correlate well with humans, rather than independently re-establishing that correlation for the specific aggregated, multi-agent critiques this pipeline produces, which are stylistically different from the single-model critiques that correlation was likely originally measured against.

## Field context

This paper positions itself between two existing approaches to teaching LLMs to critique: human-annotated critique training (exemplified by CriticGPT and DeepSeek-GRM), which the authors describe as effective but too costly to scale, and distillation from a single strong teacher model's critiques (exemplified by Auto-J, UltraFeedback/UltraCM, Feedback-Collection/Prometheus, TIGERScore, Themis, and CritiqueLLM), which the authors argue inherits that teacher's own systematic errors and propagates them through fine-tuning. Its contribution sits at a specific point in that landscape: applying multi-agent feedback during training-data construction (both the SFT and RL stages) rather than only at inference time, distinguishing it from multi-agent LLM evaluation frameworks such as ChatEval, PoLL, and PRD that use multiple agents purely to produce a better judgment at test time rather than to build better training data. Within this corpus, the paper's stated motivation for using four different models rather than one, that a single model's critique inherits that model's own blind spots, is the same concern this corpus's review of 24selfcor documents empirically for same-model self-correction of reasoning; this paper's answer is architectural (aggregate across models with an explicit meta-critique judge) rather than a claim that the underlying single-model weakness has been eliminated, since the meta-critique judge and final aggregator role are both filled by GPT-4, one of the four contributing models.

## Critical discussion

GPT-4 occupies four distinct roles across this pipeline: one of the four critique-generating agents, the meta-critique judge that classifies every unit's quality (including its own critiques' units), the final aggregator that merges the highest-quality units into the label used for supervised fine-tuning, and the subjective evaluator (F sub., R sub.) that scores the trained model's output quality at test time on CRITICEVAL. This is a deeper and more pervasive same-family dependency than a single "judge equals generator" concern, since it runs through data construction, aggregation, and evaluation. The paper's own citation that CRITICEVAL has separately validated a strong GPT-4-human correlation for subjective evaluation is reasonable support, but that correlation was established for the benchmark generally, not specifically re-verified for the aggregated, multi-model critiques this particular pipeline produces, which differ in structure and provenance from a typical single-model critique. The one place the paper does independently check a judged quantity against humans, the severity-score validation, is honestly framed under the paper's own "Limitations" heading rather than presented as a validated strength, and it covers 200 instances, a narrow slice relative to the 32.1K-sample SFT dataset and 19.7K-sample RL dataset the severity scores help construct.

The MARV ablation (Table 7) is a genuinely credible, specific result: removing the outcome-based validation step causes the RL-trained model's subjective feedback score to fall below the pre-RL SFT baseline, showing that RL fine-tuning without that filter can actively harm the property it is meant to improve, not merely fail to help. This is a stronger and more informative result than a simple "ablation hurts performance" finding, since it isolates a specific failure direction (noisy preference pairs actively degrading RL) rather than only a magnitude of gain.

The headline framing that the fine-tuned 7B model "approaches advanced 70B LLMs and GPT-4" is well supported specifically for CriticBench's F1 metric (75.66% versus GPT-4-Turbo's 78.75%, comparable to or above the 70B open models tested), but the same model trails GPT-4-Turbo by a much wider margin on CRITICEVAL's objective feedback score (63.28 versus 76.09, and versus Qwen2-72B-Instruct's 75.44), so the "approaching frontier performance" claim should be read as scoped to the specific metric it is made for rather than generalized across every reported axis of critique quality. The reported 2.15-4.22x data-efficiency gain over baseline datasets is a specific, falsifiable number, but the comparison is against externally built single-model-critique datasets rather than against a size-matched ablation of MultiCritique itself with the meta-critique aggregation step removed, so it is not fully possible to attribute the efficiency gain specifically to aggregation versus other shared components of the pipeline, such as the query curation and the "crucial information" scaffolding used identically across every dataset variant tested in this paper.

What remains well supported after these caveats: consistent gains over three externally constructed baseline datasets across two independently maintained benchmarks, a specific and credible internal ablation isolating MARV's stabilizing role in RL fine-tuning, and a real if narrow-population attempt to validate one judged quantity (severity scores) against independent human raters. The paper's own limitations section, flagging model staleness, single-reward-model dependency in MARV, and limited gains on a stronger backbone, is candid and specific rather than a generic disclaimer, and matches what the reported experiments can and cannot support.

## Relevance to us

This connects directly to our interest in independent or stronger critics for a graded verification stack (B12) and to the standing concern, also visible in this corpus's review of 24selfcor, that same-model self-critique is weak. Two mechanisms are worth taking as candidate design patterns rather than as validated conclusions we can import wholesale. First, meta-critique classification, judging each atomic unit of several independently generated critiques into a discrete quality category rather than asking one model to critique in a single pass, is a concrete way to build a graded quality signal for candidate checks or flags before they are used for training or filtering, which is directly relevant to how we might construct process-level signal for physics derivation steps from multiple independent solvers or heuristics rather than trusting a single one. Second, and more directly transferable, MARV's principle, validating a candidate judgment not by the judge's stated confidence but by whether acting on it actually improves an independent, harder-to-game downstream outcome, matches our own instinct that a check should be trusted because following it helps, not because a judge asserts it confidently; the concrete demonstration here, that skipping this outcome-based validation actively degraded the RL-trained model's quality rather than merely failing to help, is a useful, specific data point for why an analogous outcome-validation step (does acting on a candidate physics flag actually improve the derivation, verified independently) would be worth building into our own preference or reward pipelines rather than treating a single judge's severity score as sufficient. At the same time, the paper's own reported limitation, that this training approach showed limited gains when applied to a backbone already stronger than the judge model used to construct the training signal, is a useful caution for any plan that assumes a technique bootstrapped from a currently-frontier judge will keep paying off as our own backbone models improve past that judge's level; it may instead have a ceiling tied to the judge's own capability, which is worth planning around rather than assuming away.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| multi agent critique aggregation via meta critique | critique quality versus single model critiques | improves | 0.7 | papers/canonical/2026-06-09/25mcrit.md:L380 | Fine-tuning on the aggregated dataset outperforms fine-tuning on any single contributing model's critiques alone |
| MARV validating critiques by downstream revision quality | stability of RL fine tuned critique ability | improves | 0.75 | papers/canonical/2026-06-09/25mcrit.md:L394 | Removing MARV drops the RL model's subjective feedback score below the pre-RL SFT baseline |
| MultiCritique SFT dataset construction | data efficiency versus UltraFeedback and Feedback Collection | improves | 0.65 | papers/canonical/2026-06-09/25mcrit.md:L377 | A model trained on 3K MultiCritique samples matches baselines trained on 100K to 257K samples |
| crucial information task description criteria and reference response | critique quality on most CRITICEVAL metrics | implies | 0.6 | papers/canonical/2026-06-09/25mcrit.md:L390 | Removing any one of the three crucial information fields degrades most reported metrics |
| fine tuned 7B critique model | GPT-4-Turbo critique F1 on CriticBench | evaluates | 0.6 | papers/canonical/2026-06-09/25mcrit.md:L351 | The 7B model reaches 75.66 percent F1 against GPT-4-Turbo's 78.75 percent, approaching but not matching it |
