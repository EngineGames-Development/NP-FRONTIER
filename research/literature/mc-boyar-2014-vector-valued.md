# Boyar, Find (2014/2018): Multiplicative complexity of vector valued Boolean functions

| Field | Value |
|---|---|
| Title | Multiplicative Complexity of Vector Valued Boolean Functions |
| Authors | Joan Boyar, Magnus Gausdal Find. The arXiv listing was relayed as "Magnus Gausdal Find and Joan Boyar"; MaRDI and the journal list Boyar first |
| Year | 2014 (arXiv); journal 2018 |
| Venue | Theoretical Computer Science, 2018 (published online 12 March 2018 per MaRDI). Volume and pages: **unverified** (Agent D recalls vol. 720, pp. 36–46; not confirmed) |
| DOI | 10.1016/j.tcs.2018.02.023 |
| arXiv | 1407.6169 |
| Conference version | "The Relationship Between Multiplicative Complexity and Nonlinearity", MFCS 2014 |
| Group | MC: explicit lower bounds, vector-valued. Index: `index-multiplicative-complexity.md` |

## Relevant theorems (abstract level, relayed)

1. **Explicit vector-valued lower bound.** The (n, n)-function f with f_i(x) = ∏_{j ∈ [n] \ {i}} x_j (all n monomials of degree n − 1) has MC ≥ **2n − 3** for general circuits.
   - The paper also gives an upper bound of 3n − 6 and calls closing the gap an interesting open question.
   - The gap was closed by Häner (2023): MC = 2n − 3 exactly (`mc-haner-2023-monomials.md`).
2. **Generic upper bound.** Every function with n inputs and m outputs can be computed with at most 2.5(1 + o(1))·√(m·2^n) AND gates.
3. **ΣΠΣ circuits and codes.** For ΣΠΣ circuits there is a tight connection between error-correcting codes and functions with high nonlinearity. As a consequence, (n, n)-functions with the highest possible nonlinearity need at least 2.32n AND gates in that model. Nonlinearity alone cannot give stronger bounds (relayed).
4. **Open question.** Per MathWorld, Boyar and Find asked whether every quadratic map over F_2 has an optimal unrestricted circuit in which all intermediate values have degree ≤ 2.

## Why it matters for NP-FRONTIER

- It answers index item (c), vector-valued part: **2n − 3 is the best explicit general-circuit MC lower bound found for (n, n)-functions**, and it is tight for this function.
- Context, from Agent D's observation D6 in the index: m outputs that are linearly independent modulo affine functions trivially need ≥ m AND gates. The interest of 2n − 3 is that it exceeds both the number of inputs and the number of outputs.
- It does not give a single-output bound.
  - Combining the outputs into one function (for example Σ z_i f_i with selector variables z) is not known to preserve the bound.
  - Agent D found no source that converts this into a single-output MC ≥ n result.

## Limitations

- Vector-valued only.
- The proof technique was not seen. A snippet suggested a first-AND-gate/degree argument, but it was garbled.

## Retrieval

- Title, arXiv ID 1407.6169, MFCS 2014 conference version, TCS publication and items 1–3: from WebSearch summaries of the arXiv abstract (arxiv.org/abs/1407.6169v2), ar5iv, the author page (imada.sdu.dk/~joan/tcsmult.html) and NIST pages.
- The function definition f_i = ∏_{j≠i} x_j and "best lower bound … for (n, n)-functions" wording: from a WebSearch summary of the arXiv PDF text.
- DOI and online date: from WebSearch summaries of the MaRDI portal and Bohrium records.
- Item 4: from a WebSearch summary of the MathWorld entry.
- Volume and pages: recalled, unverified.
