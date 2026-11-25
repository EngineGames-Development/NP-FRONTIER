# AUDIT-002: PNE-001 at level 3 (Lemmas 11, 12, 14, 14(b′), 15, Corollary 13, Theorems 16 and 17)

- **Document audited:** `research/proofs/PNE-001-restriction-depth-and-fresh-variables.md`, lines 89–162, as of 2026-11-25. Line 159 (Dependencies) was rewritten by the main session while this audit ran; see I-5.
- **Auditor:** Agent F (adversarial reviewer), fresh context, 2026-11-25.
- **Taken as given** (audited separately, AUDIT-001): Lemmas 1–10. In particular Lemma 1, Theorem 4 (including the Case C identity), Corollary 5 and Lemma 9.
- **Read:**
  - the whole proof document;
  - the code: `EXP-005/doubly_cheap.py`, `EXP-005/check_lemma15.py`, `EXP-006/family.py`, `EXP-006/run_reps.py`, `EXP-002/first_gate_extension.py`, `EXP-002/first_gate_general.py`, `EXP-002/verify_s2_5.py`, `EXP-002/dpdt.py`, `EXP-001/mc.py`, `EXP-001/bfs4.py`;
  - the data outputs: `EXP-006/orbits.json`, `EXP-006/results.json`, `EXP-006/run_reps.log`, `EXP-006/run_drat_level3.{sh,log}`, `EXP-006/drat_recheck_*.log`, `EXP-002/drat_trim_yg_star.log`, and the list of 38 UNSAT functions in `EXP-002/sample5_results.json`.
- **Not read:** other research notes, READMEs, cycle reports, AUDIT-001.
- **No author script was executed.** Every computation below uses code I wrote: C and Python in an ephemeral scratch directory. The two core programs are reproduced in Appendix A.

## Verdicts

| Claim | Verdict |
|---|---|
| Lemma 11 (with Remarks 1–2 as used later) | SURVIVES |
| Lemma 12 | SURVIVES |
| Corollary 13, its "second proof of Proposition 10", and the scope bullets | SURVIVES |
| Lemma 14 (a), (b) | SURVIVES |
| Lemma 14(b′) | SURVIVES |
| Lemma 15 | SURVIVES (wording imprecision I-1) |
| Theorem 16 | SURVIVES (cosmetic issues I-2, I-3) |
| EXP-006 computational claims: family size, 33 orbits, 31 orbits in S_2, 2 orbits certified | SURVIVES; independently reproduced |
| **Theorem 17** | **SURVIVES** |

No finding of type BROKEN or GAP. Every issue below is cosmetic, informational or procedural.

## 1. Claim-by-claim review

### Lemma 11 (line 89)

**Claim.** Let m ≥ 1, and assume (H): MC(t·h) = MC(h)+1 for every non-constant h with MC(h) < m, on any number of variables. Let g be non-constant with MC(g) = m = MC(yg). Then:
- (a) some v ≠ 0 has both restrictions g|_{⟨v,x⟩=c} constant or of MC ≤ m−2;
- (b) for F = yg and admissibility at level m, (v,0) is admissible iff (v,1) is, and (0,1) is never admissible.

**Checks.**
- MC(F) ≥ MC(g) by setting y = 1 (F2). So an m-gate circuit for F is optimal, and Lemma 9 applies: it needs MC(F) ≥ m ≥ 1 and an m-gate circuit. OK.
- If v = 0, then u = e_y. F|_{y=1} = g has MC m > m−1, so u is not admissible. OK.
- If s = 1, the restriction to {y = ⟨v,x⟩+c} is (⟨v,x⟩+c)·g(x) ≅ t·g|_{⟨v,x⟩=1+c} (Case C identity, given). Admissibility quantifies over both c, so the relabeling c ↦ 1+c is harmless. Hence (v,0) admissible ⇔ (v,1) admissible ⇔ for both c, MC(t·g|_{⟨v,x⟩=c}) ≤ m−1. Part (b) uses neither (H) nor MC(yg) = m.
- MC(t·h) ≤ m−1 implies MC(h) ≤ m−1 (set t = 1). If h is non-constant, (H) then gives MC(h) ≤ m−2. Constant halves are exactly the case (H) excludes (MC(t·0) = 0), and the conclusion lists them separately. OK.
- Edge cases m = 1, 2: the conclusion forces MC(g) ≤ 1 < m, so no such g exists. This is consistent with Corollary 5.

**Remarks 1–2.** "MC ≤ 2 forces MC = D" is correct. If D(h) = 1, h is a multiplexer of two affine halves, so MC(h) ≤ 1; combine with Lemma 1. Remark 2's equivalence holds because D ≤ 1 ⇔ MC ≤ 1. See I-6.

**Numerical checks.**
- 20,000 random 5-variable g with MC ≥ 3, admissibility at level 3 computed with my own S_2: 0 mismatches between (v,0) and (v,1), and y was never admissible.
- All 1,801,472 five-variable functions with MC = 2: none has a direction with both halves affine, so D = 2 = MC for all of them.

### Lemma 12 (line 101)

**Checks.**
- Both directions come from the same first gate, and v1, v2 ≠ 0 by the proof of Lemma 11.
- If v1 = v2 = v, then s1 ≠ s2, because Lemma 9 gives distinct directions. At y = 1 the inputs are ℓ+s1+e and ℓ+s2+e′, with ℓ = ⟨v,x⟩. They are either equal or complementary, so the product is ℓ+const or 0, which is affine.
- An affine gate is removed by substituting its value into later forms. That leaves m−1 gates for g, contradicting MC(g) = m.
- Two distinct nonzero vectors over F_2 are linearly independent, which is what Theorem 16 needs.

No issue.

### Corollary 13 (line 104)

**Checks.**
- MC(g) ≤ MC(yg) ≤ MC(g)+1, so MC(yg) ∈ {3,4}.
- If MC(yg) = 3, Lemma 12 applies with m = 3. Its hypothesis (H) at m = 3 is PNE-001 for non-constant h with MC ≤ 2, which holds by Remark 1 and Corollary 5.
- At m = 3, "constant or MC ≤ 1" is the same as "MC ≤ 1". OK.

**Second proof of Proposition 10.** My code finds exactly one cheap direction for g* (x2), and g* ∉ S_2. The stated 3-gate circuit evaluates to 0xfff3d212.

**Scope bullets.**
- Of the 38 functions, 31 have exactly one cheap direction. The other 7 have three, and in each case those three together with 0 form a 2-dimensional subspace.
- The claim "MC = 3 ⇒ at most one cheap direction" is indeed false. Witness: 0x01234567, with MC 3 and cheap directions {x1, x2, x1+x2}.

### Lemma 14(a), 14(b), 14(b′) (lines 114–120)

**Checks.**
- (a) The computation h|_{x2=1}+h|_{x2=0} = a0b1+a1b0+a1b1+(γ|_{x2=1}+γ|_{x2=0}) is correct.
- (b′) The split on x1 gives g00+g01 and g10+g11 affine; the split on x2 gives g00+g10 and g01+g11 affine. The other two differences are sums of these. So g = g00+x1ℓ1+x2ℓ2+x1x2ℓ3 with ℓ1 = g00+g10, ℓ2 = g00+g01 and ℓ3 = Σ g_ab, all affine in x′. OK.

**Exhaustive check at n = 5.** All 122,880 functions with x1 and x2 cheap: 0 violations of 14(b′).

### Lemma 15 (line 122)

**Checks.**
- g00 is a restriction of a half with MC ≤ 1, so MC(g00) ≤ 1 and g00 = αβ+γ.
- Since g00 is not affine, α_lin and β_lin are linearly independent.
- If (ℓ2)_lin ∉ U, then α_lin, β_lin, (ℓ2)_lin and x2 are linearly independent, so the polar form of g|_{x1=0} has rank 4. That contradicts rank ≤ 2. The same argument applies to ℓ1 and to ℓ2+ℓ3. See I-1 for wording.
- G(X1,X2,A,B) = AB + X1ℓ1(A,B) + X2ℓ2(A,B) + X1X2ℓ3(A,B) has degree ≤ 3.
- (x1, x2, α, β) extends to an affine coordinate system. So MC(g) = MC(G) by (F1) and (F3).
- Every 4-variable function of degree ≤ 3 has MC ≤ 2. Independently confirmed in V-2: the 4-variable MC ≤ 2 set is exactly the degree ≤ 3 set.

**Exhaustive checks with my own code.**
- **n = 5.** 57,344 functions g have x1, x2 cheap and g00 non-affine; all have MC ≤ 2. The 21,504 functions with x1, x2 cheap and MC ≥ 3 all have four affine quarters, and all are family members.
- **n = 6.** I normalized g00 = u1u2+γ. This is without loss of generality: an affine map of x′ preserves both cheapness hypotheses and MC. I then enumerated all γ, ℓ1, ℓ2, ℓ3 affine in x′ (1,048,576 functions). Of these, 16,384 have x1, x2 cheap, and all have MC ≤ 2 by an exhaustive 6-variable MC ≤ 2 test. That test agreed with the 5-variable bitmap on 3,000 dummy-padded samples.
- The count 16,384 = 32·4³·8 is exactly what the proof's necessary condition (ℓ_i)_lin ∈ U predicts. It was obtained with a cheapness test that does not use that condition.

### Theorem 16 (line 132)

**Quantifier structure.** A level-3 counterexample is exactly a g with MC(g) = 3 = MC(yg), because MC(g) ≤ MC(yg) ≤ MC(g)+1. OK.

**Proof bullets.**
1. Lemma 12 at m = 3 gives two cheap directions. The linear change of x-coordinates leaves y untouched, and cheapness is carried along with the hyperplanes. OK.
2. Lemma 15 in contrapositive form (MC(g) = 3) gives g00 affine; then Lemma 14(b′) applies. OK.
3. The change of coordinates acts on x′ only, with x1, x2 fixed. OK (see I-3 for n = 4).
4. Vacuous; see I-2.
5. g = G′ + w, and the remaining x′-coordinates are dummies. OK.
6. MC(G′) = MC(g) = 3 by (F1) and (F3). OK.
7. MC(yG′) ≤ MC(yg) by restricting w1 and the dummies to 0 (F2), and MC(yG′) ≥ MC(G′) by setting y = 1. Note that y·w1 is not affine, so MC(yg) and MC(yG′) need not be equal. The proof uses only the ≤ direction, which is the correct one. OK.

**The "iff".** The converse is trivial: G′ is itself a function with MC 3.

**The count.** 16³·16 = 65,536 distinct functions is correct (c is redundant with the constant of λ). I reproduced 65,536 distinct truth tables.

**Edge cases you asked about.**
- *w1 absent:* g = G′ plus dummy variables. Trivial.
- *ℓ3 constant:* G′ is then quadratic in 5 variables, of rank ≤ 4, so MC ≤ 2. Confirmed: no MC ≥ 3 member has ℓ3 constant, and none has rank((ℓ1)_lin, (ℓ2)_lin, (ℓ3)_lin) < 3.
- *Dropped constant c:* handled by complementation, which preserves MC(G′) and MC(yG′) because y(G′+1) = yG′+y.
- *Degenerate gates:* excluded by Lemma 9 in the authors' certificate. My lemma-free search (V-4) covers them implicitly through the test F ∈ W2.

### Theorem 17 (line 144)

- **Case MC ≤ 2.** Correct, via Remark 1 and Corollary 5.
- **Symmetry group.** For an affine bijection T = T_x × T_u of F_2^5, (y·G′)∘(T × id_y) = y·(G′∘T). So T preserves MC(G′) and MC(yG′) by (F1). Complementation preserves both, as above. The family is the set of functions of degree ≤ 2 in (x1, x2) whose coefficients are affine in u, and AGL(2) × AGL(3) maps that set to itself. (Shears u ↦ u+Mx also preserve it but are not used. Using a subgroup is conservative.)
- **Orbits, reproduced** (V-3): 33 orbits, with the multiset of sizes identical to `orbits.json`. Exactly 10,752 members modulo complement lie outside S_2. They form exactly two orbits, each of size 5,376, with minima 0x01234567 and 0x0167abcd. No orbit mixes S_2 and non-S_2 members. The ANF formulas on lines 151–152 match the truth tables.
- **S_2 is exactly MC ≤ 2:** V-1.
- **Certificates:** reproduced without any lemma (V-4) and by SAT (V-5).
- **The Lemma 12 filter in `run_reps.py`.** It is valid because MC(G′) = 3: G′ ∉ S_2, and MC ≤ 3 by the explicit circuit z1 = x1ℓ3, z2 = x2(ℓ2+z1), z3 = x1ℓ1. A 3-gate circuit for yG′ whose first-gate directions share their x-part would give a 2-gate circuit for G′ at y = 1.
- **Enumeration in `run_reps.py`.**
  - It tests all pairs of admissible directions (each of the 63 directions is tested), skips pairs with equal x-part, and tries all 4 constants.
  - `extends` covers every W2 = W1 + ⟨z2⟩ with z2 ∉ W1, using canonical reduced-echelon coset representatives. The case z2 ∈ W1 is covered by another choice of z2 together with the test F ∈ W2.
  - It then covers every third product, plus the test F ∈ W2 itself.
  - `dpdt.hyperplane_index_lists` gives affine parametrizations (kernel basis e_j + v_j e_piv, offset e_piv).

## 2. Issues

**I-1. Lemma 15, line 124. Severity: cosmetic.**
- The text says "the quadratic part … is a single product of two linear forms". Over F_2 with x_i² = x_i, the product a_lin·b_lin also contains the linear terms Σ a_i b_i x_i. So the degree-2 component of ab+c is the degree-2 part of a_lin·b_lin, not that product itself.
- The fact actually used is correct. The polar form B(x,x′) = f(x+x′)+f(x)+f(x′)+f(0) of a function of degree ≤ 2 equals a_lin ∧ b_lin and has rank ≤ 2. The rank-4 claim for u1u2 + x2u3 is also correct.
- No effect on validity.

**I-2. Theorem 16, line 139. Severity: cosmetic.**
- "Terms a1x1 and a2x2 are absorbed into the constants of ℓ1, ℓ2" is vacuous. g00 = g|_{x1=x2=0} is by definition a function of x′ only, and ℓ1, ℓ2 already carry their constants (ℓ1 = g00+g10, and so on).
- The sentence suggests a different decomposition from the one Lemma 14(b′) defines. Harmless.

**I-3. Theorem 16, line 138. Severity: cosmetic.**
- The proof assumes x′ has at least 3 coordinates (n ≥ 5). For n = 4, pad with a dummy u3 using (F3), or use Corollary 6.
- Also implicit: n ≥ 4, because MC(g) = 3 is impossible on 3 or fewer variables. Harmless.

**I-4. Theorem 17, line 154 ("48 candidates"). Severity: informational.**
- The 48 candidates are only 4 distinct cases. (ℓ1+e)(ℓ2+e′) ≡ ℓ1ℓ2 modulo affine functions, so the constants do not change W1. And the 12 admissible pairs with distinct x-parts span only 4 two-dimensional subspaces: {1,2,3}, {1,34,35}, {2,33,35} and {3,33,34} in bit notation, with y = 32.
- In this instance the Lemma 12 filter is also implied by a stronger form of Lemma 9. Restricting along ℓ1+ℓ2 kills the first gate as well, so all three nonzero directions of span(ℓ1, ℓ2) must be admissible. The three filtered-out subspaces {1,32,33}, {2,32,34} and {3,32,35} contain y = 32, which is not admissible.
- No effect on correctness.

**I-5. Line 159 and `EXP-006/run_drat_level3.log`. Severity: low (process).**
- When this audit started, `run_drat_level3.log` contained no drat-trim verdict for either instance. For 0x01234567 it had only "c verification time: 664.000 seconds"; for 0x0167abcd drat-trim was still running.
- The cause, according to the comment the main session later added to the script: drat-trim writes "\rs VERIFIED", which the script's `grep "^s "` did not match. I did not check that explanation myself. At that point the document deferred the DRAT status to the cycle report.
- During the audit the main session made three changes:
  - added `drat_recheck_0x01234567.log` and `drat_recheck_0x0167abcd.log`, both reading "s VERIFIED" (643.280 s and 748.419 s);
  - changed `run_drat_level3.sh` to translate "\r";
  - rewrote line 159.
- I did not audit `drat_certify.py`, the CNF encoding. The DRAT result therefore certifies only that this particular CNF is unsatisfiable. Whether that CNF faithfully encodes "MC(yG′) ≤ 3" is not checked by me.
- Theorem 17 does not depend on it: V-4 and V-5 confirm the result independently.

**I-6. Remark 1, and Theorem 17 line 146. Severity: informational.**
- "MC ≤ 2 forces MC = D" has no separate proof. The step it needs, D(h) = 1 ⇒ MC(h) ≤ 1, is the multiplexer sentence of Remark 1 combined with Lemma 1.
- The claim is correct and was confirmed exhaustively at n = 5.

**I-7. Line 112 ("settled by the exhaustive first-gate certificates of EXP-004"). Severity: informational, outside scope.**
- EXP-004 was not in my reading list, and I did not check it.
- Two of those seven functions (0x06e890b2, 0x10dce02c) were certified directly by my code (V-6), and Theorem 17 covers all seven anyway.

## 3. What I verified independently, and how

**V-1. S_2 for 5 variables (C, my own construction).**
- *Method.* The first gate z1 runs over the 155 two-dimensional subspaces of linear forms (z1 = ℓ1ℓ2; constants add only affine terms). Set W1 = W0 ∪ (W0+z1), form every product P = A·B with A, B ∈ W1 (including A = B and 0), and mark P+w for every w ∈ W1, in a 2³²-bit bitmap.
- *Why this is complete.* A 2-gate circuit outputs an element of span(W1, z2) with z2 = A2B2 and A2, B2 ∈ W1. An affine first gate reduces to the 1-gate case, which is included.
- *Results.* |MC ≤ 1| = 9,984 (= 64 + 155·64) and |S_2| = 1,811,456. The member list is identical, element for element, to `EXP-006/S2_5vars.npy`.
- *Semantic cross-check.* My own SAT encoding has no symmetry breaking, and every satisfying assignment is decoded and simulated gate by gate. On 250 sampled functions (103 in S_2, 147 not) there were 0 disagreements.
- *Not externally confirmed.* Two WebSearch queries found no published count of 5-variable functions with MC ≤ 2.

**V-2. 4 variables.** The same construction gives |MC ≤ 1| = 1,152 and |MC ≤ 2| = 32,768, and the MC ≤ 2 set is exactly the set of functions of degree ≤ 3, with 0 exceptions in either direction. This is the fact Lemma 15 uses.

**V-3. Family and orbits (Python, my own code).**
- 65,536 distinct functions, closed under complement; 32,768 modulo complement.
- My generators: the 5 translations, swap of x1 and x2, x2 ← x1+x2, the 3-cycle of u, swap of u1 and u2, and u2 ← u1+u2. Closure on point permutations gives group order 32,256 = 24·1,344 = |AGL(2,2)|·|AGL(3,2)|.
- No generator maps a member outside the family.
- Union-find over the generators plus complementation gives the orbit results quoted for Theorem 17 in §1.

**V-4. Certificates, using no lemmas (C).**
- *Method.* An exhaustive search for 3-AND circuits on 6 variables. It uses only the span characterization of circuits and two elementary facts:
  - W1 depends only on span(ℓ1, ℓ2), so 651 first-gate subspaces cover every non-degenerate first gate;
  - A·B modulo W depends only on span(A, B) modulo ⟨1⟩, because (A+1)B = AB+B and (A+B)B = AB+B. So second gates range over the 2,667 two-dimensional subspaces of W1/⟨1⟩, and third gates over the 10,795 of W2/⟨1⟩.
- *What it does not use.* Lemma 9, Lemma 12, admissibility, or S_2. Reduction modulo W uses a reduced echelon basis and `pext`.
- *Results for 0x01234567 and for 0x0167abcd.* 651 first gates, 1,526,595 distinct second-gate cosets, 16,479,593,025 third-gate checks, outcome NONE.
  - The 1,526,595 cosets are 2,345 per first gate, matching the "2,345 distinct second-gate spans" of Proposition 10.
  - So MC(y·G′) ≥ 4 for both representatives, independently of the authors' code and of Lemmas 9 and 12.
- *Positive controls.* x1x2x3x4, three random 3-gate circuits and one affine function: each FOUND, with the witness re-checked by an independent Gaussian elimination.
- *Negative controls.* x1x2x3x4x5 (degree 5, so MC ≥ 4) and y·g* (Proposition 10): both NONE.
- *Admissible directions.* My own hyperplane parametrization uses the lowest set bit as pivot, where `dpdt.py` uses the highest. It gives {1,2,3,33,34,35} for both representatives and {2,34} for y·g*, as the document states.

**V-5. Certificates by SAT.**
- My own CNF encoding (PySAT with CaDiCaL 1.9.5) has no symmetry-breaking constraints, so UNSAT means no 3-AND circuit exists at all.
- Both representatives: UNSAT at k = 3 (378 s and 384 s).
- Positive controls at n = 6, k = 3: y·0x0123cdef and y·0x12569ade (representatives of MC ≤ 2 orbits) are SAT, and the decoded circuits simulate correctly.
- No proof certificate was produced for these UNSAT answers, so this is a cross-check, not a proof.

**V-6. Orbit sanity check and end-to-end checks (the V-4 search).**
- Six random non-representative MC-3 family members (0x08c419d5, 0x14c98d50, 0x3b7f195d, 0x8fdabce9, 0x17246053, 0x9e34ad07): all NONE.
- Four of the 38 sample functions, not in family coordinates:
  - 0x05a01111 and 0x08adcbcb, which have one cheap direction (the Corollary 13 case);
  - 0x06e890b2 and 0x10dce02c, which have three cheap directions.
- All four give NONE, that is MC(yg) = 4 directly.

**V-7. Lemma-level checks.** As listed in §1: the Lemma 11 pairing, Remark 1, Lemma 14(b′), Lemma 15 at n = 5 and n = 6, the Corollary 13 scope, and the g* circuit.

## 4. Barriers, literature, relevance

- **Barriers.** Theorem 17 is a statement about one measure, multiplicative complexity, at levels ≤ 3. It is not a superpolynomial lower bound and gives no oracle or "natural property" argument, so the relativization, natural-proofs and algebrization barriers do not apply to it.
- **Consistency with known results.**
  - Every 5-variable function has MC ≤ 4: Sönmez Turan and Peralta, "The Multiplicative Complexity of Boolean Functions on Four and Five Variables", LightSec proceedings, LNCS, published 2015, DOI 10.1007/978-3-319-16363-5_2. Retrieved via WebSearch; I confirmed the title and the "at most four AND gates" statement from search snippets only, not the paper text.
  - The 6-variable maximum is 6 (Çalık, Sönmez Turan, Peralta; recalled, not verified).
  - No contradiction found.
- **Novelty.** Not assessed beyond these searches.
- **Relevance to P vs NP.** Remote. The document's own "Significance and limits" paragraph (line 162) is accurate.

## 5. What I could not check

- `drat_certify.py` and the CNF/DRAT artifacts (not in scope; see I-5).
- EXP-004 (line 112), and Part 2 of EXP-005 (the random search), beyond confirming that MC-3 functions with two or more cheap directions exist.
- Lemmas 1–10, taken as given per instructions. Theorem 17's reduction depends on Lemma 9 through Lemma 12. The certificates themselves (V-4) do not.
- No Lean formalization exists for any audited claim (document line 160), so `#print axioms` checks do not apply. The proof is computer-assisted with unformalized Python, and my confirmations are unformalized C and Python.
- External confirmation of |S_2| = 1,811,456 from the literature.
- My scripts live in an ephemeral scratch directory; Appendix A reproduces the two load-bearing programs.

## Summary

- Theorem 17 survives, as do Lemmas 11, 12, 14, 14(b′), 15, Corollary 13 and Theorem 16. Every inference in the reduction checks out, including the coordinate changes, the handling of w1, the constants and degenerate gates, and the direction of the inequality MC(yG′) ≤ MC(yg).
- The computational core is reproduced by code independent of the authors':
  - S_2 has 1,811,456 elements and matches theirs exactly;
  - the 4-variable fact behind Lemma 15 holds;
  - the family has 33 orbits, of which exactly 2, each of size 5,376, lie outside S_2;
  - a complete search that uses no lemmas shows MC(y·G′) ≥ 4 for both representatives, confirmed by my own SAT encoding, with positive and negative controls.
- Lemmas 14(b′) and 15 also hold exhaustively at n = 5, and at n = 6 up to symmetry.
- Issues are cosmetic or procedural (I-1 to I-7). The most substantive is I-5: when the audit began, the committed log did not show the DRAT verification, and the CNF encoding behind it was not audited here.

## Appendix A. Core verification programs

Condensed from the versions I ran: statistics counters and unused declarations are removed, and the search logic is unchanged.

Build and run: `gcc -O2 -march=native -o cert cert.c`, then `./cert full 0x01234567 0x0167abcd`. Running `./cert full64 <hex>` tests an arbitrary 6-variable truth table. About 60 s per function on one core.

`s2lib.h` (S_1 and S_2 bitmaps for n ≤ 5):

```c
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static inline uint32_t tt_var(int n, int j) { uint32_t t = 0; for (int p = 0; p < (1 << n); p++) if ((p >> j) & 1) t |= 1u << p; return t; }
static inline uint32_t tt_one(int n) { return n == 5 ? 0xFFFFFFFFu : ((1u << (1 << n)) - 1u); }
static inline uint32_t tt_lin(int n, int mask) { uint32_t t = 0; for (int j = 0; j < n; j++) if ((mask >> j) & 1) t ^= tt_var(n, j); return t; }
static inline void bm_set(uint8_t *bm, uint32_t f) { bm[f >> 3] |= (uint8_t)(1u << (f & 7)); }
static inline int bm_get(const uint8_t *bm, uint32_t f) { return (bm[f >> 3] >> (f & 7)) & 1; }
static int affine_list(int n, uint32_t *out) { int c = 0; for (int m = 0; m < (2 << n); m++) out[c++] = ((m & 1) ? tt_one(n) : 0) ^ tt_lin(n, m >> 1); return c; }
static int build_s12(int n, uint8_t *s1, uint8_t *s2) {
  uint32_t W0[64], W1[128]; int n0 = affine_list(n, W0), nsub = 0;
  for (int i = 0; i < n0; i++) { if (s1) bm_set(s1, W0[i]); if (s2) bm_set(s2, W0[i]); }
  int L = 1 << n;
  for (int l1 = 1; l1 < L; l1++) for (int l2 = l1 + 1; l2 < L; l2++) {
    if (!((l1 ^ l2) > l2)) continue;               /* one representative pair per 2-dim subspace */
    nsub++;
    uint32_t z1 = tt_lin(n, l1) & tt_lin(n, l2);
    for (int i = 0; i < n0; i++) { W1[i] = W0[i]; W1[n0 + i] = W0[i] ^ z1; }
    int n1 = 2 * n0;
    if (s1) for (int i = 0; i < n1; i++) bm_set(s1, W1[i]);
    if (s2) for (int i = 0; i < n1; i++) for (int j = i; j < n1; j++) {
      uint32_t P = W1[i] & W1[j];
      for (int k = 0; k < n1; k++) bm_set(s2, P ^ W1[k]);
    }
  }
  return nsub;
}
```

`cert.c` (the core of the exhaustive 3-AND search; the `main` driver, which builds F = y·g, computes admissible directions for reporting and prints counters, is omitted):

```c
#include "s2lib.h"
#include <immintrin.h>
typedef uint64_t u64;
static u64 X6[6];   /* X6[j] = truth table of variable j on 64 points; x1..x5 = bits 0..4, y = bit 5 */
static u64 lin6(int m) { u64 t = 0; for (int j = 0; j < 6; j++) if ((m >> j) & 1) t ^= X6[j]; return t; }
typedef struct { int k; u64 v[12]; int piv[12]; u64 pm; u64 tab[1 << 12]; } Basis;
static int badd(Basis *B, u64 v) {
  for (int i = 0; i < B->k; i++) if ((v >> B->piv[i]) & 1) v ^= B->v[i];
  if (!v) return 0;
  int p = 63 - __builtin_clzll(v);
  for (int i = 0; i < B->k; i++) if ((B->v[i] >> p) & 1) B->v[i] ^= v;
  B->v[B->k] = v; B->piv[B->k] = p; B->k++; return 1;
}
static void bfin(Basis *B) {
  int ord[12], k = B->k; for (int i = 0; i < k; i++) ord[i] = i;
  for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) if (B->piv[ord[j]] < B->piv[ord[i]]) { int t = ord[i]; ord[i] = ord[j]; ord[j] = t; }
  B->pm = 0; for (int i = 0; i < k; i++) B->pm |= 1ull << B->piv[i];
  for (int idx = 0; idx < (1 << k); idx++) { u64 t = 0; for (int i = 0; i < k; i++) if ((idx >> i) & 1) t ^= B->v[ord[i]]; B->tab[idx] = t; }
}
static inline u64 red(const Basis *B, u64 f) { return f ^ B->tab[_pext_u64(f, B->pm)]; }
static int extends(u64 F, u64 z1, u64 wit[5]) {   /* 1 iff some 3-AND circuit for F has first gate in z1 + W0 */
  Basis B1; B1.k = 0; badd(&B1, ~0ull); for (int j = 0; j < 6; j++) badd(&B1, X6[j]);
  if (!badd(&B1, z1)) return -1;
  bfin(&B1);
  u64 q1[7]; for (int j = 0; j < 6; j++) q1[j] = X6[j]; q1[6] = z1;
  u64 e1[128]; for (int a = 0; a < 128; a++) { u64 t = 0; for (int i = 0; i < 7; i++) if ((a >> i) & 1) t ^= q1[i]; e1[a] = t; }
  static u64 R[3000], RA[3000], RB[3000]; int nr = 0;
  for (int a = 1; a < 128; a++) for (int b = a + 1; b < 128; b++) {
    if ((a ^ b) <= b) continue;                     /* one pair per 2-dim subspace of W1/<1> */
    u64 r = red(&B1, e1[a] & e1[b]);
    if (r) { R[nr] = r; RA[nr] = e1[a]; RB[nr] = e1[b]; nr++; }
  }
  static int perm[3000]; for (int i = 0; i < nr; i++) perm[i] = i;
  for (int i = 1; i < nr; i++) { int p = perm[i], j = i; while (j > 0 && R[perm[j - 1]] > R[p]) { perm[j] = perm[j - 1]; j--; } perm[j] = p; }
  for (int ii = 0; ii < nr; ii++) {
    int i = perm[ii]; if (ii > 0 && R[perm[ii - 1]] == R[i]) continue;   /* distinct z2 cosets */
    Basis B2 = B1; badd(&B2, R[i]); bfin(&B2);
    u64 t = red(&B2, F);
    if (t == 0) { wit[0] = RA[i]; wit[1] = RB[i]; wit[4] = 1; return 1; }
    u64 q2[8]; for (int j = 0; j < 7; j++) q2[j] = q1[j]; q2[7] = R[i];
    u64 e2[256]; for (int a = 0; a < 256; a++) { u64 s = 0; for (int k = 0; k < 8; k++) if ((a >> k) & 1) s ^= q2[k]; e2[a] = s; }
    for (int a = 1; a < 256; a++) for (int b = a + 1; b < 256; b++) {
      if ((a ^ b) <= b) continue;                   /* one pair per 2-dim subspace of W2/<1> */
      if (red(&B2, e2[a] & e2[b]) == t) { wit[0] = RA[i]; wit[1] = RB[i]; wit[2] = e2[a]; wit[3] = e2[b]; wit[4] = 0; return 1; }
    }
  }
  return 0;
}
/* driver: for l1 < l2 < l1^l2 over the 63 nonzero linear forms (651 subspaces): if (extends(F, lin6(l1) & lin6(l2), w) == 1) -> FOUND
   (witness re-verified by independent Gaussian elimination); otherwise NONE, i.e. MC(F) >= 4.  F = y*g: bit p set iff p>>5 & 1 and g(p & 31). */
```
