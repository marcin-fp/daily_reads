# Voice

Write as a scientist talking to another scientist. Precise language, ordinary words. If a specialist term is the shortest honest name, use it once and then speak in that meaning. Do not invent compound labels, product-speak, or checklist slang.

First person and "we" are fine. No Slack hooks ("Interesting Paper!"). No em dashes. Do not open every bullet with a bold fragment. Bold is for rare emphasis, not for list scaffolding.

The Discussion should feel like a human note: a claim, a caveat, a contrast, then what still holds. Hedging is allowed when the evidence is thin ("arguably", "to be frank", "this is only on their distribution"). Theatrical toughness is not.

## Say the thing, then say how

Bad: "define the knob-freedom map from the checklist alone"

Better: "Using the repository's steering specification, identify which inference-time control variables can be tuned in future experiments. This maps available parameters without requiring weight edits or custom decode loops."

Bad: "assign in-surface / approximate / reject verdicts"

Better: "Assess whether candidate steering strategies (arms A0–A3) are implementable in the existing codebase. Label each as in-surface (natively supported), approximate (requires placeholders or workarounds), or rejected (requires unsupported weight or code edits)."

The second versions name the object, the action, and the criterion. The first versions assume the reader already lives in your private jargon.

## Learnings

This section is a short list of reusable findings, not a recap of the paper. One finding per paragraph. Two or three sentences is the sweet spot: enough to say what happened, why it is surprising or useful, and the caveat that would change how you use it. Skip the section if nothing transfers.

Write full sentences. Do not start with a bold slogan. Do not dump TAXONOMY.md.

Examples of the target length and tone:

Varying the temperature during supervised fine-tuning usually improves out-of-distribution detection. Interestingly, the active ingredient appears to be variation itself rather than the specific shape of the schedule.

A fusion of N answers often beats picking the single best of N. The method struggles, however, on mathematics-oriented numerical tasks, which is uncomfortably close to physics.

Same-model self-critique misses a large fraction of the model's own exploits. If the paper uses an LLM judge from the same family as the generator, that is not an independent check.

## Critical, not theatrical

Discussion is where you scrutinize the paper. Restating the abstract in a colder tone is not a review. Neither is a sales recap.

A review is allowed to say a paper is wrong, incomplete, or asking the wrong question. Ground that in what the paper actually did: missing or weak baseline, circular eval, contamination, unmeasured coverage, a claim stronger than the setup, a mechanism that does not follow from the result. If you cannot point at evidence, do not perform skepticism as a style.

Praise is also allowed when earned. Empty toughness is as fake as empty enthusiasm.

## Lists

Use lists when there are several distinct points. Write them as sentences. Do not turn the review into a taxonomy dump.
