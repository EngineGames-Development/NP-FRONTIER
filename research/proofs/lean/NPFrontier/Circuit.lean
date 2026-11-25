/-!
# XOR-AND circuits: gate elimination and affine substitution

Circuits over the basis `{AND, XOR, 1}`, and the two facts about them that the PNE-001 proof documents use
(Lemma 9 of cycle 001; Lemmas 9′, 23, 24 and fact (F4) of `PNE-001-level4.md`):

* **(i) gate elimination** (`Circuit.elim_left`, `Circuit.elim_right`, `Circuit.elim_xor`). If, on a set `S` of
  inputs, one input of gate `i` is constant, or the two inputs of gate `i` differ by a constant, then some circuit
  with one AND gate fewer computes the same output on `S`.
* **(ii) affine substitution** (`Circuit.exists_comp`, `Circuit.exists_xor_affine`). Composing a circuit with an
  affine map of the inputs keeps the number of AND gates, and adding an affine function to the output is free.
* The same facts for `MCle f m` ("some circuit with `m` AND gates computes `f`", which by `MCle.mono` is
  `MC(f) ≤ m`) and its relativization `MCleOn S f m`.

## Representation (chosen so that every proof is a structural induction)

* Bit vectors are functions `Fin k → Bool`. `Vec.xorSum v = v 0 ⊕ ⋯ ⊕ v (k-1)` is defined by recursion on `k`,
  peeling off the last entry; the empty sum is `false`. `Vec.dot a v = ⊕ⱼ (a j ∧ v j)` is the inner product over
  `𝔽₂`.
* `AffForm n k` is an affine form over `n` inputs and `k` gates: a constant bit `const`, input coefficients
  `inp : Fin n → Bool` and gate coefficients `gat : Fin k → Bool`.
  `AffForm.eval L x z = const ⊕ ⟨inp, x⟩ ⊕ ⟨gat, z⟩`.
* `Circuit n m` has, for each gate `i : Fin m`, a left and a right input form `left i, right i : AffForm n i`
  (over the inputs and the `i` earlier gates), and an output form `out : AffForm n m`.
* `Circuit.vals C x i` is the value of gate `i` at input `x`, defined by well-founded recursion on `i`: gate `i`
  is `left i` AND `right i`, both evaluated at `x` and at the values of gates `0, …, i-1` (`Circuit.vals_eq`).
  `Circuit.eval C x = out.eval x (vals x)`.
* `Circuit.IsRun C x z` says that the vector `z` satisfies all gate equations at `x`. Its only solution is
  `vals x` (`Circuit.IsRun.unique`). Every correctness proof below exhibits the gate vector of the new circuit as
  an explicit run.
* `AffMap n' n` is an affine map `𝔽₂^{n'} → 𝔽₂^n`, given by a coefficient matrix `mat` and an offset `off`.
  `AffFun n` is an affine function `x ↦ const ⊕ ⟨coef, x⟩` of the inputs.
-/

namespace NPFrontier

/-! ## Bit vectors and XOR sums -/

namespace Vec

/-- `xorSum v = v 0 ⊕ v 1 ⊕ ⋯ ⊕ v (k-1)` (a sum over `𝔽₂`); the empty sum is `false`. -/
def xorSum : {k : Nat} → (Fin k → Bool) → Bool
  | 0, _ => false
  | k + 1, f => xorSum (fun j : Fin k => f ⟨j.val, Nat.lt_succ_of_lt j.isLt⟩) ^^ f ⟨k, Nat.lt_succ_self k⟩

/-- Inner product over `𝔽₂`: `dot a v = ⊕ⱼ (a j ∧ v j)`. -/
def dot {k : Nat} (a v : Fin k → Bool) : Bool := xorSum (fun j => a j && v j)

/-- The first `i` coordinates of `v`. -/
def take {k : Nat} (i : Nat) (h : i ≤ k) (v : Fin k → Bool) : Fin i → Bool :=
  fun j => v ⟨j.val, Nat.lt_of_lt_of_le j.isLt h⟩

/-- Extension of `v` by zeros from `i` to `k` coordinates. -/
def pad {i : Nat} (k : Nat) (v : Fin i → Bool) : Fin k → Bool :=
  fun j => if h : j.val < i then v ⟨j.val, h⟩ else false

/-- Delete coordinate `i` of `v`; the later coordinates move down by one. -/
def removeAt {k : Nat} (i : Nat) (v : Fin (k + 1) → Bool) : Fin k → Bool :=
  fun j => if j.val < i then v ⟨j.val, Nat.lt_succ_of_lt j.isLt⟩ else v ⟨j.val + 1, Nat.succ_lt_succ j.isLt⟩

theorem xorSum_succ {k : Nat} (f : Fin (k + 1) → Bool) :
    xorSum f = (xorSum (fun j : Fin k => f ⟨j.val, Nat.lt_succ_of_lt j.isLt⟩) ^^ f ⟨k, Nat.lt_succ_self k⟩) :=
  rfl

theorem xorSum_false : {k : Nat} → xorSum (fun _ : Fin k => false) = false
  | 0 => rfl
  | k + 1 => by rw [xorSum_succ, xorSum_false (k := k)]; rfl

/-- `xorSum` is additive. -/
theorem xorSum_xor : {k : Nat} → (f g : Fin k → Bool) →
    xorSum (fun j => f j ^^ g j) = (xorSum f ^^ xorSum g)
  | 0, _, _ => rfl
  | k + 1, f, g => by
      rw [xorSum_succ, xorSum_succ f, xorSum_succ g, xorSum_xor]
      generalize xorSum _ = a
      generalize xorSum _ = b
      generalize f _ = c
      generalize g _ = d
      cases a <;> cases b <;> cases c <;> cases d <;> rfl

theorem and_xorSum (b : Bool) : {k : Nat} → (f : Fin k → Bool) →
    (b && xorSum f) = xorSum (fun j => b && f j)
  | 0, _ => Bool.and_false b
  | k + 1, f => by
      rw [xorSum_succ, xorSum_succ (fun j => b && f j), Bool.and_xor_distrib_left, and_xorSum b]

theorem xorSum_and (b : Bool) {k : Nat} (f : Fin k → Bool) :
    (xorSum f && b) = xorSum (fun j => f j && b) := by
  rw [Bool.and_comm, and_xorSum]
  congr 1; funext j; exact Bool.and_comm _ _

/-- Exchange of the order of summation in a double XOR sum. -/
theorem xorSum_comm : {p q : Nat} → (F : Fin p → Fin q → Bool) →
    xorSum (fun i => xorSum (fun j => F i j)) = xorSum (fun j => xorSum (fun i => F i j))
  | 0, _, _ => xorSum_false.symm
  | p + 1, q, F => by
      rw [xorSum_succ, xorSum_comm (fun (i : Fin p) j => F ⟨i.val, Nat.lt_succ_of_lt i.isLt⟩ j), ← xorSum_xor]
      rfl

/-- Splitting one term `f i` off an XOR sum. -/
theorem xorSum_removeAt : {k : Nat} → (i : Nat) → (hi : i < k + 1) → (f : Fin (k + 1) → Bool) →
    xorSum f = (f ⟨i, hi⟩ ^^ xorSum (removeAt i f))
  | 0, i, hi, f => by
      obtain rfl : i = 0 := by omega
      rw [xorSum_succ]
      show (false ^^ f ⟨0, hi⟩) = (f ⟨0, hi⟩ ^^ false)
      rw [Bool.false_xor, Bool.xor_false]
  | k + 1, i, hi, f => by
      by_cases h : i = k + 1
      · subst h
        have hr : removeAt (k + 1) f = fun j : Fin (k + 1) => f ⟨j.val, Nat.lt_succ_of_lt j.isLt⟩ := by
          funext j; simp [removeAt, j.isLt]
        rw [hr, xorSum_succ f, Bool.xor_comm]
      · have hi' : i < k + 1 := by omega
        rw [xorSum_succ f, xorSum_removeAt i hi', xorSum_succ (removeAt i f)]
        have hlast : removeAt i f ⟨k, Nat.lt_succ_self k⟩ = f ⟨k + 1, Nat.lt_succ_self (k + 1)⟩ := by
          simp [removeAt, show ¬ k < i by omega]
        rw [hlast, Bool.xor_assoc]
        rfl

theorem removeAt_and {k : Nat} (i : Nat) (a v : Fin (k + 1) → Bool) :
    removeAt i (fun j => a j && v j) = fun j => removeAt i a j && removeAt i v j := by
  funext j
  by_cases h : j.val < i <;> simp [removeAt, h]

/-- Splitting coordinate `i` off an inner product. -/
theorem dot_removeAt {k : Nat} (i : Nat) (hi : i < k + 1) (a v : Fin (k + 1) → Bool) :
    dot a v = ((a ⟨i, hi⟩ && v ⟨i, hi⟩) ^^ dot (removeAt i a) (removeAt i v)) := by
  unfold dot
  rw [xorSum_removeAt i hi, removeAt_and]

theorem xorSum_take_of_zero : {k : Nat} → (i : Nat) → (h : i ≤ k) → (f : Fin k → Bool) →
    (∀ j : Fin k, i ≤ j.val → f j = false) → xorSum f = xorSum (take i h f)
  | 0, i, h, f, _ => by
      obtain rfl : i = 0 := by omega
      rfl
  | k + 1, i, h, f, hz => by
      by_cases hik : i = k + 1
      · subst hik; rfl
      · have hik' : i ≤ k := by omega
        rw [xorSum_succ f, hz ⟨k, Nat.lt_succ_self k⟩ hik', Bool.xor_false,
          xorSum_take_of_zero i hik' _ (fun j hj => hz _ hj)]
        rfl

/-- A zero-padded coefficient vector only sees the first `i` coordinates. -/
theorem dot_pad {i k : Nat} (h : i ≤ k) (a : Fin i → Bool) (v : Fin k → Bool) :
    dot (pad k a) v = dot a (take i h v) := by
  unfold dot
  rw [xorSum_take_of_zero i h]
  · congr 1; funext j; simp [take, pad, j.isLt]
  · intro j hj; simp [pad, show ¬ j.val < i by omega]

theorem dot_xor_left {k : Nat} (a b v : Fin k → Bool) :
    dot (fun j => a j ^^ b j) v = (dot a v ^^ dot b v) := by
  unfold dot; rw [← xorSum_xor]; congr 1; funext j; exact Bool.and_xor_distrib_right _ _ _

theorem dot_and_left {k : Nat} (c : Bool) (a v : Fin k → Bool) :
    dot (fun j => c && a j) v = (c && dot a v) := by
  unfold dot; rw [and_xorSum]; congr 1; funext j; exact Bool.and_assoc _ _ _

theorem dot_zero_left {k : Nat} (v : Fin k → Bool) : dot (fun _ => false) v = false := by
  unfold dot; simp only [Bool.false_and]; exact xorSum_false

theorem dot_zero_length (a v : Fin 0 → Bool) : dot a v = false := rfl

end Vec

open Vec

/-! ## Affine forms over the inputs and the earlier gates -/

/-- An affine form over `n` inputs and `k` gates: `const ⊕ ⟨inp, x⟩ ⊕ ⟨gat, z⟩`. -/
structure AffForm (n k : Nat) where
  /-- The constant term. -/
  const : Bool
  /-- Coefficients on the inputs `x 0, …, x (n-1)`. -/
  inp : Fin n → Bool
  /-- Coefficients on the gates `z 0, …, z (k-1)`. -/
  gat : Fin k → Bool

namespace AffForm

/-- Value of the form at inputs `x` and gate values `z`. -/
def eval {n k : Nat} (L : AffForm n k) (x : Fin n → Bool) (z : Fin k → Bool) : Bool :=
  (L.const ^^ dot L.inp x) ^^ dot L.gat z

/-- The zero form. -/
def zero (n k : Nat) : AffForm n k := ⟨false, fun _ => false, fun _ => false⟩

theorem eval_zero {n k : Nat} (x : Fin n → Bool) (z : Fin k → Bool) : (zero n k).eval x z = false := by
  simp only [eval, zero, dot_zero_left]; rfl

/-- Substitute the affine form `L` (over the inputs and gates `0, …, i-1`) for gate `i` in `F`, and delete gate
`i`; gates after `i` move down by one. -/
def subst {n k : Nat} (F : AffForm n (k + 1)) (i : Nat) (hi : i ≤ k) (L : AffForm n i) : AffForm n k :=
  { const := F.const ^^ (F.gat ⟨i, Nat.lt_succ_of_le hi⟩ && L.const)
    inp := fun t => F.inp t ^^ (F.gat ⟨i, Nat.lt_succ_of_le hi⟩ && L.inp t)
    gat := fun j => removeAt i F.gat j ^^ (F.gat ⟨i, Nat.lt_succ_of_le hi⟩ && pad k L.gat j) }

theorem take_removeAt {k : Nat} (i : Nat) (hi : i ≤ k) (z : Fin (k + 1) → Bool) :
    take i hi (removeAt i z) = take i (Nat.le_succ_of_le hi) z := by
  funext j; simp [take, removeAt, j.isLt]

private theorem subst_bool (Fc Fx b Lc Lx Lz R : Bool) :
    (((Fc ^^ (b && Lc)) ^^ (Fx ^^ (b && Lx))) ^^ (R ^^ (b && Lz))) =
      ((Fc ^^ Fx) ^^ ((b && ((Lc ^^ Lx) ^^ Lz)) ^^ R)) := by
  revert Fc Fx b Lc Lx Lz R; decide

/-- Correctness of substitution: if gate `i` of `z` equals `L` at the earlier gates, then the substituted form
evaluated without gate `i` equals the original form. -/
theorem eval_subst {n k : Nat} (F : AffForm n (k + 1)) (i : Nat) (hi : i ≤ k) (L : AffForm n i)
    (x : Fin n → Bool) (z : Fin (k + 1) → Bool)
    (hz : z ⟨i, Nat.lt_succ_of_le hi⟩ = L.eval x (take i (Nat.le_succ_of_le hi) z)) :
    (F.subst i hi L).eval x (removeAt i z) = F.eval x z := by
  simp only [eval, subst]
  rw [dot_xor_left, dot_and_left, dot_xor_left, dot_and_left, dot_pad hi, take_removeAt,
    dot_removeAt i (Nat.lt_succ_of_le hi) F.gat z, hz]
  exact subst_bool _ _ _ _ _ _ _

end AffForm

/-! ## Circuits and their evaluation -/

/-- An XOR-AND circuit with `n` inputs and `m` AND gates. Gate `i` computes `left i ∧ right i`, where both are
affine forms over the inputs and the `i` earlier gates; the output is an affine form over the inputs and all
`m` gates. -/
structure Circuit (n m : Nat) where
  /-- Left input of gate `i`. -/
  left : (i : Fin m) → AffForm n i.val
  /-- Right input of gate `i`. -/
  right : (i : Fin m) → AffForm n i.val
  /-- The output form. -/
  out : AffForm n m

namespace Circuit

variable {n m : Nat}

/-- Value of gate `i` at input `x`, computed from the values of the earlier gates. -/
def vals (C : Circuit n m) (x : Fin n → Bool) (i : Fin m) : Bool :=
  (C.left i).eval x (fun j => C.vals x ⟨j.val, Nat.lt_trans j.isLt i.isLt⟩) &&
  (C.right i).eval x (fun j => C.vals x ⟨j.val, Nat.lt_trans j.isLt i.isLt⟩)
termination_by i.val

/-- The function computed by the circuit. -/
def eval (C : Circuit n m) (x : Fin n → Bool) : Bool := C.out.eval x (C.vals x)

/-- Values of the gates before gate `i`. -/
def prev (C : Circuit n m) (x : Fin n → Bool) (i : Fin m) : Fin i.val → Bool :=
  take i.val (Nat.le_of_lt i.isLt) (C.vals x)

/-- Value of the left input of gate `i` at `x`. -/
def leftVal (C : Circuit n m) (x : Fin n → Bool) (i : Fin m) : Bool := (C.left i).eval x (C.prev x i)

/-- Value of the right input of gate `i` at `x`. -/
def rightVal (C : Circuit n m) (x : Fin n → Bool) (i : Fin m) : Bool := (C.right i).eval x (C.prev x i)

/-- Gate `i` is the AND of its two inputs. -/
theorem vals_eq (C : Circuit n m) (x : Fin n → Bool) (i : Fin m) :
    C.vals x i = (C.leftVal x i && C.rightVal x i) := by
  rw [vals]; rfl

/-- `z` satisfies the gate equations of `C` at input `x`. -/
def IsRun (C : Circuit n m) (x : Fin n → Bool) (z : Fin m → Bool) : Prop :=
  ∀ i : Fin m, z i = ((C.left i).eval x (take i.val (Nat.le_of_lt i.isLt) z) &&
    (C.right i).eval x (take i.val (Nat.le_of_lt i.isLt) z))

theorem vals_isRun (C : Circuit n m) (x : Fin n → Bool) : C.IsRun x (C.vals x) :=
  fun i => C.vals_eq x i

/-- The gate equations have at most one solution (induction on the gate index). -/
theorem IsRun.unique {C : Circuit n m} {x : Fin n → Bool} {z w : Fin m → Bool}
    (hz : C.IsRun x z) (hw : C.IsRun x w) : z = w := by
  have key : ∀ t : Nat, ∀ j : Fin m, j.val < t → z j = w j := by
    intro t
    induction t with
    | zero => intro j hj; exact absurd hj (Nat.not_lt_zero _)
    | succ t ih =>
      intro j hj
      have htake : take j.val (Nat.le_of_lt j.isLt) z = take j.val (Nat.le_of_lt j.isLt) w := by
        funext s
        exact ih ⟨s.val, Nat.lt_trans s.isLt j.isLt⟩ (by have := s.isLt; simp only; omega)
      rw [hz j, hw j, htake]
  funext j
  exact key (j.val + 1) j (Nat.lt_succ_self _)

/-- The output can be read off any solution of the gate equations. -/
theorem eval_eq_of_isRun {C : Circuit n m} {x : Fin n → Bool} {z : Fin m → Bool} (hz : C.IsRun x z) :
    C.eval x = C.out.eval x z := by
  unfold eval; rw [(C.vals_isRun x).unique hz]

/-! ## Gate elimination -/

/-- Delete gate `i` of `C`, substituting the affine form `L` (over the inputs and gates `0, …, i-1`) for it in
every later gate input and in the output. -/
def elim (C : Circuit n (m + 1)) (i : Fin (m + 1)) (L : AffForm n i.val) : Circuit n m where
  left j := if h : j.val < i.val then C.left ⟨j.val, Nat.lt_succ_of_lt j.isLt⟩
    else (C.left ⟨j.val + 1, Nat.succ_lt_succ j.isLt⟩).subst i.val (by omega) L
  right j := if h : j.val < i.val then C.right ⟨j.val, Nat.lt_succ_of_lt j.isLt⟩
    else (C.right ⟨j.val + 1, Nat.succ_lt_succ j.isLt⟩).subst i.val (by omega) L
  out := C.out.subst i.val (Nat.le_of_lt_succ i.isLt) L

/-- If gate `i` equals `L` at `x`, the gate values of `C` with entry `i` deleted solve the gate equations of
`C.elim i L` at `x`. -/
theorem elim_isRun (C : Circuit n (m + 1)) (i : Fin (m + 1)) (L : AffForm n i.val) (x : Fin n → Bool)
    (hL : C.vals x i = L.eval x (C.prev x i)) :
    (C.elim i L).IsRun x (removeAt i.val (C.vals x)) := by
  intro j
  by_cases h : j.val < i.val
  · have h1 : removeAt i.val (C.vals x) j = C.vals x ⟨j.val, Nat.lt_succ_of_lt j.isLt⟩ := by
      simp [removeAt, h]
    have h2 : take j.val (Nat.le_of_lt j.isLt) (removeAt i.val (C.vals x)) =
        take j.val (Nat.le_of_lt (Nat.lt_succ_of_lt j.isLt)) (C.vals x) := by
      funext s; simp [take, removeAt, show s.val < i.val by have := s.isLt; omega]
    simp only [elim, h, ↓reduceDIte]
    rw [h1, h2]
    exact C.vals_isRun x ⟨j.val, Nat.lt_succ_of_lt j.isLt⟩
  · have h1 : removeAt i.val (C.vals x) j = C.vals x ⟨j.val + 1, Nat.succ_lt_succ j.isLt⟩ := by
      simp [removeAt, h]
    have h2 : take j.val (Nat.le_of_lt j.isLt) (removeAt i.val (C.vals x)) =
        removeAt i.val (take (j.val + 1) (Nat.succ_le_succ (Nat.le_of_lt j.isLt)) (C.vals x)) := by
      funext s; simp [take, removeAt]
    have hi : i.val ≤ j.val := by omega
    have hw : take (j.val + 1) (Nat.succ_le_succ (Nat.le_of_lt j.isLt)) (C.vals x) ⟨i.val, Nat.lt_succ_of_le hi⟩ =
        L.eval x (take i.val (Nat.le_succ_of_le hi)
          (take (j.val + 1) (Nat.succ_le_succ (Nat.le_of_lt j.isLt)) (C.vals x))) := hL
    simp only [elim, h, ↓reduceDIte]
    rw [h1, h2, AffForm.eval_subst _ _ hi _ x _ hw, AffForm.eval_subst _ _ hi _ x _ hw]
    exact C.vals_isRun x ⟨j.val + 1, Nat.succ_lt_succ j.isLt⟩

/-- If gate `i` equals `L` at `x`, deleting it does not change the output at `x`. -/
theorem eval_elim (C : Circuit n (m + 1)) (i : Fin (m + 1)) (L : AffForm n i.val) (x : Fin n → Bool)
    (hL : C.vals x i = L.eval x (C.prev x i)) : (C.elim i L).eval x = C.eval x := by
  rw [eval_eq_of_isRun (C.elim_isRun i L x hL)]
  exact AffForm.eval_subst C.out i.val (Nat.le_of_lt_succ i.isLt) L x (C.vals x) hL

/-- **Gate elimination, general form.** If on `S` gate `i` equals an affine form `L` in the inputs and the
earlier gates, some circuit with one gate fewer agrees with `C` on `S`. -/
theorem elim_affine (C : Circuit n (m + 1)) (i : Fin (m + 1)) (S : (Fin n → Bool) → Prop)
    (L : AffForm n i.val) (h : ∀ x, S x → C.vals x i = L.eval x (C.prev x i)) :
    ∃ C' : Circuit n m, ∀ x, S x → C'.eval x = C.eval x :=
  ⟨C.elim i L, fun x hx => C.eval_elim i L x (h x hx)⟩

/-- **Gate elimination, constant left input.** If the left input of gate `i` equals the constant `c` at every
`x ∈ S`, some circuit with one gate fewer agrees with `C` on `S`. -/
theorem elim_left (C : Circuit n (m + 1)) (i : Fin (m + 1)) (S : (Fin n → Bool) → Prop) (c : Bool)
    (h : ∀ x, S x → C.leftVal x i = c) :
    ∃ C' : Circuit n m, ∀ x, S x → C'.eval x = C.eval x := by
  cases c
  · refine C.elim_affine i S (AffForm.zero n i.val) (fun x hx => ?_)
    rw [vals_eq, h x hx, AffForm.eval_zero, Bool.false_and]
  · refine C.elim_affine i S (C.right i) (fun x hx => ?_)
    rw [vals_eq, h x hx, Bool.true_and]; rfl

/-- **Gate elimination, constant right input.** -/
theorem elim_right (C : Circuit n (m + 1)) (i : Fin (m + 1)) (S : (Fin n → Bool) → Prop) (c : Bool)
    (h : ∀ x, S x → C.rightVal x i = c) :
    ∃ C' : Circuit n m, ∀ x, S x → C'.eval x = C.eval x := by
  cases c
  · refine C.elim_affine i S (AffForm.zero n i.val) (fun x hx => ?_)
    rw [vals_eq, h x hx, AffForm.eval_zero, Bool.and_false]
  · refine C.elim_affine i S (C.left i) (fun x hx => ?_)
    rw [vals_eq, h x hx, Bool.and_true]; rfl

/-- **Gate elimination, inputs differing by a constant.** If `left ⊕ right` of gate `i` equals the constant `c` at
every `x ∈ S`, some circuit with one gate fewer agrees with `C` on `S`. (Then gate `i` is `left` if `c = 0` and
`0` if `c = 1`.) -/
theorem elim_xor (C : Circuit n (m + 1)) (i : Fin (m + 1)) (S : (Fin n → Bool) → Prop) (c : Bool)
    (h : ∀ x, S x → (C.leftVal x i ^^ C.rightVal x i) = c) :
    ∃ C' : Circuit n m, ∀ x, S x → C'.eval x = C.eval x := by
  cases c
  · refine C.elim_affine i S (C.left i) (fun x hx => ?_)
    have hx' := h x hx
    rw [vals_eq]
    show (C.leftVal x i && C.rightVal x i) = C.leftVal x i
    revert hx'
    cases C.leftVal x i <;> cases C.rightVal x i <;> decide
  · refine C.elim_affine i S (AffForm.zero n i.val) (fun x hx => ?_)
    have hx' := h x hx
    rw [vals_eq, AffForm.eval_zero]
    revert hx'
    cases C.leftVal x i <;> cases C.rightVal x i <;> decide

end Circuit

/-! ## Affine maps of the inputs and affine output functions -/

/-- An affine map `𝔽₂^{n'} → 𝔽₂^n`: output coordinate `t` is `off t ⊕ ⟨mat t, x'⟩`. -/
structure AffMap (n' n : Nat) where
  /-- Coefficient matrix: row `t` gives output coordinate `t`. -/
  mat : Fin n → Fin n' → Bool
  /-- Offset vector. -/
  off : Fin n → Bool

/-- Apply the affine map. -/
def AffMap.apply {n' n : Nat} (A : AffMap n' n) (x' : Fin n' → Bool) : Fin n → Bool :=
  fun t => A.off t ^^ dot (A.mat t) x'

/-- Coefficients on `x'` of the linear form `x' ↦ ⟨a, mat · x'⟩` (the row vector `aᵀ · mat`). -/
def AffMap.pullback {n' n : Nat} (A : AffMap n' n) (a : Fin n → Bool) : Fin n' → Bool :=
  fun s => xorSum (fun t => a t && A.mat t s)

theorem AffMap.dot_apply {n' n : Nat} (A : AffMap n' n) (a : Fin n → Bool) (x' : Fin n' → Bool) :
    dot a (A.apply x') = (dot a A.off ^^ dot (A.pullback a) x') := by
  unfold AffMap.apply AffMap.pullback dot
  have h1 : (fun t => a t && (A.off t ^^ xorSum (fun s => A.mat t s && x' s))) =
      fun t => (a t && A.off t) ^^ xorSum (fun s => a t && (A.mat t s && x' s)) := by
    funext t; rw [Bool.and_xor_distrib_left, and_xorSum]
  rw [h1, xorSum_xor, xorSum_comm]
  congr 1; congr 1; funext s
  rw [xorSum_and]; congr 1; funext t; exact (Bool.and_assoc _ _ _).symm

/-- An affine function of `n` inputs: `x ↦ const ⊕ ⟨coef, x⟩`. -/
structure AffFun (n : Nat) where
  /-- The constant term. -/
  const : Bool
  /-- The linear coefficients. -/
  coef : Fin n → Bool

/-- Value of the affine function at `x`. -/
def AffFun.eval {n : Nat} (l : AffFun n) (x : Fin n → Bool) : Bool := l.const ^^ dot l.coef x

/-- `l ∘ A` as an affine function. -/
def AffFun.comp {n' n : Nat} (l : AffFun n) (A : AffMap n' n) : AffFun n' :=
  ⟨l.const ^^ dot l.coef A.off, A.pullback l.coef⟩

theorem AffFun.eval_comp {n' n : Nat} (l : AffFun n) (A : AffMap n' n) (x' : Fin n' → Bool) :
    (l.comp A).eval x' = l.eval (A.apply x') := by
  simp only [AffFun.eval, AffFun.comp, A.dot_apply, Bool.xor_assoc]

/-- Substitute `x = A x'` into an affine form; the gate coefficients are unchanged. -/
def AffForm.comp {n' n k : Nat} (L : AffForm n k) (A : AffMap n' n) : AffForm n' k :=
  ⟨L.const ^^ dot L.inp A.off, A.pullback L.inp, L.gat⟩

theorem AffForm.eval_comp {n' n k : Nat} (L : AffForm n k) (A : AffMap n' n) (x' : Fin n' → Bool)
    (z : Fin k → Bool) : (L.comp A).eval x' z = L.eval (A.apply x') z := by
  simp only [AffForm.eval, AffForm.comp, A.dot_apply, Bool.xor_assoc]

namespace Circuit

variable {n m : Nat}

/-- Substitute `x = A x'` into every gate input and the output. -/
def comp {n' : Nat} (C : Circuit n m) (A : AffMap n' n) : Circuit n' m where
  left i := (C.left i).comp A
  right i := (C.right i).comp A
  out := C.out.comp A

/-- **Affine substitution.** `C.comp A` computes `x' ↦ C (A x')` with the same `m` AND gates. -/
theorem eval_comp {n' : Nat} (C : Circuit n m) (A : AffMap n' n) (x' : Fin n' → Bool) :
    (C.comp A).eval x' = C.eval (A.apply x') := by
  have hrun : (C.comp A).IsRun x' (C.vals (A.apply x')) := by
    intro i
    simp only [comp, AffForm.eval_comp]
    exact C.vals_isRun (A.apply x') i
  rw [eval_eq_of_isRun hrun]
  exact AffForm.eval_comp _ _ _ _

/-- **Affine substitution (existential form).** -/
theorem exists_comp {n' : Nat} (C : Circuit n m) (A : AffMap n' n) :
    ∃ C' : Circuit n' m, ∀ x', C'.eval x' = C.eval (A.apply x') :=
  ⟨C.comp A, C.eval_comp A⟩

/-- Add the affine function `l` to the output. -/
def addOut (C : Circuit n m) (l : AffFun n) : Circuit n m where
  left := C.left
  right := C.right
  out := ⟨C.out.const ^^ l.const, fun t => C.out.inp t ^^ l.coef t, C.out.gat⟩

private theorem addOut_bool (a b c d e : Bool) :
    (((a ^^ b) ^^ (c ^^ d)) ^^ e) = (((a ^^ c) ^^ e) ^^ (b ^^ d)) := by
  revert a b c d e; decide

/-- **Adding an affine function to the output is free.** -/
theorem eval_addOut (C : Circuit n m) (l : AffFun n) (x : Fin n → Bool) :
    (C.addOut l).eval x = (C.eval x ^^ l.eval x) := by
  have hrun : (C.addOut l).IsRun x (C.vals x) := C.vals_isRun x
  rw [eval_eq_of_isRun hrun]
  simp only [addOut, AffForm.eval, AffFun.eval, eval, dot_xor_left]
  exact addOut_bool _ _ _ _ _

/-- **Adding an affine function to the output is free (existential form).** -/
theorem exists_xor_affine (C : Circuit n m) (l : AffFun n) :
    ∃ C' : Circuit n m, ∀ x, C'.eval x = (C.eval x ^^ l.eval x) :=
  ⟨C.addOut l, C.eval_addOut l⟩

/-- Append an unused gate `0 ∧ 0`. -/
def addDummy (C : Circuit n m) : Circuit n (m + 1) where
  left j := if h : j.val < m then C.left ⟨j.val, h⟩ else AffForm.zero n j.val
  right j := if h : j.val < m then C.right ⟨j.val, h⟩ else AffForm.zero n j.val
  out := ⟨C.out.const, C.out.inp, pad (m + 1) C.out.gat⟩

theorem eval_addDummy (C : Circuit n m) (x : Fin n → Bool) : C.addDummy.eval x = C.eval x := by
  have hrun : C.addDummy.IsRun x (pad (m + 1) (C.vals x)) := by
    intro j
    by_cases h : j.val < m
    · have h1 : pad (m + 1) (C.vals x) j = C.vals x ⟨j.val, h⟩ := by simp [pad, h]
      have h2 : take j.val (Nat.le_of_lt j.isLt) (pad (m + 1) (C.vals x)) =
          take j.val (Nat.le_of_lt h) (C.vals x) := by
        funext s; simp [take, pad, show s.val < m by have := s.isLt; omega]
      simp only [addDummy, h, ↓reduceDIte]
      rw [h1, h2]
      exact C.vals_isRun x ⟨j.val, h⟩
    · simp only [addDummy, h, ↓reduceDIte, AffForm.eval_zero, Bool.false_and]
      simp [pad, h]
  rw [eval_eq_of_isRun hrun]
  simp only [addDummy, AffForm.eval, eval]
  rw [dot_pad (Nat.le_succ m)]
  have h3 : take m (Nat.le_succ m) (pad (m + 1) (C.vals x)) = C.vals x := by
    funext s; simp [take, pad, s.isLt]
  rw [h3]

end Circuit

/-! ## Multiplicative complexity -/

/-- `MCle f m`: some circuit with exactly `m` AND gates computes `f` at every input. By `MCle.mono` this is
upward closed in `m`, so `MCle f m ↔ MC(f) ≤ m`. -/
def MCle {n : Nat} (f : (Fin n → Bool) → Bool) (m : Nat) : Prop :=
  ∃ C : Circuit n m, ∀ x, C.eval x = f x

/-- `MCleOn S f m`: some circuit with exactly `m` AND gates agrees with `f` at every input in `S`. -/
def MCleOn {n : Nat} (S : (Fin n → Bool) → Prop) (f : (Fin n → Bool) → Bool) (m : Nat) : Prop :=
  ∃ C : Circuit n m, ∀ x, S x → C.eval x = f x

theorem MCle.toOn {n m : Nat} {f : (Fin n → Bool) → Bool} (S : (Fin n → Bool) → Prop) (h : MCle f m) :
    MCleOn S f m :=
  let ⟨C, hC⟩ := h; ⟨C, fun x _ => hC x⟩

theorem MCleOn_true_iff {n m : Nat} (f : (Fin n → Bool) → Bool) :
    MCleOn (fun _ => True) f m ↔ MCle f m :=
  ⟨fun ⟨C, hC⟩ => ⟨C, fun x => hC x trivial⟩, fun h => h.toOn _⟩

theorem MCle.succ {n m : Nat} {f : (Fin n → Bool) → Bool} (h : MCle f m) : MCle f (m + 1) :=
  let ⟨C, hC⟩ := h; ⟨C.addDummy, fun x => (C.eval_addDummy x).trans (hC x)⟩

/-- `MCle` is monotone in the number of gates. -/
theorem MCle.mono {n m m' : Nat} {f : (Fin n → Bool) → Bool} (h : MCle f m) (hm : m ≤ m') : MCle f m' := by
  induction hm with
  | refl => exact h
  | step _ ih => exact ih.succ

theorem MCleOn.mono {n m m' : Nat} {S : (Fin n → Bool) → Prop} {f : (Fin n → Bool) → Bool}
    (h : MCleOn S f m) (hm : m ≤ m') : MCleOn S f m' := by
  induction hm with
  | refl => exact h
  | step _ ih =>
    obtain ⟨C, hC⟩ := ih
    exact ⟨C.addDummy, fun x hx => (C.eval_addDummy x).trans (hC x hx)⟩

/-- Circuits without AND gates compute exactly the affine functions (`MC(f) = 0` iff `f` is affine). -/
theorem MCle_zero_iff {n : Nat} (f : (Fin n → Bool) → Bool) :
    MCle f 0 ↔ ∃ l : AffFun n, ∀ x, f x = l.eval x := by
  constructor
  · rintro ⟨C, hC⟩
    refine ⟨⟨C.out.const, C.out.inp⟩, fun x => ?_⟩
    rw [← hC x]
    simp only [Circuit.eval, AffForm.eval, AffFun.eval, dot_zero_length, Bool.xor_false]
  · rintro ⟨l, hl⟩
    refine ⟨⟨fun i => i.elim0, fun i => i.elim0, ⟨l.const, l.coef, fun i => i.elim0⟩⟩, fun x => ?_⟩
    rw [hl x]
    simp only [Circuit.eval, AffForm.eval, AffFun.eval, dot_zero_length, Bool.xor_false]

/-- **Gate elimination for `MCle`, constant left input.** If `C` (with `m + 1` gates) computes `f` on `S` and the
left input of gate `i` is the constant `c` on `S`, then `f` has an `m`-gate circuit on `S`. The hypothesis `hC`
only asks for agreement on `S`; a circuit `C` witnessing `MCle f (m + 1)`, say `hf : ∀ x, C.eval x = f x`, is the
special case `hC := fun x _ => hf x`. -/
theorem MCleOn.of_elim_left {n m : Nat} {S : (Fin n → Bool) → Prop} {f : (Fin n → Bool) → Bool}
    (C : Circuit n (m + 1)) (hC : ∀ x, S x → C.eval x = f x) (i : Fin (m + 1)) (c : Bool)
    (h : ∀ x, S x → C.leftVal x i = c) : MCleOn S f m :=
  let ⟨C', hC'⟩ := C.elim_left i S c h; ⟨C', fun x hx => (hC' x hx).trans (hC x hx)⟩

/-- **Gate elimination for `MCle`, constant right input.** -/
theorem MCleOn.of_elim_right {n m : Nat} {S : (Fin n → Bool) → Prop} {f : (Fin n → Bool) → Bool}
    (C : Circuit n (m + 1)) (hC : ∀ x, S x → C.eval x = f x) (i : Fin (m + 1)) (c : Bool)
    (h : ∀ x, S x → C.rightVal x i = c) : MCleOn S f m :=
  let ⟨C', hC'⟩ := C.elim_right i S c h; ⟨C', fun x hx => (hC' x hx).trans (hC x hx)⟩

/-- **Gate elimination for `MCle`, inputs differing by a constant.** -/
theorem MCleOn.of_elim_xor {n m : Nat} {S : (Fin n → Bool) → Prop} {f : (Fin n → Bool) → Bool}
    (C : Circuit n (m + 1)) (hC : ∀ x, S x → C.eval x = f x) (i : Fin (m + 1)) (c : Bool)
    (h : ∀ x, S x → (C.leftVal x i ^^ C.rightVal x i) = c) : MCleOn S f m :=
  let ⟨C', hC'⟩ := C.elim_xor i S c h; ⟨C', fun x hx => (hC' x hx).trans (hC x hx)⟩

theorem MCle.xor_affine {n m : Nat} {f : (Fin n → Bool) → Bool} (l : AffFun n) (h : MCle f m) :
    MCle (fun x => f x ^^ l.eval x) m :=
  let ⟨C, hC⟩ := h; ⟨C.addOut l, fun x => by rw [C.eval_addOut, hC x]⟩

/-- **`MCle` is invariant under adding an affine function.** -/
theorem MCle_xor_affine_iff {n m : Nat} (f : (Fin n → Bool) → Bool) (l : AffFun n) :
    MCle (fun x => f x ^^ l.eval x) m ↔ MCle f m := by
  refine ⟨fun h => ?_, MCle.xor_affine l⟩
  obtain ⟨C, hC⟩ := h
  exact ⟨C.addOut l, fun x => by rw [C.eval_addOut, hC x, Bool.xor_assoc, Bool.xor_self, Bool.xor_false]⟩

/-- **`MCle` is preserved by affine substitution of the inputs:** `MC(f ∘ A) ≤ MC(f)`. -/
theorem MCle.comp_affine {n' n m : Nat} {f : (Fin n → Bool) → Bool} (A : AffMap n' n) (h : MCle f m) :
    MCle (fun x' => f (A.apply x')) m :=
  let ⟨C, hC⟩ := h; ⟨C.comp A, fun x' => by rw [C.eval_comp, hC]⟩

/-- Relativized affine substitution: if `A` maps `S'` into `S`, a circuit for `f` on `S` gives one for `f ∘ A`
on `S'`. -/
theorem MCleOn.comp_affine {n' n m : Nat} {S : (Fin n → Bool) → Prop} {S' : (Fin n' → Bool) → Prop}
    {f : (Fin n → Bool) → Bool} (A : AffMap n' n) (hA : ∀ x', S' x' → S (A.apply x')) (h : MCleOn S f m) :
    MCleOn S' (fun x' => f (A.apply x')) m :=
  let ⟨C, hC⟩ := h; ⟨C.comp A, fun x' hx' => by rw [C.eval_comp, hC _ (hA x' hx')]⟩

/-- **(F2): restriction through a parametrization.** If `A` maps every point into `S` (e.g. `A` parametrizes an
affine subspace contained in `S`), a circuit for `f` on `S` gives one for `f ∘ A` everywhere. -/
theorem MCleOn.comp_affine_of_maps_to {n' n m : Nat} {S : (Fin n → Bool) → Prop} {f : (Fin n → Bool) → Bool}
    (A : AffMap n' n) (hA : ∀ x', S (A.apply x')) (h : MCleOn S f m) : MCle (fun x' => f (A.apply x')) m :=
  (MCleOn_true_iff _).mp (h.comp_affine A (fun x' _ => hA x'))

/-- **(F4), with an explicit affine section.** If the affine map `A : 𝔽₂^n → 𝔽₂^k` has an affine right inverse
`B` and `μ` is affine, then `MC(h ∘ A + μ) ≤ m ↔ MC(h) ≤ m`. -/
theorem MCle_comp_section_iff {n k m : Nat} (h : (Fin k → Bool) → Bool) (A : AffMap n k) (B : AffMap k n)
    (hAB : ∀ u, A.apply (B.apply u) = u) (μ : AffFun n) :
    MCle (fun x => h (A.apply x) ^^ μ.eval x) m ↔ MCle h m := by
  refine ⟨fun hm => ?_, fun hm => (hm.comp_affine A).xor_affine μ⟩
  obtain ⟨C, hC⟩ := hm
  refine ⟨(C.comp B).addOut (μ.comp B), fun u => ?_⟩
  rw [Circuit.eval_addOut, Circuit.eval_comp, hC]
  simp only [hAB, AffFun.eval_comp, Bool.xor_assoc, Bool.xor_self, Bool.xor_false]

/-! ## Sanity checks of the semantics -/

/-- One AND gate computing `x₀ ∧ x₁`. -/
def andCircuit : Circuit 2 1 where
  left _ := ⟨false, fun t => decide (t.val = 0), fun _ => false⟩
  right _ := ⟨false, fun t => decide (t.val = 1), fun _ => false⟩
  out := ⟨false, fun _ => false, fun _ => true⟩

theorem andCircuit_eval (x : Fin 2 → Bool) : andCircuit.eval x = (x 0 && x 1) := by
  simp [Circuit.eval, AffForm.eval, andCircuit, Circuit.vals_eq, Circuit.leftVal, Circuit.rightVal, dot, xorSum]

theorem MCle_and2 : MCle (fun x : Fin 2 → Bool => x 0 && x 1) 1 := ⟨andCircuit, andCircuit_eval⟩

/-- `x₀ ∧ x₁` is not affine, so `MC(x₀x₁) = 1` exactly. -/
theorem not_MCle_and2_zero : ¬ MCle (fun x : Fin 2 → Bool => x 0 && x 1) 0 := by
  rw [MCle_zero_iff]
  rintro ⟨⟨c, a⟩, hl⟩
  have h00 := hl (fun _ => false)
  have h10 := hl (fun t => decide (t.val = 0))
  have h01 := hl (fun t => decide (t.val = 1))
  have h11 := hl (fun _ => true)
  simp [AffFun.eval, dot, xorSum] at h00 h10 h01 h11
  revert h00 h10 h01 h11
  cases c <;> cases a 0 <;> cases a 1 <;> simp

/-- Two AND gates computing `x₀ ∧ x₁ ∧ x₂`: `z₀ = x₀ ∧ x₁`, `z₁ = z₀ ∧ x₂`, output `z₁`. Gate 1 reads gate 0
through its gate coefficients. -/
def and3Circuit : Circuit 3 2 where
  left i := if i.val = 0 then ⟨false, fun t => decide (t.val = 0), fun _ => false⟩
    else ⟨false, fun _ => false, fun _ => true⟩
  right i := if i.val = 0 then ⟨false, fun t => decide (t.val = 1), fun _ => false⟩
    else ⟨false, fun t => decide (t.val = 2), fun _ => false⟩
  out := ⟨false, fun _ => false, fun j => decide (j.val = 1)⟩

theorem and3Circuit_eval (x : Fin 3 → Bool) : and3Circuit.eval x = (x 0 && x 1 && x 2) := by
  have hrun : and3Circuit.IsRun x (fun i => if i.val = 0 then (x 0 && x 1) else (x 0 && x 1 && x 2)) := by
    intro i
    match i with
    | ⟨0, _⟩ => simp [and3Circuit, AffForm.eval, dot, xorSum]
    | ⟨1, _⟩ => simp [and3Circuit, AffForm.eval, dot, xorSum, take]
  rw [Circuit.eval_eq_of_isRun hrun]
  simp [and3Circuit, AffForm.eval, dot, xorSum]

theorem MCle_and3 : MCle (fun x : Fin 3 → Bool => x 0 && x 1 && x 2) 2 := ⟨and3Circuit, and3Circuit_eval⟩

end NPFrontier
