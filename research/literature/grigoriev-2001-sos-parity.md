# Grigoriev (2001): Linear lower bound on degrees of Positivstellensatz calculus proofs for the parity

| Field | Value |
|---|---|
| Title | Linear lower bound on degrees of Positivstellensatz calculus proofs for the parity |
| Author | Dima Grigoriev |
| Year | 2001 (journal). Some later sources date the result to 1999, presumably an earlier preprint (unresolved) |
| Venue | Theoretical Computer Science 259(1–2):613–622, 2001 |
| DBLP | journals/tcs/Grigoriev01 |
| URL | Author PDF: https://logic.pdmi.ras.ru/~grigorev/pub/positive_journal.pdf |
| Group | No-go for candidate polynomial-time SAT algorithms (sum-of-squares / Positivstellensatz / Lasserre) |

## Definitions (recalled)

**Positivstellensatz calculus (static form).** For a system of polynomial equations {f_i = 0} over the reals (with Boolean axioms x² − x = 0, or the ±1 encoding), a refutation is an identity
- Σ_i g_i f_i + Σ_j h_j² = −1.

Its **degree** is the maximum degree of the terms. Degree-d refutations correspond to infeasibility of the degree-d sum-of-squares (Lasserre) SDP relaxation, which can be searched in n^{O(d)} time.

## Relevant theorem

**Abstract-level statement (confirmed).** Positivstellensatz-calculus refutations over the reals need **linear degree, Ω(n)**, for:
- **Tseitin tautologies** (on suitable expander graphs), and
- the **parity (mod 2) principle**.

The proof uses the Laurent-proof machinery developed for binomial systems by Buss et al.

**Standard consequence as cited by later literature (secondary).** For a random 3-XOR system with n variables and m = Δn equations (Δ a large constant), the system is w.h.p. unsatisfiable, yet **degree-Ω(n) SoS does not refute it**. Later papers attribute this to Grigoriev (2001; one source says 1999) and to Schoenebeck's 2008 rediscovery.
- Technique: build a pseudo-expectation consistent with every equation derivable by low-width linear combinations. Expansion of the constraint hypergraph rules out low-width derivations of 0 = 1.
- In this sense the SoS lower bound reduces to a width lower bound for "Gaussian-elimination-style" proofs.
- Higher densities (recalled, unverified): the degree bound degrades as m grows. SoS refutes random 3-XOR at about m ≈ n^{3/2} with constant degree, up to polylog factors.

## What it rules out or limits

1. **SoS-based SAT algorithms.** Degree-d SoS / Lasserre / Positivstellensatz refutation costs n^{O(d)} time. With d = o(n) it **cannot** refute random 3-XOR, and hence, via implication of predicates, random 3-SAT at constant density (`schoenebeck-2008-lasserre-ksat.md`). No constant-degree or polylog-degree SDP hierarchy solves 3-SAT.
2. **SoS does not capture Gaussian elimination.** 3-XOR is in P via Gaussian elimination, so degree-o(n) SoS is strictly weaker than polynomial time on this family. A "convex relaxation" P = NP candidate must explain how it handles parity.
3. **Lifting to all small SDPs.** Lee, Raghavendra, Steurer, "Lower bounds on the size of semidefinite programming relaxations" (STOC 2015, best paper; arXiv 1411.6317; confirmed via WebSearch summary) show:
   - for constraint satisfaction problems, polynomial-size SDP relaxations are no stronger than degree-O(1) SoS;
   - consequently **no family of polynomial-size SDP relaxations achieves better than a 7/8-approximation for MAX-3-SAT**;
   - the cut, TSP and stable-set polytopes have superpolynomial SDP extension complexity.

## Why it matters for NP-FRONTIER

This record closes off the "solve SAT by an SDP / polynomial optimization relaxation" family of P = NP proposals, both hierarchy-based and arbitrary polynomial-size SDP-based, at least for CSP-style formulations.

## Limitations

- Lower bounds are for refutation of specific families (Tseitin, random XOR/SAT). They do not rule out SDP-based algorithms that are not relaxations in this sense.
- The exact dependence of degree on density Δ is not recorded here.
- The 1999 vs 2001 date discrepancy is unresolved.

## Retrieval

- Title, TCS 259(1–2):613–622 (2001), DBLP key and author PDF: confirmed via WebSearch (DBLP, OpenAIRE/Czech Academy catalog, reference list of arXiv 1711.07320; result summaries).
- Abstract-level statement (linear degree lower bound for Positivstellensatz refutations over a real field, for Tseitin tautologies and the parity principle; Laurent proofs from Buss et al.): confirmed via WebSearch summary.
- Random 3-XOR consequence, the 1999 attribution, the Schoenebeck rediscovery and the "reduce to width" technique: confirmed only via WebSearch summaries of secondary sources (arXiv 1501.00734, KTH lecture notes, Barak's SoS lecture notes). Not checked against the paper.
- Higher-density remarks: recalled, unverified.
- Lee–Raghavendra–Steurer: confirmed via WebSearch summaries of the author page and the arXiv abstract.
- Proof-system definitions: recalled.
