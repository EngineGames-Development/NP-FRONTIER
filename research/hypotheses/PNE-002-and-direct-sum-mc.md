# PNE-002: AND-direct sum for multiplicative complexity

**Status:** FORMULATED. Open; believed hard. No proof attempt beyond the special case PNE-001.

## Formulation
For non-constant g on variables x and h on disjoint variables y: **MC(g(x)·h(y)) = MC(g) + MC(h) + 1.** The upper bound is trivial.

## Why it matters, and why it is hard
- **Implication (proved, elementary).** If PNE-002 holds, then for every constant c there is an explicit function in P with MC ≥ c·n, hence circuit size ≥ c·n over the full binary basis. Proof: fix k with M(k) ≥ (c+1)k (counting gives M(k) ≥ 2^{k/2} − O(k)). Find a hardest k-variable function by brute force, in constant time for fixed k. AND together n/k copies on disjoint blocks.
- The best refereed explicit circuit lower bound is 3.1n − o(n) (Li–Yang, STOC 2022). A 3.5n − o(n) bound is claimed in ECCC TR26-260 (Mishra–Santhanam, Oct 2026; unrefereed, not verified here). So PNE-002 is at least as strong as a major open problem. This is a warning sign, not a free route.
- Even the weak form MC(g·h) ≥ MC(g) + MC(h) would already give superlinear-constant bounds of this kind.
- For ordinary circuit size the analogous AND-direct sum is believed false. This is a deduction by the literature agent from Uhlig's 1974 mass-production theorem, ≈ 85% confidence, not checked against the sources.

## Competing hypothesis
PNE-002 fails for some small pair (g, h). Testable by SAT on ≤ 6 total variables. Not yet run: UNSAT proofs on 5–6 variables are slow with the current encoding (EXP-001 notes).

## Next steps
Search small pairs where both factors have MC > D (only these can fail, by the argument of Corollary 5 applied to each side; this needs a two-sided version of Theorem 4, not yet proved).
