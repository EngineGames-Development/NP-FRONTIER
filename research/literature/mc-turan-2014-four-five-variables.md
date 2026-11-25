# Sönmez Turan, Peralta (2014): The multiplicative complexity of Boolean functions on four and five variables

| Field | Value |
|---|---|
| Title | The Multiplicative Complexity of Boolean Functions on Four and Five Variables |
| Authors | Meltem Sönmez Turan, René Peralta. The family name is "Sönmez Turan"; NIST, Springer and DBLP list her first, while one library catalog lists Peralta first |
| Year | 2014 (workshop); proceedings published 2015 |
| Venue | LightSec 2014 (Istanbul), LNCS 8898, pp. 21–33 |
| DOI | 10.1007/978-3-319-16363-5_2 |
| ePrint | Listed by DBLP as IACR ePrint 2015/848 (relayed by a search summary; **unverified**) |
| Group | MC: exact values for small n. Index: `index-multiplicative-complexity.md` |

## Relevant theorems (relayed)

Let M(n) be the maximum MC over all n-variable Boolean functions.
1. Every 4-variable function has MC ≤ 3. This verifies an earlier result, so **M(4) = 3**.
2. Every 5-variable function has MC ≤ 4, so **M(5) = 4**.
3. The method uses affine equivalence classes of functions.

The lower bounds M(n) ≥ n − 1 follow from the degree bound applied to x_1⋯x_n (`mc-schnorr-1988-degree-bound.md`).

## Why it matters for NP-FRONTIER

- For n ≤ 5, the degree bound n − 1 is the exact worst case.
- So no single-output function on ≤ 5 variables has MC ≥ n. A seed function with MC ≥ number of variables first appears at n = 6 (`mc-calik-2018-six-variables.md`).
- **Testing the fresh-variable lemma (item (a)).** The MC tables for ≤ 5 variables, together with the 6-variable classification, allow direct verification of (a) for every g on ≤ 5 variables: g·y has ≤ 6 variables.

## Limitations

- Only small n.
- The computer-assisted classification was not checked by Agent D.

## Retrieval

- Title, authors, LightSec 2014 in Istanbul, LNCS 8898, pp. 21–33, DOI, keywords and the main results ("MC of a Boolean function with five variables is at most four"; four-variable functions need at most three AND gates): from WebSearch summaries of NIST, CSRC, DBLP and Springer records.
- ePrint 2015/848: mentioned in one search summary citing DBLP (journals/iacr/TuranP15); not independently confirmed.
