# Alon, Boppana (1987): The monotone circuit complexity of Boolean functions

| Field | Value |
|---|---|
| Title | The monotone circuit complexity of Boolean functions |
| Authors | Noga Alon, Ravi B. Boppana |
| Year | 1987 |
| Venue | Combinatorica 7(1), 1987, pp. 1–22 according to the PDF header (another citation gives 1–23) |
| DOI | 10.1007/BF02579196 (from an unpaywall URL in search results) |
| URL | https://web.math.princeton.edu/~nalon/PDFS/Publications/The%20monotone%20circuit%20complexity%20of%20Boolean%20functions.pdf |
| Group | Circuit lower bound frontier (restricted model: monotone circuits) |

## Relevant theorems

Abstract level, confirmed via WebSearch summaries; one OCR caveat noted.

The paper modifies Razborov's approximation method to obtain **exponential** monotone lower bounds.

1. **Exponential bound for large cliques.** Detecting cliques of size (1/4)(m/log m)^{2/3} in m-vertex graphs requires monotone circuits of size **exp(Ω((m/log m)^{1/3}))**. One OCR'd copy renders the clique-size exponent as 1/3 instead of 2/3; check the original.
2. **Fixed s.** For fixed s, monotone circuits detecting s-cliques need about m^s/(log m)^s gates (recalled form, unverified).
3. **Approximation is also hard.** Even a very rough approximation of the maximum clique size requires superpolynomial monotone circuits.
4. **Best NP-function bound.** For an NP function of n variables, the bound is **exp(Ω(n^{1/4}·(log n)^{1/2}))**, improving Andreev's exp(Ω(n^{1/8−ε})).
5. **Functions in monotone P.** The paper also gives lower bounds for some functions in monotone P (recalled).

## Later results relevant to interpretation

1. **Tardos (1988): exponential monotone/non-monotone gap.**
   - É. Tardos, "The gap between monotone and non-monotone circuit complexity is exponential", Combinatorica 8 (1988) 141–142, DOI 10.1007/BF02122563. The author-hosted PDF header says 7(4) (1987); Springer's record says 8 (1988).
   - Result: a monotone function computable in polynomial time, via the Lovász theta function / semidefinite programming, whose monotone circuit complexity is **exp(c·n^{1/6−o(1)})**.
2. **Cavalar, Kumar, Rossman (2022): improved monotone bounds via robust sunflowers.**
   - "Monotone Circuit Lower Bounds from Robust Sunflowers", Algorithmica 84(12):3655–3685, 2022; arXiv 2012.03883; ECCC TR20-181.
   - CLIQUE: monotone lower bound n^{Ω(k)} for all k ≤ n^{1/3−o(1)}, strengthening Alon–Boppana in that range.
   - Explicit monotone function: lower bound exp(n^{1/2−o(1)}), improving the previous exp(n^{1/3−o(1)}) attributed to Andreev and to Harnik–Raz.
   - Later improvements, if any, were not checked.

## What it rules out or limits

1. **P = NP side.** Even approximating max-clique cannot be done by polynomial-size monotone circuits.
   - Candidate CLIQUE / Independent Set algorithms whose computation is monotone in the edge variables are refuted, even as approximation algorithms.
2. **P ≠ NP side.** Tardos's function shows that exponential monotone lower bounds hold for functions in P.
   - Monotone lower bounds, however strong, are not evidence of non-membership in P.
   - The approximation method in its monotone form cannot separate P from NP.

## Why it matters for NP-FRONTIER

- It calibrates the strongest known lower bounds for NP-complete problems in a natural restricted model: exponential.
- It is the standard counterexample to "monotone hardness implies general hardness" reasoning.

## Limitations

- Monotone circuits only.
- Constants and exponent conventions vary between the abstract and later sources (m = number of vertices vs n = number of input variables, about m²/2).

## Retrieval

- Authors, Combinatorica 7(1) 1987, page range (1–22 per PDF header; 1–23 per another source): confirmed via WebSearch (Princeton PDF, Princeton publication record, MaRDI portal; result summaries).
- DOI: taken from an unpaywall URL in the WebSearch result list.
- Main statements 1, 3 and 4 (clique-size/size exponents; rough approximation; exp(Ω(n^{1/4}(log n)^{1/2})) vs Andreev's exp(Ω(n^{1/8−ε}))): confirmed via WebSearch summaries of the paper's abstract/introduction, with the OCR caveat above. A first WebSearch summary garbled the Andreev comparison; the second, targeted search gave the consistent version recorded here.
- Statements 2 and 5: recalled.
- Tardos 1988 bibliographic data and the exp(cn^{1/6−o(1)}) bound: confirmed via WebSearch (Springer record, author PDF, Wikipedia "Tardos function"; result summaries).
- Cavalar–Kumar–Rossman bibliographic data and bounds: confirmed via WebSearch summaries of the arXiv abstract and the Springer/PMC version.
