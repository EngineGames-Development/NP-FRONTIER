# Current state of NP-FRONTIER

Last updated: 2026-11-25, cycle 002 (AUDIT-003 and the Lean task pending at time of writing). **Single source of truth**: start every session here (CLAUDE.md §13).

## Honest summary
P versus NP is unresolved, and nothing in this program changes that.

Cycle 002 extended the fresh-variable lemma (PNE-001) from MC(g) ≤ 3 to **MC(g) ≤ 4, for every number of variables**. The result is computer-assisted. Two independent routes support it:
- formal-circuit enumeration (Lemma 23, EXP-014);
- NIST's published MC-4 class list (Lemma 26, EXP-015).

It is still a statement about a restricted measure at constant complexity levels.

Cycle 001 produced:
- a small set of rigorous results about one restricted measure, multiplicative complexity (MC: AND gates when XOR is free), in a linear-size regime far from P ≠ NP;
- formal verification of supporting lemmas in Lean;
- a sourced map of the barriers and no-go theorems.

## Active tracks and status

| ID | Direction | Status | One line |
|---|---|---|---|
| PNE-001 | P≠NP (restricted measure) | PROOF ATTEMPT (level ≤ 3 REVIEWED; level 4 proved, AUDIT-003 pending) | MC(y·g) = MC(g)+1. **Proved for all g with MC(g) ≤ 4, all n.** Level ≤ 3 is Theorem 17. Level 4 is Theorem 25 (cycle 002, computer-assisted, two independent routes). Also proved for all quadratic g, all g on ≤ 5 variables, and whenever MC(g) = D(g). Open from level 5. Novelty unconfirmed (2016 NIST email). |
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
- **Theorem 25:** PNE-001 at level 4 for every n. Computer-assisted: EXP-014 (formal circuits; all non-degenerate cases have explicit 3-gate circuits) and EXP-015 (NIST class list, 186 hyperplane cases).
- **Lemma 23:** for each level m, PNE-001 is equivalent to a finite, n-independent statement about formal m-gate circuits and coset pairs in F_2^{2m}. **Lemma 26:** the same in terms of the MC-m class list.
- **Lemma 28 / Corollary 29 (human proof, every level):** a formal circuit that is affine on a coset of a hyperplane has a degenerate last gate. Hence PNE-001 holds for every g with dim(g) ≥ 2·MC(g) − 1. EXP-016 confirms this by enumeration at m = 5.
- **Lemma 22:** dim(y·g) ≥ dim(g)+1. Consequences: PNE-001 for every quadratic g; level-m counterexamples have dim ≤ 2m−1. Part (a), MC ≥ ⌈dim/2⌉, is known (Çalık–Sönmez Turan–Peralta 2020).
- Lemmas 9′, 18–21: MC-2 structure and the cheap-plane structure of level-4 counterexamples. **Theorem 27:** all g on ≤ 5 variables, three independent confirmations.
- Exact MC of all 2^32 five-variable functions. It agrees with NIST's classification on all 48 classes.
- Audit: AUDIT-003 pending. Lean: circuit gate-elimination formalization pending.

## Priorities for cycle 003
1. **Codimension 2:** prove PNE-001 for dim(g) ≥ 2·MC(g) − 2, every level. The m = 4 data say the last gate is always redundant on C_1. Note that the stronger form "some gate of the given circuit is redundant" is refuted at codimension 3.
2. **Level 5 of PNE-001 via Lemma 23.**
   - Brute force is about 10^15 coset tests: 2.35M wirings × subspaces of F_2^10 of dimension 6–9.
   - Design pruning: Lemma 24's conditions are linear in K and can be imposed gate by gate, combined with circuit automorphisms and early affinity filtering.
   - Partial data: the NIST dimension-10 MC-5 list (EXP-015).
3. **A human-readable proof of level 4.** Explain the rarity of non-degenerate coset pairs. Try an induction on m for the statement "Φ affine on C_0 with K non-degenerate ⇒ MC(Φ|C_1) ≤ m−1".
4. **Novelty.** Find the 2016 NIST attachment (MultComp3) or a later publication of the fresh-variable claim. Resolve the s5 discrepancy with the paper text; ePrint is behind Cloudflare, so try the Springer page or the authors' pages.
5. Carried over from cycle 001: a measure that charges both branches (open question 2), the explicit MC ≥ n seed (open question 3), and the PEQ track.

## Environment notes
Lean 4.37.0-rc1 (core only). PySAT/CaDiCaL with DRAT logging. drat-trim is built by `scripts/setup_env.sh`.

Since cycle 002 the session runs on the personal cloud environment "NP-FRONTIER". It allows arxiv.org, export.arxiv.org, eprint.iacr.org, csrc.nist.gov, nist.pqcrypto.org, eccc.weizmann.ac.il and cache.mathlib.org, and runs `scripts/setup_env.sh` as its setup script (unproven until a fresh session starts). ePrint serves a Cloudflare challenge to scripts. NIST data: `git clone https://github.com/usnistgov/circuits` (public; read-only).
