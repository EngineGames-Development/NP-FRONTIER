# EXP-019: level 5 of PNE-001 — the codimension-4 residue and a class-list filter

**Context.** By Corollary 35 (`research/proofs/PNE-001-codim3.md`), a level-5 counterexample g has dim g = 6. Equivalently, a formal 5-gate circuit, a 6-dimensional K ⊆ F₂¹⁰ (codimension 4) and cosets C₀ ≠ C with Φ|C₀ affine and MC(Φ|C) = 5. Results are written up in `research/proofs/PNE-001-level5.md`.

**Programs.**
- `codim4.c`: samples swap-reduced wirings and takes all 53,743,987 four-dimensional H = K^⊥ in RREF with all 16 cosets. For every non-affine C with an affine C₀, it records the first mechanism certifying MC ≤ 4:
  - DEG: Lemma 24;
  - UNUSED: an unused gate;
  - RED: a triangularly redundant gate;
  - MERGE: Φ|C ∈ V₀ + s·V₀, with s an input of gate 4.

  Anything else is printed as HARD.
- `hard_check.py`: for each distinct HARD function modulo affine, a SAT search for a 4-gate circuit (`EXP-001/mc.py`), with every circuit re-evaluated. A failure would be a level-5 counterexample.
- `hard_struct.py`, `hard_struct2.py`: the H-structure of the HARD instances: dim π(H), H₀, and the top gate and type of the separating and non-separating elements.
- `top1_check.py`: the one-extra-gate test TOP1, Φ|C ∈ L₀ + X·L₀ with X ∈ L₀ and L₀ = span(1, coordinates, z₀, z₁, z₂).
- `decode1.py`: one HARD instance by hand, with its SAT circuit.
- `lemma37_check.py`: brute-force check of the identities in the proof of Lemma 37, including the rank-≤ 2 claim.
- `cheapplane6.c`: Lemma 36(c) applied to NIST's 148,483 representatives of 6-variable MC-5 classes (`usnistgov/circuits/data/mc_dim/mc5_dim6.txt`). The halves are looked up in our exact 5-variable S₃ table (`EXP-010/mc5.mc5`).

**Results.**
- **`codim4 4 7 200`** (4 wirings, seed 7; `codim4_try.txt`, 1.5 min):
  - 934,015 non-affine cosets: DEG 852,576; UNUSED 0; RED by gate 0–4: 0 / 1,440 / 420 / 2,211 / 19,624; MERGE 36,528.
  - **HARD 21,216.**
- **HARD structure** (600 printed instances):
  - All have dim π(H) = 2 and dim H₀ = 2, with different H₀-classes.
  - The non-separating t₂ always has its top gate at m−1.
  - NEW-1 (200): the separating elements also have their top gate at m−1. All pass TOP1, and Lemma 37 proves this sub-case.
  - NEW-2 (400): one separating element has a lower top gate. None passes TOP1.
- **No counterexample in the sample.** All 131 distinct HARD functions modulo affine have verified 4-gate circuits (`hard_check.py`: 1,202 s, at most 126 s per function). The decoded example has MC exactly 4.
- **Class-list filter** (`cheapplane6`, 1.5 min):
  - 35,861 of 148,483 MC-5 representatives have a cheap plane.
  - The degree condition 36(b) removes none of them (degrees 3: 3, 4: 1,702, 5: 34,156).

**Limitations.**
- The codimension-4 sample is tiny (4 of 2,350,080 wirings). It is exploratory, not a proof.
- The class-list filter is conditional on NIST's list being complete and correctly labelled. It also leaves 35,861 × 64 cases (representative + linear form) undecided.

**Reproduce.**
```
gcc -O2 -mbmi2 -fopenmp -o codim4 codim4.c && ./codim4 4 7 200 > codim4_try.txt
python3 hard_check.py codim4_try.txt hard_try.json
python3 hard_struct2.py codim4_try.txt; python3 top1_check.py codim4_try.txt; python3 decode1.py
gcc -O2 -o cheapplane6 cheapplane6.c && ./cheapplane6 /home/user/usnistgov/circuits/data/mc_dim/mc5_dim6.txt ../EXP-010-level4-certificates/mc5.mc5 > cheap_mc5.txt
python3 lemma37_check.py
```
