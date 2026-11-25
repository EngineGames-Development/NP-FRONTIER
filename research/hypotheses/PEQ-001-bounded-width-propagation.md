# PEQ-001: Bounded-width propagation decides 3-SAT

**Status:** DISPROVED by known theorems (cited; not re-proved in this cycle).

## Formulation
For fixed k, algorithm W_k on a 3-CNF φ derives every resolvent of width ≤ k until saturation (n^{O(k)} time) and answers UNSAT iff the empty clause appears. Hypothesis: there is a constant k such that W_k answers correctly on every 3-CNF. Equivalent forms: k-consistency, or the existential k-pebble game, detects every unsatisfiable 3-CNF. The equivalence between width-k resolution and k-consistency is Atserias–Dalmau 2008 (`research/literature/atserias-2008-width-pebble-games.md`).

## Refutation
Ben-Sasson–Wigderson 2001 (`bensasson-2001-size-width.md`) show that some unsatisfiable 3-CNF families need resolution width Ω(n). Examples are Tseitin formulas on bounded-degree expanders, converted to 3-CNF, and random 3-CNF above the threshold. For every fixed k, W_k therefore fails to refute some unsatisfiable formula. Exponential resolution size lower bounds (Haken 1985; Chvátal–Szemerédi 1988) rule out every resolution-based procedure, of any width, that runs in polynomial time. The theorem statements are confirmed only from abstracts and secondary sources (see each record's Retrieval field).

## General principle extracted (toolkit for future PEQ candidates)
If a candidate algorithm A can be converted, with polynomial overhead, into a refutation of every unsatisfiable input in a proof system S, then A is not polynomial-time whenever S has superpolynomial lower bounds for some family. This holds for resolution, bounded-width resolution, polynomial calculus, cutting planes and sum-of-squares. Cook–Reckhow (`cook-1979-proof-systems.md`): a polynomial-time SAT algorithm gives a polynomially bounded proof system, so it would imply NP = coNP. Every PEQ candidate must therefore name the proof system its unsatisfiability reasoning lives in, and explain why the known lower bounds do not apply.

## Next step
Candidates that are not obviously simulated by a proof system with known lower bounds. Example: propagation combined with 𝔽₂ Gaussian elimination, which relates to resolution over parities, Res(⊕). Literature check needed on the status of general Res(⊕) lower bounds.
