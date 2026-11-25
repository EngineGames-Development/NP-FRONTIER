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
1. **Restriction depth D** (parity decision tree depth with affine leaves) caps every restriction-robust lower-bound measure (Theorem 8). AUDIT-001 showed D = D⊕ − 1, so this is the parity-decision-tree bound, and the cap is elementary. General one-gate-per-restriction arguments are capped at n − 1 only by the folklore dimension count.
2. **Theorem 4:** D(y·g) = D(g) + 1, equivalently D⊕(y∧g) = D⊕(g) + 1 (novelty unconfirmed). So PNE-001 holds whenever MC(g) = D(g).
3. **First-gate certificates.**
   - Lemma 9: the first gate of an optimal circuit has two distinct *admissible* directions.
   - For y·g these come in pairs (v,0), (v,1) (Lemma 11).
   - A counterexample must use two distinct x-directions, each splitting g into two halves of MC ≤ m − 2 (Lemma 12).
4. **Multiplexer gap.** MC > D arises when g is cheap on both halves of a split: the tree pays for one branch, the circuit for both. On 5 variables this is common.
5. **Reduction of level 3 to a finite family (Theorem 16).**
   - A counterexample g with MC(g) = 3 has two cheap directions (Lemma 12).
   - Its quarters then differ by affine functions (Lemma 14(b′)), and they must themselves be affine (Lemma 15, via a rank-4 obstruction and the exact 4-variable table).
   - So g reduces to G' = x1ℓ1 + x2ℓ2 + x1x2ℓ3 + λ(u) on 5 variables. A leftover fresh linear variable can only increase MC(y·g).
   - The family has 32,768 members and **33 orbits** under affine symmetries that preserve MC(y·g).

## Proof attempts and exact status
All in `research/proofs/PNE-001-restriction-depth-and-fresh-variables.md`.

| Claim | Status |
|---|---|
| Lemma 1 (D ≤ MC) | Complete proof; identical to Chistopolskaya–Podolskii (AUDIT-001) |
| Lemma 2 (cap) | Complete proof |
| Lemma 3 (degree restriction-robust) | Complete proof; folklore |
| Theorem 4 | Complete proof; survives AUDIT-001; novelty unconfirmed (PDT literature) |
| Corollaries 5–7 | Complete proofs; Corollary 7 needed "non-constant" (fixed) |
| Theorem 8 | Complete proof but elementary; "barrier" framing overclaimed and corrected (AUDIT-001) |
| Lemma 9 | Complete proof |
| Proposition 10 (MC(y·g*) = 4) | Proved by Corollary 13 and by an exhaustive certificate; DRAT-verified; reconfirmed by AUDIT-001's independent search |
| Lemmas 11, 12; Corollary 13 | Complete proofs |
| Lemma 14, 14(b′), 15; Theorem 16 | Complete proofs (Lemma 15 uses the exact 4-variable table) |
| Theorem 17 (PNE-001 for MC ≤ 3) | Complete, computer-assisted (EXP-001, EXP-006) |

Independent audit: see "Proof audit" below.

Failed attempt: substituting y := α + c at the first y-gate yields only MC(g) ≤ 2m − t − 1. The two halves g·α and g·(1+α) can need separate gates, so the argument does not close. PNE-001 remains open in general.

## Experiments
- **EXP-001.** Exact MC of all 65,536 four-variable functions, by span BFS with no SAT solver: 32 / 1,120 / 31,616 / 32,768 for MC 0..3. MC = 3 exactly when the degree is 4.
- **EXP-002.** MC = D on all 4-variable functions, so PNE-001 holds for every g on ≤ 4 variables. 450 sampled 5-variable functions show MC > D occurs: 38 of 41 degree-3 functions with D = 2 have MC = 3, all 38 independently confirmed.
- **EXP-003.** SAT reports no 3-AND circuit for y·g*. The DRAT proof (767 MB) was **verified by drat-trim** (617 s).
- **EXP-004.** Exhaustive SAT-free first-gate certificates. MC(y·g*) = 4, with a positive control. 4 further functions are NONE, agreeing with Corollary 13. The 7 functions with three cheap directions are all NONE.
- **EXP-005.** 31/38 functions have one cheap direction, so PNE-001 is proved for them by Corollary 13. 7/38 have three. Random search refutes "MC = 3 ⇒ one cheap direction". All 12 multi-direction examples have affine quarters, consistent with Lemma 15.
- **EXP-006.** The finite check of Theorem 16. The exhaustive S_2 set has |S_2| = 1,811,456 five-variable functions; the construction is validated at n = 4 against the BFS, and |S_1| = 9,984 matches the closed form. Of the 33 orbit representatives, 31 have MC ≤ 2 and need no certificate. Only 2 representatives have MC = 3 (0x01234567, 0x0167abcd), and both are certified: MC(y·G') = 4, with 48 first gates checked each. **This gives Theorem 17: PNE-001 holds for every g with MC(g) ≤ 3, on any number of variables.** SAT+DRAT cross-check of the two certificates: PENDING.

## Counterexamples
- To the conjecture "MC(g) = 3 ⇒ at most one cheap direction": e.g. g = 0x47fca912, with cheap directions {x1, x2, x1+x2}.
- To PNE-001: none found.

## Proof audit
**AUDIT-001** (`research/proofs/audits/AUDIT-001-PNE-001.md`): a fresh adversarial reviewer, given only the document and code, with its own independent C and Python code.
- **Survive:** Lemmas 1–3, Theorem 4, Corollaries 5–6, Lemma 9, Proposition 10.
- **Independently recomputed:** the 4-variable MC and D tables, identical per function. MC(y·g*) = 4, by a full search that does not use Lemma 9.
- **Issues, all fixed in the document:**
  - (I-1, medium) D = D⊕ − 1. So Lemma 1 equals Chistopolskaya–Podolskii, not "marginally stronger", and Theorem 4 is a parity-decision-tree statement with unconfirmed novelty.
  - (I-2, medium) Theorem 8's "barrier" framing was overclaimed. A pair measure from Lemma 9 beats D on g*. The cap holds only for (P1) measures, and is elementary.
  - (I-3, low) Corollary 7 fails for constant g.
  - (I-4, low) The multiplexer identity fails when both halves are constant.
  - Minor points: a readable circuit for g* was supplied and verified; the four first gates are one class mod affine; a stray λ00; monotonicity of D under restriction was needed for (F3).
- **Lemmas 11–17:** bounded check only. Lemma 15 and Theorem 16 read correctly. The reviewer's own code finds the same 33 orbits, exactly 2 of them outside S_2, and no 3-gate circuit for y·G' on six members of those orbits.

**AUDIT-002** (full audit of Lemmas 11–17): see `research/proofs/audits/`.

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
- `same_direction_product`: the key step of Lemma 12.

Not formalized: Lemmas 1–2, Theorem 4, Lemmas 9–16, Theorem 17, and all computer-assisted claims.

## Results (what was actually established)
- **Main result, Theorem 17 (computer-assisted, full audit AUDIT-002 pending):** for every non-constant g with MC(g) ≤ 3, on any number of variables, MC(y·g) = MC(g) + 1.
- Rigorous, novelty unconfirmed:
  - Theorem 4, which is D⊕(y∧g) = D⊕(g) + 1.
  - Lemmas 11–12 (structure of minimal counterexamples), Lemma 15 and Theorem 16 (reduction of level 3 to a finite family).
- Rigorous but elementary or known: Lemma 1 (= Chistopolskaya–Podolskii), Lemma 3, Theorem 8.
  - PNE-001 for all g with MC(g) = D(g), hence for all g with ≤ 4 variables and all g with MC(g) ≤ 2.
  - PNE-001 for every g with MC(g) = 3 and a single cheap direction (Corollary 13).
- Computer-assisted:
  - PNE-001 for 31 + 4 certified 5-variable functions in the open regime.
  - MC(y·g*) = 4, by two independent SAT-free methods plus a DRAT-verified SAT proof.
- Refuted: "MC = 3 ⇒ one cheap direction".
- P=NP track: two standard approaches stated precisely and shown refuted by known theorems. No new PEQ mathematics.

## Failure analysis
- The main limitation is the dimension count: every argument removing one hyperplane per AND gate stops at n − 1. Our certificates are of that type at the top level, so they cannot reach the regime MC ≥ n.
- The original "barrier" framing of Theorem 8 was overclaimed; the independent audit caught it.
- Explicit MC ≥ n needs multi-kill arguments, counting, or a composition theorem proved by non-restriction means.
- SAT UNSAT on ≥ 5 variables is slow with the naive encoding; SAT-free structured certificates were faster and more trustworthy.
- Literature access is limited to search snippets, so novelty claims are uncertain.

## Next research direction
1. **Level 4 of PNE-001.** A counterexample needs two cheap directions with halves of MC ≤ 2 (Lemma 12). Find the analogue of Lemmas 14–15 using the characterization of MC-2 functions (Find–Smith-Tone–Sönmez Turan, ePrint 2015/1041). Reduce to a finite family again.
2. **Human proof of the two level-3 certificates** (G' = 0x01234567, 0x0167abcd), to remove the computer from Theorem 17.
3. **Novelty check of Theorem 4** against the parity-decision-tree literature (arXiv 2412.06552 and 1312.2143), when accessible.
4. **Seed for explicit MC ≥ n:** a certified 6-variable function with MC 6, then a test of MC(y·g₆) = 7. This needs PNE-001 at level 6, far beyond level 3.
5. **PEQ track:** a candidate not covered by known proof-system lower bounds. Start with Res(⊕) literature.
