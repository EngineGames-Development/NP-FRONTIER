# Soeken (2020): Determining the multiplicative complexity of Boolean functions using SAT

| Field | Value |
|---|---|
| Title | Determining the Multiplicative Complexity of Boolean Functions using SAT |
| Authors | Mathias Soeken. Search results list him as sole author; this was not checked against the arXiv record itself |
| Year | 2020 (arXiv May 2020) |
| Venue | arXiv 2005.01778 (cs.DS, cs.LO, quant-ph); IACR ePrint 2020/530; presented at IWLS 2020 (relayed) |
| Group | MC: exact computation (tools for experiments). Index: `index-multiplicative-complexity.md` |

## Relevant content (abstract level)

1. A constructive **SAT-based algorithm** that determines the MC of a Boolean function. It finds a minimum-AND XOR-AND-inverter graph (XAG).
2. Several **symmetry-breaking constraints** speed up solving.
3. A heuristic post-optimization reduces the number of XOR gates once the optimum AND count is found.
4. Results: all optimum XAGs for representatives of **all 5-input affine equivalence classes**, and for a set of frequently occurring 6-input functions.

## Why it matters for NP-FRONTIER

This is the most directly usable published method for the experiments suggested in the index:
- check the fresh-variable lemma (a) on small cases, for example whether g·y with an explicit 6-variable MC-6 function g needs 7 AND gates (7 inputs);
- test small instances of the AND-direct sum (b), such as MC((x_1x_2 + x_3x_4)(x_5x_6 + x_7x_8)) ∈ {4, 5}.

## Limitations

- The scaling limits of the method were not seen.
- Exact MC for 7–8 input functions with 6–7 AND gates may or may not be within reach. NIST states that AND-optimal circuits are intractable for most functions beyond 6 inputs.

## Retrieval

- Title, arXiv ID, categories, ePrint 2020/530, IWLS 2020 and items 1–4: from WebSearch summaries of arxiv.org/pdf/2005.01778, ia.cr/2020/530, the IWLS 2020 page, Emergent Mind and CORE.
- The author list (sole author) is as returned by search. A query that guessed a co-author returned no evidence of one.
