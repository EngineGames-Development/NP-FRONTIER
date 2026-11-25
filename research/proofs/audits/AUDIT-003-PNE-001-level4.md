# AUDIT-003: PNE-001 at level 4 (Lemmas 9′, 18–24, 26, 28, 30, fact (F4), Corollaries 21, 29, 31, Theorems 25 and 27)

- **Document audited:** `research/proofs/PNE-001-level4.md` at commit `592b9a7` (2026-11-25 19:58 UTC), 336 lines, md5 `26d1d53a27f136e3973c7ac8a75b00ab`.
  - The document changed three times while this audit ran (`be605f9` → `860d771` → `592b9a7` → `26e4dc7`). This audit covers `592b9a7`. Between `be605f9` and `592b9a7` the originally assigned claims are textually unchanged, except the header sentence and the `indep_check.py` bullet of the verification record, which now reports the finished k = 6 run.
  - Commit `26e4dc7` (20:06 UTC) then added 17 lines of data to "Observations" (the codimension-3 "hard core" table). They state no claim and were not audited.
  - Added during the audit and included at the coordinator's request: Lemma 28, Corollary 29, Lemma 30 with (IF′), Corollary 31, the paragraph "Structured proof of Theorem 25", the section "Observations toward a general proof", EXP-016, `EXP-014/lemma30_check.py`, and `research/proofs/lean/NPFrontier/Circuit.lean`.
- **Auditor:** Agent F (adversarial reviewer), fresh context, 2026-11-25.
- **Taken as given** (audited in AUDIT-001/002): Lemmas 1–17 of `PNE-001-restriction-depth-and-fresh-variables.md`, in particular Lemma 9, Lemma 11 (Case C identity) and Theorem 17.
- **Read:** the whole document; `EXP-014/formal4.c`, `formal4_full.c`, `formal4_k5nd.c`, `formalm.c`, `test_affine.c`, `triage.py`, `triage_full.py`, `triage_lib.py`, `indep_check.py`, `mc3_check*.py`, `lemma30_check.py`, README and logs; `EXP-015/nist_hyperplane_check.py`, `nist_level_check.py`, `check_mc5_vs_nist.py`, README and log; `EXP-016/hyper.c`, README and log; `EXP-001/mc.py`; READMEs and logs of EXP-007, EXP-008, EXP-010 and the header of `build_mc5.c`; `research/proofs/lean/NPFrontier/Circuit.lean`, `Axioms.lean` and the Lean README; `research/literature/mc-peralta-2016-nist-email-fresh-variable.md`; the novelty and status lines of `cycles/cycle-002.md`, `current_state.md` and `hypotheses/PNE-001-fresh-variable-lemma.md`.
- **Not read:** EXP-008 `orbits2.c`, EXP-010 `cert4b.c`, EXP-007 `s3.c` (only headers, READMEs and logs), `redundancy.py`, `lastgate.py`, `formal4_k5red.c`, `formal4_k5case.c`, EXP-017.
- **Executed.** No repository file was edited. Author programs were rebuilt from the committed sources into a scratch directory and run there; Python scripts that only read data were run in place with `python3 -B`. Everything in §3 marked "own code" was written by me and shares no code with the project. The load-bearing programs are reproduced in Appendix A.

## Verdicts

| Claim | Verdict |
|---|---|
| Lemma 9′ | SURVIVES |
| Lemma 18 | SURVIVES (cosmetic I-9) |
| Lemma 19 | SURVIVES |
| Lemma 20 | SURVIVES |
| Corollary 21 and the F_5 symmetry group | SURVIVES |
| Notation `dim f`, fact (F4) | SURVIVES |
| Lemma 22 (a), (b), (c) | SURVIVES. (a) is known, attribution confirmed from abstract-level sources |
| **Lemma 23** (both directions, `dim K ∈ {5,6,7}`, swap reduction `α_i ≤ β_i`) | **SURVIVES** |
| Lemma 24 | SURVIVES (cosmetic I-8) |
| **Theorem 25** | **SURVIVES.** All reported counts reproduced exactly, and re-proved by an independent enumeration with an explicit, evaluated 3-gate circuit for every coset pair, for all 32,768 wirings (V-2, V-3) |
| Lemma 26 | SURVIVES |
| EXP-015 claims (class list use, 32-linear-form reduction, fingerprint test) | SURVIVES (minor I-4) |
| Theorem 27 | SURVIVES WITH CORRECTIONS (I-1, I-2) |
| Lemma 28 and Corollary 29 | SURVIVES |
| Lemma 30, (IF′) and Corollary 31 | SURVIVES |
| "Structured proof of Theorem 25" | SURVIVES WITH CORRECTIONS (I-3: circular citation as written) |
| "Observations toward a general proof" | Data only. The codimension-2 figures are reproduced exactly (V-9) |
| EXP-016 (m = 5 hyperplane enumeration) | SURVIVES (see V-8) |
| `Circuit.lean` | SURVIVES: builds with `--wfail`, only standard axioms, statements match their stated use (V-11) |
| Scope and novelty statements | No overclaim found. One passage is stale (I-5) |

No fatal or serious finding. All issues are minor, cosmetic or informational. No counterexample to Theorem 25, to Lemma 23 or to Lemmas 28 and 30 was found.

## 1. Claim-by-claim review

### Lemma 9′ (strong first-gate criterion)
- Optimality excludes a constant input and equal linear parts (otherwise the first gate is affine and can be substituted away).
- On `⟨u1+u2,x⟩ = c`, b = a + (c + e + e′), so ab ∈ {0, a}. All three directions kill the first gate, and (F2) gives m − 1 gates. Correct.

### Lemma 18 (MC ≤ 2) and Lemma 19 (derivatives)
- (⇐) Both circuits are correct. (⇒) I re-derived the three cases. In the "both contain z1" case, AB = z1(1+α+β) + αβ and αβ = αℓ + c1α (with ℓ = 1 + c1 + α + β, α² = α), so f = ℓ(ab+α) + c1α + λ. Correct.
- Lemma 19: D_e(ℓq) = ℓδ + εq + εδ with δ = D_e q affine. The case split and the rank bound (rank(ℓδ) ≤ 2, rank(q) ≤ 2) are correct.
- The remark "top-degree part ℓ_lin a_lin b_lin" is imprecise (I-9).

### Lemma 20 and Corollary 21
- e_y is not admissible (F|_{y=1} = g has MC 4). If v1 = v2, then u1 + u2 = e_y, which Lemma 9′ makes admissible: contradiction. So v1, v2 are independent.
- For admissible (v,s) with v ≠ 0, both halves satisfy MC(t·g|) ≤ 3 by the Lemma 11 identity. Non-constant halves then have MC ≤ 3, and Theorem 17 gives MC ≤ 2. Correct.
- d2 = D_{x2}H0 and d2 + d12 = D_{x2}H1. d1 and d1 + d12 come from the x2-split, so deg d12 ≤ 2 as well. Correct.
- F_5 has 2^8·(2^7)^3 = 2^29 members. I checked that translations and GL(2) on (x1,x2), AGL(3) on u, the shears u ← u + N(x1,x2) and complementation map F_5 into itself; for the shears, the new coefficients are derivatives of degree ≤ 2 functions or of g00, of degree ≤ 2. Each preserves MC(g) and MC(yg).
- Spot checks of `EXP-008/orbit_reps.txt`: 297 representatives, sizes summing to 337,784,832, all of table-MC 4, all in F_5 (x1, x2 = bits 0, 1). The orbit BFS and `cert4b` were not re-run (§4).

### Notation, (F4)
- The equivalence of the two definitions of `dim f` is correct: v ↦ D_v f is linear on V(f) because D_{u+v}f(x) = D_v f(x+u) + D_u f(x).
- (F4) is correct; the ≥ direction needs an affine section, which exists for every affine surjection over F_2.

### Lemma 22
- (a) The span of the 2m linear parts of the gate inputs contains every gate's dependence on x, so f = λ + h(≤ 2m forms). Correct. The bound MC ≥ ⌈dim/2⌉ is stated in the abstract of Çalık–Sönmez Turan–Peralta (Cryptogr. Commun. 12, 2020; ePrint 2019/1364), as seen in search snippets of the NIST page and a library catalogue (retrieved; full text not read).
- (b) w_y = 1 forces g constant. For w_y = 0, D_wF = y·D_{w_x}g is constant only if it is 0. So V(F) = P(g) × {0}, with P(g) of codimension ≤ 1 in V(g). Correct.
- (c) Correct. For a quadratic of symplectic rank 2s, V(g) is the radical, so dim g = 2s; Dickson's normal form gives MC ≤ s and (a) gives MC ≥ s.

### Lemma 23 (formal-circuit reformulation)
I re-derived both directions and checked every point in the brief.
- **Constants.** The constants c_t of the real gate inputs become the coset offset (C0 = K + c), and all 2^{8−k} cosets of every K are enumerated.
- **Affine output part.** F = λ + Φ(w(x,y)+c). At y = 0 this gives Φ ∘ (affine surjection onto C0) = λ(·,0). By (F4) via a section this is equivalent to Φ|_{C0} being affine. Conversely, (2⇒1) adds μ = Φ(Tx+c) at the output. So "Φ|_{C0} affine" is exactly the right condition: necessary and sufficient.
- **Unused gates.** γ′_m = 1 is forced by MC(F) = m. Unused earlier gates are ordinary formal wirings and do no harm.
- **Degenerate or dependent linear parts.** The map w = (ℓ_1, …, ℓ_N) is an arbitrary linear map. Zero, equal or linearly dependent forms only change K = w(F_2^n × {0}), and every subspace is enumerated. The y-coefficients go into δ = w(0,1), and δ ∉ K because g is not affine.
- **Range of dim K.** MC(Φ|_{C1}) = MC(g) = 4 needs dim K ≥ 5, since every 4-variable function has MC ≤ 3 (EXP-001; AUDIT-002 V-2). C0 ≠ C1 forces dim K ≤ 7.
- **(2⇒1).** m ≤ MC(G) ≤ MC(yG) ≤ m, so G is a level-m counterexample.
- **Swap symmetry.** Φ′ = Φ ∘ σ_i holds by induction over the gates, and it holds simultaneously for any set of swapped gates. Subspaces and cosets map bijectively. My independent run (V-2) uses all 32,768 wirings and does not depend on this reduction; its swap-reduced subtotals equal the reported numbers.

### Lemma 24 (degenerate gates)
Correct. If α_i = 0 and w_{2i−1} vanishes on K, then A_i is constant on each coset and z_i ∈ {0, B_i}. Case (c) gives z_i = (1+ε)A_i. Case (b) is symmetric but is not written out (I-8). The gate-elimination step is formalized as `Circuit.elim_left/right/xor` (V-11).

### Theorem 25
- The logical reduction is: no level-4 counterexample exists ⇔ for every wiring, every K with dim K ∈ {5,6,7}, and every pair C0 ≠ C1 with Φ|_{C0} affine, MC(Φ|_{C1}) ≤ 3. That is exactly what was computed.
- Code review (formal4.c and variants):
  - RREF enumeration with pivot = lowest set bit gives distinct subspaces, and the counts are the Gaussian binomials, so it is complete.
  - In `precompute`, testing `q` instead of the running representative is correct, because RREF basis vectors vanish at the other pivots.
  - The Möbius-based affinity test (k = 7 across two words) is correct.
  - The wiring loops give 3·10·36·8 = 8,640 wirings.
  - Pairs are counted as (#affine)·(#non-affine), and C1 ranges over every non-affine coset.
  - The k = 5 lookup is convention-free, because MC is invariant under permutations of variables. I confirmed the table against my own search on 12 random functions (V-5).
- Degeneracy tests:
  - `triage.py`/`triage_lib.py`: gate g uses bits 2g, 2g+1; "vanishes on K" means the bit is 0 in every basis vector.
  - `formal4_k5nd.c`: `orb` is the OR of the basis vectors; `eqm` bit 2i records b_{2i} = b_{2i+1} for every basis vector.
  - `indep_check.py`: e_t lies in span(H) for H = K^⊥.
  - All three match Lemma 24 with the correct bit conventions, and my independent implementation in another coordinate convention reproduces their degenerate counts exactly (V-2).
- Deduplication modulo affine functions is sound. It is also conservative, because it does not quotient by coordinate changes.
- All SAT answers are verified circuits: I re-evaluated all 2,542 stored circuits with my own evaluator (V-4).

### Lemma 26 and EXP-015
- Lemma 26 is correct in both directions. Φ(E) ≠ F_2^d because otherwise R would be affine; Φ(E) is then an affine hyperplane H, Φ({y=1}) = H^c, and (F4) transfers affinity and MC. The condition is invariant under affine equivalence.
- If a representative were given on more variables than its dimension, checking all hyperplanes of the larger space would still cover everything. In fact every listed representative has exactly its stated dimension (asserted in the script; also checked in V-6).
- 32-linear-form reduction (`nist_level_check.py`):
  - Write g = g0∘T + ℓ + c. Then (y·(g0 + ℓ∘T^{-1}))∘(T × id) = y·(g0∘T + ℓ).
  - ℓ∘T^{-1} = ℓ′ + c′ with ℓ′ linear, and y·c′ is linear, hence free.
  - Testing y(g0 + ℓ′) for all 32 linear ℓ′ is therefore complete. The counts are 17·32 = 544 (MC-3 classes of dimension ≤ 5) and 26·32 = 832.
- Fingerprint test: the logic is sound as used ("different fingerprint ⇒ not equivalent"), with a caveat about the invariance claim (I-4).
- Both EXP-015 routes rest on NIST's list being complete and its MC labels being correct, as the document says. For dimension ≤ 6 the list has 943 + 148,483 + 931 = 150,357 classes, which matches the known number of affine classes of 6-variable functions. That count supports completeness in dimension ≤ 6, but not the MC labels. Nothing comparable checks the MC-4 lists of dimension 7 and 8.

### Theorem 27 (all g on ≤ 5 variables)
- The main proof is correct: by Theorems 17 and 25, once every 5-variable function has MC ≤ 4.
- That bound is not established by EXP-007, which is cited for it. EXP-007 computes S_3 only, and `build_mc5.c` sets MC = 4 by default for every function outside S_3 (I-2). The bound itself holds:
  - it is the published Sönmez Turan–Peralta result;
  - I found and verified a 4-gate circuit for each of NIST's 26 MC-4 classes of dimension 5, and a ≤ 3-gate circuit for each of the other 22 classes (V-6).
- Confirmation 1 (structural route) depends on EXP-007's S_3 and the table derived from it; I did not re-run it.
- Confirmation 2 (EXP-014 with dim K = 5) is independent of the table only in its table-free form (Lemma 24 plus SAT); the table form shares EXP-007 with confirmation 1. So "mutually independent" needs qualification (I-1).
- Confirmation 3 (`nist_level_check.py`) was re-run: 544 and 832 functions, 0 collisions. The claim "our 5-variable table agrees with NIST's MC for all 48 classes, 200,000 invariance tests" was re-run with the same result.
- Open discrepancy s_5: NIST's constant is exactly (63/31)·775,728,128 (I-7). It is larger than the number of 5-variable functions with MC ≤ 3, so it is not a count of 5-variable functions of MC 3. This points to a different normalization rather than an error in the table.

### Lemma 28 and Corollary 29
- Independence fact: correct. The monomial w_{2j*−1}w_{2j*} occurs only in z_{j*}, with coefficient 1, because gates j < j* read only w_1, …, w_{2j}.
- Case analysis: correct.
  - (i) If h involves neither u nor v, D_uD_v(Φ|_H) = 1.
  - (ii) If h involves u only, D_v(Φ|_H) = c + ⟨h′,w″⟩ + α_m·z, with w″ free. It is constant only if α_m = 0 (independence fact) and h′ = 0.
  - (iii) The case of v only is symmetric.
  - (iv) If h involves both, D_u(Φ|_H) = 1 + a + b′ forces α_m = β_m and h″ = 0.
- Corollary 29: dim g ≤ dim K because g = Φ|_{C1}∘(affine surjection) + affine. dim g = 2m − 1 forces a hyperplane K, and Lemma 28 with Lemma 24 then gives MC(g) ≤ m − 1. Correct.
- The case MC(g) = 0 is outside Lemma 23 (m ≥ 1) but trivial (I-10).
- Tested at m = 4, 5, 6 with my own code (V-7, V-8).

### Lemma 30, (IF′) and Corollary 31
I checked every case.
- **(IF′).** If h0 has support beyond coordinate 2j*, then E projects onto F_2^{2j*}. Ψ|_E affine would then make Ψ affine on F_2^{2j*}, by (F4) through a section, which contradicts the independence fact. Otherwise E = E′ × F_2^{rest}, and Lemma 28 applies to the j*-gate formal circuit with output Ψ. Correct.
- **dim π(H) = 0.** u and v are free on C0, and D_uD_v = 1. Impossible. Correct.
- **dim π(H) = 2.** I re-expanded Φ|_C − Φ|_{C0} = (c1+d1)Q + (c2+d2)P + c1c2 + d1d2. This matches the document's form. Since gates 1, …, m−1 read only w″, Φ|_C lies in span(affine, z_1, …, z_{m−1}) on C. Correct.
- **dim π(H) = 1.**
  - In sub-case (1,0) with α_m = 0, h1″ ∈ span(h0″), so e_u ∈ H and Lemma 24(a) applies to gate m.
  - With α_m ≠ 0, Ψ = α_m·z is affine on E0, so (IF′) applies, and h0 = (h0″,0,0) ∈ H makes gate j* degenerate for K.
  - Sub-case (1,1) is analogous, with α_m + β_m. Sub-case (0,1) is symmetric.
  - Correct for every m ≥ 1; for m = 1, K = 0 and every coset is a point.
- **Corollary 31.** Follows from Lemmas 28 and 30, since dim g ≤ dim K ≤ 2m − 1. Correct.

### "Structured proof of Theorem 25"
- The reduction is correct. Corollary 31 gives dim g ≤ 5, so g = h(x1..x5) + εx6 + c in suitable coordinates. Restricting x6 (and any dummy variables) to 0 gives a 5-variable g′ with MC(g′) = MC(g) = 4 and MC(yg′) ≤ MC(yg) = 4. That is a level-4 counterexample on 5 variables.
- As written it cites Theorem 27 to exclude g′, and Theorem 27's proof is "a special case of Theorems 17 and 25". That is circular. The non-circular reading, which the next sentence also gives, uses the 5-variable computations directly (I-3).
- Each such computation suffices on its own:
  - EXP-014 with dim K = 5 (table-free form). I re-verified this independently (V-2, V-3).
  - EXP-015 `nist_level_check.py`, given NIST's 6-variable classification.
  - EXP-010, given EXP-007.
- Data check (`lemma30_check.py`): see V-9 for my own tally.

### "Observations toward a general proof"
- The section states data and no claims. I reproduced the codimension-2 figures independently (V-9). I did not reproduce the codimension-3 figures (`formal4_k5red.c`), but my own gate-removal certificate gives a consistent picture: at dim K = 5, 1,007,061 swap-reduced pairs (4,660,001 over all wirings) cannot be certified by removing one gate of the given circuit, yet all of them have other 3-gate circuits (V-3).
- The "Lesson" bullet is an interpretation, not a theorem. It is consistent with the data.

### Scope, novelty and literature
- No overclaim found. The document says that nothing bears on P vs NP beyond this restricted measure, that PNE-001 is open in general, and that novelty is unconfirmed. It records the 2016 NIST email, in which Peralta states MC(uv·f) = 1 + MC(v·f), the special case h = v·f, with a proof attachment that is not public.
- My searches found no published statement of the general fresh-variable lemma, and no statement of the level-4 results. Sources seen (search results only; no full texts read):
  - Çalık, Sönmez Turan, Peralta, "Boolean functions with multiplicative complexity 3 and 4", Cryptogr. Commun. 12 (2020) 935–946, ePrint 2019/1364 (https://eprint.iacr.org/2019/1364; https://www.nist.gov/node/1631526). Abstract-level content: MC ≥ ⌈dim/2⌉, 24 MC-3 classes, 1,277 MC-4 classes. Retrieved.
  - Çalık, Sönmez Turan, Peralta, "The multiplicative complexity of 6-variable Boolean functions", ePrint 2018/002 (https://eprint.iacr.org/2018/002). Content: 150,357 affine classes, 931 with MC 6. Retrieved.
  - The FOIA release containing the 2016 email (https://nist.pqcrypto.org/foia/20230815/) appeared in a search result. I did not open it.
- The "Limits" section is partly stale relative to the new header (I-5).
- Barriers: these are statements about one restricted measure at constant levels, plus a reformulation that is finite for each fixed level. Relativization, natural proofs and algebrization do not apply. Nothing contradicts known results: the maximum MC on 5 variables is 4, and the results are consistent with NIST's 6-variable classification and its MC-3/MC-4 class lists.

## 2. Issues

**I-1. Theorem 27, "three further, mutually independent confirmations". Severity: minor (wording).**
- Confirmation 1 (EXP-008 and EXP-010) uses EXP-007's S_3: it finds the MC-4 members of F_5 with the S_3 bitmap, and `cert4b` uses `mc5.mc5`.
- Confirmation 2 is "the dim K = 5 case of EXP-014". In its table form it reads the same `mc5.mc5`.
- The confirmations are independent only if 2 means the table-free variant (`formal4_k5nd` plus SAT). The document should say so.

**I-2. Theorem 27, "Every 5-variable function has MC ≤ 4: by EXP-007". Severity: minor (unsupported citation; the statement is true).**
- EXP-007 computes S_3 only. `build_mc5.c` sets the default MC to 4 for every function outside S_3 ("default MC = 4"), so the table's value 4 is an upper bound taken from the literature, not computed.
- The bound is the published result of Sönmez Turan–Peralta (recalled; AUDIT-002 saw it in search snippets).
- Independent support (V-6):
  - all 26 NIST classes of dimension 5 with MC 4 have 4-gate circuits, found by SAT and verified by my evaluator;
  - all 22 classes of MC ≤ 3 and dimension ≤ 5 have ≤ 3-gate circuits, found and verified by my code.
- Together with the classification of 5-variable functions into 48 affine classes, this gives MC ≤ 4 for all of them.

**I-3. "Structured proof of Theorem 25". Severity: minor (circular citation as written).**
- It excludes the 5-variable g′ by "Theorem 27". Theorem 27's own proof is "a special case of Theorems 17 and 25".
- The intended, non-circular argument is in the next sentence: the 5-variable computation. The proof should cite one of the following directly:
  - EXP-014 with dim K = 5 in table-free form;
  - EXP-015 `nist_level_check.py`, conditional on NIST's 6-variable classification;
  - EXP-010 together with EXP-007.
- No logical gap remains once the citation is changed. V-3 independently confirms the dim K = 5 computation.

**I-4. EXP-015 fingerprint, "affine-invariant". Severity: minor (false as a general statement; harmless here).**
- The fourth component, the multiset of `anf_deg(D_v F)` with `anf_deg(0) = −1` and `anf_deg(1) = 0`, is not invariant under adding linear functions when F has a constant derivative. Example: x1x2 and x1x2 + x3, both on 3 variables, have derivative degrees −1 and 0 in direction e_3.
- The self-test uses 30 random 6-variable functions. These have no constant derivatives, so the test cannot detect the problem.
- Why the conclusion still holds:
  - every constant derivative of F = y·g is 0 (proof of Lemma 22(b));
  - every NIST representative of MC ≤ 4 and dimension ≤ 6 has exactly its stated dimension and no derivative equal to the constant 1 (checked, V-6);
  - if F ~ R, both multisets therefore contain −1 at exactly the corresponding directions.
- So a fingerprint mismatch still proves non-equivalence for the functions tested. The docstring and the Theorem 27 text should restrict the invariance claim, or the component should identify degrees −1 and 0.

**I-5. "Limits and what remains". Severity: cosmetic (stale).**
- The section still says that correctness "rests on the reformulation (Lemma 23) and on the enumeration code", with "two independent routes".
- The header now says "human reduction to 5 variables (Lemmas 23, 28, 30) plus a 5-variable computation done three ways".
- "No human-readable proof of level 4 is known" is still true, since the 5-variable step is computational. The section should be updated to match.

**I-6. Verification record, "The optimized and the direct restriction code produce identical dim K=7 output". Severity: cosmetic (provenance).**
- The direct variant is not committed. `restrict_tab` is dead code in `formal4.c` and its variants. Only its output `out_k7b.txt` exists; it equals `out_k7.txt` after sorting (checked).
- The claim cannot be reproduced from the repository. V-2 makes it moot.

**I-7. Open s_5 discrepancy (Theorem 27 paragraph). Severity: informational.**
- 1,576,479,744 = (63/31) · 775,728,128 exactly, i.e. 63 · 25,023,488.
- It exceeds |S_3| = 779,571,200, so it is not a count of 5-variable functions of MC 3.
- The exact factor (2^6 − 1)/(2^5 − 1) suggests a Gaussian-binomial normalization in the slide's formula. It is not evidence against the table, which agrees with NIST class by class. The slide was not seen by me.

**I-8. Lemma 24 proof. Severity: cosmetic.** Case (b) is omitted (it is symmetric to (a)).

**I-9. Lemma 18, second remark. Severity: cosmetic.** "Top-degree part ℓ_lin a_lin b_lin" should read "the degree-3 component of ℓ_lin a_lin b_lin", because over F_2 the product of three linear forms has lower-degree terms (compare AUDIT-002 I-1).

**I-10. Corollaries 29 and 31 at MC(g) = 0. Severity: informational.** Lemma 23 is stated for m ≥ 1. For non-constant affine g the claim (MC(yg) = 1) holds trivially, so nothing is lost; the proofs simply do not cover m = 0.

**I-11. Latent buffer overflow in `gen_subspaces`. Severity: informational.**
- In `formal4.c` and `formalm.c` the subspace buffer holds 200,000 entries, but [8 choose 4]_2 = 200,787.
- No reported run reaches this case: `formal4` takes k ∈ {5,6,7}, and `formalm` runs only with M ≤ 3 (D ≤ 6), or with M = 4 and k ≥ 5.
- It would bite any future run with D = 8 and k = 4.

**I-12. Lean README. Severity: cosmetic.** The "not formalized" list predates Lemma 30 and Corollary 31.

## 3. What I verified, and how

**V-1. Re-runs of the authors' programs** (rebuilt from the committed sources; outputs in scratch). Every reported number was reproduced exactly.

| Program | Result |
|---|---|
| `test_affine` | 1,400,000 tables, 0 mismatches |
| `formal4 7` | 255 subspaces, 1,020 affine cosets, 840 pairs |
| `formal4 6` | 10,795 subspaces, 297,128 / 509,220 |
| `formal4 5` | 97,155 subspaces, 17,467,504 / 66,989,104. Table MC distribution 1: 23,017,648; 2: 27,492,928; 3: 16,478,528; 4: 0 |
| `formal4_full 7` | 3,072 / 2,688 |
| `formal4_full 6` | 908,800 / 1,663,872 |
| `triage.py` | k = 7: 840 degenerate. k = 6: 489,576 degenerate, 19,644 non-degenerate, 72 distinct (degrees 2: 4, 3: 16, 4: 52). `nondeg_k6.txt` byte-identical |
| `formal4_k5nd 5` | 9,588,720 non-degenerate pairs, 2,142 distinct. `nondeg_k5.txt` identical |
| `formalm` | M = 2 (k = 2, 3) and M = 3 (k = 4, 5): 0 counterexamples |
| `nist_hyperplane_check.py 4` | 1,277 representatives, 186 hits, 0 counterexamples |
| `nist_level_check.py` | 943 classes (901 distinct fingerprints); 544 and 832 functions, 0 collisions |
| `check_mc5_vs_nist.py` | 48 classes, 0 mismatches; 200,000 invariance tests, 0 violations |
| EXP-016 `hyper 4` | 1,020 / 840, all degenerate |

Sorted outputs `out_k7.txt`, `out_k6.txt` and `out_k6_full.txt` are identical to the committed ones (md5). `mc3_check.py` (k = 6) was re-run in scratch and again found a re-evaluated 3-gate circuit for all 72 functions (2 min). The k = 5 SAT run (691 s) was not repeated; its circuits were re-verified instead (V-4).

**V-2. Independent enumeration (own code, `ic_enum.c`, Appendix A).**
- *Design*, deliberately different from EXP-014:
  - gate i reads formal coordinates i and 4+i, not 2i and 2i+1;
  - subspaces are generated by BFS closure from {0} and deduplicated by their 256-bit membership sets, with no RREF;
  - the basis is chosen greedily, and the base point is the least point of each coset;
  - affinity of Φ on a coset is tested by checking that D_bΦ is constant on the coset for each basis vector b. This is a derivative test, not a Möbius transform;
  - all 32,768 wirings are enumerated; the swap-reduced subset is tallied separately.
- Subspace counts by closure: 255, 10,795, 97,155, 200,787, 97,155, 10,795, 255 (dimensions 1–7), equal to the Gaussian binomials.
- Results, all wirings and swap-reduced:

| dim K | affine C0-cosets (all / reduced) | pairs (all / reduced) | Lemma-24 degenerate (all / reduced) |
|---|---|---|---|
| 7 | 3,072 / 1,020 | 2,688 / 840 | 2,688 / 840 |
| 6 | 908,800 / 297,128 | 1,663,872 / 509,220 | 1,591,296 / 489,576 |
| 5 | 55,592,448 / 17,467,504 | 229,201,152 / 66,989,104 | 192,647,040 / 57,400,384 |

- Every reported figure is reproduced exactly: all three reduced columns, the k = 6, 7 all-wiring columns, and 72,576 = 1,663,872 − 1,591,296 non-degenerate pairs at k = 6 over all wirings.

**V-3. An explicit, evaluated 3-gate circuit for every pair (own code).**
- For each pair, ic_enum first tries to delete one gate i of the given circuit on C1, using the substitutions of Lemma 24 (a), (b), (c), or z_i ↦ 0. It builds the resulting XOR-AND circuit over the wires (1, t_1..t_k, z′_1..z′_3) as explicit masks and evaluates it generically on all 2^k points of C1.
  - A certificate is accepted only if the evaluation equals Φ|_{C1}. Its correctness therefore does not depend on my own degeneracy test.
  - Every Lemma-24-degenerate pair was certified (counted explicitly: 0 exceptions at k = 5, 6 and 7).
- Pairs not certified this way were reduced modulo affine functions and deduplicated. Each distinct function then went to my own circuit search, `ic_search.c` (Appendix A). The search uses an exhaustive first and second gate and, for the third gate, the bilinearity of (C,D) ↦ CD mod W2. Each circuit found is turned into explicit masks, its output mask is found by brute force, and it is re-evaluated point by point.

| dim K | pairs (all wirings) | certified by deleting one gate | remaining pairs | distinct mod affine | circuit found and verified |
|---|---|---|---|---|---|
| 7 | 2,688 | 2,688 | 0 | 0 | — |
| 6 | 1,663,872 | 1,656,268 | 7,604 | 283 | 283 / 283 (142 s) |
| 5 | 229,201,152 | 224,541,151 | 4,660,001 | 12,261 | 12,261 / 12,261 (2 × 970 s) |

- **Conclusion.** For all 32,768 formal 4-gate circuits, all K with dim K ∈ {5,6,7}, and all pairs C0 ≠ C1 with Φ|_{C0} affine, MC(Φ|_{C1}) ≤ 3. Each case has an explicit verified circuit.
- This check uses neither the swap reduction, nor the 5-variable table, nor SAT, nor the authors' degeneracy test. With Lemma 23 it proves Theorem 25 independently of EXP-014.
- Search validation:
  - AND4 found; AND5 correctly not found (exhaustive);
  - 40 random 3-gate circuits on 5 variables and 15 on 6 variables all found;
  - on 12 random 5-variable functions the search agrees with `mc5.mc5` (10 with MC 4 and no circuit, 2 with MC 3 found).

**V-4. Stored SAT circuits (own evaluator).**
- Re-evaluated every circuit in `mc3_check.json` (72), `mc3_check_full.json` (160), `mc3_check_k5.json` (2,142) and `indep_mc3_check_k6.json` (168).
- All are well-formed 3-gate circuits that compute the stated tables. Each file covers its source list exactly: `nondeg_k6.txt`, `nondeg_full_k6.txt`, `nondeg_k5.txt` and `indep_nondeg_k6.txt`.

**V-5. The k = 5 table and my search agree** on 12 random functions and on 10 planted MC-4 samples (V-10). On the 48 NIST classes of dimension ≤ 5, both agree with NIST's labels: `check_mc5_vs_nist.py` checks the table, and V-6 checks my search. So the authors' table route and my table-free route give the same answers where they overlap.

**V-6. NIST route (own code).**
- My own Lemma-26 scan of all 1,277 MC-4 representatives finds the same 186 affine hyperplane restrictions (47, 86, 46 and 7 in dimensions 5–8).
- My search finds a verified 3-gate circuit for all 186 complementary halves, which have 4 to 7 variables.
- All NIST representatives of MC ≤ 4 and dimension ≤ 6 have exactly their stated dimension and no derivative equal to the constant 1 (relevant to I-4).
- For dimension ≤ 6 the class counts add up: 943 + 148,483 + 931 = 150,357. That is the published number of affine classes of 6-variable functions (search snippets of ePrint 2018/002; retrieved), and the 931 MC-6 classes agree with the same source.
- For I-2:
  - each of the 26 MC-4 classes of dimension 5 has a 4-gate circuit, found by `mc.py` SAT and verified by my evaluator;
  - each of the 22 classes of MC ≤ 3 and dimension ≤ 5 has a ≤ 3-gate circuit, found and verified by my search.
- Conversely, my exhaustive search finds no 3-gate circuit for any of the 26 MC-4 classes of dimension 5. So NIST's MC-4 labels in dimension 5 are confirmed independently.

**V-7. Lemmas 28 and 30 at m = 4, 5, 6: random wirings, all hyperplanes and all codimension-2 subspaces (own code, `lem2830.c`, Appendix A).**
- For each random wiring, the program tests every hyperplane (both cosets) and every 2-dimensional dual space H (all four cosets of K = H^⊥) for an affine coset. Wirings are biased so that α = 0 and α = β occur often.
  - Codimension 1: Lemma 28's exact conclusion is checked, namely that the last gate is degenerate for ker h.
  - Codimension 2: Lemma 30's case analysis is checked. Either some gate is Lemma-24-degenerate for K, or on every coset C, Φ|_C ∈ span(1, local coordinates, z_1|_C, …, z_{m−1}|_C), tested by Gaussian elimination.

| m | wirings | affine hyperplane cosets / violations | (wiring, K) with an affine coset, codim 2 | degenerate | last gate redundant on all cosets | violations |
|---|---|---|---|---|---|---|
| 4 | 200 | 46 / 0 | 5,273 | 5,135 | 138 | 0 |
| 5 | 1,500 | 138 / 0 | 61,468 | 61,160 | 308 | 0 |
| 6 | 40 | 1 / 0 | 2,079 | 2,071 | 8 | 0 |

- The m = 5 and m = 6 rows go beyond anything computed by the authors for codimension 2. They are samples, not proofs; the proofs themselves were checked by hand in §1.

**V-8. EXP-016.** `hyper.c` was read and found correct:
- the bit-sliced restriction to {⟨h,p⟩ = c} along the pivot q, the cross-word Möbius transform for D = 10, the bijective (a ≤ b) wiring decoder, and the degeneracy test h ∈ {e_{2i}, e_{2i+1}, e_{2i}+e_{2i+1}};
- `hyper 4` reproduces 1,020 / 840, all degenerate;
- my re-run of `hyper 5` (2,350,080 swap-reduced wirings × 1,023 hyperplanes, 22 min) reproduces `hyper_m5.log` exactly: 71,280 affine cosets, 64,800 pairs, all degenerate, 0 non-degenerate.
- The "degenerate" test in `hyper.c` checks Lemma 28's conclusion for some gate. My V-7 checks the sharper claim that the last gate is degenerate.

**V-9. Lemma 30 data check and the codimension-2 "Observations" (own code, `lem30_exh.c`, Appendix A).** Exhaustive over all 32,768 wirings and all 10,795 codimension-2 subspaces, in my own coordinates:

| | all 32,768 wirings | swap-reduced (8,640) |
|---|---|---|
| pairs (C0 affine, C1 not) | 1,663,872 | 509,220 |
| case dim π(H) = 0 | 0 | 0 |
| case dim π(H) = 1 | 903,168, predicted gate degenerate in all; gates 1–4: 101,376 / 50,688 / 25,344 / 725,760 | 274,536, all predicted gates degenerate |
| case dim π(H) = 2 | 760,704, last gate redundant on C1 in all | 234,684, all redundant |
| non-degenerate pairs | 72,576, all with redundant last gate | 19,644, all with redundant last gate |
| degenerate pairs whose last gate is not redundant | 129,024 | 34,736 |

- Every figure in the structured-proof data check (760,704; 903,168 = 101,376 + 50,688 + 25,344 + 725,760; case 0 never) is reproduced exactly.
- So are the two codimension-2 "Observations" (19,644 and 34,736, swap-reduced).
- Here the "predicted gate" is the one Lemma 30's proof names: gate m if the relevant coefficient vector is 0, otherwise gate j* = max of its support. "Redundant" is tested as Φ|_{C1} ∈ span(affine, z_1, z_2, z_3)|_{C1}, which is equivalent to the document's test z_4|_{C1} ∈ span(…).

**V-10. Planted tests: would the pipeline notice an MC-4 restriction?**
- *Weakened C0 condition* (Φ|_{C0} of degree ≤ 2 instead of affine; every 16th wiring, which means γ = 0 and β_4 even; dim K = 5):
  - 637,214,464 pairs; my certificate stage certifies 629,631,340 of them;
  - the table (`mc5.mc5`) assigns MC 4 to none of the C1 restrictions.
  - So even this weaker condition produced no MC-4 restriction on that subset. This is an observation, not a claim: it suggests the C0 condition has slack. It is not a detection test.
- *No C0 condition* (every coset may serve as C0; every 64th wiring, i.e. γ = 0 and β_4 = 0; dim K = 5): 2,717,570,688 (C0, C1) pairs over 388,224,384 C1 cosets.
  - `mc5.mc5` assigns MC 4 to the C1 restriction in 308,281,344 pairs. My certificate stage certifies none of them.
  - Ten sampled MC-4 restrictions, including AND5, went to `ic_search`, and the exhaustive search found no 3-gate circuit for any of them.
  - The certified pairs have table-MC 1, 2 and 3 only (459,894,904 / 781,458,825 / 796,704,944).
  - So MC-4 restrictions do occur among the cosets the pipeline enumerates, and the pipeline flags them as soon as the C0 filter admits them. In the real run they are excluded by the C0 filter alone, and that filter is validated by V-1 and V-2: three independent affinity implementations agree on every count they share. So a counterexample would have been detected.
- *Search completeness.* My search is exhaustive. On every function where the table says MC 4, it reports no circuit (12 random functions, 10 planted samples, and NIST's 26 MC-4 classes of dimension 5, which also confirms those NIST labels). Where the table says MC ≤ 3, it finds a circuit.

**V-11. Lean (`research/proofs/lean`).**
- `lake build --wfail` succeeds. `lake env lean NPFrontier/Circuit.lean` compiles with no messages.
- `Circuit.lean` contains no `sorry`, `admit`, `axiom`, `native_decide`, `implemented_by` or `extern`.
- `#print axioms` for all 26 circuit theorems lists only `propext`, `Classical.choice` and `Quot.sound`.
- Faithfulness of the statements:
  - `Circuit n m` is the XOR-AND model of §1 of cycle 001: each gate input is an affine form over the inputs and the earlier gates, and the output is an affine form over everything.
  - `MCle f m` is "some m-gate circuit computes f", and `MCle.mono` makes it upward closed.
  - `elim_left`, `elim_right` and `elim_xor` are exactly the gate-elimination steps used in Lemmas 9, 9′ and 24, relativized to an arbitrary input set S.
  - `MCleOn.comp_affine_of_maps_to` is the parametrization step (F2).
  - `MCle_comp_section_iff` is (F4), with the section given as a hypothesis.
- The Lean README states the gaps correctly: no affine subspaces, no existence of sections, no Lemma 23, and the step "vanishes on K ⇒ constant on cosets" of Lemma 24 is missing. Only the list of unformalized results is out of date (I-12).
- So nothing in the documents overstates the formalization. What is formalized is generic circuit algebra, not Theorem 25.

## 4. What I could not check

- The completeness and the MC labels of NIST's class lists, especially the MC-4 lists in dimensions 7 and 8. Lemma 26's route (EXP-015) is only as good as these. Neither Theorem 25 itself nor my V-3 depends on them.
- Confirmation 1 of Theorem 27: the EXP-008 orbit BFS (297 orbits) and EXP-010 `cert4b`. I read only READMEs and logs, and spot-checked the representatives. `s3.c` (EXP-007) was not read. Theorem 27 does not need confirmation 1.
- The SAT runs themselves (`mc3_check*.py`) were not repeated. This does not matter, because every stored circuit was re-verified (V-4).
- The paper texts: Çalık–Sönmez Turan–Peralta 2020, the BFA 2019 slide (s_5), and the 2016 attachment MultComp3. Only search-result abstracts and snippets were seen.
- EXP-017, `formal4_k5case.c`, `formal4_k5red.c`, `redundancy.py` and `lastgate.py`. These were added during the audit and are not part of the claims, except as data in "Observations".
- My programs are unformalized C, as are the authors'. Two unrelated implementations agree exactly on every reported count, and my certificates are checked by evaluation, but neither is a formal proof.

## Summary

- **Theorem 25 survives.** MC(yg) = 5 for every g with MC(g) = 4, on any number of variables; with Theorem 17, PNE-001 holds for MC(g) ≤ 4.
  - Lemma 23 is an exact reformulation. Constants, the affine output part, unused gates and degenerate or dependent input forms are all handled, and "Φ|_{C0} affine" is necessary and sufficient.
  - The reductions to dim K ∈ {5,6,7} and to α_i ≤ β_i are valid.
  - The authors' computations reproduce exactly.
  - An enumeration of my own, sharing no code with EXP-014, re-proves the computational step. It uses all 32,768 wirings, subspaces generated by closure, a different affinity test, and no swap reduction, table, SAT or degeneracy shortcut. Every one of the 2,688 + 1,663,872 + 229,201,152 coset pairs has an explicit circuit with at most 3 AND gates, checked by evaluation. For the 4,667,605 pairs not certified by deleting one gate, the circuit computes the restriction up to an affine function, which is free.
- **Lemmas 28 and 30 and Corollaries 29 and 31 survive** (every level, human proofs). I checked each case by hand and sampled at m = 4, 5, 6 with no violation. The structured proof of Theorem 25 is correct once its citation of Theorem 27 is replaced by a direct citation of the 5-variable computation (I-3).
- **Lemmas 9′, 18–22, 24, 26, Corollary 21 and (F4) survive.** Theorem 27 survives, but two supporting statements need correction:
  - the independence of its confirmations (I-1);
  - the source given for "MC ≤ 4 on 5 variables" (I-2).
- **EXP-015 survives.** It is correctly presented as conditional on NIST's list. Its fingerprint test is sound for the functions tested, although "affine-invariant" is not true in general (I-4).
- **`Circuit.lean` builds cleanly** with standard axioms only. Its statements are what the documents say they are: generic gate elimination and affine substitution, not Lemma 23 or Theorem 25.
- **No overclaim** about P vs NP or novelty. No prior statement of the general fresh-variable lemma or of these level-4 results was found; the 2016 NIST email (special case h = v·f) is recorded correctly.

## Appendix A. Auditor's programs

All written for this audit; none shares code with the project. Build: `gcc -O2 -march=native -fopenmp`. Runs: `ic_enum 7|6|5 0 <threads>` (writes the uncertified residues `unc_k<k>.txt`), then `ic_search <k> <file of hex tables>`; `lem2830 m nwirings seed`; `lem30_exh`. The "0 exceptions" count in V-3 comes from `ic_enum` with one added counter (degenerate pairs that are not certified). The planted variants of V-10 are `ic_enum` with the C0 test replaced (degree ≤ 2 on C0, or no test), a stride over wirings, and a lookup of `EXP-010/mc5.mc5` that counts certified pairs whose C1 restriction has table-MC 4 (there must be none) and writes samples of uncertified MC-4 restrictions.

### A.1 `ic_enum.c` (enumeration and gate-deletion certificates)

```c
/* AUDIT-003 independent check (written by the auditor; shares no code with EXP-014).
 * Formal 4-gate circuits on 8 formal inputs.  Convention (deliberately different from EXP-014):
 *   gate i (0..3) has A-input coordinate i and B-input coordinate 4+i; point p in [0,256), w_t = bit t of p.
 *   z_i = (w_i + sum_{j<i} al_i[j] z_j) * (w_{4+i} + sum_{j<i} be_i[j] z_j);  Phi = z_3 + sum_{j<3} gm[j] z_j.
 * Subspaces of F_2^8: generated by BFS closure from {0}, deduplicated by 256-bit membership set (no RREF).
 * Basis of K: greedy over v = 1..255.  Cosets: base = least point.  Local coords: point(t) = base ^ sum t_r b_r.
 * Affinity of Phi on a coset C: D_b Phi constant on C for every basis vector b of K.
 * For every (wiring, K, C1) with C1 non-affine and some coset C0 != C1 affine:
 *   certificate 1: remove one gate i by a Lemma-24-type substitution (or by zero), build the explicit
 *     3-gate XOR-AND circuit over wires (1, t_1..t_k, z'_1..z'_3) and EVALUATE it generically; accept iff it
 *     equals Phi|C1 on all 2^k points.
 *   otherwise: Phi|C1 (local coords) reduced modulo affine functions is written out for a circuit search.
 * Also counts my own implementation of the Lemma-24 vanishing test, for comparison with EXP-014.
 * Usage: ic_enum k [planted]   (planted=1: C0 condition replaced by "degree <= 2 on C0", see below)
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <omp.h>
typedef uint64_t u64;
typedef struct { u64 w[4]; } B256;
static const u64 MSK[6] = {0x5555555555555555ULL,0x3333333333333333ULL,0x0f0f0f0f0f0f0f0fULL,
                           0x00ff00ff00ff00ffULL,0x0000ffff0000ffffULL,0x00000000ffffffffULL};
static inline int bget(const B256 *x, int p) { return (x->w[p >> 6] >> (p & 63)) & 1; }
static inline void bset(B256 *x, int p) { x->w[p >> 6] |= 1ULL << (p & 63); }
static B256 xshift(B256 x, int v) { /* y[p] = x[p ^ v] */
  for (int j = 0; j < 6; j++) if ((v >> j) & 1) { int s = 1 << j;
    for (int i = 0; i < 4; i++) x.w[i] = ((x.w[i] & MSK[j]) << s) | ((x.w[i] >> s) & MSK[j]); }
  if ((v >> 6) & 1) { u64 t = x.w[0]; x.w[0] = x.w[1]; x.w[1] = t; t = x.w[2]; x.w[2] = x.w[3]; x.w[3] = t; }
  if ((v >> 7) & 1) { u64 t = x.w[0]; x.w[0] = x.w[2]; x.w[2] = t; t = x.w[1]; x.w[1] = x.w[3]; x.w[3] = t; }
  return x; }
static inline int beq(const B256 *a, const B256 *b) { return !memcmp(a, b, sizeof(B256)); }

/* ---------- subspace generation by closure ---------- */
typedef struct { B256 *v; int n, cap; B256 *tab; char *used; size_t tcap; } Level;
static u64 hsh(const B256 *x) { u64 h = 0x9e3779b97f4a7c15ULL; for (int i = 0; i < 4; i++) { h ^= x->w[i]; h *= 0xff51afd7ed558ccdULL; h ^= h >> 33; } return h; }
static void lv_init(Level *L, size_t tcap) { L->n = 0; L->cap = 1024; L->v = malloc(L->cap * sizeof(B256)); L->tcap = tcap; L->tab = calloc(tcap, sizeof(B256)); L->used = calloc(tcap, 1); }
static void lv_add(Level *L, B256 x) {
  size_t h = hsh(&x) & (L->tcap - 1);
  while (L->used[h]) { if (beq(&L->tab[h], &x)) return; h = (h + 1) & (L->tcap - 1); }
  L->used[h] = 1; L->tab[h] = x;
  if (L->n == L->cap) { L->cap *= 2; L->v = realloc(L->v, L->cap * sizeof(B256)); }
  L->v[L->n++] = x; }

/* ---------- per-subspace coset data ---------- */
typedef struct { int k, ncos; unsigned char b[8]; unsigned char base[8]; B256 cm[8]; unsigned char pt[8][128]; } SubD;

/* ---------- generic XOR-AND circuit evaluator on 2^k points (tables in 2 words) ---------- */
typedef struct { u64 lo, hi; } T128;
static inline T128 txor(T128 a, T128 b) { T128 r = {a.lo ^ b.lo, a.hi ^ b.hi}; return r; }
static inline T128 tand(T128 a, T128 b) { T128 r = {a.lo & b.lo, a.hi & b.hi}; return r; }
/* wires: 0 = const 1, 1..k = t_1..t_k, then gates.  ngates gates with masks A[g], B[g] (over earlier wires), out mask */
static int eval_circ(int k, int ngates, const unsigned *A, const unsigned *Bm, unsigned out, T128 *res) {
  T128 W[16]; int np = 1 << k;
  T128 one = {0, 0}; for (int p = 0; p < np; p++) { if (p < 64) one.lo |= 1ULL << p; else one.hi |= 1ULL << (p - 64); }
  W[0] = one;
  for (int r = 0; r < k; r++) { T128 t = {0, 0}; for (int p = 0; p < np; p++) if ((p >> r) & 1) { if (p < 64) t.lo |= 1ULL << p; else t.hi |= 1ULL << (p - 64); } W[1 + r] = t; }
  int nw = 1 + k;
  for (int g = 0; g < ngates; g++) {
    if ((A[g] >> nw) || (Bm[g] >> nw)) return -1;            /* forward reference: malformed */
    T128 a = {0, 0}, b = {0, 0};
    for (int j = 0; j < nw; j++) { if ((A[g] >> j) & 1) a = txor(a, W[j]); if ((Bm[g] >> j) & 1) b = txor(b, W[j]); }
    W[nw++] = tand(a, b); }
  if (out >> nw) return -1;
  T128 o = {0, 0}; for (int j = 0; j < nw; j++) if ((out >> j) & 1) o = txor(o, W[j]);
  *res = o; return 0; }

/* Moebius transform (involution) on 2^k-bit table */
static T128 moeb(T128 t, int k) {
  for (int i = 0; i < k && i < 6; i++) { t.lo ^= (t.lo & MSK[i]) << (1 << i); t.hi ^= (t.hi & MSK[i]) << (1 << i); }
  if (k == 7) t.hi ^= t.lo;
  return t; }
static T128 red_aff(T128 t, int k) {
  T128 a = moeb(t, k);
  a.lo &= ~1ULL; for (int i = 0; i < k; i++) { int p = 1 << i; if (p < 64) a.lo &= ~(1ULL << p); else a.hi &= ~(1ULL << (p - 64)); }
  return moeb(a, k); }
static int degree_of(T128 t, int k) { T128 a = moeb(t, k); int d = -1; int np = 1 << k;
  for (int p = 0; p < np; p++) { int bitv = p < 64 ? (a.lo >> p) & 1 : (a.hi >> (p - 64)) & 1; if (bitv) { int c = __builtin_popcount(p); if (c > d) d = c; } } return d; }

/* thread-local hash sets of T128 */
typedef struct { T128 *tab; char *used; size_t cap, n; } HSet;
static void hs_init(HSet *H, size_t cap) { H->cap = cap; H->n = 0; H->tab = calloc(cap, sizeof(T128)); H->used = calloc(cap, 1); }
static void hs_add(HSet *H, T128 x) {
  u64 h = (x.lo * 0x9e3779b97f4a7c15ULL) ^ (x.hi * 0xc2b2ae3d27d4eb4fULL); h ^= h >> 29; size_t i = h & (H->cap - 1);
  while (H->used[i]) { if (H->tab[i].lo == x.lo && H->tab[i].hi == x.hi) return; i = (i + 1) & (H->cap - 1); }
  H->used[i] = 1; H->tab[i] = x; H->n++;
  if (H->n * 2 > H->cap) { fprintf(stderr, "hash full\n"); exit(5); } }

int main(int argc, char **argv) {
  int k = atoi(argv[1]); int planted = argc > 2 ? atoi(argv[2]) : 0;
  int nthreads = argc > 3 ? atoi(argv[3]) : 2; omp_set_num_threads(nthreads);
  /* subspaces */
  Level L[9]; size_t caps[9] = {16, 1024, 32768, 262144, 524288, 262144, 32768, 1024, 16};
  for (int d = 0; d <= 8; d++) lv_init(&L[d], caps[d]);
  B256 z0; memset(&z0, 0, sizeof z0); bset(&z0, 0); lv_add(&L[0], z0);
  for (int d = 0; d < k; d++) for (int s = 0; s < L[d].n; s++) { B256 S = L[d].v[s];
    for (int v = 1; v < 256; v++) if (!bget(&S, v)) { B256 T = xshift(S, v); for (int i = 0; i < 4; i++) T.w[i] |= S.w[i]; lv_add(&L[d + 1], T); } }
  for (int d = 0; d <= k; d++) fprintf(stderr, "level %d: %d subspaces\n", d, L[d].n);
  int nsub = L[k].n; int ncos = 1 << (8 - k), np = 1 << k;
  SubD *SD = malloc((size_t)nsub * sizeof(SubD));
  for (int s = 0; s < nsub; s++) { B256 S = L[k].v[s]; SubD *D = &SD[s]; D->k = k; D->ncos = ncos;
    int cnt = 0; for (int p = 0; p < 256; p++) cnt += bget(&S, p); if (cnt != np) { fprintf(stderr, "size bug\n"); return 2; }
    B256 span; memset(&span, 0, sizeof span); bset(&span, 0); int r = 0;
    for (int v = 1; v < 256; v++) if (bget(&S, v) && !bget(&span, v)) { D->b[r++] = v; B256 T = xshift(span, v); for (int i = 0; i < 4; i++) span.w[i] |= T.w[i]; }
    if (r != k || !beq(&span, &S)) { fprintf(stderr, "basis bug\n"); return 2; }
    int asg[256]; for (int p = 0; p < 256; p++) asg[p] = -1; int c = 0;
    for (int p = 0; p < 256; p++) if (asg[p] < 0) { D->base[c] = p; memset(&D->cm[c], 0, sizeof(B256));
      for (int t = 0; t < np; t++) { int q = p; for (int rr = 0; rr < k; rr++) if ((t >> rr) & 1) q ^= D->b[rr];
        if (asg[q] >= 0) { fprintf(stderr, "coset bug\n"); return 2; } asg[q] = c; D->pt[c][t] = q; bset(&D->cm[c], q); }
      c++; }
    if (c != ncos) { fprintf(stderr, "ncos bug\n"); return 2; } }
  /* wirings: all 32768 */
  static int wir[32768][7]; int nw = 0;
  for (int a1 = 0; a1 < 2; a1++) for (int b1 = 0; b1 < 2; b1++) for (int a2 = 0; a2 < 4; a2++) for (int b2 = 0; b2 < 4; b2++)
  for (int a3 = 0; a3 < 8; a3++) for (int b3 = 0; b3 < 8; b3++) for (int gm = 0; gm < 8; gm++) {
    int *w = wir[nw++]; w[0] = a1; w[1] = a2; w[2] = a3; w[3] = b1; w[4] = b2; w[5] = b3; w[6] = gm; }
  B256 Wt[8]; for (int t = 0; t < 8; t++) { memset(&Wt[t], 0, sizeof(B256)); for (int p = 0; p < 256; p++) if ((p >> t) & 1) bset(&Wt[t], p); }
  /* statistics: index 0 = all wirings, index 1 = swap-reduced wirings (al_i <= be_i) */
  long naff[2] = {0}, npairs[2] = {0}, ndeg[2] = {0}, ncert[2] = {0}, nunc[2] = {0}, nC1[2] = {0}, nC1unc[2] = {0};
  long ncert_type[6] = {0};
  HSet *HS = malloc(nthreads * sizeof(HSet)); for (int i = 0; i < nthreads; i++) hs_init(&HS[i], 1 << 22);
  #pragma omp parallel for schedule(dynamic, 16) reduction(+:naff[:2],npairs[:2],ndeg[:2],ncert[:2],nunc[:2],nC1[:2],nC1unc[:2],ncert_type[:6])
  for (int wi = 0; wi < nw; wi++) {
    int *w = wir[wi]; int al[4] = {0, w[0], w[1], w[2]}, be[4] = {0, w[3], w[4], w[5]}, gm = w[6];
    int red = (al[1] <= be[1]) && (al[2] <= be[2]) && (al[3] <= be[3]);
    B256 z[4];
    for (int i = 0; i < 4; i++) { B256 A = Wt[i], B = Wt[4 + i];
      for (int j = 0; j < i; j++) { if ((al[i] >> j) & 1) for (int q = 0; q < 4; q++) A.w[q] ^= z[j].w[q]; if ((be[i] >> j) & 1) for (int q = 0; q < 4; q++) B.w[q] ^= z[j].w[q]; }
      for (int q = 0; q < 4; q++) z[i].w[q] = A.w[q] & B.w[q]; }
    B256 Phi = z[3]; for (int j = 0; j < 3; j++) if ((gm >> j) & 1) for (int q = 0; q < 4; q++) Phi.w[q] ^= z[j].w[q];
    static __thread B256 Dt[256];
    for (int v = 1; v < 256; v++) { B256 T = xshift(Phi, v); for (int q = 0; q < 4; q++) Dt[v].w[q] = T.w[q] ^ Phi.w[q]; }
    int tid = omp_get_thread_num();
    for (int s = 0; s < nsub; s++) { const SubD *D = &SD[s];
      unsigned alive = (1u << ncos) - 1;
      for (int r = 0; r < k && alive; r++) { const B256 *d = &Dt[D->b[r]];
        for (int c = 0; c < ncos; c++) if ((alive >> c) & 1) { const B256 *m = &D->cm[c];
          u64 x0 = d->w[0] & m->w[0], x1 = d->w[1] & m->w[1], x2 = d->w[2] & m->w[2], x3 = d->w[3] & m->w[3];
          int zero = !(x0 | x1 | x2 | x3), full = (x0 == m->w[0]) && (x1 == m->w[1]) && (x2 == m->w[2]) && (x3 == m->w[3]);
          if (!zero && !full) alive &= ~(1u << c); } }
      unsigned c0set = alive;          /* cosets admissible as C0 */
      if (planted) { /* planted variant: C0 condition weakened to "degree <= 2 on C0" (second derivatives constant) */
        c0set = 0; for (int c = 0; c < ncos; c++) { T128 g = {0, 0};
          for (int t = 0; t < np; t++) if (bget(&Phi, D->pt[c][t])) { if (t < 64) g.lo |= 1ULL << t; else g.hi |= 1ULL << (t - 64); }
          if (degree_of(g, k) <= 2) c0set |= 1u << c; } }
      if (!c0set) continue;
      int na = __builtin_popcount(c0set);
      naff[0] += na; if (red) naff[1] += na;
      /* my Lemma-24 vanishing test (coset independent) */
      int orv = 0, eqv = 0; for (int r = 0; r < k; r++) orv |= D->b[r];
      int deg = 0;
      for (int i = 0; i < 4; i++) {
        if (al[i] == 0 && !((orv >> i) & 1)) deg = 1;
        if (be[i] == 0 && !((orv >> (4 + i)) & 1)) deg = 1;
        int sumv = 0; for (int r = 0; r < k; r++) sumv |= ((D->b[r] >> i) ^ (D->b[r] >> (4 + i))) & 1;
        if (al[i] == be[i] && !sumv) deg = 1; }
      (void)eqv;
      for (int c1 = 0; c1 < ncos; c1++) {
        if ((alive >> c1) & 1) continue;                 /* C1 must be non-affine (affine C1 has MC 0) */
        int nc0 = na - ((c0set >> c1) & 1);              /* C0 != C1 */
        if (nc0 <= 0) continue;
        npairs[0] += nc0; if (red) npairs[1] += nc0; nC1[0]++; if (red) nC1[1]++;
        if (deg) { ndeg[0] += nc0; if (red) ndeg[1] += nc0; }
        /* g = Phi|C1 in local coordinates */
        T128 g = {0, 0}; for (int t = 0; t < np; t++) if (bget(&Phi, D->pt[c1][t])) { if (t < 64) g.lo |= 1ULL << t; else g.hi |= 1ULL << (t - 64); }
        /* local affine masks of the formal inputs on C1: bit 0 = constant, bit 1+r = coefficient of t_r */
        unsigned mw[8]; for (int tq = 0; tq < 8; tq++) { unsigned m = (D->base[c1] >> tq) & 1; for (int r = 0; r < k; r++) if ((D->b[r] >> tq) & 1) m |= 1u << (1 + r); mw[tq] = m; }
        int certified = 0;
        for (int i = 0; i < 4 && !certified; i++) {
          unsigned rep[4]; for (int l = 0; l < 4; l++) if (l != i) rep[l] = 1u << (1 + k + (l < i ? l : l - 1));
          unsigned Ai = mw[i], Bi = mw[4 + i];
          for (int l = 0; l < i; l++) { if ((al[i] >> l) & 1) Ai ^= rep[l]; if ((be[i] >> l) & 1) Bi ^= rep[l]; }
          unsigned cand[4]; int ty[4], nc = 0;
          if (al[i] == 0) { cand[nc] = (mw[i] & 1) ? Bi : 0; ty[nc++] = 0; }
          if (be[i] == 0) { cand[nc] = (mw[4 + i] & 1) ? Ai : 0; ty[nc++] = 1; }
          if (al[i] == be[i]) { int eps = (mw[i] ^ mw[4 + i]) & 1; cand[nc] = eps ? 0 : Ai; ty[nc++] = 2; }
          cand[nc] = 0; ty[nc++] = 3;
          for (int ci = 0; ci < nc && !certified; ci++) {
            rep[i] = cand[ci];
            unsigned GA[3], GB[3]; int ng = 0;
            for (int j = 0; j < 4; j++) if (j != i) { unsigned a = mw[j], b = mw[4 + j];
              for (int l = 0; l < j; l++) { if ((al[j] >> l) & 1) a ^= rep[l]; if ((be[j] >> l) & 1) b ^= rep[l]; }
              GA[ng] = a; GB[ng] = b; ng++; }
            unsigned out = rep[3]; for (int l = 0; l < 3; l++) if ((gm >> l) & 1) out ^= rep[l];
            T128 res; if (eval_circ(k, 3, GA, GB, out, &res) == 0 && res.lo == g.lo && res.hi == g.hi) { certified = 1; ncert_type[ty[ci]] += nc0; }
          } }
        if (certified) { ncert[0] += nc0; if (red) ncert[1] += nc0; }
        else { nunc[0] += nc0; if (red) nunc[1] += nc0; nC1unc[0]++; if (red) nC1unc[1]++; hs_add(&HS[tid], red_aff(g, k)); }
      } } }
  /* merge and write distinct uncertified functions (mod affine) */
  HSet all; hs_init(&all, 1 << 23);
  for (int i = 0; i < nthreads; i++) for (size_t j = 0; j < HS[i].cap; j++) if (HS[i].used[j]) hs_add(&all, HS[i].tab[j]);
  char fn[64]; sprintf(fn, "unc_k%d%s.txt", k, planted ? "_planted" : "");
  FILE *fo = fopen(fn, "w"); long nd = 0; int dh[9] = {0};
  for (size_t j = 0; j < all.cap; j++) if (all.used[j]) { T128 t = all.tab[j]; int dg = degree_of(t, k); dh[dg < 0 ? 0 : dg]++; nd++;
    fprintf(fo, "%016llx%016llx %d\n", (unsigned long long)t.hi, (unsigned long long)t.lo, dg); }
  fclose(fo);
  for (int x = 0; x < 2; x++)
    printf("k=%d planted=%d %s: C0-cosets(affine)=%ld pairs=%ld my-L24-degenerate=%ld certified-by-explicit-3-gate-circuit=%ld uncertified=%ld (C1 cosets %ld, uncertified %ld)\n",
      k, planted, x ? "swap-reduced" : "all-wirings ", naff[x], npairs[x], ndeg[x], ncert[x], nunc[x], nC1[x], nC1unc[x]);
  printf("certificate types (pairs, all wirings): a=%ld b=%ld c=%ld zero=%ld\n", ncert_type[0], ncert_type[1], ncert_type[2], ncert_type[3]);
  printf("distinct uncertified functions mod affine: %ld  degree histogram:", nd); for (int d = 0; d <= 8; d++) if (dh[d]) printf(" %d:%d", d, dh[d]); printf("  -> %s\n", fn);
  return 0; }
```

### A.2 `ic_search.c` (≤ 3-gate circuit search with point-by-point verification)

```c
/* AUDIT-003: auditor-written search for a <=3-AND XOR-AND circuit computing f (n <= 7 variables).
 * Gate 1: z1 = l1*l2 (one representative per 2-dim space of linear forms; constants are absorbed mod affine).
 * Gate 2: z2 = A*B, A,B in span(x, z1) (one representative per 2-dim space).
 * Gate 3: uses bilinearity of (C,D) -> C*D mod W2: for each C, solve r = sum_j d_j (C*e_j mod W2) for d.
 * Every circuit found is converted to explicit wire masks, the output mask is found by brute force, and the
 * circuit is re-evaluated point by point by an evaluator that knows nothing about the search.
 * Input lines: "<hex table> ..." with 2^n bits (rightmost hex digit = points 0..3).  Usage: ic_search n file */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
typedef uint64_t u64;
typedef struct { u64 lo, hi; } T;
static int N, NP;
static inline T tx(T a, T b) { T r = {a.lo ^ b.lo, a.hi ^ b.hi}; return r; }
static inline T ta(T a, T b) { T r = {a.lo & b.lo, a.hi & b.hi}; return r; }
static inline int tz(T a) { return !(a.lo | a.hi); }
static inline int tbit(T a, int p) { return p < 64 ? (a.lo >> p) & 1 : (a.hi >> (p - 64)) & 1; }
static inline int teq(T a, T b) { return a.lo == b.lo && a.hi == b.hi; }
typedef struct { int n; T v[16]; int piv[16]; } Ech;
static int lowbit(T x) { if (x.lo) return __builtin_ctzll(x.lo); if (x.hi) return 64 + __builtin_ctzll(x.hi); return -1; }
static T red(const Ech *E, T x) { for (int i = 0; i < E->n; i++) if (tbit(x, E->piv[i])) x = tx(x, E->v[i]); return x; }
static int add(Ech *E, T x) { x = red(E, x); if (tz(x)) return 0; int p = lowbit(x);
  for (int i = 0; i < E->n; i++) if (tbit(E->v[i], p)) E->v[i] = tx(E->v[i], x);
  E->v[E->n] = x; E->piv[E->n] = p; E->n++; return 1; }
static T ONE, X[8];
static T lin(int m) { T r = {0, 0}; for (int j = 0; j < N; j++) if ((m >> j) & 1) r = tx(r, X[j]); return r; }
/* point-by-point evaluator: wires 0 = 1, 1..N = x, then gates */
static T evalpp(int ng, const unsigned *A, const unsigned *B, unsigned out) {
  T res = {0, 0};
  for (int p = 0; p < NP; p++) { int w[16]; int nw = 0; w[nw++] = 1; for (int j = 0; j < N; j++) w[nw++] = (p >> j) & 1;
    for (int g = 0; g < ng; g++) { int a = 0, b = 0; for (int j = 0; j < nw; j++) { if ((A[g] >> j) & 1) a ^= w[j]; if ((B[g] >> j) & 1) b ^= w[j]; }
      if ((A[g] >> nw) || (B[g] >> nw)) { fprintf(stderr, "malformed\n"); exit(9); } w[nw] = a & b; nw++; }
    int o = 0; for (int j = 0; j < nw; j++) if ((out >> j) & 1) o ^= w[j];
    if (o) { if (p < 64) res.lo |= 1ULL << p; else res.hi |= 1ULL << (p - 64); } }
  return res; }
static long nodes;
/* returns number of gates used (0..3) or -1; fills masks */
static int search(T f, unsigned *GA, unsigned *GB, unsigned *OUT) {
  Ech E0 = {0}; add(&E0, ONE); for (int j = 0; j < N; j++) add(&E0, X[j]);
  if (tz(red(&E0, f))) { *OUT = 0; return 0; }
  int L = 1 << N;
  for (int l1 = 1; l1 < L; l1++) for (int l2 = l1 + 1; l2 < L; l2++) { if ((l1 ^ l2) <= l2) continue;
    T z1 = ta(lin(l1), lin(l2)); Ech E1 = E0; if (!add(&E1, z1)) continue;
    GA[0] = (unsigned)l1 << 1; GB[0] = (unsigned)l2 << 1;
    if (tz(red(&E1, f))) return 1;
    T e1[8]; for (int j = 0; j < N; j++) e1[j] = X[j]; e1[N] = z1;
    int L1 = 1 << (N + 1);
    for (int a = 1; a < L1; a++) for (int b = a + 1; b < L1; b++) { if ((a ^ b) <= b) continue;
      T va = {0, 0}, vb = {0, 0}; for (int j = 0; j <= N; j++) { if ((a >> j) & 1) va = tx(va, e1[j]); if ((b >> j) & 1) vb = tx(vb, e1[j]); }
      T z2 = ta(va, vb); Ech E2 = E1; if (!add(&E2, z2)) continue;
      nodes++;
      GA[1] = ((unsigned)(a & (L - 1)) << 1) | (((a >> N) & 1u) << (N + 1)); GB[1] = ((unsigned)(b & (L - 1)) << 1) | (((b >> N) & 1u) << (N + 1));
      T rf = red(&E2, f); if (tz(rf)) return 2;
      T e2[9]; for (int j = 0; j <= N; j++) e2[j] = e1[j]; e2[N + 1] = z2; int M = N + 2;
      T P[9][9]; for (int i = 0; i < M; i++) { P[i][i].lo = P[i][i].hi = 0; for (int j = i + 1; j < M; j++) { P[i][j] = red(&E2, ta(e2[i], e2[j])); P[j][i] = P[i][j]; } }
      int LC = 1 << M;
      for (int c = 1; c < LC; c++) {
        T v[9]; for (int j = 0; j < M; j++) { T s = {0, 0}; for (int i = 0; i < M; i++) if ((c >> i) & 1) s = tx(s, P[i][j]); v[j] = s; }
        /* eliminate with coefficient tracking */
        T bv[9]; unsigned bc[9]; int bp[9], nb = 0;
        for (int j = 0; j < M; j++) { T x = v[j]; unsigned cm = 1u << j;
          for (int i = 0; i < nb; i++) if (tbit(x, bp[i])) { x = tx(x, bv[i]); cm ^= bc[i]; }
          if (tz(x)) continue; int p = lowbit(x);
          for (int i = 0; i < nb; i++) if (tbit(bv[i], p)) { bv[i] = tx(bv[i], x); bc[i] ^= cm; }
          bv[nb] = x; bc[nb] = cm; bp[nb] = p; nb++; }
        T x = rf; unsigned dm = 0; for (int i = 0; i < nb; i++) if (tbit(x, bp[i])) { x = tx(x, bv[i]); dm ^= bc[i]; }
        if (!tz(x)) continue;
        /* D = sum_{j in dm} e2[j]; gate 3 = C * D */
        GA[2] = ((unsigned)(c & (L - 1)) << 1) | (((c >> N) & 1u) << (N + 1)) | (((c >> (N + 1)) & 1u) << (N + 2));
        GB[2] = ((unsigned)(dm & (L - 1)) << 1) | (((dm >> N) & 1u) << (N + 1)) | (((dm >> (N + 1)) & 1u) << (N + 2));
        return 3; } } }
  return -1; }
int main(int argc, char **argv) {
  N = atoi(argv[1]); NP = 1 << N;
  ONE.lo = ONE.hi = 0; for (int p = 0; p < NP; p++) { if (p < 64) ONE.lo |= 1ULL << p; else ONE.hi |= 1ULL << (p - 64); }
  for (int j = 0; j < N; j++) { X[j].lo = X[j].hi = 0; for (int p = 0; p < NP; p++) if ((p >> j) & 1) { if (p < 64) X[j].lo |= 1ULL << p; else X[j].hi |= 1ULL << (p - 64); } }
  FILE *fi = fopen(argv[2], "r"); char line[512]; long cnt = 0, ok = 0, fail = 0; int hist[5] = {0};
  clock_t t0 = clock();
  while (fgets(line, sizeof line, fi)) {
    char hx[64]; if (sscanf(line, "%63s", hx) != 1) continue;
    int len = strlen(hx); T f = {0, 0};
    for (int i = 0; i < len; i++) { char ch = hx[len - 1 - i]; int d = (ch >= '0' && ch <= '9') ? ch - '0' : (ch | 32) - 'a' + 10; int p = 4 * i;
      for (int b = 0; b < 4; b++) if ((d >> b) & 1) { if (p + b < 64) f.lo |= 1ULL << (p + b); else f.hi |= 1ULL << (p + b - 64); } }
    if (NP < 64) f.lo &= (1ULL << NP) - 1; if (NP <= 64) f.hi = 0;
    cnt++;
    unsigned GA[3] = {0}, GB[3] = {0}, out = 0;
    int ng = search(f, GA, GB, &out);
    if (ng < 0) { fail++; printf("NOCIRCUIT %s\n", hx); fflush(stdout); continue; }
    /* find output mask by brute force over all subsets of wires 0..N+ng, then verify point by point */
    int nwires = 1 + N + ng, found = 0;
    for (unsigned o = 0; o < (1u << nwires) && !found; o++) { T r = evalpp(ng, GA, GB, o); if (teq(r, f)) { out = o; found = 1; } }
    if (!found) { fail++; printf("SEARCH-BUG %s\n", hx); continue; }
    ok++; hist[ng]++;
    printf("OK %s gates=%d", hx, ng); for (int g = 0; g < ng; g++) printf(" [%x*%x]", GA[g], GB[g]); printf(" out=%x\n", out);
  }
  fprintf(stderr, "n=%d: %ld functions, %ld verified circuits (gates: 0:%d 1:%d 2:%d 3:%d), %ld without circuit, %.1fs, nodes %ld\n",
          N, cnt, ok, hist[0], hist[1], hist[2], hist[3], fail, (double)(clock() - t0) / CLOCKS_PER_SEC, nodes);
  return fail != 0; }
```

### A.3 `lem2830.c` (random-wiring test of Lemmas 28 and 30)

```c
/* AUDIT-003: random-wiring test of Lemma 28 (codim 1) and Lemma 30 (codim 2) for m gates, D = 2m formal inputs.
 * Auditor's convention: gate i (0..m-1) has A-coordinate i and B-coordinate m+i.
 * For each random wiring: every hyperplane h (both cosets) and every 2-dim dual subspace H = span(h1,h2) (all 4
 * cosets of K = H^perp).  If some coset is affine:
 *   codim 1: Lemma 28 claims the LAST gate is degenerate for ker h (h = e_A & al=0, h = e_B & be=0, h = e_A+e_B & al=be).
 *   codim 2: Lemma 30's proof claims: some gate is Lemma-24-degenerate for K, or for EVERY coset C the last gate is
 *            redundant: Phi|C in span(1, local coords, z_1|C..z_{m-1}|C).  Checked by Gaussian elimination.
 * Usage: lem2830 m nwirings seed */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u64;
#define MAXW 64
static int M, D, NP, NW;
typedef struct { u64 w[MAXW]; } T;
static inline int tget(const T *t, int p) { return (t->w[p >> 6] >> (p & 63)) & 1; }
static u64 rs = 88172645463325252ULL; static u64 rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static T *Par; /* Par[h*2+c] */
static int par(int x) { return __builtin_popcount(x) & 1; }
/* affinity of f on coset mask cm along basis b[0..k-1] via derivative constancy */
static int affine_on(const T *f, const T *cm, const int *b, int k) {
  for (int r = 0; r < k; r++) { int v = b[r]; int zero = 1, full = 1;
    for (int p = 0; p < NP && (zero || full); p++) if (tget(cm, p)) { int d = tget(f, p) ^ tget(f, p ^ v); if (d) zero = 0; else full = 0; }
    if (!zero && !full) return 0; }
  return 1; }
/* Gaussian elimination membership test on vectors of length L bits (L <= 4096) */
typedef struct { int n; u64 *v[64]; int piv[64]; int L; } Ech;
static int vbit(const u64 *v, int p) { return (v[p >> 6] >> (p & 63)) & 1; }
static void ech_reduce(const Ech *E, u64 *x) { int nw = (E->L + 63) / 64; for (int i = 0; i < E->n; i++) if (vbit(x, E->piv[i])) for (int q = 0; q < nw; q++) x[q] ^= E->v[i][q]; }
static int ech_add(Ech *E, const u64 *x0) { int nw = (E->L + 63) / 64; u64 *x = malloc(nw * 8); memcpy(x, x0, nw * 8); ech_reduce(E, x);
  int p = -1; for (int q = 0; q < E->L; q++) if (vbit(x, q)) { p = q; break; }
  if (p < 0) { free(x); return 0; }
  for (int i = 0; i < E->n; i++) if (vbit(E->v[i], p)) for (int q = 0; q < nw; q++) E->v[i][q] ^= x[q];
  E->v[E->n] = x; E->piv[E->n] = p; E->n++; return 1; }
static void ech_free(Ech *E) { for (int i = 0; i < E->n; i++) free(E->v[i]); E->n = 0; }
int main(int argc, char **argv) {
  M = atoi(argv[1]); long nwir = atol(argv[2]); rs ^= (u64)atol(argv[3]) * 0x9e3779b97f4a7c15ULL;
  D = 2 * M; NP = 1 << D; NW = NP / 64; if (NW < 1) NW = 1;
  Par = calloc((size_t)NP * 2, sizeof(T));
  for (int h = 1; h < NP; h++) for (int p = 0; p < NP; p++) { int c = par(h & p); Par[h * 2 + c].w[p >> 6] |= 1ULL << (p & 63); }
  long n1aff = 0, n1viol = 0, n2sub = 0, n2aff = 0, n2deg = 0, n2red = 0, n2viol = 0;
  for (long wi = 0; wi < nwir; wi++) {
    int al[8] = {0}, be[8] = {0}, gm;
    for (int i = 1; i < M; i++) { al[i] = rnd() & ((1 << i) - 1); be[i] = rnd() & ((1 << i) - 1); }
    gm = rnd() & ((1 << (M - 1)) - 1);
    if (wi % 4 == 1) { int i = 1 + rnd() % (M - 1); be[i] = al[i]; }       /* bias toward al=be and zeros */
    if (wi % 4 == 2) { al[M - 1] = 0; }
    if (wi % 4 == 3) { be[M - 1] = 0; al[1 + rnd() % (M - 1)] = 0; }
    T z[8]; T Wt;
    for (int i = 0; i < M; i++) { T A, B; memset(&A, 0, sizeof A); memset(&B, 0, sizeof B);
      for (int p = 0; p < NP; p++) { if ((p >> i) & 1) A.w[p >> 6] |= 1ULL << (p & 63); if ((p >> (M + i)) & 1) B.w[p >> 6] |= 1ULL << (p & 63); }
      for (int j = 0; j < i; j++) { if ((al[i] >> j) & 1) for (int q = 0; q < NW; q++) A.w[q] ^= z[j].w[q]; if ((be[i] >> j) & 1) for (int q = 0; q < NW; q++) B.w[q] ^= z[j].w[q]; }
      for (int q = 0; q < NW; q++) z[i].w[q] = A.w[q] & B.w[q]; }
    T Phi = z[M - 1]; for (int j = 0; j < M - 1; j++) if ((gm >> j) & 1) for (int q = 0; q < NW; q++) Phi.w[q] ^= z[j].w[q];
    (void)Wt;
    int eA = 1 << (M - 1), eB = 1 << (2 * M - 1);   /* last gate coordinates */
    /* codim 1 */
    for (int h = 1; h < NP; h++) {
      int kb[16], k = 0, span[1] = {0}; (void)span;
      /* basis of ker h: e_j for j != q plus e_q-adjusted, q = lowest bit of h */
      int q0 = __builtin_ctz(h);
      for (int j = 0; j < D; j++) if (j != q0) { int v = 1 << j; if ((h >> j) & 1) v |= 1 << q0; kb[k++] = v; }
      for (int c = 0; c < 2; c++) if (affine_on(&Phi, &Par[h * 2 + c], kb, k)) {
        n1aff++;
        int ok = (h == eA && al[M - 1] == 0) || (h == eB && be[M - 1] == 0) || (h == (eA | eB) && al[M - 1] == be[M - 1]);
        if (!ok) { n1viol++; printf("L28 VIOLATION m=%d h=%x c=%d\n", M, h, c); } } }
    /* codim 2 */
    for (int h1 = 1; h1 < NP; h1++) for (int h2 = h1 + 1; h2 < NP; h2++) { if ((h1 ^ h2) <= h2) continue;
      n2sub++;
      /* basis of K = {p : h1.p = h2.p = 0}: pivots q1 = lowbit(h1'), q2 for reduced pair */
      int a = h1, b = h2; int q1 = __builtin_ctz(a); if ((b >> q1) & 1) b ^= a; int q2 = __builtin_ctz(b); if ((a >> q2) & 1) a ^= b;
      int kb[16], k = 0;
      for (int j = 0; j < D; j++) if (j != q1 && j != q2) { int v = 1 << j; if ((a >> j) & 1) v |= 1 << q1; if ((b >> j) & 1) v |= 1 << q2; kb[k++] = v; }
      /* sanity: kb in K */
      for (int r = 0; r < k; r++) if (par(kb[r] & h1) || par(kb[r] & h2)) { fprintf(stderr, "basis bug\n"); return 3; }
      T cm[4]; int any = 0, aff[4];
      for (int c = 0; c < 4; c++) { for (int q = 0; q < NW; q++) cm[c].w[q] = Par[h1 * 2 + (c & 1)].w[q] & Par[h2 * 2 + (c >> 1)].w[q];
        aff[c] = affine_on(&Phi, &cm[c], kb, k); any |= aff[c]; }
      if (!any) continue;
      n2aff++;
      /* Lemma-24 degeneracy of some gate for K: functional in span(h1,h2) */
      int Hs[3] = {h1, h2, h1 ^ h2}, deg = 0;
      for (int i = 0; i < M && !deg; i++) { int fa = 1 << i, fb = 1 << (M + i);
        for (int s = 0; s < 3; s++) { if (al[i] == 0 && Hs[s] == fa) deg = 1; if (be[i] == 0 && Hs[s] == fb) deg = 1; if (al[i] == be[i] && Hs[s] == (fa | fb)) deg = 1; } }
      if (deg) { n2deg++; continue; }
      /* else: last gate redundant on every coset? */
      int allred = 1;
      for (int c = 0; c < 4 && allred; c++) {
        int base = -1; for (int p = 0; p < NP; p++) if (tget(&cm[c], p)) { base = p; break; }
        int L = 1 << k; Ech E; E.n = 0; E.L = L; int nwl = (L + 63) / 64;
        u64 *vec = calloc(nwl, 8);
        /* point list */
        int *pt = malloc(L * sizeof(int)); for (int t = 0; t < L; t++) { int p = base; for (int r = 0; r < k; r++) if ((t >> r) & 1) p ^= kb[r]; pt[t] = p; }
        memset(vec, 0, nwl * 8); for (int t = 0; t < L; t++) vec[t >> 6] |= 1ULL << (t & 63); ech_add(&E, vec);
        for (int r = 0; r < k; r++) { memset(vec, 0, nwl * 8); for (int t = 0; t < L; t++) if ((t >> r) & 1) vec[t >> 6] |= 1ULL << (t & 63); ech_add(&E, vec); }
        for (int j = 0; j < M - 1; j++) { memset(vec, 0, nwl * 8); for (int t = 0; t < L; t++) if (tget(&z[j], pt[t])) vec[t >> 6] |= 1ULL << (t & 63); ech_add(&E, vec); }
        memset(vec, 0, nwl * 8); for (int t = 0; t < L; t++) if (tget(&Phi, pt[t])) vec[t >> 6] |= 1ULL << (t & 63);
        ech_reduce(&E, vec); int zero = 1; for (int q = 0; q < nwl; q++) if (vec[q]) zero = 0;
        if (!zero) allred = 0;
        ech_free(&E); free(vec); free(pt); }
      if (allred) n2red++; else { n2viol++; printf("L30 VIOLATION m=%d h1=%x h2=%x\n", M, h1, h2); }
    }
  }
  printf("m=%d wirings=%ld | codim1: affine cosets %ld, Lemma-28 violations %ld | codim2: subspaces/wiring %ld, (wiring,K) with affine coset %ld, degenerate %ld, last-gate-redundant-on-all-cosets %ld, violations %ld\n",
         M, nwir, n1aff, n1viol, n2sub / (nwir ? nwir : 1), n2aff, n2deg, n2red, n2viol);
  return 0; }
```

### A.4 `lem30_exh.c` (exhaustive m = 4 codimension-2 tally)

```c
/* AUDIT-003: exhaustive m = 4, codimension-2 tally for Lemma 30 and the "Observations" data (auditor's code).
 * Convention: gate i (0..3) has A-coordinate i, B-coordinate 4+i; last gate: u = coord 3, v = coord 7.
 * For every wiring (all 32768; swap-reduced subset tallied separately) and every 2-dim dual space H (10795):
 * cosets of K = H^perp; pairs (C0 affine, C1 non-affine).  Per pair: case d = dim pi(H) (pi = (h_u, h_v));
 * Lemma-24 degeneracy of K; whether the last gate is redundant on C1 (Phi|C1 in span(1,t,z1,z2,z3 on C1)). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u64;
static inline int par(int x) { return __builtin_popcount(x) & 1; }
static int inspan(u64 *rows, int nr, u64 x) { /* rows: 64-bit vectors; Gaussian elimination */
  u64 b[16]; int piv[16], nb = 0;
  for (int i = 0; i < nr; i++) { u64 v = rows[i]; for (int j = 0; j < nb; j++) if ((v >> piv[j]) & 1) v ^= b[j];
    if (!v) continue; int p = __builtin_ctzll(v); for (int j = 0; j < nb; j++) if ((b[j] >> p) & 1) b[j] ^= v; b[nb] = v; piv[nb] = p; nb++; }
  for (int j = 0; j < nb; j++) if ((x >> piv[j]) & 1) x ^= b[j];
  return x == 0; }
int main(void) {
  /* dual 2-spaces and K bases */
  static int H1[10795], H2[10795], KB[10795][6]; int ns = 0;
  for (int h1 = 1; h1 < 256; h1++) for (int h2 = h1 + 1; h2 < 256; h2++) { if ((h1 ^ h2) <= h2) continue;
    int a = h1, b = h2, q1 = __builtin_ctz(a); if ((b >> q1) & 1) b ^= a; int q2 = __builtin_ctz(b); if ((a >> q2) & 1) a ^= b;
    int k = 0; for (int j = 0; j < 8; j++) if (j != q1 && j != q2) { int v = 1 << j; if ((a >> j) & 1) v |= 1 << q1; if ((b >> j) & 1) v |= 1 << q2; KB[ns][k++] = v; }
    for (int r = 0; r < 6; r++) if (par(KB[ns][r] & h1) || par(KB[ns][r] & h2)) { fprintf(stderr, "bug\n"); return 1; }
    H1[ns] = h1; H2[ns] = h2; ns++; }
  static unsigned char PT[10795][4][64];
  for (int s = 0; s < ns; s++) for (int c = 0; c < 4; c++) { int b0 = -1; for (int p = 0; p < 256; p++) if (par(p & H1[s]) == (c & 1) && par(p & H2[s]) == (c >> 1)) { b0 = p; break; }
    for (int t = 0; t < 64; t++) { int q = b0; for (int rr = 0; rr < 6; rr++) if ((t >> rr) & 1) q ^= KB[s][rr]; PT[s][c][t] = q; } }
  long T[2][16]; memset(T, 0, sizeof T);
  /* index: 0 pairs,1 degenerate,2 nondeg,3 nondeg&lastred,4 deg&!lastred,5 case0,6 case1,7 case2,8 case2&lastred,9 case1&predicted-gate-degenerate,
     10..13 case1 predicted gate 0..3 */
  for (int wi = 0; wi < 32768; wi++) {
    int r = wi, gm = r & 7; r >>= 3; int b3 = r & 7; r >>= 3; int a3 = r & 7; r >>= 3; int b2 = r & 3; r >>= 2; int a2 = r & 3; r >>= 2; int b1 = r & 1; r >>= 1; int a1 = r & 1;
    int al[4] = {0, a1, a2, a3}, be[4] = {0, b1, b2, b3};
    int red = (a1 <= b1) && (a2 <= b2) && (a3 <= b3);
    int z[4][256], Phi[256];
    for (int p = 0; p < 256; p++) { int zz[4];
      for (int i = 0; i < 4; i++) { int A = (p >> i) & 1, B = (p >> (4 + i)) & 1; for (int j = 0; j < i; j++) { if ((al[i] >> j) & 1) A ^= zz[j]; if ((be[i] >> j) & 1) B ^= zz[j]; } zz[i] = A & B; z[i][p] = zz[i]; }
      int o = zz[3]; for (int j = 0; j < 3; j++) if ((gm >> j) & 1) o ^= zz[j]; Phi[p] = o; }
    for (int s = 0; s < ns; s++) {
      int h1 = H1[s], h2 = H2[s];
      u64 tab[4] = {0}, ztab[4][3]; memset(ztab, 0, sizeof ztab);
      for (int c = 0; c < 4; c++) for (int t = 0; t < 64; t++) if (Phi[PT[s][c][t]]) tab[c] |= 1ULL << t;
      int aff[4], na = 0;
      for (int c = 0; c < 4; c++) { u64 t = tab[c]; static const u64 M[6] = {0x5555555555555555ULL,0x3333333333333333ULL,0x0f0f0f0f0f0f0f0fULL,0x00ff00ff00ff00ffULL,0x0000ffff0000ffffULL,0x00000000ffffffffULL};
        for (int i = 0; i < 6; i++) t ^= (t & M[i]) << (1 << i);
        aff[c] = (t & ~(1ULL | 2ULL | 4ULL | 16ULL | 256ULL | 65536ULL | (1ULL << 32))) == 0; na += aff[c]; }
      if (!na) continue;
      for (int c = 0; c < 4; c++) for (int t = 0; t < 64; t++) for (int j = 0; j < 3; j++) if (z[j][PT[s][c][t]]) ztab[c][j] |= 1ULL << t;
      int Hs[3] = {h1, h2, h1 ^ h2};
      int deg = 0; for (int i = 0; i < 4; i++) { int fa = 1 << i, fb = 1 << (4 + i);
        for (int q = 0; q < 3; q++) { if (al[i] == 0 && Hs[q] == fa) deg = 1; if (be[i] == 0 && Hs[q] == fb) deg = 1; if (al[i] == be[i] && Hs[q] == (fa | fb)) deg = 1; } }
      /* dim pi(H), pi(h) = (bit 3, bit 7) */
      int pis = 0; for (int q = 0; q < 3; q++) { int pu = (Hs[q] >> 3) & 1, pv = (Hs[q] >> 7) & 1; pis |= 1 << (pu | (pv << 1)); }
      pis &= ~1; int d = __builtin_popcount(pis) == 0 ? 0 : (__builtin_popcount(pis) == 1 ? 1 : 2);
      int pred_ok = 0, pred_gate = -1;
      if (d == 1) { int h0 = -1, hh = -1; for (int q = 0; q < 3; q++) { if (((Hs[q] >> 3) & 1) == 0 && ((Hs[q] >> 7) & 1) == 0) h0 = Hs[q]; else hh = Hs[q]; }
        (void)h0; int pu = (hh >> 3) & 1, pv = (hh >> 7) & 1; int coef = (pu && !pv) ? al[3] : (!pu && pv) ? be[3] : (al[3] ^ be[3]);
        pred_gate = coef == 0 ? 3 : 31 - __builtin_clz(coef);
        int i = pred_gate, fa = 1 << i, fb = 1 << (4 + i);
        for (int q = 0; q < 3; q++) { if (al[i] == 0 && Hs[q] == fa) pred_ok = 1; if (be[i] == 0 && Hs[q] == fb) pred_ok = 1; if (al[i] == be[i] && Hs[q] == (fa | fb)) pred_ok = 1; } }
      for (int c1 = 0; c1 < 4; c1++) { if (aff[c1]) continue; int nc0 = na; if (!nc0) continue;
        u64 rows[10]; int nr = 0; rows[nr++] = ~0ULL; for (int rr = 0; rr < 6; rr++) { u64 v = 0; for (int t = 0; t < 64; t++) if ((t >> rr) & 1) v |= 1ULL << t; rows[nr++] = v; }
        for (int j = 0; j < 3; j++) rows[nr++] = ztab[c1][j];
        int lastred = inspan(rows, nr, tab[c1]);
        for (int x = 0; x < 2; x++) { if (x == 1 && !red) continue; long *TT = T[x];
          TT[0] += nc0; if (deg) TT[1] += nc0; else { TT[2] += nc0; if (lastred) TT[3] += nc0; }
          if (deg && !lastred) TT[4] += nc0;
          TT[5 + d] += nc0; if (d == 2 && lastred) TT[8] += nc0; if (d == 1 && pred_ok) TT[9] += nc0; if (d == 1) TT[10 + pred_gate] += nc0; } } } }
  for (int x = 0; x < 2; x++) printf("%s: pairs %ld | degenerate %ld, non-degenerate %ld (last gate redundant on C1: %ld) | degenerate with last gate NOT redundant: %ld | case0 %ld, case1 %ld (predicted gate degenerate: %ld; gates 1..4: %ld %ld %ld %ld), case2 %ld (last gate redundant: %ld)\n",
    x ? "swap-reduced" : "all wirings ", T[x][0], T[x][1], T[x][2], T[x][3], T[x][4], T[x][5], T[x][6], T[x][9], T[x][10], T[x][11], T[x][12], T[x][13], T[x][7], T[x][8]);
  return 0; }
```
