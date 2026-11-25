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

## Update, cycle 002 (2026-11-25): retrieved and used

**Retrieved this session:**
- The full abstract, from the CSRC journal page https://csrc.nist.gov/pubs/journal/2020/07/boolean-functions-with-multiplicative-complexity-3/final. It confirms the dimension bound MC(f) ≥ ⌈dim(f)/2⌉, the 24 MC-3 classes, the 1277 MC-4 classes, and the closed formulas.
- Peralta's BFA 2019 talk slides (CSRC presentation "mc3and4", PDF).
  - Dimension definition: dim(f) = n − d_l(f), where d_l is the linearity dimension. This matches our dim in PNE-001-level4.md.
  - Proof sketch of the bound: 2k linear inputs.
  - Class counts by dimension.
  - The counting formulas.
- The class lists, from `data/mc_dim` in github.com/usnistgov/circuits (cloned). The counts match the paper: MC 3 has 3 + 14 + 7 = 24 classes; MC 4 has 26 + 888 + 321 + 42 = 1277.

**Not retrieved:** the paper PDF (ePrint 2019/1364 is behind a Cloudflare challenge).

**Checked against our data** (EXP-007, EXP-015):
- The slide's MC-1 formula 2·C(2^n,3) and MC-2 formula reproduce our counts exactly: 9,920 and 1,801,472 at n = 5; 1,120 and 31,616 at n = 4.
- The slide's MC-3 formula, with s4 = 32768, s5 = 1576479744 and s6 = 183894007808, does **not** reproduce our count at n = 5. Ours: 777,759,744 MC-3 functions, of which 775,728,128 have dimension 5.
- Our table nevertheless agrees with the class data on all 48 five-variable classes. The discrepancy is unresolved; possibly the normalization of s_d differs from what we assume.

**Used in cycle 002:**
- Lemma 22(a) is their bound.
- Lemma 26 combined with their complete MC-4 class list gives an independent proof route for Theorem 25 (level 4 of PNE-001 for all n; 186 affine hyperplane restrictions, all harmless).
- Their 6-variable classification independently confirms PNE-001 for every 5-variable g.
