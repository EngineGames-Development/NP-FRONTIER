# Index: barriers, circuit-lower-bound frontier, and no-go results for SAT algorithms

This is the source-verified map that every P = NP and P ≠ NP hypothesis in NP-FRONTIER must be checked against.
- Compiled by Agent D (literature researcher) on 2026-11-25, using WebSearch only; arxiv.org could not be fetched.
- Each record has a **Retrieval** field. It separates what search results confirmed (bibliographic data, abstract-level statements) from what is recalled from memory and marked unverified.
- No record's theorem statement was checked against the full primary text. Treat precise constants and quantifiers as "to be checked against the original" before using them in a proof.

One line per record: what it rules out or limits.

## 1. Barriers

| Record | Rules out / limits |
|---|---|
| [baker-1975-relativization.md](baker-1975-relativization.md) | Any proof of P ≠ NP or P = NP whose every step holds relative to all oracles: pure simulation/diagonalization, and black-box witness search. |
| [razborov-1997-natural-proofs.md](razborov-1997-natural-proofs.md) | If 2^{n^ε}-hard PRGs exist: any NP ⊄ P/poly proof via a truth-table property that is checkable in poly(2^n) time, holds for a ≥ 2^{−O(n)} fraction of functions, and implies hardness. |
| [aaronson-2009-algebrization.md](aaronson-2009-algebrization.md) | Settling P vs NP (either direction), or even proving NEXP ⊄ P/poly, by relativizing techniques plus arithmetization (low-degree extensions, sum-check, IP/PCP-style machinery). |
| [chen-2020-locality-barrier.md](chen-2020-locality-barrier.md) | Proving hardness-magnification lower bounds (e.g. for MCSP variants) with techniques that also work for circuits with small-fan-in oracle gates. Most known weak-model techniques are of this kind. |

## 2. Circuit lower bound frontier

| Record | Rules out / limits |
|---|---|
| [li-2022-3.1n-lower-bound.md](li-2022-3.1n-lower-bound.md) | Frontier: the best **refereed** explicit lower bound for general (B2) circuits is 3.1n − o(n) (affine dispersers). Any superlinear claim for an explicit function is a major claim. |
| [mishra-2026-3.5n-lower-bound.md](mishra-2026-3.5n-lower-bound.md) | **Unrefereed claim**, ECCC TR26-260 (Oct 2026): 3.5n − o(n) for an explicit function in P. Not verified; still linear. |
| [find-2016-better-than-3n.md](find-2016-better-than-3n.md) | Frontier: (3 + 1/86)n − o(n), the first improvement over Blum's 3n (1984) in more than 30 years. Shows how slowly gate elimination advances. |
| [golovnev-2016-gate-elimination-limits.md](golovnev-2016-gate-elimination-limits.md) | Gate elimination with a bounded number of substitutions per step (or a subadditive measure with up to about N/2 substitutions) cannot prove cn bounds beyond a fixed constant c, let alone superlinear ones. |
| [williams-2011-acc.md](williams-2011-acc.md) | Frontier: NEXP ⊄ ACC0 (poly/quasi-poly size) and E^NP ⊄ ACC0 of size 2^{n^{o(1)}}, via the algorithms-to-lower-bounds method. NP ⊄ ACC0 remains open. |
| [murray-2018-nqp-acc.md](murray-2018-nqp-acc.md) | Frontier: NQP ⊄ ACC0∘THR of size n^{log^k n}; easy witness lemma for NP (witness circuits n^{O(k³)}). NP ⊄ ACC0 still open. |
| [hastad-1986-switching-lemma.md](hastad-1986-switching-lemma.md) | PARITY needs depth-d size exp(Ω(n^{1/(d−1)})), so PARITY ∉ AC0. Random-restriction/switching techniques are natural and fail beyond AC0 (AC0[2], TC0, P/poly). |
| [razborov-1985-monotone-clique.md](razborov-1985-monotone-clique.md) | Polynomial-size **monotone** circuits, and hence monotone algorithms, for CLIQUE. Also shows monotone lower bounds can hold for problems in P (perfect matching), so they do not transfer to general circuits. |
| [alon-1987-monotone-circuits.md](alon-1987-monotone-circuits.md) | Exponential monotone bounds for CLIQUE, even for rough approximation. With Tardos 1988 (exponential monotone/non-monotone gap for a function in P), monotone hardness ≠ general hardness. |

## 3. No-go results for candidate polynomial-time SAT algorithms

| Record | Rules out / limits |
|---|---|
| [cook-1979-proof-systems.md](cook-1979-proof-systems.md) | Framework: NP = coNP iff a polynomially bounded proof system exists. Any SAT algorithm whose UNSAT runs convert to proofs in a system S inherits S's proof-size lower bounds as running-time lower bounds. |
| [haken-1985-pigeonhole.md](haken-1985-pigeonhole.md) | Resolution-based algorithms (DPLL, CDCL, DP elimination): ¬PHP^{n+1}_n needs superpolynomial (recalled: 2^{Ω(n)}) resolution refutations. |
| [chvatal-1988-random-resolution.md](chvatal-1988-random-resolution.md) | Resolution-based algorithms on **typical** instances: random k-CNF with c·2^{−k} ≥ 0.7 needs (1+ε)^n resolution clauses w.h.p. |
| [bensasson-2001-size-width.md](bensasson-2001-size-width.md) | Resolution-based algorithms on any family of large refutation width, via S ≥ exp(Ω((w − w₀)²/n)). Tseitin on expanders (easy for Gaussian elimination) and random 3-CNF have width Ω(n). |
| [atserias-2008-width-pebble-games.md](atserias-2008-width-pebble-games.md) | Fixed-level local consistency (k-consistency, pebble-game propagation, bounded-width Datalog) as a SAT/CSP algorithm. It equals width-k resolution, so it fails on PHP, Tseitin and random 3-CNF. |
| [grigoriev-2001-sos-parity.md](grigoriev-2001-sos-parity.md) | Degree-o(n) SoS / Positivstellensatz refutation of Tseitin and random 3-XOR (hence random 3-SAT). With Lee–Raghavendra–Steurer 2015: any polynomial-size SDP relaxation for CSPs (no better than 7/8 for MAX-3-SAT). |
| [schoenebeck-2008-lasserre-ksat.md](schoenebeck-2008-lasserre-ksat.md) | Lasserre/SoS refutation of random k-SAT / k-XOR (k ≥ 3) below linear level. Linear-level gaps for Vertex Cover (7/6), hypergraph VC (2) and hypergraph independent set. |
| [fiorini-2015-extension-complexity.md](fiorini-2015-extension-complexity.md) | Polynomial-size LP extended formulations, symmetric or not, of the TSP, cut and stable-set polytopes. Refutes "P = NP via a compact LP". |
| [rothvoss-2014-matching-polytope.md](rothvoss-2014-matching-polytope.md) | Compact LP extended formulations of perfect matching (a problem in P!) and of TSP (2^{Ω(n)}). Extension-complexity bounds are therefore not evidence for P ≠ NP. |
| [yannakakis-1991-symmetric-lp.md](yannakakis-1991-symmetric-lp.md) | Polynomial-size **symmetric** LPs for TSP and matching. Provides xc(P) = rank₊(slack matrix) and the communication-complexity method used to audit any LP-based claim. |

## Triage checklist derived from these records

### For a P ≠ NP proof attempt

1. **Relativization.** Does every step hold relative to an arbitrary oracle? If yes, reject. Otherwise name the non-relativizing step.
2. **Natural proofs.** Is there an implicit truth-table property that is constructive (poly(2^n)), large (≥ 2^{−O(n)}) and useful against P/poly? If yes, the argument also breaks strong PRGs: reject unless that is separately justified. Otherwise state which condition fails.
3. **Algebrization.** Is the only non-relativizing ingredient arithmetization or low-degree extension? If yes, reject.
4. **Locality.** If the argument goes through hardness magnification, does the technique also bound circuits with small-fan-in oracle gates? If yes, reject.
5. **Gate elimination.** If the argument restricts variables and counts eliminated gates, is it inside the GHKK framework? If yes, it is capped at a linear bound.
6. **Restricted-model results.** Monotone, AC0, ACC0 and proof-system lower bounds do not imply P ≠ NP. Check that no such implication is assumed (see the Tardos function and perfect matching).
7. **Calibration.** Do the intermediate corollaries include currently open statements? Examples: NP ⊄ ACC0, NEXP ⊄ TC0 (recalled as open), or a superlinear explicit B2 bound. If so, the proof claims more than the frontier and must be audited at that point first.

### For a P = NP algorithm

1. **Proof-system simulation.** Do its runs on unsatisfiable inputs convert into proofs in a known system?
   - DPLL/CDCL → resolution.
   - Local consistency → bounded-width resolution.
   - SDP/SoS relaxations → degree-bounded SoS.
   - LP relaxations → Sherali–Adams / LP extension complexity.

   If yes, test PHP, Tseitin on expanders and random 3-CNF at density about 5–10. Known lower bounds then give exponential running time.
2. **Monotonicity.** Is the computation monotone in the input edges/variables? If yes, it cannot solve CLIQUE, even approximately.
3. **Compact LP formulation.** Does the algorithm write down a polynomial-size LP/SDP that is supposed to be exact for all objectives? If yes, its projection must equal the combinatorial polytope, which is refuted for TSP, cut, stable set and (for LPs) matching.
4. **Black-box use of the verifier.** Does the algorithm only use the NP verifier as a black box? If yes, the BGS oracle B refutes it.
5. **Linear algebra over F₂.** Does it handle Tseitin / random 3-XOR? These are easy for Gaussian elimination but hard for resolution and SoS. Any candidate must subsume both clause reasoning and F₂ linear algebra.

## Related results recorded inside the records

Each has its own verification status in the record that mentions it.
- Bennett–Gill 1981 (random oracle): in the BGS record.
- Williams 2016, "Natural Proofs Versus Derandomization": in the natural proofs and ACC records.
- Oliveira–Santhanam 2018 (hardness magnification): in the locality record.
- Blum 1984 (3n): in the FGHK record.
- Furst–Saxe–Sipser 1984 and Ajtai 1983: in the Håstad record.
- Tardos 1988 and Cavalar–Kumar–Rossman 2022: in the Alon–Boppana record.
- Urquhart 1987 (Tseitin): in the BSW record.
- Kolaitis–Vardi 2000 and Berkholz (pebble games / k-consistency): in the Atserias–Dalmau record.
- Pipatsrisawat–Darwiche 2011 (CDCL vs resolution): in the Cook–Reckhow record.
- Lee–Raghavendra–Steurer 2015 (SDP size): in the Grigoriev record.

Two further items were seen by WebSearch but **not** cited in any record:
- Chan–Lee–Raghavendra–Steurer (FOCS 2013 / JACM 2016, arXiv 1309.0563). Per the WebSearch summary: for approximating CSPs, polynomial-size LPs are no stronger than O(1) rounds of Sherali–Adams. This is the LP analogue of LRS 2015.
- A 2026 Lean formalization of PARITY lower bounds (arXiv 2609.24188, not reviewed): pointer in the Håstad record, for the proof engineer.

## Open verification tasks

1. Retrieve ECCC TR26-260 (Mishra–Santhanam) and record the function, technique and theorem.
2. Confirm the JACM volume/issue for Chen et al. (2022), Rothvoss (2017) article number, SICOMP pages for Murray–Williams (2020), STOC pages for Li–Yang (2022) and Yannakakis (1988).
3. Check against the primary texts the precise forms flagged as recalled:
   - Haken's exponent;
   - Razborov's 1985 clique and matching bounds;
   - Håstad's original switching-lemma constant;
   - the AW oracle statements for NP vs P in both directions;
   - FMPTW's correlation-polytope and stable-set exponents.
