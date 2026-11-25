# EXP-013: fixed-first-gate SAT cross-check of EXP-010 (infeasible; recorded)

**Method.**
- `allplanes.py` tests all 651 first-gate planes with SAT for F = y*g (6 variables, k = 4).
- `admplanes.py` tests only the admissible planes. Admissibility is read from `mc5.mc5` with an independent hyperplane parametrization; the counts agree with cert4b (140 and 620).

**Result.** Each fixed-first-gate SAT call takes about 700 s. The two planes completed were UNSAT (`admplanes_*.log`). A full check would take days per representative, so it was stopped. It is superseded by EXP-014 and EXP-015.
