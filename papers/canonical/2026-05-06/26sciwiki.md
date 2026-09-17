
Beyond Retrieval: Compounding Scientific Extelligence with Artificial Intelligence Wikis
Luiz E. F. C. Lopes ,1 Pedro H. M. Zanineli ,1, 2 Bruno Focassio ,1 and Gabriel R. Schleder 1, 2, ∗
1Brazilian Nanotechnology National Laboratory (LNNano/CNPEM), 13083-100, Campinas, SP, Brazil 2Universidade Federal do ABC (UFABC), 09210-580, Santo André, São Paulo, Brazil
Information overload severely bottlenecks scientific synthesis and continuity. We argue that AI-assisted science requires more than retrieval: persistent memory systems that accumulate structured knowledge across interactions must become a foundational layer of future research infrastructure.
Scientific production increasingly depends on the ability to read, catalogue, and correlate information distributed across papers, datasets, code repositories, and laboratory notes. Yet, the rapid growth of scientific literature has transformed this foundational activity into a bottleneck, challenging how researchers monitor advances, identify gaps, evaluate evidence, and preserve continuity across projects.
Large Language Models (LLMs), agentic systems [1], and retrieval-based pipelines increasingly assist these tasks. However, most current approaches remain fundamentally retrieval-centric and session-bound. They retrieve relevant information for a specific query, synthesize a transient response, and discard the contextual structure generated during the interaction. As a result, insights produced during one session rarely become durable components of future scientific reasoning.
We argue that a central limitation of current AI-assisted science is not retrieval quality or context window size alone, but the absence of persistent scientific memory capable of preserving relationships, provenance, and evolving hypotheses across interactions and extended timelines.
I. THE CURRENT LANDSCAPE AND ITS LIMITATIONS: ARE WEBCHAT-AIS ENOUGH?
Large Language Models (LLMs) increasingly support scientific workflows by assisting literature comprehension, synthesis, and task orchestration. Recent work highlights their potential to accelerate components of research while also documenting continual limitations in contextual consistency, provenance tracking, and domain-specific reasoning [2, 3].
Current systems span a spectrum from conversational assistants to retrieval-based scientific platforms capable of indexing corpora of papers and responding to domainspecific queries. Retrieval-Augmented Generation (RAG) approaches represent one of the dominant paradigms, retrieving semantically relevant text chunks from indexed documents to ground generated responses [4].
Despite their utility, most retrieval-based systems remain fundamentally session-bound and fragment-centric.
∗ Corresponding author. gabriel.schleder@lnnano.cnpem.br
Knowledge is typically reconstructed at query time rather than accumulated across time: the relationship between a methodology introduced in one study, a contradictory result encountered months later, and a local experimental observation are rarely preserved as an explicit and evolving structure [5]. Consequently, researchers often return to repetitive cycles of rediscovery of insights.
Recent agentic systems illustrate both the promise and limitations of AI-assisted science. On one end, systems such as Agent Laboratory position the model as a collaborative co-pilot for literature review, experimentation, and report generation under iterative human feedback [6]. On the other, highly autonomous systems such as The AI Scientist explore end-to-end research automation while exposing important weaknesses, including methodological fragility, incorrect implementations, and citation hallucinations [7]. Across these approaches, the limiting challenge increasingly becomes continuity rather than generation itself: preserving structured context and intermediate reasoning across the research lifecycle.
Emerging paradigms such as vibe researching suggest a different direction [8]. Rather than pursuing full scientific automation, these workflows establish a “cognitive delegation boundary”. The researcher acts as a high-level orchestrator who provides tacit domain intuition and critical judgement, while delegating codifiable, labour-intensive tasks to LLM-based agents. In this framing, the challenge shifts from information retrieval alone toward the construction of systems capable of preserving and navigating scientific context over time.
This gap motivates a shift from retrieval-centric paradigms toward enduring scientific memory systems, in which knowledge is not repeatedly reconstructed from isolated prompts but incrementally accumulated, organised, and revised across time.
II. THE SCIENTIFIC LARGE LANGUAGE MODEL WIKI
One response to the limitations of retrieval-centric AI is the Large Language Model (LLM) Wiki paradigm, which reframes language models from conversational interfaces into maintainers of enduring (manifested as type-specific markdown files), structured knowledge bases [9]. In this framing, information is not merely context to be retrieved on demand, but an evolving virtual memory substrate [10].
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_H8YDldw_DYF2vV1D6vb6D2FCU4Qs0eubXspiky8u_1vJcXu-7i0GhIXQ0N4PFk0OJOCG0Xfz9_q9P81mWdf5uFpl2gbSCOAT1zR-lOrFuo1mCSZgdP8mUet5Z6DFgOQqI8YPfEg=w128-h128-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX978aPeDHCovQpE3EA_u1KfXGvI1AqPoDTo5SCzFXC4AL6N5c2Ga-oBgfaaaDeqsELXq-GyRljYEphsEHNNUNTLHgE6DnLv6_YaT39h-kgwpy7xyq-SlDJQlEryaE2tTLsnWwnbng=w128-h128-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9jpdMxgefEyXU668Ihzi0d-momFwu6BLIKYupqup954LFzW003kR6M-07-5mT-7oXhswgRsTvK6Hd4MCrwCBlogtm_g-3R-KClXbnptKYNdbm-PPVYi5t6so3sgot9s8_A22BJbQ=w128-h128-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX__dRhZwnWr6iMR8l9uEDQW76ZeLODYsWoMTs4d9C3eSKKAAkyoj4FLoG9npfj-pvJi1U7j8zPuIRgsZ3Im8iTyP4VmCBFQVzUTjewB4iITngFrLYZU26ZUOb-_v7EJ3x6oKu8YWw=w128-h128-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-MVC1FCQ_4guaYTo--Pp1chZog_Fwca3et8Zm73UN7xuaFEgAemH7NIdlir_5_3y75bxYr3NPTB4BBFD3beR3yAxdCbZpDPtdgYz8QVgNymsmI-az02rtgGt-ze_ijWkOWJLRcgA=w128-h128-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX80W4KhFo6-QHxUxl6WQr-RmIKKhxdeI-Ro_jr0qd-pVybOIiUETO82K7cxMsxSOAGiq1v66aVlLXOCfoOralYkYe_sXm98i_dHM5Y1reaZ0MdH-HbvGsoY-hyFPdhAkF2XClK7=w128-h128-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-HxvN3AKEsyFcmK0d4xMiPtDuSGDg924QNa5ayAf1Tnn_bGbk-s55RM-tUh1eiUFQAZKG8V2cZoGGHXopB7oK4sqsvcw6tYQHNbj7DE1wSMM34Iq0gwEqWF2PCNfLkGbBzIyLc2w=w81-h81-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX97I627UEZQxbjbgeIviXKDttB_mFWJ9iGvfjCkd_W2U42dZ1PdpDuJdRgQM8Xkb9S2AW8JlTWVY_cWoAa28Eucm6Yv9X1z-qLdPJpYNG8cNpSk7vNm75sK476bymKNojy7Vu_jdw=w128-h128-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8rOF4AhHwoWHfwUsoKoyzqLEr2Abq7RcFnaETv1L0g_OkHA2Wi1HVpgAkuBZhL9tYvltMrT-j_ypXIMfgoZKiQHyiobV43DMhHkbeVfBLk3F6qDZGuT7SyLGmDIe3RngxX1szA=w125-h125-v0?authuser=0)

# *Full human control*
# *Full AI autonomy*
# **Traditional Research**
# Human-driven discovery at every
# stage
# **Tool-Assisted Research**
# Humans augmented by specialized
# computational tools
# **AI for Science**
# AI accelerates computation, humans
# steer reasoning
# **AI-Guided Discovery**
# Humans define objectives, AI
# executes workflows
# **Autonomous Research**
# End-to-end scientific discovery driven by
# AI
# **Scientific Large Language Models Wiki: knowledge graphs as source code; human direct, AI execute and maintains**Instead of traditional methods such as RAG, that retrieve-and-answer-and-forget from scratch every time, the LLM incrementally builds and
# maintains a persistent wiki from your sources
# **1. (Immutable) Raw sources**Data from multiple modalities/sources
# **2. LLM wiki layer**Markdown linked content
# generated by the LLM
# Iterative knowledge feedback
# Structured scientific memory formation
# **3. Schema layer**Configuration: data structures,
# rules, conventions, and workflows
# Markdown files
# **Sci AI Wiki Architecture (3-part)**
# `
# **D. Review Skill**Automated literature synthesis
# Synthesis agent
# **LLM**Dense hierarchical connections**Structured narrative argument:**Full backbone of manuscripts + comprehensive literature review
# Check repository structure
# **LLM****Structural violations**Broken links, orphan pages, and schema violations**Semantic conflicts**Stale claims and contradictory assertions between ingested papersGraph coherence + logical consistency
# **B. Maintenance**Structural and semantic audit
# **A. Ingestion**Knowledge acquisition
# **LLM**Parameterizable entities with explicit cross-links
# **…**Concept Method AuthorRaw sources + Researcher Interview*+ “Align focus with my goal”*
# **C. Query**Reasoning + Multi-Depth Query
# Example: What are the gaps of the literature?
# **LLM**Responses with citations**New insight generation**Identify knowledge gap + propose new persistent concept page**Multi-depth reasoning**Connect methods to local experimental results over time
# **3 Core operations + User-defined task skills**
# - Index - Log - Contents
### Papers Repositories Notes
### …
### Books
FIG. 1. The Scientific Large Language Model (SciAI) Wiki framework transitions AI from transient retrieval tools to partners [8] and maintainers of persistent scientific memory. Historically, the primary bottleneck of structured knowledge bases has been continuous maintenance, a burden that LLMs eliminate through automated cognitive bookkeeping. While the underlying idea applies broadly to personal or business domains, adapting it to scientific workflows directly tackles modern challenges like literature overload, peer review fatigue, and contextual fragmentation. The system operates across three layers (1–3) and the resulting compounding memory is maintained via three core skills (A – C) and additional user-defined task skills.
Concepts, methods, datasets, and hypotheses are progressively accumulated into interconnected, inspectable structures. Rather than repeatedly reconstructing understanding from isolated prompts, the system incrementally compiles and preserves scientific context across interactions.
The drive to augment scientific cognition through external memory builds upon historic visions. From Vannevar Bush’s 1945 Memex, a hypothetical device for linking associative information trails [11], to the Zettelkasten method of interconnected note-taking, researchers have long sought tools to support cumulative reasoning. This reflects the concept of extelligence: the externalised body of cultural and cognitive knowledge accumulated outside the human mind [12]. While scientific literature already
functions as extelligence, LLM Wikis automate its maintenance, transforming fragmented data into a navigable, collaborative memory.
The Scientific LLM Wiki (SciAI Wiki) adapts this paradigm specifically for research environments. Its primary contribution is infrastructural rather than purely architectural: it proposes persistent memory as the missing layer in AI-assisted science. The framework is designed to preserve relationships and provenance between literature, experiments, hypotheses, and intermediate reasoning across time, allowing scientific context to accumulate over extended timelines rather than repeatedly disappear between interactions.
Scientific workflows increasingly evolve from fragmented manual literature connections toward AI-assisted syn-
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_eLwNvPY-YJyJgKvuq4ssm1pTJXxiQdpYIq8vp9xkeA5M0ILVuSTEouRJ-wh0mFXR1cj4LYi09doK02x1fARiPcJL4sNJBjIAnhG-rfRo2um7GJl0aN-uf_LkJkbnZFTfvjpDsGA=w716-h566-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8DgUBwAxyRy5P5y0naGU0hzBJguDIspjRPDUAKe-C30aGyuc4EarhUwhTaGS42ClPcBGiwJD7y8RUFcipQH8NRIFvtTjNYnTPcm6wg915H62sBNpTVjv-_qqTr16o1a25UrQZ6kg=w60-h60-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_RJg5ISF-vBnGlMt_hLxtf_VKxzKtQrTUPferehfDUjBAM9mChc1HF8sVsDp7XYZTWZN7E2OOhUpivhYwQc9DDgRE3NqjPDXKyRcCrNEFoCSkEieKqx5EyRUptUWRUZdja62Zf=w120-h120-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8AMfeh1WlxKW64FvpjWUEnXVZYHpK_CLiT_31fmjwQczvcL_J6tg7uPZQIaw2YrZjiq8tmU6vCD7fIDwa00KBgYHMVKJPViNNBcEuC8zNTFcfmzfQFHO-XZAjG4_CWURhy8G4WIQ=w120-h120-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_GDAO7OpUVPwgO9Vk0k4lOByVCzCfgFkG9K9OMvw0Dk5uxHZ9PmtBF4qJA1lzhQhFweYg3vG0Dh900BDe2EOfwtxtD9A5xpYI_gltpfANOnWk85Wlgfbn-40yRtmuZ1dk4NT2EHw=w120-h120-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX88-1_gMUG2hCbrbUEkE9Q7Er3UlCxhbGX8igqtOkIcFeYxAEBqoLDzu8riluHC0VCVFFl8OEwmRcRUx72A34mgxsrYmofRYd2pLSZ7MAzavTQ9CR3JE62ydLJIcAXztZMC33ZyFQ=w42-h41-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_rKmMw-Gp7CfMrSr-1r7hIb15vZdKAUrdnUb4zANEfQTcq2tHjlAMUYQnhSmQU4BC3VRD--rEkKXuFTLz9GOmpPjxcfhzsNNyq-h8e9CA5aUJgN7NrvoGlVtuvgrz6PxerLWy_dg=w41-h41-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_JS59jm5mAq3vP24rN4Pksxgl58upXXSRmlFy6bbpVb0hawIT_1H9qJlCHu2hXNCgB6aQAi6Ae8_aw7ByupRgFiPDAx0K5k31H4cP1mZ5H5QqS7z4yalxJDwY_QyGOAN6wIIgW=w42-h41-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8frqgCzSMjXWJOyHV5zF7_cG537rSq8vhYksZfGgpkDcuFXvy6Ctj-FZz2dPWcyW6xGu5pVWtDnBo34DinvYAUE3fEbNPImKNYlFI-gK8TBe-T-1srdueyA7DHhP1UUMLeFyiRww=w42-h41-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-b83MlHxvk_bDkFNSx5rRRyUnaqaN8vULMR9TuyLfCK8bbaXMDOSANWlj0-qk8szjVHC2hHP2TkLmb_jVPjIXC8-aX4ySHDP7-5YhWvQSccvUqsT8r_7u45mfbwgH5a-IaZU1P8g=w120-h120-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9ULyYsrCEIk2zcEfrYiq9Kyroje6WPkRa8wrfnoRbP_WAkDQJYAfvCUAe2vG0Pe38PsZgnGrG9oxFXuLzd96P5HjizFm9i7j2jJ3WIqITpvVO6VHhDzLIuJCmBJZmwMhAW_EkVeQ=w120-h120-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-wBZ5R9kfl4nvZQQXPwgURi39kUEGGVCFFVJDU8xGph0YDcjdAvBe6DdTdX0-kL7vtb5wRXFEyXVe2XLxU38CDqOjBcPAv18LetCJ20k1Ew6nZ1lNU_sxW0H0AcdhCw0STzi22=w120-h120-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9Rn29wurZRaO78uaR2CXJd1Yz5lmErY6YnZCXRUwewCpSrSvbxF1qyq765zBpiqAYAomqDPGGnCWT__b3JxGwOZaLthhadPPZZi3G_ZQGXX0BI1x8p_98MOv6W-UdbE5yiH7mvIQ=w42-h41-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX9b74eXNm0InIy9OHCut20jnD6OlQ1qpcJRfrDnUigNRqiOSYBavgstnxSDzHWj0pqtzrN4BDcA5iNfxj9oI18fVWC4PeZpiM9nPyJxunFfv1XkU8m_ZCfm2mgkJwOhnDMwVBv6Xw=w42-h41-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX-9J_vQVJcQrXPd6RiwaU_BDn-GfNJteJPztUylKH6uzplfZGDwCgcTiwehDrFvERkEphofR7vm2mGru4kv-E8LcIHtFjmnKPCpy-REoAV1pKDH_npXw6syc40_XEbw_sWY_6Qu=w42-h41-v0?authuser=0)

![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX889zibAIoR-YWdiw9ubWLXgIodBJwH46nGGCgQ0wIQ2yv8v8LPkYFA9JDiKywR0hxf1f1jrp2szpkh8J_jGfVcYPj5Wu-2m8RmfSbz9_uQd903s1DXQHOZjt4Oty_E7sDp1RtK=w42-h41-v0?authuser=0)

thesis, organisation, and contextual reasoning (Fig. 1). The SciAI Wiki extends this progression toward a collaborative framework in which an agent incrementally maintains structured scientific context, preserves intermediate reasoning, and assists researchers through enduring knowledge compounding across the research lifecycle.
Operationally, the SciAI Wiki separates immutable scientific sources (papers, datasets, laboratory records, repositories) from AI-managed structured representations, typically interconnected markdown entities governed by explicit behavioural protocols (Fig. 2). Unlike conventional retrieval pipelines, relationships are not inferred solely at query time through embedding similarity; they are progressively compiled into navigable structures that preserve provenance and contextual continuity.
Behavioural protocols, implemented through editable instruction files (for example, AGENTS.md), define how agents ingest, validate, cross-reference, and maintain knowledge. Consequently, part of the agent’s operational reasoning becomes externalised into inspectable artefacts rather than remaining implicit within model parameters. These lightweight protocols adapt organisational schemas, domain context, and research priorities to specific areas, transforming personal workflows into reproducible environments for long-term collaboration between researchers and intelligent agents.
Durable scientific memory, organized in purpose-specific markdown files, naturally complements both collaborative and autonomous research systems. Collaborative frameworks, such as Agent Laboratory, benefit from improved continuity between literature review, experimentation, and writing under human guidance [6]. Conversely, highly autonomous systems, such as The AI Scientist, gain critical provenance tracking and contextual grounding to mitigate hallucination risks [7]. The primary emphasis of the SciAI Wiki is therefore not the automation of research itself, but the preservation of scientific continuity.
The transition from probabilistic chunk retrieval toward structured representations is increasingly supported by emerging evidence. Recent benchmarks demonstrate that graph-based and pre-structured knowledge systems outperform purely chunk-based retrieval pipelines on multihop reasoning tasks while requiring fewer retrieved tokens [13].
Ultimately, a SciAI Wiki functions as a split-screen environment where conversational interactions coexists with evolving knowledge graphs, interconnected markdown entities, and continuously updated literature (Fig. 2). As new sources are ingested, the system can progressively link concepts, preserve intermediate reasoning, and surface potential contradictions for human inspection. By relying on model-agnostic, human-readable formats, the framework ensures that cumulative scientific reasoning remains verifiable, portable, and progressively refined through the sustained partnership between researchers and intelligent agents.
# **Applications and tasks examples**
# Human-AI knowledge base interactionsRaw filesPromptProtocolBooks PapersPaper 2Paper 1SciAIWikiAuthors ConceptsWikilog.mdindex.mdschema.mdoverview.md
### Wiki index
### Wiki logExample of minimal Knowledge Graph
### Automatically evolving and compounding over time…
### Concept Instance Source Query
FIG. 2. A minimal SciAI Wiki implementation transforms standard document folders into actionable scientific memory. Users require no advanced technical expertise; simply providing a directory of raw sources (e.g., papers, books, and references) allows the AI to autonomously build an interlinked knowledge graph. This compounding structure unlocks a broad spectrum of workflows, assisting researchers (and other science-related occupations) in valuable routine tasks such as automated literature synthesis, gap identification, research ideation, results interpretation, report writing, peer review validation, rebuttal generation, and continuous literature discovery.
III. OPERATIONAL MECHANICS
The SciAI Wiki functions as an iterative research environment where scientific sources are progressively transformed into structured, interconnected knowledge. Papers, datasets, repositories, and experimental notes are incorporated into a memory substrate, allowing contextual relationships to accumulate rather than being repeatedly reconstructed.
This environment relies on externalised operational routines–or skills–that govern agent behaviour without requiring modifications to the underlying model parameters [14]. By unifying these externalized skills, memory structures, and interaction protocols, developers construct a coherent runtime environment–a paradigm recently defined as harness engineering [15]. These routines are logically grouped into three core (+ user-created) function files (Fig. 1): Ingestion transforms raw sources into structured representations while preserving provenance and researcher intent; Query navigates this accumulated context to synthesise answers; Maintenance (or Lint) performs continuous structural and semantic auditing
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8ZKBWwwui0Ei-eEa2dqIFg3hckWXFX9mqPGXY-yu7rABYgbYNp7BPs0iE1X3K5wxmOXf87O6FGOteD2oRxa_LtiLtpJLgSEdlLNBI-GueCMr4evMT928kFQcyhB8y8RI8d9sP33Q=w346-h363-v0?authuser=0)

to identify broken links, outdated claims, contradictions, or inconsistent relationships; and user-defined task skills such as Review generation constructs comprehensive literature syntheses grounded in the evolving repository.
While this functional decomposition mirrors the modular specialised stages increasingly adopted by human-in-the-loop agentic systems (like Agent Laboratory [6]), the fundamental distinction lies in statefulness. Rather than merely orchestrating transient tasks, persistent memory systems ensure that intermediate reasoning (e.g. indexes, logs, markdown contents, ...), structural audits, and contextual relationships survive beyond individual sessions to continuously compound over time.
IV. HOW SCIAI WIKI AFFECTS THE WAY RESEARCH IS DONE
Rather than repeatedly reconstructing context through isolated searches, researchers may increasingly rely on persistent memory to preserve relationships across papers, methods, and intermediate reasoning. Beyond literature synthesis, this paradigm directly supports peer review and scientific evaluation workflows. While recent autonomous frameworks explore fully automated LLM-driven peer review [7], these black-box evaluations risk obscuring methodological nuance. In contrast, an evolving SciAI Wiki assists human expert judgement by contextualizing submitted manuscripts against a pre-compiled repository; automatically surfacing omitted literature, conflicting evidence, or methodological divergence for human inspection. Similarly, editorial work, funding agencies, and reviewers may benefit from improved contextualization of proposals within rapidly evolving research landscapes.
Importantly, the SciAI Wiki does not constrain researchers to a minimal markdown interface implementation. The repository functions as a canonical, machinereadable substrate upon which richer environments can be built. Lightweight implementations demonstrate inspectable markdown knowledge accumulation [16], while more elaborate frameworks layer interactive knowledge graphs, hybrid retrieval, agentic skills, and visual exploration on top of the wiki structure [17].
Ultimately, the SciAI Wiki represents an operational framework combining structured knowledge representations, agentic reasoning, and explicit governance. It shifts the interaction between researchers and language models from transient, stateless exchanges toward long-term, collaborative knowledge construction.
V. LIMITATIONS AND GOVERNANCE
Persistent scientific memory also introduces new risks. Unlike transient conversational systems, errors within a long-term repository may accumulate and recursively influence future reasoning. Hallucinated links between concepts, unsupported syntheses, or outdated claims can become embedded into the knowledge structure itself. This creates a form of epistemic contamination in which incorrect interpretations compound rather than disappear.
Scientific disagreement further complicates this challenge. Contradictory findings often reflect differences in methodology, instrumentation, or experimental assumptions rather than simple factual conflict. Consequently, systems designed for persistent scientific memory must prioritise provenance, uncertainty tracking, versioning, and human verification rather than treating accumulated knowledge as inherently reliable.
In this sense, governance becomes as critical as retrieval quality. Emerging frameworks for agentic memory emphasise that systems must implement explicit maintenance protocols, structured auditing, and verification loops to prevent the entrenchment of false assumptions. Such oversight will ultimately determine whether persistent memory systems amplify scientific understanding or merely accumulate epistemic noise.
As scientific workflows increasingly integrate language models and autonomous agents, the principal bottleneck is no longer access to information or context window size alone. It is the difficulty of preserving and navigating scientific context across time. Scientific AI will therefore require not only stronger models or better retrievers, but fundamentally more reliable forms of memory. Persis-tent systems such as the SciAI Wiki offer an actionable framework for this transition.
CODE AVAILABILITY
The operational protocols, generalized prompt and agent skills associated with the SciAI Wiki are openly available this repository (https://github.com/cnpem/sci-ai-wiki). The repository contains the markdown schemas, behavioural instruction files, and specialised agent skills described in this work and is intended to support testing, adaptation, and further community development.
ACKNOWLEDGMENTS
The authors acknowledge CNPq grants no. 422069/2023-0, 313301/2025-5, and 371610/2023-0 (INCT (National Institute of Science and Technology on Materials Informatics)), and FAPESP grants no. 2024/22392-2, 2024/00989-7, and 2023/13081-0.
[1] P. Jiang, J. Lin, Z. Shi, Z. Wang, L. He, Y. Wu, M. Zhong, P. Song, Q. Zhang, H. Wang, X. Xu, H. Xu, P. Han, D. Zhang, J. Sun, C. Yang, K. Qian, T. Wang, C. Hu, M. Li, Q. Li, H. Peng, S. Wang, J. Shang, C. Zhang, J. You, L. Liu, P. Lu, Y. Zhang, H. Ji, Y. Choi, D. Song, J. Sun, and J. Han, Adaptation of agentic ai: A survey of post-training, memory, and skills (2025).
[2] M. Sänger, N. De Mecquenem, K. E. Lewinska, V. Boun-tris, F. Lehmann, U. Leser, and T. Kosch, arXiv preprint arXiv:2311.01825 10.48550/arXiv.2311.01825 (2023).
[3] O. Yildiz and T. Peterka, arXiv preprint arXiv:2412.10606 10.48550/arXiv.2412.10606 (2024).
[4] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W.-t. Yih, T. Rocktäschel, S. Riedel, and D. Kiela, Advances in Neural Information Processing Systems 33, 9459 (2020).
[5] D. Edge, H. Trinh, N. Cheng, J. Bradley, A. Chao, A. Mody, S. Truitt, D. Metropolitansky, R. O. Ness, and J. Larson, From local to global: A graph rag approach to query-focused summarization (2025), arXiv:2404.16130 [cs.CL].
[6] S. Schmidgall, Y. Su, Z. Wang, X. Sun, J. Wu, X. Yu, J. Liu, M. Moor, Z. Liu, and E. Barsoum, in Findings of the Association for Computational Linguistics: EMNLP 2025 (Association for Computational Linguistics, 2025) pp. 5977–6043.
[7] C. Lu, C. Lu, R. T. Lange, Y. Yamada, S. Hu, J. Foerster, D. Ha, and J. Clune, Nature 651, 914–919 (2026).
[8] Y. Feng and Y. Liu, arXiv preprint arXiv:2604.00945 (2026), arXiv:2604.00945 [cs.CY].
[9] A. Karpathy, Llm wiki, https://gist.github.com/ karpathy/442a6bf555914893e9891c11519de94f (2026), gitHub Gist, accessed May 2026.
[10] C. Packer, S. Wooders, K. Lin, V. Fang, S. G. Patil, I. Stoica, and J. E. Gonzalez, Memgpt: Towards llms as operating systems (2023).
[11] V. Bush, The Atlantic Monthly 176, 101 (1945). [12] I. Stewart and J. Cohen, Figments of Reality: The Evolu-
tion of the Curious Mind (Cambridge University Press, 1997).
[13] D. Yarmoluk and D. McCreary, Compact knowledge graph benchmark, https://github.com/Yarmoluk/ ckg-benchmark (2026), accessed: 2026-05-13.
[14] R. Xu and Y. Yan, arXiv preprint arXiv:2602.12430 10.48550/arXiv.2602.12430 (2026).
[15] C. Zhou, H. Chai, W. Chen, Z. Guo, R. Shan, Y. Song, T. Xu, Y. Yang, A. Yu, W. Zhang, C. Zheng, J. Zhu, Z. Zheng, Z. Zhang, X. Lou, C. Zhang, Z. Fu, J. Wang, W. Liu, J. Lin, and W. Zhang, Externalization in llm agents: A unified review of memory, skills, protocols and harness engineering (2026).
[16] N. Su, Llm wiki, https://github.com/nashsu/llm_wiki (2026), gitHub repository, accessed May 2026.
[17] Tencent, Weknora, https://github.com/Tencent/ WeKnora (2026), gitHub repository, accessed May 2026.