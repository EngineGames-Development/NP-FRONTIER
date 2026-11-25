# Çalık, Sönmez Turan, Peralta (2018): The multiplicative complexity of 6-variable Boolean functions

| Field | Value |
|---|---|
| Title | The Multiplicative Complexity of 6-variable Boolean Functions |
| Authors | Çağdaş Çalık, Meltem Sönmez Turan, René Peralta |
| Year | 2018 (ePrint January 2018; journal online 2018, NIST lists 2018/04); journal issue 2019 |
| Venue | Cryptography and Communications 11(1), 93–107 (2019) |
| DOI | 10.1007/s12095-018-0297-2 |
| ePrint | IACR ePrint 2018/002 (CC BY) |
| Related talk | NIST presentation "mc6bits" (2017) and slides at BFA 2017 |
| Group | MC: exact values for small n. Index: `index-multiplicative-complexity.md` |

## Relevant theorems (abstract level, relayed)

1. **Upper bound.** Every 6-variable Boolean function can be implemented with at most 6 AND gates.
2. **Exact maximum.** The paper exhibits **specific 6-variable functions with MC exactly 6**. Hence **M(6) = 6**, the first n with M(n) ≥ n.
3. **Full classification.** The authors compute the MC of all **150,357** affine equivalence classes of 6-variable functions. The method analyzes circuits with a fixed number of AND gates and uses affine equivalence.
4. **Context stated in the abstract.**
   - Earlier work gives M(n) ≤ n − 1 for n ≤ 5.
   - "A counting argument shows that for n ≥ 7 there are functions needing at least n AND gates."

**Explicit MC-6 functions:** the ANF or truth tables of the 6-variable functions with MC 6 were **NOT visible** in any search snippet. They must be taken from the paper (ePrint 2018/002) or from NIST data.

**Unverified detail:** a search summary of the BFA 2017 slides says that 149,426 of the 150,357 classes are generated with at most 5 AND gates. If correct, 931 classes have MC 6 (Agent D's arithmetic). The slides reportedly print the class count as 150,537, which is presumably a typo.

## Why it matters for NP-FRONTIER

- The explicit MC-6 functions g6 are the natural **seeds** for index item (c).
  - If the fresh-variable lemma (a) holds, f_n = g6(x_1..x_6)·x_7⋯x_n has MC exactly n (index observation D1).
  - If the AND-direct sum (b) held for copies of g6, AND-ing k copies would give MC 7k − 1 = (7/6)n − 1 (index observation D2').
- **Checking (a) directly.** For every g on ≤ 5 variables, g·y is a 6-variable function whose MC is in this classification. So (a) can be checked for all g with ≤ 5 variables by an affine-class lookup.
- **Checking (a) at seven variables.** MC(g6·x_7) = 7 for an explicit g6 would give the **first explicit 7-variable function with MC 7**. M(7) ≥ 7 is otherwise known only non-constructively (`mc-codish-2015-six-gates.md`). Testable with SAT-based exact methods (`mc-soeken-2020-sat.md`).
- **Evidence on (a).** The abstract derives n ≥ 7 existence by counting, not by a fresh-variable argument from M(6) = 6. This is weak evidence that (a) was not an available tool.

## Limitations

- Computer-assisted; not independently checked by Agent D.
- The explicit functions were not retrieved.

## Retrieval

- Title, authors, journal, volume, issue, pages, DOI, ePrint number and abstract statements (items 1–4, including "150357"): from multiple WebSearch summaries (ePrint 2018/002 page, CSRC/NIST publication pages, library records).
- 2017 slides details (149,426 / 150,537): from a WebSearch summary of the BFA 2017 slides PDF (org.uib.no); unverified.
- Absence of explicit functions in snippets: two targeted searches (for ANF and for hexadecimal truth tables) returned none.
