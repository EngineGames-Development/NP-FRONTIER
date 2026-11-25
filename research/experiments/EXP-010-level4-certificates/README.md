# EXP-010: exact certificates MC(y*g) >= 5 for the 297 representatives

**Question.** Is MC(y*g) = 5 for every EXP-008 orbit representative g (5 variables, MC 4)?

**Method.**
- `build_mc5.c` builds the exact MC table of all 5-variable functions, `mc5.mc5` (4 bits per function, 2 GiB, gitignored), from EXP-007. `mc4.bin` holds the 4-variable table.
- `cert4b.c` is an exact decision procedure for MC(F) <= 4 on 6 variables. The header comment lists its steps. Steps 1 to 3 are necessary conditions from Lemma 9' applied at each level; step 4 is an exact span test.

**Results.**
- All 297 representatives give NONE, i.e. MC(y*g) >= 5 (`all297.log`).
- The 245 degree-4 representatives have 140 admissible planes each; the 52 degree-3 representatives have 620.
- Runtime: 2 to 35 s each.

**Positive controls (must give FOUND), all passed:**
- 60 random circuits from `gen_circuit_controls.py`: 30 random 4-gate circuits on 6 variables (F-mode) and 30 y*g with g from random 3-gate circuits (yg-mode).
- 12 random product trees of degree 5 (`gen_controls.py`).
- y*g* (g* = 0xfff3d212) and y*x1x2x3x4.

**Independent confirmations of the same conclusion:**
- EXP-014, k = 5: an unrelated method.
- EXP-015: NIST's 6-variable classification.

**Reproduce:**
```
gcc -O2 -o build_mc5 build_mc5.c && ./build_mc5
gcc -O2 -o cert4b cert4b.c && ./cert4b yg $(cat deg4_part1.txt)
```
