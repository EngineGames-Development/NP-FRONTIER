# Find (2014): On the complexity of computing two nonlinearity measures

| Field | Value |
|---|---|
| Title | On the Complexity of Computing Two Nonlinearity Measures |
| Authors | Magnus Gausdal Find |
| Year | 2014 |
| Venue | CSR 2014 (Computer Science in Russia), LNCS 8476 (Springer chapter DOI 10.1007/978-3-319-06686-8_13) |
| arXiv | 1403.0417 |
| Group | MC: computational hardness of computing MC. Index: `index-multiplicative-complexity.md` |

## Relevant statements (abstract level, relayed)

1. **Truth-table input.** If one-way functions exist, no algorithm computes the MC of an n-variable function from its truth table (length 2^n) in time 2^{O(n)}. The same assumption also rules out good approximations.
   - This is the Springer abstract's wording. The arXiv introduction states the assumption as the existence of pseudorandom function families.
2. **Circuit input.** For functions given as circuits, MC is in the second level of the polynomial hierarchy, while nonlinearity is #P-hard.
3. **Contrast.** Nonlinearity from a truth table is computable in almost linear time via the fast Walsh transform.

## Why it matters for NP-FRONTIER

- Experimental expectations: exact MC computation is expected to be inherently expensive. Any experiment testing (a) or (b) must stay at small n or use special structure.
- An algorithm computing MC from truth tables in time 2^{O(n)} would contradict standard cryptographic assumptions. This is relevant if an agent proposes efficient MC-computing procedures.

## Limitations

- Abstract level only.
- The exact hardness assumption differs between versions.

## Retrieval

- Title, author, arXiv ID, CSR 2014, LNCS 8476 and Springer DOI: from WebSearch summaries of arXiv, ar5iv, CORE and Springer.
- Items 1–3: from the same summaries, which quote the Springer abstract and the arXiv introduction. The assumption discrepancy was reported by the summary.
