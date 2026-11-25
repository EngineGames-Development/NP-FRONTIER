/-!
# Boolean functions as Shannon trees, algebraic normal form, weight parity, degree

A function on `n + 1` variables is the pair `(f₀, f₁)` of its restrictions to `x = 0` and `x = 1`, where `x` is
the last variable. Over this representation:

* `anf` is the Möbius transform: the coefficient tree of the algebraic normal form (ANF) over `𝔽₂`,
  using `f = f₀ + x·(f₀ + f₁)`.
* `par f` is the parity of the number of inputs on which `f` is `1`.
* `top c` reads the coefficient of the full monomial `x₁⋯xₙ` from a coefficient tree.

Main results (all proved, no axioms beyond Lean's core):
* `top_anf` : the coefficient of `x₁⋯xₙ` in the ANF of `f` equals the parity of the weight of `f`
  (so `deg f = n` iff `f` has odd weight).
* `degC_xor_le` : the degree of a sum of polynomials is at most the larger degree.
* `deg_le_restrict_succ` : for the last variable, `deg f ≤ 1 + max (deg f₀) (deg f₁)`, i.e. one of the two
  restrictions has degree at least `deg f - 1` (Lemma 3 of PNE-001, coordinate-hyperplane case).
* `deg_restrict_le` : restricting a variable does not increase degree.
-/

namespace NPFrontier

/-- Shannon trees of depth `n`: Boolean functions on `n` variables. -/
inductive BF : Nat → Type
  | leaf : Bool → BF 0
  | node {n : Nat} : BF n → BF n → BF (n + 1)

namespace BF

/-- Pointwise XOR (addition over `𝔽₂`). -/
def xor : {n : Nat} → BF n → BF n → BF n
  | _, leaf a, leaf b => leaf (a ^^ b)
  | _, node a₀ a₁, node b₀ b₁ => node (xor a₀ b₀) (xor a₁ b₁)

/-- Parity of the number of ones of the truth table. -/
def par : {n : Nat} → BF n → Bool
  | _, leaf a => a
  | _, node a₀ a₁ => par a₀ ^^ par a₁

/-- Möbius transform: ANF coefficient tree. Left subtree: monomials without the last variable `x`;
right subtree: monomials containing `x`. -/
def anf : {n : Nat} → BF n → BF n
  | _, leaf a => leaf a
  | _, node a₀ a₁ => node (anf a₀) (anf (xor a₀ a₁))

/-- Coefficient of the full monomial `x₁⋯xₙ` in a coefficient tree. -/
def top : {n : Nat} → BF n → Bool
  | _, leaf a => a
  | _, node _ c₁ => top c₁

theorem par_xor : {n : Nat} → (a b : BF n) → par (xor a b) = (par a ^^ par b)
  | _, leaf a, leaf b => by simp [xor, par]
  | _, node a₀ a₁, node b₀ b₁ => by
      simp only [xor, par, par_xor a₀ b₀, par_xor a₁ b₁]
      cases par a₀ <;> cases par a₁ <;> cases par b₀ <;> cases par b₁ <;> rfl

/-- The coefficient of `x₁⋯xₙ` in the ANF equals the weight parity. -/
theorem top_anf : {n : Nat} → (f : BF n) → top (anf f) = par f
  | _, leaf a => rfl
  | _, node a₀ a₁ => by simp only [anf, top, par, top_anf (xor a₀ a₁), par_xor]

theorem xor_swap : {n : Nat} → (a b c d : BF n) → xor (xor a b) (xor c d) = xor (xor a c) (xor b d)
  | _, leaf a, leaf b, leaf c, leaf d => by cases a <;> cases b <;> cases c <;> cases d <;> rfl
  | _, node a₀ a₁, node b₀ b₁, node c₀ c₁, node d₀ d₁ => by
      simp only [xor, xor_swap a₀ b₀ c₀ d₀, xor_swap a₁ b₁ c₁ d₁]

theorem xor_cancel : {n : Nat} → (a b : BF n) → xor a (xor a b) = b
  | _, leaf a, leaf b => by cases a <;> cases b <;> rfl
  | _, node a₀ a₁, node b₀ b₁ => by simp only [xor, xor_cancel a₀ b₀, xor_cancel a₁ b₁]

/-- The Möbius transform is linear over `𝔽₂`. -/
theorem anf_xor : {n : Nat} → (a b : BF n) → anf (xor a b) = xor (anf a) (anf b)
  | _, leaf _, leaf _ => rfl
  | _, node a₀ a₁, node b₀ b₁ => by
      simp only [xor, anf]
      rw [anf_xor a₀ b₀, xor_swap a₀ b₀ a₁ b₁, anf_xor (xor a₀ a₁) (xor b₀ b₁)]

/-! ### Semantics. Inputs are lists of bits, head = last variable (missing bits read as `false`). -/

/-- Evaluate a function at an input. -/
def eval : {n : Nat} → BF n → List Bool → Bool
  | _, leaf a, _ => a
  | _, node f₀ _, [] => eval f₀ []
  | _, node f₀ f₁, x :: xs => if x then eval f₁ xs else eval f₀ xs

/-- Evaluate a coefficient tree as a polynomial over `𝔽₂`: `c₀(xs) + x · c₁(xs)`. -/
def peval : {n : Nat} → BF n → List Bool → Bool
  | _, leaf a, _ => a
  | _, node c₀ _, [] => peval c₀ []
  | _, node c₀ c₁, x :: xs => peval c₀ xs ^^ (x && peval c₁ xs)

theorem eval_xor : {n : Nat} → (a b : BF n) → (xs : List Bool) → eval (xor a b) xs = (eval a xs ^^ eval b xs)
  | _, leaf _, leaf _, _ => rfl
  | _, node a₀ _, node b₀ _, [] => by simp only [xor, eval]; exact eval_xor a₀ b₀ []
  | _, node a₀ a₁, node b₀ b₁, x :: xs => by
      cases x <;> simp only [xor, eval] <;> simp [eval_xor]

/-- **`anf` is the algebraic normal form**: evaluating the coefficient tree as a polynomial gives the
function's value at every input. -/
theorem peval_anf : {n : Nat} → (f : BF n) → (xs : List Bool) → peval (anf f) xs = eval f xs
  | _, leaf _, _ => rfl
  | _, node f₀ _, [] => by simp only [anf, peval, eval]; exact peval_anf f₀ []
  | _, node f₀ f₁, x :: xs => by
      simp only [anf, peval, eval, peval_anf f₀ xs, peval_anf (xor f₀ f₁) xs, eval_xor]
      cases x <;> cases eval f₀ xs <;> cases eval f₁ xs <;> rfl

/-! ### Degree. `DegLE c d` says the coefficient tree `c` has degree at most `d`
(the zero polynomial has every degree bound). -/

/-- The zero polynomial / zero function. -/
def IsZero : {n : Nat} → BF n → Prop
  | _, leaf a => a = false
  | _, node c₀ c₁ => IsZero c₀ ∧ IsZero c₁

/-- Degree bound on a coefficient tree: monomials without the last variable have degree `≤ d`, and
monomials with it have degree `≤ d` (so the remaining part has degree `≤ d - 1`) unless there are none. -/
def DegLE : {n : Nat} → BF n → Nat → Prop
  | _, leaf _, _ => True
  | _, node c₀ c₁, d => DegLE c₀ d ∧ (IsZero c₁ ∨ (1 ≤ d ∧ DegLE c₁ (d - 1)))

/-- `deg f ≤ d` for a function `f` (degree of its algebraic normal form). -/
def DegLEf {n : Nat} (f : BF n) (d : Nat) : Prop := DegLE (anf f) d

theorem degLE_mono : {n : Nat} → (c : BF n) → {d d' : Nat} → DegLE c d → d ≤ d' → DegLE c d'
  | _, leaf _, _, _, _, _ => trivial
  | _, node c₀ c₁, _, _, h, hle => by
      simp only [DegLE] at h ⊢
      obtain ⟨h₀, h₁⟩ := h
      refine ⟨degLE_mono c₀ h₀ hle, ?_⟩
      rcases h₁ with hz | ⟨hd, h⟩
      · exact Or.inl hz
      · exact Or.inr ⟨by omega, degLE_mono c₁ h (by omega)⟩

theorem degLE_of_isZero : {n : Nat} → (c : BF n) → IsZero c → (d : Nat) → DegLE c d
  | _, leaf _, _, _ => trivial
  | _, node c₀ c₁, h, d => by
      simp only [IsZero] at h; simp only [DegLE]
      exact ⟨degLE_of_isZero c₀ h.1 d, Or.inl h.2⟩

theorem isZero_xor : {n : Nat} → (a b : BF n) → IsZero a → IsZero b → IsZero (xor a b)
  | _, leaf a, leaf b, ha, hb => by
      simp only [IsZero] at ha hb; subst ha; subst hb; rfl
  | _, node a₀ a₁, node b₀ b₁, ha, hb => by
      simp only [IsZero, xor] at ha hb ⊢
      exact ⟨isZero_xor a₀ b₀ ha.1 hb.1, isZero_xor a₁ b₁ ha.2 hb.2⟩

/-- Degree of a sum is at most the larger degree. -/
theorem degLE_xor : {n : Nat} → (a b : BF n) → {d : Nat} → DegLE a d → DegLE b d → DegLE (xor a b) d
  | _, leaf _, leaf _, _, _, _ => trivial
  | _, node a₀ a₁, node b₀ b₁, _, ha, hb => by
      simp only [DegLE, xor] at ha hb ⊢
      obtain ⟨ha₀, ha₁⟩ := ha
      obtain ⟨hb₀, hb₁⟩ := hb
      refine ⟨degLE_xor a₀ b₀ ha₀ hb₀, ?_⟩
      rcases ha₁ with hza | ⟨hda, ha⟩ <;> rcases hb₁ with hzb | ⟨hdb, hb⟩
      · exact Or.inl (isZero_xor a₁ b₁ hza hzb)
      · exact Or.inr ⟨hdb, degLE_xor a₁ b₁ (degLE_of_isZero a₁ hza _) hb⟩
      · exact Or.inr ⟨hda, degLE_xor a₁ b₁ ha (degLE_of_isZero b₁ hzb _)⟩
      · exact Or.inr ⟨hda, degLE_xor a₁ b₁ ha hb⟩

/-- **Lemma 3 of PNE-001, coordinate-hyperplane case (contrapositive form).** If both restrictions of `f`
to `x = 0` and `x = 1` (last variable) have degree `≤ d`, then `deg f ≤ d + 1`. Equivalently, one of the
two restrictions has degree `≥ deg f - 1`. -/
theorem degLE_node_of_restrict {n : Nat} (f₀ f₁ : BF n) (d : Nat)
    (h₀ : DegLEf f₀ d) (h₁ : DegLEf f₁ d) : DegLEf (node f₀ f₁) (d + 1) := by
  unfold DegLEf at *
  simp only [anf, DegLE]
  refine ⟨degLE_mono _ h₀ (by omega), Or.inr ⟨by omega, ?_⟩⟩
  rw [Nat.add_sub_cancel, anf_xor]
  exact degLE_xor _ _ h₀ h₁

/-- Restricting a variable does not increase degree. -/
theorem degLE_restrict {n : Nat} (f₀ f₁ : BF n) (d : Nat) (h : DegLEf (node f₀ f₁) d) :
    DegLEf f₀ d ∧ DegLEf f₁ d := by
  unfold DegLEf at *
  simp only [anf, DegLE] at h
  obtain ⟨h₀, h₁⟩ := h
  have hx : DegLE (anf (xor f₀ f₁)) d := by
    rcases h₁ with hz | ⟨_, h⟩
    · exact degLE_of_isZero _ hz d
    · exact degLE_mono _ h (by omega)
  refine ⟨h₀, ?_⟩
  have : f₁ = xor f₀ (xor f₀ f₁) := (xor_cancel f₀ f₁).symm
  rw [this, anf_xor]
  exact degLE_xor _ _ h₀ hx

theorem degLE_self : {n : Nat} → (c : BF n) → DegLE c n
  | _, leaf _ => trivial
  | _, node c₀ c₁ => by
      simp only [DegLE]
      exact ⟨degLE_mono c₀ (degLE_self c₀) (by omega), Or.inr ⟨by omega, by simpa using degLE_self c₁⟩⟩

theorem top_of_isZero : {n : Nat} → (c : BF n) → IsZero c → top c = false
  | _, leaf _, h => h
  | _, node _ c₁, h => by
      simp only [IsZero] at h; simp only [top]
      exact top_of_isZero c₁ h.2

/-- A coefficient tree on `n + 1` variables has degree `≤ n` iff the coefficient of `x₁⋯xₙ₊₁` is `0`. -/
theorem degLE_pred_iff_top : {n : Nat} → (c : BF (n + 1)) → (DegLE c n ↔ top c = false)
  | 0, node c₀ (leaf b) => by
      simp only [DegLE, top, IsZero]
      constructor
      · rintro ⟨_, h | ⟨h, _⟩⟩
        · exact h
        · omega
      · intro h; exact ⟨degLE_self c₀, Or.inl h⟩
  | m + 1, node c₀ c₁ => by
      simp only [DegLE, top]
      have ih := degLE_pred_iff_top (n := m) c₁
      constructor
      · rintro ⟨_, hz | ⟨_, h⟩⟩
        · exact top_of_isZero c₁ hz
        · exact ih.mp (by simpa using h)
      · intro h
        exact ⟨degLE_self c₀, Or.inr ⟨by omega, by simpa using ih.mpr h⟩⟩

/-- **Full degree iff odd weight.** For `f` on `n + 1` variables, `deg f ≤ n` iff the number of inputs
with `f = 1` is even. -/
theorem degLE_pred_iff_even_weight {n : Nat} (f : BF (n + 1)) : DegLEf f n ↔ par f = false := by
  unfold DegLEf
  rw [degLE_pred_iff_top, top_anf]

end BF

/-! ### Boolean identities used in the proof of Theorem 4 (PNE-001). -/

/-- Gate normalization: `(y + α)(y + β) = (y + α)(1 + α + β)` over `𝔽₂`, so at most one input of an AND gate
needs to contain the fresh variable `y`. -/
theorem gate_normalize (y a b : Bool) : ((y ^^ a) && (y ^^ b)) = ((y ^^ a) && !(a ^^ b)) := by
  cases y <;> cases a <;> cases b <;> rfl

/-- Fresh-variable identity used in Case C: `u · h(u, x) = u · h(1, x)`. -/
theorem mul_eval_one {α : Type} (h : Bool → α → Bool) (u : Bool) (x : α) :
    (u && h u x) = (u && h true x) := by
  cases u <;> rfl

end NPFrontier
