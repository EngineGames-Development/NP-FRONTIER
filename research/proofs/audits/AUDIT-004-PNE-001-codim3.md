# AUDIT-004: PNE-001, codimension 3 (facts (P1), (P2), Lemma 32, Corollaries 33–35)

- **Document audited:** `research/proofs/PNE-001-codim3.md` at commit `bcdbb42` (208 lines, md5 `9020deb225fa97ff140dbaac23887850`).
  - During the audit the author committed `7b45ceb` (document md5 `3cd03d55729bf2b703185fd2b0567044`). Its only change to the document fills in the m = 5 row of the verification table. That row is checked in V-5 and agrees exactly. Nothing else in the document changed.
- **Auditor:** Agent F (adversarial reviewer), fresh context, 2026-11-25/26. The audit was interrupted by an API rate limit and a container restart; every computation reported here was run after the restart.
- **Taken as given** (audited in AUDIT-003): Lemmas 23, 24, 28, Lemma 30 with (IF′), and Corollaries 29 and 31 of `PNE-001-level4.md`. I re-read their proofs to check that they deliver what Lemma 32 uses.
- **Read:**
  - the whole document;
  - Part II of `PNE-001-level4.md` (notation, (F4), Lemmas 22–30, Corollaries 29 and 31);
  - AUDIT-003, and AUDIT-002 V-2;
  - EXP-018: `codim3.c`, `hc_lib.py`, `merge_check.py`, `README.md`, both logs, the header of `hc_dump.c`, and the data file `hc_sample.txt`;
  - EXP-001 `README.md`.
- **Not read:** the body of `hc_dump.c`; EXP-019 (later codimension-4 work, not under review).
- **Not run:** the author's programs. My own code reproduces both of their logs exactly from the same wiring sets (V-5).
- **Executed:** only my own programs, written for this audit and sharing no code with the project, in a scratch directory. The load-bearing ones are in Appendix A. No repository file other than this report was created or edited. CPU used: about 35 minutes.

## Verdicts

| Claim | Verdict |
|---|---|
| (P1), restriction to a hyperplane of w″-space (types 1–3) | SURVIVES |
| (P2), independence on E | SURVIVES |
| "Non-degeneracy gives the hypothesis of (P2)" | SURVIVES |
| Exits (X1), (X2), (X3) | SURVIVES |
| **Lemma 32 (every m)** | **SURVIVES.** Every case checked by hand. No counterexample in exhaustive tests at m = 3 and 4, nor in large samples at m = 5 and 6. Presentation corrections I-2, I-3, I-4. Case-by-case: |
| — dim π(H) = 0 | survives |
| — dim π(H) = 1: sub-cases (1,0), (0,1), (1,1); recursion through Ψ, H*, K*; cosets projecting into cosets of K* | survives. Relies on the *proof* of Lemma 30, which delivers exactly what is used (I-3) |
| — case (a) | survives |
| — case (b1), the merge | survives, with f_y, g_y read as coefficients on E (I-2) |
| — case (b2): expansion, sub-cases (i)–(iv), exits | survives |
| Corollary 33 | SURVIVES |
| Corollary 34 | SURVIVES WITH CORRECTION (citation of the 4-variable fact, I-1) |
| Corollary 35 and the finite level-5 reformulation | SURVIVES |
| Verification section and EXP-018 | Every number reproduced exactly, and no bug found in `codim3.c`. "Implements every case prediction" overstates what it tests (I-5) |
| Scope and novelty statements | No overclaim found |

No fatal or serious issue. No counterexample to Lemma 32 or to any intermediate claim of its proof.

## 1. Claim-by-claim review

### (P1)
- **Gates j < k.** They read only w_1, …, w_{2j} ⊆ {w_1, …, w_{2k−2}}. Neither the substitution for w_e nor the translation by τ = e_e touches these coordinates, so the gates are unchanged on E and τ-invariant.
- **Type 1.** On E, w_{2k−1} = c + ⟨t_{<k}, w″⟩, so A_k = Ã ∈ L_{<k} and z_k = Ã·B_k. Translation by e_{2k−1} adds 1 to A_k and fixes B_k = s.
- **Type 2.** Symmetric.
- **Type 3.** On E, B_k = A_k + D with D = c + ⟨t_{<k}, w″⟩ + (α_k+β_k)·z, so z_k = A_k(1+D). Translation by e_{2k} adds 1 to B_k, giving A_k·D = (Ã+1)s.
- **Form of s.** In all three types, s = (a coordinate of E) + (an element of L_{<k}). In type 3 that coordinate is w_{2k−1}, which is a coordinate of E because e = 2k.

### (P2)
- **j := max supp c, case j ≠ k.**
  - w_{2j−1} and w_{2j} are coordinates of E, because e ∈ {2k−1, 2k}.
  - Gates i < j do not read them. The substitution for w_e involves only coordinates ≤ 2k, so it introduces neither of them, whether j < k or j > k. Gates i > j do not occur.
  - In E-coordinates the ANF of z_j contains w_{2j−1}w_{2j} with coefficient 1, and no other term of the expression contains it. So the expression is not affine. Correct.
- **Case j = k.**
  - Let y be the E-coordinate inside s. It occurs in z_k and in ℓ. In type 3 it also occurs through the substitution w_e = c + w_{2k−1} + ⟨t_{<k}, w″⟩, but only inside ℓ, hence affinely.
  - Gates i < k do not contain y, and gates i > k do not occur.
  - Hence D_y = Ã + const, with Ã ∈ L_{<k} free of y. Correct.
- **The hypothesis is needed.** When Ã is constant, the kernel of (ℓ, c) ↦ (ℓ + c·z)|_E modulo constants has dimension 2, not 1. This holds in every such case tested (V-1).
- **Last step.** A linear form is constant on the affine hyperplane E iff ℓ ∈ {0, t}. Correct.

### Non-degeneracy gives the hypothesis of (P2)
- Ã ∈ L_{<k} is a function of w_1, …, w_{2k−2}, all of which are free on E.
- By the independence fact for the (k−1)-gate circuit, ⟨t_{<k}, ·⟩ + (coefficient vector)·z is constant iff the coefficient vector is 0 and t_{<k} = 0.
- This gives exactly the three stated conditions. In each, h_0 = (t,0,0) ∈ H is a Lemma-24 degeneracy vector of gate k. Correct.
- Edge case k = 1: Ã is always constant, and gate 1 is always degenerate (α_1 = β_1 = 0). Consistent.

### Exits
- (X1) is Lemma 24, and (X2) is immediate.
- (X3): substituting the span expression for z_j into the later gates and the output leaves m − 1 gates. For j = m this is the condition Φ|_C ∈ span(affine, z_{<m}|_C). Correct.

### Lemma 32: dim π(H) = 0 and dim π(H) = 1
- **dim π(H) = 0.** u and v are free on C_0, so D_uD_vΦ|_{C_0} = 1. Correct. The claim is unconditional, and no run found any affine coset with dim π(H) = 0 (V-3, V-4).
- **(p,q) = (1,0), first step.** v is free on C_0, because every h ∈ H has h_v = 0. So D_vΦ|_{C_0} = u + a. If α_m = 0, then ⟨h_1″, ·⟩ is constant on E_{d_0}, so h_1″ ∈ H_0″ and e_u ∈ H. Correct.
- **Projection claims.** Let ρ: F_2^{2m−2} → F_2^{2j*} be the projection and W = (H_0″)^⊥.
  - ρ(W)^⊥ = {x : (x,0) ∈ H_0″} = H*, so ρ(W) = K*.
  - Hence ρ(E_d) is a coset of K* for every d. Every coset of K maps *onto* a single coset of K*.
  - Ψ|_{E*} is affine, by composing with an affine section. Correct.
- **dim H* ≤ 1.** dim H* ∈ {0,1,2}, because H* embeds in H_0″.
  - dim H* = 0 contradicts the independence fact.
  - dim H* = 1 is Lemma 28 applied to the j*-gate circuit with output Ψ, whose last gate has coefficient 1. The vector (h*, 0, …, 0) lies in H. Correct.
- **dim H* = 2** (then H* = H_0″). I re-read Lemma 30's proof applied to (Ψ, K*):
  - its case dim π* = 0 is impossible;
  - in its case dim π* = 1, the degeneracy vector found is e_{2j*−1}, e_{2j*} or e_{2j*−1}+e_{2j*} (each in H*), or, via (IF′), the normal h_0* of the hyperplane E_0*, which is an element of H* with π*(h_0*) = 0. Padded with zeros, each lies in H, and the wiring condition is about the same gate of Φ. So that gate is degenerate for K, which is (X1). Correct;
  - in its case dim π* = 2 (Case II), Ψ|_{C*} ∈ span(affine, z_{<j*})|_{C*} on *every* coset C* of K*. Adding Σ_j α_{mj} z_j gives z_{j*}|_{C*} ∈ span(affine, z_{<j*}). Pulling back along the affine map ρ: C → C* gives (X3) for gate j*. Correct.
- **Sub-cases (0,1) and (1,1).** Symmetric. In (1,1), D_uΦ|_{C_0} = 1 + a + b + e, and α_m = β_m forces h_1″ ∈ H_0″, hence e_u + e_v ∈ H. The text elides the step from "e constant" to "h_1″ ∈ H_0″" (cosmetic, I-4). Correct.

### Lemma 32: dim π(H) = 2
- **Parametrization.** C′ → E_{d′_0}, w ↦ w″, is an affine bijection, with u = d′_1 + f and v = d′_2 + g. Correct.
- **Case (a).** (P+d_1)(Q+d_2) − (P+c_1)(Q+c_2) = (c_1+d_1)Q + (c_2+d_2)P + c_1c_2 + d_1d_2. Correct.
- **Case (b), common part.**
  - Ã is non-constant by non-degeneracy.
  - Translation: for w″ ∈ E, P(w″+τ) − P(w″) = f(τ) + Σ_j α_{mj}(z_j(w″+τ) − z_j(w″)). For k = m−1 this equals f(τ) + α_{m,m−1}·s. Correct (on the notation X^τ see I-4).
- **Case (b1), the merge.**
  - Let y be the E-coordinate inside s. Then L_0 = span(1, coordinates of gates < m−1, z_1, …, z_{m−2}), s = y + B_0 with B_0 ∈ L_0, and Ã ∈ L_0.
  - P + c_1 = p + 𝗎s with 𝗎 = f_y + α_{m,m−1}Ã, where f_y must be the y-coefficient of f restricted to E (I-2). Likewise for Q.
  - F = (pq + Γ_0) + G_1·s. Since D_yF = G_1, G_1 is a constant λ_y, and then G_0 = λ_0 + λ_yB_0 ∈ L_0.
  - The expansion of R_1 checks term by term. With α = α_{m,m−1} and β = β_{m,m−1}: R_1 = λ_y + βp + αq + (δ_1+α)𝗏 + (δ_2+β)𝗎 + (δ_1β + δ_2α + αβ + γ_{m−1}).
  - Circuit: the m − 2 original gates; one gate R_1·s, both factors in span(affine, z_{≤m−2}); output R_0 + R_1·s. Correct.
- **Case (b2), set-up.**
  - For k < m−1, x = w_{2m−3} and y = w_{2m−2} are coordinates of E, fixed by τ and untouched by the substitution.
  - The multilinear expansion in (X, Y) is unique. I re-derived F_XY, F_X and F_Y; they agree with the text.
- **Case (b2), sub-cases.**
  - (i) π_z = ρ_z = 0. If γ_{m−1} = 0, gate m−1 is unused, since gate m is the only later gate. Otherwise π_xρ_y + π_yρ_x = 1, and the 2×2 system in (q, p) is invertible. Correct.
  - (ii) π_z = 1, ρ_z = 0. F_XY = 0 makes q constant. If ρ_x = ρ_y = 0, then Q + c_2 = q, and (P2) gives β_m = 0 and g ∈ {0,t}; hence e_v ∈ H and Lemma 24(b) applies. Otherwise F_X or F_Y makes p constant. Correct.
  - (iii) Symmetric to (ii).
  - (iv) π_z = ρ_z = 1. Then p + q = κ. If (π_x,π_y) = (ρ_x,ρ_y), then (P+c_1) + (Q+c_2) = κ, and (P2) gives α_m = β_m and f+g ∈ {0,t}; hence e_u + e_v ∈ H. Correct.
- **Case (b2), remaining cases.**
  - p = ℓ_p + c_1 + (coefficient vector)·z is constant on E. Here ℓ_p is f minus its x and y terms, *as a linear form on F_2^{2m−2}*.
  - (P2) gives coefficient vector 0 and ℓ_p ∈ {0,t}.
  - With this ℓ_p, the identity P + c_1 = p + π_xX + π_yY + π_zXY holds on all of F_2^{2m−2}. Evaluating at w″+τ gives A_m|_C ∈ span(1, X|_C, Y|_C, z_{m−1}|_C) ⊆ span(affine, z_{≤m−1}|_C), and likewise for B_m. Correct.
- **Small m.**
  - m = 1: there is no codimension-3 subspace.
  - m = 2: dim K = 1, and every function on a line is affine.
  - m = 3: case (b2) cannot occur without (X1), because k = 1 forces Ã to be constant. Observed: 0 such pairs (V-3).
  - Case (b2) first occurs at m = 4.

### Corollaries 33–35
- **Corollary 33.** dim g ≤ dim K ≤ 2m − 1, by Lemma 23 and C_0 ≠ C_1. So dim g ≥ 2m − 3 forces codimension 1, 2 or 3. The cases m = 1 and MC(g) = 0 are handled. Correct.
- **Corollary 34.** If dim K ≤ 4, Φ|_{C_1} is a function of at most 4 variables. dim K ∈ {5,6,7} is excluded by Lemmas 32, 30 and 28 (with 24). Correct, apart from the citation (I-1). The fact itself is re-verified in V-9.
- **Corollary 35.**
  - dim g ≤ 6 by Corollary 33.
  - dim g ≥ 6, because every function on at most 5 variables has MC ≤ 4 (literature; AUDIT-003 V-6, which checks NIST's 48 classes with explicit circuits).
  - Hence dim K = 6. Correct.
- **The finite reformulation.**
  - The equivalence with the formal-circuit statement for dim K = 6 is Lemma 23 together with the exclusions above.
  - The 6-variable form: since dim g = 6, in suitable coordinates g = h(x_1, …, x_6) + εx_7 + c. Restricting the other variables to 0 gives g′ with MC(g′) = MC(g) by (F4), and MC(y·g′) ≤ MC(y·g). Correct.

## 2. Issues

**I-1. Corollary 34, "independently checked in AUDIT-002 V-2". Severity: minor (citation).**
- AUDIT-002 V-2 shows only that the 4-variable functions with MC ≤ 2 are exactly those of degree ≤ 3. It does not show the upper bound MC ≤ 3 for the 32,768 functions of degree 4.
- The same citation appears in AUDIT-003's review of Lemma 23 ("Range of dim K"), so the error has propagated.
- The fact itself is true. It is supported by:
  - EXP-001 (`bfs4.py`, exact MC of all 65,536 functions);
  - the literature (Sönmez Turan–Peralta);
  - AUDIT-003 V-6 (NIST's classes of dimension ≤ 4, each with a verified circuit of at most 3 gates);
  - this audit, V-9 (my own span search: all 65,536 functions have a circuit with at most 3 ANDs).
- Fix: cite AUDIT-003 V-6 and AUDIT-004 V-9 instead of AUDIT-002 V-2.

**I-2. Case (b1), "f_y, g_y are the y-coefficients of f, g". Severity: minor (ambiguous, and one natural reading is false).**
- The formula 𝗎 = f_y + α_{m,m−1}Ã is correct only if f_y is the y-coefficient of f *restricted to E*, in E-coordinates.
- In type 3 (e = 2m−2, y = w_{2m−3}), the substitution w_{2m−2} = c_0 + w_{2m−3} + ⟨t_{<k}, w″⟩ also contributes. So f_y = (h_1″)_{2m−3} + (h_1″)_{2m−2}, and likewise for g_y with h_2.
- Under the other reading (the coefficient of w_{2m−3} in the linear form f), the displayed decomposition P + c_1 = p + 𝗎s with p ∈ L_0 is false.
  - Witness: my harness with that reading reports p ∉ L_0 in 44,884 pairs (m = 4, 512 biased wirings, all subspaces; mutant `mutFY`, V-2).
- The proof is unaffected under the correct reading. The argument only needs some 𝗎 ∈ span(1, Ã), and with the correct 𝗎 all the displayed formulas hold exactly (V-3, V-4).
- Fix: write "the coefficient of y in f|_E", and give the type-3 value.

**I-3. The recursion uses the *proof* of Lemma 30, not its statement. Severity: minor (presentation).**
- Lemma 30 as stated gives only MC ≤ m − 1 on the cosets of K*. That is not what is pulled back to C.
- Lemma 32 needs two structural conclusions:
  - in the case dim π* = 1, a degenerate gate whose degeneracy vector lies in H*;
  - in Case II, Ψ|_{C*} ∈ span(affine, z_{<j*}) on every coset of K*.
- I checked that Lemma 30's written proof establishes exactly these (§1). To make the chain citable, they should be stated as a lemma, for example a structural form of Lemma 30.
- The statements of Lemma 28 and (IF′) already name the degeneracy vector (h, resp. the normal of E), so they need no change; only Lemma 30 is cited through its proof.

**I-4. Notation X^τ and small elisions. Severity: cosmetic.**
- "X^τ: add the constant ℓ(τ) to every linear form" is an operation on *expressions*, not on functions on E. Two expressions that agree on E can have τ-images that differ by 1 on E; for example ℓ and ℓ + ⟨t,·⟩ + c.
  - The proof is correct when expressions are read as functions on F_2^{2m−2} and translated values are computed pointwise, as in §1.
  - V-3 and V-4 confirm that δ_1 and δ_2 are constants and that the R_0, R_1 formulas are exact.
- In (b2), p is written on E using "f_rest" and is then translated. That is legitimate only if f_rest is the linear form on F_2^{2m−2}, which is the reading used in §1, and not its restriction to E.
- Sub-case (1,1) of dim π(H) = 1 elides the step "e constant on E_{d_0} ⇒ h_1″ ∈ H_0″".
- (P2) is stated for linear forms ℓ but applied to ℓ + constant. Harmless.

**I-5. "codim3.c implements every case prediction of the proof". Severity: minor (overstates the evidence).**
- `codim3.c` checks the *conclusion* of each case:
  - (X1), via Lemma 24;
  - the impossibility claims;
  - redundancy of gate j*;
  - redundancy of the last gate (cases 2a and 2b2);
  - membership in the merge space.
- It does not check:
  - any affine C_0 other than the first in its coset order, although the proof applies to every affine C_0;
  - the proof's form R_0, R_1 ∈ L_0: its merge space V_0 = span(1, *all* coordinates of C, z_1, …, z_{m−2}) contains y;
  - (P1), (P2), the non-constancy of Ã, the (b2) exits of sub-cases (ii) and (iv), the constancy of p and q on C_0 and on C, or the R_0, R_1 formulas;
  - the degenerate cases, which it counts but does not certify.
- I found no bug in `codim3.c` (V-10), and its counts are reproduced exactly (V-5).
- My harness tests every item it omits, on every pair (C_0, C), with 0 violations (V-3 to V-6).
- Fix: "checks the conclusion of every case".

**I-6. The m = 5 row of the verification table read "see log". Severity: cosmetic. Resolved in `7b45ceb`.** The numbers filled in there are exactly those of my replay (V-5).

**I-7. EXP-018 README (outside the audited document): "For types 1 and 2 the other input fails, as the proof predicts". Severity: cosmetic.** The proof predicts that the named input works; it says nothing about the other input. The observation itself reproduces: none of the type-1 and type-2 samples merges with the other input (V-8).

**I-8. Informational.**
- The hypothesis of (P2) is used only in case (b2). The merge in (b1) holds without it.
- The table's split into 2a, 2b1 and 2b2 counts non-affine C relative to the first affine coset. My replay reproduces that split. Counting all pairs (C_0, C) gives larger totals (V-5).

## 3. What I verified, and how

All programs are my own (Appendix A). Their conventions deliberately differ from EXP-018:
- gate i reads coordinates i and m+i, not 2i and 2i+1;
- subspace bases are in RREF with the *highest* set bit as pivot (EXP-018 uses the lowest);
- every hit is re-tested for affinity by a derivative test (EXP-018 uses only the Möbius transform);
- all wirings are used, not only swap-reduced ones, except in the replay (V-5).

**V-1. (P1), (P2) and the non-degeneracy equivalence, tested directly (`p12.c`).**
- Setting: w″-space with G = m − 1 gates. For each wiring, each t ≠ 0 and each c ∈ F_2 the program checks:
  - (P1a) gates j < k are τ-invariant on E;
  - (P1b) z_k = Ãs on E;
  - (P1c) z_k(w+τ) = (Ã+1)s on E;
  - (ND) Ã is constant iff the stated condition holds;
  - (P2) if Ã is not constant, the kernel of (ℓ, c) ↦ (ℓ + Σ c_j z_j)|_E modulo constants is exactly {0, (t,0)}.

| m | wirings of gates 1..m−1 | triples (wiring, t, c) | Ã non-constant | failures of P1a, P1b, P1c, ND, P2 | kernel dimension when Ã is constant |
|---|---|---|---|---|---|
| 3 | all 4 | 120 | 84 | 0, 0, 0, 0, 0 | 2 in 36 of 36 |
| 4 | all 64 | 8,064 | 7,392 | 0, 0, 0, 0, 0 | 2 in 672 of 672 |
| 5 | all 4,096 | 2,088,960 | 2,042,880 | 0, 0, 0, 0, 0 | 2 in 46,080 of 46,080 |
| 6 | random 400 of 2^20 | 818,400 | 813,738 | 0, 0, 0, 0, 0 | 2 in 4,662 of 4,662 |
| 7 | random 24 of 2^30 | 196,560 | 196,284 | 0, 0, 0, 0, 0 | 2 in 276 of 276 |

- The last column is a built-in control: where the hypothesis of (P2) fails, the test does see a larger kernel.

**V-2. The Lemma 32 harness (`lem32.c`) and its mutation tests.**
- The harness takes every (wiring, codimension-3 K) with at least one affine and one non-affine coset, and *every* pair (C_0 affine, C non-affine). It determines the proof's case and checks every prediction:
  - (X1): the degenerate gate is redundant on C (span test);
  - dim π(H) = 0: there is never an affine coset;
  - dim π(H) = 1: ψ ≠ 0, dim H* = 2, dim π* = 2, and z_{j*} is redundant on all 8 cosets;
  - case (a): the last gate is redundant;
  - case (b): Ã is non-constant, and (P1) holds on C_0 and on C;
  - case (b1):
    - s|_C ∈ w_y + L_0;
    - Φ|_C ∈ L_0 + s·L_0, with the strict, y-free L_0;
    - p, q ∈ L_0, with the proof's 𝗎 and 𝗏;
    - G_1 is constant, and G_0 ∈ L_0;
    - δ_1 and δ_2 are constant;
    - R_1 from its definition equals the simplified formula;
    - Φ|_C = R_0 + R_1·s pointwise;
  - case (b2): (X2) for gate m−1; otherwise the sub-case (i)–(iv) and its predicted exit, p and q constant on C_0 and on C, and the last gate redundant.
- Every case yields an explicit, checked certificate of MC(Φ|_C) ≤ m − 1: a redundant gate, an unused gate, or the merged gate. So the conclusion is verified for every instance tested, whether or not the proof is right.
- Mutation tests (each mutant must fail):

| mutant | run | violations |
|---|---|---|
| wrong merge input s | m = 3 | 1,072,832 |
| j* lowered by one | m = 4 sample | 3,016 (dim H* check) |
| f_y without the type-3 term (see I-2) | m = 4 sample | 44,884 |
| π_x flipped in (b2) | m = 4 sample | 13,716 |

- A mutant that admits y into L_0 passes, as it should, since it only weakens the test.

**V-3. m = 3 and m = 4, exhaustive.**
- m = 3: all 256 wirings × all 1,395 subspaces give 793,920 non-affine C with an affine C_0 and 1,547,904 pairs, with 0 violations. No (b2) pair occurs (see §1, small m).
- m = 4: all 32,768 wirings (no swap reduction) × all 97,155 subspaces, every pair:

| quantity | count |
|---|---|
| (wiring, K) with an affine and a non-affine coset | 17,240,154 |
| non-affine C with an affine C_0 | 87,899,496 |
| pairs (C_0, C) | 229,201,152 |
| degenerate (X1): pairs / cosets C | 192,647,040 / 65,740,920 |
| dim π = 1, non-degenerate C (cosets checked for j*) | 2,322,432 (2,709,504) |
| pairs in case (a) | 15,399,936 |
| pairs in case (b1), types 1/2/3 | 11,992,320 (3,997,440 each) |
| pairs in case (b2), gate m−1 unused | 5,944,320 |
| pairs in case (b2), used: (i)/(ii)/(iii)/(iv) | 604,800: 72,576 / 177,408 / 177,408 / 177,408 |
| violations of any prediction; affinity cross-check errors | 0; 0 |

- The pair counts 229,201,152 and 192,647,040 equal AUDIT-003 V-2's all-wiring figures for dim K = 5.
- The swap-reduced subtotals equal the author's m = 4 log exactly: 24,282,232 non-affine C; 18,787,840 degenerate; 561,600 with dim π = 1; and 4,932,792 = 2,167,708 + 1,690,160 + 1,012,800 + 62,124 with dim π = 2.
- CPU: 2 min 15 s.

**V-4. m = 5: own wiring samples × all 6,347,715 subspaces.**

| sample | non-affine C | pairs | degenerate pairs | dim π = 1 C | (a) | (b1) | (b2) unused | (b2) used: (i)/(ii)/(iii)/(iv) | violations |
|---|---|---|---|---|---|---|---|---|---|
| 1,024 uniform from all 2^24 wirings (seed 777) | 4,640,596 | 15,926,750 | 15,394,284 | 25,599 | 243,497 | 168,180 | 83,192 | 10,654: 324 / 3,376 / 2,796 / 4,158 | 0 |
| 768 biased: α_i = 0, β_i = 0, α_i = β_i likely (seed 4242) | 9,549,045 | 36,641,959 | 35,939,813 | 11,800 | 329,634 | 253,154 | 93,854 | 11,256: 2,720 / 6,240 / 684 / 1,612 | 0 |

**V-5. Replay of the author's wiring sets: exact agreement.** `picks.c` reproduces the sample of `codim3.c` (glibc `srand(2026)` and its decoder), and my harness then processes exactly those wirings.
- **m = 4, all 8,640 swap-reduced wirings.** 24,282,232 / 18,787,840 / 561,600 / 2,167,708 / 1,690,160 / 1,012,800 / 62,124. Identical to `codim3_m4.log`, including the split by the first affine coset.
- **m = 5, the 300 sampled wirings.** 1,839,901 / 1,762,553 / 5,279 / 34,026 / 21,530 / 15,649 / 864. Identical to `codim3_m5.log` and to the row added in `7b45ceb`.
  - My harness also checks all 6,592,837 pairs of this sample: 88,513 in (a), 62,272 in (b1), 29,962 + 1,728 in (b2). 0 violations.
- Two unrelated implementations therefore agree on every count they share.

**V-6. m = 6, sampled.** An exhaustive run is infeasible: there are 4.1·10^8 codimension-3 subspaces of F_2^12.
- *Mode 2:* all 971,550 subspaces supported on the coordinates of the last gate and three other gates, against 64 + 384 uniform and 384 biased wirings. 525,702 + 845,898 + 10,069,059 pairs.
- *Mode 3:* 40 + 40 random wirings of gates 1–5 (uniform and biased), each with 400 structured random H, and for each H *all* 32,768 wirings of the last gate. 932,280 + 931,648 pairs.
  - Mode 3 targets case (b2): it gives 768 + 544 pairs with gate m−1 used, covering all four sub-cases.
- In total about 13.3 million pairs, with every case represented and 0 violations.

**V-7. Self-test of the screening.**
- The bit-sliced Möbius screening was compared with the single-wiring derivative test on random (subspace, wiring block) samples, hits and non-hits alike:

| m | cosets compared | affine among them | mismatches |
|---|---|---|---|
| 4 | 10,240,000 | 50,362 | 0 |
| 5 | 10,240,000 | 5,781 | 0 |
| 6 | 3,072,000 | 1,451 | 0 |

- In addition, every hit is re-tested by the derivative test inside the harness, with 0 mismatches in all runs.

**V-8. The sample claims (`hc_audit.py`, own code; reads only `hc_sample.txt`).**
- All 1,084 lines are genuine hard-core pairs. For each:
  - the stored truth table equals Φ|_{C_1};
  - C_0 is affine and C_1 is not;
  - dim π(H) = 2, and C_0, C_1 lie in different H_0-classes;
  - no gate is Lemma-24-degenerate;
  - no gate of the given circuit is redundant on C_1.
- 770 have an unused gate. By highest unused gate (1-based numbering): gate 3: 553, gate 2: 160, gate 1: 57.
- The other 314 have all gates used, and all of them have top(t) = m − 1.
- All 553 samples with top(t) = m − 2 have gate m − 1 unused.
- All 531 samples with top(t) = m − 1 satisfy the merge identity with the predicted s, also in the strict y-free form. For types 1 and 2 the other input works in 0 cases.

**V-9. Every 4-variable function has MC ≤ 3 (`mc4.c`).**
- Method: exhaustive span search. z_1 = ℓ_1ℓ_2, z_2 ∈ W_1·W_1, z_3 ∈ W_2·W_2, and the output is z_3 plus an element of W_2.
- Result: all 65,536 functions have a circuit with at most 3 ANDs. The set with at most 2 ANDs is exactly the 32,768 functions of degree ≤ 3.
- CPU: 1 min 49 s.

**V-10. Code review of `codim3.c`.**
- *Subspaces:* RREF with lowest-bit pivots, and free positions exclude the other pivots. The counts equal the Gaussian binomials (97,155 and 6,347,715).
- *Cosets:* `pdep` on the free bits, with the pivot bits set by parity. So ⟨h_i, base[t]⟩ = 0, and the shift e_{P_i} sets d_i. Correct.
- *Affinity:* Möbius transform over KD ≤ 7 bits across one or two words, with masking for KD = 5. Correct.
- *GF(2) spans:* fully reduced basis with highest-bit pivots and one-pass reduction. Its capacity of 64 vectors exceeds the 22 needed.
- *Case logic:* the choice of s by type, the class test `same`, the array `used[]` and the wiring decoder are correct.
- Its weaknesses are those listed in I-5. The sample draws with `rand()` with replacement; the 300 drawn wirings contain no duplicate (checked).

**V-11. Literature (search results only; no full text read).**
- Two WebSearch queries: MC of a product with a new variable; MC and restrictions to affine subspaces.
- Neither found a statement of Lemma 32, of the codimension-2 or codimension-3 results, or of the fresh-variable lemma. The closest items were:
  - an upper bound C∧(x_1x_2f_1 + f_2) ≤ 1 + C∧(x_1f_1 + f_2), used for symmetric functions (Brandão, Çalık, Sönmez Turan, Peralta; NIST page);
  - the Boyar–Peralta fact, as cited by Find and Boyar (arXiv:1407.6169), that a function of MC n − k is affine on some affine subspace of dimension k.
- So the document's "novelty unconfirmed" stands.
- Barriers: relativization, natural proofs and algebrization are not relevant to a statement about MC at small fixed levels. The document claims nothing about P vs NP.

## 4. What I could not check

- **Lemma 32 for m ≥ 7, and for m = 5, 6 beyond samples.** The human proof covers every m, and I checked it line by line. The computations cover:
  - m = 3 and m = 4 exhaustively;
  - m = 5 for 2,092 wirings (out of 16.7 million) × all subspaces;
  - m = 6 on structured families only.
- **The 5-variable bound MC ≤ 4 used in Corollary 35.** I relied on the literature (recalled; AUDIT-002 saw search snippets) and on AUDIT-003 V-6 (NIST's 48 classes, each with a verified circuit). I did not recompute it.
- **The cycle-002 hard core (2,152,192 pairs) "lies exactly in 2b1 and (X2)".** My enumeration implies the inclusion: every pair in (a), in dim π = 1 and in (b2) with gate m−1 used has a redundant gate, and degenerate pairs are excluded. I did not recount the 2,152,192.
- **`hc_dump.c`** beyond its header. Its output sample was re-checked independently (V-8).
- **Formal verification.** No Lean formalization of (P1), (P2), Lemma 32 or Corollaries 33–35 exists, and the document claims none. My programs, like the author's, are unformalized C.

## Summary

- **Lemma 32 survives.** I checked every case of the proof by hand:
  - dim π(H) ∈ {0, 1, 2};
  - the recursion through Ψ, H* and K*, including the projection of cosets and the use of Lemma 30's proof;
  - case (a);
  - the merge (b1), including the decomposition into L_0 + L_0·s and the identities for R_0 and R_1;
  - case (b2), with its multilinear expansion and all its exits.
- **No gap was found.** The three corrections are presentational:
  - the ambiguous f_y and g_y (I-2);
  - citing Lemma 30's proof rather than a stated lemma (I-3);
  - the τ-notation (I-4).
- **(P1), (P2) and the non-degeneracy equivalence survive,** by hand and by an exhaustive computer check at m ≤ 5 (sampled at m = 6, 7).
- **No counterexample.** Every prediction of the proof holds, and every non-affine coset receives an explicit, checked certificate with m − 1 gates:
  - exhaustively at m = 3 and 4 (all 32,768 wirings, all subspaces, all 229,201,152 pairs);
  - on 2,092 wirings × all 6,347,715 subspaces at m = 5;
  - on about 13 million pairs at m = 6.
- **The author's m = 4 and m = 5 logs are reproduced exactly** by unrelated code from the same wirings.
- **Corollaries 33, 34 and 35 survive.**
  - Corollary 34 needs a citation fix (I-1): AUDIT-002 V-2 does not check the 4-variable upper bound. The fact itself holds (EXP-001, AUDIT-003 V-6, V-9 here).
  - The description of EXP-018 overstates what `codim3.c` tests (I-5); this audit's tests cover the gap.
- **No overclaim** about P vs NP or novelty.

## Appendix A. Auditor's programs

Build: `gcc -O2 -march=native -fopenmp -o lem32 lem32.c`, `gcc -O2 -march=native -o p12 p12.c`, `gcc -O2 -o mc4 mc4.c`, `gcc -O2 -o picks picks.c`.

Runs behind each section:
- **V-1:** `p12 2 0 1`, `p12 3 0 1`, `p12 4 0 1`, `p12 5 400 7` and `p12 6 24 11`. The first argument is G = m − 1; nsamples ≤ 0 means all wirings.
- **V-3:** `lem32 3 0 0 1 0` and `lem32 4 0 0 1 0`. Mode 0 is all RREF subspaces; nblocks ≤ 0 means all wirings.
- **V-4:** `lem32 5 0 16 777 0` and `lem32 5 0 12 4242 1`.
- **V-5:** `picks 4 0 0 > p4.txt; lem32 4 5 p4.txt` and `picks 5 300 2026 > p5.txt; lem32 5 5 p5.txt`. Mode 5 reads the wirings from a file.
- **V-6:** `lem32 6 2 1 99 0`, `lem32 6 2 6 31 0`, `lem32 6 2 6 32 1`, `lem32 6 3 40 400 2027 0` and `lem32 6 3 40 400 2028 1`.
- **V-7:** `SELFTEST=3000 lem32 6 2 4 5 1`, `SELFTEST=3000 lem32 6 2 4 6 0`, `SELFTEST=20000 lem32 5 0 2 8 1` and `SELFTEST=20000 lem32 4 0 4 9 1`.
- **V-9:** `mc4`.
- **V-8:** `python3 -I hc_audit.py hc_sample.txt`.

Notes on the source:
- Mode 1 (random subspaces) exists in the source but was not used for any reported figure.
- Each mutant of V-2 is `lem32.c` with one line changed:
  - mutS: `s = type == 1 ? &A[k] : &B[k]`;
  - mutJ: `js = hb(psi) - 1`;
  - mutFY: `fy = (h1 >> y) & 1`;
  - mutPX: `px = 1 ^ ((h1 >> x) & 1)`;
  - mutL0: `Wc[y]` added to the generators of L_0.
- md5 of the sources: `lem32.c` c158be32b8c5d71c7e7761d31301251a, `p12.c` 394d94e36dccbbdaf67d660b2d26562a, `mc4.c` 444fd8f8a3bbb0d3204ccd6049d1e4c3, `picks.c` 0f255c7bcbfac4035646ed344b6216d1, `hc_audit.py` ef1fca2fe2b0b9463aa725c25300ce1f.

### A.1 `lem32.c`

```c
/* lem32.c -- AUDIT-004 (auditor's own code; shares nothing with EXP-018).
 * Tests every case prediction of the proof of Lemma 32 (PNE-001-codim3.md) and certifies MC(Phi|C) <= m-1.
 * Convention: m gates 0..m-1; gate i reads A-coordinate i and B-coordinate m+i (u = m-1, v = 2m-1):
 *   z_i = (w_i + sum_{j<i} al[i]_j z_j)(w_{m+i} + sum_{j<i} be[i]_j z_j),  Phi = z_{m-1} + sum_{j<m-1} gm_j z_j.
 * H = 3-dim subspace of F_2^D (D=2m), K = H^perp.  Basis put in RREF with pivot = HIGHEST set bit.
 * Screening: Phi bit-sliced over 64 wirings; affinity on each coset by Moebius transform.
 * Each hit (some coset affine, some not) is re-examined for one wiring; affinity is re-tested by a
 * derivative test (independent of the Moebius code), and every pair (C0 affine, C non-affine) is analysed.
 * Modes:  lem32 m 0 nblocks seed bias   : all RREF subspaces; wirings: all (nblocks<=0) or nblocks random blocks of 64
 *         lem32 m 1 nsub nblk seed bias : nsub random subspaces (structured mix), each against nblk random blocks
 *         lem32 m 2 nblocks seed bias   : all subspaces supported on the coordinates of 4 gates {last} u S, |S|=3
 * bias=1: wirings biased (al_i=0, be_i=0, al_i=be_i each with prob. 1/4). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <omp.h>
typedef uint64_t u64;
#define MAXM 6
#define MAXD 12
#define TWW 64
#define CW 8
static int M, D, NP, KD, NC, TW, CWn;
typedef struct { u64 w[TWW]; } Tab;
typedef struct { u64 w[CW]; } V;
typedef struct { int al[MAXM], be[MAXM], gm; } Wir;
static Tab Wc[MAXD];
static V ONE, XC[16];   /* constant 1 and local coordinate functions on a coset */

static void decode(u64 code, Wir *W) { memset(W, 0, sizeof *W);
  for (int i = 1; i < M; i++) { W->al[i] = code & ((1u << i) - 1); code >>= i; W->be[i] = code & ((1u << i) - 1); code >>= i; }
  W->gm = code & ((1u << (M - 1)) - 1); }
static int nbits_wiring(void) { return M * M - 1; }
static u64 rs_next(u64 *s) { u64 x = *s; x ^= x << 13; x ^= x >> 7; x ^= x << 17; *s = x; return x; }
static u64 rand_code(u64 *s, int bias) {
  if (!bias) return rs_next(s) & ((1ULL << nbits_wiring()) - 1);
  Wir W; memset(&W, 0, sizeof W);
  for (int i = 1; i < M; i++) { int msk = (1 << i) - 1; u64 r = rs_next(s);
    W.al[i] = (r & 3) == 0 ? 0 : (int)((r >> 8) & msk); int c = (r >> 2) & 3;
    W.be[i] = c == 0 ? 0 : c == 1 ? W.al[i] : (int)((r >> 20) & msk); }
  W.gm = rs_next(s) & ((1u << (M - 1)) - 1);
  u64 code = 0; int sh = 0;
  for (int i = 1; i < M; i++) { code |= (u64)W.al[i] << sh; sh += i; code |= (u64)W.be[i] << sh; sh += i; }
  code |= (u64)W.gm << sh; return code; }

static void eval_tabs(const Wir *W, Tab *z, Tab *A, Tab *B, Tab *Phi) {
  for (int i = 0; i < M; i++) { A[i] = Wc[i]; B[i] = Wc[M + i];
    for (int j = 0; j < i; j++) { if ((W->al[i] >> j) & 1) for (int q = 0; q < TW; q++) A[i].w[q] ^= z[j].w[q];
                                  if ((W->be[i] >> j) & 1) for (int q = 0; q < TW; q++) B[i].w[q] ^= z[j].w[q]; }
    for (int q = 0; q < TW; q++) z[i].w[q] = A[i].w[q] & B[i].w[q]; }
  *Phi = z[M - 1]; for (int j = 0; j < M - 1; j++) if ((W->gm >> j) & 1) for (int q = 0; q < TW; q++) Phi->w[q] ^= z[j].w[q]; }
static void eval_block(const Wir *Wb, u64 *PHI) {
  u64 AL[MAXM][MAXM] = {{0}}, BE[MAXM][MAXM] = {{0}}, GM[MAXM] = {0};
  for (int w = 0; w < 64; w++) for (int i = 0; i < M; i++) { for (int j = 0; j < i; j++) {
      if ((Wb[w].al[i] >> j) & 1) AL[i][j] |= 1ULL << w; if ((Wb[w].be[i] >> j) & 1) BE[i][j] |= 1ULL << w; }
    if (i < M - 1 && ((Wb[w].gm >> i) & 1)) GM[i] |= 1ULL << w; }
  for (int p = 0; p < NP; p++) { u64 z[MAXM];
    for (int i = 0; i < M; i++) { u64 a = ((p >> i) & 1) ? ~0ULL : 0, b = ((p >> (M + i)) & 1) ? ~0ULL : 0;
      for (int j = 0; j < i; j++) { a ^= AL[i][j] & z[j]; b ^= BE[i][j] & z[j]; } z[i] = a & b; }
    u64 ph = z[M - 1]; for (int j = 0; j < M - 1; j++) ph ^= GM[j] & z[j]; PHI[p] = ph; } }

/* ---- subspaces ---- */
typedef struct { int r[3], P[3], Hv[8], fr[MAXD]; unsigned short pt[8][512]; } Sub;
static int hb(int x) { return 31 - __builtin_clz(x); }
static int setup_sub(Sub *S, const int h[3]) {
  int r[3] = {h[0], h[1], h[2]};
  for (int i = 0; i < 3; i++) { int best = i; for (int j = i + 1; j < 3; j++) if (r[j] && (!r[best] || hb(r[j]) > hb(r[best]))) best = j;
    int t = r[i]; r[i] = r[best]; r[best] = t; if (!r[i]) return 0; S->P[i] = hb(r[i]);
    for (int j = 0; j < 3; j++) if (j != i && ((r[j] >> S->P[i]) & 1)) r[j] ^= r[i]; }
  for (int i = 0; i < 3; i++) S->r[i] = r[i];
  for (int l = 0; l < 8; l++) { S->Hv[l] = 0; for (int i = 0; i < 3; i++) if ((l >> i) & 1) S->Hv[l] ^= r[i]; }
  int nf = 0; int pv = (1 << S->P[0]) | (1 << S->P[1]) | (1 << S->P[2]);
  for (int c = 0; c < D; c++) if (!((pv >> c) & 1)) S->fr[nf++] = c;
  int kv[MAXD]; for (int q = 0; q < nf; q++) { int f = S->fr[q]; kv[q] = 1 << f; for (int i = 0; i < 3; i++) if ((r[i] >> f) & 1) kv[q] |= 1 << S->P[i]; }
  for (int d = 0; d < 8; d++) { int rep = 0; for (int i = 0; i < 3; i++) if ((d >> i) & 1) rep |= 1 << S->P[i];
    S->pt[d][0] = rep; for (int x = 1; x < NC; x++) S->pt[d][x] = S->pt[d][x & (x - 1)] ^ kv[__builtin_ctz(x)]; }
  return 1; }
static int inH(const Sub *S, int vec) { for (int l = 1; l < 8; l++) if (S->Hv[l] == vec) return 1; return 0; }

static void screen(const Sub *S, const u64 *PHI, u64 aff[8]) {
  u64 T[512];
  for (int d = 0; d < 8; d++) { const unsigned short *pt = S->pt[d];
    for (int x = 0; x < NC; x++) T[x] = PHI[pt[x]];
    for (int r = 0; r < KD; r++) { int s = 1 << r; for (int b = 0; b < NC; b += 2 * s) for (int x = b + s; x < b + 2 * s; x++) T[x] ^= T[x - s]; }
    u64 bad = 0; for (int x = 3; x < NC; x++) if (x & (x - 1)) bad |= T[x];
    aff[d] = ~bad; } }

/* ---- coset vectors and GF(2) spans ---- */
static V restr(const Tab *f, const Sub *S, int d) { V v; memset(&v, 0, sizeof v);
  for (int x = 0; x < NC; x++) { int p = S->pt[d][x]; if ((f->w[p >> 6] >> (p & 63)) & 1) v.w[x >> 6] |= 1ULL << (x & 63); } return v; }
static V vx(V a, V b) { for (int q = 0; q < CWn; q++) a.w[q] ^= b.w[q]; return a; }
static V va(V a, V b) { for (int q = 0; q < CWn; q++) a.w[q] &= b.w[q]; return a; }
static V vk(int c) { V v; memset(&v, 0, sizeof v); if (c) v = ONE; return v; }
static int veq(V a, V b) { for (int q = 0; q < CWn; q++) if (a.w[q] != b.w[q]) return 0; return 1; }
static int vconst(V a) { V z; memset(&z, 0, sizeof z); return veq(a, z) ? 0 : (veq(a, ONE) ? 1 : -1); }
static int vlow(const V *v) { for (int q = 0; q < CWn; q++) if (v->w[q]) return q * 64 + __builtin_ctzll(v->w[q]); return -1; }
static int vbit(const V *v, int p) { return (v->w[p >> 6] >> (p & 63)) & 1; }
typedef struct { V r[48]; u64 cb[48]; int piv[48]; int n; } Bas;
static void bred(const Bas *b, V *v, u64 *cb) { for (int i = 0; i < b->n; i++) if (vbit(v, b->piv[i])) { *v = vx(*v, b->r[i]); *cb ^= b->cb[i]; } }
static void badd(Bas *b, V v, u64 cb) { bred(b, &v, &cb); int p = vlow(&v); if (p < 0) return;
  for (int i = 0; i < b->n; i++) if (vbit(&b->r[i], p)) { b->r[i] = vx(b->r[i], v); b->cb[i] ^= cb; }
  b->r[b->n] = v; b->cb[b->n] = cb; b->piv[b->n] = p; b->n++; }
static int binspan(const Bas *b, V v, u64 *cb) { u64 c = 0; bred(b, &v, &c); if (cb) *cb = c; return vlow(&v) < 0; }
static int is_affine_deriv(V f) {           /* derivative test: D_r f constant for every local direction r */
  for (int r = 0; r < KD; r++) { int s = 1 << r, ref = -1;
    for (int x = 0; x < NC; x++) if (!(x & s)) { int dv = vbit(&f, x) ^ vbit(&f, x | s); if (ref < 0) ref = dv; else if (dv != ref) return 0; } }
  return 1; }
/* span(1, all local coords, z_j|C for j < jmax) */
static void base_aff_z(Bas *b, const V *zC, int jmax) { b->n = 0; badd(b, ONE, 0); for (int r = 0; r < KD; r++) badd(b, XC[r], 0); for (int j = 0; j < jmax; j++) badd(b, zC[j], 0); }

/* ---- counters ---- */
enum { C_HIT_WH, C_NONAFF, C_PAIRS, C_DEG, V_DEGCERT, V_AFFMIS, V_PI0, C_PI1, V_PSI0, V_DIMHS, V_DIMPIS, V_JSRED,
  C_SAME, V_SAME, C_B1, V_ACONST, V_P1, V_SFORM, V_MERGE, V_PFORM, V_QFORM, V_G1, V_G0, V_DELTA, V_R1EQ, V_R01,
  C_B2UN, C_B2, V_B2EXIT, V_PQ0, V_PQC, V_B2RED, C_B1T1, C_B1T2, C_B1T3, C_B2I, C_B2II, C_B2III, C_B2IV,
  CF_SAME, CF_B1, CF_B2UN, CF_B2, C_PI1ALL8, C_DEG_PAIRS, R_NONAFF, R_DEG, R_PI1, R_CF2, NCNT };
static const char *cname[NCNT] = {"(wiring,K) hits", "non-affine C with an affine C0", "pairs (C0,C)", "C degenerate (X1)",
  "VIOL degenerate-gate certificate", "ERR screen/derivative affinity mismatch", "VIOL dim pi=0 with affine coset",
  "C dim pi=1 (non-deg)", "VIOL psi=0", "VIOL dim H*<2", "VIOL dim pi*<2", "VIOL gate j* not redundant on some coset",
  "pairs 2a same class", "VIOL 2a last gate not redundant", "pairs 2b1 merge", "VIOL Atilde constant", "VIOL (P1) on C0/C",
  "VIOL s != y + L0", "VIOL merge Phi|C in L0 + s L0", "VIOL p notin L0 (C0 side)", "VIOL q notin L0", "VIOL G1 not const",
  "VIOL G0 notin L0", "VIOL delta1/delta2 not const", "VIOL R1 direct != R1 simplified", "VIOL Phi|C != R0 + R1 s",
  "pairs 2b2 gate m-1 unused", "pairs 2b2 used", "VIOL 2b2 exit (X1 predicted)", "VIOL p,q not const on C0",
  "VIOL p,q not const on C", "VIOL 2b2 last gate not redundant", "pairs 2b1 type1", "pairs 2b1 type2", "pairs 2b1 type3",
  "pairs 2b2 (i)", "pairs 2b2 (ii)", "pairs 2b2 (iii)", "pairs 2b2 (iv)",
  "C(first C0) 2a same", "C(first C0) 2b1", "C(first C0) 2b2 unused", "C(first C0) 2b2 used", "cosets checked j* (all 8)", "pairs degenerate", "[swap-reduced] non-affine C w/ affine C0", "[swap-reduced] C degenerate", "[swap-reduced] C dim pi=1 non-deg", "[swap-reduced] C dim pi=2 non-deg"};
static long first_report = 0;

static void analyze(u64 code, const Sub *S, const u64 affs, long *cnt) {
  Wir W; decode(code, &W);
  static __thread Tab z[MAXM], A[MAXM], B[MAXM], Phi;
  eval_tabs(&W, z, A, B, &Phi);
  V ph[8]; int aff[8], naff = 0;
  for (int d = 0; d < 8; d++) { ph[d] = restr(&Phi, S, d); aff[d] = is_affine_deriv(ph[d]); naff += aff[d];
    if (aff[d] != (int)((affs >> d) & 1)) cnt[V_AFFMIS]++; }
  if (naff == 0 || naff == 8) return;
  cnt[C_HIT_WH]++; cnt[C_NONAFF] += 8 - naff; cnt[C_PAIRS] += (long)naff * (8 - naff);
  int red = 1; for (int i = 1; i < M; i++) if (W.al[i] > W.be[i]) red = 0;
  if (red) cnt[R_NONAFF] += 8 - naff;
  int u = M - 1, v = 2 * M - 1;
  /* (X1) */
  int dg = -1;
  for (int g = 0; g < M && dg < 0; g++) {
    if (W.al[g] == 0 && inH(S, 1 << g)) dg = g; else if (W.be[g] == 0 && inH(S, 1 << (M + g))) dg = g;
    else if (W.al[g] == W.be[g] && inH(S, (1 << g) | (1 << (M + g)))) dg = g; }
  int pr[8], seen[4] = {0}; for (int l = 0; l < 8; l++) { pr[l] = ((S->Hv[l] >> u) & 1) | (((S->Hv[l] >> v) & 1) << 1); seen[pr[l]] = 1; }
  int npi = seen[1] + seen[2] + seen[3], dpi = npi == 0 ? 0 : (npi == 1 ? 1 : 2);
  if (dpi == 0) cnt[V_PI0]++;
  if (dg >= 0) {
    cnt[C_DEG] += 8 - naff; cnt[C_DEG_PAIRS] += (long)naff * (8 - naff); if (red) cnt[R_DEG] += 8 - naff;
    for (int d = 0; d < 8; d++) if (!aff[d]) { V zC[MAXM]; for (int j = 0; j <= dg; j++) zC[j] = restr(&z[j], S, d);
      Bas b; base_aff_z(&b, zC, dg); if (!binspan(&b, zC[dg], NULL)) cnt[V_DEGCERT]++; }
    return; }
  if (dpi == 0) return;
  if (dpi == 1) {
    cnt[C_PI1] += 8 - naff; if (red) cnt[R_PI1] += 8 - naff;
    int pq = 0; for (int l = 1; l < 8; l++) if (pr[l]) pq = pr[l];
    int psi = pq == 1 ? W.al[M - 1] : pq == 2 ? W.be[M - 1] : (W.al[M - 1] ^ W.be[M - 1]);
    if (!psi) { cnt[V_PSI0]++; return; }
    int js = hb(psi); int gmask = 0; for (int g = 0; g <= js; g++) gmask |= (1 << g) | (1 << (M + g));
    int nhs = 0, sp[4] = {0};
    for (int l = 1; l < 8; l++) if (!pr[l] && !(S->Hv[l] & ~gmask)) { nhs++; sp[((S->Hv[l] >> js) & 1) | (((S->Hv[l] >> (M + js)) & 1) << 1)] = 1; }
    if (nhs != 3) { cnt[V_DIMHS]++; return; }
    if (sp[1] + sp[2] + sp[3] != 3) { cnt[V_DIMPIS]++; return; }
    for (int d = 0; d < 8; d++) { V zC[MAXM]; for (int j = 0; j <= js; j++) zC[j] = restr(&z[j], S, d);
      Bas b; base_aff_z(&b, zC, js); cnt[C_PI1ALL8]++; if (!binspan(&b, zC[js], NULL)) cnt[V_JSRED]++; }
    return; }
  /* dim pi = 2 */
  int h0 = 0, h1 = 0, h2 = 0; for (int l = 1; l < 8; l++) { if (pr[l] == 0) h0 = S->Hv[l]; if (pr[l] == 1) h1 = S->Hv[l]; if (pr[l] == 2) h2 = S->Hv[l]; }
  int cls[8]; for (int d = 0; d < 8; d++) cls[d] = __builtin_popcount(h0 & S->pt[d][0]) & 1;
  int k = -1; for (int g = 0; g < M - 1; g++) if (((h0 >> g) & 1) || ((h0 >> (M + g)) & 1)) k = g;
  int tA = (h0 >> k) & 1, tB = (h0 >> (M + k)) & 1, type = (tA && !tB) ? 1 : (!tA && tB) ? 2 : 3;
  int e = type == 1 ? k : M + k, y = type == 1 ? M + k : k; const Tab *s = type == 1 ? &B[k] : &A[k];
  int tlow = h0 & ~((1 << k) | (1 << (M + k)));
  int al1 = (W.al[M - 1] >> (M - 2)) & 1, be1 = (W.be[M - 1] >> (M - 2)) & 1, gm1 = (W.gm >> (M - 2)) & 1;
  int first0 = -1; for (int d = 0; d < 8; d++) if (aff[d]) { first0 = d; break; }
  if (red) cnt[R_CF2] += 8 - naff;
  for (int c0 = 0; c0 < 8; c0++) if (aff[c0]) for (int c = 0; c < 8; c++) if (!aff[c]) {
    int isfirst = (c0 == first0);
    V zC[MAXM]; for (int j = 0; j < M; j++) zC[j] = restr(&z[j], S, c);
    if (cls[c] == cls[c0]) {                                  /* (a) */
      cnt[C_SAME]++; if (isfirst) cnt[CF_SAME]++;
      Bas b; base_aff_z(&b, zC, M - 1); if (!binspan(&b, ph[c], NULL)) cnt[V_SAME]++;
      continue; }
    /* (b): Atilde for c = class of C0 */
    int cc = cls[c0];
    Tab At; for (int q = 0; q < TW; q++) At.w[q] = cc ? ~0ULL : 0;
    for (int i = 0; i < D; i++) if ((tlow >> i) & 1) for (int q = 0; q < TW; q++) At.w[q] ^= Wc[i].w[q];
    int cf = type == 1 ? W.al[k] : type == 2 ? W.be[k] : (W.al[k] ^ W.be[k]);
    for (int j = 0; j < k; j++) if ((cf >> j) & 1) for (int q = 0; q < TW; q++) At.w[q] ^= z[j].w[q];
    if (type == 3) for (int q = 0; q < TW; q++) At.w[q] = ~At.w[q];
    { int c1 = -1, nc = 1; for (int p = 0; p < NP && nc; p++) { int b = (At.w[p >> 6] >> (p & 63)) & 1; if (c1 < 0) c1 = b; else if (b != c1) nc = 0; }
      if (nc) { cnt[V_ACONST]++; continue; } }
    V At0 = restr(&At, S, c0), AtC = restr(&At, S, c), s0 = restr(s, S, c0), sC = restr(s, S, c);
    V zk0 = restr(&z[k], S, c0);
    if (!veq(zk0, va(At0, s0)) || !veq(zC[k], va(vx(AtC, ONE), sC))) cnt[V_P1]++;
    if (k == M - 2) {                                          /* (b1) merge */
      cnt[C_B1]++; if (isfirst) cnt[CF_B1]++; cnt[C_B1T1 + type - 1]++;
      /* generators of L0: 1, w_t (t in coordinates of gates 0..m-3), z_0..z_{m-3} */
      int ng = 0; Tab gen[3 * MAXM]; Tab one; for (int q = 0; q < TW; q++) one.w[q] = ~0ULL; gen[ng++] = one;
      for (int g = 0; g <= M - 3; g++) { gen[ng++] = Wc[g]; gen[ng++] = Wc[M + g]; }
      for (int j = 0; j <= M - 3; j++) gen[ng++] = z[j];
      V g0[3 * MAXM], gC[3 * MAXM]; Bas L0, LC; L0.n = 0; LC.n = 0;
      for (int i = 0; i < ng; i++) { g0[i] = restr(&gen[i], S, c0); gC[i] = restr(&gen[i], S, c); badd(&L0, g0[i], 1ULL << i); badd(&LC, gC[i], 1ULL << i); }
      V wyC = restr(&Wc[y], S, c);
      if (!binspan(&LC, vx(sC, wyC), NULL)) cnt[V_SFORM]++;
      { Bas Mg = LC; for (int i = 0; i < ng; i++) badd(&Mg, va(gC[i], sC), 0); if (!binspan(&Mg, ph[c], NULL)) cnt[V_MERGE]++; }
      int fy = type == 3 ? (((h1 >> y) ^ (h1 >> e)) & 1) : ((h1 >> y) & 1);
      int gy = type == 3 ? (((h2 >> y) ^ (h2 >> e)) & 1) : ((h2 >> y) & 1);
      V U0 = vx(vk(fy), al1 ? At0 : vk(0)), Vv0 = vx(vk(gy), be1 ? At0 : vk(0));
      V UC = vx(vk(fy), al1 ? AtC : vk(0)), VvC = vx(vk(gy), be1 ? AtC : vk(0));
      V Am0 = restr(&A[M - 1], S, c0), Bm0 = restr(&B[M - 1], S, c0), AmC = restr(&A[M - 1], S, c), BmC = restr(&B[M - 1], S, c);
      V p0 = vx(Am0, va(U0, s0)), q0 = vx(Bm0, va(Vv0, s0)); u64 cp, cq;
      int okp = binspan(&L0, p0, &cp), okq = binspan(&L0, q0, &cq);
      if (!okp) cnt[V_PFORM]++; if (!okq) cnt[V_QFORM]++;
      if (!okp || !okq) continue;
      V Gam0 = vx(ph[c0], restr(&z[M - 1], S, c0));              /* Gamma on C0 */
      V Gam00 = vx(Gam0, gm1 ? va(At0, s0) : vk(0));              /* Gamma_0 */
      V G1 = vx(vx(va(p0, Vv0), va(q0, U0)), vx(va(U0, Vv0), gm1 ? At0 : vk(0)));
      int lam = vconst(G1); if (lam < 0) { cnt[V_G1]++; continue; }
      if (!binspan(&L0, vx(va(p0, q0), Gam00), NULL)) cnt[V_G0]++;
      V pC = vk(0), qC = vk(0); for (int i = 0; i < ng; i++) { if ((cp >> i) & 1) pC = vx(pC, gC[i]); if ((cq >> i) & 1) qC = vx(qC, gC[i]); }
      V U1C = vx(UC, vk(al1)), V1C = vx(VvC, vk(be1));
      int d1 = vconst(vx(vx(AmC, va(U1C, sC)), pC)), d2 = vconst(vx(vx(BmC, va(V1C, sC)), qC));
      if (d1 < 0 || d2 < 0) { cnt[V_DELTA]++; continue; }
      V Gam0C = vk(0); for (int j = 0; j <= M - 3; j++) if ((W.gm >> j) & 1) Gam0C = vx(Gam0C, zC[j]);
      V R0 = vx(va(vx(pC, vk(d1)), vx(qC, vk(d2))), Gam0C);
      V R1d = vx(vx(va(vx(pC, vk(d1)), V1C), va(vx(qC, vk(d2)), U1C)), vx(va(U1C, V1C), gm1 ? vx(AtC, ONE) : vk(0)));
      V R1s = vx(vk(lam), vx(be1 ? pC : vk(0), al1 ? qC : vk(0)));
      R1s = vx(R1s, vx((d1 ^ al1) ? VvC : vk(0), (d2 ^ be1) ? UC : vk(0)));
      R1s = vx(R1s, vk((d1 & be1) ^ (d2 & al1) ^ (al1 & be1) ^ gm1));
      if (!veq(R1d, R1s)) cnt[V_R1EQ]++;
      if (!veq(ph[c], vx(R0, va(R1d, sC)))) cnt[V_R01]++;
      continue; }
    /* (b2) */
    int used = ((W.al[M - 1] | W.be[M - 1] | W.gm) >> (M - 2)) & 1;
    if (!used) { cnt[C_B2UN]++; if (isfirst) cnt[CF_B2UN]++; continue; }
    cnt[C_B2]++; if (isfirst) cnt[CF_B2]++;
    int x = M - 2, yy = 2 * M - 2;
    int px = (h1 >> x) & 1, py = (h1 >> yy) & 1, pz = al1, rx = (h2 >> x) & 1, ry = (h2 >> yy) & 1, rz = be1;
    if (!pz && !rz) { cnt[C_B2I]++; if (((px & ry) ^ (py & rx)) != 1) cnt[V_B2EXIT]++; }
    else if (pz && !rz) { cnt[C_B2II]++; if (!rx && !ry) cnt[V_B2EXIT]++; }
    else if (!pz && rz) { cnt[C_B2III]++; if (!px && !py) cnt[V_B2EXIT]++; }
    else { cnt[C_B2IV]++; if (px == rx && py == ry) cnt[V_B2EXIT]++; }
    V X0 = restr(&A[M - 2], S, c0), Y0 = restr(&B[M - 2], S, c0), Z0 = restr(&z[M - 2], S, c0);
    V XC_ = restr(&A[M - 2], S, c), YC_ = restr(&B[M - 2], S, c), ZC_ = zC[M - 2];
    V Am0 = restr(&A[M - 1], S, c0), Bm0 = restr(&B[M - 1], S, c0), AmC = restr(&A[M - 1], S, c), BmC = restr(&B[M - 1], S, c);
    V pp0 = vx(Am0, vx(vx(px ? X0 : vk(0), py ? Y0 : vk(0)), pz ? Z0 : vk(0)));
    V qq0 = vx(Bm0, vx(vx(rx ? X0 : vk(0), ry ? Y0 : vk(0)), rz ? Z0 : vk(0)));
    V ppC = vx(AmC, vx(vx(px ? XC_ : vk(0), py ? YC_ : vk(0)), pz ? ZC_ : vk(0)));
    V qqC = vx(BmC, vx(vx(rx ? XC_ : vk(0), ry ? YC_ : vk(0)), rz ? ZC_ : vk(0)));
    if (vconst(pp0) < 0 || vconst(qq0) < 0) cnt[V_PQ0]++;
    if (vconst(ppC) < 0 || vconst(qqC) < 0) cnt[V_PQC]++;
    Bas b; base_aff_z(&b, zC, M - 1); if (!binspan(&b, ph[c], NULL)) cnt[V_B2RED]++;
  }
  (void)first_report; }


/* mode 3: nlow random wirings of gates 0..m-2 (bias as above); for each, nh random structured H; for each H, ALL
 * 2^(3(m-1)) wirings (al_{m-1}, be_{m-1}, gm) of the last gate are screened (bit-sliced) and every hit analysed. */
static u64 enc(const Wir *W) { u64 code = 0; int sh = 0;
  for (int i = 1; i < M; i++) { code |= (u64)W->al[i] << sh; sh += i; code |= (u64)W->be[i] << sh; sh += i; }
  code |= (u64)W->gm << sh; return code; }
static int rand_vec_in(u64 *rs, int mask, int sparse) { int v; do { if (sparse) { v = 0; int wt = 1 + rs_next(rs) % 3;
      for (int q = 0; q < wt; q++) { int b; do b = rs_next(rs) % D; while (!((mask >> b) & 1)); v ^= 1 << b; } }
    else v = (int)(rs_next(rs) & mask); } while (!v); return v; }
static int mode3(long nlow, long nh, u64 seed, int bias) {
  u64 rs = seed * 0x9E3779B97F4A7C15ULL + 777;
  int nlast = 3 * (M - 1); long nlw = 1L << nlast, nbk = nlw / 64;
  u64 *PHI = malloc(sizeof(u64) * nbk * NP); u64 *codes = malloc(sizeof(u64) * nlw);
  long tot[NCNT] = {0};
  int wpp = 0; for (int i = 0; i < D; i++) if (i != M - 1 && i != 2 * M - 1) wpp |= 1 << i;   /* w'' coordinates */
  int lowk = 0; for (int g = 0; g <= M - 3; g++) lowk |= (1 << g) | (1 << (M + g));         /* gates 0..m-3 */
  for (long li = 0; li < nlow; li++) {
    Wir W; decode(rand_code(&rs, bias), &W);
    for (long c = 0; c < nlw; c++) { Wir X = W; X.al[M - 1] = c & ((1 << (M - 1)) - 1); X.be[M - 1] = (c >> (M - 1)) & ((1 << (M - 1)) - 1);
      X.gm = (c >> (2 * (M - 1))) & ((1 << (M - 1)) - 1); codes[c] = enc(&X); }
    for (long b = 0; b < nbk; b++) { Wir Wb[64]; for (int w = 0; w < 64; w++) decode(codes[b * 64 + w], &Wb[w]); eval_block(Wb, PHI + b * NP); }
    int (*HL)[3] = malloc(sizeof *HL * nh);
    for (long i = 0; i < nh; i++) { int hh[3]; Sub tmp;
      do { int kind = rs_next(&rs) % 4, sp = rs_next(&rs) & 1;
        if (kind <= 1) {        /* dim pi = 2 aimed at (b): t with top < m-2 (kind 0) or any (kind 1) */
          hh[0] = rand_vec_in(&rs, kind == 0 ? lowk : wpp, sp);
          hh[1] = (1 << (M - 1)) | (int)(rs_next(&rs) & wpp & (sp ? (int)rs_next(&rs) : -1));
          hh[2] = (1 << (2 * M - 1)) | (int)(rs_next(&rs) & wpp & (sp ? (int)rs_next(&rs) : -1)); }
        else if (kind == 2) {   /* dim pi = 1 */
          hh[0] = rand_vec_in(&rs, wpp, sp); hh[1] = rand_vec_in(&rs, wpp, sp);
          int pq = 1 + rs_next(&rs) % 3; hh[2] = (int)(rs_next(&rs) & wpp) | ((pq & 1) << (M - 1)) | ((pq >> 1) << (2 * M - 1)); }
        else { for (int j = 0; j < 3; j++) hh[j] = (int)(rs_next(&rs) & (NP - 1)); }
      } while (!setup_sub(&tmp, hh));
      HL[i][0] = hh[0]; HL[i][1] = hh[1]; HL[i][2] = hh[2]; }
    #pragma omp parallel
    { long cnt[NCNT] = {0}; Sub *S = malloc(sizeof(Sub));
      #pragma omp for schedule(dynamic, 1)
      for (long si = 0; si < nh; si++) { setup_sub(S, HL[si]);
        for (long b = 0; b < nbk; b++) { u64 aff[8]; screen(S, PHI + b * NP, aff);
          u64 any = 0, all = ~0ULL; for (int d = 0; d < 8; d++) { any |= aff[d]; all &= aff[d]; }
          u64 hit = any & ~all;
          while (hit) { int w = __builtin_ctzll(hit); hit &= hit - 1; u64 affs = 0; for (int d = 0; d < 8; d++) affs |= ((aff[d] >> w) & 1) << d;
            analyze(codes[b * 64 + w], S, affs, cnt); } } }
      #pragma omp critical
      for (int i = 0; i < NCNT; i++) tot[i] += cnt[i];
      free(S); }
    free(HL); }
  long viol = 0; for (int i = 0; i < NCNT; i++) if (!strncmp(cname[i], "VIOL", 4) || !strncmp(cname[i], "ERR", 3)) viol += tot[i];
  printf("m=%d mode=3 lower wirings=%ld H per lower wiring=%ld last-gate wirings each=%ld bias=%d seed=%llu\n", M, nlow, nh, nlw, bias, (unsigned long long)seed);
  for (int i = 0; i < NCNT; i++) printf("  %-48s %ld\n", cname[i], tot[i]);
  printf("  TOTAL VIOLATIONS/ERRORS: %ld\n", viol);
  return 0; }

int main(int argc, char **argv) {
  M = atoi(argv[1]); int mode = atoi(argv[2]);
  D = 2 * M; NP = 1 << D; KD = D - 3; NC = 1 << KD; TW = NP / 64; CWn = NC >= 64 ? NC / 64 : 1;
  if (M < 3 || M > MAXM) { fprintf(stderr, "m in 3..6\n"); return 1; }
  for (int i = 0; i < D; i++) { memset(&Wc[i], 0, sizeof(Tab)); for (int p = 0; p < NP; p++) if ((p >> i) & 1) Wc[i].w[p >> 6] |= 1ULL << (p & 63); }
  memset(&ONE, 0, sizeof ONE); for (int x = 0; x < NC; x++) ONE.w[x >> 6] |= 1ULL << (x & 63);
  for (int r = 0; r < KD; r++) { memset(&XC[r], 0, sizeof(V)); for (int x = 0; x < NC; x++) if ((x >> r) & 1) XC[r].w[x >> 6] |= 1ULL << (x & 63); }
  long nblocks = 0; u64 seed = 1; int bias = 0; long nsub_rand = 0;
  long nlist = 0; u64 *list = NULL;
  if (mode == 5) { FILE *fp = fopen(argv[3], "r"); list = malloc(sizeof(u64) * 4000000); unsigned long long cv;
    while (fscanf(fp, "%llu", &cv) == 1) list[nlist++] = cv; fclose(fp); }
  if (mode == 3) return mode3(atol(argv[3]), atol(argv[4]), strtoull(argv[5], 0, 10), atoi(argv[6]));
  if (mode == 5) { nblocks = 0; }
  else if (mode == 0 || mode == 2) { nblocks = atol(argv[3]); seed = strtoull(argv[4], 0, 10); bias = atoi(argv[5]); }
  else { nsub_rand = atol(argv[3]); nblocks = atol(argv[4]); seed = strtoull(argv[5], 0, 10); bias = atoi(argv[6]); }
  u64 rs = seed * 0x9E3779B97F4A7C15ULL + 12345;
  /* wiring blocks */
  long nw_all = 1L << nbits_wiring(); long nb;
  if (mode == 0 && nblocks <= 0) nb = (nw_all + 63) / 64; else nb = nblocks;
  if (mode == 5) nb = (nlist + 63) / 64;
  u64 *codes = malloc(sizeof(u64) * nb * 64);
  for (long i = 0; i < nb * 64; i++) codes[i] = (mode == 5) ? list[i < nlist ? i : 0] : (mode == 0 && nblocks <= 0) ? (u64)(i % nw_all) : rand_code(&rs, bias);
  u64 *PHI = malloc(sizeof(u64) * nb * NP);
  for (long b = 0; b < nb; b++) { Wir Wb[64]; for (int w = 0; w < 64; w++) decode(codes[b * 64 + w], &Wb[w]); eval_block(Wb, PHI + b * NP); }
  /* subspaces */
  long nsub = 0, cap = 0; int (*HL)[3] = NULL;
  if (mode == 0 || mode == 2 || mode == 5) {
    int Dsub = (mode == 0 || mode == 5) ? D : 8; int gsets[64][4], ngs = 0;
    if (mode == 2) { for (int a = 0; a < M - 1; a++) for (int b = a + 1; b < M - 1; b++) for (int c = b + 1; c < M - 1; c++) { gsets[ngs][0] = a; gsets[ngs][1] = b; gsets[ngs][2] = c; gsets[ngs][3] = M - 1; ngs++; } }
    else ngs = 1;
    cap = 7000000L * (mode == 2 ? 2 : 1); HL = malloc(sizeof *HL * cap);
    for (int gsi = 0; gsi < ngs; gsi++) {
      int cmap[16]; if (mode == 2) { for (int q = 0; q < 4; q++) { cmap[2 * q] = gsets[gsi][q]; cmap[2 * q + 1] = M + gsets[gsi][q]; } } else for (int q = 0; q < D; q++) cmap[q] = q;
      for (int P1 = Dsub - 1; P1 >= 0; P1--) for (int P2 = P1 - 1; P2 >= 0; P2--) for (int P3 = P2 - 1; P3 >= 0; P3--) {
        int Pp[3] = {P1, P2, P3}; int fq[3][16], nfq[3];
        for (int i = 0; i < 3; i++) { nfq[i] = 0; for (int q = 0; q < Pp[i]; q++) if (q != P1 && q != P2 && q != P3) fq[i][nfq[i]++] = q; }
        for (long a = 0; a < (1L << nfq[0]); a++) for (long b2 = 0; b2 < (1L << nfq[1]); b2++) for (long c2 = 0; c2 < (1L << nfq[2]); c2++) {
          long cc[3] = {a, b2, c2}; int hh[3];
          for (int i = 0; i < 3; i++) { int hv = 1 << Pp[i]; for (int j = 0; j < nfq[i]; j++) if ((cc[i] >> j) & 1) hv |= 1 << fq[i][j];
            int hm = 0; for (int q = 0; q < Dsub; q++) if ((hv >> q) & 1) hm |= 1 << cmap[q]; hh[i] = hm; }
          if (nsub >= cap) { fprintf(stderr, "cap\n"); return 2; }
          HL[nsub][0] = hh[0]; HL[nsub][1] = hh[1]; HL[nsub][2] = hh[2]; nsub++; } } }
  } else {
    nsub = nsub_rand; HL = malloc(sizeof *HL * nsub);
    for (long i = 0; i < nsub; i++) { int hh[3]; Sub tmp;
      do { for (int j = 0; j < 3; j++) { u64 r = rs_next(&rs); int kind = r & 3; int hv;
          if (kind == 0) hv = (int)((r >> 8) & (NP - 1));                                /* uniform */
          else { hv = 0; int wt = 1 + ((r >> 4) & 3) % 3; for (int q = 0; q < wt; q++) hv ^= 1 << ((rs_next(&rs) >> 7) % D); }  /* weight <= 3 */
          if (j == 1 && ((r >> 40) & 1)) hv |= 1 << (M - 1); if (j == 2 && ((r >> 41) & 1)) hv |= 1 << (2 * M - 1);
          hh[j] = hv; } } while (!setup_sub(&tmp, hh));
      HL[i][0] = hh[0]; HL[i][1] = hh[1]; HL[i][2] = hh[2]; } }
  fprintf(stderr, "m=%d mode=%d subspaces=%ld wiring blocks=%ld (wirings %ld) bias=%d\n", M, mode, nsub, nb, nb * 64, bias);
  long tot[NCNT] = {0};
  if (getenv("SELFTEST")) {            /* compare bit-sliced screening with the single-wiring derivative test */
    long nt = atol(getenv("SELFTEST")), mism = 0, affpos = 0, cos_checked = 0; Sub *S = malloc(sizeof(Sub));
    for (long it = 0; it < nt; it++) { long si = (long)(rs_next(&rs) % (u64)nsub), b = (long)(rs_next(&rs) % (u64)nb);
      if (!setup_sub(S, HL[si])) continue; u64 aff[8]; screen(S, PHI + b * NP, aff);
      for (int w = 0; w < 64; w++) { Wir W; decode(codes[b * 64 + w], &W); static Tab z[MAXM], A[MAXM], B[MAXM], Ph; eval_tabs(&W, z, A, B, &Ph);
        for (int d = 0; d < 8; d++) { int a1 = is_affine_deriv(restr(&Ph, S, d)), a0 = (aff[d] >> w) & 1; cos_checked++; affpos += a1; if (a1 != a0) mism++; } } }
    printf("SELFTEST m=%d: (H,block) samples %ld, cosets checked %ld, affine cosets %ld, screening mismatches %ld\n", M, nt, cos_checked, affpos, mism);
    return 0; }
  #pragma omp parallel
  { long cnt[NCNT] = {0}; Sub *S = malloc(sizeof(Sub));
    #pragma omp for schedule(dynamic, 64)
    for (long si = 0; si < nsub; si++) {
      if (!setup_sub(S, HL[si])) continue;
      long bl0 = 0, bl1 = nb;
      if (mode == 1) { u64 st = (u64)si * 0x9E3779B97F4A7C15ULL ^ seed; bl0 = rs_next(&st) % (nb > nblocks ? nb : nb); bl1 = bl0 + 1; }
      for (long b = bl0; b < bl1; b++) {
        u64 aff[8]; screen(S, PHI + b * NP, aff);
        u64 any = 0, all = ~0ULL; for (int d = 0; d < 8; d++) { any |= aff[d]; all &= aff[d]; }
        u64 hit = any & ~all;
        if (mode == 5 && (b + 1) * 64 > nlist) { long valid = nlist - b * 64; hit &= valid >= 64 ? ~0ULL : ((1ULL << valid) - 1); }
        while (hit) { int w = __builtin_ctzll(hit); hit &= hit - 1;
          u64 affs = 0; for (int d = 0; d < 8; d++) affs |= ((aff[d] >> w) & 1) << d;
          analyze(codes[b * 64 + w], S, affs, cnt); } } }
    #pragma omp critical
    for (int i = 0; i < NCNT; i++) tot[i] += cnt[i];
    free(S); }
  long viol = 0; for (int i = 0; i < NCNT; i++) if (!strncmp(cname[i], "VIOL", 4) || !strncmp(cname[i], "ERR", 3)) viol += tot[i];
  printf("m=%d mode=%d subspaces=%ld wirings=%ld bias=%d seed=%llu\n", M, mode, nsub, nb * 64, bias, (unsigned long long)seed);
  for (int i = 0; i < NCNT; i++) printf("  %-48s %ld\n", cname[i], tot[i]);
  printf("  TOTAL VIOLATIONS/ERRORS: %ld\n", viol);
  return 0; }
```

### A.2 `p12.c`

```c
/* AUDIT-004 (auditor's own code): direct test of facts (P1), (P2) and the "non-degeneracy" equivalences
 * of PNE-001-codim3.md, on the w''-space of a formal circuit.
 * Convention (differs from EXP-018): G gates 0..G-1 on 2G coordinates; gate i reads A-coordinate i and
 * B-coordinate G+i:  z_i = (w_i + sum_{j<i} al[i]_j z_j)(w_{G+i} + sum_{j<i} be[i]_j z_j).
 * (These are gates 1..m-1 of an m-gate formal circuit, G = m-1.)
 * For every wiring (or a random sample), every t != 0 and every c:
 *   k = top(t), type, e, tau = e_e, s, Atilde as in (P1);  E = {<t,w> = c}.
 *   (P1a) z_j(w+tau) = z_j(w) on E for j<k;  (P1b) z_k = Atilde*s on E;  (P1c) z_k(w+tau) = (Atilde+1)*s on E.
 *   (ND)  Atilde constant on E  <=>  stated degeneracy condition (type1: al_k=0 & t=e_A; type2: be_k=0 & t=e_B;
 *         type3: al_k=be_k & t=e_A+e_B).
 *   (P2)  if Atilde non-constant: {(l,c): l + c.z constant on E} = {0,(t,0)}  (kernel dimension exactly 1).
 * Usage: p12 G nsamples seed   (nsamples <= 0: all wirings) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u64;
#define MAXG 6
#define MAXW 64            /* 2^(2G) <= 4096 bits */
#define MAXE 32            /* |E| <= 2048 bits */
static int G, D, NP, NE, NWE;
typedef struct { u64 w[MAXW]; } Tab;
typedef struct { u64 w[MAXE]; } Vec;
static int tget(const Tab *t, int p) { return (t->w[p >> 6] >> (p & 63)) & 1; }
static u64 rng_s = 88172645463325252ULL;
static u64 rng(void) { rng_s ^= rng_s << 13; rng_s ^= rng_s >> 7; rng_s ^= rng_s << 17; return rng_s; }
/* rank of a set of vectors over F2 (destroys input) */
static int rank_of(Vec *v, int n) {
  int r = 0;
  for (int col = 0; col < NE && r < n; col++) {
    int piv = -1; for (int i = r; i < n; i++) if ((v[i].w[col >> 6] >> (col & 63)) & 1) { piv = i; break; }
    if (piv < 0) continue;
    Vec t = v[piv]; v[piv] = v[r]; v[r] = t;
    for (int i = 0; i < n; i++) if (i != r && ((v[i].w[col >> 6] >> (col & 63)) & 1)) for (int q = 0; q < NWE; q++) v[i].w[q] ^= v[r].w[q];
    r++; }
  return r; }
static int is_const(const Vec *v) { int b = v->w[0] & 1; u64 ref = b ? ~0ULL : 0;
  for (int q = 0; q < NWE; q++) { u64 m = (NE >= 64 * (q + 1)) ? ~0ULL : ((1ULL << (NE - 64 * q)) - 1); if ((v->w[q] ^ ref) & m) return 0; } return 1; }

int main(int argc, char **argv) {
  G = atoi(argv[1]); long ns = atol(argv[2]); rng_s ^= (u64)atol(argv[3]) * 0x9E3779B97F4A7C15ULL;
  D = 2 * G; NP = 1 << D; NE = NP / 2; NWE = NE >= 64 ? NE / 64 : 1;
  int nwt = NP >= 64 ? NP / 64 : 1;
  Tab W[2 * MAXG]; for (int i = 0; i < D; i++) { memset(&W[i], 0, sizeof(Tab)); for (int p = 0; p < NP; p++) if ((p >> i) & 1) W[i].w[p >> 6] |= 1ULL << (p & 63); }
  int wbits = G * (G - 1); long nw_all = 1L << wbits;
  long nrun = (ns <= 0 || ns >= nw_all) ? nw_all : ns;
  long cnt_trip = 0, cnt_nd = 0, cnt_deg = 0, f_p1a = 0, f_p1b = 0, f_p1c = 0, f_nd = 0, f_p2 = 0;
  long kerhist_deg[8] = {0};
  int *Eidx = malloc(sizeof(int) * NE);
  for (long ii = 0; ii < nrun; ii++) {
    long code = (nrun == nw_all) ? ii : (long)(rng() & (nw_all - 1));
    int al[MAXG] = {0}, be[MAXG] = {0}; long r = code;
    for (int i = 1; i < G; i++) { al[i] = r & ((1 << i) - 1); r >>= i; be[i] = r & ((1 << i) - 1); r >>= i; }
    Tab z[MAXG], A[MAXG], B[MAXG];
    for (int i = 0; i < G; i++) { A[i] = W[i]; B[i] = W[G + i];
      for (int j = 0; j < i; j++) { if ((al[i] >> j) & 1) for (int q = 0; q < nwt; q++) A[i].w[q] ^= z[j].w[q];
                                    if ((be[i] >> j) & 1) for (int q = 0; q < nwt; q++) B[i].w[q] ^= z[j].w[q]; }
      for (int q = 0; q < nwt; q++) z[i].w[q] = A[i].w[q] & B[i].w[q]; }
    for (int t = 1; t < NP; t++) for (int c = 0; c < 2; c++) {
      cnt_trip++;
      int k = -1; for (int i = 0; i < G; i++) if (((t >> i) & 1) || ((t >> (G + i)) & 1)) k = i;
      int tA = (t >> k) & 1, tB = (t >> (G + k)) & 1, type = tA && !tB ? 1 : (!tA && tB ? 2 : 3);
      int e = (type == 1) ? k : G + k; int tau = 1 << e;
      int tlow = t & ~((1 << k) | (1 << (G + k)));
      /* Atilde as a function on F_2^D */
      Tab At; for (int q = 0; q < nwt; q++) At.w[q] = c ? ~0ULL : 0;
      for (int i = 0; i < D; i++) if ((tlow >> i) & 1) for (int q = 0; q < nwt; q++) At.w[q] ^= W[i].w[q];
      int cf = (type == 1) ? al[k] : (type == 2 ? be[k] : (al[k] ^ be[k]));
      for (int j = 0; j < k; j++) if ((cf >> j) & 1) for (int q = 0; q < nwt; q++) At.w[q] ^= z[j].w[q];
      if (type == 3) for (int q = 0; q < nwt; q++) At.w[q] = ~At.w[q];
      const Tab *s = (type == 1) ? &B[k] : &A[k];
      int ne = 0; for (int p = 0; p < NP; p++) if ((__builtin_popcount(p & t) & 1) == c) Eidx[ne++] = p;
      /* P1 */
      int bad1a = 0, bad1b = 0, bad1c = 0, atc = -1, atconst = 1;
      for (int n = 0; n < ne; n++) { int p = Eidx[n];
        for (int j = 0; j < k; j++) if (tget(&z[j], p ^ tau) != tget(&z[j], p)) bad1a = 1;
        int a = tget(&At, p), sv = tget(s, p);
        if (tget(&z[k], p) != (a & sv)) bad1b = 1;
        if (tget(&z[k], p ^ tau) != ((a ^ 1) & sv)) bad1c = 1;
        if (atc < 0) atc = a; else if (a != atc) atconst = 0; }
      f_p1a += bad1a; f_p1b += bad1b; f_p1c += bad1c;
      int pred_const = (type == 1) ? (al[k] == 0 && t == (1 << k)) : (type == 2) ? (be[k] == 0 && t == (1 << (G + k)))
                                    : (al[k] == be[k] && t == ((1 << k) | (1 << (G + k))));
      if (pred_const != atconst) f_nd++;
      /* P2 kernel */
      Vec v[3 * MAXG + 1]; int nv = 0; memset(v, 0, sizeof(v));
      for (int n = 0; n < ne; n++) v[0].w[n >> 6] |= 1ULL << (n & 63);
      nv = 1;
      for (int i = 0; i < D; i++) { for (int n = 0; n < ne; n++) if ((Eidx[n] >> i) & 1) v[nv].w[n >> 6] |= 1ULL << (n & 63); nv++; }
      for (int j = 0; j < G; j++) { for (int n = 0; n < ne; n++) if (tget(&z[j], Eidx[n])) v[nv].w[n >> 6] |= 1ULL << (n & 63); nv++; }
      int rk = rank_of(v, nv); int ker = (nv - 1) - (rk - 1);
      if (!atconst) { cnt_nd++; if (ker != 1) f_p2++; }
      else { cnt_deg++; if (ker < 8) kerhist_deg[ker]++; }
    }
  }
  printf("G=%d (m=%d) wirings=%ld (of %ld) triples(w,t,c)=%ld | Atilde non-const=%ld const=%ld\n", G, G + 1, nrun, nw_all, cnt_trip, cnt_nd, cnt_deg);
  printf("  failures: P1a(gates<k tau-invariant)=%ld P1b(z_k=A~s)=%ld P1c(z_k(w+tau)=(A~+1)s)=%ld ND(equivalence)=%ld P2(kernel dim 1)=%ld\n", f_p1a, f_p1b, f_p1c, f_nd, f_p2);
  printf("  (info) kernel dims when Atilde const:"); for (int i = 0; i < 8; i++) printf(" %d:%ld", i, kerhist_deg[i]); printf("\n");
  return 0; }
```

### A.3 `mc4.c`

```c
/* AUDIT-004: every 4-variable Boolean function has MC <= 3 (independent span search; truth tables = 16-bit ints).
 * z1 = l1*l2 (l1,l2 linear forms), W1 = aff + <z1>; z2 = A*B (A,B in W1), W2 = W1 + <z2>; z3 = A*B (A,B in W2);
 * mark z3 + W2.  Union over all choices = functions with an (at most) 3-AND circuit whose output is z3 + (W2 element). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static unsigned char mark[65536], mark2[65536];
static int lin[16];
int main(void) {
  for (int a = 0; a < 16; a++) { int t = 0; for (int x = 0; x < 16; x++) if (__builtin_popcount(a & x) & 1) t |= 1 << x; lin[a] = t; }
  int W0[32]; for (int a = 0; a < 16; a++) { W0[a] = lin[a]; W0[16 + a] = lin[a] ^ 0xFFFF; }
  static unsigned char seenW2[1 << 16]; long nW2 = 0;
  for (int l1 = 0; l1 < 16; l1++) for (int l2 = 0; l2 < 16; l2++) {
    int z1 = lin[l1] & lin[l2]; int W1[64]; for (int i = 0; i < 32; i++) { W1[i] = W0[i]; W1[32 + i] = W0[i] ^ z1; }
    for (int i = 0; i < 64; i++) mark2[W1[i]] = 1;
    for (int ia = 0; ia < 64; ia++) for (int ib = ia; ib < 64; ib++) {
      int z2 = W1[ia] & W1[ib]; int W2[128]; for (int i = 0; i < 64; i++) { W2[i] = W1[i]; W2[64 + i] = W1[i] ^ z2; }
      for (int i = 0; i < 128; i++) mark2[W2[i]] = 1;
      /* canonical id of W2: min over elements is not canonical; use sorted set hash -> just process (cheap enough) */
      int key = 0; for (int i = 0; i < 128; i++) if (W2[i] != 0 && (key == 0 || W2[i] < key) && W2[i] != 0xFFFF && __builtin_popcount(W2[i]) != 8) key = W2[i];
      (void)key; nW2++;
      /* cosets z3 + W2: reduce z3 mod W2 via a basis */
      int bas[8], piv[8], nb = 0;
      for (int i = 0; i < 128; i++) { int v = W2[i]; for (int j = 0; j < nb; j++) if ((v >> piv[j]) & 1) v ^= bas[j];
        if (v) { int p = 31 - __builtin_clz(v); for (int j = 0; j < nb; j++) if ((bas[j] >> p) & 1) bas[j] ^= v; bas[nb] = v; piv[nb] = p; nb++; } }
      static unsigned char cos[65536]; static int clist[65536]; int nc = 0;
      for (int a = 0; a < 128; a++) for (int b = a; b < 128; b++) { int v = W2[a] & W2[b];
        for (int j = 0; j < nb; j++) if ((v >> piv[j]) & 1) v ^= bas[j];
        if (!cos[v]) { cos[v] = 1; clist[nc++] = v; } }
      for (int c = 0; c < nc; c++) { for (int i = 0; i < 128; i++) mark[clist[c] ^ W2[i]] = 1; cos[clist[c]] = 0; }
    } }
  long n3 = 0, n2 = 0, deg4 = 0, deg4_in3 = 0, le3_in2 = 0, nle3 = 0;
  for (int f = 0; f < 65536; f++) { n3 += mark[f]; n2 += mark2[f];
    int a = f; for (int i = 0; i < 4; i++) { int s = 1 << i; for (int x = 0; x < 16; x++) if (x & s) if ((a >> (x ^ s)) & 1) a ^= 1 << x; }
    int top = (a >> 15) & 1; if (top) { deg4++; deg4_in3 += mark[f]; } else { nle3++; le3_in2 += mark2[f]; } }
  printf("W2 choices %ld | functions with <=3-AND circuit: %ld of 65536 | with <=2-AND circuit: %ld | degree-4: %ld (all in <=3: %ld) | degree<=3: %ld (in <=2: %ld)\n",
         nW2, n3, n2, deg4, deg4_in3, nle3, le3_in2);
  return 0; }
```

### A.4 `picks.c`

```c
/* Reproduce EXP-018 codim3.c's wiring sample (srand(seed); pick = (((long)rand() << 31) ^ rand()) % nw) and decode it
 * with codim3.c's decoder; print each wiring in the auditor's encoding (al_i, be_i for i=1..M-1, then gm). */
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
  int M = atoi(argv[1]); long samples = atol(argv[2]); unsigned seed = atoi(argv[3]);
  int lim[5] = {1, 2, 4, 8, 16}; long nw = 1; for (int i = 1; i < M; i++) nw *= (long)lim[i] * (lim[i] + 1) / 2; nw *= 1 << (M - 1);
  long nrun = samples <= 0 || samples > nw ? nw : samples;
  long *pick = malloc(nrun * sizeof(long)); srand(seed);
  for (long i = 0; i < nrun; i++) pick[i] = (nrun == nw) ? i : ((((long)rand() << 31) ^ rand()) % nw);
  for (long ii = 0; ii < nrun; ii++) {
    long r = pick[ii]; int al[5] = {0}, be[5] = {0}, gm = r % (1 << (M - 1)); r /= (1 << (M - 1));
    for (int i = M - 1; i >= 1; i--) { int L = lim[i], np = L * (L + 1) / 2, kk = r % np; r /= np; int a = 0; while (kk >= L - a) { kk -= L - a; a++; } al[i] = a; be[i] = a + kk; }
    unsigned long long code = 0; int sh = 0;
    for (int i = 1; i < M; i++) { code |= (unsigned long long)al[i] << sh; sh += i; code |= (unsigned long long)be[i] << sh; sh += i; }
    code |= (unsigned long long)gm << sh; printf("%llu\n", code); }
  return 0; }
```

### A.5 `hc_audit.py`

```python
# AUDIT-004: independent re-check of the claims about hc_sample.txt (own code; reads only the data file).
# Line format (from hc_lib.parse): HC a1 a2 a3 b1 b2 b3 gm  basis(5 ints)  c0 c1  tab(hex)
# Convention of the data: gate i (0..3) reads bits 2i (A) and 2i+1 (B) of a point p in [0,256).
import sys
from collections import Counter
def gatevals(p, al, be):
    z, ins = [], []
    for i in range(4):
        A = (p >> (2*i)) & 1; B = (p >> (2*i+1)) & 1
        for j in range(i):
            if (al[i] >> j) & 1: A ^= z[j]
            if (be[i] >> j) & 1: B ^= z[j]
        ins.append((A, B)); z.append(A & B)
    return z, ins
def span_has(gens, target):
    piv = {}
    for g in gens:
        v = g
        while v:
            h = v.bit_length() - 1
            if h in piv: v ^= piv[h]
            else: piv[h] = v; break
    v = target
    while v:
        h = v.bit_length() - 1
        if h in piv: v ^= piv[h]
        else: return False
    return True
def is_affine(vec, k):
    a = [(vec >> t) & 1 for t in range(1 << k)]
    for i in range(k):
        for t in range(1 << k):
            if (t >> i) & 1: a[t] ^= a[t ^ (1 << i)]
    return all(a[t] == 0 for t in range(1 << k) if bin(t).count('1') >= 2)
C = Counter(); bad = Counter()
lines = [l for l in open(sys.argv[1]) if l.startswith('HC')]
for l in lines:
    t = l.split(); a1,a2,a3,b1,b2,b3,gm = map(int, t[1:8]); basis = list(map(int, t[8:13])); c0, c1 = int(t[13]), int(t[14]); tab = int(t[15], 16)
    al = [0,a1,a2,a3]; be = [0,b1,b2,b3]; k = len(basis); n = 1 << k
    def pts(c): 
        out = []
        for x in range(n):
            q = c
            for r in range(k):
                if (x >> r) & 1: q ^= basis[r]
            out.append(q)
        return out
    P0, P1 = pts(c0), pts(c1)
    if len(set(q ^ c0 for q in P0)) != n: bad['basis not independent'] += 1
    def vec(P, f): return sum(1 << x for x, p in enumerate(P) if f(p))
    def phi(p):
        z, _ = gatevals(p, al, be); v = z[3]
        for j in range(3):
            if (gm >> j) & 1: v ^= z[j]
        return v
    ph1 = vec(P1, phi); ph0 = vec(P0, phi)
    if ph1 != tab: bad['stored table != Phi|C1'] += 1
    if not is_affine(ph0, k): bad['C0 not affine'] += 1
    if is_affine(ph1, k): bad['C1 affine'] += 1
    H = [h for h in range(1, 256) if all(bin(h & b).count('1') % 2 == 0 for b in basis)]
    proj = set((h >> 6) & 3 for h in H)
    if len(H) != 7 or not {1, 2, 3} <= proj: bad['not dim pi = 2'] += 1; continue
    h0 = [h for h in H if (h >> 6) & 3 == 0][0]
    if (bin(h0 & c0).count('1') & 1) == (bin(h0 & c1).count('1') & 1): bad['same H0 class'] += 1
    # degenerate (Lemma 24) and redundancy (hard core = no gate redundant on C1)
    deg = any((al[i] == 0 and (1 << 2*i) in H) or (be[i] == 0 and (1 << (2*i+1)) in H) or (al[i] == be[i] and (3 << 2*i) in H) for i in range(4))
    if deg: bad['degenerate'] += 1
    zs = [vec(P1, lambda p, i=i: gatevals(p, al, be)[0][i]) for i in range(4)]
    one = n and (1 << n) - 1; coords = [sum(1 << x for x in range(n) if (x >> r) & 1) for r in range(k)]
    aff = [one] + coords
    zs3 = zs[:3] + [ph1]
    red = [span_has(aff + zs[:i], zs3[i] if i == 3 else zs[i]) for i in range(4)]
    if any(red): bad['some gate redundant on C1 (not hard core)'] += 1
    used = [False]*3
    for i in range(1, 4):
        for j in range(i):
            if ((al[i] | be[i]) >> j) & 1: used[j] = True
    for j in range(3):
        if (gm >> j) & 1: used[j] = True
    unused = [j for j in range(3) if not used[j]]
    topk = max(i for i in range(3) if (h0 >> (2*i)) & 3); typ = (h0 >> (2*topk)) & 3
    C['total'] += 1
    if unused: C['has unused gate'] += 1; C['unused gate %d (highest unused)' % max(unused)] += 1
    else: C['all used'] += 1; C['all used, top=%d' % topk] += 1
    C['top=%d, gate m-1 (0-idx 2) used=%s' % (topk, used[2])] += 1
    if topk == 2:
        C['top=m-1'] += 1
        A2 = vec(P1, lambda p: gatevals(p, al, be)[1][2][0]); B2 = vec(P1, lambda p: gatevals(p, al, be)[1][2][1])
        s = B2 if typ == 1 else A2
        V = aff + zs[:2]
        if span_has(V + [v & s for v in V], ph1): C['top=m-1: merge with predicted s'] += 1
        else: bad['merge fails'] += 1
        # strict (y-free) version: coordinates of gates 0,1 only (bits 0..3), evaluated on C1
        y = 5 if typ == 1 else 4
        L0 = [one] + [vec(P1, lambda p, b=b: (p >> b) & 1) for b in range(4)] + zs[:2]
        if span_has(L0 + [v & s for v in L0], ph1): C['top=m-1: strict y-free merge'] += 1
        else: bad['strict merge fails'] += 1
        so = A2 if typ == 1 else B2
        if typ in (1, 2):
            C['type %d: other input also works' % typ] += span_has(V + [v & so for v in V], ph1)
for kk, v in sorted(C.items()): print('  %-45s %d' % (kk, v))
print('  anomalies:', dict(bad) if bad else 'none')
```

