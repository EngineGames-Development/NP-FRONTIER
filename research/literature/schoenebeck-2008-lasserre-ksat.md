# Schoenebeck (2008): Linear level Lasserre lower bounds for certain k-CSPs

| Field | Value |
|---|---|
| Title | Linear Level Lasserre Lower Bounds for Certain k-CSPs |
| Author | Grant Schoenebeck |
| Year | 2008 |
| Venue | 49th IEEE FOCS (Philadelphia, October 25–28, 2008), pp. 593–602 |
| URL | https://www.schoeneb.people.si.umich.edu/papers/Lasserre.html |
| Group | No-go for candidate polynomial-time SAT algorithms (Lasserre / SoS hierarchy) |

## Relevant theorem

**Abstract-level statement (confirmed).** For k ≥ 3, the **Ω(n)-level Lasserre hierarchy** cannot refute random k-CSP instances over predicates implied by k-XOR constraints, such as k-SAT and k-XOR. The constraint density in the main statement is recalled as m = O(n), i.e. constant density.

**Corollaries (confirmed at abstract level)** — Ω(n)-level Lasserre integrality gaps for:
- Vertex Cover: 7/6 − ε;
- k-uniform hypergraph vertex cover: 2 − ε;
- k-uniform hypergraph independent set: any constant.

Relationship to Grigoriev:
- Later literature (WebSearch summary) describes this as a rediscovery of Grigoriev's random 3-XOR result (`grigoriev-2001-sos-parity.md`).
- Schoenebeck noted that it implies the 3-SAT statement, because a ⊕ b ⊕ c = 1 implies a ∨ b ∨ c.
- Tulsiani (2008) extended such gaps via reductions within the Lasserre hierarchy.

## What it rules out or limits

1. **SDP hierarchies cannot solve random 3-SAT.** Lasserre/SoS relaxations at level o(n), and even at level cn for small c > 0, cannot certify unsatisfiability of random 3-SAT at constant density. Level-d Lasserre takes n^{O(d)} time.
2. **Approximation consequences.** For approximation-based approaches to NP-hard optimization (Vertex Cover, hypergraph vertex cover, independent set), linear-level SoS does not beat the stated ratios.

## Why it matters for NP-FRONTIER

- It is a canonical citation, alongside Grigoriev, for the statement "the SoS/Lasserre hierarchy needs linear degree on random 3-SAT".
- Any proposed algorithm that is a hierarchy relaxation of a SAT/CSP encoding, or that is simulated by one, is refuted on random instances.

## Limitations

- Random instances at constant density.
- Says nothing about non-SoS algorithms.
- The precise density-versus-level tradeoff is not recorded here.

## Retrieval

- Title, author, FOCS 2008 dates, location and pages 593–602: confirmed via WebSearch (researchr BibTeX, author's paper page; result summaries).
- Main statement (Ω(n)-level Lasserre cannot refute random k-CSPs over predicates implied by k-XOR, k ≥ 3, e.g. k-SAT and k-XOR) and the three integrality-gap corollaries: confirmed via WebSearch summary of the abstract.
- Rediscovery relationship to Grigoriev and the a ⊕ b ⊕ c ⇒ a ∨ b ∨ c remark: confirmed via WebSearch summaries of secondary sources (arXiv 1501.00734 and others).
- Tulsiani extension: from WebSearch summary (ECCC 2008 report), details not checked.
- Density regime: recalled.
