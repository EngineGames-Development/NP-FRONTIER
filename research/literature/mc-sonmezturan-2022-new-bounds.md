# Sönmez Turan (2022): New bounds on the multiplicative complexity of Boolean functions

| Field | Value |
|---|---|
| Title | New Bounds on the Multiplicative Complexity of Boolean Functions |
| Authors | Meltem Sönmez Turan (NIST) |
| Year | 2022 (ePrint revised August 2022) |
| Venue | IACR ePrint 2022/1077. Presented at the 7th International Workshop on Boolean Functions and their Applications (BFA 2022), Balestrand, Norway, September 11–16, 2022. Reported to appear in a *Cryptography and Communications* special issue (details **unverified**) |
| Slides | csrc.nist.gov, "20220913-BFA-2022-New-Bounds-MC-Bool-Funcs.pdf" |
| Group | MC: counting bounds and maximum MC M(n). Index: `index-multiplicative-complexity.md` |

## Relevant statements (relayed)

1. **Improved counting bound.** The paper improves the Boyar et al. (2000) upper bound on the number of n-variable functions computable with k AND gates.
   - A NIST page describes the improvement as a factor of roughly 2^{3k}/3^k; the snippet was garbled, so this is **unverified**.
2. **Maximum MC.** The paper gives new bounds on M(n), the maximum MC of n-variable functions, in a table for n = 6, …, 16. The table values were **not visible**.
3. **Context in the abstract.** The Boyar et al. bound shows the existence of an 8-variable function with MC > 7.
4. **From the slides.** The best known upper bound on M(7) is **13**.

## Why it matters for NP-FRONTIER

- Index item (c): known existence results for M(n) ≥ n are non-constructive. M(7) ∈ [7, 13] per Codish et al. and these slides.
- Counting bounds of this type are the source of "almost all functions have large MC". They give no explicit witnesses.
- None of the snippets mentions a fresh-variable argument M(n+1) ≥ M(n) + 1, which would follow from index item (a).

## Limitations

- Full text not seen.
- The improvement factor and table values are unverified.

## Retrieval

- Title, author, ePrint number, revision month, BFA 2022 venue, location and dates: from WebSearch summaries of ia.cr/2022/1077, NIST and CSRC pages, and DBLP (journals/iacr/Turan22).
- Items 1–3: from WebSearch summaries of the ePrint abstract and NIST pages.
- Item 4: from a WebSearch summary of the BFA 2022 slides.
- Special issue: from a WebSearch summary of a NIST page; not checked.
