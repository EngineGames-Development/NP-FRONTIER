# EXP-007: exact set S_3 of 5-variable functions with MC <= 3

**Question.** Compute exactly, without SAT, which 5-variable Boolean functions have MC <= 3.

**Method (`s3.c`, OpenMP).** Span enumeration over the first gate (155 classes of 2-dim spaces of linear forms modulo affine terms), all second-gate spaces W2 (77,035 distinct), and all third-gate cosets (150,409,210). Every element of each coset W3 = W2 + span(A*B) is marked in a 2^32-bit bitmap, `s3_5vars.bitmap`. The bitmap is gitignored and is rebuilt in about 2 minutes on 4 cores.

**Results** (`s3_run.log`): |S_2| = 1,811,456 and |S_3| = 779,571,200. No degree-5 function lies in S_3.

**Validation.**
- |S_2| matches cycle 001 (AUDIT-002).
- Lemma 18 holds exactly (`lemma18_check.py`).
- S_3 is affine-invariant under the EXP-008 generators.
- The derived table `EXP-010/mc5.mc5` gives NIST's MC value for every one of the 48 affine classes of 5-variable functions and passes 200,000 random affine-invariance tests (`EXP-015/check_mc5_vs_nist.py`).
- MC distribution of all 2^32 functions: 0: 64, 1: 9,920, 2: 1,801,472, 3: 777,759,744, 4: 3,515,396,096.
- The MC-1 and MC-2 counts match the published closed forms 2*C(32,3) and Find et al.'s formula, as shown on NIST's BFA 2019 slide.
- Unresolved: that slide's MC-3 constant s_5 = 1,576,479,744 does not match our 775,728,128 dimension-5 MC-3 functions (see PNE-001-level4.md, Theorem 27).

**Reproduce:** `gcc -O2 -fopenmp -o s3 s3.c && ./s3`.
