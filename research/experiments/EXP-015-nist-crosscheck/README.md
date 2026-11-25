# EXP-015: cross-checks against NIST's published classification

**Source.** github.com/usnistgov/circuits (cloned in cycle 002), `data/mc_dim/`. It contains representatives of all affine equivalence classes of MC <= 4 (MC 3: 24 classes; MC 4: 1,277 classes in dimensions 5-8). For 6 variables it covers all classes (MC 5 and 6 in dimension 6). Related publications: Çalık, Sönmez Turan, Peralta, Cryptogr. Commun. 2019 (6 variables) and 2020 (MC 3 and 4).

**Checks.**
1. `check_mc5_vs_nist.py`: our exact 5-variable table gives NIST's MC for all 48 classes of dimension <= 5 (that is, all 5-variable classes) and passes 200,000 random affine-invariance tests. **0 mismatches, 0 violations.**
2. `nist_level_check.py`: PNE-001 at levels 3 and 4 for all 5-variable g. For each class representative g0 and each of the 32 linear forms l, the function y*(g0+l) must not be affine-equivalent to any class of MC <= m. Test: an affine-invariant fingerprint (degree, |Walsh| multiset, |autocorrelation| multiset, derivative degrees), checked against all 943 classes of MC <= 4 and dimension <= 6. The fingerprint's invariance is self-tested.
   - Level 3: 544 functions, 0 collisions.
   - Level 4: 832 functions, 0 collisions.
3. `nist_hyperplane_check.py m`: Lemma 26. For each class representative R of MC m and each affine hyperplane H, if R|H is affine, then the other half must have MC <= m-1. A 3-gate (or 2-gate) circuit is found by SAT and re-evaluated.
   - Level 3: 24 classes, 27 hits, 0 counterexamples.
   - **Level 4: 1,277 classes, 186 hits, 0 counterexamples** (`nist_level4.log`). This is an independent proof route for Theorem 25, resting on the published class list.
   - Level 5, dimension-10 classes only (`mc5_dim10.txt`, 575 classes): see `nist_level5_dim10.log`. This is partial, because NIST's MC-5 lists are not complete.

**Reproduce:** clone the repository to `/home/user/usnistgov/circuits`, then run each script with python3.
