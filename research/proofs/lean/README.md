# NP-FRONTIER Lean project

Core Lean 4 only (toolchain in `lean-toolchain`; no Mathlib, because its build-cache host is blocked in the
cloud container). Setup: `scripts/setup_env.sh`. Build: `lake build --wfail` (fails on any warning, including
`sorry`). `NPFrontier/Axioms.lean` prints `#print axioms` for every headline theorem on each build.

## Verified theorems (cycle 001)

File `NPFrontier/BoolFun.lean`. Boolean functions on `n` variables are Shannon trees `BF n`:
`node f₀ f₁` is the function whose restrictions to `x = 0` and `x = 1` (last variable) are `f₀`, `f₁`.

| Lean name | Informal statement | Axioms |
|---|---|---|
| `BF.peval_anf` | The Möbius transform `anf f`, evaluated as a polynomial over 𝔽₂, equals `f` at every input. This ties `anf` to the usual algebraic normal form. | propext |
| `BF.anf_xor` | The ANF is linear: `anf (f ⊕ g) = anf f ⊕ anf g`. | propext |
| `BF.top_anf` | The ANF coefficient of `x₁⋯xₙ` equals the parity of the weight of `f`. | propext |
| `BF.degLE_pred_iff_even_weight` | For `f` on `n+1` variables: `deg f ≤ n` iff `f` has even weight. Equivalently, `deg f = n+1` iff the weight is odd. | propext, Classical.choice, Quot.sound |
| `BF.degLE_xor` | `deg (a ⊕ b) ≤ max (deg a) (deg b)`. | propext |
| `BF.degLE_node_of_restrict` | If both restrictions of `f` on the last variable have degree `≤ d`, then `deg f ≤ d+1`. This is Lemma 3 of PNE-001 for coordinate hyperplanes: one restriction keeps degree `≥ deg f − 1`. | propext, Classical.choice, Quot.sound |
| `BF.degLE_restrict` | Restricting a variable does not increase degree. | propext, Classical.choice, Quot.sound |
| `gate_normalize` | `(y+α)(y+β) = (y+α)(1+α+β)` over 𝔽₂ (gate normalization in Theorem 4 of PNE-001). | none |
| `mul_eval_one` | `u·h(u,x) = u·h(1,x)` (the identity used in Case C of Theorem 4). | none |
| `same_direction_product` | Affine forms with the same linear part multiply to an affine function (`l+c` or `0`). This is the key step of Lemma 12. | none |

## Gaps between the formal and informal statements

- **Weight parity:** `par` is defined recursively, as the XOR of the parities of the two halves. Its agreement with "number of inputs `xs` with `eval f xs = true`, mod 2" is not proved; it holds by construction of the Shannon split.
- **Degree:** `DegLE c d` is a recursive predicate on coefficient trees. Its agreement with "every monomial with nonzero coefficient has at most `d` variables" holds by construction and is not separately proved.
- **Lemma 3** is formalized only for hyperplanes `{x = c}` on a single coordinate. The general case `{⟨v,x⟩ = c}` needs affine changes of coordinates, which are not formalized.
- **Not formalized:** Lemma 1 (D ≤ MC), Lemma 2, Theorem 4 (`D(y·g) = D(g) + 1`), and Corollaries 5–7 of PNE-001. XOR-AND circuits and their gate-elimination and affine-substitution facts are now formalized (cycle 002, next section). These results still need restriction depth `D` and affine parametrizations of hyperplanes, which are not formalized.

## XOR-AND circuits (cycle 002)

File `NPFrontier/Circuit.lean`. It formalizes facts (i) and (ii) below, in the form in which the PNE-001 documents use
them. Among other places, (i) is used in Lemmas 1, 9 and 12 of `../PNE-001-restriction-depth-and-fresh-variables.md`
and in Lemmas 9′, 24 and (through Lemma 24) 28 of `../PNE-001-level4.md`. Among other places, (ii) is used in (F1),
(F2) and (F4), and therefore in Lemmas 23 and 26.

- **(i) Gate elimination.** Suppose that on a set `S` of inputs one input of gate `i` is constant, or the two inputs
  of gate `i` differ by a constant. Then some circuit with one AND gate fewer computes the same output on `S`.
- **(ii) Affine substitution.** Composing a circuit with an affine map of the inputs keeps the number of AND gates.
  Adding an affine function to the output is free.

### Definitions and representation

Bit vectors are functions `Fin k → Bool`. This makes deleting a coordinate (`Vec.removeAt`), taking a prefix
(`Vec.take`) and padding with zeros (`Vec.pad`) one-line definitions, and every vector lemma a structural induction
on `k`.

| Lean name | Meaning |
|---|---|
| `Vec.xorSum v` | `v 0 ⊕ ⋯ ⊕ v (k−1)`, by recursion on `k` (peeling off the last entry); the empty sum is `false`. |
| `Vec.dot a v` | Inner product over 𝔽₂: `xorSum (fun j => a j && v j)`. |
| `AffForm n k` | Affine form over `n` inputs and `k` gates: fields `const : Bool`, `inp : Fin n → Bool`, `gat : Fin k → Bool`. `AffForm.eval L x z = const ⊕ ⟨inp, x⟩ ⊕ ⟨gat, z⟩`. |
| `Circuit n m` | `left i, right i : AffForm n i` for each gate `i : Fin m` (forms over the inputs and the `i` earlier gates), and `out : AffForm n m`. |
| `Circuit.vals C x i` | Value of gate `i` at input `x`. It is defined by well-founded recursion on `i`: gate `i` is `left i` AND `right i`, both evaluated at `x` and at the values of gates `0, …, i−1`. |
| `Circuit.eval C x` | `out.eval x (vals x)`, the function computed by `C`. |
| `Circuit.prev`, `leftVal`, `rightVal` | The values of the gates before gate `i`, and the values of the left and right inputs of gate `i` at `x`. |
| `Circuit.IsRun C x z` | `z : Fin m → Bool` satisfies every gate equation of `C` at `x`. |
| `AffMap n' n` | Affine map `𝔽₂^{n'} → 𝔽₂^n` given by a matrix `mat : Fin n → Fin n' → Bool` and an offset `off : Fin n → Bool`. `AffMap.apply A x' t = off t ⊕ ⟨mat t, x'⟩`. |
| `AffFun n` | Affine function of the inputs, `x ↦ const ⊕ ⟨coef, x⟩` (`AffFun.eval`). |
| `MCle f m` | `∃ C : Circuit n m, ∀ x, C.eval x = f x`: some circuit with exactly `m` AND gates computes `f`. |
| `MCleOn S f m` | `∃ C : Circuit n m, ∀ x, S x → C.eval x = f x`, the same agreement but only on the predicate `S`. |
| `Circuit.elim C i L` | Delete gate `i`, substituting the affine form `L` (over the inputs and gates `0, …, i−1`) for it in every later gate input and in the output. Later gates move down by one. |
| `Circuit.comp C A` | Substitute `x = A x'` into every gate input and the output. Gate coefficients are unchanged. |
| `Circuit.addOut C l` | Add the affine function `l` to the output form. |
| `Circuit.addDummy C` | Append an unused gate `0 ∧ 0`. |

Proof method. `IsRun.unique` says the gate equations have exactly one solution, `vals x`. So every correctness
proof for a constructed circuit (`elim`, `comp`, `addOut`, `addDummy`) writes down the candidate gate vector and
checks the gate equations. It never unfolds the recursion.

### Verified theorems

The table paraphrases the statements. The exact Lean statements of the headline theorems are in the block after the
table. Names in the `Circuit` namespace are written `Circuit.…`.

| Lean name (file `NPFrontier/Circuit.lean`) | Statement and explanation |
|---|---|
| `Circuit.vals_eq` | `C.vals x i = (C.leftVal x i && C.rightVal x i)`. Gate `i` is the AND of its two inputs, each evaluated on the inputs and the earlier gates. This is the defining equation of the semantics. |
| `Circuit.IsRun.unique` | `C.IsRun x z → C.IsRun x w → z = w`. *Proof:* strong induction on the gate index; gate `j` depends only on gates `< j`. With `vals_isRun` and `eval_eq_of_isRun`, this reads the output off any solution of the gate equations. |
| `Circuit.eval_elim` | If `C.vals x i = L.eval x (C.prev x i)`, then `(C.elim i L).eval x = C.eval x`. *Proof:* the gate vector of `C` with entry `i` deleted solves the gate equations of `C.elim i L` (`elim_isRun`). The key computation `AffForm.eval_subst` splits the term of gate `i` off each inner product and replaces it by `L`. |
| `Circuit.elim_affine` | `(∀ x, S x → C.vals x i = L.eval x (C.prev x i)) → ∃ C' : Circuit n m, ∀ x, S x → C'.eval x = C.eval x`, for `C : Circuit n (m+1)`. General form of (i): if gate `i` is an affine form in the inputs and the earlier gates on `S`, it can be removed. |
| `Circuit.elim_left` | `(∀ x, S x → C.leftVal x i = c) → ∃ C' : Circuit n m, ∀ x, S x → C'.eval x = C.eval x`. (i) for a constant left input. Gate `i` is then `0` (if `c = 0`) or equal to its right input (if `c = 1`). |
| `Circuit.elim_right` | The same with `C.rightVal x i = c`. |
| `Circuit.elim_xor` | `(∀ x, S x → (C.leftVal x i ^^ C.rightVal x i) = c) → ∃ C' …` (same conclusion). (i) for inputs that differ by a constant. Gate `i` equals `a ∧ (a ⊕ c)`, which is `a` if `c = 0` and `0` if `c = 1`. |
| `Circuit.eval_comp` | `(C.comp A).eval x' = C.eval (A.apply x')`. (ii), substitution. *Proof:* `AffMap.dot_apply` rewrites `⟨a, A x'⟩ = ⟨a, off⟩ ⊕ ⟨aᵀ·mat, x'⟩`, using an exchange of XOR sums (`Vec.xorSum_comm`). |
| `Circuit.exists_comp` | `∃ C' : Circuit n' m, ∀ x', C'.eval x' = C.eval (A.apply x')`, for `C : Circuit n m` and `A : AffMap n' n`. Existential form of (ii). |
| `Circuit.eval_addOut` | `(C.addOut l).eval x = (C.eval x ^^ l.eval x)`. |
| `Circuit.exists_xor_affine` | `∃ C' : Circuit n m, ∀ x, C'.eval x = (C.eval x ^^ l.eval x)`. Adding an affine function to the output is free. |
| `Circuit.eval_addDummy` | `C.addDummy.eval x = C.eval x`. An extra unused gate changes nothing. |
| `MCle.mono`, `MCleOn.mono` | `MCle f m → m ≤ m' → MCle f m'`, and the same for `MCleOn S`. Because of monotonicity, `MCle f m` says `MC(f) ≤ m`. |
| `MCle_zero_iff` | `MCle f 0 ↔ ∃ l : AffFun n, ∀ x, f x = l.eval x`. `MC(f) = 0` iff `f` is affine. |
| `MCleOn.of_elim_left` | `(C : Circuit n (m+1)) → (∀ x, S x → C.eval x = f x) → (∀ x, S x → C.leftVal x i = c) → MCleOn S f m`. Corollary of (i). A circuit witnessing `MCle f (m+1)` (say `hf : ∀ x, C.eval x = f x`) is the special case `hC := fun x _ => hf x`. |
| `MCleOn.of_elim_right`, `MCleOn.of_elim_xor` | The same for a constant right input and for `leftVal ⊕ rightVal = c`. |
| `MCle_xor_affine_iff` | `MCle (fun x => f x ^^ l.eval x) m ↔ MCle f m`. MC is invariant under adding affine functions. |
| `MCle.comp_affine` | `MCle f m → MCle (fun x' => f (A.apply x')) m`. `MC(f ∘ A) ≤ MC(f)` for every affine map `A`, not necessarily injective or surjective. |
| `MCleOn.comp_affine` | If `A` maps `S'` into `S`: `MCleOn S f m → MCleOn S' (f ∘ A) m`. |
| `MCleOn.comp_affine_of_maps_to` | If `A` maps every point into `S`: `MCleOn S f m → MCle (f ∘ A) m`. This is (F2), restriction through a parametrization. |
| `MCle_comp_section_iff` | If `A : AffMap n k` has an affine right inverse `B` (`∀ u, A.apply (B.apply u) = u`) and `μ : AffFun n`, then `MCle (fun x => h (A.apply x) ^^ μ.eval x) m ↔ MCle h m`. This is (F4) with the section given explicitly. |
| `MCle_and2`, `not_MCle_and2_zero`, `MCle_and3` | Sanity checks of the semantics. `x₀x₁` has a 1-gate circuit but no 0-gate circuit, so `MC = 1`. `x₀x₁x₂` has a 2-gate circuit whose second gate reads the first one. |

Exact statements (inside `namespace NPFrontier`; in `namespace Circuit` the binders `{n m : Nat}` come from
`variable`):

```lean
theorem Circuit.vals_eq (C : Circuit n m) (x : Fin n → Bool) (i : Fin m) :
    C.vals x i = (C.leftVal x i && C.rightVal x i)
theorem Circuit.elim_affine (C : Circuit n (m + 1)) (i : Fin (m + 1)) (S : (Fin n → Bool) → Prop)
    (L : AffForm n i.val) (h : ∀ x, S x → C.vals x i = L.eval x (C.prev x i)) :
    ∃ C' : Circuit n m, ∀ x, S x → C'.eval x = C.eval x
theorem Circuit.elim_left (C : Circuit n (m + 1)) (i : Fin (m + 1)) (S : (Fin n → Bool) → Prop) (c : Bool)
    (h : ∀ x, S x → C.leftVal x i = c) : ∃ C' : Circuit n m, ∀ x, S x → C'.eval x = C.eval x
theorem Circuit.elim_right (C : Circuit n (m + 1)) (i : Fin (m + 1)) (S : (Fin n → Bool) → Prop) (c : Bool)
    (h : ∀ x, S x → C.rightVal x i = c) : ∃ C' : Circuit n m, ∀ x, S x → C'.eval x = C.eval x
theorem Circuit.elim_xor (C : Circuit n (m + 1)) (i : Fin (m + 1)) (S : (Fin n → Bool) → Prop) (c : Bool)
    (h : ∀ x, S x → (C.leftVal x i ^^ C.rightVal x i) = c) :
    ∃ C' : Circuit n m, ∀ x, S x → C'.eval x = C.eval x
theorem Circuit.exists_comp {n' : Nat} (C : Circuit n m) (A : AffMap n' n) :
    ∃ C' : Circuit n' m, ∀ x', C'.eval x' = C.eval (A.apply x')
theorem Circuit.exists_xor_affine (C : Circuit n m) (l : AffFun n) :
    ∃ C' : Circuit n m, ∀ x, C'.eval x = (C.eval x ^^ l.eval x)
theorem MCle.mono {n m m' : Nat} {f : (Fin n → Bool) → Bool} (h : MCle f m) (hm : m ≤ m') : MCle f m'
theorem MCle_zero_iff {n : Nat} (f : (Fin n → Bool) → Bool) :
    MCle f 0 ↔ ∃ l : AffFun n, ∀ x, f x = l.eval x
theorem MCleOn.of_elim_left {n m : Nat} {S : (Fin n → Bool) → Prop} {f : (Fin n → Bool) → Bool}
    (C : Circuit n (m + 1)) (hC : ∀ x, S x → C.eval x = f x) (i : Fin (m + 1)) (c : Bool)
    (h : ∀ x, S x → C.leftVal x i = c) : MCleOn S f m
theorem MCleOn.of_elim_right {n m : Nat} {S : (Fin n → Bool) → Prop} {f : (Fin n → Bool) → Bool}
    (C : Circuit n (m + 1)) (hC : ∀ x, S x → C.eval x = f x) (i : Fin (m + 1)) (c : Bool)
    (h : ∀ x, S x → C.rightVal x i = c) : MCleOn S f m
theorem MCleOn.of_elim_xor {n m : Nat} {S : (Fin n → Bool) → Prop} {f : (Fin n → Bool) → Bool}
    (C : Circuit n (m + 1)) (hC : ∀ x, S x → C.eval x = f x) (i : Fin (m + 1)) (c : Bool)
    (h : ∀ x, S x → (C.leftVal x i ^^ C.rightVal x i) = c) : MCleOn S f m
theorem MCle_xor_affine_iff {n m : Nat} (f : (Fin n → Bool) → Bool) (l : AffFun n) :
    MCle (fun x => f x ^^ l.eval x) m ↔ MCle f m
theorem MCle.comp_affine {n' n m : Nat} {f : (Fin n → Bool) → Bool} (A : AffMap n' n) (h : MCle f m) :
    MCle (fun x' => f (A.apply x')) m
theorem MCleOn.comp_affine_of_maps_to {n' n m : Nat} {S : (Fin n → Bool) → Prop} {f : (Fin n → Bool) → Bool}
    (A : AffMap n' n) (hA : ∀ x', S (A.apply x')) (h : MCleOn S f m) : MCle (fun x' => f (A.apply x')) m
theorem MCle_comp_section_iff {n k m : Nat} (h : (Fin k → Bool) → Bool) (A : AffMap n k) (B : AffMap k n)
    (hAB : ∀ u, A.apply (B.apply u) = u) (μ : AffFun n) :
    MCle (fun x => h (A.apply x) ^^ μ.eval x) m ↔ MCle h m
```

A throwaway cross-check, not part of the build, also compared `Circuit.eval` with an independent Python evaluator of
XOR-AND circuits. It used 300 random circuits with `n ≤ 5` and `m ≤ 5`, which have 180 distinct truth tables, and
found no disagreement.

### Axioms (`#print axioms`, from `lake build --wfail`, 2026-11-25)

Every theorem depends only on standard axioms. There is no `sorryAx`, no `native_decide` axiom, and no axiom
declared in the project. The `decide` tactic is used only to check closed Bool identities with at most 7 variables,
by kernel evaluation. The other occurrences of `decide` are the function `decide : Prop → Bool`, which writes
coefficient vectors in the sanity examples.

```text
'NPFrontier.Circuit.vals_eq' depends on axioms: [propext, Quot.sound]
'NPFrontier.Circuit.IsRun.unique' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.Circuit.eval_elim' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.Circuit.elim_affine' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.Circuit.elim_left' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.Circuit.elim_right' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.Circuit.elim_xor' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.Circuit.eval_comp' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.Circuit.exists_comp' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.Circuit.eval_addOut' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.Circuit.exists_xor_affine' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.Circuit.eval_addDummy' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.MCle.mono' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.MCleOn.mono' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.MCle_zero_iff' depends on axioms: [propext]
'NPFrontier.MCleOn.of_elim_left' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.MCleOn.of_elim_right' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.MCleOn.of_elim_xor' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.MCle_xor_affine_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.MCle.comp_affine' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.MCleOn.comp_affine' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.MCleOn.comp_affine_of_maps_to' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.MCle_comp_section_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'NPFrontier.MCle_and2' depends on axioms: [propext, Quot.sound]
'NPFrontier.not_MCle_and2_zero' depends on axioms: [propext]
'NPFrontier.MCle_and3' depends on axioms: [propext, Classical.choice, Quot.sound]
```

### How the documents' uses map onto these theorems

- **Lemma 9 (cycle 001) and Lemma 9′.** The first gate is `a·b`. On the hyperplane `H = {⟨u,x⟩ = c}` with
  `u = u₁`, `u₂` or `u₁+u₂`, respectively `a`, `b` or `a ⊕ b` is constant. Take `S = H`; then
  `MCleOn.of_elim_left`, `of_elim_right` or `of_elim_xor` gives an `(m−1)`-gate circuit that agrees with `F` on `H`.
  Composing with an affine parametrization `φ` of `H` (`MCleOn.comp_affine_of_maps_to`) gives
  `MCle (F ∘ φ) (m−1)`, which is the document's `MC(F|_H) ≤ m−1`.
- **Lemma 24.**
  - In case (a), the left input of gate `i` is `w_{2i−1}`, which is constant on every coset of `K`: apply
    `elim_left` with `S` = the coset.
  - Case (b) is `elim_right`.
  - In case (c), the two inputs differ by `w_{2i−1} ⊕ w_{2i}`, which is constant on every coset: apply `elim_xor`.
- **(F1)/(F2)/(F4).** These are `MCle_xor_affine_iff`, `MCle.comp_affine` / `MCleOn.comp_affine_of_maps_to`, and
  `MCle_comp_section_iff`.

### Gaps: what is NOT formalized

- **MC itself is not defined.** Only `MCle f m` ("an `m`-gate circuit exists") is defined. Its reading as
  `MC(f) ≤ m` uses `MCle.mono`. The fact that every `f` has some circuit, so that `MC(f)` is finite, is not proved.
  No formal statement here needs it.
- **Affine subspaces, hyperplanes and their parametrizations are not formalized.** A set `S` is an arbitrary
  predicate, and restriction to a subspace is expressed as `f ∘ A` for an `AffMap` `A` that maps into it.
  - The existence of an affine bijection `𝔽₂^{n−1} → {⟨u,x⟩ = c}` is not proved.
  - The invariance of `MC(f|_V)` under the choice of parametrization is not proved. It follows from
    `MCle.comp_affine` once two parametrizations are known to differ by an affine bijection, but that fact is not
    formalized.
- **(F4) assumes an explicit affine section.** The document assumes only that `A` is surjective onto `C`. Every
  affine surjection over 𝔽₂ has an affine section, but that linear-algebra fact (Gaussian elimination) is not
  formalized.
- **The following results are not formalized:**
  - from `PNE-001-level4.md`: the reformulation Lemma 23 itself, the formal-circuit and coset setting of Lemma 24
    (only its gate-elimination step is formalized), Lemmas 18, 19, 20, 22, 26, 28 and 30 (with (IF′)), Corollaries 21, 29 and 31, and
    Theorems 25 and 27;
  - the enumerations behind Theorem 25 (EXP-014, EXP-015), which remain computer-assisted and outside Lean;
  - from cycle 001: Lemma 1 (`D ≤ MC`), Theorem 4 and the restriction depth `D`.
- **Lemma 24 needs one more step.** "`w_t` vanishes on `K`" has to be turned into "the form is constant on a coset
  of `K`" before Lemma 24 becomes a formal instance of `elim_left`/`elim_xor`. This step is elementary but not
  formalized.
