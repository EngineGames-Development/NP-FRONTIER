# Research cycle 002 — 2026-11-25

## Research question
Does the fresh-variable lemma (PNE-001) hold at multiplicative complexity 4? Precisely: is $\mathrm{MC}(y\cdot g)=5$ for every $g:\mathbb F_2^n\to\mathbb F_2$ (any $n$) with $\mathrm{MC}(g)=4$? Here $y$ is a fresh variable and MC counts AND gates over $\{\wedge,\oplus,1\}$. The cycle-001 result, Theorem 17, settles $\mathrm{MC}(g)\le3$. We did not assume the conjecture: the cycle searched for counterexamples first.

## Motivation
PNE-001 is the one-variable case of the AND-direct-sum question PNE-002. If PNE-002 held, it would give explicit circuit lower bounds $cn$ for every $c$. PNE-001 is also the step needed to turn certified small seeds into explicit functions with MC $\ge n$ (open question 3). None of this bears on P vs NP directly. MC is a restricted measure, and every result here is about constant-size complexity levels.

## Previous knowledge
- Cycle 001:
  - Theorem 4 ($D(y\,g)=D(g)+1$ for restriction depth);
  - Lemma 9 (first-gate criterion);
  - Lemma 11 (admissible directions pair up);
  - Theorem 17 (level $\le3$, DRAT-verified, AUDIT-002).
- Literature retrieved this cycle (records in `research/literature/`):
  - Çalık–Sönmez Turan–Peralta 2020: the bound $\mathrm{MC}\ge\lceil\dim/2\rceil$, 24 classes of MC 3 and 1277 of MC 4. The abstract, slides and class lists were retrieved; the paper PDF was not.
  - NIST's MC classification of all functions on $n\le6$ variables (github.com/usnistgov/circuits, cloned).
  - Sönmez Turan–Peralta 2014: every 5-variable function has MC $\le4$ (search summary).
  - A 2016 NIST email (FOIA release, read): Peralta claims $\mathrm{MC}(uv f)=1+\mathrm{MC}(vf)$ "as a corollary of the claim in the attached", and the attachment is not released.

## New ideas
1. **Lemma 9′ and the MC-2 structure** (Lemmas 18–21). These reduce level 4 on 5 variables to a finite family $\mathcal F_5$ of $2^{29}$ functions.
2. **Lemma 22**: $\dim(y\,g)\ge\dim g+1$. So level-$m$ counterexamples have $\dim g\le 2m-1$, and PNE-001 holds for all quadratics.
3. **Lemma 23 (formal-circuit reformulation)** is the key idea of the cycle. Every $m$-gate circuit for $y\,g$ is a fixed formal circuit on $2m$ free inputs composed with an affine map. Under that map, $y=0$ and $y=1$ become two cosets $C_0\neq C_1$ of one linear subspace $K$. So a level-$m$ counterexample exists **for some $n$** iff some formal circuit is affine on $C_0$ and has MC $m$ on $C_1$. This is a finite problem, independent of $n$.
4. **Lemma 24 (degenerate gates)**: one linear condition on $K$ per gate makes that gate free on every coset.
5. **Lemma 26 (class-list reformulation)**: equivalently, some MC-$m$ class representative $R$ is affine on an affine hyperplane while having MC $m$ on the complement. Published class lists can therefore be used directly.

## Proof attempts and exact status
- Lemmas 9′, 18–24, 26 and fact (F4): full proofs in `research/proofs/PNE-001-level4.md`. They await AUDIT-003.
- **Theorem 25 (level 4, all $n$; computer-assisted):** $\mathrm{MC}(g)=4\Rightarrow\mathrm{MC}(y\,g)=5$. Consequently **PNE-001 holds for every $g$ with $\mathrm{MC}(g)\le4$.** The proof is Lemma 23 plus the EXP-014 enumeration. It is independently confirmed by Lemma 26 plus NIST's complete MC-4 class list (EXP-015).
- **Theorem 27:** PNE-001 holds for all $g$ on $\le5$ variables. This is a special case of Theorems 17 and 25, and has three further independent confirmations (EXP-010, EXP-014 with $\dim K=5$, EXP-015).
- General PNE-001 (level $\ge5$): open.

## Experiments
| ID | Question | Result |
|---|---|---|
| EXP-007 | Exact $S_3$ on 5 variables (no SAT) | $\lvert S_3\rvert=779{,}571{,}200$. MC distribution 64 / 9,920 / 1,801,472 / 777,759,744 / 3,515,396,096. Matches NIST on all 48 classes. |
| EXP-008 | MC-4 members of $\mathcal F_5$ up to symmetry | 337,784,832 members in 297 orbits |
| EXP-009 | Heuristic SAT counterexample search | 25 representatives, all UNKNOWN; superseded |
| EXP-010 | Exact procedure cert4b on the 297 representatives | all NONE, i.e. $\mathrm{MC}(y\,g)\ge5$. 74/74 positive controls FOUND |
| EXP-013 | SAT with the first gate fixed | about 700 s per plane, infeasible; 2 planes UNSAT |
| EXP-014 | Formal 4-gate circuits, $\dim K\in\{5,6,7\}$ | 840 / 509,220 / 66,989,104 coset pairs. Every pair is degenerate or one of 0 / 72 / 2,142 distinct functions, each with an explicit 3-gate circuit. No counterexample. |
| EXP-015 | NIST data | 48/48 class agreement. Levels 3 and 4 confirmed on 5 variables. Class-list route: levels 3 and 4, no counterexample for any $n$ (27 and 186 hyperplane cases). |

Limitations:
- Theorem 25 rests on code, though on two code bases that share only the SAT encoding (DRAT-validated in cycle 001) and the published NIST list.
- The 5-variable MC-3 count disagrees with a constant on a NIST slide ($s_5$), though our table agrees with NIST's class data. The cause is unresolved.

## Counterexamples
None found to PNE-001. Refuted along the way:
- Our own expectation that the degree-3 representatives would be hard for cert4b (they took 35 s each).
- The approach "SAT with the first gate fixed" as a verification method: too slow.

## Proof audit
AUDIT-003 (fresh adversarial reviewer; Lemmas 9′–26, Theorems 25 and 27, all code): **pending**. The verdict will be recorded in `research/proofs/audits/AUDIT-003-PNE-001-level4.md` and summarized here.

## Formal verification
Lean (core 4.37.0-rc1): the proof engineer is formalizing XOR-AND circuits with gate elimination and affine substitution. These are the circuit facts behind Lemmas 9, 9′, 23 and 24. **Status: pending.** The enumeration in Theorem 25 and the reformulation in Lemma 23 are not formalized.

## Results (what was actually established)
1. **Theorem 25 (computer-assisted, all $n$):** $\mathrm{MC}(y\,g)=\mathrm{MC}(g)+1$ for every non-constant $g$ with $\mathrm{MC}(g)\le4$.
2. **Lemma 23:** for every fixed level $m$, PNE-001 is equivalent to a finite, $n$-independent statement about formal $m$-gate circuits.
3. **Lemma 22:** PNE-001 holds for all quadratic $g$. Level-$m$ counterexamples have dimension $\le2m-1$.
4. Exact MC of all $2^{32}$ five-variable functions without SAT. It agrees with NIST's classification.
5. Structural results: Lemmas 18–21 on MC-2 functions and the cheap-plane structure.

Novelty:
- **Unconfirmed.** The 2016 NIST email shows that a special case was claimed in unpublished form.
- The bound in Lemma 22(a) is known.

## Failure analysis
- The structural route (Lemmas 18–21) explains only the 5-variable case. For $n=6,7$ its family is far too large ($\sim10^{14}$ members).
- What worked was changing the object enumerated: formal circuits and coset pairs instead of functions $g$.
- Two verification ideas failed on cost: fixed-first-gate SAT, and SAT budgets on the full problem.
- The "tight functions are product trees" route (EXP-011) was not pursued further. Its induction does not close, because a single restricted half can lose more than one degree.

## Next research direction
1. **Level 5 via Lemma 23.**
   - There are $\approx2.35\cdot10^6$ wirings, and subspaces of $\mathbb F_2^{10}$ of dimension 6–9 ($\approx6\cdot10^7$ of them). Brute force is about $10^{15}$ coset tests.
   - Needed: prune non-degenerate $(\Phi,K)$ pairs gate by gate, since Lemma 24's conditions are linear in $K$, and exploit the circuit automorphisms.
   - A partial result is available now: Lemma 26 on NIST's dimension-10 MC-5 list (`EXP-015/nist_level5_dim10.log`).
2. **A human-readable proof of level 4.** Explain why non-degenerate coset pairs are so rare (0, 72 and 2,142 distinct functions), and try to prove "non-degenerate and affine on $C_0$ implies MC $\le m-1$ on $C_1$" by induction on $m$.
3. Resolve the $s_5$ discrepancy once the paper text is accessible.
