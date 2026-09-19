---
schema_version: 1
paper: slug:26eva
title: "I Don't Need Solution. I Need Emotional Support: Empathetic LLMs based on Emotional Validation"
authors:
  - Suhyune Son
  - Jungwoo Lim
  - Myunghoon Kang
  - Seongtae Hong
  - Yuna Hur
  - Evelyn Hayoon Zi
  - Heuiseok Lim
publication:
  first_public_date: "2026-07"
  first_public_date_precision: month
  venue: "Findings of ACL 2026"
  status: conference
  reviewed_version: null
  reviewed_version_date: null
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-06-09/26eva.md
raw: papers/raw/2026-06-09/26eva-pdf.md
source_url: https://aclanthology.org/2026.findings-acl.1/
organizations:
  - name: Korea University
    sector: academia
    roles: [author_affiliation]
    authors: [Suhyune Son, Jungwoo Lim, Myunghoon Kang, Seongtae Hong, Evelyn Hayoon Zi, Heuiseok Lim]
    grants: []
  - name: Human-Inspired AI Research
    sector: other
    roles: [author_affiliation]
    authors: [Yuna Hur]
    grants: []
  - name: National Research Foundation of Korea
    sector: government
    roles: [funder]
    authors: []
    grants: ["NRF-2021R1A6A1A03045425"]
  - name: Commercialization Promotion Agency for R&D Outcomes
    sector: government
    roles: [funder]
    authors: []
    grants: ["2710086166"]
  - name: Institute for Information & communications Technology Promotion
    sector: government
    roles: [funder]
    authors: []
    grants: ["RS-2024-00398115"]
artifacts:
  - type: code
    url: https://github.com/sonsuhyune/EVA
  - type: data
    url: https://github.com/sonsuhyune/EVA
facets:
  domains: [machine-learning, natural-language-processing, psychology]
  paper_type: [method, dataset, experiment]
  methods: [supervised-fine-tuning, direct-preference-optimization, llm-as-judge, human-evaluation]
  models: [GPT-3.5-Turbo, GPT-4o, Mistral-7B-Instruct, LLaMA-3-8B-Instruct, Qwen2-Instruct, ChatCounselor, MeChat, EmoLLM]
  benchmarks: [ESConv, EmpatheticDialogues]
assessment:
  extract_quality: partial
  extract_limitations: [figures-not-visually-assessed]
  critical_flags: [circular-evaluation, missing-uncertainty]
metadata_notes: "Venue and DOI (10.18653/v1/2026.findings-acl.1) confirmed via the ACL Anthology page for this paper; only month precision is used for the publication date since no exact day is listed there. 'Human-Inspired AI Research' (Yuna Hur's affiliation) is recorded with sector 'other' since no further description of this organization is given in the paper. Funding grants (NRF, COMPA, IITP) are stated for 'this research'/'this work' collectively without naming which specific authors each grant covers, so no per-author attribution is recorded. Several figures central to the paper's diagnostic and analysis sections (n-gram frequency charts, response-type pie charts, the human-evaluation win/tie/loss bar chart, reliability/calibration-style plots) render as unlabeled images in the extraction; numeric findings used in this review are drawn from the surrounding prose discussion of each figure."
---

Citation: Son, S., Lim, J., Kang, M., Hong, S., Hur, Y., Zi, E. H., and Lim, H. I Don't Need Solution. I Need Emotional Support: Empathetic LLMs based on Emotional Validation. Findings of the Association for Computational Linguistics: ACL 2026.

## What this paper is about

When someone tells a language model they're upset, current models tend to respond the way a well-meaning but tone-deaf friend might: jumping straight to a list of suggestions rather than first showing they've actually heard and accepted the person's feelings. This paper measures that problem directly (most LLM responses in a small study were rated as not comforting) and proposes a fix grounded in an established psychological framework: staging a conversation's supportive responses through four increasingly deep levels of "emotional validation," borrowed from Dialectical Behavior Therapy, so that a model listens and reflects before it validates and finally offers guidance, rather than offering guidance immediately and repetitively regardless of where the conversation actually is.

## Extended summary

A preliminary study prompts Mistral-7B-Instruct and GPT-4o on 100 ESConv test dialogues and has 15 crowd workers judge whether each response felt comforting; 87.82% of responses were rated as not comforting (inter-annotator agreement, Fleiss κ = 0.69). Two concrete failure modes are diagnosed: patterned responses (the same top-4-gram phrases recur across many different dialogues, suggesting the models draw on a narrow, templated set of expressions) and a bias toward suggesting solutions (a "Suggesting Solution" response-type classification accounts for 40.5% of Mistral's and 61.3% of GPT-4o's responses, while "Understanding and Validation" responses, which convey emotional validation, are rare).

To address this, the paper adapts emotional validation theory from Dialectical Behavior Therapy (DBT), which frames validation as a hierarchical progression from careful attention to explicit acknowledgment, into four operational levels suited to open-domain, text-based, single-session LLM dialogue, explicitly stripping out the original theory's assumptions of rich shared context, long-term rapport, and multimodal cues that do not hold in this setting: Level 1 (Listening and Observing, e.g., "I'm sorry to hear that you're going through that"), Level 2 (Accurate Reflection, paraphrasing the help-seeker's situation and emotion), Level 3 (Validating, confirming the feelings are natural and reasonable), and Level 4 (Radical Genuineness, acknowledging the person's inherent worth and offering guidance from that grounded position).

The proposed method, EVA, trains a model in two stages. Empathy Acquisition (ACQ) is standard supervised fine-tuning on existing empathetic dialogue data (ESConv and EmpatheticDialogues) to establish general empathetic response capability. Emotional Validation Alignment (ALI) then applies Direct Preference Optimization using a newly constructed dataset, the Emotional Validation Aware Dataset (EVAD): GPT-3.5-Turbo generates candidate responses at each validation level given a dialogue history and an explanation of the theory, and 12 annotators with at least a bachelor's degree in psychology select the most preferred response as "chosen" and label others "rejected," filtering out low-quality generations in the process. An analysis of the resulting chosen-response distribution shows Level 1 responses concentrated early in dialogues and Level 4 responses increasing toward the end, confirming the curated preference data itself tracks the intended theoretical progression.

To evaluate whether a model's generated responses actually follow this progression across a full conversation, rather than only being empathetic utterance-by-utterance, the paper introduces EVAEval: each generated utterance is labeled with its validation level by a pretrained classifier, its relative position within the dialogue is computed and binned into quartiles, and for each level the squared difference between the model's per-quartile level distribution and EVAD's gold per-quartile distribution is averaged across quartiles, with lower scores indicating closer alignment to the theorized progression. The metric's validity is checked via Spearman correlation with human evaluation scores, reported in an appendix not included in the extracted main text.

Experiments compare EVA-trained versions of Mistral-7B-Instruct, Qwen2-Instruct, and LLaMA-3-8B-Instruct against their untrained counterparts, general-purpose models (GPT-3.5-Turbo, GPT-4o), and ESC-specialized baselines (ChatCounselor, MeChat, EmoLLM), using general generation metrics (BLEU-2, ROUGE-L, Dist-2), EPITOME's empathy-specific Interpretations (IP), Explorations (EX), and Emotional Reactions (ER) metrics, and EVAEval. On the ESConv test set, EVA-based models perform comparably to baselines on general metrics while substantially improving IP (for example, EVAMistral reaches 0.3050 versus Mistral's 0.0810, and EVAQwen reaches 0.1235 versus Qwen's 0.0308), the metric the paper considers most directly tied to emotional validation, and generally improve EX as well. ER sometimes favors GPT-3.5-Turbo and GPT-4o over the EVA models, which the authors attribute to ER measuring raw emotional expression regardless of conversational progression, whereas EVA specifically targets staged validation rather than maximal emotional expression in every utterance. Ablations show removing either ACQ or ALI degrades general metrics and IP; removing ALI specifically increases Dist-2 (more lexically diverse but less contextually aligned responses, a disclosed trade-off) and destabilizes EX. On EVAEval, EVA-based models achieve the lowest (best) average scores across all three backbones, outperforming both general-purpose and ESC-specialized baselines, and ablations show removing ALI worsens the score for every EVA variant, with removing ACQ worsening it by an even larger margin.

A human evaluation recruits 15 psychology majors to rate EVAMistral against Mistral on 100 ESConv dialogues across four criteria (Comfortness, Comprehensibility, Emotional Validation, Fluency; Fleiss κ = 0.61). EVAMistral wins on every criterion except Fluency, most notably with roughly 60% of its responses rated superior on Comfortness, but shows a slight fluency decrease, which the paper's limitations section attributes to the richer, longer, multi-clause phrasing that comes with deeper empathetic framing. Further analysis confirms the two originally diagnosed failure modes are mitigated: EVAMistral's frequently generated phrases are rarely repeated more than 30% within a single dialogue (unlike Mistral's heavy reliance on a narrow set of stock phrases), and its Solution-Suggestion response share drops substantially while its Understanding-and-Validation share rises from 11.7% to 26.0%.

The paper's own limitations section names six specific concerns: the number of human annotators, while defended as above-average for this subfield; the self-developed response-type taxonomy, used for lack of an established one; the inherent subjectivity of empathy annotation; an explicitly documented empathy-fluency trade-off; EVAEval's dependence on an imperfect classifier whose errors mostly occur between adjacent rather than distant levels; and the fact that EVAD's candidate responses were partially generated by ChatGPT before human filtering, which the authors state could introduce annotation artifacts or "circularity between model-generated data and model evaluation" that future work should address.

## Learnings

The specific pattern driving perceived lack of empathy in this study was not flat or generic emotional tone but a structural mismatch: models defaulted to offering solutions far more often than validating feelings, and repeated the same handful of stock phrases within individual conversations even when those phrases were not unusually rare in the model's overall output. This distinction, between overall phrase frequency and within-dialogue repetition of the same phrase, is a specific, measurable diagnostic worth checking in any dialogue system meant to feel responsive to a particular conversation rather than templated.

Adapting a clinical psychological framework developed for a richer interactional context (in-person therapy with shared history and multimodal cues) into a workable structure for stateless, text-only LLM dialogue required explicitly stripping out the assumptions the original theory depended on, while preserving its core hierarchical structure as a four-stage textual progression. This is a reusable pattern for importing any theory built for a richer human context into a text-only LLM interaction: the theory's structural skeleton can transfer usefully even when the assumptions underlying its original medium do not.

Aligning a model toward a specific theoretically motivated behavioral pattern is not a uniform improvement across every axis: removing the alignment stage increased lexical diversity but reduced how well responses tracked the intended validation progression, and the fully aligned model showed a small, consistently observed fluency cost in human evaluation attributed to its longer, more multi-clause empathetic phrasing. This is a concrete, disclosed example of a real trade-off (depth of framing versus perceived smoothness) worth expecting whenever a generation system is optimized toward a specific qualitative behavioral target rather than fluency alone.

## Verification

Verification appears in this paper mainly as metric validation and training-data quality control rather than scientific claim-checking. The paper's own automatic metric, EVAEval, is checked against human judgment via a reported Spearman correlation (detailed in an appendix not present in the extracted text), a legitimate step toward establishing that a purpose-built metric actually tracks what it claims to measure rather than being assumed valid by construction. EVAEval's underlying classifier is separately and honestly assessed as a source of residual noise: the paper reports it achieves a strong overall F1 score but that most of its errors occur between adjacent validation levels rather than distant ones, a disclosed rather than hidden limitation. The EVAD preference dataset itself went through a human-filtering step specifically intended to catch and remove low-quality model-generated candidate responses before they could be used as a training signal, a form of quality control on the training data; the authors are candid, however, that this does not fully resolve a circularity concern, since the underlying candidates were originally sampled from a language model (ChatGPT) rather than authored by humans from scratch, and they name this directly as an open issue for future work rather than treating the human-filtering step as sufficient on its own.

## Field context

This paper extends the empathetic dialogue generation literature (prior architectures such as MoEL and MIME, and more recent LLM-based mental-health and emotional-support systems including SoulChat, ChatCounselor, MeChat, and EmoLLM, several of which serve as this paper's baselines) by building specifically on EPITOME (Sharma et al., 2020) as an existing per-utterance empathy metric framework, while arguing that per-utterance metrics like EPITOME cannot capture whether a model's supportive behavior appropriately progresses across a multi-turn conversation, which is the specific gap EVAEval is built to address. Its theoretical grounding in Dialectical Behavior Therapy (Linehan, 1997) is a genuine cross-disciplinary import rather than an NLP-native empathy taxonomy, distinguishing its approach from most cited baselines. Within this corpus, the paper is a specific, quantified instance of the "helper versus mentor versus skeptic" tension named in this project's own framing, and of the concern that unconditional helpfulness can undermine the quality of support; here the finding runs in a particular, mechanistic direction, that premature solution-offering (rather than warmth or tone as such) is what damages perceived empathy, and the proposed fix operates by staging behavior across a multi-turn interaction rather than adjusting single-turn tone.

## Critical discussion

The preliminary study motivating the whole paper is a genuine strength: it is a specific, quantified diagnostic (87.82% of responses rated as not comforting, with substantial inter-annotator agreement) supported by two independently measured, concrete failure modes (n-gram repetition and response-type skew), grounding the paper's approach in a reproducible measurement rather than an assumed complaint about LLM empathy.

The paper also earns credit for naming, rather than hiding, a real circularity concern in its own core training-data construction: EVAD's candidate responses were generated by ChatGPT before human filtering, so despite that filtering step, the preference signal used to align EVA is not fully independent of an LLM's own output distribution, an honestly self-disclosed limitation the authors correctly flag as unresolved rather than presenting the human-filtering step as having fully addressed it (circular-evaluation). Separately, none of the headline comparisons in the main results table (the BLEU-2, ROUGE-L, Dist-2, IP, EX, ER, and EVAEval differences between EVA-based and baseline models) are accompanied by variance estimates, confidence intervals, or significance tests, despite several of the reported gaps being the paper's central quantitative evidence for its claims; a reader cannot tell from the reported numbers alone how much of the observed improvement would survive a formal significance test (missing-uncertainty), though the separately conducted human evaluation, which does report inter-annotator agreement, partially compensates by providing an independent, uncertainty-aware source of evidence for the paper's central claim. The paper's explanation for the ER metric's inconsistent results, that EVA targets validation-level progression rather than maximal per-utterance emotional expression, is plausible and consistent with the paper's own theoretical framing, but it is offered after the fact rather than as a prediction stated in advance, and the paper does not report a direct check (such as whether ER specifically anti-correlates with EVAEval score) that would make this explanation more than simply plausible-sounding.

What remains well supported: the core empirical claim, that a two-stage training pipeline (general empathetic fine-tuning plus preference alignment toward an explicit, theory-derived validation-level progression) measurably shifts model behavior away from repetitive, solution-first responses and toward acknowledgment-and-validation-first responses, is supported convergently by three largely independent measurement approaches (the EPITOME IP and EX metrics, the purpose-built EVAEval metric, and an independent human evaluation with reasonable annotator agreement), which is a stronger evidentiary basis than any single measure alone would provide. The paper's extensive, specific, self-disclosed limitations section, six distinct and concretely described concerns rather than a generic disclaimer, matches the actual scope of what the reported evidence can and cannot support.

## Relevance to us

This paper's subject matter, emotional support and mental-health dialogue, is outside our physics-reasoning domain, and this review does not force a substantive connection to our own bets. One methodological pattern is worth noting only as a structural analogy, not a finding to import: the paper's core mechanism, deliberately staging a specific behavior (validation before solution-offering) across a multi-turn interaction rather than optimizing a single-turn response in isolation, required building a bespoke conversation-level metric (EVAEval) specifically because an existing per-utterance metric (EPITOME) could not capture that staged progression. If we were ever to want a physics-reasoning collaborator to follow a staged interaction pattern within a session, for instance clarifying assumptions before proposing a derivation, or flagging uncertainty before committing to a claim, we would face the same measurement gap this paper identifies (a single-turn or per-step metric would miss whether the staging happened at the right point in the session) and might adapt a similar approach: a theory- or design-derived stage taxonomy paired with a distributional-alignment metric computed against relative position within a session. Beyond this structural parallel, the paper's substantive content does not bear on our work.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| existing LLM empathetic responses | help-seeker perceived comfort in emotional support conversations | contradicts | 0.75 | papers/canonical/2026-06-09/26eva.md:L84 | 87.82 percent of preliminary-study responses were rated as not comforting |
| EVA two stage training with empathy acquisition and validation alignment | EPITOME interpretations score relative to baseline models | improves | 0.75 | papers/canonical/2026-06-09/26eva.md:L162 | EVA-based models substantially outperform baselines on the IP empathy metric across backbones |
| removing emotional validation alignment ALI | alignment with the theorized validation level progression | contradicts | 0.7 | papers/canonical/2026-06-09/26eva.md:L171 | EVAEval score worsens for every EVA variant when the ALI component is ablated |
| EVA trained models | frequency of solution suggestion type responses relative to baseline | contradicts | 0.65 | papers/canonical/2026-06-09/26eva.md:L192 | Solution Suggestion share drops while Understanding and Validation share rises from 11.7 to 26.0 percent |
| EVAD preference dataset construction from ChatGPT generated candidates | full independence of the alignment training signal from LLM generated data | contradicts | 0.55 | papers/canonical/2026-06-09/26eva.md:L240 | Authors self-disclose a residual circularity concern despite human filtering of candidates |
