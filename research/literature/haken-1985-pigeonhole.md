# Haken (1985): The intractability of resolution

| Field | Value |
|---|---|
| Title | The Intractability of Resolution |
| Author | Armin Haken |
| Year | 1985 |
| Venue | Theoretical Computer Science 39(2–3):297–308, 1985 |
| DOI | 10.1016/0304-3975(85)90144-6 |
| Group | No-go for candidate polynomial-time SAT algorithms (resolution-based) |

## Definitions

- **Resolution:** from clauses C ∨ x and D ∨ ¬x, derive C ∨ D. A refutation of a CNF F derives the empty clause.
  - Size = number of clauses in the derivation.
  - Tree-like resolution requires each derived clause to be used at most once.
- **Pigeonhole formulas ¬PHP^{m}_{n}** (m pigeons, n holes, m > n), standard CNF encoding (recalled):
  - Variables p_{i,j}: "pigeon i sits in hole j".
  - Pigeon clauses ∨_{j∈[n]} p_{i,j} for each i ∈ [m].
  - Hole clauses ¬p_{i,j} ∨ ¬p_{i',j} for each i ≠ i' and j ∈ [n].

## Relevant theorem

**Abstract-level statement (confirmed).** For infinitely many DNF tautologies ξ, the length of the shortest resolution proof of ξ cannot be bounded by any polynomial in the length of ξ.
- The tautologies are the pigeonhole formulas introduced by Cook and Reckhow (1979).
- Extended resolution does have polynomial-length proofs of them.

**Quantitative form (recalled, unverified).** Every resolution refutation of ¬PHP^{n+1}_{n} has size 2^{Ω(n)}. The formula has O(n³) size, so the bound is 2^{Ω(N^{1/3})} in terms of the formula size N.

**Context (via WebSearch summary of a MaRDI review).**
- Tseitin (1970) had proved exponential bounds for **regular** resolution. General resolution remained open until this paper.
- Buss and Turán (1988) extended the result to generalized pigeonhole principles.

## What it rules out or limits

**Every SAT algorithm whose runs on unsatisfiable inputs yield resolution refutations needs exponential time on ¬PHP^{n+1}_{n}.** This covers:
- DPLL with any branching heuristic;
- CDCL with any learning or restart policy (CDCL is polynomially equivalent to resolution; see `cook-1979-proof-systems.md`);
- Davis–Putnam variable elimination;
- "local" clause-reasoning procedures.

Contrast (recalled, unverified): PHP has polynomial-size proofs in extended resolution (stated in Haken's abstract), in Frege, and in cutting planes. A P = NP candidate must therefore at least reason about counting or extension variables; resolution-like reasoning is refuted.

## Why it matters for NP-FRONTIER

- PHP is the first test instance for any proposed SAT algorithm.
- It isolates the counting deficiency of clause-based reasoning.
- It also shows that hardness for a weak system says nothing about NP-hardness per se: the PHP family is trivially unsatisfiable by counting.

## Limitations

- Lower bound only for resolution and systems it p-simulates, not for stronger proof systems.
- It does not show that PHP is hard for all algorithms. PHP is easy for counting-based algorithms.

## Retrieval

- Author, title, TCS 39(2–3):297–308 (1985) and DOI: confirmed via WebSearch (Utah TCS 1985 bibliography, Crossref API, MaRDI portal; result summaries).
- Abstract-level statement, including the extended-resolution sentence and the Cook–Reckhow origin of the formulas: confirmed via WebSearch summary of the abstract.
- Tseitin 1970 and Buss–Turán 1988 context: from the WebSearch summary of the MaRDI review and related bibliographic results. Their bibliographic data were not separately confirmed.
- The 2^{Ω(n)} form and the CNF encoding: recalled, unverified.
- The simulations (DPLL, CDCL, Frege, cutting planes): recalled. That CDCL runs yield resolution refutations, the direction used here, is standard and recalled. The Pipatsrisawat–Darwiche search confirmed only the converse direction (CDCL p-simulates resolution; see the Cook–Reckhow record).
