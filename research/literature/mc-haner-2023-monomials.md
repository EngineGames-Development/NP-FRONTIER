# Häner (2023): Computing all monomials of degree n−1 using 2n−3 AND gates

| Field | Value |
|---|---|
| Title | Computing all monomials of degree n−1 using 2n−3 AND gates |
| Authors | Thomas Häner (sole author; Amazon Quantum Solutions Lab, Zürich, per search summary) |
| Year | 2023 (DeepAI dates it June 2023) |
| Venue | arXiv preprint 2307.07424. A refereed venue was **not confirmed** |
| Group | MC: explicit vector-valued bounds (tightness). Index: `index-multiplicative-complexity.md` |

## Relevant theorem (abstract level)

- The paper gives an AND-optimal circuit with **2n − 3 AND gates** for the (n, n)-function whose outputs are all n monomials of degree n − 1. This is the Boyar–Find function f_i = ∏_{j≠i} x_j.
- Combined with Boyar–Find's lower bound 2n − 3, the MC of this function is **exactly 2n − 3**. Previously it was known to lie in [2n − 3, 3n − 6].

## Why it matters for NP-FRONTIER

- The best explicit vector-valued (n, n) lower bound is tight for its function. Any improvement beyond 2n − 3 for explicit (n, n)-functions needs a different function.
- This is an example of a degree-type lower bound being tight even for multi-output functions.

## Limitations

- Vector-valued.
- Abstract level only.

## Retrieval

- Title, arXiv ID, sole author and affiliation, approximate date and main statement: from WebSearch summaries of arxiv.org/pdf/2307.07424, ar5iv and DeepAI. Consistent with the Boyar–Find abstract (`mc-boyar-2014-vector-valued.md`).
