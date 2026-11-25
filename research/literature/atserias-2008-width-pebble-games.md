# Atserias, Dalmau (2008): A combinatorial characterization of resolution width

| Field | Value |
|---|---|
| Title | A Combinatorial Characterization of Resolution Width |
| Authors | Albert Atserias, Víctor Dalmau |
| Year | 2008 (journal) |
| Venue | Journal of Computer and System Sciences 74(3):323–334, May 2008. An earlier conference version (recalled as CCC 2003) is **unverified** |
| DOI | 10.1016/j.jcss.2007.06.025 |
| Preprints | ECCC TR02-035 (2002); ALCOM-FT technical report TR-03-81 |
| Group | No-go for candidate polynomial-time SAT/CSP algorithms (local consistency) |

## Definitions (recalled)

**Existential k-pebble game** (Kolaitis–Vardi), played on relational structures (A, B):
- Spoiler places and removes up to k pebbles on elements of A.
- Duplicator answers each placement with an element of B.
- Duplicator must keep the current pebbled correspondence a partial homomorphism. Spoiler wins if he forces a violation.

For a CNF F, the relevant pair is (structure encoding F, Boolean structure).

## Relevant theorems

**(1) Main characterization.** Confirmed via WebSearch summaries of the paper and of the ECCC report.
- F has a resolution refutation of width ≤ k **iff** Spoiler wins the existential **(k+1)**-pebble game on the structures associated with F.
- Equivalently, F has no width-k refutation iff Duplicator wins that game.
- The precise side condition on k relative to the initial width of F was not checked.

**(2) Link to local consistency.** Kolaitis–Vardi, "A Game-Theoretic Approach to Constraint Satisfaction", AAAI 2000, pp. 175–181 (confirmed via WebSearch summary).
- Strong k-consistency can be established for a CSP instance iff Duplicator wins the existential k-pebble game.
- Combining (1) and (2): on CNF formulas, **the k-consistency / bounded-width algorithm refutes F exactly when F has a resolution refutation of width about k**. The index offset (k vs k+1) depends on the consistency convention; check both papers before quoting exact parameters.

**(3) Further results** (abstract level, confirmed via WebSearch summary):
- For 3-CNFs, minimum refutation clause space ≥ minimum refutation width − 3, solving an open problem.
- A width lower bound for the Dense Linear Order principle, which has polynomial-size resolution refutations. This shows that size and width cannot be related subpolynomially.

## What it rules out or limits

**Every algorithm in the local-consistency family is exactly as strong as bounded-width resolution on CNFs.** The family includes:
- arc consistency, path consistency, (strong) k-consistency for fixed k;
- bounded-width Datalog;
- existential k-pebble-game propagation.

Consequences:
- Each such algorithm runs in n^{O(k)} time and fails to detect unsatisfiability on every family needing width > k: pigeonhole, Tseitin on expanders, random 3-CNF (widths Ω(n) or comparable; see `bensasson-2001-size-width.md`).
- With k growing so as to succeed, the running time becomes superpolynomial.
- **No fixed-level local consistency algorithm solves 3-SAT.**
- Determining the winner of the existential k-pebble game itself has no O(n^{(k−3)/12})-time algorithm (Berkholz, arXiv 1205.0679, via WebSearch summary). So the k-consistency computation cannot be shortcut dramatically.

## Why it matters for NP-FRONTIER

Many "new" polynomial-time SAT/CSP algorithms are propagation schemes in disguise. This record gives the exact test: if the scheme's inferences can be simulated by the existential k-pebble game or by width-k resolution for fixed k, it fails on known families.

## Limitations

- The characterization concerns refutations; it covers procedures that detect unsatisfiability.
- It says nothing about algorithms combining propagation with global steps (Gaussian elimination, counting, SDP).
- Exact parameter offsets must be checked against the original.

## Retrieval

- Title, authors, JCSS 74(3):323–334 (May 2008), DOI 10.1016/j.jcss.2007.06.025, ECCC TR02-035 and ALCOM-FT TR-03-81: confirmed via WebSearch (UPF repository, ECCC page, Aarhus ALCOM-FT page; result summaries). Conference version not confirmed.
- Main characterization with the (k+1)-pebble convention: confirmed via WebSearch summary citing the Karlin-hosted PDF of the paper and the 2002 ECCC report.
- Space ≥ width − 3 and Dense Linear Order results: confirmed via WebSearch summary of the abstract.
- Kolaitis–Vardi AAAI 2000 (pp. 175–181) and the strong k-consistency ⇔ Duplicator-wins equivalence: confirmed via WebSearch summary.
- Berkholz lower bound: confirmed via WebSearch summary of arXiv 1205.0679 (author per summary).
- Game definition: recalled.
