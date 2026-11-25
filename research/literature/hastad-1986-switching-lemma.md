# Håstad (1986/1987): Switching lemma; parity is not in AC0

| Field | Value |
|---|---|
| Title | Almost Optimal Lower Bounds for Small Depth Circuits |
| Author | Johan Håstad |
| Year | 1986 (conference); thesis 1987 |
| Venue | 18th ACM STOC (1986), pp. 6–20 |
| Thesis | "Computational Limitations of Small-Depth Circuits", PhD thesis, MIT, 1987. Publication by MIT Press is recalled, not confirmed |
| URLs | Paper PDF: https://people.kth.se/~johanh/largesmalldepth.pdf ; thesis PDF: https://www.csc.kth.se/~johanh/thesis.pdf |
| Group | Circuit lower bound frontier (restricted model: AC0) |

## Definitions

- **AC0:** constant-depth, polynomial-size circuits with unbounded fan-in AND/OR gates (negations at the inputs).
- **Random restriction ρ ∈ R_p:** independently for each variable, leave it free with probability p, otherwise fix it to 0 or 1 with equal probability.

## Relevant theorems

**(a) Switching lemma.** Form used in modern presentations; the constant varies across sources.
- Let F be a k-DNF: every term has at most k literals.
- Then for every s ≥ 0: Pr_{ρ ∈ R_p}[ F|ρ has decision-tree depth ≥ s ] ≤ (C·p·k)^s, where C is an absolute constant.
- Depth < s implies F|ρ can be written as both an s-CNF and an s-DNF. This is the "switch" that collapses one layer of a circuit.
- Versions seen in sources surfaced by WebSearch use (5pk)^s, (7pk)^s (with p ≤ 1/7) and (10σw)^d.
- Håstad's original is stated for conversion to s-CNF with constant α ≈ 4.16, namely 2/ln φ with φ the golden ratio (recalled, unverified).

**(b) Parity lower bound.**
- Every depth-d circuit computing PARITY_n has size at least **exp(Ω_d(n^{1/(d−1)}))**.
- This is tight up to the constant in the exponent: depth-d circuits of size n·2^{O(n^{1/(d−1)})} exist (recalled).
- Consequence: **PARITY ∉ AC0**. The same holds for MAJORITY and other functions to which parity reduces in AC0.

**Earlier and independent bounds.**
- Furst–Saxe–Sipser: superpolynomial lower bound. Mathematical Systems Theory 17(1):13–27, 1984, DOI 10.1007/BF01744431; FOCS 1981 version.
- Ajtai: n^{Ω_d(log n)}-type lower bound. Annals of Pure and Applied Logic, 1983; title recalled as "Σ¹₁-formulae on finite structures"; volume/pages unverified.
- Yao (FOCS 1985): first exponential bound.

## What it rules out or limits

- **Restricted model:** constant-depth polynomial-size circuits cannot compute parity, majority, etc.
- **Technique limits** (important for the program):
  - Random restrictions and switching lemmas need the circuit class to simplify under random restrictions. This fails for AC0[2] (a restricted parity gate is still a parity gate on the surviving variables and does not collapse), ACC0, TC0 and P/poly.
  - The argument is **natural** in the Razborov–Rudich sense, so it cannot be extended to P/poly lower bounds under standard cryptographic assumptions.
  - Restriction-based arguments typically **localize**, so they also face the locality barrier when used for magnification targets.
- **Frontier:** a 2026 preprint (arXiv 2609.34029, "Optimal Shallow Circuits for Majority"; via WebSearch summary, unverified) states that Håstad's bound remains the best known AC0 lower bound for any explicit function.

## Why it matters for NP-FRONTIER

- It is the archetype of a successful restricted-model lower bound whose technique provably cannot reach P/poly by itself.
- A P ≠ NP hypothesis built from random restrictions or switching must explain how it escapes naturalness and locality.
- **Formalization pointer (for the proof engineer):** a 2026 preprint, arXiv 2609.24188 "Formalizing PARITY Circuit Lower Bounds in Lean", cites Lean 4 and Mathlib sources and a formalized switching lemma. Author per a search summary: Saint Wesonga (unverified). **Not reviewed**; check what exactly was formalized before reuse.

## Limitations

- AC0 only.
- Constants in the switching lemma differ by presentation. Cite the specific version you use.

## Check to apply to a hypothesis

- If an argument restricts variables at random and claims that the circuit simplifies, what property of the circuit class guarantees simplification?
- If the class contains parity or threshold gates, the switching lemma does not apply as is.

## Retrieval

- STOC 1986 pp. 6–20: confirmed via WebSearch (reference list in MIT OCW 18.405J notes).
- Author-hosted PDFs (paper, thesis): from WebSearch result URLs.
- Thesis (MIT PhD, 1987): confirmed via WebSearch summary citing Wikipedia "Switching lemma". MIT Press publication not confirmed.
- Parity bound exp(Ω_d(n^{1/(d−1)})) and its tightness remark: confirmed via WebSearch summaries of secondary sources. Exact original constants not checked.
- That different presentations use different switching-lemma constants: confirmed via WebSearch summaries of lecture notes (UMass, UMD) and an ECCC report. Håstad's original statement and constant: recalled, unverified.
- Furst–Saxe–Sipser bibliographic data: confirmed via WebSearch (researchr, Springer DOI).
- Ajtai: venue and year confirmed via WebSearch summary; volume/pages and exact title not confirmed.
- Yao 1985 as the first exponential bound: from the WebSearch summary of Håstad's paper text.
- 2026 arXiv items: seen via WebSearch only, not reviewed.
