# Schnorr (1988): The multiplicative complexity of Boolean functions (degree lower bound)

| Field | Value |
|---|---|
| Title | The Multiplicative Complexity of Boolean Functions |
| Authors | Claus-Peter Schnorr |
| Year | 1988 (AAECC-6, Rome, July 4–8, 1988). Some citations give 1989, the year the Springer volume appeared |
| Venue | Applied Algebra, Algebraic Algorithms and Error-Correcting Codes (AAECC-6), ed. Teo Mora, LNCS 357, pp. 45–58 |
| DOI | 10.1007/3-540-51083-4_47 (as given by MathWorld; relayed by a search summary) |
| Group | Multiplicative complexity (MC): foundations. Index: `index-multiplicative-complexity.md` |

## Definitions

- **MC(f) = c∧(f):** the minimum number of AND gates in a circuit over the basis {AND, XOR, 1}. XOR gates and constants are free. This equals the minimum over {AND, XOR, NOT}.
- For a vector-valued F = (f_1, …, f_m), MC(F) counts AND gates in one circuit with m outputs.
- **deg f:** the degree of the GF(2) algebraic normal form (ANF).

## Relevant theorem

**Degree bound** (attributed to this paper by MathWorld and by later MC papers). Let d be the largest algebraic degree among the coordinate functions of F. Then MC(F) ≥ d − 1.

Consequences:
- Every f of degree n on n variables has MC(f) ≥ n − 1.
- MC(x_1 x_2 ⋯ x_n) = n − 1. The upper bound comes from a chain of ANDs.

**Proof sketch.** Reconstructed by Agent D from the standard argument; not checked against Schnorr's text.

The proof is by induction on the number k of AND gates.
1. If k = 0, F is affine, so deg ≤ 1.
2. Otherwise, let A·B be a topologically first AND gate, so A and B are affine in the inputs. If A is constant, the gate is affine and can be removed.
3. If A is not constant, change coordinates so that A = z_1. For any output f, write f = (1 + z_1)·f_0 + z_1·f_1 with f_c = f|_{z_1 = c}. Then deg f ≤ 1 + max_c deg f_c.
4. On the hyperplane z_1 = c, the gate equals c·B, which is affine. So f_c is computed with k − 1 AND gates, and by induction deg f_c ≤ k.
5. Hence deg f ≤ k + 1.

This is the prototype of the **affine-restriction** technique, the MC analogue of gate elimination.

## Why it matters for NP-FRONTIER

- It gives the best known explicit single-output MC lower bound, n − 1. See `mc-kojevnikov-2010-circuit-vs-mc.md` and `mc-demenkov-2011-affine-dispersers.md`.
- **Fresh-variable lemma (index item (a)).** Since deg(g·y) = deg(g) + 1, the bound gives MC(g·y) ≥ deg(g).
  - So (a) holds automatically for every "degree-tight" g, meaning MC(g) = deg(g) − 1.
  - It gives nothing when MC(g) ≥ deg(g).
- **AND-direct sum (index item (b)).** If g and h are both degree-tight, then MC(g·h) ≥ deg g + deg h − 1 = MC(g) + MC(h) + 1, so (b) holds in that special case.

## Limitations

- For a single output on n variables, the bound can never exceed n − 1.
- The statement is relayed from MathWorld and secondary citations. The exact formulation and theorem number in the paper were not seen.

## Retrieval

- Title, author, AAECC-6, LNCS 357, pp. 45–58, editor Teo Mora, and "Rome, Italy, July 4-8, 1988": from a WebSearch result summary of the researchr.org record (Schnorr88:0).
- DOI and the statement "MC ≥ d − 1 where d is the largest degree among coordinate functions (Schnorr 1989)": from a WebSearch summary of the MathWorld "MultiplicativeComplexity" entry. That entry is a secondary source and also cites 2026 preprints.
- Proof sketch: reconstructed by Agent D; not checked against the paper.
