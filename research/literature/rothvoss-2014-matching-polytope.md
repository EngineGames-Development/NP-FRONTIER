# Rothvoss (2014): The matching polytope has exponential extension complexity

| Field | Value |
|---|---|
| Title | The Matching Polytope has Exponential Extension Complexity |
| Author | Thomas Rothvoss (also written Rothvoß) |
| Year | 2014 (conference); 2017 (journal) |
| Venues | 46th ACM STOC (New York, May 31–June 3, 2014), pp. 263–272, DOI 10.1145/2591796.2591834. Journal of the ACM 64(6), 2017, DOI 10.1145/3127497; pages 1–19 per the CiNii record, article number **not confirmed** |
| arXiv | 1311.2369 (first posted November 2013; last revised March 2017 per the listing summary) |
| Group | No-go for candidate polynomial-time algorithms (compact LP formulations) |

## Relevant theorem

Abstract level, confirmed.
1. **Matching.** The extension complexity of the **perfect matching polytope** of the complete n-node graph is **2^{Ω(n)}**. No polynomial-size extended formulation exists.
2. **TSP corollary.** Via a known reduction, the extension complexity of the **TSP polytope** is 2^{Ω(n)}, improving the earlier 2^{Ω(√n)} (`fiorini-2015-extension-complexity.md`).

**Method (recalled, unverified).** Lower-bound the nonnegative rank of the slack matrix, restricted to odd-set inequalities × perfect matchings, by a rectangle-corruption ("hyperplane separation") argument in the style of Razborov's disjointness bound. Rectangle covering alone is insufficient for matching.

## What it rules out or limits

1. **No compact LP for matching or TSP.** Compact LP extended formulations of the perfect matching polytope are impossible, and those of the TSP polytope are pushed to 2^{Ω(n)}.
2. **Extension complexity is not a proxy for NP-hardness.** Perfect matching is solvable in polynomial time (Edmonds), yet its polytope has exponential extension complexity. Consequences:
   - LP-extension lower bounds are **not evidence for P ≠ NP**;
   - LP extended formulations cannot capture all of P;
   - Edmonds' algorithm works through a separation oracle over exponentially many constraints, not a compact extension.

## Why it matters for NP-FRONTIER

- **P = NP side:** refutes "write a polynomial-size LP for TSP via a matching-polytope gadget" style constructions.
- **P ≠ NP side:** shows that no P ≠ NP argument can be based on "NP-hard polytopes need exponential extended formulations", since easy polytopes do too.

## Limitations

- Exact extended formulations only.
- Approximate versions: a related result, arXiv 1403.6710 "The matching polytope does not admit fully-polynomial size relaxation schemes" (title seen via WebSearch; authors recalled as G. Braun and S. Pokutta, unverified), is not reviewed here.
- SDP extension complexity of the matching polytope is not addressed.

## Retrieval

- STOC 2014 pages 263–272 and DOI, JACM 64(6) (2017) with DOI 10.1145/3127497 and CiNii pages 1–19, and arXiv 1311.2369 with revision history: confirmed via WebSearch (researchr BibTeX, CiNii record, arXiv listing; result summaries).
- Statements 1 and 2, including "improves the lower bound on the extension complexity for the TSP polytope from 2^{Ω(√n)} to 2^{Ω(n)}": confirmed via WebSearch summary of the abstract.
- Proof method: recalled, unverified.
- Edmonds/separation-oracle remark: standard background, recalled.
