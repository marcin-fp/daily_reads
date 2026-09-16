
## AI-assisted rank and locality conjectures for CSS quantum codes via Theo-Conjecture
Randy Davila1,2
1First Principles 2Rice University
**We present an AI-assisted conjecturing study in quantum error correction using Theo-Conjecture, a Graffiti-style conjecturing environment with finite invariant tables, a built-in LLM Co-Pilot, and verifierbacked counterexample checks. Starting from a small registry of explicit CSS check presentations, the system generated rankand locality-sensitive distance inequalities, exposed missing hypotheses, and guided the addition of a small number of benchmark quantum codes, counterexample objects, and new Boolean predicates. The episode is therefore a small-data discovery workflow rather than a trained largecorpus prediction task: each added object changed the finite theory in an auditable way. The first discovered pattern proposed a square-root upper bound on CSS distance in terms of independent****Z-check****rank. Steane, Golay, BCH, and toric examples show that this rankonly bound is false in general but isolates a meaningful geometric question. Af-ter the counterexamples were added to the registry, the Theo-Conjecture workflow produced a rank-plus-locality discovery path: deterministic runs surfaced one-sided candidates relating distance to check rank and maximum check weight, while verifier-backed counterexample interaction and Co-Pilot interpretation exposed their****X/Z-asymmetry****through Shor. The resulting symmetric maximum envelope remains conjectural in general and is explicitly presentation-level; it is sharp on Steane, is proved here for several regimes and infinite families, and has survived registry and out-of-sample stress tests, while a stronger symmetric minimum form sur-**
**vives only under additional balance hypotheses. The paper documents a reproducible path from finite CSS-code data to quantum-error-correction conjectures, certified counterexamples, and partial theorems.**
1 Non-technical summary and main contributions This paper has two intertwined goals. The first is methodological: to document a reproducible episode in which an automated conjecturing system, equipped with an LLM Co-Pilot and a verifier for explicit candidate objects, generated quantum-error-correction conjectures and helped find the counterexamples that refined them. The second is mathematical: to isolate rank- and locality-sensitive questions for CSS stabilizer codes that are not simply restatements of standard block-length bounds.
The discovery began with a clean but false inequality suggesting that the CSS distance*d*might be bounded by 2
√*rank(HZ),*where*rank(HZ)*
is the number of independent*Z-type*checks. The failure was informative rather than accidental. Steane is sharp for the floor form, Golay forces a ceiling, a length-127 BCH construction refutes the ceiling in general, and toric codes show that the square-root exponent is the natural twodimensional geometric scale. After those examples were added back to the registry, the Theo -Conjecture system surfaced rank–locality candidates bounding*d*in terms of both check rank and maximum check weight. The first deterministic candidates were one-sided; the system’s counterexample workflow and Co-Pilot interpretation exposed the failure mode through Shor and the natural*X/Z-swapped*presentation. Thus no unrestricted theorem should privilege a single check
1
side. A symmetric maximum form and a balanced minimum refinement survived the current registry. We prove the symmetric maximum envelope for several families and regimes, report stress tests on curated and out-of-sample CSS presentations, and state the remaining conjectures as concrete targets for quantum-code theory.
The main contributions are as follows.
1. We give a traceable AI-assisted discovery narrative in which false conjectures are not discarded as failures, but used as structured information about missing CSS-code hypotheses; the workflow begins from a small seed registry and becomes more informative through a handful of targeted additions.
2. We prove elementary universal rank bounds for CSS distances and show how the twodimensional Bravyi–Poulin–Terhal tradeoff implies a rank-sensitive square-root bound when*Z-check*rank is linearly dense in block length.
3. We identify a geometric rank–distance problem whose exponent is sharp on toric codes and whose unrestricted form is refuted by BCH-type algebraic behavior.
4. We formulate presentation-level rank–locality envelopes, show that the unrestricted onesided and minimum forms are not*X/Z-stable*in general, prove the symmetric maximum form for rank-one-side codes, check-weight-three codes, the quantum Hamming family, toric codes, hypergraph products of repetition checks, cyclic-pair bicycle codes, dense-check regimes, and direct sums, and report stress tests that found no counterexample.
5. We record a second false but informative conjecture, the rankless self-CSS envelope, and explain how the*[[47, 1,*11]] quadratic-residue code shows that the rank term in the surviving envelope is structurally necessary.
The main limitation is equally important. The symmetric maximum rank–locality envelope is not claimed as a theorem in full generality, and its check-weight term depends on the specified check presentation. The paper also does not claim a new asymptotic qLDPC construction. Its contribution is a set of explicit, computable conjectures, counterexamples, and partial theorems
that sharpen how rank and locality enter finite CSS-code distance questions.
2 Introduction Binary CSS codes are among the central objects in quantum error correction [1, 2, 3]. They are specified by binary matrices
*HX*∈*FmX×n*2*, HZ*∈*FmZ×n*
2*,*
satisfying the commutation condition
*HXHT Z*=*0.*
Here*HX*records the supports of the*X-type*stabilizer generators and*HZ*records the supports of the*Z-type*stabilizer generators. All ranks, kernels, and row spaces are over F2. For a binary vector*v*∈*Fn*
2 ,*wt(v)*denotes its Hamming weight, i.e. the number of nonzero coordinates. We do not distinguish notationally between a binary vector and the support of the corresponding Pauli operator. The associated quantum code has
*k*=*n*−*rank(HX)*−*rank(HZ),*
and CSS distances
*dX*=*min{wt(v)*:*v*∈*ker(HZ)*\*row(HX)},*
*dZ*=*min{wt(v)*:*v*∈*ker(HX)*\*row(HZ)},*
with*d*=*min(dX , dZ)*when both distances are defined. Thus*dX*is the minimum weight of a nontrivial*X-type*logical operator: it must commute with all*Z-checks,*so its support lies in*ker(HZ),*and it is considered modulo*X-type*stabilizers*row(HX).*Similarly,*dZ*is the minimum weight of a nontrivial*Z-type*logical operator, computed as*ker(HX)*\*row(HZ).*Some authors index these distances by the error type and some by the checks that detect the error; throughout this paper we use the logical-operator convention above.
Several statements below are intentionally statements about CSS check presentations, not only about abstract stabilizer codes up to a change of generators. Ranks and row spaces are invariant under replacing a check matrix by another basis for the same row space, but maximum displayed check weight is not: adding a redundant high-weight check can only make the
2
Statement Status in this paper
Role in the discovery narrative
*d*≤ ⌊ 2 √
*rank(HZ)*⌋
Refuted First system-generated rank-only law; sharp on Steane, false on Golay.
*d*≤ ⌈ 2 √
*rank(HZ)*⌉
Refuted Natural Co-Pilot refinement; false on the length-127 BCH benchmark.
Geometric*d*=*O(*
√*rank(HZ))*
Open in intrinsic form
Toric codes show the exponent*1/2*is sharp; a rank-dense version follows from known twodimensional stabilizer tradeoffs.
*d*≤*⌊7wmax Z /8⌋*for self-CSS
presentations Refuted Sharp on Steane and Golay, but the
*[[47, 1,*11]] quadratic-residue code shows that check weight alone is insufficient.
Unrestricted minimum rank–locality envelope
Refuted Shor shows that the smaller side budget need not control the total CSS distance.
One-sided rank–locality candidate
Not*X/Z-stable*Machine-surfaced precursor; the*X/Z-*swapped Shor presentation refutes any unrestricted theorem privileging one side.
Symmetric maximum rank– locality envelope
Open in general Main finite-code conjecture; sharp on Steane, proved for several broad regimes and infinite families, and stress-tested without failures.
Table 1: Status of the principal statements. The table separates proved facts, refuted conjectures, and live targets, since the paper uses false conjectures as part of the discovery process rather than as final claims.
upper bounds below easier to satisfy. The registry therefore uses canonical or specified presentations for each object, and the rank–locality envelope is read in that presentation-level sense. A fully basis-invariant version would replace the displayed maximum row weight by an optimized width of the check space; we return to this as an open refinement after stating the envelope.
The search for useful quantum error-correcting codes is partly a search for the right structural invariants: which measurements certify distance, which forms of locality constrain it, and which algebraic mechanisms escape low-dimensional intuition. Automated conjecturing offers a complementary way to explore such questions. Instead of beginning with a proposed theorem, one begins with a finite, auditable table of objects and invariants, asks for compact laws that are true on that table, and then treats counterexamples as new information about the missing hypotheses.
We report such a discovery episode for CSS codes using Theo-Conjecture, an automated conjecturing environment with an integrated LLM Co-Pilot and verifier-backed counterexample tools. The system is not a machine-learning
oracle for theorem truth. It descends from Fa-jtlowicz’s Graffiti program [18], the Dalmatian heuristic [19], TxGraffiti [20], and Graffiti3 [21]. TxGraffiti is a successor in the Graffiti lineage whose graph-theoretic conjectures have led to nontrivial theorems, especially around domination, forcing, and related graph invariants [20]. Graffiti3 then makes explicit the broader theoryselection viewpoint: the output is not merely a list of isolated guesses, but a compact, nonredundant, snapshot-true theory of the current evidence table [21]. Theo-Conjecture imports that viewpoint into an interactive research environment: conjectures are generated from a finite snapshot table of explicit objects, numerical invariants, and Boolean predicates; counterexamples can be verified and added; and new definitions can become part of the evolving theory. A statement is therefore initially table true, not proved.
To our knowledge, this is the first direct application of the TxGraffiti/Graffiti3 snapshot-theory paradigm to quantum error correction. We are also not aware of a previous report in which an automated conjecturing system with integrated LLM assistance produced a traceable sequence of
3
quantum-information conjectures, certified counterexamples, new domain predicates, and partial mathematical results. What is new in this workflow is the tight coupling of that snapshot-theory engine to a Co-Pilot that assists with mathematical explanation, definition design, example proposal, and structured counterexample checks. The discovery path is also traceable: runs, selected conjectures, Co-Pilot interactions, verified counterexamples, new definitions, registry synchronizations, and reruns are recorded as part of the research environment. When a candidate object is supplied, the verifier computes the relevant invariants and checks the premise and conclusion directly; explicit counterexamples are therefore certified computationally even though positive conjectures still require mathematical proof.
A notable feature of the episode is that the strongest conjectures did not require a large initial training corpus or a hidden corpus of quantum-code data. The workflow began from a small seed registry of explicit CSS presentations. As false conjectures appeared, a handful of mathematically meaningful examples—Steane, Golay, BCH, Shor, toric, quadratic-residue, generalizedbicycle, and hypergraph-product presentations— were added as counterexamples, stress tests, or boundary cases. The point is not that small finite data certify a theorem. Rather, the small evolving table acted as a disciplined research instrument: each added example changed the finite theory, exposed a missing hypothesis, or forced a sharper invariant.
Other AI-for-science methods have used learned models to guide mathematical intuition [22], symbolic regression to rediscover physical laws [23], and automated search to design quantum optics experiments [24]. AI methods are also increasingly used across the quantum-computing stack [25]. The contribution here is different and deliberately concrete: a Graffiti3-style conjecturing workflow, augmented by an LLM Co-Pilot and run on a small evolving CSS-code registry, generated explicit quantum-error-correction conjectures, found and certified counterexamples, motivated new code invariants, and led to partial theorems about CSS rank, locality, and distance.
The first machine-generated pattern was the clean inequality
*d*≤ ⌊ 2 √
*rank(HZ)*⌋
under the nondegeneracy hypothesis*mX >*0 and*mZ >*0. It was attractive because it replaced block length by independent*Z-check*rank. The formula is false, but its failures were structured: Steane is sharp for the floor form, Go-lay forces a ceiling, and a length-127 BCH construction refutes the ceiling version in full generality. This sequence changed the mathematical question from “does rank alone control distance?” to “which geometric hypotheses make square-root rank–distance control valid?” The toric family then shows that the exponent*1/2*is the correct geometric scale.
The surviving difficult conjecture came only after those failures were added back to the registry. Once construction-class and locality features were included, the Theo-Conjecture workflow produced the rank–locality phenomenon. Its deterministic conjecture generator first surfaced one-sided candidates, for example inequalities of the form
*d(C)*≤*⌊rank(Hσ)*+*7wmax*
*σ*
8
⌋*.*
Taken literally, such a statement depends on which side is called*X*and which side is called*Z.*Since exchanging*HX*and*HZ*gives another valid CSS presentation with the same distance, an unrestricted general theorem should be stable under this exchange. The asymmetric Shor code exposes the issue: one side has enough budget and the other does not. This was not an external correction to the discovery process; it was part of the Theo-Conjecture process itself. Verifier-backed counterexample interaction supplied the Shor obstruction, and Co-Pilot summaries identified the asymmetry as the relevant missing symmetry. The system-level outcome is the surviving*X/Z-stable*general target: the symmetric maximum envelope. Sharper minimum envelopes then become meaningful only under balance hypotheses. The symmetric maximum envelope is this paper’s main open finite-code target. It is sharp on Steane, consistent with the algebraic examples that defeat rank-only bounds, and supported below by registry checks, out-of-sample stress tests, and theorems for several infinite families.
This positioning is important for quantum error correction. We do not claim a new asymptotic qLDPC construction, and we do not claim that square-root distance behavior is new: twodimensional local stabilizer codes already sat-
4
isfy Bravyi–Poulin–Terhal type tradeoffs [4], with related surface- and color-code refinements [5], while high-dimensional and algebraic qLDPC constructions show that
√*n*intuition is not uni-
versal [7, 8, 9, 10, 11]. The new, system-generated question is rank-sensitive. It asks when independent syndrome rank, and in the finite-code envelope also check locality, constrain distance more sharply than the universal linear-algebra bounds. Equally important for this paper, the question was produced by an automated conjecturing system with built-in LLM assistance, counterexample verification, user-extensible definitions, and a replayable run history, rather than by a post-hoc search for examples fitting a predetermined theorem.
3 Results 3.1 A false rank-only law and the geometric question it exposes The first result is a counterexample-guided rank– distance phenomenon. In the initial quantumcode registry, each object was an explicit pair*HX , HZ*, and the feature table recorded exact small-code quantities such as ranks, logical distances, check counts, Tanner-graph features, and qubit-interaction features. Early counterexamples were dominated by degenerate presentations with an empty*X-*or*Z-check*side, so the predicate has_both_check_types was added as a genuine mathematical nondegeneracy condition rather than a cosmetic filter.
With that predicate in place, Theo -Conjecture generated the following rank– distance statement. On the small base registry, it was the first CSS conjecture whose failure was not immediately exposed by Co-Pilot counterexample search.
**Conjecture 1**(Initial system-generated floor**version).***Let C be a binary CSS code with mX >*0*and mZ > 0. Then*
*d*≤ ⌊ 2 √
*rank(HZ)*⌋
*.*
This resistance was informative but not decisive. Subsequent Co-Pilot-assisted and humanguided searches showed that the conjecture is false in a structured way. The first two named examples reveal a precise floor/ceiling phenomenon.
For the*[[7, 1,*3]] Steane code, take
*HX*=*HZ*=
1 1 1 1 0 0 0 1 1 0 0 1 1 0 1 0 1 0 1 0 1
*.*
Then*rank(HZ)*=*3, d*=*3,*
and ⌊ 2 √
3 ⌋
= 3 while ⌈ 2 √
3 ⌉
=*4.*
Thus Steane is sharp for the generated floor form. The next natural perfect-code successor is the
quantum Golay code [15]. Let*HX*=*HZ*=*H,*where*H*is the following 11 × 23 cyclic paritycheck matrix:
10100100111110000000000 01010010011111000000000 00101001001111100000000 00010100100111110000000 00001010010011111000000 00000101001001111100000 00000010100100111110000 00000001010010011111000 00000000101001001111100 00000000010100100111110*00000000001010010011111.*
This gives the*[[23, 1,*7]] quantum Golay code, and exact verification gives
*rank(HZ)*=*11, dX*=*dZ*=*d*=*7.*
Therefore⌊ 2 √
11 ⌋
= 6 and ⌈ 2 √
11 ⌉
=*7.*
Golay is a decisive counterexample to the floor conjecture, but it is also a sharp witness for the corresponding ceiling statement. In this sense the counterexample did not erase the pattern; it sharpened it. Co-Pilot’s subsequent mathematical summaries emphasized this distinction and suggested the ceiling version as the next candidate.
**Conjecture 2**(Ceiling**version).***Let C be a binary CSS code with mX >*0*and mZ > 0. Then*
*d*≤ ⌈ 2 √
*rank(HZ)*⌉
*.*
5
The ceiling version survived the original small registry and the Golay repair, but it is also false in full generality. The obstruction comes from a standard BCH direction rather than a surface-like one [13, 14]. Consider the primitive narrow-sense binary BCH code of length
*n*= 127 = 27 − 1
with designed distance*δ*= 15. The 2-cyclotomic cosets modulo 127 with leaders
*1, 3, 5, 7, 9, 11,*13
all have size 7. Hence the generator polynomial has degree 49, and the parity-check rank is 49. This BCH code is dual-containing at this designed distance, so the CSS construction with
*HX*=*HZ*=*H*
is valid. It has
*rank(HZ)*=*49, k*= 127 − 2 · 49 =*29,*
and quantum distance at least the BCH designed distance:
*d*≥*15.*
But ⌈ 2 √
*rank(HZ)*⌉
= ⌈ 2 √
49 ⌉
=*14.*
Thus*d*≥ 15*> 14,*
so the ceiling conjecture is false for general CSS codes. Adding this BCH obstruction back to the registry was a turning point: later Theo -Conjecture runs stopped treating*Z-check*rank alone as the whole story and began surfacing hypotheses involving construction class and locality.
**Proposition 1.***There exists a binary CSS code with both check types and d >*
⌈ 2 √
*rank(HZ)*⌉*.*
*Proof.*The length-127, designed-distance-15, primitive narrow-sense binary BCH construction above gives a dual-containing classical code with check rank 49. The self-CSS construction*HX*=*HZ*=*H*therefore commutes and has*k*= 127 − 98 = 29. The BCH designed-distance bound gives*d*≥ 15, whereas
⌈ 2 √
49 ⌉
= 14. This proves the claim.
The figure below also includes the next BCH benchmark used in the stress tests. For length 511 = 29 − 1 and designed distance 31, the relevant 2-cyclotomic coset leaders are the odd integers
*1, 3, 5, . . . , 29,*
and each coset has size 9. Thus the check rank is 15 · 9 = 135. The standard dual-containment criterion for primitive narrow-sense binary BCH codes again gives a valid self-CSS construction*HX*=*HZ*=*H,*now with
*k*= 511 − 2 · 135 = 241 and*d*≥*31.*
Since ⌈ 2 √
135 ⌉
=*24,*
this larger benchmark is far above the ceiling line even when plotted only at its designed-distance lower bound. It is not needed to refute the conjecture, but it shows that the BCH obstruction is a family-level algebraic phenomenon rather than a single exceptional code.
The resulting interpretation is not that rank– distance control is illusory. Rather, the examples separate two regimes. Algebraic BCH-type constructions can have distance too large for a rankonly square-root bound, while surface-like constructions naturally exhibit square-root behavior. The toric family makes this interpretation precise at the exponent level.
Let*CL*be the*L×L*toric code on the square lattice with periodic boundary conditions [6]. There are*n*=*2L2*physical qubits,*L2*vertex checks, and*L2*plaquette checks. Taking*HZ*to be the plaquette-check matrix, the only linear dependency among the*Z-checks*is the product of all plaquettes. Hence
*rank(HZ)*=*L2*−*1.*
The toric code has distance*d*=*L,*so
*d*=*L*= ⌈√
*L2*− 1 ⌉
= ⌈√
*rank(HZ)*⌉
*.*
**Proposition 2.***For the L×L toric-code family,*
*d*= ⌈√
*rank(HZ)*⌉
*.*
*In particular, any general geometric rank– distance theorem of the form*
*d*≤*A rank(HZ)α*
*valid for all L×L toric codes must have α*≥*1/2, unless the constant A is allowed to grow with L.*
6
*Proof.*The rank and distance computations above give*d*=*L*and*rank(HZ)*=*L2*− 1. Since
√*L2*− 1*< L*and
√*L2*− 1*> L*− 1 for
*L*≥ 2, we have ⌈√
*L2*− 1 ⌉
=*L*=*d.*If*d*≤*A rank(HZ)α*held with fixed*A*and*α < 1/2,*then*L*≤*A(L2*−*1)α*=*O(L2α),*impossible as*L*→ ∞.
Thus the first Theo-Conjecture episode produced more than a false inequality. It produced a sequence of increasingly informative witnesses: Steane explains the floor, Golay forces the ceiling, BCH refutes rank-only control, and toric codes identify the geometric exponent. The resulting object is no longer an isolated formula but a candidate geometric rank–distance principle.
3.2 Universal rank baselines Although the square-root inequality is false in general, CSS linear algebra still gives nontrivial universal rank bounds. These bounds are weaker than the geometric square-root principle, but they explain why rank is a natural feature for automated conjecturing and why the failed conjecture was mathematically close to a real resource constraint.
**Proposition 3**(One-sided CSS rank**bounds).***Let C be a CSS code with k > 0. Put*
*rX*=*rank(HX), rZ*=*rank(HZ).*
*Then*
*dX*≤*rZ*+*1, dZ*≤*rX*+*1,*
*and hence*
*d*≤*min{rX*+*1, rZ*+*1}.*
*Proof.*We prove the*dX*inequality; the*dZ*inequality follows by symmetry. Put*K*=*ker(HZ).*After choosing pivot columns for*HZ*, the kernel*K*has a generating set whose vectors have weight at most*rZ*+ 1: each free coordinate determines a kernel vector supported on that free coordinate and at most the*rZ*pivot coordinates. Since
*k*= dim*K*−*rank(HX) > 0,*
the row space*row(HX)*is a proper subspace of*K.*If all such kernel generators belonged to*row(HX),*then all of*K*would belong to*row(HX),*contradicting*k >*0. Hence one generator lies in*K*\*row(HX),*and it has weight at most*rZ*+ 1. Thus*dX*≤*rZ*+ 1.
**Corollary 1**(Small-rank cases of the ceiling**bound).***Let C be a CSS code with k >*0*and rZ*=*rank(HZ). If rZ*∈*{1, 2, 3}, then*
*d*≤ ⌈2 √
*rZ⌉ .*
*Similarly, if rX*∈*{1, 2, 3}, then d*≤ ⌈ 2√
*rX*
⌉*.*
*Proof.*For*r*∈*{1, 2,*3}, one has*r*+ 1 ≤ ⌈2 √
*r⌉.*Apply the one-sided rank bound.
**Proposition 4**(Quantum Singleton bound in rank**form).***Every CSS stabilizer code satisfies*
*d*≤ ⌊
*rX*+*rZ*
2
⌋ +*1.*
*Proof.*The quantum Singleton bound for an*[[n, k, d]]*code gives
*n*−*k*≥*2(d*−*1).*
For a CSS code,
*n*−*k*=*rank(HX)*+*rank(HZ)*=*rX*+*rZ .*
Therefore*d*≤*rX*+*rZ*
2 +*1.*
Since*d*is an integer, this is equivalent to the stated bound.
Together, these universal inequalities show that check rank always gives at least linear control of distance. The discovery arc above asks whether, after adding the right geometric hypotheses, this baseline can be strengthened to square-root control.
3.3 Toward a rank-sensitive geometric theorem
The BCH counterexample shows that rank alone cannot control CSS distance. For a QEC reader, this is exactly what one should expect: modern algebraic and high-dimensional qLDPC constructions are designed to escape two-dimensional area-boundary intuition. Conversely, the squareroot exponent itself is not new. Bravyi, Poulin, and Terhal proved that two-dimensional geometrically local stabilizer codes obey a tradeoff of the form
*kd2*=*O(n),*
with constants depending on locality data [4]; related surface-code and color-code refinements
7
are also known [5]. Thus, for*k*≥ 1, any genuinely two-dimensional local family already satisfies*d*=*O(*
√*n).*
The generated pattern is therefore interesting only if it does something more specific than rediscover
√*n.*The proposed refinement is to replace
the ambient block length by a syndrome-rank resource. A bound
*d*≤*A*√
*rank(HZ)*
is equivalent to the resource lower bound
*rank(HZ)*≥*A−2d2.*
This distinction matters when stabilizer presentations contain redundant checks:*n*counts qubits, while*rank(HZ)*counts independent*Z-type*syndrome constraints. If a two-dimensional rank– distance theorem held under intrinsic hypotheses, then a family with*d*≫
√*rank(HZ)*would be cer-
tified as using something other than ordinary twodimensional rank geometry: high-dimensional expansion, algebraic structure, dense checks, or another non-surface-like mechanism.
This gives the QEC content of the section. The theorem below is not offered as a new substitute for the Bravyi–Poulin–Terhal tradeoff; it is a short consistency check showing that the proposed rank form follows immediately when*Z-*check rank is linearly dense in*n.*The genuinely open question is whether one can replace this density assumption by natural, computable geometric predicates and then determine sharp constants or floor/ceiling refinements.
**Conjecture 3**(Geometric rank–distance princi-**ple).***For a bounded-degree CSS code whose Tan-ner presentation is geometrically local on a twodimensional surface and for which rank(HZ) is comparable to n, there is a constant A, depending only on the geometric locality data, such that*
*d*≤*A*√
*rank(HZ).*
**Conjecture 4**(Asymptotic geometric rank–distance**principle).***Let {Ci}i≥1 be a family of bounded-degree CSS codes with geometrically local Tanner presentations on two-dimensional surfaces of uniformly bounded local geometry. Let*
*rZ(Ci)*=*rank(HZ(Ci)).*
*If rZ(Ci)*=*Ω(ni), then*
*d(Ci)*=*O*
(√*rZ(Ci)*
)*.*
*Equivalently,*
*rZ(Ci)*=*Ω(d(Ci)2).*
The asymptotic form is the resource statement behind the geometric rank–distance principle. It says that, in a fixed two-dimensional geometric regime, independent*Z-check*rank must grow quadratically with distance. In particular, a family with*d(Ci)*≫
√*rZ(Ci)*must eventually leave
the two-dimensional geometric regime or violate the rank-density hypothesis*rZ*=*Ω(n).*
**Proposition 5**(Rank-dense consequence of the two-dimensional stabilizer**tradeoff).***Assume the Bravyi–Poulin–Terhal two-dimensional locality tradeoff: for a family of geometrically local two-dimensional stabilizer codes with uniformly bounded locality data, there is a constant B such that*
*kid*2*i*≤*Bni*
*for all i. Let {Ci} be a CSS subfamily with ki*≥ 1*and*
*ni*≤ Γ*rank(HZ(Ci))*
*for a fixed constant Γ. Then*
*di*≤ √
*BΓ*√
*rank(HZ(Ci)).*
*Proof.*Since*ki*≥ 1, the tradeoff*kid*2*i*≤*Bni*
implies*d2 i*≤*Bni.*The rank-density hypothesis
gives*ni*≤ Γ*rank(HZ(Ci)),*and hence
*d2 i*≤*BΓ rank(HZ(Ci)).*
Taking square roots gives the claimed rank– distance bound.
This proposition deliberately lowers the temperature of the claim: the rank-dense asymptotic form is already contained in known QEC tradeoffs. What Theo-Conjecture contributed was the route to the question and the specific finite formulation: Steane, Golay, BCH, and toric codes forced the distinction between exact floor/ceiling laws, rank-only failure, and geometric exponent sharpness. The open problem is to identify intrinsic, registry-computable hypotheses under which the rank-dense consequence can be strengthened to small constants or to an exact integral law.
8
0 2 4 6 8 10 12*rZ*=*rank(HZ)*
0
5
10
15
20
25
30 C
SS  d
is ta
nc e
*d*algebraic escape
2D geometric  scale
Rank-distance geometry for CSS code instances
*d*2*rZ*region*d*=*rZ*
*d*= 2*rZ*
classical CSS surface/toric hypergraph product bicycle CSS*toric family: d*=*rZ*
Steane
Golay
BCH(127,15)
BCH(511,31)
Figure 1: Rank–distance geometry for the quantum-code registry and benchmark families. The horizontal axis is√*rZ*=
√*rank(HZ),*and the vertical axis is the CSS distance*d.*The shaded region is the experimental*d*≤ 2√
*rZ*
region. Registry instances and the toric family exhibit the expected geometric square-root behavior, with toric codes showing the sharp exponent*d*=
⌈√*rZ*
⌉ . The quantum Golay code is sharp for the ceiling*A*= 2 line, while the
BCH benchmarks escape above that line, illustrating why rank alone cannot imply the conjecture without geometric hypotheses.
The experimental constant*A*= 2 is especially appealing because the quantum Golay code is ceiling-sharp for it and the discovered floor version is sharp on Steane. This suggests a finer finite-code question: within a natural geometric subuniverse, the best integral bound may not be uniformly a floor or uniformly a ceiling, but may depend on an additional structural feature of the presentation. At present we do not know whether this feature is topological, parity-like, related to check dependencies, or an artifact of the small registry. For this reason we state the main conjecture in the robust*A*
√*rank(HZ)*form and
leave the floor/ceiling choice as a sharper experimental problem. The toric family shows that the exponent*1/2*is best possible in the geometric setting. The BCH counterexample indicates that any theorem with a universal constant must include hypotheses which exclude algebraic highdistance BCH behavior.
**Question 1.***For which natural finite classes of*
*CSS presentations does*
*d*≤ ⌈ 2 √
*rank(HZ)*⌉
*hold? Does it hold for planar Tanner graphs, bounded-genus Tanner graphs, surface-code chain complexes, or other explicit low-dimensional CSS geometries?*
**Question 2**(Floor/ceiling**refinement).***Is there a natural CSS-geometric predicate P(C) such that, on a meaningful geometric class,*
*d*≤ ⌊ 2 √
*rank(HZ)*⌋
*when P(C) holds, while the complementary cases require only the ceiling*
*d*≤ ⌈ 2 √
*rank(HZ)*⌉ ?
*Equivalently, can the one-unit gap between the Steane-type floor-sharp behavior and the Golay-type ceiling-sharp behavior be explained by an intrinsic property of the CSS presentation?*
9
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX_ErFY6z2FBMtBfCt9pizrNtiw7FtrrWUc5AEWTrX5YY6omCbeI8nk8FY1GjzBD5U02OpYkHPRkM1PCtp-_Cev53CdIjN4pZFZKQYmqRz3YN28yyx7XPeGG058OpUx2SAAw1m1Mzw=w626-h420-v0?authuser=0)

3.4 Rank–locality envelopes
The BCH counterexample shows that rank alone is too coarse. A natural next feature is check weight. This feature is presentation-level: for a specified CSS check presentation
*P*=*(HX , HZ)*
of a code*C,*define, for*σ*∈*{X, Z},*
*rσ*=*rank(Hσ), wmax*
*σ*=*max{wt(h)*:*h*is a row of*Hσ},*
and define
*Bσ(C)*= ⌊
*rσ*+*7wmax σ*
8
⌋*,*
*Bmin(C)*=*min{BX(C), BZ(C)},*
*Bmax(C)*=*max{BX(C), BZ(C)},*
*B(C)*=*Bmax(C).*
Here*d(C)*is an invariant of the represented CSS code, while*B(C)*is shorthand for the budget of the chosen presentation*P*. This distinction is important: the conjecture below is designed to be tested on the canonical presentations recorded in the registry and on named check presentations used in QEC. A basis-invariant strengthening would replace*wmax*
*σ*by
*ωσ(C)*= min*Bσ*
max*h∈Bσ*
*wt(h),*
where*Bσ*ranges over bases for*row(Hσ).*We do not claim that optimized version here; it is a natural next target once the presentation-level envelope is understood. The quantities*BX*and*BZ*
combine two pieces of information that pure rank cannot see: the number of independent checks on a side and the largest locality scale of a check on that same side. The two natural symmetric envelopes are the stronger minimum budget*Bmin,*which asks both sides to be large enough, and the symmetric maximum budget*Bmax,*which asks that at least one side has enough rank-locality budget to explain the total distance. In bounded-check-weight families, even the maximum version is much stronger than the universal linear rank bound*d*≤*rσ*+ 1; in dense-check presentations, the check-weight term allows algebraic examples such as Golay and BCH codes to coexist with the observed envelope.
**Conjecture 5**(Symmetric maximum rank–locality**envelope).***Let P*=*(HX , HZ) be a specified binary CSS check presentation of a code C with k > 0, mX > 0, and mZ > 0. Then*
*d(C)*≤ max*σ∈{X,Z}*
*⌊rank(Hσ)*+*7wmax σ*
8
⌋*.*
The maximum in Conjecture 5 is not cosmetic. In the Theo-Conjecture workflow, the first rank–locality candidates were one-sided. The counterexample interaction then exposed Shor as the obstruction to controlling distance by the smaller side budget. The natural symmetric strengthening uses*Bmin,*but the Shor code refutes it:
*(rX , rZ , wmax X , wmax*
*Z , d)*=*(2, 6, 6, 2, 3),*
so*BX*= 5,*BZ*= 2, and*d*= 3*> Bmin*= 2. Equivalently, after exchanging*X*and*Z,*the same example refutes the corresponding one-sided theorem for the displayed*X-side*budget. The failure is caused by asymmetric check presentations: the smaller side budget need not control the total CSS distance. This is why the system-level discovery is recorded as the symmetric maximum envelope rather than as a one-sided law. In the current synced registry, Conjecture 5 holds for all 46 objects with both check types and known distance, interpreted with their recorded check presentations, including the Shor counterexample to the minimum form. We also stresstested the symmetric maximum form on 2560 benchmark and out-of-sample CSS presentations, including toric, Golay, BCH, generalized bicycle, hypergraph-product, Hamming, and random exact-distance examples, and then on 4500 additional sparse exact-distance random CSS presentations with 6 ≤*n*≤ 20. In these tests there were no failures of the symmetric maximum bound.
The stronger minimum form remains interesting under balance hypotheses. In the current registry it has no failures among objects with equal*X/Z*row spaces, equal*X/Z*ranks, equal maximum*X/Z*check weights, or both equal ranks and equal maximum check weights. This motivates the following sharper target.
**Conjecture 6**(Balanced minimum rank–locality**envelope).***Let P*=*(HX , HZ) be a specified binary CSS check presentation of a code C with k > 0, mX > 0, and mZ > 0. Suppose that*
*rX*=*rZ and wmax X*=*wmax*
*Z .*
10
*Then d(C)*≤*Bmin(C).*
Other balance hypotheses may be sufficient, but the equal-rank/equal-maximum-weight form is the clean version tested in the current registry.
A still cleaner specialization appears when the*X-*and*Z-check*row spaces agree. This is the self-CSS situation: if
*row(HX)*=*row(HZ)*=*S,*
then the two CSS distances are equal and
*dX*=*dZ*=*min{wt(v)*:*v*∈*S⊥*\*S}.*
In this setting early registry data suggested that the rank term in the symmetric envelope might be unnecessary. The following machine-surfaced candidate is presentation-sensitive:*wmax*
*Z*refers to the maximum row weight in the chosen*Z-*check matrix. A basis-invariant variant would replace it by an optimized width parameter of the subspace*S.*
Machine-surfaced rankless candidate. Let*C*be a binary CSS code with*k >*0 and
*row(HX)*=*row(HZ).*Then
*d(C)*≤*⌊7wmax*
*Z*
8
⌋*.*
This candidate is attractive because it is sharp for both the Steane code and the quantum Golay code:
Steane:*(wmax Z , d)*=*(4, 3),*
Golay:*(wmax Z , d)*=*(8, 7).*
Thus it isolates the same two sharp witnesses that motivated the floor/ceiling square-root story, but now through check-locality rather than rank. A later Co-Pilot-guided stress test, however, found that the rankless form fails on a larger self-CSS algebraic code.
**Proposition 6**(Quadratic-residue counterexample to the rankless**envelope).***The refuted self-CSS rankless envelope is false. There is a binary self-CSS code with*
*row(HX)*=*row(HZ), wmax*
*Z*=*12, d*=*11.*
*In particular,*
11 =*d >*
⌊7 · 12 8
⌋ =*10.*
*Proof.*Take*S*to be the even-like binary quadratic-residue code of length 47. This is a self-orthogonal*[47,*23] cyclic code whose odd-like supercode has parameters*[47, 24,*11] [16, 17]. The CSS presentation
*HX*=*HZ*=*H,*
where the rows of*H*generate*S,*therefore defines a self-CSS code with
*k*= 47 − 2*dim(S)*= 1
and distance*d*= 11. A cyclic generator for*S*has weight 12; taking its 23 cyclic shifts gives a rank-23 check matrix*H*with*wmax*
*Z*= 12. Hence the proposed rankless bound gives 10, while the actual CSS distance is 11. This proves the counterexample.
The counterexample is mathematically useful. It explains why the rank term in Conjecture 5 is not just a cosmetic artifact: once larger algebraic self-CSS codes enter the registry, check weight alone no longer controls distance.
**Proposition 7**(Steane is sharp for the enve-**lope).***The [[7, 1,*3]]*Steane code satisfies*
*d*=*B(C)*=*3.*
*Proof.*For the Steane presentation above,*HX*=*HZ*,*rX*=*rZ*= 3, and*wmax*
*X*=*wmax Z*= 4. Hence
*BX(C)*=*BZ(C)*= ⌊3 + 7 · 4
8
⌋ =
⌊31 8
⌋ =*3.*
Since*d*= 3, the envelope is attained with equality.
**Proposition 8**(Steane and Golay are sharp for the rankless self-CSS**envelope).***The Steane code and the quantum Golay code both satisfy*
*d*=*⌊7wmax*
*Z*
8
⌋*.*
*Proof.*For Steane,*wmax Z*= 4 and*d*= 3,*so⌊7wmax*
*Z*
8
⌋ =
⌊28 8
⌋ = 3 =*d.*
For the quantum Golay presentation above,*wmax*
*Z*= 8 and*d*= 7,*so⌊7wmax Z*
8
⌋ =
⌊56 8
⌋ = 7 =*d.*
11
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0*B(C)*= max
*{X, Z} (r*+*7wmax)/8*
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0
C SS
d is
ta nc
e*d*
2 large-slack points off scale
Envelope test, sharp-example zoom
Steane Shor (min form fails)
Golay
tight bicycle
conjectured region counterexample region*d*=*B(C)*geometric/topological hypergraph product algebraic/cyclic other registry CSS
101 102
*rank-locality budget B(C)*
0.0
0.2
0.4
0.6
0.8
1.0
ut ili
za tio
n*d/*
*B( C)*
All registry instances
Golay
Figure 2: Evidence for the symmetric maximum rank–locality envelope. The left panel plots the CSS distance*d*against*B(C)*=*maxσ∈{X,Z} ⌊(rσ*+*7wmax*
*σ )/8⌋*for the sharp-example range of the quantum-code registry. Points above the diagonal would be counterexamples to Conjecture 5. Steane is sharp, Shor illustrates why the maximum rather than the minimum is needed in asymmetric presentations, and Golay lies below the diagonal. The right panel shows the utilization ratio*d/B(C)*for all registry instances, including large-slack algebraic and hypergraph-product examples.
**Proposition 9**(Closure under direct**sums).***Let C*=*C1*⊕ · · · ⊕*Ct be a block-diagonal CSS direct sum of codes with positive distance. If Conjec-ture 5 holds for each Ci, then it holds for C.*
*Proof.*For a block-diagonal direct sum, the CSS distance is
*d(C)*= min*i*
*d(Ci).*
Moreover, for each*σ*∈*{X, Z},*
*rσ(C)*= ∑
*i*
*rσ(Ci),*
*wmax σ (C)*= max
*i wmax*
*σ (Ci).*
Therefore*Bσ(C)*≥*Bσ(Ci)*for every*i,*and hence*B(C)*≥*B(Ci)*for every*i.*Choose*j*with*d(C)*=*d(Cj).*Since the conjecture holds for*Cj*,
*d(C)*=*d(Cj)*≤*B(Cj)*≤*B(C).*
**Proposition 10**(A dense-check regime where the envelope follows from**rank).***Let C be a CSS code with k > 0. If*
*wmax X*≥*rX*+ 2*and wmax*
*Z*≥*rZ*+*2,*
*then Conjecture 5 holds.*
*Proof.*By the one-sided rank bound,*d*≤*rX*+ 1 and*d*≤*rZ*+ 1. If*wmax*
*σ*≥*rσ*+ 2, then
*rσ*+*7wmax σ*≥*rσ*+*7(rσ*+ 2) =*8rσ*+*14,*
so*Bσ(C)*=
⌊*rσ*+*7wmax*
*σ*
8
⌋ ≥*rσ*+*1.*
Thus*d*≤*BX(C)*and*d*≤*BZ(C),*and hence*d*≤*min{BX(C), BZ(C)}.*
**Proposition 11**(One independent check on one**side).***If C is a binary CSS code with k > 0, mX , mZ > 0, and*
*min{rX , rZ}*=*1,*
*then Conjecture 5 holds.*
*Proof.*By symmetry, suppose*rZ*= 1, and let*row(HZ)*=*⟨z⟩*with support*S.*If*dX*≥ 3, then every vector of weight one or two in*ker(HZ)*must lie in*row(HX).*The weight-one vectors outside*S,*together with the weight-two vectors*ei+ej*for*i, j*∈*S,*span*ker(HZ).*Since CSS commutation gives*row(HX)*⊆*ker(HZ),*this would force
*row(HX)*=*ker(HZ), rX*=*n*−*1,*
and hence*k*=*n*−*rX*−*rZ*= 0, a contradiction. Therefore*d*≤*dX*≤ 2.
12
![image](https://lh3.googleusercontent.com/notebooklm/AKYWMX94gWJygu6v8z4Bj8ROjUzzCIr-eUYu2E8JRF5Q8EaqvM2D5hlddz9Z-O9lJbAAyHlFVkxgX3BEJJoN4HB04UIO8FaxttQg_7vgP0aSpw209Pe2bUVpaiSPp294BgBfTOfCJTae2g=w679-h306-v0?authuser=0)

If*d*= 1, the conjecture is immediate because*B(C)*≥ 1. It remains to exclude*d*= 2 and*B(C)*= 1. If*B(C)*= 1, then both sides have*rσ*+*7wmax*
*σ*≤ 15. Since*rZ*= 1, this gives*|S|*=*wmax*
*Z*≤ 2. On the*X-side,*the same inequality implies the following dichotomy: either*wmax*
*X*= 1, so the row space is generated by weight-one checks, or*wmax*
*X*= 2, in which case*rX*≤ 1. Thus, under*B(C)*= 1, any*X-row*space containing a weight-two vector has rank at most one.
If*|S|*= 1, say*S*=*{a},*then CSS commutation forbids every*X-check*from touching*a.*To avoid a weight-one*X-logical*operator on a coordinate outside*S,*each*ei*with*i*̸=*a*must lie in*row(HX).*Hence*rX*≥*n*− 1, so*k*=*n*−*rX*−*rZ*≤ 0, a contradiction.
If*|S|*= 2, say*S*=*{a, b},*then every*X-check*intersects*S*in either zero or two positions. To avoid weight-one*Z-logical*operators on*a*and on*b,*some*X-check*must touch*S.*Since*wmax*
*X*≤ 2, such a check is exactly*ea*+*eb,*so*row(HX)*contains a weight-two vector supported on*S.*To avoid a weight-one*X-logical*operator outside*S,*each coordinate outside*S*must also contribute its unit vector to*row(HX).*Thus either*n*= 2, in which case*rX*=*rZ*= 1 and*k*= 0, or*rX*≥ 2, contradicting*BX(C)*= 1 with*wmax*
*X*≤ 2. Therefore*d*= 2 forces*B(C)*≥ 2, and the proposition follows.
**Proposition 12**(Check-weight-three**regime).***Let C be a CSS code with k > 0, mX , mZ > 0, and*
*wmax X*≤*3, wmax*
*Z*≤*3.*
*Then Conjecture 5 holds.*
*Proof.*Wang, Liu, Li, Kubica, and Gu prove that any stabilizer code generated by checks of weight at most three and encoding at least one logical qubit has distance at most two [12]. Thus*d(C)*≤ 2. If*d*= 1, the claim is immediate. It remains to show that*B(C)*≥ 2 when*d*= 2. Sup-pose, for contradiction, that*d*= 2 and*B(C)*= 1. Then*BX(C)*=*BZ(C)*= 1. If either side has rank one, Proposition 11 already gives*d*≤*B(C),*contradicting*d*= 2*> B(C)*= 1. Hence both sides have rank at least two. But*Bσ(C)*= 1 and*rσ*≥ 2 force*wmax*
*σ*= 1 for each side, since*rσ*+*7wmax*
*σ*≤ 15. The code is then a direct sum of fixed one-qubit stabilizer constraints and free qubits, so*k >*0 implies a weight-one logical op-
erator. This contradicts*d*= 2. Hence*B(C)*≥ 2 whenever*d*= 2, and the envelope follows.
**Proposition 13**(The toric family satisfies the symmetric**envelope).***For the L*×*L toric code with L*≥*2,*
*d*≤*B(C).*
*Proof.*For the standard square-lattice toric presentation,
*rX*=*rZ*=*L2*−*1,*
*wmax X*=*wmax*
*Z*=*4, d*=*L.*
Therefore
*B(C)*= ⌊
*L2*− 1 + 28 8
⌋ =
⌊*L2*+ 27
8
⌋*.*
Since*L2*−*8L*+ 27 =*(L*− 4)2 + 11*>*0, we have*L*≤*(L2*+*27)/8.*As*L*is an integer,
*L*≤ ⌊
*L2*+ 27 8
⌋ =*B(C).*
**Proposition 14**(Quantum Hamming**family).***For every m*≥*3, the self-CSS quantum Ham-ming code obtained from the m*×*(2m*− 1)*binary Hamming parity-check matrix satisfies Con-jecture 5. It is sharp when m*=*3, i.e. for the Steane code.*
*Proof.*Let*Hm*be the binary matrix whose columns are the nonzero vectors of*Fm*
2 . For*m*≥ 3, each row has weight*2m−1,*and any two distinct rows overlap in*2m−2*positions, so
*HmHT m*= 0 over*F2.*
Thus*HX*=*HZ*=*Hm*defines a self-CSS code. The matrix*Hm*has rank*m,*and the classical Hamming code*ker(Hm)*has minimum distance 3. Since every nonzero word in*row(Hm)*has weight*2m−1 >*3, the CSS distance is*d*= 3. On the other hand,
*B(C)*= ⌊
*m*+ 7 ·*2m−1*
8
⌋ ≥ 3
for all*m*≥ 3, with equality at*m*= 3. Hence the conjecture holds for the entire family, and the*m*= 3 member is sharp.
13
**Theorem 1**(Two infinite registry families satisfy the rank–locality**envelope).***Conjecture 5 holds for the following infinite families.*
*(i) Hypergraph products of two classical repetition-check matrices.*
*(ii) The cyclic-pair bicycle family with HX equal to disjoint adjacent-pair checks and HZ*
*equal to the all-one check.*
*Proof.*Let*Pm*be the*(m*− 1) ×*m*repetition parity-check matrix with rows*ei*+*ei+1.*Con-sider the hypergraph product of*Pm*and*Pn,*with*m, n*≥ 2. In the standard block form,
*HX*= [*Pm*⊗*In*|*Im−1*⊗*P T*
*n*
]*,*
*HZ*= [*Im*⊗*Pn*|*P T*
*m*⊗*In−1*]*.*
The first block of qubits may be indexed by*[m]× [n].*The vector supported on a fixed column
*{(1, j), (2, j), . . . , (m, j)}*⊆*[m]*×*[n]*
has weight*m,*commutes with every*X-check,*and is not in the row space of*HZ*: every vector in the first-block projection of*row(HZ)*has even parity in each horizontal row, while this column vector has odd parity in each such row. Hence*d*≤*m.*Similarly, the vector supported on a fixed row of*[m]*×*[n]*has weight*n,*commutes with every*Z-*check, and is not in the row space of*HX*. Thus
*d*≤*min{m, n}.*
Moreover,
*rX*=*(m*−*1)n, rZ*=*m(n*−*1),*
and every check has weight at most 4, while for*m, n*≥ 2 both sides have maximum check weight at least 3. Therefore
*BX(C)*≥*⌊(m*−*1)n*+ 21
8
⌋*,*
*BZ(C)*≥ ⌊
*m(n*− 1) + 21 8
⌋*.*
Put*s*=*min{m, n}.*If*s*=*m*≤*n,*then
*(m*−*1)n*+ 21 ≥*(m*−*1)m*+ 21 ≥*8m*=*8s,*
because*m2*−*9m*+ 21*>*0. If*s*=*n < m,*then*m*− 1 ≥*n,*so
*(m*−*1)n*+ 21 ≥*n2*+ 21 ≥*8n*=*8s.*
Thus*BX(C)*≥*s.*The proof that*BZ(C)*≥*s*is the same with*m*and*n*interchanged. Hence
*d*≤*s*≤*Bmin(C)*≤*B(C),*
which proves the hypergraph-product repetition case.
Now consider the cyclic-pair family of length*2t, t*≥ 2. The*X-checks*are the*t*disjoint pairs
*e1*+*e2, e3*+*e4, . . . , e2t−1*+*e2t,*
and the single*Z-check*is the all-one vector. The code has a weight-two*X-type*logical operator: take one qubit from each of two distinct pairs. This vector has even overlap with the all-one*Z-*check and is not a sum of pair checks. Therefore*d*≤ 2. On the other hand,
*rX*=*t, wmax X*=*2,*
*rZ*=*1, wmax Z*=*2t,*
so*BX(C)*=
⌊*t*+ 14
8
⌋ ≥*2,*
*BZ(C)*= ⌊1 +*14t*
8
⌋ ≥ 2
for every*t*≥ 2. Hence*d*≤ 2 ≤*Bmin(C)*≤*B(C).*
These propositions and the theorem above give more than isolated evidence. They show that the conjecture is sharp in a nontrivial named code; stable under direct sums; automatic in a densecheck regime; true for rank-one-side and check-weight-three presentations; compatible with the main geometric family; and provable for the quantum Hamming family, hypergraph products of repetition checks, and cyclic-pair bicycle codes. The difficult and interesting regime is therefore narrower: qLDPC-like families with check weight at least four, both*X-*and*Z-check*ranks larger than one, and growing rank and distance. In that regime the conjecture predicts a linear rank budget with a small slope:
*d*≲ 1 8*max{rX , rZ}*+*O(1).*
This is far weaker than the geometric square-root principle asymptotically, but much sharper than the universal*d*≤*rσ*+ 1 linear-algebra bound. It may therefore be best viewed as a finite-code envelope: a practical obstruction to unusually large distance when both independent check rank and check weight are small.
14
**Question 3.***Is the coefficient 7/8 in Conjec-ture 5 intrinsic, or is it a finite-registry artifact? More invariantly, for which constants a, b does an envelope of the form*
*d(C)*≤ max*σ∈{X,Z}*
*⌊a rank(Hσ)*+*b wmax σ*⌋
*hold on natural CSS subclasses? Under which balance hypotheses can the maximum be replaced by a minimum?***Question 4.***Can Conjecture 5 be proved for broader generalized bicycle codes, for hypergraph products involving Hamming checks, or for other explicit algebraic families appearing in the registry?*
4 Discussion The initially discovered inequality was false, but fruitfully false. It surfaced a square-root rank–distance pattern with sharp finite witnesses: Steane for the floor form and Golay for the ceiling form. The BCH counterexample shows exactly why no rank-only theorem can hold, while the toric-code family shows that the square-root exponent is the right geometric scale. The resulting research direction is sharper than the original conjecture: identify geometric hypotheses under which CSS distance is controlled by the square root of check rank, and determine the best constants in natural two-dimensional families.
The later rank–locality envelope suggests a complementary finite-code program. Instead of asking rank alone to control distance, it combines independent check rank with maximum check weight on both the*X*and*Z*sides. The Shor code refutes the most optimistic minimum version in asymmetric presentations, while the symmetric maximum version is sharp on Steane, consistent with Golay and BCH behavior, and experimentally stable under substantial out-of-sample stress testing. Its constants are not treated here as canonical. Rather, the envelope gives a concrete finite-code target: determine whether distance can be bounded by a small linear combination of independent check rank and maximum check weight on natural CSS subclasses, and identify which balance conditions allow the stronger minimum form.
For AI for science, the point is methodological: a conjecturing system can produce useful scientific questions even when its first conjecture is
false. In this case, falsification did not end the process; it revealed the distinction between geometric and algebraic CSS behavior, motivated new registry features, and produced sharper conjectures. The same pattern repeats at a finer scale: Shor explains why an unrestricted minimum rank–locality budget is too strong, and the rankless self-CSS envelope is sharp on Steane and Golay, but the*[[47, 1,*11]] quantum QR code explains why check weight alone is insufficient and why the rank term in the surviving envelope is structurally meaningful. For quantum error correction, the point is structural: the discovered relationships suggest new ways to measure when distance is governed by check rank, when it is governed by locality, and when a family is escaping two-dimensional geometric intuition.
This is also why the counterexamples are central rather than incidental. The Golay, BCH, and QR examples are not merely failures of formulas generated from a small table. They identify the boundary between plausible finite-code regularities and genuinely algebraic high-distance behavior. In that sense, the paper’s QEC contribution is a set of falsifiable rank/locality problems equipped with named witnesses, verified counterexamples, and proof targets, rather than a claim that the current conjecturing engine has certified a new universal law.
5 Methods 5.1 Registry and feature computation The basic input to Theo-Conjecture is a finite registry of explicit mathematical objects. In the present study each quantum-code object was represented by binary matrices*HX , HZ*
satisfying*HXHT Z*= 0 over F2. The feature
table included numerical invariants such as*n, mX*,*mZ*,*rank(HX), rank(HZ),*maximum row weights, exact CSS distances when computationally available, Tanner-graph statistics, and qubit-interaction graph statistics. It also included Boolean predicates introduced during the study, including nonempty*X-*and*Z-check*sides, equal*X/Z*row spaces, geometric/topological construction class, hypergraph-product construction class, algebraic or cyclic construction class, and self-CSS presentation.
For small and moderate examples, distances were computed exactly from the definitions of*dX*
15
and*dZ*by searching the relevant quotient spaces. For large named families where exhaustive distance computation is not practical in the local workflow, the manuscript uses standard codetheoretic facts, such as designed distance certificates for the BCH examples and known distances for Steane, Golay, toric, and quadratic-residue codes. All linear-algebraic quantities in the feature table were computed over F2.
5.2 Conjecture generation
Theo-Conjecture follows the TxGraf-fiti/Graffiti3 snapshot-theory framework. Candidate conjectures are generated from a fixed table of objects, numerical invariants, and Boolean predicates. The expression grammar constructs compact inequalities and implications, and ranking filters remove weaker or redundant statements. In this sense the software is not only a conjecture generator but a theory-building tool: it maintains a compact, auditable collection of laws, hypotheses, counterexamples, and definitions attached to a particular evidence snapshot. A generated statement is therefore not a theorem; it is a compact law that survives all objects in the current snapshot. This distinction is essential in the present paper: the floor and ceiling rank–distance conjectures were generated or promoted because they were true on an early snapshot, and their later failures became mathematically informative counterexamples.
The finite status of each statement was evaluated by computing the premise and conclusion on each registry object for which the required features were available. When a new object or feature was added, the registry was resynchronized and the conjecture generation process was rerun against the enlarged table. This is how empty-check counterexamples led to the predicate has_both_check_types, and how BCH, Golay, toric, and quadratic-residue examples changed the conjecture landscape. The reduced provenance record separates the initial seed registry from later added examples, so the counterexample-guided evolution of the table can be audited independently of the private platform logs.
For reproducibility, each discovery run can be associated with a snapshot of the registry, the selected area and target invariant, the Boolean hypotheses available at the time, the generated
conjecture list, any statements selected for inspection, and subsequent counterexample objects added to the registry. The raw platform artifacts also include implementation-level metadata from the private research environment, so the archival record for this paper is kept in two layers: a reduced provenance manifest containing run identifiers, statement identifiers, registrysynchronization milestones, counterexample objects, and feature tables; and internal full run exports retained by the author. This makes the workflow auditable without requiring the publication of proprietary platform traces.
5.3 Co-Pilot and counterexample verification
The LLM Co-Pilot is part of the Theo -Conjecture environment rather than a separate post-processing step. In this study it was used to translate formulas into mathematical language, propose proof strategies, suggest candidate counterexamples, identify missing hypotheses, and help author new Boolean definitions. Positive theorems still require proof. Counterex-amples, however, were checked through a structured verifier: given a proposed CSS object, the verifier parsed the*HX , HZ*matrices, recomputed the local feature row, evaluated the premise and conclusion of the current statement, and returned a GUI-renderable object that could be added to the registry. Thus the workflow separates heuristic assistance from explicit computational certification.
Human judgment remained part of the loop. The author decided which Co-Pilot suggestions were mathematically meaningful, which known code families should be added, which definitions should become registry predicates, and which claims required proof rather than finite evidence. The discovery process should therefore be read as system-level human–AI collaboration inside Theo-Conjecture: deterministic conjecture generation produced table-true laws, verifier-backed counterexample interaction tested them on explicit CSS objects, Co-Pilot accelerated mathematical interpretation of failures, and the final statements were selected and proved or refuted by ordinary mathematical standards.
The public release of Theo-Conjecture is intended to include a redacted version of this kind of run trace. In the present study, the trace separates four roles that are easily con-
16
flated in informal AI-discovery narratives: deterministic conjecture generation from a feature table, LLM-assisted mathematical interpretation, verifier-backed counterexample certification, and human selection of meaningful definitions and research directions.
5.4 Stress tests and figures
The symmetric maximum rank–locality envelope was tested on the curated registry and on additional out-of-sample CSS presentations. The reported stress tests included 2560 benchmark and generated presentations from toric, Golay, BCH, generalized bicycle, hypergraph-product, Ham-ming, and random exact-distance sources, followed by 4500 additional sparse random CSS presentations with 6 ≤*n*≤ 20. In each case the test recomputed the relevant features and checked the symmetric maximum bound in Conjecture 5; balanced subfamilies were also checked against the stronger minimum form. The plots in Figs. 1 and 2 were produced from the same registry and benchmark feature tables used for these checks. These tests are used as counterexample search and finite evidence only; they are not treated as proof of the conjecture beyond the regimes proved in the Results section.
Data availability
The reduced reviewer-facing archive for this study contains the named code matrices, computed feature tables, feature dictionary, reduced run-history manifest, counterexample-object payloads, registry-synchronization records, and plotting data needed to audit the claims made here. The archive separates public mathematical objects and feature tables from full authenticated Theo-Conjecture run exports, which may contain proprietary platform metadata or private workflow traces. Those full internal artifacts are retained by the author and can be made available to editors or referees under appropriate confidentiality and access constraints. Before public release, the submission version of the reduced archive will be frozen with a registry snapshot hash, exported CSV feature tables, random seeds for out-of-sample stress tests, the seed-registry object list, the subsequently added benchmark and counterexample objects, and a mapping from
each manuscript conjecture or counterexample to its corresponding run, statement, and object identifiers.
Code availability
The figure-generation script and reduced analysis artifacts needed to reproduce the manuscript plots are included with the reviewer-facing archive. The broader Theo-Conjecture code used for registry synchronization, feature computation, conjecture generation, Co-Pilot-assisted inspection, counterexample verification, and stress testing is under active development. A reproducible snapshot sufficient to recompute the released feature tables, counterexample checks, stress tests, and figures will be provided for review and released with the data before publication. Platform code and private run-replay infrastructure that are not necessary to verify the mathematical claims may remain proprietary.
Author contributions
R.D. conceived the quantum-code conjecturing study, developed the Theo-Conjecture workflow used here, performed the registry experiments, developed the mathematical interpretation, selected the quantum-error-correction examples, checked the proofs and counterexamples, and drafted and revised the manuscript.
Generative AI use
This study used large-language-model assistance in two distinct ways. First, the integrated Theo -Conjecture Co-Pilot was used as part of the research workflow described in Methods. Second, large-language-model writing assistance was used during manuscript preparation for outlining, editorial critique, mathematical phrasing, and TEX revision. All mathematical statements, proofs, counterexample claims, citations, figures, and final wording were reviewed by the author, who takes full responsibility for the manuscript content.
17
Competing interests
R.D. develops Theo-Conjecture, the conjecturing environment used in this study. The author declares no other competing interests.
References [1] A. R. Calderbank and P. W. Shor, Good quan-
tum error-correcting codes exist, Physical Re-view A 54 (1996), 1098–1105.
[2] A. M. Steane, Simple quantum errorcorrecting codes, Physical Review A 54 (1996), 4741–4751.
[3] A. R. Calderbank, E. M. Rains, P. W. Shor, and N. J. A. Sloane, Quantum error correction via codes over GF(4), IEEE Transactions on Information Theory 44 (1998), 1369–1387.
[4] S. Bravyi, D. Poulin, and B. Terhal, Trade-offs for reliable quantum information storage in 2D systems, Physical Review Letters 104 (2010), 050503.
[5] N. Delfosse, Tradeoffs for reliable quantum information storage in surface codes and color codes, Proceedings of the IEEE International Symposium on Information Theory (2013), 917–921.
[6] A. Yu. Kitaev, Fault-tolerant quantum computation by anyons, Annals of Physics 303 (2003), 2–30.
[7] J.-P. Tillich and G. Zémor, Quantum LDPC codes with positive rate and minimum distance proportional to*n1/2,*IEEE Transactions on Information Theory 60 (2014), 1193–1202.
[8] M. B. Hastings, J. Haah, and R. O’Donnell, Fiber bundle codes: breaking the*N1/2 polylog(N)*barrier for quantum LDPC codes, Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing (2021), 1276–1288.
[9] P. Panteleev and G. Kalachev, Quantum LDPC codes with almost linear minimum distance, IEEE Transactions on Information Theory 68 (2022), 213–229.
[10] P. Panteleev and G. Kalachev, Asymptoti-cally good quantum and locally testable classical LDPC codes, Proceedings of the 54th An-nual ACM SIGACT Symposium on Theory of Computing (2022), 375–388.
[11] A. Leverrier and G. Zémor, Quantum Tan-ner codes, Proceedings of the 63rd IEEE An-
nual Symposium on Foundations of Computer Science (2022), 872–883.
[12] L. Wang, A. Z. Liu, R. Li, A. Kubica, and S. Gu, Check-weight-constrained quantum codes: Bounds and examples, preprint (2026). https://arxiv.org/abs/2601.15446.
[13] S. A. Aly, A. Klappenecker, and P. K. Sarvepalli, Primitive quantum BCH codes over finite fields, Proceedings of the IEEE In-ternational Symposium on Information The-ory (2006), 1114–1118. https://arxiv.org/ abs/quant-ph/0501126.
[14] S. A. Aly, A. Klappenecker, and P. K. Sarvepalli, On quantum and classical BCH codes, IEEE Transactions on Information Theory 53 (2007), 1183–1188. https:// arxiv.org/abs/quant-ph/0604102.
[15] V. V. Albert et al.,*[[23, 1,*7]] Quantum Go-lay code, The Error Correction Zoo. https:// errorcorrectionzoo.org/c/qubit_golay.
[16] R. He, I. S. Reed, T. K. Truong, and X. Chen, High speed decoding of the binary*(47, 24,*11) quadratic residue code, Informa-tion Sciences 180 (2010), 4060–4068.
[17] V. V. Albert et al., Quantum quadraticresidue code, The Error Correction Zoo. https://errorcorrectionzoo.org/c/ galois_quad_residue.
[18] S. Fajtlowicz, On conjectures of Graffiti, Dis-crete Mathematics 72 (1988), 113–118.
[19] C. E. Larson and N. Van Cleemput, Auto-mated conjecturing I: Fajtlowicz’s Dalmatian heuristic revisited, Artificial Intelligence 231 (2016), 17–38.
[20] R. Davila, Automated conjecturing with Tx-Graffiti, Annals of Mathematics and Artificial Intelligence (2026).
[21] R. Davila, Graffiti3: Compact The-ory Libraries for Automated Math-ematical Discovery, preprint (2026). https://assets-eu.researchsquare. com/files/rs-8493329/v1_covered_ f3b2ebd5-1eff-4ba6-aa7a-671608894aaf. pdf?c=1768810987.
[22] A. Davies, P. Veličković, L. Buesing, S. Blackwell, D. Zheng, N. Tomašev, R. Tan-burn, P. Battaglia, C. Blundell, A. Juhász, M. Lackenby, G. Williamson, D. Hassabis, and P. Kohli, Advancing mathematics by guiding human intuition with AI, Nature 600 (2021), 70–74.
18
[23] S.-M. Udrescu and M. Tegmark, AI Feyn-man: A physics-inspired method for symbolic regression, Science Advances 6 (2020), eaay2631.
[24] M. Krenn, M. Malik, R. Fickler, R. Lap-kiewicz, and A. Zeilinger, Automated search for new quantum experiments, Physical Re-view Letters 116 (2016), 090405.
[25] Y. Alexeev et al., Artificial intelligence for quantum computing, Nature Communications 16 (2025), 10829.
19