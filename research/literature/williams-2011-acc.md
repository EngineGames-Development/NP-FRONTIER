# Williams (2011/2014): Non-uniform ACC circuit lower bounds

| Field | Value |
|---|---|
| Title | Non-uniform ACC Circuit Lower Bounds (journal title: "Nonuniform ACC Circuit Lower Bounds") |
| Author | Ryan Williams |
| Year | 2011 (conference); 2014 (journal) |
| Venues | 26th IEEE Conference on Computational Complexity (CCC 2011); page numbers not confirmed. Journal of the ACM 61(1), Article 2, pp. 2:1–2:32, January 2014 |
| DOI | 10.1145/2559903 (journal) |
| Preprint | ECCC TR11-017 |
| Group | Circuit lower bound frontier (restricted model: ACC0) |

## Definitions

- **ACC0:** families of constant-depth, polynomial-size circuits with unbounded fan-in AND, OR, NOT and MOD_m gates, where m > 1 is an arbitrary fixed constant. ACC0 = ∪_m AC0[m].
- **NEXP** = NTIME[2^{n^{O(1)}}].
- **E^NP** = DTIME[2^{O(n)}] with an NP oracle.

## Relevant theorems

Confirmed at abstract level.
1. **NEXP ⊄ ACC0.** NEXP does not have non-uniform ACC0 circuits of polynomial size. The size bound extends to quasi-polynomial size and some less natural functions.
2. **E^NP ⊄ ACC0 of size 2^{n^{o(1)}}.** E^NP does not have non-uniform ACC0 circuits of size 2^{n^{o(1)}}.

## Method: the "algorithmic method" (abstract level, details recalled)

Strategy (confirmed at abstract level): design faster-than-brute-force satisfiability algorithms for ACC0 circuits, and prove that such algorithms imply the lower bounds.

Ingredients (recalled, unverified):
- **ACC0-SAT algorithm.** For each depth d and modulus m there is ε > 0 such that satisfiability of n-input ACC0 circuits of depth d and size 2^{n^ε} is decidable in time 2^{n − n^ε}. It uses a quasi-polynomial-size SYM∘AND representation of ACC0 (Yao; Beigel–Tarui) and fast rectangular matrix multiplication.
- **Algorithms-to-lower-bounds connection** (Williams STOC 2010 / SIAM J. Comput. 2013). A SAT algorithm for C-circuits that beats 2^n by a superpolynomial factor implies NEXP ⊄ C. The proof combines the nondeterministic time hierarchy, succinct reductions, and the easy-witness lemma of Impagliazzo–Kabanets–Wigderson.

## Barrier status (secondary sources)

- **Relativization and algebrization.** Aaronson's blog (2010) states it crosses both: one can build an oracle A with NEXP^A ⊆ ACC^A.
- **Natural proofs.** The heuristic explanation is that the proof is non-constructive, because the ACC-SAT algorithm is only mildly faster than brute force. A later paper (via WebSearch summary) notes that it is "not completely settled" whether the proof is truly non-naturalizing.
- **Williams 2016** ("Natural Proofs Versus Derandomization", SIAM J. Comput. 45(2):497–529). NEXP ⊄ C is **equivalent** to the existence of a polynomial-time **constructive** property useful against C, without largeness.

## What it rules out or limits

This is a frontier result, not a no-go. It marks the state of the art for restricted circuit classes:
- The best lower bounds against ACC0 are for very large uniform classes: NEXP, and later NQP (`murray-2018-nqp-acc.md`). They are **not** for NP.
- Whether NP ⊄ ACC0 is open, and NEXP vs TC0 is open (recalled). A hypothesis that implies NP ⊄ ACC0 or NEXP ⊄ TC0 as a corollary is claiming an open result and must be audited accordingly.

## Why it matters for NP-FRONTIER

- It is the main example of a lower-bound technique that evades relativization and algebrization, and is at least not obviously natural. Its ingredient is the **algorithms-to-lower-bounds connection**.
- The route to NP ⊄ P/poly through this connection would need, at minimum, non-trivial SAT algorithms for general polynomial-size circuits. Even that gives NEXP ⊄ P/poly, not NP ⊄ P/poly, so it does not imply P ≠ NP.
- For P = NP hunters: the same connection says that very fast algorithms for Circuit-SAT imply circuit lower bounds. A claimed polynomial-time Circuit-SAT algorithm therefore also implies NEXP ⊄ P/poly. That is consistent but useful as a sanity check on claimed algorithmic speedups.

## Limitations

- The model is ACC0, constant depth; the lower bound is for NEXP (later NQP), not NP.
- Extensions to stronger models (ACC0∘THR, etc.) exist but remain far from P/poly.

## Retrieval

- J. ACM 61(1), Article 2, pp. 2:1–2:32 (2014), DOI 10.1145/2559903: confirmed via WebSearch (DOI page as cited in Wikipedia; reference list of a Springer paper). The publication date January 2014 is from the ACM listing as summarized by WebSearch.
- CCC 2011: confirmed via WebSearch summary (UCI seminar page).
- ECCC TR11-017: seen as a URL in WebSearch results.
- Theorem statements (NEXP: polynomial and quasi-polynomial size; E^NP: 2^{n^{o(1)}}) and the "SAT algorithms imply lower bounds" strategy: confirmed via WebSearch summary of the ACM abstract.
- ACC definition: confirmed via WebSearch summary of the author's PDF. That PDF's header is inconsistent (it shows another paper's citation), so it was not used for bibliographic data.
- SAT-algorithm parameters and proof ingredients: recalled, unverified.
- Barrier commentary: from Aaronson's blog and the Williams 2016 abstract, via WebSearch summaries.
