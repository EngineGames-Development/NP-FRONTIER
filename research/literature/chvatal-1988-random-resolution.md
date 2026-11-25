# Chvátal, Szemerédi (1988): Many hard examples for resolution

| Field | Value |
|---|---|
| Title | Many Hard Examples for Resolution |
| Authors | Vašek Chvátal, Endre Szemerédi |
| Year | 1988 |
| Venue | Journal of the ACM 35(4):759–768, October 1988 |
| DOI | 10.1145/48014.48016 |
| Group | No-go for candidate polynomial-time SAT algorithms (resolution-based; typical-case hardness) |

## Relevant theorem

Abstract level, confirmed except for the rendering of one exponent.

For every choice of positive integers c and k with **k ≥ 3** and **c·2^{−k} ≥ 0.7**, there is ε > 0 such that, with probability tending to 1 as n → ∞, a randomly chosen family of cn clauses of size k over n variables:
- (i) is **unsatisfiable**, but
- (ii) every resolution refutation of it contains at least **(1 + ε)^n** clauses.

Notes:
- The WebSearch summary rendered the bound as "(1 + ε) n". I read it as (1 + ε)^n with the superscript lost.
- The exponential reading is also how the result is universally cited: a secondary summary says "no resolution proof of length less than 2^{εn}".
- A 2026 Lean-formalization preprint (arXiv 2606.16134; via WebSearch summary, not reviewed) states the same density hypothesis "7/10 ≤ c·2^{−k}" and the bound "(1+ε)^n".
- 0.7 > ln 2 ≈ 0.693, consistent with the first-moment unsatisfiability threshold of about 2^k ln 2 clauses per variable.

Random model (recalled, unverified): each clause picks k distinct variables uniformly and negates each with probability 1/2, independently across clauses.

## What it rules out or limits

1. **Hardness is typical, not just worst-case.** Every resolution-based algorithm needs exponential time on almost all random k-CNFs at constant density above the unsatisfiability threshold. This covers DPLL with any heuristic and CDCL with any policy (CDCL ≡ resolution: `cook-1979-proof-systems.md`).
2. **Average-case escape routes are closed.** A candidate algorithm "polynomial on random instances" cannot be resolution-based in the unsatisfiable regime.
3. **Other systems.** The same random 3-CNFs are, w.h.p., also hard for:
   - degree-o(n) SoS (`grigoriev-2001-sos-parity.md`, `schoenebeck-2008-lasserre-ksat.md`);
   - cutting planes: ECCC TR17-045 "Random CNFs are Hard for Cutting Planes" (title seen via WebSearch; authors not confirmed).

## Why it matters for NP-FRONTIER

- Random 3-CNF at density about 5–10 clauses per variable (unsatisfiable w.h.p.) is the standard stress test for any proposed SAT procedure.
- A candidate must either refute such formulas in polynomial time with proofs outside resolution, cutting planes and low-degree SoS, or it fails.
- Recalled, unverified: no polynomial-time algorithm is known that certifies unsatisfiability for most random 3-CNFs at large constant density. Feige's hypothesis conjectures that none exists. Polynomial-size refutations in strong proof systems are known only at much higher clause densities (m ≫ n). A candidate algorithm that succeeds at constant density would be refuting a widely believed conjecture.

## Limitations

- Resolution only, plus systems simulated by it.
- The theorem concerns a fixed constant density. Behaviour at growing densities (m ≫ n) differs and was treated in later work (not checked).

## Retrieval

- Authors, title, JACM 35(4):759–768 (October 1988) and DOI 10.1145/48014.48016: confirmed via WebSearch (JACM bibliography at MIT, researchr BibTeX, DBLP; result summaries).
- Abstract-level statement (integers c, k; k ≥ 3; c2^{−k} ≥ 0.7; unsatisfiable w.h.p.; every resolution proof generates at least (1+ε)·…·n clauses): confirmed via WebSearch summary of the Scilit abstract record. The exponent was rendered ambiguously; the exponential reading is from memory and corroborated by secondary summaries.
- Random model details and the Feige-hypothesis remark: recalled, unverified.
- Cutting-planes paper: title only, from WebSearch results.
