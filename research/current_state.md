# Current state of NP-FRONTIER

Last updated: 2026-11-26, cycle 003 (AUDIT-004 done; corrections applied; level 5 open). **Single source of truth**: start every session here (CLAUDE.md §13).

## Honest summary
P versus NP is unresolved, and nothing in this program changes that.

Cycle 002 extended the fresh-variable lemma (PNE-001) from MC(g) ≤ 3 to **MC(g) ≤ 4, for every number of variables** (Theorem 25).
- The human-proved part (Lemmas 23, 24, 28, 30) reduces it to one 5-variable (codimension-3) computation.
- That computation is done by our formal-circuit enumeration (EXP-014), by NIST's published classification (EXP-015), and by an independent re-implementation in AUDIT-003.
- AUDIT-003 found no fatal or serious issue.

It is still a statement about a restricted measure at constant complexity levels.

Cycle 001 produced:
- a small set of rigorous results about one restricted measure, multiplicative complexity (MC: AND gates when XOR is free), in a linear-size regime far from P ≠ NP;
- formal verification of supporting lemmas in Lean;
- a sourced map of the barriers and no-go theorems.

## Active tracks and status

| ID | Direction | Status | One line |
|---|---|---|---|
| PNE-001 | P≠NP (restricted measure) | PROOF ATTEMPT for the general statement; levels ≤ 4 and codimension ≤ 3 REVIEWED (AUDIT-002/003/004) | MC(y·g) = MC(g)+1. **Proved for all g with MC(g) ≤ 4, all n.** Level ≤ 3 is Theorem 17. Level 4 is Theorem 25 (cycle 002): a human reduction to codimension 3, plus a computation re-done independently by AUDIT-003. Human proof for every level whenever dim g ≥ 2·MC(g) − 3 (Corollary 33, cycle 003). Level 5 reduces to 6-variable g and is open. Also proved for all quadratic g, all g on ≤ 5 variables, and whenever MC(g) = D(g). Open from level 5. Novelty unconfirmed (2016 NIST email). |
| PNE-002 | P≠NP (restricted measure) | FORMULATED | AND-direct sum for MC. It would imply explicit c·n circuit lower bounds for every c, so it is believed hard. |
| OTH-001 | barrier | REVIEWED: elementary, framing corrected | Restriction-robust (P1) measures are ≤ D = D⊕−1 ≤ n−1. General one-kill-per-restriction arguments are capped at n−1 only by the folklore dimension count. |
| PEQ-001 | P=NP | DISPROVED (known theorems) | Bounded-width propagation / k-consistency fails (Ben-Sasson–Wigderson). |
| PEQ-002 | P=NP | DISPROVED as approach (known theorems) | Compact exact LP/SDP formulations are ruled out (Fiorini et al.; Lee–Raghavendra–Steurer). Not evidence for P ≠ NP (Rothvoss). |

## Established in cycle 001 (see `research/proofs/PNE-001-restriction-depth-and-fresh-variables.md`)

Results with unconfirmed novelty. Audit status: AUDIT-001 covers Lemmas 1–10 and Theorem 8; claims survive and the framing was corrected. AUDIT-002 covers Lemmas 11–17; everything survives.
- **Theorem 4:** D(y·g) = D(g)+1. Here D is the restriction depth, which equals D⊕ − 1 (AUDIT-001), so this is D⊕(y∧g) = D⊕(g)+1. It may be folklore.
- **Theorem 8:** a cap for restriction-robust measures.
- **Lemma 11:** structure of a minimal counterexample to PNE-001. Also: admissible first-gate directions for y·g come in pairs.
- **Proposition 10:** MC(y·g*) = 4 for g* = 0xfff3d212. Proved three ways: by Corollary 13, by an exhaustive SAT-free first-gate certificate, and by SAT with a DRAT proof checked by drat-trim.
- **Corollary 13:** PNE-001 holds at level MC(g) = 3 whenever g has a single cheap direction.
- **Lemmas 14(b′), 15 and Theorem 16:** PNE-001 for all g with MC(g) ≤ 3 is equivalent to MC(y·G') = 4 for the MC-3 members of an explicit 5-variable family G' = x1ℓ1 + x2ℓ2 + x1x2ℓ3 + λ(u), which has 33 symmetry orbits. EXP-006 finished: 31 orbits have MC ≤ 2 and 2 have MC 3, both certified by the exhaustive search and by DRAT-verified SAT proofs. **This gives Theorem 17: PNE-001 for all g with MC(g) ≤ 3.**

Known or folklore, included for completeness:
- Lemma 1 (D ≤ MC; essentially Chistopolskaya–Podolskii).
- Lemma 3 (degree is restriction-robust).

Computational facts:
- MC is known exactly for all 2^16 functions on 4 variables, and MC = D on all of them.
- On 5 variables, MC > D occurs: 38 of 41 sampled degree-3 functions with D = 2 have MC 3. All 38 were independently confirmed.
- Lean: core-Lean ANF/degree library (no sorry; standard axioms only). Theorem 4 itself is **not** formalized.

## Established in cycle 002 (see `research/proofs/PNE-001-level4.md`, `research/cycles/cycle-002.md`)
- **Theorem 25:** PNE-001 at level 4 for every n.
  - Lemmas 28 and 30 exclude dim K = 7 and dim K = 6.
  - dim K = 5 is computed: EXP-014, where all non-degenerate cases have explicit 3-gate circuits; EXP-015, the NIST class list with 186 hyperplane cases; and AUDIT-003 V-3, the auditor's own code with an evaluated circuit for every pair.
- **Lemma 23:** for each level m, PNE-001 is equivalent to a finite, n-independent statement about formal m-gate circuits and coset pairs in F_2^{2m}. **Lemma 26:** the same in terms of the MC-m class list.
- **Lemmas 28 and 30, Corollary 31 (human proofs, every level).**
  - Lemma 28: a formal circuit that is affine on a coset of a subspace of codimension 1 has a degenerate last gate.
  - Lemma 30: for codimension 2, the last gate is redundant or some gate is degenerate.
  - Corollary 31: **PNE-001 holds for every g with dim(g) ≥ 2·MC(g) − 2.** So level 4 reduces by hand to 5 variables.
  - Checks: EXP-016 (m = 5, codimension 1), lemma30_check.py (m = 4, all 1,663,872 codimension-2 pairs) and EXP-017 (m = 5, a random 4,000-wiring sample: 133,333 codimension-2 cosets, 0 violations of the proof's case predictions).
- **Lemma 22:** dim(y·g) ≥ dim(g)+1. Consequences: PNE-001 for every quadratic g; level-m counterexamples have dim ≤ 2m−1. Part (a), MC ≥ ⌈dim/2⌉, is known (Çalık–Sönmez Turan–Peralta 2020).
- Lemmas 9′, 18–21: MC-2 structure and the cheap-plane structure of level-4 counterexamples. **Theorem 27:** all g on ≤ 5 variables, three independent confirmations.
- Exact MC of all 2^32 five-variable functions. It agrees with NIST's classification on all 48 classes.
- **Audit: AUDIT-003 done.** No fatal or serious finding. Corrections I-1 to I-12 are applied:
  - the circular citation in the structured proof;
  - the sources for MC ≤ 4 on 5 variables;
  - the fingerprint caveat;
  - s₅ is (63/31) × our count, a normalization difference;
  - wording fixes.
- Lean: `Circuit.lean` covers gate elimination, affine substitution and free affine output shifts. It builds under `--wfail` with standard axioms only.

## Established in cycle 003 (see `research/proofs/PNE-001-codim3.md`, `research/proofs/PNE-001-level5.md`, `research/cycles/cycle-003.md`)
- **Lemma 32 (codimension 3, every m; human proof; AUDIT-004: survives).** A formal m-gate circuit that is affine on one coset of a codimension-3 subspace has MC ≤ m−1 on every coset.
  - The proof's key new step is the merge: when top(h0) = m−1, gates m−1 and m collapse into one gate on the other coset.
  - Lemma 30′ states the structural form of Lemma 30.
- **Corollary 33:** PNE-001 whenever dim g ≥ 2·MC(g) − 3.
- **Corollary 34:** level 4 needs no enumeration beyond the classical "MC ≤ 3 on 4 variables".
- **Corollary 35:** a level-5 counterexample has dim g = 6, i.e. codimension 4 at m = 5.
- **Lemma 37 (top-two perturbation; unaudited):** for any circuit affine on S, perturbing the input constants of the top two gates gives MC ≤ m−1. This gives a one-line proof of the merge.
- **Lemma 38 (unaudited):** a redundant product persists unless its top gate is the separating gate. So the codimension-4 residue NEW-2 is a "double merge"; all 400 sampled NEW-2 instances are.
- **Lemma 39 (unaudited; exhaustively checked for small circuits):** product closure on the full domain. If XY ∈ L, then a factor is constant, or X+Y is constant, or both are functions of one gate's inputs.
- **Double merge, open.** Simple bilinear savings explain 101 of the 200 sampled k = m−2 double merges. The other 99 need the lower gates rewired; all have MC ≤ 4 by SAT.
- **Lemma 36 (unaudited):** a level-5 counterexample has a cheap plane. On NIST's 148,483 six-variable MC-5 classes, 35,861 survive.
- **EXP-018:** 0 violations of the Lemma 32 case analysis (m = 4 exhaustive; m = 5 sample). AUDIT-004's own harness: 0 violations at m = 4, 5, 6.
- **EXP-019 (codimension 4, m = 5):**
  - The residue NEW-2 is isolated: dim π(H) = 2, dim H0 = 2, the non-separating t2 hits gate m−1, and the separating t1 is lower.
  - Every sampled hard function has a verified 4-gate circuit.

## Priorities for cycle 004
1. **Codimension 4, every m (settles level 5).**
   - Prove the NEW-2 sub-case and write the dim π(H) = 1 branch.
   - Target: explain why, in Φ|C = R0' + R1'·s, the two slice functions share one product.
   - General frame: statement (G). Perturbing the gate-input constants of an m-gate circuit that is affine on S leaves MC ≤ m−1. (G) is equivalent to PNE-001 at level m; Lemma 37 proves it for the top two gates.
2. **AUDIT-005 of Lemmas 36–39** before using them further.
3. **Computational level 5 as a fallback.**
   - Sharpen Lemma 36 with second-gate conditions on the halves, to cut the 35,861 NIST candidates.
   - Or reduce formal 5-gate circuits by their full symmetry group (GL(2) per gate, z_i ↦ z_i + A_i) and enumerate NEW-2 only.
   - Finish the 40-wiring EXP-019 sample and SAT-check its distinct HARD functions.
4. **Novelty:**
   - the 2016 NIST attachment (MultComp3);
   - the paper text of Çalık–Sönmez Turan–Peralta 2020, for the s5 normalization (factor 63/31).
5. Carried over: a measure that charges both branches (open question 2), the explicit MC ≥ n seed (open question 3), the PEQ track, and Lean for Lemmas 23–32.

## Environment notes
Lean 4.37.0-rc1 (core only). PySAT/CaDiCaL with DRAT logging. drat-trim is built by `scripts/setup_env.sh`.

Since cycle 002 the session runs on the personal cloud environment "NP-FRONTIER". It allows arxiv.org, export.arxiv.org, eprint.iacr.org, csrc.nist.gov, nist.pqcrypto.org, eccc.weizmann.ac.il and cache.mathlib.org, and runs `scripts/setup_env.sh` as its setup script (unproven until a fresh session starts). ePrint serves a Cloudflare challenge to scripts. NIST data: `git clone https://github.com/usnistgov/circuits` (public; read-only).
