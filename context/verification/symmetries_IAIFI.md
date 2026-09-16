# Why "Approximate Structure" Beats "Exact Structure" in Physics-Informed ML
 
**Source:** IAIFI Summer Workshop 2026, Day 2 (Tuesday, Aug 11, 2026) — MIT Schwarzman College of Computing
**Talks:** Tilman Plehn (Heidelberg) — *ML-Enhanced LHC Simulations*; Behrooz Tahmasebi (Harvard) — *Approximate Symmetry Is Exponentially Easier than Exact Symmetry*
 
---
 
## The Core Claim
 
On the same day, two speakers — one a particle physicist arguing from detector physics, one a learning theorist arguing from Fourier analysis on groups — independently reached the same conclusion: **neural networks should be built with approximately correct symmetry constraints, never exact ones.** Exact symmetry is both physically wrong (it doesn't match how nature or the detector actually behaves) and computationally intractable (it costs exponentially more and buys nothing in generalization).
 
---
 
## Part 1 — Plehn: The Physics Argument
 
**Speaker background.** Plehn is a theoretical particle physicist (phenomenologist) at Heidelberg and one of the founding figures of the modern ML-for-LHC community. His group works on generative networks, uncertainty quantification, and precision simulation. He is lead author of the standard reference *Modern Machine Learning for LHC Physicists* ([arXiv:2211.01421](https://arxiv.org/abs/2211.01421)).
 
### Setup: why symmetry matters for dimensionality
 
> A basic observation from any QFT course: a 2→2 scattering process involves four four-vectors — 16 numbers — but after imposing all symmetries the amplitude depends on only **two invariants**. "I don't have to calculate over 16 dimensions; I only have to calculate over two." The curse of dimensionality is real, so exploiting symmetry to reduce dimensionality is the first move, for machine learning as much as for humans.
 
This motivated work on **equivariant** (Plehn: physicists say *covariant* — "it's literally the same thing") **transformers**.
 
### The results: equivariant transformers get the best of both worlds
 
- The **specialized equivariant network** is excellent at low dimension but degrades as dimension grows.
- The **standard out-of-the-box transformer** is poor at low dimension but scales far better.
- **Equivariant/covariant transformers** (he showed two realizations: L-GATr, geometric-algebra-based, and LLoCa, based on local canonicalization — performing almost identically) **beat the best specialized network at low dimension while scaling like a transformer.** Best of both worlds.
These architectures generalize beyond amplitudes — also applied to jet tagging and event generation.
 
> "My claim is that **understanding data beats performance**. I don't like the bitter lesson a lot, as you might guess."
 
### The caveat: exact symmetry doesn't exist in particle physics
 
> **Stated flatly:** "For particle physics, **every good symmetry is broken** — either by the Higgs mechanism or by the experiment. So don't try to build perfect symmetries. **Perfect symmetries in particle physics don't exist.**"
 
**Why:** The electroweak symmetry is spontaneously broken by the Higgs mechanism — the vacuum itself selects a direction, so a network hard-coding the unbroken symmetry group encodes a fiction. Independently, the detector geometry, readout, and measurement process break symmetries that the underlying theory would otherwise respect. A model forced into *exact* invariance is invariant under a symmetry the real data doesn't actually have.
 
### On inference cost
 
> He showed loss (top-tagging quality) against CPU inference time: if you want a very cheap network, use a plain transformer, because equivariant transformers carry overhead you must pay for. But once you are willing to spend on the order of a millisecond per evaluation, the four equivariant implementations shown all beat the standard transformer.
 
---
 
## Part 2 — Tahmasebi: The Learning-Theory Argument
 
**Speaker background.** A researcher in geometric machine learning at Harvard, working on the theory of symmetry in learning across applications from AI-for-science onward. This was the only pure-theory talk of the session, supplying formal backing for a position several other speakers reached empirically.
 
### Why exact symmetry enforcement is expensive
 
> **Background — group averaging.** If you want a model that is invariant under a group of transformations G (rotations, permutations, Lorentz boosts), the canonical construction is **group averaging**: take any function f, apply every group element to the input, and average the results. The output is exactly invariant by construction, and it works for any architecture.
 
The problem: this requires averaging over the **entire group**, and groups are typically enormous discrete sets.
 
> "It's a really nice way to make any architecture or function symmetric, but unfortunately it's just impractical, because you'd have to average over something like 10⁶⁴ elements." (Illustration: the number of permutations of 50 letters exceeds the number of atoms in the observable universe.)
 
You cannot enumerate that, and you cannot differentiate your way around it either, because the group is discrete — there is no gradient to follow.
 
### The fix: random subsets are (almost) as good as the whole group
 
A **generating set** is a subset of a group whose products reproduce the whole group. Two facts:
- Finding a *minimal* generating set is NP-hard.
- But generating sets of only **logarithmic size** in |G| exist — exponentially better than the whole group.
**The answer is randomness.** A theorem from random-graph/group theory (random Cayley graphs / expanders, developed in the 1990s) states that a random subset of size **≈ 3 log|G|** is a generating set with high probability.
 
> "Imagine you have some symmetries in your dataset, and you can discover them randomly. You just randomly choose elements, and using log|G| elements you discover the whole group."
 
### The main result: one sampled subset works for the entire training run
 
The key theorem bounds the error between the **full group average** and a **partial average over a randomly chosen subset**, with subset size logarithmic in |G| — and, crucially, the bound holds **uniformly over the whole function class**.
 
> "Not only do you have this nice approximation result for a function — you have it for **all** functions. You can approximate averages uniformly without changing the subset. Just one set S works for all of them."
 
**Why the uniformity matters practically:** during training, the function changes at every step. If the bound only held for one fixed function, you'd need to resample the subset constantly. Because it holds uniformly, you can **sample the subset once, offline**, and use it throughout training.
 
**Experimental confirmation** (small-scale, by design — a 3-layer MLP learning the sign-invariant absolute-value function):
- One fixed subset improves test loss uniformly over the whole course of training, exactly as predicted.
- Even for a group of order 2²⁰, the test-loss improvement **saturates once the subset reaches roughly log|G|**. Beyond that, no further gains.
> "You might remove other modes of asymmetry, but in terms of **generalization error**, you're done."
 
### The complementary result: exact symmetry requires the entire group
 
The other half of the paper asks: what if you need the partial average to *exactly equal* the full group average, for every function in the class? Even allowing arbitrary non-negative weights on the subset (maximal generosity), the result for **moderate-degree polynomials** is:
 
> "Even for polynomial function spaces, which are more regular than neural networks, **you cannot achieve this unless S is the full group.**"
 
**Summary as delivered:**
- **Exact symmetry enforcement by averaging is hard** — you must average over the whole group; no clever subset exists.
- **Approximate symmetry, sufficient for test loss and generalization, needs only a logarithmically-sized random subset** — supported by both theory and experiment.
### Proof technique
 
Rests on **Fourier analysis on groups**. Standard tools fail here — classical large-deviation theory and the usual concentration inequalities don't work because of the supremum over the function class ("apply them and you get nothing"). What's required is a **chaining argument** (the group analogue of Dudley's entropy integral).
 
Published at **ICLR 2026**. Related applications from the same group: constrained optimization over groups (ICML, prior year), and data augmentation, where expanders yield scaling laws for how much augmentation is needed.
 
---
 
## Part 3 — The Convergence
 
> **Note (from the Day 2 transcript, appended to Plehn's section):** Compare Behrooz Tahmasebi's contributed talk that afternoon, which proves that *approximate* symmetry is exponentially cheaper to enforce than exact symmetry. Plehn arrives at the same conclusion empirically and from physics; Tahmasebi arrives at it from learning theory. **That convergence is one of the strongest technical throughlines of the day.**
 
> **Insight (from the annotated transcript's synthesis):** "Theory arrived at the same place as practice, independently and on the same day. Plehn: 'every good symmetry is broken — don't try to build perfect symmetries.' Tahmasebi: exact symmetry costs the whole group; approximate symmetry costs log|G|. One argument is from detector physics, the other from Fourier analysis on groups. When a community's empirical heuristic and its learning theory converge, the heuristic is worth treating as a design rule rather than a shortcut."
 
> **From the day's closing impressions notes:** "Plehn reached the identical conclusion that morning from detector physics ('every good symmetry is broken; don't build perfect symmetries'). So the same day, two people suggested the same thing: **impose an approximately correct structure, know which constraints are approximations, and stop paying for exactness.**"
 
---
 
## The Two Independent Reasons, Side by Side
 
| | **Plehn (Physics)** | **Tahmasebi (Learning Theory)** |
|---|---|---|
| **Claim** | Exact symmetries don't exist in particle physics — broken by the Higgs mechanism or the detector | Exact symmetry enforcement by group averaging requires the *entire* group, even for simple function classes |
| **Cost of insisting on exactness** | You build a model that's invariant under a symmetry the real data doesn't actually respect — systematically wrong | Exponential: e.g. averaging over 10⁶⁴ group elements for 50-object permutations |
| **What works instead** | Equivariant/covariant transformers that beat specialized networks at low dimension while scaling like plain transformers | A random subset of size ≈ 3 log\|G\| — sampled once, offline — captures essentially all the generalization benefit |
| **Where the benefit plateaus / caveat** | Equivariant architectures carry inference overhead; worth it once you can spend ~1ms/evaluation | Test-loss improvement **saturates** at |S| ≈ log|G|; further averaging removes residual asymmetry but doesn't improve generalization |
 
---
 
## Practical Upshot
 
Don't build neural network architectures that enforce **perfect, exact** symmetry constraints (full group averaging, exactly-equivariant layers over the entire symmetry group). Instead:
 
1. **Identify the approximate symmetry** the real physical system actually has (accounting for how it's broken — by dynamics, by the measurement apparatus, etc.).
2. **Enforce it approximately** — e.g., via a small random subset of the symmetry group, or via architectures like L-GATr/LLoCa that are equivariant but don't insist on exactness beyond what's physically warranted.
3. **Know which constraints are approximations.** The "right move is approximately correct structure, never exact structure" — because exact structure is both physically false and computationally wasteful, while approximate structure captures essentially all the achievable benefit at a fraction of the cost.
---
 
## References Mentioned
 
- Plehn, Butter, Dillon, Heimel, Krause, Winterhalder — *Modern Machine Learning for LHC Physicists*, [arXiv:2211.01421](https://arxiv.org/abs/2211.01421)
- Krämer & Plehn — *Machine Learning is Good for Physics — and Vice Versa*, [arXiv:2608.05812](https://arxiv.org/abs/2608.05812) (Eur. Phys. J. C)
- Tahmasebi et al. — *Approximate Symmetry Is Exponentially Easier than Exact Symmetry*, ICLR 2026 (title reconstructed from the talk; check ICLR 2026 proceedings for the exact arXiv ID)
- Related: Alon–Roichman expander/random-Cayley-graph results (1990s), the classical basis for the log|G| generating-set theorem
---
 
*Compiled from `IAIFI_2026_Day2_Annotated_Transcript.md` and `Impressions_and_learnings_Day2.tex`, IAIFI Summer Workshop 2026 project notes.*