
Journal Title Here, 2022, 1–26
doi: DOI HERE
Advance Access Publication Date: Day Month Year
Paper
### AI for Science: Reframing AI’s Role in Discovery
Kyle Cranmer ,1 Neil D. Lawrence ,2 Jessica Montgomery 2,∗
and Denis Thérien3
1UW–Madison Data Science Institute, University of Wisconsin-Madison, 500 Lincoln Dr, WI 53706,
Wisconsin, US, 2Department of Computer Science and Technology, University of Cambridge, 15 JJ
Thomson Avenue, CB3 0FD, Cambridge, UK and 3ServiceNow, 6650 Saint-Urbain, H2S 3G6, Montreal,
Canada
∗Corresponding author. jkm40@cam.ac.uk
FOR PUBLISHER ONLY Received on Date Month Year; revised on Date Month Year; accepted on Date Month Year
Abstract
Digital computers have reshaped scientific practice, moving working scientific knowledge from printed texts
into algorithms, simulations, and models. Advances in artificial intelligence (AI) are now accelerating that shift,
progressing science in areas from protein folding to climate modelling, and raising the prospect of a further
transformation in how science is done. With growing hype around the field, there is a risk that inflated claims
about AI’s potential obscure both its current limitations and its longer-term possibilities. This paper explores
how AI contributes to science, introducing a framework organised around task capabilities, scientific workflow
integration, and domain constraints. It uses that framework to open wider questions about the role of AI
in scientific discovery. These include: Is scientific knowledge constructed and used by AI agents considered
scientific understanding if it is impenetrable to humans, or does scientific understanding refer to an activity that
is intrinsically human? What technical advances are needed to move AI beyond pattern matching toward causal
reasoning? And what institutional changes are needed to support responsible AI adoption? How researchers and
policymakers engage with these questions will shape whether AI accelerates progress within existing scientific
paradigms or catalyses the generation of new forms of scientific knowledge. This paper marks the opening of
a call for papers from RSS Data Science and AI, which invites contributions that take up these and related
questions from multiple perspectives.
Key words: artificial intelligence, machine learning, scientific discovery, causality, mechanism, scientific inductive biases,
epistemology
1. Introduction
From its inception, the digital computer has been used in the service of science. Numerical solutions of
differential equations were some of the first algorithms deployed on the earliest wave of electronic computers.
From climate models to cosmological models to pandemic models, modern science is unimaginable without
digital tools. These techniques have typically relied on mechanistic understanding of how the world operates,
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX8plXJh2ezhwVm9sb0cfvS7Y32GWZQmW3xZn2s2DlITQ7-n1RDspizLnePIrTmT6AOokkPZpfNPysI2Vn0oXx1AFHqhD8W7Xydf8yfWGEVvV4YKmMr65I3kBIEYKjTXIR0bOb2MtA=w63-h77-v0?authuser=0)

2 Cranmer, Lawrence, Montgomery, and Thérien
but they have always been accompanied and aided by data. Whether through statistical analysis or parameter-
setting, a combination of mechanism and data shapes our views of the world. Our knowledge of the world is
in our computer code as well as in our own minds.
This relationship between data and mechanism has deep roots. When Gauss used the method of least
squares to predict the orbit of the dwarf planet Ceres from Piazzi’s observations in 1801, he was combining
empirical data with Kepler’s mechanistic theory. This approach became a template for quantitative science.
In the two hundred years that followed, the derivation and solution of differential equations to predict and
understand the world became central to the physical sciences.
Physics was perhaps the field that most embraced this methodology, leading Rutherford to reportedly claim
that all science is either physics or stamp-collecting (Bernal, 1939; Pielke, 2014). Rutherford’s comments
reflected a bias in the physics community towards universal laws, dismissively characterising other fields
as observational and descriptive. This distinction, while rigid and of its time in its disciplinary attitudes,
captures a continuing tension in scientific approaches: the search for mechanistic principles to explain why
phenomena occur, versus empirical methods that focus on identifying patterns and making predictions from
data.
Rutherford’s dichotomy is echoed in debates about the ‘unreasonable effectiveness of mathematics’
(Wigner, 1960) and the ‘unreasonable effectiveness of data’ (Halevy et al., 2009) in making predictions.
However, this apparent dichotomy may be misleading. Both approaches may succeed for the same reason:
the unreasonable effectiveness of pattern identification in dealing with Hume’s ‘problem of induction’ (Hume,
1748), or the problem of inferring general principles from particular observations.
Reframing Rutherford’s distinction can lead to a more nuanced view of scientific explanation. At one level
sit mechanistic models, which encode how a system works in terms of underlying physical principles. On
another, observational models, which describe the patterns that appear in data without committing to the
mechanisms that produce them. Between these lie causal models, which can answer questions about what
would happen under intervention, without requiring the full mechanistic apparatus of physics (Peters et al.,
2017).
The merging of these worlds is now taking place under the banner of artificial intelligence (AI), driven by
progress in machine learning. Machine learning marries predictive mathematical models with large quantities
of data. The empirical spirit of machine learning has historical roots in Gauss’s work on orbits (Gauss,
1809), but the difference today is in the scale of the data (now potentially billions of observations) and the
comparatively diluted use of mechanistic understanding (which may involve only notions of smoothness or
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 3
composability). In the case of Ceres, Piazzi made the observations and Gauss developed the mathematical
framework that combined mechanistic theory with data analysis. In the modern age of the computer,
sophisticated pattern recognition from data is taking on a more prominent role.
This combination has already supported scientific advances in areas including protein folding (Jumper
et al., 2021), weather forecasting (Allen et al., 2025), materials discovery (Merchant et al., 2023), economics
(Korinek, 2025), and social sciences (Bail, 2024), signalling the potential of AI as a tool to accelerate discovery
(Berens et al., 2023). Spurred on by these successes, some now envision a future where intelligent agents
pursue complex investigations autonomously across the physical, life, environmental, and social sciences and
humanities.
Despite their apparent boldness, claims that AI could replace scientists or automate science miss the depth
of AI’s potential, what is needed from the next wave of advances in AI to deliver on that potential, and what
widespread adoption of AI means for science, even including the definition of science itself.
Understanding AI’s impact in science requires moving beyond individual project success stories to examine
whether AI is leading to a new scientific paradigm, or whether it risks undermining the progress it proposes
to accelerate. This paper explores these tensions in five parts. It begins by asking whether AI represents
a paradigm shift or an evolution of existing computational practice, and considers what this means for
scientific progress. It then proposes a framework for making sense of AI applications in science, distinguishing
between task capabilities, scientific workflow needs, and domain constraints. From these, it examines the
technical challenges of grounding AI in scientific understanding, in areas such as causal reasoning, abstraction,
and simulation (Krenn et al., 2022), before turning to the human dimensions of scientific inquiry, and the
relationship between AI, science, and human understanding. It closes by considering the institutional changes
needed to support responsible AI adoption.
Running through these five parts are two threads considering the disruptive potential of AI in science.
One is about how AI is reshaping what counts as scientific knowledge and understanding, and whether the
distinction between the two is changing. The other is a set of practical concerns about what AI adoption in
science requires from AI technologies, research infrastructure and institutions, and research culture. Questions
about what AI changes for science—and whether those changes could bring new paradigm shifts—engage
both these epistemological and practical dimensions.
The paper surfaces these debates as an invitation to the RSS Data Science and AI community to take
them up in the special series that follows.
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
4 Cranmer, Lawrence, Montgomery, and Thérien
2. Signal and noise
2.1. Is AI a paradigm shift, or an evolution of current science?
Thomas Kuhn’s work on the Structure of Scientific Revolutions (Kuhn, 1962) provides a lens for examining
AI’s role in science. Kuhn suggests that scientific progress consists of two different stages: so-called ‘normal
science’, where researchers solve puzzles within existing paradigms, and paradigm shifts, which bring dramatic
changes in scientific understanding.
For example, Laplace’s and Gauss’s work on the motion of celestial bodies took place within the paradigm
of Newtonian mechanics (Stigler, 1986, 1999). When Gauss predicted where the dwarf planet Ceres would
be recovered (Gauss, 1801) he solved a puzzle within the context of Keplerian motion of planets based on
observations by Piazzi (Piazzi, 1801). His work on planetary motions (Gauss, 1809) was the foundation of
how planetary orbits were calculated until numerical solutions became available through the digital computer.
The puzzle was a complex one, but it still sat within the paradigm of Newtonian mechanics. At its heart, it
was combining data with a mechanistic model to make predictions. In contrast, the emergence of Einstein’s
theories of General and Special Relativity upended or extended the rules by which scientists were solving
puzzles. This paradigm shift led to a new phase of normal science.
For Kuhn, scientific paradigms were stored in textbooks; initially in texts such as Principia or Gauss’s
Theoria motus corporum coelestium but later in books that summarised the best understanding derived
from those advances. Today, elements of scientific understanding are increasingly encapsulated in computer
code—in simulations, algorithms or models that represent scientific understanding of how the world works.
This shift has been underway for some time; seen, for example, in numerical solvers of differential equations
in climate science or reconstruction pipelines in particle physics, and sets the stage for understanding AI’s
potential role in science.
The question facing science today is whether AI represents normal science within our existing
computational paradigm, or signals a more fundamental shift. Digital computers transformed scientific
practice by enabling complex calculations and simulations beyond what researchers could previously have
achieved. They made non-parametric approaches that had been theoretically possible but computationally
infeasible, from histograms to kernel density estimation to Gaussian processes, practical for the first time. This
started a long-term shift towards models that were less directly interpretable than parametric approaches,
but that continued to operate within existing frameworks of scientific knowledge.
Is AI-enabled science a continuation of this trend, or something qualitatively different? Recent successes in
AI for mathematics illustrate the distinction. Reports from OpenAI suggest that a general-purpose reasoning
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 5
model might have disproved a longstanding conjecture in discrete geometry, potentially offering the first case
of a prominent open mathematical challenge being solved by AI (OpenAI, 2026). There remains, however,
a gap between this type of advance—an addition to mathematical knowledge—and the reframing of a field
enabled by work such as Grothendieck’s in algebraic geometry, which changed how mathematicians thought
about their subject.
The possibility that AI systems could generate knowledge through pattern recognition (or other
capabilities) that humans cannot interpret or relate to existing bodies of knowledge has profound implications
for how we understand the nature of scientific knowledge. AI could represent an acceleration of existing
computational trends within our current paradigm, or a step towards a new paradigm for science itself in
which knowledge is no longer interpretable by humans.
There are indicators that suggest the latter. Unlike numerical solvers or simulation codes, which
encode mechanistic understanding even when their implementation is complex, many AI methods generate
predictions without an underlying mechanistic model of the system they describe. The infrastructure required
to train today’s most capable systems is concentrated outside of public scientific institutions. AI is being
positioned as a general-purpose tool, with autonomous AI agents capable of pursuing scientific investigation
independently.
These features do not settle the paradigm question, but they suggest that AI may introduce challenges
that differ in kind from those of earlier computational science. They also illustrate the different types of
paradigm shift potentially in play. Kuhn’s original framing envisaged paradigm shifts within a science; new
theories of gravity, for example, that change the questions or approaches pursued by normal science. AI could
drive such shifts. It also presents the possibility of a paradigm shift at a meta-level, in what is considered
scientific knowledge, how that can be held, and by whom or what. If AI systems produce knowledge that
resists human interpretation, the relationship between discovery and human insight could weaken or take on
new forms.
Whether this constitutes scientific progress or a threat to scientific understanding depends partly on how
AI relates to the broader scientific enterprise.
2.2. Or is AI a threat to scientific progress?
This potential paradigm shift intersects with continuing concerns about a decline in scientific productivity
and the ‘reproducibility crisis’ in science. Even if AI represents a paradigm shift, its impact on scientific
progress is not guaranteed to be positive (Kapoor and Narayanan, 2025).
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
6 Cranmer, Lawrence, Montgomery, and Thérien
Scientific output is growing, with one estimate suggesting the overall volume of research doubles every 15
years (Fortunato et al., 2018). However, this growth in output does not map onto increases in productivity. By
some measures, discovery appears to be slowing (Collison and Nielsen, 2018), despite increased investment,
with both economic and social implications (Bloom et al., 2020). This productivity paradox reflects a broader
disconnect: accelerating output does not guarantee progress in the areas that matter most to science or society.
Public dialogues indicate that, despite impressive technical progress, AI advances are failing to address areas
of societal need (ai@cam et al., 2024).
AI risks intensifying this disconnect between output and progress. Individual researchers may benefit
from AI tools that help generate plausibly publishable manuscripts, creating an impression of enhanced
productivity. In aggregate, the effect could be a wave of research that mimics scientific progress without
delivering new insights.
The research community is negotiating questions about acceptable uses of AI in generating papers, with
divided views on where and how its use should be permitted (Kwon, 2025). While this conversation continues,
the impacts of AI on publishing practices are already visible. AI-generated papers of variable quality have
proliferated (O’Grady, 2025), with implications for publishing practices, the spread of misinformation, and
the integrity of the scientific information environment (Haider et al., 2024). Agentic systems sharpen these
concerns. How these outputs should be treated as scientific contributions, and how scientific publishing
should respond to them in the context of already strained systems for peer review, are questions the research
community is beginning to address. For example, the Parallel Science project takes the stance that AI-
generated research should be published and evaluated in a separate space (Parallel Science Project, 2026).
Publishing quality concerns connect with continuing challenges around reproducibility and the
maintenance of scientific rigour as the volume of outputs increases (Baker, 2016). The field of AI itself brings
its own reproducibility challenges to science (Donoho, 2024), with gaps in code publication or openness
in training data undermining research transparency (Straiton, 2024). As AI agents move from supporting
individual research tasks to coordinating workflows, they accrue what might be termed agentic debt: the
risk of delegating scientific workflows without clear boundaries around who can take which action, on what
evidence, with what route to recovery or process for reconstructing outputs. This raises further questions
about what accountability structures trustworthy AI-enabled science requires, from the responsibilities of the
scientist developing the workflow to the community that accepts the results.
In this environment, clarity on where and how AI is useful for science is an important starting point in
bridging the gap between innovation and progress.
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 7
3. Creating a conceptual framework
Rapid AI advances, vague promises, and inflated expectations contribute to breathless discussions about
AI’s role in science. The result is conflation of distinct problems and approaches under the broad umbrella
of ‘AI for science’, mixing realistic capabilities with unrealistic expectations about AI’s potential. These
conversations about the role of AI in science matter: they can influence research priorities, inform funding
decisions, and shape expectations about what AI can deliver for science and who it is delivered by (Cave
et al., 2018).
Computational approaches have been influencing research across disciplines for decades (Hey et al., 2009;
Kitchin, 2014), with each new technological capability leading to both advances and inflated expectations. In
some respects, AI is a continuation of this shift, bringing new analytical tools alongside familiar challenges of
distinguishing hype from real value. And yet in others, AI is distinct, bringing new capabilities to machines
that make it hard to believe the shared origin in Gauss’s analysis of Piazzi’s data.
Navigating this landscape requires conceptual tools to make sense of the role of AI in science. A framework
that shows AI’s contribution to science could help clarify how these new technologies can be useful in practice.
A taxonomy could distinguish between different types of AI tools or applications, allowing researchers to
match AI capabilities to scientific needs. The result should be more strategic deployment of AI where it offers
scientific benefit, rather than unrealistic hopes of magical solutions to long-standing scientific challenges.
The value of AI in science depends on alignment of technical capabilities, scientific questions, and required
infrastructure and resources. This suggests a framework that distinguishes between AI applications based
on three dimensions: task capabilities, scientific workflow needs, and scientific context and constraints. Each
dimension reveals different aspects of how AI tools can be matched to scientific applications.
Task capabilities: Understanding what different AI tools can deliver in practice underpins successful
applications of AI in science. The perception that AI offers general problem-solving capabilities obscures
the reality that different AI tools serve different functions and are suited to different scientific questions.
For example, excitement about ‘foundation models for science’ often conflates mixed ideas about what a
foundation model is, what researchers are trying to achieve with them, and why they might be useful in
specific scientific applications. A foundation model that can be applied across different domains (such as
image recognition tools or language models that are applicable in different fields (Bommasani et al., 2021))
is different to one that combines diverse data types within a domain to address a specific field of inquiry (for
example, using multispectral data to study galaxies (Parker et al., 2024)). Recognising these differences is
important in designing AI tools that are appropriate for the scientific task at hand.
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
8 Cranmer, Lawrence, Montgomery, and Thérien
Scientific workflow needs: Identifying where AI adds value in research processes can help researchers to
understand its impact. AI applications now span the entire scientific workflow, from hypothesis generation,
to experimental design, to data analysis (European Research Council, 2023; Berman et al., 2024; Arranz
et al., 2023). For example, AI-guided approaches to materials discovery have been used to propose candidate
compounds that researchers then synthesise and test (Merchant et al., 2023), while Large Language Model
(LLM) based tools are increasingly used to support literature synthesis and evidence review in biomedical
research (Lieberum et al., 2025). Agentic AI systems are binding these workflow stages together, planning
experiments, executing them, interpreting the results, and drafting papers (Villaescusa-Navarro et al., 2025;
Lu et al., 2026). LLMs and agentic AI also provide a way to integrate AI in daily activities, from automating
coding tasks, to drafting emails, to reviewing literature (Berman et al., 2024). While some of these routine
administrative tasks might seem mundane, the addition of AI wraps them up in a narrative about superhuman
AI abilities that fails to convey the practical uses of AI in supporting everyday science. Understanding these
differences enables more thoughtful AI tool selection while maintaining appropriate expectations about its
role in fundamental discovery (Narayanan and Kapoor, 2025).
Scientific context and constraints: Recognising the practical constraints that shape AI adoption is crucial.
Many of today’s most successful methods require substantial data and computational resources, and the
availability of these shapes what scientific questions can be addressed. Different scientific domains also have
varying tolerance for uncertainty, different validation requirements, and different collaborative cultures that
influence how AI tools can be integrated into research practice. Even within a single domain, validation
requirements can vary depending on operational constraints. For example, AI systems used in real-time
data acquisition where latency is an issue, such as particle accelerators that operate at MHz rates, face
different validation challenges than those used offline (Duarte et al., 2018). Compared to exploratory research
applications, AI systems used in clinical decision-making face stricter requirements around validation, safety,
interpretability, and bias due to their direct impact on patients (Wiens et al., 2019).
Distinguishing between task capabilities, workflow needs, and domain constraints can help researchers
identify where AI can provide immediate benefits versus where transformative breakthroughs might occur.
The framework described above is one attempt to provide a taxonomy for understanding the role of AI in
science.
Across these areas, successful deployment of AI in science requires rooting technical capabilities in
scientific needs. This brings with it a need for a new wave of progress in AI methods and capabilities,
and an understanding of what best practices in deployment look like. The analysis that follows explores
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 9
these technical and institutional challenges as open questions rather than settled issues, recognising that the
research community holds diverse views on how AI should relate to scientific practice.
4. The challenge of making AI scientific
The advent of generative AI and agentic AI systems has allowed us to emulate parts of the scientific process
using orchestrated groups of agents. LLMs have been trained on large quantities of human text, allowing
them to emulate human thought processes and reasoning. This has led them to be characterised as human-
analogue machines (Lawrence, 2024). But this emulation comes without deep understanding of the original
human thought process or the ways in which it has been faithfully recreated, altered or enhanced.
4.1. The science gap
Today’s AI excels at approximating functions and identifying statistical patterns in data. The success of
LLMs is driven by this process applied at scale to human language data. A central challenge for the future
success of AI in science is bridging the gap between this capability and identification of the mechanisms
that generate those patterns. This gap is more than a technical limitation. It reflects underlying differences
between statistical AI methods, which look for patterns and correlations, and scientific reasoning, which seeks
causal mechanisms that explain patterns across different contexts and extrapolate (or generalise) to unseen
conditions.
This mismatch can be seen in AI for science applications as a guess-and-verify approach to research.
AI generates predictions based on statistical patterns in large datasets, which must then be experimentally
validated to determine their scientific validity. While predictions from traditional scientific theories also
need to be experimentally tested, the hypotheses are usually grounded in or motivated by an interpretable
mechanistic model.
The limitations of pattern-matching approaches have led to characterisations of AI systems as ‘stochastic
parrots’ (Bender et al., 2021) that recombine patterns from training data without grasping the underlying
meaning. The potential result is an illusion of understanding without insight. Hybrid and agentic approaches
attempt to mitigate these limitations by using generative AI as an interface to classical digital tools such as
simulations or databases working within an established conceptual framework (Laurent et al., 2024). Agentic
AI systems take this further by generating hypotheses, designing experiments, and using tools developed
within established conceptual frameworks (for example, Laverick et al. (2024)). These systems are doing
some combination of pattern matching, human emulation, interface provision, and reasoning. Agentic AI
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
10 Cranmer, Lawrence, Montgomery, and Thérien
offers a path towards AI that can extend these conceptual frameworks in a way that is compatible with
novel mechanisms that are interpretable by humans and support human insight. At the same time, their use
may widen the gap between discovery and human-understandable insight, allowing scientific advances that
are operationally successful yet resistant to mechanistic interpretation. Although related tensions between
predictive success and explanatory understanding have long been recognised in the philosophy of science
(Popper, 1963; Kuhn, 1962), AI systems may expand this divide in unprecedented ways.
4.2. Grounding AI in scientific understanding
While machine learning’s pattern-matching capabilities are powerful, they often struggle to generalise to
unseen settings. In contrast, this is a strength of traditional scientific reasoning, which seeks to find the
underlying mechanisms, such as laws, causal relationships, or organising principles, that govern natural
systems. Whether this mechanistic understanding is essential for scientific progress, and whether strong
generalisation can emerge from systems that primarily rely on pattern recognition, are open questions that
will be answered in time. An open question in the philosophy of science is whether a system can be considered
scientifically valid if it is not connected to an underlying mechanism, or whether the ability to make accurate
predictions in novel settings is sufficient.
Connecting statistical patterns to traditional, mechanistic, forms of scientific understanding requires a new
generation of AI tools (Lawrence et al., 2023; Cranmer et al., 2020). These tools would bridge from pattern-
matching directly to mechanistic explanation, equipping AI systems with capabilities that allow exploration
of the causal layer. Several technical priorities follow: developing causal reasoning capabilities that elucidate
why patterns or correlations appear (Peters et al., 2017), creating simulations that combine mechanistic and
data-driven knowledge (Cranmer et al., 2020), and encoding existing scientific understanding into AI systems
in ways that enhance rather than replace human reasoning.
Causality : The ability to reason about cause and effect is central to scientific understanding (Pearl and
Mackenzie, 2018). Researchers seek to understand not only what phenomena occur, but why, when, and
how. However, current AI methods often struggle to distinguish between spurious correlations and causal
relationships, undermining the scientific value of AI-generated knowledge. Embedding causal structure in
models can also help create AI systems that are more interpretable and generalisable (Schölkopf, 2022;
Schölkopf et al., 2012).
Abstraction : Major scientific breakthroughs often come from discovering intermediate scales that bridge
different levels of explanation. In physics, for example, researchers first observed and described entropy as
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 11
a macroscopic phenomenon, then later understood how it emerges from the statistical behaviour of systems
of particles (Jaynes, 1957). The ability to work across scales, identifying emerging properties at one level
and tracing their origins to a lower level, has driven important scientific advances (Anderson, 1972). Finding
these connections is challenging, particularly in natural and social science domains characterised by complex
multi-scale interactions in which patterns do not neatly resolve to lower-level explanations. AI systems that
could discover new abstractions that cross scales would bring profound scientific advances.
Simulation : Sophisticated simulations of natural, physical, and social systems enable researchers to
interrogate the dynamics and causal drivers of change in complex systems. Today’s approaches to simulation
span a spectrum from purely mechanistic models, which encode known physical laws to purely data-driven
models that learn patterns directly from observations. Each approach has limitations. Mechanistic models
may oversimplify complex systems or become computationally impractical when operating across multiple
scales, while data-driven models risk violating physical constraints or producing scientifically implausible
results. Hybrid approaches offer a route forward, combining the reliability of mechanistic components with
the flexibility of data-driven methods (Cranmer et al., 2020).
Scale-driven performance gains in AI, framed through Sutton’s “Bitter Lesson” (Sutton, 2019), have been
read as an argument against the need for methods and approaches that integrate domain knowledge into
AI systems. In the scientific context, while scale may ‘solve’ prediction, it is not clear whether it addresses
questions about why predictions do, or do not, hold. Further, AI for science is data-limited in many domains:
the most cited successes, from weather forecasting to protein folding, have leveraged decades of carefully
curated scientific data. Most areas of science do not have comparable data resources from which to draw.
Solving these technical challenges—causality, abstraction, and simulation—could each advance science in
important ways. Could progress on these technical fronts also help address deeper questions about how AI
systems should relate to the human enterprise of scientific discovery?
4.3. AI as repository or interface
These technical challenges raise new uncertainties about how AI systems should relate to scientific knowledge.
There is historical precedent for this concern: for Kuhn, writing in the early sixties, scientific paradigms
lived in textbooks (Kuhn, 1962); the frontier of today’s working scientific knowledge increasingly resides
in complex computational simulations and algorithms. This pattern has been seen previously. Numerical
models in climate science or reconstruction pipelines in particle physics influence how knowledge is recorded.
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
12 Cranmer, Lawrence, Montgomery, and Thérien
However, AI brings renewed focus to questions about how scientific knowledge is preserved, updated, and
transmitted (Humphreys, 2009).
AI systems can relate to scientific knowledge in different ways. Two metaphors to consider are a repository
and an interface.
As a repository, an AI system could encode knowledge as model parameters or learned representations.
This might have different variants: a relatively static encoding of established facts, which requires retraining
to update, or a flexible function approximator that fits whatever data it is presented with.
As an interface, an AI system could provide a conduit to external sources of scientific information, such as
databases, simulation tools, or published literature. This might be settled and curated databases that reflect
existing consensus, or live and contested sources that show knowledge in development.
These modes have different vulnerabilities and different implications for how scientific knowledge evolves.
Systems anchored in current consensus, either through training or through interfaces to established knowledge
bases, may suit areas of science with well-established frameworks, but they risk calcifying outdated knowledge
in fields where knowledge is moving. Systems that absorb new data smoothly lack constraints to flag when
new data is in tension with established theory. A system that fits any pattern makes it more difficult to
understand when an anomaly is scientifically significant. Each also brings different validation requirements:
verification of what they have learned, or verification of how knowledge is retrieved and applied by the system.
If AI systems become repositories of knowledge whose internal workings resist human inspection and
interpretation, science might be entering a new paradigm where scientific knowledge is no longer human-
comprehensible. This represents a departure from the assumption that scientific knowledge should be
understandable by the researchers who create and use it, with implications for how we understand the
nature of scientific discovery itself.
5. Science as a human project
The relationship between AI and scientific knowledge raises questions about the nature of understanding itself.
Whether science discovers objective truths about reality or constructs models that happen to work, a common
assumption is that science has a subjective dimension; that it is oriented toward human comprehension and
meaning-making.
This human orientation creates tensions when AI systems identify statistical patterns that do not align
with existing scientific principles. Science has long grappled with data that does not fit existing theoretical
frameworks, from anomalies in astronomical surveys to correlations in genomic data. AI changes the scale
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 13
at which such patterns can be generated. Faced with a pattern that does not fit, scientists can respond by
changing theoretical understanding to fit the patterns, or by treating the patterns as artefacts that require
explanations within existing frameworks. Which approach to take becomes more difficult to identify when
AI systems generate knowledge that resists human interpretation or integration into existing theory.
Progress in AI for science offers a moment for reflection on what types of understanding remain essentially
human and how AI might enhance rather than replace such human capabilities (Lawrence, 2024; Krenn et al.,
2022).
One perspective is that science serves fundamentally human purposes, whether advancing human
understanding of the world, solving social or environmental challenges, or informing policy and governance,
and those purposes are better served by AI tools that enhance human reasoning. From this view, effective AI
systems would function as ‘Socratic guides’ that probe a researcher’s thinking and challenge them to develop
ideas further.
An alternative perspective is that human understanding is an unnecessary limitation on artificial scientific
systems; that autonomous AI systems might discover predictive models or mechanisms beyond human
comprehension, without requiring human interpretability to advance the frontiers of science. Recent agentic
systems offer test cases. Self-driving laboratories and end-to-end research agents produce outputs whose
provenance runs through autonomous planning and execution that may be opaque to humans. How those
outputs should be validated is an open problem.
These perspectives stem in part from what is meant by understanding. Scientific work draws on different
kinds of understanding: operational understanding (can a system be used safely and reliably?), mechanistic
understanding (is there an interpretable or causal account of why something works?), paradigm understanding
(can a community reproduce or contest the result?) and social understanding (are the ideas legible to
the wider community?). AI affects these differently. A prediction system may deliver strong operational
understanding without offering mechanistic insight; an autonomous discovery pipeline may produce results
that are mechanistically opaque and epistemologically difficult to contest. These kinds of understanding have
previously developed together. A human moving from observations to predictive generalisation discovers and
understands in the same process. AI loosens this connection: a system can perform that induction without
understanding. The question of whether AI enhances scientific understanding depends on which kinds of
understanding are preserved, which are displaced, and whether those trade-offs are acceptable in a given
context.
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
14 Cranmer, Lawrence, Montgomery, and Thérien
These perspectives each have implications for how AI systems are designed and validated in scientific
contexts. Science is in a messy phase of developing these modes of AI use. There are examples of collaboration:
mathematicians have used systems such as AlphaEvolve to explore open problems, with the AI generating
candidate constructions that researchers then interrogate and develop (Georgiev et al., 2025). At the same
time, early evidence suggests that routine use of LLMs can erode reasoning skills: studies of LLM-assisted
writing and knowledge work suggest diminished critical thinking among frequent users (Kosmyna et al., 2025;
Lee et al., 2025).
The insight–discovery gap has implications beyond the laboratory. It bears on the social role of the scientist
and the scientific community. Even before the advent of generative AI, in the context of policy advice given
during the Covid-19 pandemic, the use of large mathematical models that have escaped the understanding
of their creators has been questioned (Saltelli et al., 2020). Generative AI brings further challenges to how
scientists convene such advice and present it to policy-makers.
Developing AI as a collaborative partner, which supports researchers as they build conceptual frameworks
and theoretical structures in the human process of making sense of the world, is therefore both a technical
and social challenge. Several strategies for enhancing human-AI collaboration are already emerging (Berens
et al., 2023). These include:
symmetries;
Each approach addresses different aspects of the collaboration challenge, from embedding human
understanding in AI models to extracting expertise that researchers may struggle to articulate.
6. Institutional readiness
AI adoption in science is outpacing institutional adaptation, creating misalignments between rapidly
evolving AI capabilities and the policies, processes, and infrastructure needed to support their responsible
use. These challenges are compounded by the concentration of AI capabilities in a small number of
technology companies, which creates new frictions that potentially threaten open innovation. Addressing
these institutional considerations requires creativity in policy development and coordinated responses across
funding, governance, infrastructure, and skills development.
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 15
6.1. The governance gap
AI creates new governance challenges and amplifies familiar research integrity issues (Resnik and Hosseini,
2025). The use of large datasets to train AI systems raises ethical concerns about bias, meaningful consent
for data use, and privacy or security in data handling. Meanwhile, the complexity and opacity of AI systems
create new challenges for transparency and explainability in scientific analysis, with direct implications for
both scientific understanding and reproducibility (Ball, 2023). These concerns come into sharp focus in the
context of generative AI systems that can produce plausible but inaccurate results—what has been termed
‘careless speech’—requiring careful expert validation to detect and address (Wachter et al., 2024). AI also
introduces questions about attribution and accountability, and the contours of acceptable use in the creation
of scientific outputs. In parallel, by identifying errors in code, surfacing inconsistencies in statistics, and
detecting weak results in the published literature, AI could offer a route to addressing some of today’s
challenges in scientific reproducibility (Gibney, 2025).
Whether AI’s net effect on scientific rigour is positive or negative will depend on how these tools are used.
While a range of policy frameworks addressing elements of these challenges already exist, from principles for
trustworthy AI to guidelines for the use of generative AI in science to policies on research integrity, there is
a persistent gap between policy and practice (European Commission: Directorate-General for Research and
Innovation and Montgomery, 2025).
6.2. The research culture gap
The importance of collaboration between AI and domain researchers in advancing AI for science highlights
longstanding challenges in supporting interdisciplinary work (National Academy of Sciences et al., 2005).
Research institutions are typically designed to reward disciplinary depth over cross-domain collaboration.
Incentive structures struggle to accommodate interdisciplinary research, resulting in limited career pathways
for researchers working at the interface of AI and science. A lack of scientifically-tailored training opportunities
means it can be difficult for domain researchers to develop AI skills. Meanwhile, funding mechanisms remain
poorly adapted to team science approaches, creating barriers to supporting essential roles such as research
software engineers and data managers.
6.3. The infrastructure gap
Digital divides in access to AI infrastructure create the conditions for unequal participation in AI for science.
Many of today’s most successful AI approaches depend on high-performance computing facilities that require
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
16 Cranmer, Lawrence, Montgomery, and Thérien
substantial financial resources and generate significant environmental costs (Bommasani et al., 2021). Large-
scale scientific projects have often required concentrated infrastructure, as seen, for example, in the Human
Genome Project and the Large Hadron Collider. However, these have typically been publicly funded and
openly accessible. What distinguishes today’s AI landscape is that the computational infrastructure needed
for advanced AI capabilities is concentrated in a handful of private technology companies. The scale and
cost of developing such infrastructure is cultivating new dependencies on commercial entities. Commercial
drivers also mean that, for some companies, science is also being seen as a test-bed for a company’s AI
capabilities. Dependence on closed model or datasets, or restricted access to computational resources, and
the commercial importance of results compromises the independence that characterises scientific inquiry.
When a few companies control the development of AI systems that are embedded in research, they also
influence methodological choices and research directions. This represents a departure from the tradition
of publicly-funded, openly-accessible scientific infrastructure that has been the backbone of much modern
scientific progress.
Alongside this compute infrastructure, AI for science relies on data infrastructures that ensure data is
accessible, curated, and appropriately governed, ensuring its use aligns with research participant expectations
and ethical frameworks. What ‘data readiness’ for AI looks like in practice varies across disciplines and
applications (Brewer et al., 2025). A shared challenge in many areas of science is the design of incentive
structures to encourage trustworthy data governance and use, and resources to support this.
An open science approach can help address these challenges (Lawrence and Montgomery, 2024).
Traditional models of open science assumed that research tools and infrastructure could be freely shared and
replicated. Today’s AI capabilities often depend on computational resources, training datasets, and specialised
expertise that are difficult to reproduce. The challenge that follows is to bridge the ideal of open innovation
with the reality of AI deployment. Investment in open-source toolkits and shared engineering services can
bridge the implementation gap by making AI deployment more accessible to domain researchers (Donoho,
2024). International collaborations are helping to widen access to compute resources1 and institution-led
programmes that provide engineering support for AI implementation2. The question is how to scale these
initiatives and deliver a sustainable open infrastructure that enables widespread participation in AI-enabled
scientific discovery. Growing concerns about AI sovereignty in many countries adds a new urgency to this
1 Such as the International Computation and AI Network and EuroHPC programmes 2 Such as the Accelerate Programme for Scientific Discovery: science.ai.cam.ac.uk
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 17
policy agenda. Without proactive policy responses, science risks becoming dependent on proprietary systems
that may not align with scientific values such as openness, reproducibility, and independence.
6.4. The discourse gap
The concentration of advanced AI capabilities in a small number of technology companies brings with it a
new challenge in framing the public conversation about AI in science. These entities benefit from substantial
public relations resources that allow them to take a prominent position in public and policy discourse about
AI, and about its role in science. While the scientific contributions are often impressive, the amplification of
corporate AI projects distorts perceptions of AI progress. It contributes to a policy environment where AI
for science becomes synonymous with corporate interests, despite foundational work originating in a wider
community of institutions. Such high-profile successes often depend on decades of publicly-funded research,
which is often poorly recognised, potentially misdirecting policy support away from the research infrastructure
that enables innovation. For example, the protein folding advances that came from AlphaFold (Jumper et al.,
2021) were enabled by a significant investment in data infrastructure and benchmarking dating back to 1994
(Moult et al., 1995).
This narrative dominance also shapes perceptions of what AI for science looks like in practice. Successful AI
for science projects can be large-scale, infrastructure and engineering-heavy projects; they can also be smaller
scale innovations rooted in democratised access to AI capabilities. When corporate narratives dominate, policy
discourse may reflect this emphasis, potentially shaping preferences toward particular models of innovation
and infrastructure, which struggle to envision a distributed, accessible infrastructure that would enable
broader participation in AI-enabled scientific discovery.
This political economy of AI for science links to an issue of epistemic attribution. Science communication
has long struggled to counter a ‘lone genius’ narrative of discovery. AI adds a new version of this narrative,
with headlines that proclaim AI discoveries obscuring the work of the teams and communities that sit behind
those advances. The Protein Data Bank, for example, reflects the cumulative work of thousands of researchers.
These stories about autonomous discovery make the work of building interdisciplinary teams, curating data,
and developing human-machine collaborations harder to see, and potentially harder to build as a result.
6.5. The policy and coordination gap
Addressing these institutional readiness gaps requires policy interventions that tackle governance, cultural,
and infrastructure challenges.
# ACCEPTED M NUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
18 Cranmer, Lawrence, Montgomery, and Thérien
Public funding agencies face particular challenges in navigating AI for science as an area that is both fast-
moving and that cuts across all areas of research and research governance. Large-scale scientific transformation
has typically required coordinated public investment; projects like the Large Hadron Collider and Human
Genome Project succeeded with sustained public funding and scientific collaboration. That infrastructure,
however, focuses on specific challenges in targeted domains, while the potential of AI comes from its
applicability across the sciences. Traditional funding models struggle to accommodate the computational
scale and interdisciplinary nature of AI research, which requires both ground-up and top-down interventions.
The latter to provide core infrastructure, such as compute or data resources, and the former to support
researchers to respond to the opportunities they see in their field in innovative and agile ways.
A policy agenda for AI in science should enable adoption while fostering responsible research and
innovation through action in five key areas (European Commission: Directorate-General for Research and
Innovation and Montgomery, 2025):
application across domains, with attention to supporting interdisciplinary collaborations;
ethical AI use in research contexts;
democratise AI capabilities;
with privacy and security; and
training opportunities for domain researchers.
History shows that periods of heightened expectations around new technologies can reduce critical scrutiny
and sow the seeds of practices that undermine trust. Thoughtful policy interventions can help prevent a
default to technology production over scientific understanding. The goal is to create an environment where
AI accelerates scientific progress while maintaining scientific integrity and public trust.
7. Advancing an agenda for AI in science
In 2023, we developed a research agenda for AI in science inspired by experiences of deploying machine
learning in scientific contexts (Berens et al., 2023). Those experiences showed both the potential of AI
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 19
tools—in areas from agriculture to zoology—and the technical gaps that needed to be addressed to realise
that potential.
Since then, the field of AI for science has changed rapidly. LLMs expanded the range of applications of
AI for science, and brought natural language interfaces to AI systems that made AI more accessible to a
wider community of users. Generative AI has demonstrated capabilities in coding, literature synthesis, and
hypothesis generation that suggest new opportunities to integrate AI in scientific workflows. At the same time,
foundation models trained on large-scale scientific datasets have demonstrated breakthrough performance
in scientifically challenging areas. Agentic AI brings with it a new wave of excitement about autonomous
research assistants. This progress has captured the attention of policymakers, who are increasingly looking to
AI as a lever for scientific innovation and economic competitiveness. The result is an environment of growing
expectations about the role of AI in driving innovation.
Fundamental challenges in the field persist. The core technical problems we set out in 2023—grounding
AI in scientific understanding, developing sophisticated simulations, and bridging from pattern matching
to causal reasoning—remain mostly unresolved. Other challenges have changed or become more salient
over time. Concerns about accuracy and reproducibility have intensified as AI systems have grown more
complex. Meanwhile, the computational demands of state-of-the-art AI approaches risk creating a system
where advanced capabilities are concentrated in a few institutions, potentially undermining the open nature
of scientific inquiry, and bring fresh concerns about the environmental impact of AI development.
There is an opportunity now for the field to reframe the role of AI in science in ways that connect AI
advances to areas of scientific need. This reframing would prioritise developing AI tools designed specifically
for scientific contexts. It would address the broader transformation of scientific practice that AI enables,
considering both technical capabilities and the institutional changes needed to support responsible adoption.
8. Conclusion
This call for papers on AI for science by RSS Data Science and AI seeks to move beyond the current hype cycle
to a deeper understanding of the possibilities and limitations of AI in science. Underpinning the analysis in
this paper is a question about whether AI represents a paradigm shift in scientific practice, or a continuation
of the computational trajectory that has shaped research for decades. That question has implications for the
practice, purpose, and policies surrounding AI for science, including: what technical advances are needed
to move AI beyond pattern matching toward causal reasoning and mechanistic understanding; whether
scientific understanding is intrinsically human or whether science can progress through knowledge that resists
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
20 Cranmer, Lawrence, Montgomery, and Thérien
human interpretation; and what institutional changes are needed to support responsible AI adoption. These
are questions the special issue invites contributors to take up from technical, methodological, empirical,
institutional, and philosophical perspectives, alongside examples of innovative research at the intersection of
AI and the sciences. Contributions might consider:
reimagine its role in future.
responsible AI adoption.
The aim is to move beyond the current hype cycle to a more intentional conversation about the possibilities
and limitations of AI in science, guided by a vision of AI that enhances scientific inquiry.
Data availability
Not applicable.
Funding
Not applicable.
Conflict of interests
No competing interest is declared.
9. Author contributions statement
K.C., N.D.L., and J.K.M. conceived the position paper, J.K.M. drafted the manuscript. K.C., N.D.L., J.M.,
and D.T. reviewed and refined the manuscript.
10. Acknowledgments
The authors thank the anonymous reviewers for their valuable suggestions.
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 21
References
ai@cam, Bennett Institute for Public Policy, and Minderoo Centre for Technology & Democracy.
Policy brief: Refreshing the uk’s strategic approach to ai. Technical report, University
of Cambridge, Cambridge, UK, December 2024. URL https://www.ai.cam.ac.uk/reports/
policy-brief-refreshing-the-uk-s-strategic-approach-to-ai/.
A. Allen, S. Markou, W. Tebbutt, J. Requeima, W. P. Bruinsma, T. R. Andersson, M. Herzog, N. D. Lane,
M. Chantry, J. S. Hosking, and R. E. Turner. End-to-end data-driven weather prediction. Nature, 641:1172–1179,
2025. doi: 10.1038/s41586-025-08897-0.
P. W. Anderson. More is different. Science, 177(4047):393–396, 1972. doi: 10.1126/science.177.4047.393.
D. Arranz, S. Bianchini, V. Di Girolamo, and J. Ravet. Trends in the use of AI in science: A bibliometric analysis.
Technical report, Publications Office of the European Union, 2023.
C. A. Bail. Can generative AI improve social science? Proceedings of the National Academy of Sciences,
121(21):e2314021121, 2024. doi: 10.1073/pnas.2314021121. URL https://www.pnas.org/doi/abs/10.1073/pnas.
2314021121.
M. Baker. 1,500 scientists lift the lid on reproducibility. Nature, 533:452–454, May 2016. doi: 10.1038/533452a.
URL https://www.nature.com/articles/533452a.
P. Ball. Is AI leading to a reproducibility crisis in science? Nature, 624:22–25, 2023. doi: 10.1038/
d41586-023-03817-6.
E. M. Bender, T. Gebru, A. McMillan-Major, and M. Mitchell. On the dangers of stochastic parrots: Can
language models be too big? In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and
Transparency, pages 610–623, 2021. doi: 10.1145/3442188.3445922.
P. Berens, K. Cranmer, N. D. Lawrence, U. von Luxburg, and J. Montgomery. Machine learning for science:
Bridging data-driven and mechanistic modelling. In Dagstuhl Reports, volume 12, pages 150–199. Schloss
Dagstuhl – Leibniz-Zentrum für Informatik, 2023. doi: 10.4230/DagRep.12.9.150.
G. Berman, J. Chubb, and K. Williams. The use of artificial intelligence in science, technology, engineering, and
medicine. Technical report, The Royal Society, 2024.
J. D. Bernal. The Social Function of Science. George Routledge & Sons, London, 1939.
N. Bloom, C. I. Jones, J. Van Reenen, and M. Webb. Are ideas getting harder to find? American Economic
Review, 110(4):1104–1144, 2020. doi: 10.1257/aer.20180338. URL https://doi.org/10.1257/aer.20180338.
R. Bommasani, D. A. Hudson, E. Adeli, R. Altman, S. Arora, S. von Arx, M. S. Bernstein, J. Bohg, A. Bosselut,
E. Brunskill, E. Brynjolfsson, S. Buch, D. Card, R. Castellon, N. Chatterji, A. Chen, K. Creel, J. Q. Davis,
D. Demszky, C. Donahue, M. Doumbouya, E. Durmus, S. Ermon, J. Etchemendy, K. Ethayarajh, L. Fei-Fei,
C. Finn, T. Gale, L. Gillespie, K. Goel, N. Goodman, S. Grossman, N. Guha, T. Hashimoto, P. Henderson,
J. Hewitt, D. E. Ho, J. Hong, K. Hsu, J. Huang, T. Icard, S. Jain, D. Jurafsky, P. Kalluri, S. Karamcheti,
G. Keeling, F. Khani, O. Khattab, P. W. Koh, M. Krass, R. Krishna, R. Kuditipudi, A. Kumar, F. Ladhak,
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
22 Cranmer, Lawrence, Montgomery, and Thérien
M. Lee, T. Lee, J. Leskovec, I. Levent, X. L. Li, X. Li, T. Ma, A. Malik, C. D. Manning, S. Mirchandani,
E. Mitchell, Z. Munyikwa, S. Nair, A. Narayan, D. Narayanan, B. Newman, A. Nie, J. C. Niebles, H. Nilforoshan,
J. Nyarko, G. Ogut, L. Orr, I. Papadimitriou, J. S. Park, C. Piech, E. Portelance, C. Potts, A. Raghunathan,
R. Reich, H. Ren, F. Rong, Y. Roohani, C. Ruiz, J. Ryan, C. Ré, D. Sadigh, S. Sagawa, K. Santhanam, A. Shih,
K. Srinivasan, A. Tamkin, R. Taori, A. W. Thomas, F. Tramèr, R. E. Wang, W. Wang, B. Wu, J. Wu, Y. Wu,
S. M. Xie, M. Yasunaga, J. You, M. Zaharia, M. Zhang, T. Zhang, X. Zhang, Y. Zhang, L. Zheng, K. Zhou, and
P. Liang. On the opportunities and risks of foundation models. 2021. doi: 10.48550/arXiv.2108.07258. URL
https://arxiv.org/abs/2108.07258.
W. Brewer, P. Widener, V. Anantharaj, F. Wang, T. Beck, A. Shankar, and S. Oral. Data readiness for scientific
ai at scale. ICPP Workshops ’25, page 18–24, New York, NY, USA, 2025. Association for Computing Machinery.
ISBN 9798400721090. doi: 10.1145/3750720.3757282. URL https://doi.org/10.1145/3750720.3757282.
S. Cave, C. Craig, K. Dihal, S. Dillon, J. Montgomery, B. Singler, and L. Taylor. Portrayals and perceptions of
AI and why they matter. Technical report, The Royal Society, 2018. URL https://royalsociety.org/-/media/
policy/projects/ai-narratives/AI-narratives-workshop-findings.pdf.
P. Collison and M. Nielsen. Science is getting less bang for its buck. The Atlantic, November 2018. URL
https://www.theatlantic.com/science/archive/2018/11/diminishing-returns-science/575665/.
K. Cranmer, J. Brehmer, and G. Louppe. The frontier of simulation-based inference. Proceedings of the National
Academy of Sciences, 117(48):30055–30062, 2020. doi: 10.1073/pnas.1912789117.
D. Donoho. Data Science at the Singularity. Harvard Data Science Review, 6(1), January 2024. doi: 10.1162/
99608f92.b91339ef.
J. Duarte, S. Han, P. Harris, S. Jindariani, E. Kreinar, B. Kreis, J. Ngadiuba, M. Pierini, R. Rivera, N. Tran, and
Z. Wu. Fast inference of deep neural networks in fpgas for particle physics. Journal of Instrumentation, 13(07),
7 2018. doi: 10.1088/1748-0221/13/07/P07027.
European Commission: Directorate-General for Research and Innovation and J. Montgomery. Framework conditions
and funding for AI in science – mutual learning exercise on national policies for AI in science – first thematic
report. Technical report, Publications Office of the European Union, 2025.
European Research Council. Use and impact of artificial intelligence in the scientific process. Technical report,
European Research Council, 2023.
S. Fortunato, C. T. Bergstrom, K. Börner, J. A. Evans, D. Helbing, S. Milojević, A. M. Petersen, F. Radicchi,
R. Sinatra, B. Uzzi, A. Vespignani, L. Waltman, D. Wang, and A.-L. Barabási. Science of science. Science,
359(6379):eaao0185, 2018. doi: 10.1126/science.aao0185. URL https://www.science.org/doi/10.1126/science.
aao0185.
C. F. Gauss. Fortgesetzte Nachrichten über den Längst vermutheten neuen Haupt-Planeten unseres Sonnen-
Systems. In von Zach (1801), pages 638–649. URL http://books.google.co.uk/books?id=JBw4AAAAMAAJ.
C. F. Gauss. Theoria motus corporum coelestium in sectionibus conicis solem ambientium. F. Perthes und I.
H. Besser, Hamburg, 1809. Translated in 1857 as Theory of Motion of the Heavenly Bodies moving about the
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 23
Sun in Conic Sections by C. H. Davies, Boston: Little, Brown. Reprinted in 1963, New York: Dover.
B. Georgiev, J. Gómez-Serrano, T. Tao, and A. Z. Wagner. Mathematical exploration and discovery at scale, 2025.
URL https://arxiv.org/abs/2511.02864.
E. Gibney. AI tools are spotting errors in research papers: inside a growing movement. Nature, Mar. 2025. doi:
10.1038/d41586-025-00648-5. URL https://doi.org/10.1038/d41586-025-00648-5. News.
J. Haider, K. R. Söderström, B. Ekström, and M. Rödl. Gpt-fabricated scientific papers on google scholar: Key
features, spread, and implications for preempting evidence manipulation. Harvard Kennedy School (HKS)
Misinformation Review, September 2024. doi: 10.37016/mr-2020-156.
A. Halevy, P. Norvig, and F. Pereira. The unreasonable effectiveness of data. IEEE Intelligent Systems, 24(2):
8–12, 2009. doi: 10.1109/MIS.2009.36.
T. Hey, S. Tansley, and K. Tolle, editors. The Fourth Paradigm: Data-Intensive Scientific Discovery. Microsoft
Research, 2009. ISBN 978-0-9825442-0-4.
D. Hume. An Enquiry Concerning Human Understanding. A. Millar, London, 1748. Section IV: ”Sceptical
Doubts Concerning the Operations of the Understanding”.
P. Humphreys. The philosophical novelty of computer simulation methods. Synthese, 169:615–626, 2009. doi:
10.1007/s11229-008-9435-2.
E. T. Jaynes. Information theory and statistical mechanics. Physical Review, 106(4):620–630, 1957. doi: 10.1103/
PhysRev.106.620.
J. Jumper, R. Evans, A. Pritzel, et al. Highly accurate protein structure prediction with AlphaFold. Nature, 596:
583–589, 2021. doi: 10.1038/s41586-021-03819-2.
S. Kapoor and A. Narayanan. Could AI slow science? https://www.aisnakeoil.com/p/could-ai-slow-science, 2025.
R. Kitchin. Big data, new epistemologies and paradigm shifts. Big Data & Society, 1(1), 2014. doi: 10.1177/
2053951714528481.
A. Korinek. Ai agents for economic research. NBER Working Paper 34202, National Bureau of Economic Research,
Sept. 2025. URL https://www.nber.org/papers/w34202.
N. Kosmyna, E. Hauptmann, Y. T. Yuan, J. Situ, X.-H. Liao, A. V. Beresnitzky, I. Braunstein, and P. Maes. Your
brain on chatgpt: Accumulation of cognitive debt when using an ai assistant for essay writing task, 2025. URL
https://arxiv.org/abs/2506.08872.
M. Krenn, R. Pollice, S. Y. Guo, M. Aldeghi, A. Cervera-Lierta, P. Friederich, G. dos Passos Gomes, F. Häse,
A. Jinich, A. Nigam, Z. Yao, and A. Aspuru-Guzik. On scientific understanding with artificial intelligence.
Nature Reviews Physics, 4:761–769, December 2022. doi: 10.1038/s42254-022-00518-3. URL https://doi.org/
10.1038/s42254-022-00518-3.
T. S. Kuhn. The Structure of Scientific Revolutions. University of Chicago Press, Chicago, IL, 1962.
D. Kwon. Scientists split on ethics of AI use. Nature, 641:574–578, May 2025. doi: 10.1038/d41586-025-01463-8.
J. M. Laurent, J. D. Janizek, M. Ruzo, M. M. Hinks, M. J. Hammerling, S. Narayanan, M. Ponnapati, A. D.
White, and S. G. Rodriques. Lab-bench: Measuring capabilities of language models for biology research. arXiv
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
24 Cranmer, Lawrence, Montgomery, and Thérien
preprint arXiv:2407.10362, 2024. doi: 10.48550/arXiv.2407.10362. URL https://arxiv.org/abs/2407.10362.
A. Laverick, K. Surrao, I. Zubeldia, B. Bolliet, M. Cranmer, A. Lewis, B. Sherwin, and J. Lesgourgues. Multi-agent
system for cosmological parameter analysis, 2024. URL https://arxiv.org/abs/2412.00431.
N. Lawrence, J. Montgomery, and B. Schölkopf. Machine learning for science: Mathematics at the interface of
data-driven and mechanistic modelling. Oberwolfach Reports, 20(2):1453–1484, 2023. doi: 10.4171/OWR/2023/
26.
N. D. Lawrence. The Atomic Human. Allen Lane, 2024.
N. D. Lawrence and J. Montgomery. Accelerating AI for science: open data science for science. Royal Society
Open Science, 11:231130, 2024. doi: 10.1098/rsos.231130.
H.-P. H. Lee, A. Sarkar, L. Tankelevitch, I. Drosos, S. Rintel, R. Banks, and N. Wilson. The impact of generative ai
on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge
workers. In Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems, CHI ’25, New
York, NY, USA, 2025. Association for Computing Machinery. ISBN 9798400713941. doi: 10.1145/3706598.
3713778. URL https://doi.org/10.1145/3706598.3713778.
J.-L. Lieberum, M. Toews, M.-I. Metzendorf, F. Heilmeyer, W. Siemens, C. Haverkamp, D. Böhringer, J. J.
Meerpohl, and A. Eisele-Metzger. Large language models for conducting systematic reviews: on the rise, but
not yet ready for use—a scoping review. Journal of Clinical Epidemiology, 181:111746, May 2025. doi:
10.1016/j.jclinepi.2025.111746.
C. Lu, C. Lu, R. T. Lange, Y. Yamada, S. Hu, J. Foerster, D. Ha, and J. Clune. Towards end-to-end automation
of AI research. Nature, 651:914–919, 2026. doi: 10.1038/s41586-026-10265-5.
A. Merchant, S. Batzner, S. S. Schoenholz, et al. Scaling deep learning for materials discovery. Nature, 624:80–85,
2023. doi: 10.1038/s41586-023-06735-9.
J. Moult, J. T. Pedersen, R. Judson, and K. Fidelis. A large-scale experiment to assess protein structure prediction
methods. Proteins: Structure, Function, and Genetics, 23(3):ii–iv, 1995. doi: 10.1002/prot.340230303.
A. Narayanan and S. Kapoor. Ai as normal technology: An alternative to the vision of ai as a potential
superintelligence. Technical report, Knight First Amendment Institute at Columbia University, April 2025.
URL https://knightcolumbia.org/content/ai-as-normal-technology.
National Academy of Sciences, National Academy of Engineering, and Institute of Medicine. Facilitating
Interdisciplinary Research. The National Academies Press, Washington, DC, 2005. doi: 10.17226/11153.
C. O’Grady. Low-quality papers are surging by exploiting public data sets and ai. Science, 388(6749):807–808,
May 2025. doi: 10.1126/science.adz1715. URL https://doi.org/10.1126/science.adz1715.
OpenAI. An OpenAI model has disproved a central conjecture in discrete geometry. https://openai.com/index/
model-disproves-discrete-geometry-conjecture/, May 2026. Accessed: 2026-05-26.
Parallel Science Project. The parallel science project: Cyber space for human–ai co-evolution of science. Preprint,
2026. URL https://parallelscience.github.io/preprint/paper.pdf. Preprint credited to “Claude and the
Denario Core Team”; cited here under the project name.
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
AI for Science 25
L. Parker, F. Lanusse, S. Golkar, L. Sarra, M. Cranmer, A. Bietti, M. Eickenberg, G. Krawezik, M. McCabe,
R. Morel, R. Ohana, M. Pettee, B. Régaldo-Saint Blancard, K. Cho, S. Ho, and T. P. A. Collaboration. Astroclip:
a cross-modal foundation model for galaxies. Monthly Notices of the Royal Astronomical Society, 531(4):
4990–5011, 06 2024. ISSN 0035-8711. doi: 10.1093/mnras/stae1450. URL https://doi.org/10.1093/mnras/
stae1450.
J. Pearl and D. Mackenzie. The Book of Why: The New Science of Cause and Effect. Allen Lane, London, 2018.
J. Peters, D. Janzing, and B. Schölkopf. Elements of Causal Inference: Foundations and Learning Algorithms.
MIT Press, Cambridge, MA, 2017.
G. Piazzi. Fortgesetzte Nachrichten über den Längst vermutheten neuen Haupt-Planeten unseres Sonnen-Systems.
In von Zach (1801), pages 279–283. URL http://books.google.co.uk/books?id=JBw4AAAAMAAJ.
R. Pielke. In retrospect: The social function of science. Nature, 507:427–428, March 2014. doi: 10.1038/507427a.
URL https://doi.org/10.1038/507427a.
K. R. Popper. Conjectures and Refutations: The Growth of Scientific Knowledge. Routledge, London, 1963.
D. B. Resnik and M. Hosseini. The ethics of using artificial intelligence in scientific research: new guidance needed
for a new tool. AI Ethics, 5:1499–1521, 2025. doi: 10.1007/s43681-024-00493-8. URL https://doi.org/10.1007/
s43681-024-00493-8.
A. Saltelli, G. Bammer, I. Bruno, E. Charters, M. Di Fiore, E. Didier, W. N. Espeland, J. Kay, S. Lo Piano,
D. Mayo, R. Pielke Jr, T. Portaluri, T. M. Porter, A. Puy, I. Rafols, J. R. Ravetz, E. Reinert, D. Sarewitz, P. B.
Stark, A. Stirling, J. van der Sluijs, and P. Vineis. Five ways to ensure that models serve society: a manifesto.
Nature, 582(7813):482–484, 2020. doi: 10.1038/d41586-020-01812-9.
B. Schölkopf. Causality for machine learning. In H. Geffner, R. Dechter, and J. Y. Halpern, editors, Probabilistic
and Causal Inference: The Works of Judea Pearl, chapter 39, pages 765–804. ACM, 2022. doi: 10.1145/3501714.
B. Schölkopf, D. Janzing, J. Peters, E. Sgouritsa, K. Zhang, and J. Mooij. On causal and anticausal learning.
In Proceedings of the 29th International Conference on Machine Learning, pages 1255–1262, New York, NY,
USA, 2012. Omnipress.
S. M. Stigler. Laplace’s 1774 memoir on inverse probability. Statistical Science, 1:359–378, 1986. doi: 10.1214/ss/
1177013620.
S. M. Stigler. Statistics on the Table: The History of Statistical Concepts and Methods. Harvard University
Press, Cambridge, MA, 1999. ISBN 0-674-00979-7.
J. Straiton. Artificial intelligence: help or hindrance in solving the reproducibility crisis? BioTechniques, 76(7):
291–294, 2024. doi: 10.1080/07366205.2024.2355776. PMID: 38899492.
R. Sutton. The bitter lesson. http://www.incompleteideas.net/IncIdeas/BitterLesson.html, Mar. 2019. Accessed:
2026-05-22.
F. Villaescusa-Navarro, B. Bolliet, P. Villanueva-Domingo, A. E. Bayer, A. Acquah, C. Amancharla, A. Barzilay-
Siegal, P. Bermejo, C. Bilodeau, P. C. Ramı́rez, M. Cranmer, U. L. França, C. Hahn, Y.-F. Jiang, R. Jimenez,
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026
26 Cranmer, Lawrence, Montgomery, and Thérien
J.-Y. Lee, A. Lerario, O. Mamun, T. Meier, A. A. Ojha, P. Protopapas, S. Roy, D. N. Spergel, P. Tarancón-
Álvarez, U. Tiwari, M. Viel, D. Wadekar, C. Wang, B. Y. Wang, L. Xu, Y. Yovel, S. Yue, W.-H. Zhou, Q. Zhu,
J. Zou, and Íñigo Zubeldia. The denario project: Deep knowledge ai agents for scientific discovery, 2025. URL
https://arxiv.org/abs/2510.26887.
F. X. von Zach, editor. Monatliche Correspondenz zur beförderung der Erd- und Himmels-kunde. Number v. 4.
Beckerische Buchhandlung., 1801. URL http://books.google.co.uk/books?id=JBw4AAAAMAAJ.
S. Wachter, B. Mittelstadt, and C. Russell. Do large language models have a legal duty to tell the truth? Royal
Society Open Science, 11:240197, 2024. doi: 10.1098/rsos.240197. URL https://doi.org/10.1098/rsos.240197.
J. Wiens, S. Saria, M. Sendak, M. Ghassemi, V. X. Liu, F. Doshi-Velez, K. Jung, K. Heller, D. Kale, M. Saeed,
P. N. Ossorio, S. Thadaney-Israni, and A. Goldenberg. Do no harm: a roadmap for responsible machine learning
for health care. Nature Medicine, 25:1337–1340, Sept. 2019. doi: 10.1038/s41591-019-0548-6.
E. P. Wigner. The unreasonable effectiveness of mathematics in the natural sciences. Communications on Pure
and Applied Mathematics, 13(1):1–14, 1960. doi: 10.1002/cpa.3160130102.
Kyle Cranmer. Kyle Cranmer leads the Data Science Institute at UW-Madison in its mission for innovation,
translation and collaboration on data science. He is also Professor of Physics, Computer Sciences, and Statistics at
UW–Madison, and leads the RISE-AI initiative. Prior to joining UW-Madison, he was a Professor of Physics and
Data Science and the Executive Director of the Moore-Sloan Data Science Environment at New York University.
His primary research interests are in machine learning and statistical inference for the physical sciences, and his
background is in experimental particle physics.
Neil D. Lawrence. Neil D. Lawrence is the inaugural DeepMind Professor of Machine Learning at the University
of Cambridge where he is also the academic lead of ai@cam, the University’s flagship mission on AI. He is visiting
Professor at the University of Sheffield and author of the book The Atomic Human. His research focus is on
challenges of deploying AI in the real world.
Jessica Montgomery. Jessica Montgomery is Director of ai@cam, the University of Cambridge’s strategic mission to
develop AI technologies that serve science, citizens, and society. Her research interests focus on AI for science and
governance challenges of deploying AI for societal benefit. She leads programmes including Accelerate Science and
the Data Trusts Initiative. Previously, she established AI policy programmes at the Royal Society involving public
dialogue and stakeholder engagement, and worked in parliamentary science policy roles.
Denis Thérien. Denis Thérien is VP of Research Partnerships at ServiceNow. Before joining ServiceNow Research, Dr.
Thérien was Vice-President Research and Partnerships at Element AI. He previously occupied a similar position at
the Canadian Institute for Advanced Research (CIFAR), after serving as Vice Principal of Research and International
Relations at McGill University.
# ACCEPTED M ANUSCRIPT
D ow
nloaded from  academ
ic.oup.com /rssdat/advance-article/doi/10.1093/rssdat/udag003/8781111 by guest on 09 Septem
ber 2026