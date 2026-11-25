# Paul (1976): Realizing Boolean functions on disjoint sets of variables

| Field | Value |
|---|---|
| Title | Realizing Boolean functions on disjoint sets of variables |
| Authors | Wolfgang J. Paul (W. J. Paul) |
| Year | 1976 (journal). Cornell technical report TR 75-215, October 1975 |
| Venue | Theoretical Computer Science 2(3), 383–396 (September 1976) |
| DOI | 10.1016/0304-3975(76)90089-X |
| Other copies | Cornell eCommons handle 1813/6996; a scan is hosted at web.vu.lt/mif/s.jukna/Knizka/Paul-disjoint76.pdf (not fetched) |
| Keywords | Ashenhurst decomposition, combinational complexity, switching functions |
| Group | Circuit size of compositions on disjoint variables (direct-sum questions). Index: `index-multiplicative-complexity.md`, item (b) |

## Relevant content (partly garbled in all snippets; treat as UNVERIFIED)

1. **Question posed.**
   - Let C(f) be the combinational complexity over a complete basis; the exact basis was not seen.
   - The paper asks how C(f × f) relates to C(f), where f × f is f evaluated on two disjoint sets of variables with two outputs.
   - It also asks about C(∨∘(f × f)) = C(f(x) ∨ f(y)).
   - The stated naive intuition is C(f × f) = 2C(f), "since two evaluations of f on disjoint sets of variables do not interact".
2. **Claimed answer.**
   - The text reportedly says this intuition is wrong for some functions and that "certain conjectures are far from reality".
   - The eCommons abstract, as relayed, states that for every ε > 0 there are arbitrarily complex functions whose two-copy combination on disjoint variables costs at most (1 + ε)·C(f).
   - It reportedly states a related statement for a composed construction. A different summary rendered this as "(2 − ε)·C(f)".
   - **The exact statements could not be confirmed.**
3. **Applications.** Ashenhurst decomposition does not always yield optimal circuits. There is also a result on the trade-off between circuit size and monotone circuit size (relayed).
4. **Direct sum for matrices.** Jukna's exercise notes attribute to "Paul, Corollary 2" the fact that the XOR (linear-circuit) complexity of a direct sum of matrices can be smaller than the sum of the complexities.

## Why it matters for NP-FRONTIER

- This is the classical source on circuit size for functions on disjoint variable sets. If item 2 is as relayed, it already refutes the naive additivity C(f(x) ∨ f(y)) ≈ 2C(f) for suitable arbitrarily complex f.
- By De Morgan duality over B2, the same holds for ∧. That refutes the AND-direct sum C(f ∧ g) = C(f) + C(g) + 1 of index item (b) for g a copy of f.
- Independently of Paul, the same conclusion follows from Uhlig's mass-production theorem (`mc-uhlig-1974-mass-production.md`, index observation D3).

## Limitations

- Every snippet of the abstract and body was OCR-garbled. Nothing in item 2 is confirmed beyond its general direction (naive additivity fails for some arbitrarily complex functions).
- The paper concerns circuit size over a complete basis, not MC.

## Retrieval

- Title, author, journal, volume, issue, pages, DOI, month and keywords: from WebSearch summaries of the Utah TCS bibliography entry (Paul:1976:RBF), researchr (Paul76) and Scilit.
- Cornell TR 75-215, October 1975, handle 1813/6996: from a WebSearch summary of the eCommons record.
- Items 1–3: from several WebSearch summaries of the eCommons abstract and the Jukna-hosted scan. They are mutually inconsistent in detail.
- Item 4: from a WebSearch summary of Jukna's "problem 7.7" notes page.
