# EXP-006: the finite check that completes PNE-001 at level 3 (Theorem 16)

**Question.** Theorem 16 reduces "PNE-001 holds for every g with MC(g) ≤ 3" to a finite statement: MC(y·G') = 4 for every G' = x1ℓ1 + x2ℓ2 + x1x2ℓ3 + λ(u) on 5 variables with MC(G') = 3. Here ℓ1, ℓ2, ℓ3 are affine in u = (u1, u2, u3) and λ is linear in u. The constant term is WLOG 0, because MC(y·(G'+1)) = MC(y·G' + y) = MC(y·G').

**Method.**
1. `family.py` enumerates all 16³·8 = 32,768 members, pairwise distinct modulo complement. It merges them into orbits under generators of AGL(2) on (x1,x2) × AGL(3) on u, plus complementation, by union-find. These maps are affine bijections of the input space, so they preserve MC(G') and MC(y·G'). No image leaves the family. Result: **33 orbits**.
2. `run_reps.py` builds S_2, the set of 5-variable functions with MC ≤ 2, exhaustively, as all W2 = W1 + span{A·B} with A, B ∈ W1, over all 155 W1. Then, for each orbit representative:
   - (a) G' ∈ S_2 means MC ≤ 2, so the representative is excluded. Otherwise MC(G') = 3, since MC ≤ 3 by the explicit circuit x1·ℓ3, x2·(ℓ2 + z1), x1·ℓ1.
   - (b) For MC-3 representatives: compute the admissible directions of y·G' by lookups in S_2, then run the exhaustive first-gate extension check over every first gate allowed by Lemma 9 and Lemma 12.

**Validation of the S_2 construction.**
- The same code at n = 4 gives 35 W1 spaces, |S_1| = 1,152 and |S_2| = 32,768, matching the independent span BFS of EXP-001 exactly.
- At n = 5, |S_1| = 9,984 matches the closed form 2^{n+1}·(1 + #2-dim subspaces) = 64·156.
- |S_2| for n = 5 is 1,811,456 (not compared with a published count; none was retrieved).
- The extension code is the one positive-controlled in EXP-004 (x1x2x3·y gives FOUND).

**Results.**
- 31 of 33 orbit representatives lie in S_2, so they have MC ≤ 2.
- 2 have MC = 3: 0x01234567 and 0x0167abcd. Both are certified NONE, i.e. MC(y·G') = 4, with 48 first gates each. This gives **Theorem 17**.
- Cross-check (`run_drat_level3.sh`): CaDiCaL reports UNSAT for "MC(y·G') ≤ 3" on both.
  - The DRAT proof for 0x01234567 is **verified by drat-trim** (643 s; `drat_recheck_0x01234567.log`).
  - The DRAT proof for 0x0167abcd is **verified by drat-trim** (748 s; `drat_recheck_0x0167abcd.log`).
  - Note: drat-trim prints its verdict as `\rs VERIFIED`, so the script's `^s ` filter dropped it. The re-check converts `\r` to newlines.

Logs: `run_reps.log`, `results.json`.
