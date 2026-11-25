# Razborov (1985): Monotone lower bounds for CLIQUE (and for perfect matching)

This record covers two companion 1985 papers.

| Field | Paper (a) | Paper (b) |
|---|---|---|
| Title | Lower bounds on the monotone complexity of some Boolean functions | Lower bounds on monotone complexity of the logical permanent |
| Author | Alexander A. Razborov | Alexander A. Razborov |
| Year | 1985 | 1985 |
| Venue | Doklady Akademii Nauk SSSR 281(4):798–801 | Matematicheskie Zametki 37(6):887–900 |
| English translation | Soviet Mathematics Doklady 31 (1985), pp. 354–357 (the search record names the journal "Doklady Mathematics", a later name of the same translation series) | Mathematical Notes 37(6):485–493, DOI 10.1007/BF01157687 |
| URLs | https://www.mathnet.ru/eng/dan9192 | https://mathnet.ru/eng/mzm5393 |

Group: circuit lower bound frontier (restricted model: monotone circuits).

## Definitions

- **Monotone circuit:** fan-in-2 AND and OR gates only, no negations.
- **CLIQUE(m, s):** input is the C(m,2) edge indicators of an m-vertex graph; output 1 iff the graph contains an s-clique.
- **Bipartite perfect matching (logical permanent):** input is an m×m 0/1 matrix; output 1 iff the permanent is non-zero, i.e. the bipartite graph has a perfect matching.

## Relevant theorems

Recalled from memory, corroborated only by secondary sources; not checked against the papers.

1. **(a) CLIQUE.** Monotone circuits for CLIQUE(m, s) need superpolynomial size: **m^{Ω(log m)}** for s = ⌊(log m)/4⌋.
   - For fixed s, the bound has the form m^{s}/(log m)^{O(s)}. This is Alon–Boppana's summary of Razborov; the exact exponent in the OCR'd copy seen via WebSearch is ambiguous.
   - Jukna's textbook (secondary) states n^{Ω(√k)} for 3 ≤ k ≤ n^{1/4}, attributed jointly to Razborov 1985 and Alon–Boppana 1987.
2. **(b) Perfect matching.** Monotone circuits for bipartite perfect matching need size **n^{Ω(log n)}**. Perfect matching is in **P** (Edmonds).
   - A 2024 arXiv paper (2411.14267, via WebSearch summary) states that this matching bound has not been improved. It poses as open whether monotone circuits of size n^{O(log n)} for bipartite perfect matching exist.
3. **Method: the approximation method.** Replace each gate by an "approximator" from a restricted family: OR of a bounded number of cliques, kept small using the Erdős–Rado sunflower lemma. Count the errors introduced per gate on test distributions of positive inputs (planted cliques) and negative inputs (complete (s−1)-partite graphs). Conclude that small circuits make too many errors.

## What it rules out or limits

1. **Algorithms (P = NP side).** No polynomial-time algorithm for CLIQUE can be implemented as a polynomial-size **monotone** circuit, i.e. using only AND/OR of edge indicators with no negation or cancellation.
   - Any candidate whose computation is monotone in the input edges (e.g. monotone dynamic programs or propagation over edge indicators) is refuted for CLIQUE.
   - A polynomial-time clique algorithm must be inherently non-monotone.
2. **Lower bounds (P ≠ NP side).** Monotone lower bounds do **not** transfer to general circuits.
   - Result (b) gives a superpolynomial monotone lower bound for a problem in P.
   - Tardos 1988 gives an exponential gap (see `alon-1987-monotone-circuits.md`).
   - So "CLIQUE is monotone, so optimal circuits for it may be assumed monotone" is **false** as a general principle. An argument that relies on it is invalid.

## Why it matters for NP-FRONTIER

It is the strongest classical lower bound for an NP-complete problem in a natural restricted model, and the cleanest example of why restricted-model results do not imply P ≠ NP.

## Limitations

- Monotone model only.
- Razborov later studied the limits of the approximation method for general circuits (recalled, unverified; not searched).
- Recent analyses connect the approximation method to the locality barrier: "Localizability of the approximation method" (arXiv 2212.09285, not reviewed) and "On the Approximation Method and the P versus NP Problem" (arXiv 1708.03486, not reviewed).

## Retrieval

- Paper (a): journal, volume/issue 281(4), pages 798–801 and translation data (vol. 31, pp. 354–357): confirmed by WebSearch (Math-Net.Ru and mathdoc records; result summary). The translation journal name is given as recorded; the "Soviet Mathematics Doklady" name is recalled.
- Paper (b): Mat. Zametki 37(6) 887–900, Math. Notes 37(6) 485–493 and DOI 10.1007/BF01157687: confirmed by WebSearch (Math-Net.Ru, mathdoc). Tardos's note cites it under the variant title "A lower bound on the monotone network complexity of the logical permanent".
- Theorem content: **not** confirmed from the primary texts. Corroborated by WebSearch summaries of secondary sources (Jukna textbook chapter 9; Tardos's note; arXiv 2411.14267; Alon–Boppana's introduction). Exact bounds as stated above are recalled from memory.
- Approximation-method description: recalled.
