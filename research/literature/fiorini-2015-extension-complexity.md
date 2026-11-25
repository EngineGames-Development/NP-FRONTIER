# Fiorini, Massar, Pokutta, Tiwary, de Wolf (2012/2015): Exponential lower bounds for polytopes in combinatorial optimization

| Field | Value |
|---|---|
| Title (journal) | Exponential Lower Bounds for Polytopes in Combinatorial Optimization |
| Title (conference) | Linear vs. Semidefinite Extended Formulations: Exponential Separation and Strong Lower Bounds |
| Authors | Samuel Fiorini, Serge Massar, Sebastian Pokutta, Hans Raj Tiwary, Ronald de Wolf |
| Year | 2015 (journal); 2012 (conference) |
| Venues | Journal of the ACM 62(2), Article 17, 2015, DOI 10.1145/2716307 (page count given as 17 or 23 by different records). 44th ACM STOC (New York, May 19–22, 2012), pp. 95–106, DOI 10.1145/2213977.2213988 |
| arXiv | 1111.0837 |
| Group | No-go for candidate polynomial-time algorithms (compact LP formulations) |

## Definitions

- **Extension (extended formulation)** of a polytope P ⊆ R^d: a polyhedron Q ⊆ R^{d+k} whose projection onto the first d coordinates is P.
- **Size** of the extension: its number of facets (inequalities).
- **Extension complexity xc(P):** the minimum size over all extensions.
- **Yannakakis factorization theorem:** xc(P) equals the nonnegative rank of the slack matrix of P (`yannakakis-1991-symmetric-lp.md`).
- **Correlation polytope:** COR(n) = conv{ b bᵀ : b ∈ {0,1}^n }.
- **TSP polytope:** TSP(n) = convex hull of the incidence vectors of Hamiltonian cycles of K_n.

## Relevant theorems

1. **No compact LP for TSP, cut or stable set** (confirmed at abstract level). There is **no polynomial-size linear program whose polytope projects onto the TSP polytope**, even when the LP is not required to be symmetric. The same holds for the **cut polytope** and the **stable set polytope**: the paper gives unconditional super-polynomial lower bounds for max-cut and max-stable-set formulations.
2. **Quantitative bounds** (recalled; partly implied by other confirmed sources):
   - xc(COR(n)) = 2^{Ω(n)}, via a nondeterministic communication-complexity / rectangle-covering bound for the unique-disjointness matrix. The cut polytope is linearly related to COR, so CUT(n) is also 2^{Ω(n)}.
   - xc(TSP(n)) = 2^{Ω(√n)}, via a reduction from COR. This bound is the one Rothvoss's abstract reports improving from 2^{Ω(√n)} to 2^{Ω(n)} (`rothvoss-2014-matching-polytope.md`).
   - Stable set polytopes of suitable n-vertex graphs: 2^{Ω(√n)}.
3. **LP vs SDP separation** (title of the conference version; details recalled). There is an explicit family exhibiting an exponential gap between LP extension complexity (nonnegative rank) and SDP extension complexity (PSD rank).

## What it rules out or limits

**It unconditionally refutes the "P = NP by a polynomial-size LP" strategy**: writing down an explicit LP of polynomial size whose feasible region projects onto the TSP polytope (or the cut or stable-set polytope).
- This holds independently of whether P = NP, and applies to every such LP, symmetric or not.
- The check is purely polyhedral. Suppose the LP must give the exact optimum for **every** linear objective on the original variables. Then its projection Q must equal P: if Q ⊋ P, some objective has min over Q < min over P. So "exact for all costs" claims reduce to "the projection is the polytope", and this theorem then applies.

## Why it matters for NP-FRONTIER

Many P = NP claims in the literature are LP formulations of TSP or other NP-hard problems. This is the definitive filter for them.

## Limitations

- **Only extended formulations of the fixed polytope are covered.** It does not cover:
  - algorithms whose LP depends on the instance in ways not captured by a fixed polytope;
  - approximate formulations (separate literature, not checked);
  - non-LP algorithms.
- **SDP extensions are a different model.** Superpolynomial lower bounds for SDP extension complexity of cut/TSP/stable set came later: Lee–Raghavendra–Steurer 2015 (see `grigoriev-2001-sos-parity.md`).
- **Not evidence for P ≠ NP.** The perfect matching polytope (a problem in P) also has exponential extension complexity (`rothvoss-2014-matching-polytope.md`). Extension complexity limits a modeling technique, not polynomial-time computability.

## Retrieval

- Author list, JACM 62(2) Article 17 (2015) with DOI 10.1145/2716307, the STOC 2012 title, pages 95–106 and DOI 10.1145/2213977.2213988, and arXiv 1111.0837: confirmed via WebSearch (ZIB OPUS record, CWI repository, unpaywall DOI link, arXiv listing, bibbase; result summaries).
- Statement 1 (no polynomial-size LP projecting onto the TSP polytope even without symmetry; same for cut and stable set; super-polynomial lower bounds for max-cut and max-stable-set): confirmed via WebSearch summaries of the abstract.
- The correlation-polytope bound and the rectangle-covering method: recalled. The WebSearch did not surface the correlation-polytope statement.
- The TSP 2^{Ω(√n)} bound: corroborated by Rothvoss's abstract (confirmed via WebSearch).
- LP-vs-SDP separation details and the stable-set exponent: recalled, unverified.
- The polyhedral "exact for all costs ⇒ projection equals P" remark: standard convexity, my own derivation.
