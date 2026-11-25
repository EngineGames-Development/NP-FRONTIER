# Yannakakis (1988/1991): Expressing combinatorial optimization problems by linear programs

| Field | Value |
|---|---|
| Title | Expressing Combinatorial Optimization Problems by Linear Programs |
| Author | Mihalis Yannakakis (AT&T Bell Laboratories at the time) |
| Year | 1991 (journal); 1988 (conference) |
| Venues | Journal of Computer and System Sciences 43, 1991, pp. 441–466 (received December 28, 1988; revised April 1, 1990); issue number recalled as 43(3). Conference version: STOC 1988 (pages not confirmed) |
| URL | PDF copy hosted by S. Jukna: https://web.vu.lt/mif/s.jukna/boolean/Yannakakis1991.pdf |
| Group | No-go for candidate polynomial-time algorithms (symmetric LP formulations); foundation of extension complexity |

## Definitions

- **Slack matrix** of a polytope P = {x : Ax ≤ b} = conv(V):
  - rows are indexed by the inequalities (facets) i;
  - columns by the vertices v_j;
  - entries S_{ij} = b_i − A_i v_j ≥ 0.
- **Nonnegative rank** rank₊(S): the smallest r such that S = U·W with U (rows × r) and W (r × columns) entrywise nonnegative.
- **Symmetric extended formulation** (informal; recalled): an extension whose variables and constraints are permuted consistently by every permutation of the underlying ground set, e.g. the vertex set of K_n for TSP and matching.

## Relevant theorems

1. **Factorization theorem** (confirmed via secondary sources). For a polytope P (dimension ≥ 1), the minimum size of an extended formulation equals **rank₊(S_P)**.
2. **Communication-complexity link** (confirmed via secondary sources).
   - A deterministic protocol of complexity c computing a nonnegative matrix M gives a nonnegative factorization of rank ≤ 2^c.
   - Conversely-type bound: the rectangle covering number of supp(M), equivalently 2^{nondeterministic communication complexity}, is a lower bound on rank₊(M).
   - These are the tools behind every later lower bound (`fiorini-2015-extension-complexity.md`, `rothvoss-2014-matching-polytope.md`).
3. **Symmetric LP lower bound** (confirmed at summary level). The **perfect matching polytope** and the **TSP polytope** cannot be expressed by polynomial-size **symmetric** linear programs. The explicit size bounds were not checked.

## What it rules out or limits

- Polynomial-size **symmetric** LP formulations of TSP and matching are impossible.
- Historical note (recalled, unverified): this answered claimed polynomial-size LP formulations of TSP circulating in the 1980s, which were symmetric. The symmetry assumption was removed for TSP by Fiorini et al. (2012) and for matching by Rothvoss (2014).
- The factorization theorem turns "does a compact LP for P exist?" into a matrix-rank / communication-complexity question. This is how a claimed LP formulation should be audited:
  1. Identify the polytope it claims to project to.
  2. Compare its size to known nonnegative-rank lower bounds.

## Why it matters for NP-FRONTIER

- It is the foundational reference for auditing LP-based P = NP claims.
- Symmetry matters. Kaibel, Pashkovich and Theis ("Symmetry matters for the sizes of extended formulations", arXiv 0911.3712; title seen via WebSearch, content per summary) show symmetric and non-symmetric extension complexity can differ (recalled example: matchings of logarithmic size).
- So the symmetric result alone does **not** refute non-symmetric LPs. Use the FMPTW and Rothvoss results for those.

## Limitations

- The 1991 lower bounds assume symmetry.
- The factorization theorem concerns exact extensions of a fixed polytope.

## Note for the adversarial reviewer

The search also surfaced arXiv 1902.03549, "On modeling hard combinatorial optimization problems as linear programs: Refutations of the 'unconditional impossibility' claims". It disputes the applicability of extension-complexity lower bounds. **Not reviewed.** It is listed only so that the program knows such disputes exist and checks any claim of this kind against the precise theorem statements above.

## Retrieval

- Journal volume 43, pages 441–466, year 1991, received/revised dates and author affiliation: confirmed via WebSearch summary of the journal header in the Jukna-hosted PDF.
- Issue number 3: recalled.
- STOC 1988 conference version: existence confirmed via a later paper citing "Yannakakis [1988, 1991]" (WebSearch summary). Pages not confirmed.
- Factorization theorem and the protocol ⇒ factorization link: confirmed via WebSearch summaries of secondary sources (Wikipedia "Nonnegative rank (linear algebra)"; Toronto communication-complexity lecture notes; arXiv 1105.4127 and 1111.0444).
- Symmetric matching/TSP result: confirmed via WebSearch summary of the abstract and of Kaibel–Pashkovich–Theis.
- Symmetric-formulation definition, historical note and explicit bounds: recalled, unverified.
