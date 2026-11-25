# EXP-009: heuristic SAT search for a level-4 counterexample (superseded)

**Method.** `sat_batch.py` runs CaDiCaL on "MC(y*g) <= 4" (6 variables) for each EXP-008 representative, with a budget of 10^6 conflicts.
**Result.** 25 of 297 representatives were run, all UNKNOWN (budget exhausted, about 85 s each). The run was stopped once the exact procedure of EXP-010 was available (`sat_batch_1M_partial.log`). No counterexample was found. This experiment proves nothing; it is kept only as a record.
