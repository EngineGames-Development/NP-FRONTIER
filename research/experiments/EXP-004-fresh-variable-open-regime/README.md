# EXP-004: PNE-001 in the open regime (MC(g) = 3 > D(g) = 2), exhaustive first-gate certificates

**Question.** For 5-variable g with MC(g) = 3 > D(g) = 2, where Theorem 4 does not apply, is MC(y·g) = 4?

**Method.** `../EXP-002-restriction-depth/first_gate_general.py <g> [--distinct-x]`, SAT-free:
1. Compute the admissible directions of F = y·g: both restrictions satisfy MC ≤ 2, decided by an exhaustive span search.
2. For every first gate (⟨v,x⟩+e)(⟨w,x⟩+e') with v ≠ w admissible, test exhaustively whether two more AND gates can finish F.

"NONE" proves MC(y·g) ≥ 4 by Lemma 9. `--distinct-x` additionally skips pairs v, w with equal x-part, which is justified by Lemma 12. Positive control: x1x2x3·y gives "FOUND" (first gate x1·x2).

**Runs.**
- `run_batch.py` covered all 38 certified functions. It was stopped after 4, because Corollary 13 (EXP-005) settles the 31 functions with a single cheap direction without search. The 4 completed results are in `results_partial_all38.json`. All 4 are single-cheap-direction functions, and all are NONE, agreeing with Corollary 13 by an independent method.
- `run_hard7.py` covers the 7 functions with three cheap directions, where Corollary 13 does not apply. **All 7 are NONE**, so MC(y·g) = 4 for each, at 500–850 s per function (`results_hard7.json`, `run_hard7.log`).

**Conclusion.** PNE-001 holds for all 38 sampled 5-variable functions with MC 3 > D 2: 31 by Corollary 13, and 7 plus 4 by exhaustive certificates. This is subsumed by Theorem 17. It also cross-validates Theorem 17 through a different code path, which computes admissible directions by per-restriction exhaustive search rather than the precomputed S_2 array.

**Limitations.** Exhaustiveness depends on the span-enumeration code. This is the same code as Proposition 10, which is under independent audit.
