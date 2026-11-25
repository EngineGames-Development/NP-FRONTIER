# Boyar, Peralta, Pochuev (2000): On the multiplicative complexity of Boolean functions over the basis (∧, ⊕, 1)

| Field | Value |
|---|---|
| Title | On the multiplicative complexity of Boolean functions over the basis (∧, ⊕, 1) |
| Authors | Joan Boyar, René Peralta, Denis Pochuev |
| Year | 2000 |
| Venue | Theoretical Computer Science 235(1), 43–57 |
| DOI | 10.1016/S0304-3975(99)00182-6 |
| Group | MC: generic (worst-case / random-function) bounds. Index: `index-multiplicative-complexity.md` |

## Relevant results (relayed by search summaries; full text not seen)

1. **Constructive upper bound for every n-variable function, n even.**
   - The snippet renders it as "c∧(f) = 2^(n/2)+1−n/2−2", which is ambiguous.
   - Agent D reads it as **MC(f) ≤ 2^{n/2+1} − n/2 − 2**. This reading is from memory and **unverified**.
2. **Random functions.** The MC of a random n-variable function is at least **2^{n/2} − O(n)** with high probability. This is a counting argument and is non-explicit.
3. **Separation.** There is an exponential-factor separation between worst-case Boolean circuit complexity, which is Θ(2^n/n), and worst-case MC.
4. **Counting bound.** The paper bounds the number of n-variable functions computable with k AND gates.
   - Sönmez Turan (2022) reports that this bound shows the existence of **8-variable functions with MC > 7**.
   - NIST materials relay the bound as "at most 2^{k²+2k+2kn+n+1} functions".
   - **Caution:** with n = 8 and k = 8, that formula gives 2^{217} < 2^{256}, which would already imply MC > 8 for some 8-variable function. The relayed formula and the relayed conclusion are therefore not mutually consistent. Check the PDF before using either number.
5. **Symmetric functions.** The paper also gives a construction for symmetric functions. The snippet formula is garbled, so the bound is **unverified**. Agent D recalls a bound of the form n + O(√n), also unverified.

## Why it matters for NP-FRONTIER

- Almost all functions have MC far above n, but no explicit function is known to exceed n − 1 for a single output. See index item (c).
- **Observation D2 in the index** uses item 2. Seeds h on m = log log n variables with MC(h) ≥ 2^{m/2} − O(m) can be found by exhaustive search in poly(n) time. A general AND-direct-sum theorem for MC would then give explicit superlinear lower bounds.
- Item 4 supplies the non-constructive existence statements M(8) ≥ 8 (and maybe more) used in the "maximum MC" literature.

## Limitations

- All existence results here are non-constructive.
- The exact constants and formulas need the full text.

## Retrieval

- Title, authors, journal, volume, issue, pages and DOI: from WebSearch summaries (researchr BibTeX record, library catalog record, NIST page).
- Item 3 and the definition sentence: quoted fragments in a WebSearch summary of the abstract.
- Item 1: from a garbled listing snippet; the reading is from memory.
- Item 2: from a WebSearch summary of NIST's 2022 BFA talk slides (Sönmez Turan).
- Item 4: from WebSearch summaries of ePrint 2022/1077 and NIST pages. The inconsistency was computed by Agent D.
- Item 5: garbled snippet; the recalled form is unverified.
