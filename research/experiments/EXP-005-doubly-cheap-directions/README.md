# EXP-005: cheap directions of MC-3 functions (Corollary 13)

**Question.** For 5-variable g with MC(g) = 3, how many directions v have both restrictions g|⟨v,x⟩=c of MC ≤ 1? By Lemma 12 and Corollary 13, at most one such direction implies MC(y·g) = 4.

**Method.** `doubly_cheap.py` uses the exact 4-variable MC table (EXP-001), so it needs no SAT solver. Part 2 samples random multiplexers along x1 with MC-≤1 halves, and certifies MC ≥ 3 with the exhaustive S_2 test.

**Results.**
- Over the 38 certified MC-3 functions of EXP-002, the number of cheap directions is 1 for 31 functions and 3 for 7 functions. In all 7, the directions together with 0 form a 2-dimensional subspace. So PNE-001 is **proved** for the 31 by Corollary 13, including g* = 0xfff3d212.
- Random multiplexers: 9 tried, 7 with MC ≥ 3, 5 of those with three cheap directions (e.g. 0x47fca912 with A = {x1, x2, x1+x2}). So the conjecture "MC = 3 implies at most one cheap direction" is false.

**Reproduce.** `python3 doubly_cheap.py` (a few minutes).

**Interpretation.** The number of cheap directions was never 2 in the data. A plausible structural statement, unproved: the set of cheap directions together with 0 is always a linear subspace.
