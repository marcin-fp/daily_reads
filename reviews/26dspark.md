---
schema_version: 1
paper: slug:26dspark
title: "DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation"
authors:
  - Xin Cheng
  - Xingkai Yu
  - Chenze Shao
  - Jiashi Li
  - Yunfan Xiong
  - Yi Qian
  - Jiaqi Zhu
  - Shirong Ma
  - Xiaokang Zhang
  - Jiasheng Ye
  - Qinyu Chen
  - Chengqi Deng
  - Jiping Yu
  - Damai Dai
  - Zhengyan Zhang
  - Yixuan Wei
  - Yixuan Tan
  - Wenkai Yang
  - Runxin Xu
  - Yu Wu
  - Zhean Xu
  - Xuanyu Wang
  - Muyang Chen
  - Rui Tian
  - Xiao Bi
  - Zhewen Hao
  - Shaoyuan Chen
  - Huanqi Cao
  - Wentao Zhang
  - Anyi Xu
  - Huishuai Zhang
  - Dongyan Zhao
  - Wenfeng Liang
publication:
  first_public_date: "2026-07-06"
  first_public_date_precision: day
  venue: arXiv
  status: preprint
  reviewed_version: v1
  reviewed_version_date: "2026-07-06"
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-06-09/26dspark.md
raw: papers/raw/2026-06-09/26dspark-pdf.md
source_url: https://arxiv.org/abs/2607.05147
organizations:
  - name: Peking University
    sector: academia
    roles: [author_affiliation]
    authors: [Xin Cheng, Huishuai Zhang, Dongyan Zhao]
    grants: []
  - name: DeepSeek-AI
    sector: industry
    roles: [author_affiliation]
    authors: [Xin Cheng, Xingkai Yu, Chenze Shao, Jiashi Li, Yunfan Xiong, Yi Qian, Jiaqi Zhu, Shirong Ma, Xiaokang Zhang, Jiasheng Ye, Qinyu Chen, Chengqi Deng, Jiping Yu, Damai Dai, Zhengyan Zhang, Yixuan Wei, Yixuan Tan, Wenkai Yang, Runxin Xu, Yu Wu, Zhean Xu, Xuanyu Wang, Muyang Chen, Rui Tian, Xiao Bi, Zhewen Hao, Shaoyuan Chen, Huanqi Cao, Wentao Zhang, Anyi Xu, Wenfeng Liang]
    grants: []
artifacts:
  - type: code
    url: https://github.com/deepseek-ai/DeepSpec
  - type: model
    url: https://github.com/deepseek-ai/DeepSpec
facets:
  domains: [machine-learning, systems, natural-language-processing]
  paper_type: [method, system, experiment]
  methods: [speculative-decoding, semi-autoregressive-generation, confidence-calibration, temperature-scaling, rejection-sampling]
  models: [DeepSeek-V4, DeepSeek-V4-Flash, DeepSeek-V4-Pro, Qwen3-4B, Qwen3-8B, Qwen3-14B, Gemma4-12B, Eagle3, DFlash]
  benchmarks: [GSM8K, MATH500, AIME25, MBPP, HumanEval, LiveCodeBench, MT-Bench, Alpaca, Arena-Hard]
assessment:
  extract_quality: good
  extract_limitations: [figures-not-visually-assessed]
  critical_flags: [incomplete-reporting]
metadata_notes: "No funding or acknowledgments section is present in the extracted text; this appears to be an internally funded DeepSeek-AI production research report with academic co-authorship from Peking University, and no external grants are stated. The paper's numerous figures (position-wise acceptance curves, throughput-vs-TPS plots, reliability diagrams) render as unlabeled image placeholders in the extraction; numeric details used in this review are drawn from the surrounding prose discussion of each figure rather than from direct inspection of the plots themselves."
---

Citation: Cheng, X., Yu, X., Shao, C., Li, J., Xiong, Y., et al. DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation. arXiv:2607.05147, 2026.

## What this paper is about

Large language models normally generate one token at a time, which is slow. Speculative decoding speeds this up by having a small, cheap "draft" model propose several tokens at once, which the full model then checks in a single pass, keeping only the tokens that check out. Recent drafters that propose an entire block of tokens in one shot are fast but get worse and worse toward the end of the block, since each position is guessed independently of the others; and simply checking every proposed token wastes valuable compute on tokens that were unlikely to survive the check anyway, especially when a server is busy with many users at once. DSpark, from DeepSeek-AI, addresses both problems together: it adds a small amount of genuine token-to-token dependency back into the fast parallel drafter, and it uses a calibrated, load-aware scheduler to decide, request by request, exactly how much of each draft block is worth checking given how busy the system currently is. Deployed in DeepSeek's live production serving system, it delivers substantial real-world speedups over the prior production setup.

## Extended summary

Speculative decoding's core guarantee is exactness: a draft token is accepted with probability min(1, target-probability / draft-probability), so the accepted output is distributed exactly as if the target model had generated it alone, at no quality cost. The per-token latency is (drafting time + verification time) divided by the number of accepted tokens per round, so speedup comes from drafting faster, drafting better, or verifying smarter. Autoregressive drafters (each position conditioned on the previous one) model dependencies well but get slower as the block grows, forcing small, shallow drafters. Parallel drafters like DFlash, the paper's main baseline, produce an entire block in one forward pass regardless of block size, which lets them use deeper networks, but because each position is predicted independently, they suffer "multi-modal collisions" (for example, mixing "of course" and "no problem" into "of problem") and their accuracy decays rapidly toward the end of the block.

DSpark's first component, semi-autoregressive generation, keeps a deep parallel backbone (DFlash, with a minor modification treating the anchor token itself as the first prediction position) for the initial pass, then adds a lightweight sequential head that reintroduces genuine left-to-right conditioning within the block via a small transition-bias term added to the backbone's base logits, factorized as a proper autoregressive chain so that exact per-token probabilities remain computable (required for the rejection-sampling rule to stay exact). Two instantiations are given, a low-rank "Markov" head (used by default) and a small RNN-style head; the Markov head keeps both storage and per-step compute small even for large vocabularies.

The second component, confidence-scheduled verification, addresses the separate problem of deciding how much of a draft block is worth checking. A lightweight confidence head estimates, for each draft position, the conditional probability that the token will survive verification given all prior tokens in the block were accepted, trained against the analytically defined true acceptance rate (one minus half the total variation distance between the draft and target distributions). Because neural confidence estimates are typically overconfident, the raw scores are recalibrated with "Sequential Temperature Scaling," a left-to-right, order-preserving calibration of the cumulative product of per-position confidences against a held-out validation set, which the paper shows reduces expected calibration error from 3-8% to roughly 1% while leaving the relative ranking of tokens unchanged. These calibrated cumulative survival probabilities feed a hardware-aware prefix scheduler that, given a batch of concurrent requests and a profiled engine throughput curve (steps per second as a function of batch size), greedily admits the globally most-likely-to-survive draft tokens across all requests until adding more would reduce total expected system throughput, an approach the paper shows is exactly the greedy-optimal allocation because per-position survival probability is monotonically non-increasing along a block. A key correctness constraint is that speculative decoding's exactness requires admission decisions not to depend on future, not-yet-sampled tokens; because the confidence head's own computation depends on the actual previously sampled token, an unconstrained retrospective search over the whole batch would violate this and bias the output distribution (the paper reports a concrete counterexample of this failure mode in an appendix), which is why the deployed algorithm stops the greedy search as soon as it would reduce throughput rather than searching further.

Offline evaluation across four target models (Qwen3-4B/8B/14B and Gemma4-12B) and nine benchmarks in math, code, and chat, with all drafters retrained under identical conditions for a fair comparison, shows DSpark improving the macro-average accepted length over the autoregressive Eagle3 baseline by 26.7-30.9% and over the parallel DFlash baseline by 16.3-18.4%, consistently across model families. A fine-grained, position-wise analysis explains a counter-intuitive pattern: at the very first draft position, the deep parallel drafter has a substantial accuracy edge over the shallow autoregressive drafter purely from architectural capacity, and because speculative decoding is a strict prefix-matching process, this first-position advantage carries outsized leverage even though the parallel drafter's accuracy then decays badly at later positions (dropping from roughly 0.87 to 0.78 on code, for example) while the autoregressive drafter's accuracy holds steady or even improves deeper into the block. DSpark's sequential head is shown to substantially close this later-position gap while inheriting the parallel backbone's strong first-position accuracy. A depth ablation finds a 2-layer DSpark outperforms a 5-layer DFlash, and a proposal-length ablation finds DSpark's relative advantage over DFlash grows from roughly 15-18% at a block size of 7 to 22-30% at a block size of 15, while the added sequential-sampling loop adds only 0.2-1.3% to per-round latency at a serving batch size of 128. A static confidence-threshold sweep confirms the confidence head can identify and prune low-value suffix tokens, with the effect strongest on open-ended chat (acceptance rate rising from 45.7% to 95.7% as the threshold increases) and milder on structured math and code tasks that already have naturally higher acceptance.

Deployed within the DeepSeek-V4-Flash and DeepSeek-V4-Pro production serving systems against the prior MTP-1 production baseline, DSpark is evaluated on live user traffic at several interactivity service-level-agreement (SLA) anchors. At moderate SLAs, DSpark improves aggregate throughput by 51% (Flash) and 52% (Pro); at the strictest SLAs, where the single-token MTP-1 baseline approaches its operational limit and can sustain only a small concurrent batch, DSpark shows a nominal 661% (Flash) and 406% (Pro) throughput advantage, which the authors explicitly characterize as evidence of extending the feasible interactivity frontier rather than as a representative multiplicative speedup over a well-utilized baseline. At matched practical throughput levels, a more stable basis for comparison, DSpark accelerates per-user generation speed by 60-85% (Flash) and 57-78% (Pro). Deploying the theoretically exact scheduler in production required adapting it to an asynchronous pipeline compatible with continuous CUDA-graph replay and zero-overhead scheduling: rather than computing the current step's admission capacity synchronously (which would stall the GPU pipeline), the deployed scheduler approximates the batch capacity limit using confidence-head outputs from two steps prior, while still sorting candidate tokens by their actual, up-to-date confidence scores; the paper argues this preserves the causality (non-anticipating) requirement because the capacity estimate depends only on information from two steps earlier, not on the currently sampled token. The paper's own limitations note that DSpark still incurs a fixed draft-side cost to generate the initial block regardless of a request's eventual acceptance rate, which is unrecoverable for complex, low-acceptance queries, and suggests difficulty-aware early exiting within the draft model as a direction for addressing this.

## Learnings

A parallel drafter's overall advantage over an autoregressive one in speculative decoding can come almost entirely from a large accuracy edge at the very first draft position, not from being uniformly better across the block. A position-wise conditional-acceptance analysis shows the parallel drafter actually decays badly at later positions relative to the autoregressive drafter, but because speculative decoding is a strict prefix-matching process, an error early in the block invalidates everything after it, so a first-token capacity advantage carries disproportionate leverage. This is a transferable lesson for evaluating any prefix-dependent, sequential decision process: where in a sequence an error occurs matters far more than the raw count of positions with good average accuracy.

A small, targeted amount of genuine sequential dependency added to an otherwise-parallel model can be dramatically more parameter-efficient than simply scaling up the parallel architecture. A 2-layer semi-autoregressive drafter outperformed a 5-layer purely parallel drafter, and the added sequential-sampling loop cost only a fraction of a percent of additional per-round latency while delivering up to a 30% improvement in accepted length, suggesting that reintroducing a small, cheap inductive bias for a known structural weakness (independence across positions) beats brute-force capacity scaling that does not address that weakness directly.

A confidence estimator can be excellent at ranking candidates (here, ROC-AUC of 0.81-0.90) while still being badly miscalibrated in absolute terms (3-8% expected calibration error, always overconfident), and this distinction only matters once a downstream decision needs the actual probability value rather than just a relative ordering. A scheduler that must compute an expected cumulative survival probability to trade off against measured system throughput cannot safely use raw, overconfident scores, which is why an explicit, order-preserving post-hoc calibration step was applied before the scores were used for resource allocation rather than only for filtering or ranking.

## Verification

Verification is the structural core of this paper's subject matter, not a side concern: speculative decoding's entire value proposition rests on a formally exact verification rule (accepting a draft token with probability min(1, target-probability/draft-probability)) that preserves the target model's output distribution exactly, and a "non-anticipating" causality requirement that admission decisions must not depend on not-yet-sampled future tokens, which the paper treats carefully, including reporting a concrete counterexample of what goes wrong if this requirement is violated. The paper also demonstrates good practice in verifying its own confidence estimator before trusting it for a decision: a reliability-diagram check shows the raw confidence head is well-discriminating but overconfident, and an explicit post-hoc calibration step (Sequential Temperature Scaling) is applied and separately validated (reducing expected calibration error from 3-8% to roughly 1%) before the calibrated scores are used to drive the production scheduler's throughput optimization. However, the production deployment introduces a load-bearing correctness compromise that is argued for in prose rather than independently confirmed empirically within the paper: to fit asynchronous, zero-overhead serving infrastructure, the deployed scheduler approximates batch capacity using confidence estimates from two steps prior rather than the current step, and the paper argues this still satisfies the causality requirement needed for the exact-distribution guarantee, without reporting a direct empirical check (such as a distributional or downstream-quality comparison between the exact synchronous scheduler and the deployed asynchronous approximation) confirming that the guarantee holds in the actual production system.

## Field context

This paper sits within the fast-moving speculative decoding literature that followed the field's foundational exact-verification formulation (Leviathan et al., 2023; Chen et al., 2023), and builds most directly on DFlash, a state-of-the-art parallel, diffusion-inspired drafter that DSpark adopts as its own parallel backbone and extends with a sequential correction module. It distinguishes itself from prior confidence-based adaptive-length approaches, which the paper characterizes as typically relying on static per-request thresholds or rank-based heuristics evaluated under isolated, single-request assumptions, by formulating verification-length selection as a system-wide throughput-maximization problem with a calibrated, globally optimal greedy solution, and by validating this not only on offline benchmarks but inside a real, large-scale production serving system (DeepSeek-V4) under live user traffic, which the paper explicitly notes is a step beyond most cited prior work in this area. It also relates its sequential-head design to a specific line of prior non-autoregressive generation research (CRF-based and CTC-based sequential correction layers), explaining precisely why those designs cannot provide the exact per-token probabilities speculative decoding requires (a globally normalized partition function or marginalized alignment paths, respectively) while its own local, exactly-normalized sequential head can. Within this corpus, this is a pure LLM-inference-systems paper with no direct physics content, and its closest conceptual echo elsewhere in this corpus is the general theme (visible in reviews of 25tpbench and 24semant) that a confidence or judgment signal is only as useful as its calibration against ground truth, here applied to a production engineering problem rather than a scientific verification one.

## Critical discussion

The paper's offline evaluation methodology is a strength worth naming directly: all drafters are retrained under identical conditions, on the same data, with matched architectural choices (aligned block sizes and target-feature layers), which avoids the weak-baseline problem of comparing a well-tuned new method against an under-tuned or mismatched prior one. The paper is also commendably direct about the limits of its own most dramatic-looking headline numbers: at the strictest interactivity SLAs, where the reported relative throughput gain reaches 661% and 406%, the authors explicitly state this reflects the baseline collapsing into a small, poorly utilized concurrent batch near its operational limit, rather than a representative multiplicative speedup, and they direct the reader instead to the more stable matched-throughput comparison (60-85% and 57-78% faster). Flagging one's own most impressive-sounding statistic as not the right one to generalize from is a genuinely good practice worth crediting.

The one significant gap is the production scheduler's central correctness claim. Speculative decoding's entire appeal rests on being provably lossless, and the paper is careful to establish this property for its idealized, synchronous scheduling algorithm, including a proof sketch and a documented counterexample for what breaks the guarantee. But the actual deployed system uses a materially different, approximate scheduler (relying on confidence estimates from two steps prior to fit asynchronous, zero-overhead serving infrastructure), and the paper's argument that this still preserves the exact-distribution guarantee is presented as a prose argument rather than backed by a direct empirical check, such as comparing output distributions or downstream task quality between the exact and the approximate scheduler under production conditions (incomplete-reporting). Given that the paper's central selling point throughout is that speculative decoding, and by extension DSpark, delivers speedups "at no quality cost," this is the one place where the paper's evidentiary standard drops from the rigor shown everywhere else, and it is precisely the place, a real-world engineering compromise made to satisfy infrastructure constraints, where an empirical check would matter most. Relatedly, the confidence head's reported calibration quality (ROC-AUC 0.81-0.90, post-calibration ECE around 1%) is demonstrated in detail on one dataset (Alpaca) in the main reliability-diagram figure, even though the paper's own domain-variance analysis elsewhere shows acceptance behavior differs substantially between math, code, and chat; it is not fully clear from the text whether the reported post-calibration ECE is representative across all three domains or specific to the one shown.

What remains well supported: the core semi-autoregressive architecture change is demonstrated with a genuinely fair, matched-condition offline comparison across four target models and nine benchmarks, with a specific and well-evidenced mechanistic explanation (the position-wise leverage argument) for why it works rather than simply reporting an aggregate number; the depth and proposal-length ablations isolate the sequential head's contribution cleanly and quantify its negligible latency cost directly; and the production deployment results, read at the matched-throughput comparison points the authors themselves recommend rather than at the most extreme SLA anchors, represent a real, substantial, and honestly characterized improvement over an established production baseline.

## Relevance to us

This is a pure LLM-inference-systems paper with no physics content, and most of its substance, drafter architecture design and production serving infrastructure, is not directly applicable to our work. One technique is worth noting as a general, transferable pattern rather than a specific result to import: the explicit discipline of checking whether a confidence signal is well-calibrated in absolute terms, not just good at ranking, before trusting it for a decision that depends on the actual probability value (here, a resource-allocation scheduling decision; in our own context, potentially a decision about how much verification effort to spend checking a candidate physics derivation step based on an estimated confidence that it is correct). The paper's finding that a well-discriminating estimator can still be substantially overconfident, and that a simple, order-preserving post-hoc calibration step measurably fixes this before the score is used for a downstream resource-allocation decision, is a directly reusable pattern for any graded verification stack we build that wants to spend more scrutiny on lower-confidence candidates and less on higher-confidence ones (a cost-aware verification allocation problem structurally similar to DSpark's own "verify smarter, not longer" framing), as long as the confidence signal driving that allocation is calibrated first. Beyond this one methodological parallel, the paper's substantive contributions (semi-autoregressive drafting, hardware-aware serving schedulers) are not load-bearing for our own research program and this review does not force a broader connection.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| semi-autoregressive sequential head on a parallel drafter backbone | accepted length versus purely parallel and purely autoregressive drafters | improves | 0.85 | papers/canonical/2026-06-09/26dspark.md:L184 | DSpark improves macro-average accepted length by 16 to 31 percent over DFlash and Eagle3 across all target models |
| post hoc sequential temperature scaling calibration | expected calibration error of survival probability estimates | improves | 0.8 | papers/canonical/2026-06-09/26dspark.md:L355 | Calibration reduces expected calibration error from 3 to 8 percent down to roughly 1 percent |
| hardware aware prefix scheduler under live production traffic | per user generation speed at matched throughput versus MTP-1 baseline | improves | 0.75 | papers/canonical/2026-06-09/26dspark.md:L416 | DSpark accelerates per-user generation speed by 60 to 85 percent on Flash and 57 to 78 percent on Pro |
| parallel drafter's first draft position accuracy advantage | overall accepted length advantage despite later position suffix decay | implies | 0.7 | papers/canonical/2026-06-09/26dspark.md:L214 | Prefix matching gives the first position outsized leverage over the final accepted length |
| asynchronous scheduler using two step stale confidence estimates | preservation of the exact lossless target distribution under production constraints | implies | 0.5 | papers/canonical/2026-06-09/26dspark.md:L373 | Argued via a causality argument in prose rather than confirmed by a direct empirical distributional check |
