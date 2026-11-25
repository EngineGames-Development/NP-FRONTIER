# Research cycle 001 — 2026-11-25

## Research question
**PNE-001.** For every non-constant Boolean function g and a fresh variable y, is MC(y·g) = MC(g) + 1? Here MC is multiplicative complexity: the minimum number of AND gates over {AND, XOR, 1}.
Context question: which lower-bound principles for MC can go beyond the degree barrier MC ≥ n − 1?

## Motivation
- An explicit single-output function with MC > n is called "an important open problem" (Chistopolskaya–Podolskii, arXiv 1810.08668, per search summary). The best explicit single-output bound is n − 1.
- PNE-001, together with one certified 6-variable function of MC 6 (reported by Çalık–Sönmez Turan–Peralta), gives an explicit family with MC = n.
- Full composition (PNE-002) would give explicit circuit lower bounds c·n for every c, far beyond the refereed 3.1n.
- Distance to P ≠ NP: these are linear lower bounds for a restricted measure. They do not imply P ≠ NP, and no claim of the sort is made.

## Previous knowledge (sources in `research/literature/`, retrieval status in each record)
- MC ≥ deg − 1 (Schnorr 1988). D⊕ ≤ MC + 1 (Chistopolskaya–Podolskii).
- Maximum MC: n − 1 for n ≤ 5; 6 for n = 6 (Çalık et al.); some 7-variable function has MC ≥ 7 (Codish–Cruz-Filipe–Frank–Schneider-Kamp, non-constructive).
- Vector-valued explicit bound 2n − 3 (Boyar–Find; exact by Häner 2023).
- The fresh-variable lemma was not found in the literature (≈ 70% confidence).
- Circuit-size frontier: 3.1n − o(n) refereed (Li–Yang 2022); 3.5n − o(n) claimed, unrefereed (ECCC TR26-260).
- Barriers: relativization, natural proofs, algebrization, locality. No-go theorems for propagation, LP and SDP approaches.

## New ideas
1. **Restriction depth D** (parity decision tree depth with affine leaves) is the exact ceiling of "one restriction kills one AND gate" lower bounds (Theorem 8). In particular D ≤ n − 1.
2. **Theorem 4:** D(y·g) = D(g) + 1. So PNE-001 holds whenever MC(g) = D(g).
3. **First-gate certificates.**
   - Lemma 9: the first gate of an optimal circuit has two distinct *admissible* directions.
   - For y·g these come in pairs (v,0), (v,1) (Lemma 11).
   - A counterexample must use two distinct x-directions, each splitting g into two halves of MC ≤ m − 2 (Lemma 12).
4. **Multiplexer gap.** MC > D arises when g is cheap on both halves of a split: the tree pays for one branch, the circuit for both. On 5 variables this is common.

## Proof attempts and exact status
All in `research/proofs/PNE-001-restriction-depth-and-fresh-variables.md`.

| Claim | Status |
|---|---|
| Lemma 1 (D ≤ MC) | Complete proof; essentially known |
| Lemma 2 (cap) | Complete proof |
| Lemma 3 (degree restriction-robust) | Complete proof; folklore |
| Theorem 4 | Complete proof |
| Corollaries 5–7 | Complete proofs |
| Theorem 8 | Complete proof |
| Lemma 9 | Complete proof |
| Proposition 10 (MC(y·g*) = 4) | Proved twice: by Corollary 13 and by an exhaustive certificate |
| Lemmas 11, 12; Corollary 13 | Complete proofs |

Independent audit: see "Proof audit" below.

Failed attempt: substituting y := α + c at the first y-gate yields only MC(g) ≤ 2m − t − 1. The two halves g·α and g·(1+α) can need separate gates, so the argument does not close. PNE-001 remains open in general.

## Experiments
- **EXP-001.** Exact MC of all 65,536 four-variable functions, by span BFS with no SAT solver: 32 / 1,120 / 31,616 / 32,768 for MC 0..3. MC = 3 exactly when the degree is 4.
- **EXP-002.** MC = D on all 4-variable functions, so PNE-001 holds for every g on ≤ 4 variables. 450 sampled 5-variable functions show MC > D occurs: 38 of 41 degree-3 functions with D = 2 have MC = 3, all 38 independently confirmed.
- **EXP-003.** SAT reports no 3-AND circuit for y·g*. DRAT check: PENDING.
- **EXP-004.** Exhaustive SAT-free first-gate certificates. MC(y·g*) = 4, with a positive control. 4 further functions are NONE, agreeing with Corollary 13. The 7 functions with three cheap directions: PENDING.
- **EXP-005.** 31/38 functions have one cheap direction, so PNE-001 is proved for them by Corollary 13. 7/38 have three. Random search refutes "MC = 3 ⇒ one cheap direction".

## Counterexamples
- To the conjecture "MC(g) = 3 ⇒ at most one cheap direction": e.g. g = 0x47fca912, with cheap directions {x1, x2, x1+x2}.
- To PNE-001: none found.

## Proof audit
PENDING (adversarial reviewer, fresh agent, given only the proof document and code).

## Formal verification (Lean 4.37.0-rc1, core; `lake build --wfail`; axioms: standard only)
Proved:
- `peval_anf`: the ANF transform is correct (evaluation agrees).
- `anf_xor`: the ANF is linear.
- `top_anf`: the top ANF coefficient equals the weight parity.
- `degLE_pred_iff_even_weight`: full degree iff odd weight.
- `degLE_xor`: degree of a sum is at most the larger degree.
- `degLE_node_of_restrict`: Lemma 3 for coordinate hyperplanes.
- `degLE_restrict`: restriction does not increase degree.
- `gate_normalize`, `mul_eval_one`: the identities used in Theorem 4.

Not formalized: Lemmas 1–2, Theorem 4, Lemmas 9–12, and all computer-assisted claims.

## Results (what was actually established)
- Rigorous, novelty unconfirmed:
  - Theorem 4 and Theorem 8.
  - PNE-001 for all g with MC(g) = D(g), hence for all g with ≤ 4 variables and all g with MC(g) ≤ 2.
  - PNE-001 for every g with MC(g) = 3 and a single cheap direction (Corollary 13).
- Computer-assisted:
  - PNE-001 for 31 + 4 certified 5-variable functions in the open regime.
  - MC(y·g*) = 4, by two independent SAT-free methods.
- Refuted: "MC = 3 ⇒ one cheap direction".
- P=NP track: two standard approaches stated precisely and shown refuted by known theorems. No new PEQ mathematics.

## Failure analysis
- The main limitation is the cap of Theorem 8: every argument removing one hyperplane per AND gate stops at n − 1, and our certificates are of that type at the top level.
- Explicit MC ≥ n needs multi-kill arguments, counting, or a composition theorem proved by non-restriction means.
- SAT UNSAT on ≥ 5 variables is slow with the naive encoding; SAT-free structured certificates were faster and more trustworthy.
- Literature access is limited to search snippets, so novelty claims are uncertain.

## Next research direction
Prove PNE-001 for all g with MC(g) = 3 by hand, i.e. multiplexers whose halves have MC ≤ 1, including those with three cheap directions forming a plane. Then test level 4, and obtain a certified 6-variable seed to attack explicit MC ≥ n.
