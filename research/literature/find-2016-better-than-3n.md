# Find, Golovnev, Hirsch, Kulikov (2016): A better-than-3n lower bound for the circuit complexity of an explicit function

| Field | Value |
|---|---|
| Title | A Better-than-3n Lower Bound for the Circuit Complexity of an Explicit Function |
| Authors | Magnus Gausdal Find, Alexander Golovnev, Edward A. Hirsch, Alexander S. Kulikov |
| Year | 2016 |
| Venue | 57th IEEE FOCS (2016), New Brunswick NJ, pp. 89–98 |
| DOI | 10.1109/FOCS.2016.19 |
| Preprint | ECCC TR15-166 (October 2015; revised 2016 and 2022). A revision PDF is titled "Improving 3n Circuit Complexity Lower Bounds" in search result titles; whether a journal version under that title exists is unverified |
| Group | Circuit lower bound frontier (general circuits) |

## Relevant theorems

Statements are confirmed at abstract level. B2 is the full binary basis (all fan-in-2 Boolean gates), and size is the number of gates.

1. **Main theorem.** Any B2 circuit computing an affine disperser for sublinear dimension has size at least **(3 + 1/86)n − o(n)**.
   - Affine disperser: non-constant on every affine subspace of dimension ≥ d.
   - Explicit constructions for sublinear d exist (recalled), so this is a bound for an explicit function.
2. **Quadratic dispersers.** A much simpler proof gives a stronger **3.11n** lower bound for quadratic dispersers. Recalled, unverified: explicit quadratic dispersers with the required parameters were not known at the time, so this second bound is not for an explicit function.

**Historical position.** This is the first improvement on Blum's 3n − o(n), which had stood for over 30 years. Blum's bound:
- N. Blum, "A Boolean function requiring 3n network size", Theoretical Computer Science 28(3):337–345, 1984.
- It applies to a slightly modified version of Paul's function.
- Earlier history: Paul 2.5n; Schnorr's claimed 3n had a gap found by Wegener.

**Method (recalled, unverified in detail).**
- Gate elimination using affine substitutions.
- A complexity measure that combines the number of gates with a weighted count of inputs.
- A generalized circuit model that permits certain cyclic structures.

## What it rules out or limits

Frontier calibration, not a no-go: it shows how slowly gate elimination advances. It took over 30 years to move the explicit constant from 3 to 3 + 1/86. Follow-up bounds: 3.1n (Li–Yang 2022), claimed 3.5n (Mishra–Santhanam 2026, unrefereed). Gate elimination has a provable ceiling (`golovnev-2016-gate-elimination-limits.md`).

## Why it matters for NP-FRONTIER

Linear-size lower bounds for explicit functions are the best known for general circuits. Any hypothesis implying, for example, a 10n or n log n lower bound for an explicit function over B2 would be a major result. Such a claim calls for the full breakthrough protocol, including a check that it does not rely on unrestricted gate elimination.

## Limitations

- B2 basis only.
- The hard function is in P, so this says nothing about P vs NP per se.
- The 3.11n bound is for a function not known to be explicit (recalled).

## Retrieval

- Authors, FOCS 2016 venue, pages 89–98 and DOI 10.1109/FOCS.2016.19: confirmed by WebSearch (NIST bibliographic record, SPbU research portal, researchr; result summaries).
- ECCC TR15-166 and its revision history (2016, 2022): confirmed via WebSearch summary of the ECCC page.
- The (3 + 1/86)n − o(n) affine-disperser bound and the 3.11n quadratic-disperser bound: confirmed via WebSearch summaries of the abstract.
- Blum 1984 bibliographic data and abstract ("We modify the definition of Paul's function slightly and prove a 3n-lower bound for the network complexity of that function"), plus the Paul/Schnorr/Wegener history: confirmed via a separate WebSearch (Utah TCS bibliography, Crossref, University of Bonn page).
- The method description and the non-explicitness of quadratic dispersers: recalled, unverified.
