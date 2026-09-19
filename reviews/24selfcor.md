---
schema_version: 1
paper: slug:24selfcor
title: "Large Language Models Cannot Self-Correct Reasoning Yet"
authors:
  - Jie Huang
  - Xinyun Chen
  - Swaroop Mishra
  - Huaixiu Steven Zheng
  - Adams Wei Yu
  - Xinying Song
  - Denny Zhou
publication:
  first_public_date: "2023-10-03"
  first_public_date_precision: day
  venue: "ICLR 2024"
  status: conference
  reviewed_version: v2
  reviewed_version_date: "2024-03-14"
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-06-09/24selfcor.md
raw: papers/raw/2026-06-09/24selfcor-pdf.md
source_url: https://arxiv.org/abs/2310.01798
organizations:
  - name: Google DeepMind
    sector: industry
    roles: [author_affiliation]
    authors: [Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou]
    grants: []
  - name: University of Illinois at Urbana-Champaign
    sector: academia
    roles: [author_affiliation]
    authors: [Jie Huang]
    grants: []
artifacts: []
facets:
  domains: [machine-learning, natural-language-processing]
  paper_type: [analysis, experiment]
  methods: [self-correction, chain-of-thought-prompting, self-consistency, multi-agent-debate]
  models: [GPT-3.5-Turbo, GPT-4, GPT-4-Turbo, Llama-2-70B-chat]
  benchmarks: [GSM8K, CommonSenseQA, HotpotQA, CommonGen-Hard]
assessment:
  extract_quality: good
  extract_limitations: [figures-not-visually-assessed]
  critical_flags: [missing-uncertainty]
metadata_notes: "The paper is a slug entry (no arXiv id was assigned by the corpus at ingestion), but its content, title, and author list unambiguously match arXiv:2310.01798. The raw dump carries no version marker, but the text evaluates gpt-4-1106-preview (\"GPT-4-Turbo\"), a model released after the v1 submission date, so the reviewed content is v2 (the ICLR 2024 camera-ready revision), not v1. No funding, grants, or compute support are stated in the text beyond an informal acknowledgment of colleague discussion; no code or data release is mentioned."
---

Citation: Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X., and Zhou, D. Large Language Models Cannot Self-Correct Reasoning Yet. International Conference on Learning Representations (ICLR), 2024.

## What this paper is about

"Self-correction" — having a language model review and revise its own answer — sounds like it should make reasoning more reliable, since the same model that got something wrong is asked to catch and fix the mistake. This paper asks whether that actually works when the model gets no outside help: no ground-truth label telling it whether its answer was right, no code execution, no external critic. Running exactly this "intrinsic" setting on several reasoning benchmarks and model families, the authors find that self-correction does not improve reasoning accuracy and frequently makes it worse, and they trace several previously published claims of self-correction success to specific confounds in how those studies were set up rather than to a genuine correction ability.

## Extended summary

The paper defines intrinsic self-correction as a model revising its own response using only its own inherent capability, without external feedback (ground-truth labels, human input, tools, or other models). This is contrasted with prior self-correction pipelines (RCI, Reflexion) that use external, oracle information about answer correctness to decide when to stop revising, and with methods that use genuinely external feedback (code execution, retrieval, trained verifiers), which the paper does not dispute.

Three empirical arguments are made, each isolating a different confound in prior self-correction claims. First (Section 3), the authors replicate RCI (Kim et al., 2023) and Reflexion (Shinn et al., 2023) on GSM8K, CommonSenseQA, and HotpotQA using GPT-3.5-Turbo (gpt-3.5-turbo-0613) and GPT-4, following a three-step prompt: initial generation, self-produced feedback, and a revised answer, run for up to two rounds. With oracle labels gating the loop (only refining an answer already flagged as wrong), scores rise substantially (GSM8K 75.9→84.3 for GPT-3.5, 95.5→97.5 for GPT-4; CommonSenseQA 75.8→89.7 and 82.0→85.5; HotpotQA 26.0→29.0 and 49.0→59.0), reproducing the earlier papers' pattern. Removing the oracle and letting the model decide for itself whether to keep revising reverses the effect: accuracy drops across all three benchmarks for GPT-3.5 and GPT-4, and the same pattern holds for GPT-4-Turbo (gpt-4-1106-preview) and Llama-2-70b-chat, and across several differently worded feedback prompts (Tables 3–6). A per-response breakdown (Figure 1) shows why: on GSM8K, GPT-3.5 leaves 74.7% of answers unchanged and is more likely to turn a correct answer incorrect (8.8%) than the reverse (7.6%); Llama-2 changes answers far more often and loses substantial accuracy as a result (GSM8K 62.0→43.5→36.5; CommonSenseQA 64.0→37.5→36.5). GPT-4 and GPT-4-Turbo retain their initial answers roughly 90–96% of the time, which the authors attribute to higher confidence or robustness, but even these models see a net accuracy decline.

Second (Section 4), the authors test multi-agent debate (Du et al., 2023) as an alternative self-correction mechanism, where several LLM instances critique each other's answers over multiple rounds, replicated on the full GSM8K test set with gpt-3.5-turbo-0301, 3 agents, and 2 rounds. Debate does improve over standard prompting (Table 7), but when compared to self-consistency (independent sampling plus majority vote) at an equal number of total model calls, debate underperforms it at every matched budget (83.2 vs. 85.3 at 6 responses; 83.0 vs. 88.2 at 9 responses). The authors argue debate's apparent gain is functionally the same aggregation-over-samples mechanism as self-consistency, differing only in whether the final vote is taken by the model or by majority count, and that the "critique" framing is not supported once cost is matched.

Third (Section 5), the authors revisit Self-Refine's (Madaan et al., 2023) constrained-generation task (CommonGen-Hard: write a coherent sentence using 20–30 given concepts, scored by concept coverage), noting that the original initial-generation prompt never states the "use all concepts" requirement, which appears only in the feedback prompt. Adding that requirement directly to the initial prompt ("Standard Prompting (ours)") raises coverage to 81.8% without any self-correction step, exceeding both of the previously published self-correction results (67.0% and 61.1%, Table 8) obtained with the under-specified initial prompt; applying the self-correction procedure on top of the stronger initial prompt again reduces performance (81.8→75.1). The authors conclude the earlier reported gain reflected an uninformative initial prompt rather than a correction capability.

## Learnings

Several reported "self-correction" gains in prior work rely on oracle labels that check ground-truth correctness to decide when to stop revising an answer. Once that oracle signal is removed, the same procedures reverse and the model's own judgment of correctness is not a reliable substitute; any self-correction or self-critique evaluation should be checked for whether ground truth is quietly gating the revision loop rather than being absent as claimed.

Techniques that make multiple model calls, such as multi-agent debate, need to be compared against a resampling baseline (self-consistency) at an equal number of total calls, not against a single-pass baseline. When matched for cost, debate's apparent improvement over standard prompting collapses to the same mechanism as sampling multiple answers and voting, with the model-driven vote actually doing worse than plain majority count.

A self-correction pipeline can look like it fixes reasoning errors when it is actually fixing an incomplete task specification: if a constraint (such as "the output must include every listed item") is stated only in the feedback prompt and not in the initial prompt, moving that constraint into the initial prompt alone can outperform the full self-correction pipeline, and self-correction on top of the corrected prompt then hurts rather than helps.

## Verification

Verification is the paper's central subject, though framed as a critique of self-judgment rather than a proposal for a better verifier. The paper treats "can the model tell whether its own reasoning is correct, without external help" as the question, and answers it empirically: without a ground-truth or tool-based signal, models are more likely to turn a correct answer into an incorrect one than the reverse (Figure 1's per-benchmark, per-model transition counts), so letting a model gate its own revision reduces net accuracy. GPT-4 and GPT-4-Turbo are shown to be more conservative (retaining their initial answer 88–96% of the time) than GPT-3.5 and Llama-2, but this reduces the damage rather than reversing it into a net gain. The paper reports no precision/recall numbers for a self-judgment "verifier" as such; the transition-rate breakdown functions as an implicit error analysis of how often self-judgment moves an answer in the wrong direction. The paper explicitly leaves open, and does not dispute, that external verifiable feedback (executed code, retrieved evidence, a separately trained critic model) is a different and more promising regime, citing prior work (self-debugging with execution feedback, CRITIC's tool-interactive critiquing, PRM-style trained verifiers) as the contrast case.

## Field context

This paper is a direct methodological response to the wave of 2023 "self-refine" and "self-correct" papers (Self-Refine, RCI, Reflexion) and to multi-agent debate work (Du et al., 2023; Liang et al., 2023), all of which it re-implements using the original papers' own prompts and benchmarks rather than proposing a new method. Its contribution is identifying three specific confounds — oracle-label leakage, cost-unmatched baselines, and under-specified initial prompts — in claims that were, at the time, widely cited as evidence that LLMs can self-improve their reasoning through introspection. It sits upstream of, and is frequently invoked by, later work on chain-of-thought faithfulness and reasoning-instruction compliance that treats a model's self-report about its own reasoning with skepticism (a theme also visible in this corpus's review of 2604.27251, which documents models' chain-of-thought diverging from their actual reasoning operation). The paper's own framing draws a clear boundary it does not cross: it argues against unaided intrinsic self-correction specifically, not against feedback-driven correction in general, and names externally verifiable feedback (execution, tools, trained critics) as the more promising direction, a boundary later verification-focused work has generally respected.

## Critical discussion

The paper's central methodological move, holding inference cost and the presence of an oracle constant while removing each in turn, is exactly the right design to isolate genuine self-correction ability from a verifier leak or a resampling effect, and it produces directly comparable before/after numbers on the same benchmarks and models the original papers used. The multi-agent debate and constrained-generation replications in particular are surgical: both identify a single, specific, checkable confound (an unmatched call budget; an omitted constraint in the initial prompt) and show the effect disappears once that confound is controlled.

The main intrinsic self-correction results rest on fairly small, cost-driven samples for every model beyond GPT-3.5-Turbo (200 questions per dataset, 100 for HotpotQA), and the paper reports no confidence intervals or repeated-run variance anywhere in Tables 3–6, even though several of the reported drops are only a few accuracy points (for example GPT-4-Turbo's CommonSenseQA moving from 84.0 to 81.5 to 83.0 across rounds). Some of this movement plausibly reflects sampling noise on a 200-item set rather than a directional effect, and the paper does not give the reader a way to judge which is which. Decoding temperature is also not held constant across the model comparisons (temperature 1 for GPT-3.5/GPT-4, temperature 0 for GPT-4-Turbo/Llama-2), a choice the authors explain as deliberately probing different decoding algorithms, but it means the paper cannot cleanly separate how much of GPT-4-Turbo and Llama-2's answer-retention behavior is a property of the model versus a property of greedy decoding at temperature 0. The multi-agent debate result is demonstrated on one benchmark (GSM8K) at one configuration (3 agents, 2 rounds), enough to make the specific point that this configuration is not obviously better than self-consistency at matched cost, but not enough to rule out some other debate configuration or task showing a genuine critique effect beyond resampling.

What remains well supported after these caveats: on the four benchmarks and four model families tested, letting a model revise its own reasoning without an oracle stop signal or external tool reliably reduces accuracy rather than improving it, and two specific, previously influential claims (oracle-style self-correction gains, and the Self-Refine constrained-generation result) are traced to identifiable confounds rather than a demonstrated self-correction capability. The paper does not claim, and should not be read as claiming, that no form of model-driven revision can ever help; it argues specifically against the unaided, no-feedback setting it defines and tests.

## Relevance to us

This is early, clean evidence for a caution already built into our verification thinking: same-model self-critique, with no external check, is not a trustworthy gate for revising a reasoning trace, and it can actively make a correct answer worse more often than it fixes a wrong one. For any physics-reasoning pipeline where we consider adding a self-review or "double-check your work" step, this argues for two concrete controls before crediting the step with a gain: compare it against plain resampling and majority vote at the same number of model calls (since a review step that just samples again and re-decides may only be self-consistency in disguise), and make sure the check driving any revision is not simply the same model re-reading its own text, but something with independent signal (a deterministic dimensional or numerical check, executed code, or a genuinely separate verifier). It also flags a specific evaluation trap worth checking in our own harnesses: an apparent improvement from a "review your answer" prompt can come from that second prompt stating the task more completely than the first, rather than from any actual error correction, which is checkable by moving the same information into the initial instruction and seeing whether the gain survives.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| intrinsic self correction without oracle labels | reasoning accuracy on GSM8K CommonSenseQA HotpotQA | contradicts | 0.85 | papers/canonical/2026-06-09/24selfcor.md:L46 | Accuracy drops for all four models across all three benchmarks once the oracle stop signal is removed |
| oracle labels gating the correction loop | reported self correction accuracy gains in prior work | implies | 0.8 | papers/canonical/2026-06-09/24selfcor.md:L43 | Reproducing RCI and Reflexion with oracle labels reproduces their reported gains, which vanish without the oracle |
| multi agent debate at matched call budget | accuracy relative to self consistency voting | contradicts | 0.7 | papers/canonical/2026-06-09/24selfcor.md:L133 | Debate underperforms self-consistency at 6 and 9 matched total responses on GSM8K |
| adding the missing constraint to the initial prompt | constrained generation concept coverage without self correction | improves | 0.75 | papers/canonical/2026-06-09/24selfcor.md:L139 | The corrected initial prompt alone scores 81.8 percent coverage, above the previously published self-correction results |
