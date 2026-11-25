# EXP-017: falsification test of Lemma 30 (codimension 2) at m = 5

**Question.** Does the case analysis in the proof of Lemma 30 hold beyond m = 4? The case analysis says: for a formal m-gate circuit Φ and a codimension-2 subspace K with Φ affine on some coset, every non-affine coset C₁ falls into one of three cases.
- **Case 0,** dim π(H) = 0: never occurs.
- **Case 2,** dim π(H) = 2: the last gate is redundant on C₁.
- **Case 1,** dim π(H) = 1: the gate named by the proof is degenerate for K.

Here H = K^⊥ and π projects H onto the coordinates of the last gate's two private inputs.

**Method.** `codim2.c m samples seed` enumerates all codimension-2 subspaces as dual planes {h1, h2}: 10,795 for m = 4 and 174,251 for m = 5. For each subspace it builds all 4 cosets using a BMI2 pdep parametrization, then runs a Möbius affinity test. Redundancy is tested by GF(2) elimination on 256-bit vectors. Degeneracy is tested by membership of the degeneracy vector in H.

**Validation (m = 4, all 8,640 swap-reduced wirings).**
- 509,220 ordered (C₀, C₁) pairs, matching formal4's dim K = 6 count.
- Case 0: none.
- Case 2: 121,212 cosets, all with a redundant last gate.
- Case 1: 157,432 cosets, all with the predicted gate degenerate.
- No violations.

**m = 5 (random sample: 4,000 of the 2,350,080 swap-reduced wirings, seed 2026; wall time 28.5 min on 4 cores).**
- 258,841 ordered (C₀, C₁) pairs, involving 133,333 distinct non-affine cosets C₁.
- Case 0: none.
- Case 2: 63,368 cosets, all with a redundant last gate.
- Case 1: 69,965 cosets, all with the predicted gate degenerate.
- 0 violations. The cases add up: 63,368 + 69,965 = 133,333.
- Full log: `codim2_m5.log`.

**Interpretation.** No counterexample to the case analysis of Lemma 30 was found at m = 5. This is evidence, not proof: the sample covers 0.17 % of the wirings, and Lemma 30's validity for every m rests on its written proof, which AUDIT-003 reviews. The test can falsify the proof's specific case predictions, not merely its conclusion, and it did not.

**Reproduce.**
```
gcc -O2 -mbmi2 -fopenmp -o codim2 codim2.c
./codim2 4 0
./codim2 5 4000 2026
```
