# Research cycle 003 — 2026-11-25/26

## Research question
1. **Codimension 3, every level.** Let $\Phi$ be a formal $m$-gate circuit that is affine on one coset of a codimension-3 subspace $K\subseteq\mathbb F_2^{2m}$. Is $\mathrm{MC}(\Phi|_C)\le m-1$ on every coset $C$? By Lemma 23 this is PNE-001 for $\dim g=2\,\mathrm{MC}(g)-3$. PNE-001 is the claim $\mathrm{MC}(y\,g)=\mathrm{MC}(g)+1$, where MC counts AND gates over $\{\wedge,\oplus,1\}$.
2. **Level 5.** Is there a non-constant $g$ with $\mathrm{MC}(g)=5=\mathrm{MC}(y\,g)$?

## Motivation
- In cycle 002 codimensions 1 and 2 were proved by hand at every level, and level 4 was settled by a codimension-3 computation.
- That computation exposed a "hard core" of 2,152,192 coset pairs in which no gate of the given circuit is redundant. A human proof of codimension 3 would explain it, make level 4 essentially computation-free, and push the reduction for every level one step further.
- PNE-001 is the one-variable case of the AND-direct-sum question PNE-002, and a route to explicit MC $\ge n$ seeds (open question 3).
- It is a statement about one restricted measure at constant levels. It does not bear on P vs NP.

## Previous knowledge
Cycle 002 (`research/proofs/PNE-001-level4.md`, AUDIT-003):
- Lemma 23 (formal-circuit reformulation) and Lemma 24 (degenerate gates);
- Lemma 28 (codimension 1), Lemma 30 with (IF′) (codimension 2), Corollary 31;
- Theorem 25 (level 4, computer-assisted);
- the codimension-3 hard core located in $\dim\pi(H)=2$ with different $H_0$-classes.

## New ideas
1. **Unused gates.** 71% of the sampled hard core has a gate that nothing reads, which is trivially harmless. In every other sampled pair, $\mathrm{top}(h_0)=m-1$.
2. **Restriction to a hyperplane of $w''$-space, (P1)/(P2).** One private variable of gate $k=\mathrm{top}(t)$ is eliminated, giving $z_k=\tilde A s$. Translating to the parallel hyperplane flips $\tilde A$. Independence survives when gate $k$ is non-degenerate.
3. **The merge (Lemma 32, case b1).** When $k=m-1$, the last two gates collapse into one gate $R_1\cdot s$ on the other coset. This is a new circuit, not a shortening of the given one, which explains the hard core exactly.
4. **Top-gate analysis (case b2).** Gate $m-1$ has two free private variables. A multilinear expansion forces $P,Q\in\mathrm{span}(1,X,Y,XY)$ or an exit.
5. **Recursion for $\dim\pi(H)=1$.** The sub-circuit $\Psi$ is affine on a codimension-$\le2$ coset, so Lemmas 28 and 30′ apply to it.
6. **Lemma 37 (top-two perturbation, any circuit, any domain).** Perturbing the input constants of the top two gates of a circuit that is affine on $S$ costs at most $m-1$ gates. A ternary quadratic form has rank $\le2$, so one AND gate suffices. This re-proves case b1 and settles one codimension-4 sub-case.
7. **Lemma 36 (a necessary condition at level 5).** A counterexample has a cheap plane: all six halves have MC $\le3$. This follows from Lemma 9′, Lemma 11, and PNE-001 at level $\le4$. It can be tested on NIST's class list.

## Proof attempts and exact status
- **Lemma 32 (codimension 3, every $m$): proved.** It survives AUDIT-004 with presentational corrections I-1 to I-8, all applied (`research/proofs/PNE-001-codim3.md`). Lemma 30′, the structural form of Lemma 30, is stated for citation.
- **Corollary 33:** PNE-001 whenever $\dim g\ge2\,\mathrm{MC}(g)-3$, at every level.
- **Corollary 34:** level 4 follows from Lemmas 23, 24, 28, 30 and 32, plus the classical fact that every 4-variable function has MC $\le3$. The cycle-002 enumerations become independent confirmations.
- **Corollary 35:** a level-5 counterexample has $\dim g=6$ exactly. In Lemma 23 it lives in codimension 4 of $\mathbb F_2^{10}$.
- **Lemma 36 and Lemma 37: proved** (`research/proofs/PNE-001-level5.md`). They are not yet audited. The identities behind Lemma 37 were brute-force checked.
- **Codimension 4 / level 5: open.** The written arguments cover every sampled configuration except NEW-2:
  - $\dim\pi(H)=2$ and $\dim H_0=2$;
  - the non-separating $t_2$ eliminates a private variable of gate $m-1$;
  - the separating $t_1$ has a lower top gate.

  The $\dim\pi(H)=1$ branch also needs a written argument: its recursion meets the merge and unused sub-cases of $\Psi$.

## Experiments
| ID | Question | Result |
|---|---|---|
| EXP-018 `hc_dump`, `merge_check` | Structure of the cycle-002 hard core | 1,084 samples: 770 have an unused gate; the other 314 all have $\mathrm{top}(h_0)=m-1$. Merge identity holds for all 531 samples with $\mathrm{top}=m-1$. |
| EXP-018 `codim3` $m=4$ | All cases of Lemma 32, exhaustive (8,640 wirings × 97,155 subspaces) | 5,494,392 non-degenerate cases, **0 violations** |
| EXP-018 `codim3` $m=5$ | Same, 300 random wirings × 6,347,715 subspaces | 77,348 non-degenerate cases, **0 violations** |
| AUDIT-004 harness | Every prediction and formula of the proof, with certificates | $m=4$ all 32,768 wirings (229,201,152 pairs); $m=5$ about 52.6M pairs; $m=6$ about 13.3M pairs. **0 violations.** Mutation tests detect planted errors. |
| EXP-019 `codim4` | Codimension 4 at $m=5$: mechanisms, 4 wirings × 53,743,987 subspaces | 934,015 cosets: 91% degenerate. 2.3% HARD, all NEW-1 or NEW-2. **All 131 distinct HARD functions have verified 4-gate circuits.** |
| EXP-019 `cheapplane6` | Lemma 36 on NIST's 148,483 MC-5 classes on 6 variables | 35,861 survive (24%) |
| EXP-019 `codim4` (40 wirings) | Larger falsification sample | Running at the time of writing; see `EXP-019/codim4_s40.log` |

## Counterexamples
None to PNE-001.

Refuted along the way:
- the reading of $f_y$ as the coefficient of $w_{2m-3}$ in $f$, which the auditor's mutant shows false (AUDIT-004 I-2); the proof uses $f|_E$;
- the expectation that the merge with an input of gate $m-1$ explains all codimension-4 HARD cases. NEW-1 needs the rank-2 product of Lemma 37, and NEW-2 needs rewired circuits.

## Proof audit
AUDIT-004 (`research/proofs/audits/AUDIT-004-PNE-001-codim3.md`) was done by a fresh adversarial reviewer, which received only the document and the code. Verdict: **no fatal or serious issue.**
- (P1), (P2), the exits, Lemma 32 for every $m$, and Corollaries 33 and 35 survive. Corollary 34 survives with a citation fix.
- Issues:
  - I-1: the 4-variable fact was cited to AUDIT-002 V-2, which does not check it.
  - I-2: $f_y$ must be read in $f|_E$.
  - I-3: cite a structural Lemma 30′ rather than the proof of Lemma 30.
  - I-4: the notation $X^\tau$ acts on expressions; $f_{\rm rest}$ is a form on the whole space; one step in sub-case (1,1) was missing.
  - I-5: `codim3.c` checks conclusions only.
  - I-7: wording in the README.
- All of these are corrected.
- The auditor's own harness, in different coordinates with a different affinity test, reproduced every author count exactly and checked every formula of the proof.
- It could not check $m\ge7$, or Lemma 32 in Lean.

## Formal verification
No new Lean this cycle. `Circuit.lean` from cycle 002 is unchanged; it builds under `--wfail` with standard axioms only. Lemmas 30′, 32, 36 and 37 and Corollaries 33–35 are **not formalized**.

## Results (what was actually established)
1. **Lemma 32 and Corollary 33 (human proofs, every level, audited):** PNE-001 holds whenever $\dim g\ge2\,\mathrm{MC}(g)-3$.
2. **Level 4 without enumeration (Corollary 34),** modulo the classical 4-variable fact.
3. **Level 5 reduced to 6 variables (Corollary 35).**
4. **Lemma 37 (unaudited):** top-two perturbations are always cheap, for any circuit and any domain.
5. **Lemma 36 + NIST data (unaudited; conditional on NIST's list):** a level-5 counterexample is $R+\ell$ for one of 35,861 representatives $R$ and a linear form $\ell$.

Novelty: unconfirmed. No prior statement was found in searches by us or by AUDIT-004, which saw snippets only. The 2016 NIST email claims a special case.

## Failure analysis
- **Shortening the given circuit is not enough at codimension 3 and beyond.** The fix was to construct new circuits: the merge in Lemma 32 and the rank-2 product in Lemma 37.
- **Level 5 by brute force is out of reach.** It would take about $1.3\cdot10^{14}$ (wiring, subspace) pairs at codimension 4. The class-list route leaves $35{,}861\times64$ SAT instances on 7 variables, and fixed-first-gate SAT was already about 700 s per plane at 5 variables (EXP-013).
- **NEW-2 resists the codimension-3 arguments.** Gate $m-1$ has only one free variable there, so the (b2) top-gate analysis fails, and the perturbation touches a lower gate, so Lemma 37 does not apply. In the decoded example, the cheap circuit rewires gates 2–4 around a shared product $\Pi$.

## Next research direction
1. **Prove NEW-2,** and write the $\dim\pi(H)=1$ branch, for codimension 4 at every $m$. This would settle level 5 and give PNE-001 whenever $\dim g\ge2\,\mathrm{MC}(g)-4$.
   - Concretely: in $\Phi|_C=R_0'+R_1's$, explain why $R_0'$ and $R_1'$ share one product. This probably needs a statement about products $XY$, with $X,Y\in L$, that lie in $L$ on a coset ("product-closure"), proved by induction on the gates.
   - A natural general target is statement (G): an $m$-gate circuit that computes an affine function on $S$ still has MC $\le m-1$ after any perturbation of its gate-input constants. By Lemma 23 and (F4), (G) is equivalent to PNE-001 at level $m$. Lemma 37 is (G) for perturbations of the top two gates.
2. **Computational level 5.**
   - Sharpen Lemma 36 using the second gate on each half, to cut the 35,861 candidates.
   - Or reduce formal 5-gate circuits by their full symmetry group, and enumerate only NEW-2 configurations.
3. Audit Lemmas 36 and 37 (AUDIT-005) before relying on them.
