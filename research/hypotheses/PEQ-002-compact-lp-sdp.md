# PEQ-002: A polynomial-size LP or SDP formulation solves an NP-hard problem exactly

**Status:** DISPROVED as an approach, by known theorems (cited; not re-proved in this cycle). Scope is precise and limited; see below.

## Formulation
Hypothesis: for an NP-hard problem such as TSP, max-cut or 3-SAT, there is a polynomial-size linear program whose feasible region projects onto the problem's polytope (an extended formulation), or a polynomial-size semidefinite relaxation that is exact. Many claimed P = NP proofs have this form.

## Refutation
- **LP.** Fiorini–Massar–Pokutta–Tiwary–de Wolf (JACM 2015; `fiorini-2015-extension-complexity.md`): TSP, cut and correlation polytopes have extension complexity 2^{Ω(n^c)} for some c > 0. Exponents are recalled, not confirmed. Yannakakis 1991 (`yannakakis-1991-symmetric-lp.md`) earlier ruled out symmetric formulations.
- **SDP.** Sum-of-squares degree lower bounds for random 3-XOR and 3-SAT (Grigoriev; Schoenebeck; `grigoriev-2001-sos-parity.md`, `schoenebeck-2008-lasserre-ksat.md`). Lee–Raghavendra–Steurer 2015: no polynomial-size SDP relaxation beats 7/8 for MAX-3-SAT (relayed by the literature agent, record in the Fiorini/Grigoriev files).

## Scope (what is not refuted)
- **This is not evidence for P ≠ NP.** Rothvoss 2014 (`rothvoss-2014-matching-polytope.md`): the perfect matching polytope, a problem in P, also has exponential extension complexity. These theorems refute "compact exact LP" algorithms, not polynomial-time algorithms in general.
- Adaptive uses of LP/SDP, such as rounding with branching, are not covered and must be analysed separately. Usually that is done through the proof-system principle in PEQ-001.
