# Current state of NP-FRONTIER

Last updated: 2026-11-25, end of cycle 001. **Single source of truth**: start every session here (CLAUDE.md §13).

## Honest summary
P versus NP is unresolved, and nothing in this program changes that. Cycle 001 produced:
- a small set of rigorous results about one restricted measure, multiplicative complexity (MC: AND gates when XOR is free), in a linear-size regime far from P ≠ NP;
- formal verification of supporting lemmas in Lean;
- a sourced map of the barriers and no-go theorems.

## Active tracks and status

| ID | Direction | Status | One line |
|---|---|---|---|
| PNE-001 | P≠NP (restricted measure) | PROOF ATTEMPT | MC(y·g) = MC(g)+1. **Proved for all g with MC(g) ≤ 3 (Theorem 17, computer-assisted)** and whenever MC(g) = D(g). Open from level 4. |
| PNE-002 | P≠NP (restricted measure) | FORMULATED | AND-direct sum for MC. It would imply explicit c·n circuit lower bounds for every c, so it is believed hard. |
| OTH-001 | barrier | REVIEWED: elementary, framing corrected | Restriction-robust (P1) measures are ≤ D = D⊕−1 ≤ n−1. General one-kill-per-restriction arguments are capped at n−1 only by the folklore dimension count. |
| PEQ-001 | P=NP | DISPROVED (known theorems) | Bounded-width propagation / k-consistency fails (Ben-Sasson–Wigderson). |
| PEQ-002 | P=NP | DISPROVED as approach (known theorems) | Compact exact LP/SDP formulations are ruled out (Fiorini et al.; Lee–Raghavendra–Steurer). Not evidence for P ≠ NP (Rothvoss). |

## Established in cycle 001 (see `research/proofs/PNE-001-restriction-depth-and-fresh-variables.md`)

Results with unconfirmed novelty. Audit status: AUDIT-001 covers Lemmas 1–10 and Theorem 8. Lemmas 11–17 got a bounded check, and the core of Theorem 17 was independently recomputed. A full audit of Lemmas 11–17 is AUDIT-002.
- **Theorem 4:** D(y·g) = D(g)+1. Here D is the restriction depth, which equals D⊕ − 1 (AUDIT-001), so this is D⊕(y∧g) = D⊕(g)+1. It may be folklore.
- **Theorem 8:** a cap for restriction-robust measures.
- **Lemma 11:** structure of a minimal counterexample to PNE-001. Also: admissible first-gate directions for y·g come in pairs.
- **Proposition 10:** MC(y·g*) = 4 for g* = 0xfff3d212. Proved three ways: by Corollary 13, by an exhaustive SAT-free first-gate certificate, and by SAT with a DRAT proof checked by drat-trim.
- **Corollary 13:** PNE-001 holds at level MC(g) = 3 whenever g has a single cheap direction.
- **Lemmas 14(b′), 15 and Theorem 16:** PNE-001 for all g with MC(g) ≤ 3 is equivalent to MC(y·G') = 4 for the MC-3 members of an explicit 5-variable family G' = x1ℓ1 + x2ℓ2 + x1x2ℓ3 + λ(u), which has 33 symmetry orbits. EXP-006 finished: 31 orbits have MC ≤ 2 and 2 have MC 3, both certified. **This gives Theorem 17: PNE-001 for all g with MC(g) ≤ 3.**

Known or folklore, included for completeness:
- Lemma 1 (D ≤ MC; essentially Chistopolskaya–Podolskii).
- Lemma 3 (degree is restriction-robust).

Computational facts:
- MC is known exactly for all 2^16 functions on 4 variables, and MC = D on all of them.
- On 5 variables, MC > D occurs: 38 of 41 sampled degree-3 functions with D = 2 have MC 3. All 38 were independently confirmed.
- Lean: core-Lean ANF/degree library (no sorry; standard axioms only). Theorem 4 itself is **not** formalized.

## Priorities for cycle 002
1. **Level 4 of PNE-001.** A counterexample needs two cheap directions with halves of MC ≤ 2 (Lemma 12). Find the analogue of Lemmas 14–15 for MC-2 halves, using the structure theory of MC-2 functions (Find–Smith-Tone–Sönmez Turan characterize them). Also look for a human proof of the two level-3 certificates.
2. **Find a measure that charges both branches** of a split, valid for circuits and exceeding D. Note that any measure that removes one hyperplane per gate is capped at n−1 (Theorem 8). See open question 2.
3. **Seed for explicit MC ≥ n.** Obtain a certified 6-variable g₆ with MC 6 (ePrint 2018/002), then test MC(y·g₆) = 7 with the first-gate certificate method.
4. **Formalize Lemma 1 and Theorem 4 in Lean** (XOR-AND circuits, affine restrictions).
5. **PEQ track:** find a candidate outside known proof-system lower bounds. First, check the literature on Res(⊕).

## Environment notes
Lean 4.37.0-rc1 (core only). PySAT/CaDiCaL with DRAT logging. drat-trim is built by `scripts/setup_env.sh`. arXiv, ECCC and cache.mathlib.org are blocked; WebSearch works.
