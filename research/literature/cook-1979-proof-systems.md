# Cook, Reckhow (1979): The relative efficiency of propositional proof systems

| Field | Value |
|---|---|
| Title | The Relative Efficiency of Propositional Proof Systems |
| Authors | Stephen A. Cook, Robert A. Reckhow |
| Year | 1979 |
| Venue | Journal of Symbolic Logic 44(1):36–50, March 1979 (Association for Symbolic Logic) |
| DOI | 10.2307/2273702 |
| URL | Author PDF: https://www.cs.utoronto.ca/~sacook/homepage/cook_reckhow.pdf |
| Earlier versions | Parts appeared in a 1974 conference paper and in Reckhow's 1976 PhD thesis (per the paper's own text, via WebSearch summary) |
| Group | No-go framework for candidate polynomial-time SAT algorithms |

## Definitions

- **TAUT:** the set of propositional tautologies. It is coNP-complete. Dually, UNSAT is coNP-complete.
- **Propositional proof system (Cook–Reckhow):** a polynomial-time computable function f from strings **onto** TAUT. A string π with f(π) = τ is an f-proof of τ.
  - Equivalently: a polynomial-time verifier V(τ, π) that is sound (accepts only tautologies) and complete (every tautology has some accepted π).
- **Polynomially bounded system:** there is a polynomial p such that every τ ∈ TAUT has an f-proof of length ≤ p(|τ|).
- **p-simulation:** g p-simulates f if a polynomial-time function maps f-proofs to g-proofs of the same tautology.

## Relevant theorem

**Theorem.** NP = coNP if and only if there exists a polynomially bounded propositional proof system.

Proof (standard, recalled):
- (⇐) Guess a proof of length ≤ p(|τ|) and run f. This puts TAUT ∈ NP, hence coNP ⊆ NP and NP = coNP.
- (⇒) If TAUT ∈ NP via verifier V, let f(⟨τ, w⟩) = τ when V accepts, and a fixed tautology otherwise.

**Other content (abstract level).**
- Frege (Hilbert-style) systems and natural deduction systems are equivalent up to a polynomial in minimum proof length.
- The paper introduces **extended Frege** (abbreviations of formulas).
- The pigeonhole tautologies used by Haken 1985 were introduced here. Recalled, unverified: they are shown to have polynomial-size extended Frege proofs.

## What it rules out or limits

**Basic no-go mechanism (direct consequence of the definitions).** Any correct deterministic SAT algorithm A defines a proof system for UNSAT: the proof of unsatisfiability of F is the transcript of A's run on F.
- If A runs in polynomial time, this proof system is polynomially bounded. So P = NP implies NP = coNP, which implies a polynomially bounded proof system exists.
- More usefully, suppose A's runs on unsatisfiable inputs can be converted in polynomial time into refutations in a concrete proof system S. Then on every family of unsatisfiable formulas, **A's running time is at least the minimum S-refutation size, up to a polynomial**. Known S-lower bounds become runtime lower bounds for A.

Known simulations (recalled unless noted):
- DPLL with any branching rule yields tree-like resolution refutations.
- CDCL and general resolution are polynomially equivalent:
  - The direction needed for no-go arguments: CDCL runs on unsatisfiable inputs yield resolution refutations of comparable size. Standard, recalled.
  - The converse: CDCL with restarts p-simulates general resolution. Pipatsrisawat–Darwiche, "On the power of clause-learning SAT solvers as resolution engines", Artificial Intelligence 175(2):512–525, 2011, DOI 10.1016/j.artint.2010.10.002; bibliographic data and this p-simulation claim confirmed via WebSearch summary.
- k-consistency corresponds to width-k resolution (`atserias-2008-width-pebble-games.md`).
- Low-degree SoS/Lasserre relaxations correspond to degree-bounded Positivstellensatz/SoS proofs (`grigoriev-2001-sos-parity.md`, `schoenebeck-2008-lasserre-ksat.md`).

**P ≠ NP side (the "Cook program").** Superpolynomial lower bounds for **every** propositional proof system would prove NP ≠ coNP, hence P ≠ NP.

## Why it matters for NP-FRONTIER

This is the master framework for falsifying candidate polynomial-time SAT algorithms:
1. Identify the proof system implicitly used by the algorithm on unsatisfiable instances.
2. Look up the known hard families for that system (PHP, Tseitin on expanders, random 3-CNF, etc.).
3. Run or analyze the algorithm on them.

## Limitations

- Lower bounds for specific proof systems do not imply P ≠ NP. Superpolynomial lower bounds for Frege or extended Frege are open (recalled).
- An algorithm that does not correspond to any known weak proof system yields no immediate no-go. Its "proof system" may be strong (e.g. extended Frege-like) or unknown. Then the no-go method only tells the reviewer where to look.
- The equivalence concerns the existence of short proofs, not the efficient finding of them (automatability). Automatability results are a separate literature, not covered here.

## Retrieval

- Title, authors, JSL 44(1):36–50 (March 1979), DOI 10.2307/2273702 and the author-hosted PDF: confirmed via WebSearch (Cambridge Core, Crossref API, researchr, bibbase; result summaries).
- Abstract-level content (Frege ≡ natural deduction up to a polynomial; extended Frege introduced; earlier 1974 conference paper and Reckhow thesis): confirmed via WebSearch summary of the paper text.
- "NP = coNP iff there is a polynomially bounded propositional proof system": confirmed via WebSearch summary of a secondary source.
- PHP formulas introduced by Cook–Reckhow: confirmed via the WebSearch summary of Haken's abstract.
- Formal definitions as written above and the proof sketch: standard, recalled.
- Pipatsrisawat–Darwiche bibliographic data and claim: confirmed via WebSearch summary (MaRDI, Scilit, researchr).
- DPLL ↔ tree-like resolution: recalled.
