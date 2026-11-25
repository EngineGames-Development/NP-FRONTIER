# Boyar, Find, Peralta (2013/2016): Four measures of nonlinearity / On various nonlinearity measures for Boolean functions

| Field | Value |
|---|---|
| Title | Four Measures of Nonlinearity (conference); On various nonlinearity measures for Boolean functions (journal) |
| Authors | Joan Boyar, Magnus Gausdal Find, René Peralta |
| Year | 2013 (conference); 2016 (journal) |
| Venue | CIAC 2013, LNCS 7878, pp. 61–72 (DOI 10.1007/978-3-642-38233-8_6). Journal: Cryptography and Communications (2016), DOI 10.1007/s12095-015-0150-9 |
| ePrint | IACR ePrint 2013/633 |
| Group | MC vs other nonlinearity measures. Index: `index-multiplicative-complexity.md` |

## Relevant statements (abstract level)

1. **Incomparability.** The journal version shows that six common measures are pairwise incomparable: nonlinearity, algebraic degree, annihilator immunity, algebraic thickness, normality and multiplicative complexity. The conference version treats four of them.
2. **Collision-free functions.** Both versions give a lower bound on the MC of collision-free functions. The exact bound was not seen.
3. **Nonlinearity versus MC.** Recalled by Agent D, **not confirmed** by any snippet: if MC(f) = M then nl(f) ≤ 2^{n−1} − 2^{n−M−1}.
   - With nl ≤ 2^{n−1} − 2^{n/2−1} (bent functions), this gives MC ≥ n/2 at best.

## Why it matters for NP-FRONTIER

- Index item (c), observation D5: lower bounds on MC via nonlinearity are capped around n/2 for single-output functions, if item 3 is right.
- Item 1 shows that MC is a genuinely different measure from degree. Degree-based arguments cannot capture MC in general.

## Limitations

- Item 3 is unconfirmed.
- The collision-free bound was not seen.

## Retrieval

- Titles, authors, CIAC 2013, LNCS 7878, pp. 61–72, conference DOI, journal DOI, ePrint 2013/633 and items 1–2: from WebSearch summaries of NIST, CSRC, ePrint and Springer records.
- Item 3: recalled, unverified.
