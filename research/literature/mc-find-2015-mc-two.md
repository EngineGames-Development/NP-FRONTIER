# Find, Smith-Tone, Sönmez Turan (2015): The number of Boolean functions with multiplicative complexity 2

| Field | Value |
|---|---|
| Title | The Number of Boolean Functions with Multiplicative Complexity 2 |
| Authors | Magnus Gausdal Find, Daniel Smith-Tone, Meltem Sönmez Turan |
| Year | 2015 (ePrint); journal 2017 |
| Venue | International Journal of Information and Coding Theory (Inderscience), 2017. Volume, issue and pages **not confirmed** |
| ePrint | IACR ePrint 2015/1041 (CC BY) |
| Group | MC: classification of low-MC functions. Index: `index-multiplicative-complexity.md` |

## Relevant theorem (abstract level)

- The authors characterize the structure of functions with MC 2 in terms of affine equivalence. This gives a **closed-form formula for the number of n-variable functions with MC 2**.
- It builds on Fischer–Peralta (2002), who counted the functions with MC 1. That paper was not checked.
- Sönmez Turan's 2022 slides summarize the result: MC-2 functions are affine equivalent to one of **three representative forms**. The representatives and the formula were **not legible** in the snippets.

## Why it matters for NP-FRONTIER

- This is the paper the task brief probably had in mind when it attributed "When six gates are not enough" to these authors. That attribution is wrong; see `mc-codish-2015-six-gates.md`.
- The MC ≤ 2 classification is a small sanity check for the fresh-variable lemma (index item (a)).
  - For g with MC(g) = 1, g is a quadratic of rank 2, which is degree-tight, so (a) holds by the degree bound.
  - g with MC(g) = 2 that are not degree-tight are rank-4 quadratics. For these, (a) follows from the quadratic argument (index observation D4).

## Limitations

- Abstract level only.
- The journal bibliographic details are incomplete.
- The ePrint abstract and the NIST/CSRC abstract reportedly give different formulas for the MC-1 count, so do not rely on either without the PDF.

## Retrieval

- Title, authors, ePrint 2015/1041, journal name and year (Inderscience offer id 86890), the closed-form-count statement and the Fischer–Peralta 2002 dependence: from WebSearch summaries of the ePrint page, NIST/CSRC pages, DBLP (journals/iacr/FindST15) and the Inderscience page.
- "Three representative forms": from a WebSearch summary of Sönmez Turan's BFA 2022 slides.
- Formula discrepancy note: from the same WebSearch summary.
