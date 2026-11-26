# EXP-018: the codimension-3 "hard core" and Lemma 32

**Questions.**
1. What structure do the 2,152,192 codimension-3 coset pairs of cycle 002 have, at m = 4? In those pairs no gate of the given circuit is redundant, yet MC(Φ|C₁) ≤ 3.
2. Does the case analysis of the proof of Lemma 32 (`research/proofs/PNE-001-codim3.md`) hold for every circuit and every codimension-3 subspace?

**Programs.**
- `hc_dump.c` is `formal4_k5case.c` plus a sampler. It prints a pseudo-random 1/2000 of the hard-core pairs (dim π(H) = 2, C₀ and C₁ in different H₀-classes, no redundant gate) as wiring, basis of K, coset representatives and the truth table of Φ|C₁. Output: `hc_sample.txt`, 1,084 lines.
- `hc_lib.py` holds the helpers: circuits, cosets, duals, ANF.
- `merge_check.py` tests the merge identity Φ|C₁ ∈ V₀ + s·V₀ on the samples with top(h₀) = m−1.
- `codim3.c` is the falsification test of the conclusion of every case of the Lemma 32 proof (AUDIT-004 I-5 notes what it does not test; the auditor's harness covers that):
  - impossibility claims;
  - j* redundant when dim π = 1;
  - last gate redundant in case 2a;
  - the merge identity in case 2b1;
  - gate m−1 unused, or last gate redundant, in case 2b2.

  It enumerates all codimension-3 subspaces (RREF dual bases), all 8 cosets (pdep parametrisation), and runs a Möbius affinity test and GF(2) span tests. Swap-reduced wirings are used: all of them for m = 4, a random sample for m = 5.

**Results.**
- **Samples (`hc_sample.txt`).**
  - 770 of 1,084 have an unused gate (gate 3: 553, gate 2: 160, gate 1: 57). For these, MC ≤ 3 is trivial.
  - The other 314 have every gate used, and all of them have top(h₀) = m−1.
  - Every sample with top(h₀) = m−2 has gate m−1 unused.
  - All 531 samples with top(h₀) = m−1 satisfy the merge identity with the predicted input s. For types 1 and 2 the other input fails. The proof only predicts that the named input works and says nothing about the other one (AUDIT-004 I-7).
- **`codim3 4 0`** (exhaustive: 8,640 wirings, 97,155 subspaces; `codim3_m4.log`, 5.3 min on 4 cores):
  - 24,282,232 non-affine cosets C with an affine coset C₀; 18,787,840 of them are Lemma-24-degenerate.
  - dim π = 1: gate j* redundant in 561,600 cases.
  - 2a: last gate redundant in 2,167,708 cases.
  - 2b1: merge identity holds in 1,690,160 cases.
  - 2b2: gate m−1 unused in 1,012,800 cases, last gate redundant in 62,124.
  - **0 violations.**
- **`codim3 5 300 2026`** (a random sample of 300 of the 2,350,080 swap-reduced wirings, against all 6,347,715 codimension-3 subspaces of F₂¹⁰; `codim3_m5.log`, 32 min on 4 cores):
  - 1,839,901 non-affine cosets with an affine C₀; 1,762,553 degenerate.
  - dim π = 1: gate j* redundant in 5,279 cases.
  - 2a: 34,026. 2b1, merge: 21,530. 2b2: 15,649 unused, 864 last gate redundant.
  - **0 violations.**

**Interpretation.** The cycle-002 hard core is explained exactly:
- either a gate is unused;
- or the eliminated variable of the codimension-3 normal h₀ belongs to gate m−1, and then gates m−1 and m merge into one gate R₁·s on C₁.

The exhaustive m = 4 run checks every case of the proof, not only its conclusion. The m = 5 run is a sample: evidence, not proof.

**Reproduce.**
```
gcc -O2 -fopenmp -o hc_dump hc_dump.c && ./hc_dump 5 ../EXP-010-level4-certificates/mc5.mc5 > hc_sample.txt
python3 merge_check.py
gcc -O2 -mbmi2 -fopenmp -o codim3 codim3.c
./codim3 4 0
./codim3 5 300 2026
```
