# Demenkov, Kulikov (2011): An elementary proof of a 3n − o(n) lower bound on the circuit complexity of affine dispersers

| Field | Value |
|---|---|
| Title | An Elementary Proof of a 3n − o(n) Lower Bound on the Circuit Complexity of Affine Dispersers |
| Authors | Evgeny Demenkov, Alexander S. Kulikov. First name "Evgeny" recalled, **unverified**; the search summaries gave only surnames |
| Year | 2011 (ECCC posting 27 February 2011) |
| Venue | MFCS 2011, pp. 256–265 (LNCS volume not confirmed). Also ECCC TR11-026 |
| DOI | 10.1007/978-3-642-22993-0_25 |
| Group | Circuit lower bounds via affine restrictions; MC of affine dispersers. Index: `index-multiplicative-complexity.md`. Related: `li-2022-3.1n-lower-bound.md`, `find-2016-better-than-3n.md` |

## Relevant statements (relayed)

1. **Main theorem.** B2 circuits computing an affine disperser for dimension d = o(n) have size ≥ 3n − o(n).
   - An affine disperser is non-constant on every affine subspace of dimension ≥ d.
   - Proof: gate elimination by affine substitutions x_j ← ⊕_{i∈F_j} x_i ⊕ c, each removing ≥ 3 gates.
2. **MC corollary.** As an easy consequence, the **MC of an affine disperser for dimension d is ≥ n − d − 1**.
3. **Frontier statement** (relayed): the **best known lower bound on the MC of an explicit function is n − 1**.
4. **Attribution** (relayed): similar ideas, "substituting variables by linear functions", were used by Boyar and Peralta to prove MC lower bounds.

## Why it matters for NP-FRONTIER

- Item 3 is the second independent "best known explicit MC bound is n − 1" statement, relevant to index item (c).
- Item 2 gives n − o(n) for explicit affine dispersers, still below n − 1.
- These are one-AND-gate-per-affine-restriction arguments.
  - Such an argument cannot exceed n − 1 for a single output: after n − 1 restrictions the domain is a line, on which every function is affine.
  - Index observation D5 explains why exceeding n − 1 needs an argument that removes more than one AND gate per restriction. The fresh-variable lemma (a) would be such a "+1" device.
- Later B2 bounds for affine dispersers: (3 + 1/86)n by Find–Golovnev–Hirsch–Kulikov and 3.1n by Li–Yang (relayed; see `li-2022-3.1n-lower-bound.md`).

## Limitations

- Introduction excerpts only; the MC corollary's exact statement was seen only in a search summary.

## Retrieval

- Title, MFCS 2011, pp. 256–265, ECCC TR11-026 with its date, and DOI: from WebSearch summaries of DBLP (conf/mfcs/DemenkovK11), ECCC and doi.org.
- Items 1–4: from WebSearch summaries of the ECCC PDF introduction. The phrase "best known lower bound for an explicit function's multiplicative complexity is n − 1" is attributed by a summary to ECCC 2011/026.
- First author's first name: recalled, unverified.
