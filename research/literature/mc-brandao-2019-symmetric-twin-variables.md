# Brandão, Çalık, Sönmez Turan, Peralta (2019): Upper bounds on the multiplicative complexity of symmetric Boolean functions

| Field | Value |
|---|---|
| Title | Upper Bounds on the Multiplicative Complexity of Symmetric Boolean Functions |
| Authors | Luís T. A. N. Brandão, Çağdaş Çalık, Meltem Sönmez Turan, René Peralta |
| Year | 2019 |
| Venue | Cryptography and Communications 11 (2019), 1339–1362 |
| ePrint | IACR ePrint 2019/708 |
| Workshop version | "On the Multiplicative Complexity of Symmetric Boolean Functions", BFA 2018 (3rd Int. Workshop on Boolean Functions and their Applications), Loen, Norway, June 19, 2018; abstract at org.uib.no/selmer/workshops/BFA2018/Abstracts/Calik.pdf |
| Group | MC: upper bounds; "twin variables" reduction. Index: `index-multiplicative-complexity.md` |

## Relevant statements (relayed)

1. **Twin variables.** Variables x_1, x_2 are *twins* in f if f = x_1 x_2·f_1 + f_2 with f_1 ≠ 0. Presumably f_1 and f_2 do not depend on x_1, x_2; that condition is unverified.
2. **Symmetric functions.** Every nonlinear symmetric Boolean function is affine equivalent to a function with twin variables.
3. **Reduction bound.** C∧(f) ≤ 1 + C∧(x_1 f_1 + f_2).
   - Agent D's reading of why: take a circuit for x_1 f_1 + f_2 and substitute the product x_1 x_2 for x_1, which costs one AND.
4. **Computations.**
   - Upper bounds for symmetric functions on up to 25 variables.
   - Bounds on the maximum MC of n-variable symmetric functions for n ≤ 132 (relayed).
   - The 8-variable functions Σ^8_4 and E^8_4 have MC 6. This answers two questions from Boyar–Peralta 2008.

## Relationship to the fresh-variable lemma (index item (a))

Take f_2 = 0 and set g := x_1 f_1, y := x_2 (y is fresh for g). Item 3 then reads MC(g·y) ≤ MC(g) + 1, which is the trivial upper-bound half of (a).
- Lemma (a) asserts that the twin-variable reduction is **tight** in this case: MC(x_1 x_2 f_1) = MC(x_1 f_1) + 1.
- Item 3 is an upper bound, so it neither implies nor refutes (a).

## Limitations

- Abstract level only.
- The precise hypotheses of the twin-variable definition are unverified.

## Retrieval

- Journal title, authors, volume and pages (1339–1362), ePrint 2019/708, BFA 2018 details and items 1–4: from WebSearch summaries of the BFA 2018 abstract PDF (org.uib.no …/Calik.pdf), the CSRC publication page and ePrint 2019/708.
- The substitution explanation of item 3: Agent D's reasoning.
