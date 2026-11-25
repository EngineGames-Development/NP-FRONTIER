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

## Gaps between the formal and informal statements

- **Weight parity:** `par` is defined recursively, as the XOR of the parities of the two halves. Its agreement with "number of inputs `xs` with `eval f xs = true`, mod 2" is not proved; it holds by construction of the Shannon split.
- **Degree:** `DegLE c d` is a recursive predicate on coefficient trees. Its agreement with "every monomial with nonzero coefficient has at most `d` variables" holds by construction and is not separately proved.
- **Lemma 3** is formalized only for hyperplanes `{x = c}` on a single coordinate. The general case `{⟨v,x⟩ = c}` needs affine changes of coordinates, which are not formalized.
- **Not formalized:** Lemma 1 (D ≤ MC), Lemma 2, Theorem 4 (`D(y·g) = D(g) + 1`), and Corollaries 5–7 of PNE-001. They need XOR-AND circuits, affine subspaces and restrictions over 𝔽₂. This is the next formalization target.
