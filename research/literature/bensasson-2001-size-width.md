# Ben-Sasson, Wigderson (2001): Short proofs are narrow — resolution made simple

| Field | Value |
|---|---|
| Title | Short Proofs Are Narrow—Resolution Made Simple |
| Authors | Eli Ben-Sasson, Avi Wigderson |
| Year | 2001 (journal); 1999 (conference) |
| Venues | Journal of the ACM 48(2):149–169, 2001. 31st ACM STOC (1999), pp. 517–526 |
| Preprint | ECCC TR99-022 |
| Group | No-go for candidate polynomial-time SAT algorithms (resolution / bounded-width reasoning) |

## Definitions

- **Width:** w(C) = number of literals in clause C; w(F) = maximum clause width in CNF F.
- **Refutation width:** w(F ⊢ ⊥) = minimum, over resolution refutations of F, of the maximum clause width appearing in the refutation.
- **Refutation size:** S(F) = minimum number of clauses in a resolution refutation; S_T(F) = the same for tree-like refutations.
- n = number of variables.

## Relevant theorems

**(1) Size–width relations.** Stated as cited by later papers; confirmed via WebSearch summaries.
- Tree-like: w(F ⊢ ⊥) ≤ w(F) + log₂ S_T(F). Hence S_T(F) ≥ 2^{w(F⊢⊥) − w(F)}.
- General resolution: w(F ⊢ ⊥) ≤ w(F) + O(√(n · ln S(F))). Hence **S(F) ≥ exp(Ω((w(F ⊢ ⊥) − w(F))² / n))**.
  - Explicit-constant form, as cited by a 2016 paper: log₂ S(F) > (w(F ⊢ ⊥) − w(F))² / (16n).

**(2) Width lower bounds from expansion (recalled).** If every small set of clauses of F is satisfiable and medium-size sets of clauses have large "boundary", then w(F ⊢ ⊥) is large. Boundary = variables occurring in exactly one clause of the set. Applications:
- Tseitin formulas on bounded-degree expanders need width Ω(n), hence size 2^{Ω(n)}.
- Random k-CNFs at constant density need large width, re-deriving Chvátal–Szemerédi-type bounds.
- Pigeonhole-type bounds via a graph-restricted PHP (details recalled, unverified).

**(3)** An exponential separation between tree-like and general resolution (abstract level, confirmed).

**Tseitin formulas (recalled definition).**
- Graph G = (V, E) with charges χ: V → {0,1} such that Σ_v χ(v) is odd.
- One variable x_e per edge; for each v, the parity constraint ⊕_{e∋v} x_e = χ(v), written as 2^{deg(v)−1} clauses.
- The formula is unsatisfiable, since summing all constraints gives 0 = 1.
- It is solvable in polynomial time by Gaussian elimination over F₂.

**Original exponential resolution bound for Tseitin formulas on expanders:** A. Urquhart, "Hard examples for resolution", Journal of the ACM 34(1):209–219, 1987 (confirmed via WebSearch).

## What it rules out or limits

1. **A quantitative criterion for resolution-based algorithms.** Any SAT algorithm whose behaviour on unsatisfiable inputs is simulated by resolution (DPLL, CDCL, clause-learning variants) needs time ≥ exp(Ω((w − w₀)²/n)) on formulas of refutation width w and initial width w₀.
2. **Concrete hard families.**
   - Width Ω(n) for Tseitin on expanders and for random 3-CNF gives 2^{Ω(n)} lower bounds.
   - Tseitin formulas are easy for Gaussian elimination. So resolution-like reasoning fails on instances that are algebraically trivial, and a P = NP candidate must at least subsume both clause reasoning and linear algebra over F₂.
3. **Bounded-width methods.** Bounded-width resolution, which coincides with k-consistency (`atserias-2008-width-pebble-games.md`), cannot refute any family needing width ω(1).

## Why it matters for NP-FRONTIER

- Width is the most usable invariant for testing resolution-based or local-consistency-based SAT procedures: compute or bound the width of the target family.
- Hard families with linear width (Tseitin on expanders, random 3-CNF) are the standard benchmark set.

## Limitations

- **Not tight in all cases.** The general-resolution relation loses a square and a factor n. There are formulas with polynomial-size refutations but width about √n (recalled as Bonet–Galesi, unverified). Atserias–Dalmau 2008 give a related example (dense linear order).
- **System-specific.** Resolution only. The size–width relation fails for some other systems (e.g. many QBF systems, per a WebSearch summary of later work).

## Retrieval

- JACM 48(2):149–169 (2001), STOC 1999 pp. 517–526 and ECCC TR99-022: confirmed via WebSearch (HUJI CRIS records, IAS publication page, bibtex.github.io STOC-1999 entry; result summaries).
- Size–width relations (tree-like: w ≤ w(F) + lg S_T; general: w ≤ w(F) + O(√(n ln S)); explicit form log₂ S > (w − k)²/(16n)): confirmed via WebSearch summaries of later papers quoting BSW (Bonacina STACS 2016; a QBF paper; lecture notes). Not checked against the BSW text.
- Abstract-level claims (unified simple proofs of known exponential lower bounds; tree-like vs general separation): confirmed via WebSearch summary.
- Expansion criterion, its applications, and the Tseitin definition: recalled from memory.
- Urquhart 1987 bibliographic data and the expander/Tseitin result: confirmed via a separate WebSearch (Scilit / ACM listing summaries).
