# Boyar, Peralta (2008): Tight bounds for the multiplicative complexity of symmetric functions

| Field | Value |
|---|---|
| Title | Tight bounds for the multiplicative complexity of symmetric functions |
| Authors | Joan Boyar, René Peralta |
| Year | 2008 |
| Venue | Theoretical Computer Science 396, 223–246 |
| DOI | 10.1016/j.tcs.2008.01.030 |
| Earlier version | "The Exact Multiplicative Complexity of the Hamming Weight Function", LATIN 2006 (relayed; venue details unverified) |
| Group | MC: exact bounds for explicit functions. Index: `index-multiplicative-complexity.md` |

## Relevant theorems (relayed)

1. **Hamming weight.** The vector-valued function that outputs the binary representation of the number of ones among n input bits has MC **exactly n − H_N(n)**. Here H_N(n) is the number of ones in the binary representation of n.
2. **Sierpinski's gasket.** The paper relates the complexities of basic symmetric functions to the Sierpinski gasket fractal. The exact statements were **not seen**.
3. **Exact values.** It gives exact values for several classes of symmetric functions. Two questions it left open, for n = 8, k = 4, were answered by Brandão–Çalık–Sönmez Turan–Peralta (2019): both Σ^8_4 and E^8_4 have MC 6. See `mc-brandao-2019-symmetric-twin-variables.md`.

## Why it matters for NP-FRONTIER

- These are explicit, exactly determined MC values, but all are below n. They do not bear on getting MC ≥ n for an explicit single-output function.
- The lower-bound techniques for symmetric functions are a source of methods that go beyond the plain degree bound for multi-output functions.
- Symmetric functions are unlikely to give single-output bounds well above n. Agent D recalls, unverified, that all symmetric functions have MC ≤ n + O(√n).

## Limitations

- The Hamming-weight result is vector-valued, with about log n outputs.
- Statements of the single-output (Σ^n_k, E^n_k) bounds were not seen.

## Retrieval

- Title, authors, venue, volume, pages and DOI: from WebSearch summaries (NIST record, CSRC publication page, author's page imada.sdu.dk/u/joan/tcs08.html).
- Item 1: from WebSearch summaries of the author's page and the NIST "exact multiplicative complexity hamming weight function" page.
- Item 2: from a WebSearch summary of the CSRC page.
- Item 3: from a WebSearch summary of the 2019 Brandão et al. abstract.
- The LATIN 2006 version: from a WebSearch summary of the NIST publication page. Venue details beyond "LATIN 2006" are unverified.
- The n + O(√n) remark: recalled, unverified.
