# EXP-008: level-4 candidates on 5 variables (cheap-plane family F_5)

**Question.** Which members of the family F_5 = { g00(u) + x1 d1(u) + x2 d2(u) + x1x2 d12(u) : deg d_i <= 2 } (2^29 functions; Corollary 21) have MC 4, and how many orbits do they form under the symmetry group of F_5?

**Method.**
- `scan.c` tests every member against the MC <= 3 bitmap of EXP-007 and writes the MC-4 members to `mc4_members.u32` (gitignored).
- `orbits2.c` runs a BFS with a visited bitmap under 11 generators plus complementation: AGL(2) on (x1,x2), AGL(3) on u, and the shears u <- u + N(x1,x2).

**Results.**
- 337,784,832 members have MC 4.
- They form **297 orbits** (`orbit_reps.txt`: representative and size).
- No generator image leaves S_3 or the family.
- `rep_profile.json` lists the degree and number of cheap planes of each representative: 245 have degree 4, 52 have degree 3.

**Use.** PNE-001 for every g on <= 5 variables is equivalent to MC(y*g) = 5 for the 297 representatives (Corollary 21 plus Theorem 17). EXP-010 settles this.
