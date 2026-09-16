# Comments to Shay
 
Good selection. I like the tools. A few comments:
 
1) Is everything kept in plain text (input as text, e.g., SKILL.md for the LLM, output as text), or is there a more complex data representation? The Missing-Physics Detector is important (perhaps the most important). The example is correct in one regime. Another regime involves small object diameter or high viscosity.
2) The uncertainty engine is important. Are the intervals kept as text or as objects? Broader context might matter; take two papers, one where the error is reported as sigma, another as three sigma; or one error is the error of a single measurement and another is the error of an estimate of the mean value (the difference being a factor of 1/√N, where N is the number of measurements). Finally, error is often associated not just with a number but with an assumption. E.g., neglecting the second-order hopping terms when modeling magnetic order in cuprates is associated with a certain error (in some parameter regions it might be under 1%; in others it might determine the order of the phases).
Even more important (and this is a lesson from IAIFI): a single number for the error is not enough; what physicists really care about is information about what contributes to the error (e.g., random vs. systematic). The error from neglecting the second-order hopping term is systematic. The error associated with grid discretization is ... [actually, I don't know; I have arguments for both]. Measurement errors are often both.
 
3) Very, very cool! [I mean it; no sarcasm]
Though there are regimes where you are UNABLE to perform inverse calculations (e.g., near critical points - see my paper https://www.nature.com/articles/s41524-022-00889-2).
 
4) Cool. I hadn't thought about it.
Is it trackable? Seems like a very hard problem in general. I mean... it seems like the core of what physicists do...
 
5) Very cool.
Just one comment: the checks have different weights. "Simulation settings recorded" is more important than "software versions," which can often be inferred from when the code was created... (and I'd say most physicists don't bother to record versions, sadly).
 
"Do we get the same result again?" needs intervals. And it can be prohibitively expensive to run some calculations - computational physics often pushes the boundary of what's possible, with simulations that can run for months (I myself once had such a case). Repeating this several times to get statistics could cost an insane amount of money.
 
6–9) Cool. I see direct synergy with what we've done for TREC RAG. The competitions pay off :tada:
 
Though the most interesting sentences (the novel ideas, disagreements, etc.) will, by definition, have no "evidence" attached. 
 
# Comments to Moinul
 
A really cool presentation, @Moinul Hossain Rahat, and great work! :tada:
 
A few comments.
 
1) There's probably an infinite number of families, and even so they won't cover all of physics given how "family" is currently defined. The selection process is also likely to get harder, not easier, as the number of families grows... We might already have problems distinguishing the family - and if you add to this the problem of selecting the right oracle (or group of oracles), it will be even harder... I'm thinking a hierarchical (or tree-like) system might help here (so the number of searches grows like logN, not N)...
2) A more basic issue: just changing notation can move a problem from one "family" to another, even when the physics hasn't changed. Three coupled masses between two walls is canonically the same system as three independent, non-interacting single-mass oscillators, each on its own wall, once you switch to normal-mode coordinates. Same physics, different family under your template matching (assuming I understood your template matching well; correct me, if I misread this).
One way around this is to define a family as a group in the algebraic sense: a set of formulations all generated from any single member via canonical transformations. That would handle the normal-mode case fine, since both forms are just elements of the same orbit. But it raises two questions of its own. First, does the family as it's currently built actually satisfy closure under those transformations? Can we even build a group in the strict algebraic sense? Second, even if it does, does the union of all these groups actually cover "the physics," or only the slice of analytical portions of physics?
 
3) That's the generalization worry more broadly too. I don't know how well this approach carries over from simple analytical-mechanics problems to frontier physics: non-commutative algebras, equivalent-but-differently-written formulations (different Hamiltonian gauges, for instance), Feynman diagrams, etc. There may not be a clean template to match against in any of those cases.
It might not be a big issue - covering something is still better than nothing. And I can also envision a "marketplace" where people add various verification components or layers (maybe some community-driven)... This would also simplify the selection choice (if we select oracles only from a smaller, predefined group...). So there are some ways to deal with it. But the question of how much we can actually cover is still valid to ask, I think.
 
4) Last point, from IAIFI. Plehn said something like
the real physics you're trying to describe doesn't live in a perfectly symmetric regime
 
I'm still trying to understand this - because this stands a bit in opposition to our effort of using symmetries as one of our verification toolkits. I think (@Xingyang Yu, you might help me and verify the following statement), it means that most (all?) fundamental symmetries get broken by interactions, dynamics, or measurement along the way. So yes, we have those symmetries on one, theoretical end of our description, but while we move towards real systems (such as those that MERL might care about), nothing from those symmetries is left (or rather, they become "approximate" only...).
 
Tahmasebi's talk (again IAIFI) contributed to this... It was about enforcing exact group symmetry requires averaging over the whole group, which is usually intractable; the proposed approach used a random subset of size roughly log|G| to capture "approximate symmetry".
 
This finally ties in with my previous comment. My point was that often, physics derivations are not "correct." The most interesting ones break rules on purpose: they drop terms, neglect effects, invent fields that don't exist, and break symmetries the exact theory respects. Strictly read, they don't conserve the quantities they should, and the before/after is often not algebraically equivalent. Though, in this case, I accept the argument by @Moinul Hossain Rahat that it is still good to check (deterministically, if possible) if something is broken or if convention is changed - and then let the higher-level system (LLM? User?) interpret what it means - e.g., whether the equation that does not meet the unit check (e.g., log(1/T) term) is incorrect, or whether we just silently moved to natural units...