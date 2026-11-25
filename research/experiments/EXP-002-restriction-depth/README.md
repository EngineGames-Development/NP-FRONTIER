# EXP-002 / EXP-003: Restriction depth D vs. MC, and the fresh-variable test

**Research questions.** (EXP-002) For which functions does MC = D hold, where D is the restriction depth (Theorem 4 transfers the fresh-variable lemma exactly to these functions)? (EXP-003) For a function with MC > D, does MC(y·g) = MC(g) + 1 still hold?

**Methods.**
- `dpdt.py`: D for all functions on ≤ 4 variables by recursion over hyperplane restrictions. For 5–6 variables it uses the 4-variable table.
- `sample5.py`: 450 sampled 5-variable functions (150 uniform, 150 of degree ≤ 4, 150 of degree ≤ 3; seed 20261125). For each it computes D and asks SAT for a circuit with exactly D ANDs (budget 300k conflicts). SAT certifies MC = D, since D ≤ MC (Lemma 1). UNKNOWN means undecided within the budget.
- `verify_s2_5.py`: SAT-free exhaustive test of "MC ≤ 2" on 5 variables, over 155 distinct W_1 spaces × all products.
- `fresh_test.py`, `drat_certify.py`, `run_drat_yg_star.sh`: decide "MC(y·g) ≤ k" by SAT. The UNSAT answer is certified with a DRAT proof checked by drat-trim (github.com/marijnheule/drat-trim, compiled from source).

**Results.**
- All 4-variable functions: MC = D for all 65,536 (counts (0,0) 32, (1,1) 1120, (2,2) 31616, (3,3) 32768). With Corollary 5, this proves the fresh-variable lemma for every g on ≤ 4 variables.
- 5 variables: MC > D occurs. g* = 0xfff3d212 has deg 3 and D = 2, with witness query x2 whose restrictions have D = 1, 1. A 3-AND circuit exists: `([(58,5),(119,4),(175,223)], 511)`, as wire masks with bit 0 = constant, bits 1–5 = x1..x5, then z's. No 2-AND circuit exists, by the exhaustive SAT-free check. So MC(g*) = 3 > D(g*) = 2. Structure: a multiplexer on x2 of two rank-2 quadratics.
- EXP-003: SAT says no 3-AND circuit computes y·g* (UNSAT in 305 s). DRAT certification status: see `drat_yg_star.log` and the cycle report. If certified, MC(y·g*) = 4 = MC(g*) + 1, so the fresh-variable lemma holds for a function outside Theorem 4's reach.
- Sample statistics: see `sample5.log` and `sample5_results.json`. Summary in the cycle report.

**Limitations.** Samples are not exhaustive over the 5-variable affine-equivalence classes. "UNKNOWN" is not evidence of MC > D. The DRAT certificate depends on the correctness of the CNF encoding (`mc.encode`). The SAT direction is independently re-verified. The UNSAT direction was cross-validated on the 5-variable instance g* (k = 2) against the exhaustive check.
