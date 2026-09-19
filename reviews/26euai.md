---
schema_version: 1
paper: slug:26euai
title: "Challenges in applying the EU AI act research exemptions to contemporary AI research"
authors:
  - Janos Meszaros
  - Isabelle Huys
  - John P. A. Ioannidis
publication:
  first_public_date: "2026-01-31"
  first_public_date_precision: day
  venue: "npj Digital Medicine"
  status: journal
  reviewed_version: published
  reviewed_version_date: "2026-01-31"
reviewed_at: "2026-09-17"
canonical: papers/canonical/2026-05-06/26euai.md
raw: papers/raw/2026-05-06/26euai-pdf.md
source_url: https://doi.org/10.1038/s41746-025-02263-0
organizations:
  - name: Clinical Pharmacology and Pharmacotherapy, Department of Pharmaceutical and Pharmacological Sciences, KU Leuven
    sector: academia
    roles: [author_affiliation]
    authors: [Janos Meszaros, Isabelle Huys]
    grants: []
  - name: Center for IT & IP law (CiTiP), KU Leuven
    sector: academia
    roles: [author_affiliation]
    authors: [Janos Meszaros, Isabelle Huys]
    grants: []
  - name: Meta-Research Innovation Center at Stanford (METRICS), Stanford University
    sector: academia
    roles: [author_affiliation]
    authors: [John P. A. Ioannidis]
    grants: []
  - name: Innovative Medicines Initiative 2 Joint Undertaking (EU Horizon 2020)
    sector: other
    roles: [funder]
    authors: []
    grants: ["945358 (Bigpicture project)"]
artifacts: []
facets:
  domains: [ai-policy, ai-regulation, law]
  paper_type: [position, analysis]
  methods: [doctrinal-legal-analysis, scenario-based-reasoning]
  models: []
  benchmarks: []
assessment:
  extract_quality: good
  extract_limitations: [table-extraction-damaged, figures-not-visually-assessed]
  critical_flags: []
metadata_notes: "The extract gives Received (2025-06-14) and Accepted (2025-12-07) dates but no explicit 'Published online' line; first_public_date (2026-01-31) and the journal/volume/article-number (npj Digital Medicine 9:288) are corroborated via web search against the article's Nature/PubMed listing rather than the extract itself. The Innovative Medicines Initiative 2 Joint Undertaking is a public-private partnership (European Commission plus the EFPIA pharmaceutical-industry association); it is coded here as sector 'other' rather than 'government' or 'industry' to avoid overstating either side. The acknowledgements state the funder had no role in study design, analysis, or the decision to publish. Table 2's checkmark/Ø layout renders as a loosely ordered list of symbols in the extraction and is reconstructed here from the surrounding prose rather than read directly off a clean table."
---

Citation: Janos Meszaros, Isabelle Huys, and John P. A. Ioannidis. Challenges in applying the EU AI act research exemptions to contemporary AI research. npj Digital Medicine 9, 288 (2026). https://doi.org/10.1038/s41746-025-02263-0

## What this paper is about

The EU's AI Act carves scientific research out of its regulatory scope, on the reasonable idea that a system still being built or tested in a lab shouldn't face the same rules as one already making decisions about real people. This paper is a legal analysis arguing that the line the Act draws — lab-based development versus real-world use, and research versus commercial activity — is much blurrier in practice than the text assumes, especially for AI systems that increasingly train and test on live data as a normal part of development. Using the Act's own definitions and a set of worked scenarios, the authors show where that ambiguity could let some AI activity dodge oversight it should probably get, or conversely let genuine research get miscategorized as regulated commercial deployment.

## Extended summary

The paper is a doctrinal legal analysis (the authors' own description: examining the Act's text, related EU legislation, and Commission guidance, supplemented by scenario-based reasoning; no empirical data, systems, or experiments are involved). It focuses on two provisions the authors label, for clarity, the "development-phase exemption" (Article 2(8): the Act does not apply to research, testing, or development of AI systems before they are placed on the market or put into service, except that "testing in real world conditions shall not be covered by that exclusion") and the "scientific-use exemption" (Article 2(6): the Act does not apply to AI systems or models, including their output, developed and put into service solely for scientific research).

For the development-phase exemption, the authors work through the Act's own definitions of "putting into service" (first use for the system's intended purpose, e.g. a hospital starting to use a diagnostic AI) and "testing in real-world conditions" (temporary use outside the lab, with participant consent and regulator approval, to collect data and verify conformity before market placement or service). They note the Act does not itself define "real-world conditions," leaving its scope to be inferred from surrounding provisions — an interpretive gap the paper treats as consequential because it determines when a system is deemed to have left the lab. The paper's central hypothetical is a system placed silently in a hospital room, capturing data but showing no output to clinicians: the authors argue whether this counts as exempt lab development or regulated real-world testing turns on the system's intended purpose — if the silent capture serves the system's eventual diagnostic/treatment-support function, it may already constitute testing "for its intended purpose" and thus fall outside the exemption, even though no output is ever shown to a clinician. A table of four hypothetical circumvention methods (offshore cloud deployment testing on non-EU patients; a "synthetic environment" quietly fed live data; splitting a multi-model system so only one component is declared for real-world testing while others operate undeclared; silent on-site data capture) illustrates possible strategic exploitation of this ambiguity — the authors explicitly label these as hypothetical, and immediately note that most would likely fail under Article 2's extraterritorial scope (the Act applies to any system affecting individuals in the EU regardless of where it is hosted or tested) and Recital 22, which reinforces that scope.

For the scientific-use exemption, the paper walks through four combinations of whether a system was developed and/or put into service "for the sole purpose of scientific research," summarized in a table: research-development plus research-deployment is exempt; non-research-development plus research-deployment is not exempt (buying a commercial tool and only using it for research does not qualify); non-research development plus non-research deployment is not exempt; and the fourth combination — developed for a non-research purpose but the developers changed intent mid-project and it was ultimately deployed solely for research — is flagged by the authors as genuinely unclear under a literal reading, since the exemption's "sole purpose" language does not obviously accommodate a change of purpose partway through a project. The paper connects this to Recital 25, which the authors read as confirming that a system merely being used for research by its acquirer (rather than being built for that sole purpose) does not qualify.

The Discussion section extends this into broader structural concerns: the Act's exemption logic assumes research and commercial activity are cleanly separable, which the authors argue does not match how much contemporary AI research operates (public-private partnerships, university-industry collaborations, and funder-mandated knowledge-transfer obligations that push research findings toward commercial partners), and note that a comparable lack of a harmonized "scientific research" definition already exists under the GDPR and the EU Copyright Directive's research exemptions. They also raise a distinct concern for non-profit or humanitarian AI (e.g., climate modelling, disease prediction, disaster response) freely distributed to public or nonprofit users: if that distribution counts as "real-world use," such projects could be forced into full compliance despite no commercial motive, potentially ceding that space to commercial (including non-EU) providers instead. The paper's recommendations are: clearer regulatory definitions of "scientific research" and "real-world conditions," including explicit treatment of silent-mode deployments; a structured framework for responsible knowledge transfer between academic and commercial partners that doesn't treat every such partnership as disqualifying; and published practical implementation guidelines, developed collaboratively with researchers and industry and periodically revisited as AI capabilities change.

## Learnings

Under the AI Act as the authors read it, an AI system does not need to produce a visible output to count as being tested in "real-world conditions": if a system silently captures data in a live setting toward its eventual intended purpose (e.g., diagnosis), that data capture can itself satisfy "testing for its intended purpose," meaning invisibility of output does not, by itself, keep a deployment inside the lab-development exemption. This is a specific, non-obvious reading with a direct product-design implication for anyone assuming a "silent shadow-mode" deployment automatically avoids extra regulatory obligations.

A purpose-based exemption test breaks down cleanly when intent changes mid-project: the paper shows that a system built for one purpose (patient diagnosis) but redirected partway through development to a different purpose (research only) produces a genuinely unclear result under the Act's literal "sole purpose" language, neither clearly exempt nor clearly not. This is a specific instance of a more general pattern worth remembering when reasoning about any purpose- or intent-based regulatory or policy carve-out: such tests are comparatively easy to apply to a project with a fixed goal from start to finish, and comparatively hard to apply once the goal itself changes along the way.

## Verification

None. This is a legal-interpretive analysis of regulatory text and hypothetical scenarios, not a study of scientific claims, derivations, or AI system outputs, so the checking apparatus this repo's verification interest tracks (deterministic checks, LLM-as-judge, coverage/precision, agent-trace monitoring) does not apply here. The nearest analogue — how a regulator or researcher would establish, in practice, whether a given deployment satisfies the "sole purpose" or "real-world conditions" tests — is exactly the ambiguity the paper is arguing has not yet been resolved, rather than a checking method the paper itself proposes or evaluates.

## Field context

The paper sits within a growing literature specifically on the EU AI Act's implications for healthcare and digital medicine (the authors cite prior npj Digital Medicine pieces on navigating the Act for healthcare and for regulated digital medical products, and a Health Policy paper on healthcare implications), and situates its central concern — an under-defined "scientific research" carve-out — alongside comparable ambiguities the same lead author has previously examined under the GDPR's research exemption (Meszaros & Ho 2021, cited here) and under the EU Copyright Directive's text-and-data-mining research exemption, suggesting a consistent research programme across multiple EU legal instruments that use similar, loosely defined "research" carve-outs. It also draws on the "Brussels Effect" literature (Bradford 2020; Siegmann & Anderljung 2022) to frame the AI Act's interpretive choices as potentially influencing how other jurisdictions structure their own AI research exemptions. None of these specific precedents are yet reviewed in this corpus. Separately, and not cited by this paper, a web search surfaced a contemporaneous but apparently independent 2026 preprint ("Position: EU AI Act's Research Exemptions Can Break the Publication Norms of Major AI Conferences") making a related argument about the same exemptions from the angle of open-science publication norms at AI/ML conferences rather than healthcare deployment; this is noted here as an external observation from this review's own search, not as a connection the paper itself draws.

## Critical discussion

As a piece of legal scholarship rather than an empirical study, the appropriate standard here is whether the textual and interpretive analysis is well-grounded, not whether it has a control group or a validated benchmark, and by that standard the core analysis holds up: each key interpretive claim is tied to a specific, quoted or paraphrased Article or Recital (Articles 2(6), 2(8), 3(1), 3(9), 3(11), 3(57); Recitals 22 and 25), which a reader can check against the Official Journal text the paper cites. The "silent-mode deployment" hypothetical and the "sole purpose" ambiguity are both derived directly from applying the Act's own stated definitions to a concrete scenario, which is the right method for this kind of claim.

One point of internal tension is worth naming: Table 1 presents four "circumvention methods" as genuine regulatory-arbitrage risks, each paired with a stated "issue" (e.g., "regulatory bodies may have difficulty enforcing compliance on non-EU infrastructure"), but the paragraph immediately following the table asserts that "such strategies are unlikely to succeed under Article 2" because of the Act's extraterritorial scope. The paper does not fully reconcile these two framings — if Article 2's broad territorial reach already closes the legal gap as cleanly as the text suggests, the practical "issue" in each row is arguably not about whether the Act applies (a question of legal scope) but about whether it can actually be enforced against, say, testing conducted on patients outside the EU with no EU touchpoint until a product is later imported — a distinct and harder question about enforcement capacity that the paper raises implicitly (the parenthetical about "difficulty enforcing compliance") but does not develop further. This does not undermine the paper's broader point that ambiguity exists, but it does mean the practical severity of the four illustrated "circumvention methods" is less settled than presenting them as a clean list might suggest.

A second, more structural limitation, which the paper's own Methods section makes transparent rather than hides, is that the analysis is necessarily anticipatory: the AI Act's research exemptions are new enough that the paper works from the statutory text and Commission guidance rather than from observed enforcement decisions or case law interpreting these specific provisions, since none yet exist in the areas discussed. This is an appropriate and disclosed limitation for a paper published this soon after the Act's provisions took effect, not a flaw in execution, but it means every scenario in Tables 1-3 is a prediction about how the text would likely be read, not a report of how it has actually been applied.

The Discussion's recommendations (clearer definitions, a structured knowledge-transfer framework, published implementation guidelines) correctly identify the gaps the analysis surfaces, but stop short of proposing specific replacement language, thresholds, or criteria (for instance, what would concretely distinguish an acceptable university-industry partnership from a strategic reclassification, beyond "transparency requirements"). This is consistent with the genre — the paper's stated goal is to expose ambiguity and argue for clarification, not to draft the clarifying text itself — but it does mean the practical next step (what, specifically, should regulators write) is left open rather than answered.

What remains well supported after these caveats: the central claim that the Act's development-phase and scientific-use exemptions rest on textual boundaries ("real-world conditions," "sole purpose") that are not self-defining and can produce genuinely unclear outcomes in realistic scenarios (silent-mode deployment, mid-project purpose changes, publicly funded partnerships with mandated industry knowledge-transfer) is directly demonstrated by the paper's own worked examples and is a reasonable, well-cited legal-interpretive conclusion. The four specific "circumvention methods," while clearly labeled hypothetical, illustrate the shape of the ambiguity even if their practical viability under Article 2's extraterritorial scope is less resolved than the table alone conveys.

## Relevance to us

None. This is a legal-policy analysis of EU AI regulation as applied mainly to healthcare and general-purpose AI deployment; it does not touch physics, AI-for-science methodology, evaluation, or verification, and none of our tracked tensions, bets, or verification interests are engaged by its content. Forcing a connection here (for example, to hypothetical future regulatory exposure for a physics research tool) would go beyond what the paper actually argues.

## Claims

| from | to | relation | conf | anchor | gloss |
|------|----|----------|------|--------|-------|
| AI Act development-phase exemption | AI systems tested in real-world conditions | contradicts | 0.8 | papers/canonical/2026-05-06/26euai.md:L19 | Act's own text excludes real-world-conditions testing from the development-phase exemption |
| silent-mode real-world data capture | development-phase exemption | contradicts | 0.6 | papers/canonical/2026-05-06/26euai.md:L23 | Authors argue silent capture serving the system's intended purpose may already be real-world testing |
| AI Act scientific-use exemption sole-purpose requirement | systems with changing developer intent over time | contradicts | 0.5 | papers/canonical/2026-05-06/26euai.md:L88 | Literal reading yields an unclear, arguably illogical result for mid-project purpose changes |
| public-private research partnerships in AI | AI Act's research-commercial separability assumption | contradicts | 0.7 | papers/canonical/2026-05-06/26euai.md:L73 | Central thesis: funder-mandated knowledge transfer and industry collaboration blur the Act's research/commercial divide |
