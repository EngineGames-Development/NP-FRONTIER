# EXP-014: level 4 of PNE-001 for every n via formal circuits (Theorem 25)

**Question.** Is there g (on any number of variables) with MC(g) = 4 = MC(y*g)?

**Reduction (Lemma 23 in `research/proofs/PNE-001-level4.md`).** Such a g exists iff the following holds:
- there is a formal 4-gate circuit Phi on 8 formal inputs (each gate input has its own variable w_t plus earlier gates);
- there is a subspace K of F_2^8 with dim K in {5,6,7};
- there are two distinct cosets C0, C1 of K;
- Phi|C0 is affine and MC(Phi|C1) = 4.

Gate-input swaps reduce the 32,768 wirings to 8,640. Lemma 24: if a gate input (or the sum of a gate's inputs) is constant on K-cosets without gate terms, then MC(Phi|C) <= 3 on every coset.

**Programs.**
- `formal4.c K`: enumeration over all subspaces of dimension K (RREF), all cosets, and the affinity test. For K = 5 it also does the exact table lookup.
  - `formal4_full.c` (-DFULL) uses all 32,768 wirings.
  - `formal4_k5nd.c` deduplicates the non-degenerate K = 5 functions modulo affine.
- `triage.py`: degeneracy test and deduplication modulo affine for K = 6, 7.
- `mc3_check*.py`: SAT search for a 3-gate circuit with `mc.py` (cycle 001, DRAT-validated); every circuit is re-evaluated.
- `formalm.c M K`: the same method for M <= 3 gates.
- `test_affine.c`: 1.4M unit tests of the affinity routine.
- `indep_check.py`: independent numpy re-implementation (dual-subspace enumeration, interpolation-based affinity test, dual degeneracy test, all wirings).

**Results.**

| dim K | affine cosets | (C0,C1) pairs | degenerate | non-degenerate | distinct mod affine | 3-gate circuit |
|---|---|---|---|---|---|---|
| 7 | 1,020 | 840 | 840 | 0 | 0 | n/a |
| 6 | 297,128 | 509,220 | 489,576 | 19,644 | 72 | 72/72 |
| 5 | 17,467,504 | 66,989,104 | 57,400,384 | 9,588,720 | 2,142 | 2,142/2,142 |

- For K = 5 the exact table additionally gives the MC distribution 1: 23,017,648; 2: 27,492,928; 3: 16,478,528; 4: 0.
- Full wirings (`formal4_full`): K = 7 gives 3,072 / 2,688; K = 6 gives 908,800 / 1,663,872, of which 72,576 are non-degenerate, giving 160 distinct functions, all with a 3-gate circuit (`mc3_check_full.json`).
- `indep_check.py` reproduces K = 7 exactly (3,072 / 2,688 / 0); for K = 6 see `indep_check.log`.
- Levels 1-3 (`formalm`): no counterexample. This re-derives Theorem 17 independently.

**Conclusion.** No level-4 counterexample exists for any n. This is computer-assisted, and its correctness rests on Lemma 23 and this code.

**Reproduce:**
```
gcc -O2 -fopenmp -o formal4 formal4.c
./formal4 7 > out_k7.txt; ./formal4 6 > out_k6.txt
python3 triage.py
python3 mc3_check.py
gcc -O2 -fopenmp -o formal4_k5nd formal4_k5nd.c && ./formal4_k5nd 5 > /dev/null
python3 mc3_check_n.py 5 nondeg_k5.txt mc3_check_k5.json
```
Runtime: seconds for K = 6 and 7, about 2 minutes for K = 5 (4 cores), and about 12 minutes for the SAT checks.
