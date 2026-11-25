# Çalık, Sönmez Turan, Peralta (2020): Boolean functions with multiplicative complexity 3 and 4

| Field | Value |
|---|---|
| Title | Boolean Functions with Multiplicative Complexity 3 and 4 |
| Authors | Çağdaş Çalık, Meltem Sönmez Turan, René Peralta |
| Year | 2020 (ePrint 2019) |
| Venue | Cryptography and Communications 12(5), 935–946 (2020) |
| DOI | 10.1007/s12095-020-00445-z |
| ePrint | IACR ePrint 2019/1364 |
| Group | MC: classification of low-MC functions; dimension bound. Index: `index-multiplicative-complexity.md` |

## Relevant statements (relayed)

1. **Classification.**
   - Identification of the affine equivalence classes of functions with MC 3 and MC 4: **1277 classes with MC 4**.
   - Per a mirror of the abstract, no classes with MC 3 beyond the 24 identified in the authors' earlier 2018 work.
   - Closed formulas for the number of n-variable functions with MC 3 and 4.
2. **Dimension bound.** MC(f) ≥ ⌈dim(f)/2⌉.
   - dim(f) is a "linearity dimension": the number of linear forms on which f essentially depends, modulo affine terms. The exact definition is **unverified**.
   - The bound was seen only on a Chinese-language mirror of the abstract (x-mol).

## Why it matters for NP-FRONTIER

- The dimension bound is easy to see: k AND gates have 2k affine inputs, so modulo affine terms f depends on at most 2k linear forms. Agent D's reading.
- It is capped at ⌈n/2⌉, so it is irrelevant for beating n − 1 (index item (c), observation D5).
- It is useful in small test cases. For example, MC((x_1x_2 + x_3x_4)(x_5x_6 + x_7x_8)) ≥ 4, which is relevant to testing (b).

## Limitations

- The dimension definition and the bound were seen only via a mirror summary.

## Retrieval

- Title, authors, journal, volume, issue, pages, DOI, ePrint 2019/1364, "1277 equivalence classes having MC 4" and the closed-formula statement: from WebSearch summaries of NIST, ePrint, Springer and library records.
- The ⌈dim(f)/2⌉ bound and the "24 classes" remark: from a WebSearch summary of the x-mol mirror. An earlier search summary also mentioned "Calik et al. give a lower bound of ⌈dim(f)/2⌉ for functions with MC 3 and 4".
- The explanation of the bound: Agent D's reasoning.
