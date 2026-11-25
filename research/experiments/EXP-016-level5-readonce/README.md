# EXP-016: the read-once case (dim K = 2m − 1) of Lemma 23, at m = 4 and m = 5

**Question.** Take a formal m-gate circuit Φ on F_2^{2m} and a hyperplane K = ker(h). If Φ is affine on one coset of K, is the pair always degenerate (Lemma 24)?

Lemma 28 (PNE-001-level4.md) proves this by hand for every m; it even forces the *last* gate to be degenerate. This experiment checks the prediction by exhaustive enumeration.

**Method.** `hyper.c m` enumerates:
- all formal m-gate circuits with α_i ≤ β_i, giving 8,640 wirings for m = 4 and 2,350,080 for m = 5;
- all 2^{2m} − 1 hyperplanes and both cosets of each.

The affinity test uses a bit-sliced restriction followed by a Möbius transform. Hyperplane pairs where one coset is affine and the other is not are classified as degenerate if h is the degeneracy vector of some gate. Only non-degenerate pairs are printed.

**Validation.** At m = 4 it reproduces formal4's dim K = 7 counts exactly: 1,020 affine cosets and 840 pairs, all degenerate.

**Results.**
- m = 4: 840 pairs, 0 non-degenerate.
- m = 5: 2,350,080 wirings × 1,023 hyperplanes give 71,280 affine cosets and 64,800 pairs, **all degenerate; 0 non-degenerate** (`hyper_m5.log`, 11 min on 4 cores). This agrees with Lemma 28. So there is no level-5 counterexample in which the 10 gate-input forms are linearly independent, also by direct enumeration.

Lemma 28 predicts 0 non-degenerate pairs for every m.

**Reproduce:** `gcc -O2 -fopenmp -o hyper hyper.c && ./hyper 5 > out_m5_nd.txt`
