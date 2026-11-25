# NIST Circuit Complexity Project (web page; accessed 2026-11-25)

| Field | Value |
|---|---|
| Title | Circuit Complexity (NIST CSRC project page) |
| Authors / contacts | NIST Cryptographic Technology Group. Listed contacts: René Peralta, Meltem Sönmez Turan, Luís T. A. N. Brandão |
| Year | Living web page. "2026" in the file name is the **access year**, not a publication year |
| URL | https://csrc.nist.gov/projects/circuit-complexity (sub-pages /publications, /references, /presentations) |
| Code and data | https://github.com/usnistgov/Circuits (circuit library mirror) |
| Group | MC: reference data and open problems. Index: `index-multiplicative-complexity.md` |

## Relevant content (relayed)

1. **Goals.**
   - Improve understanding of the circuit complexity of Boolean and vectorial Boolean functions.
   - Develop techniques for building better circuits.
   - The project mainly uses the {AND, XOR, NOT} basis and MC as the main measure.
2. **Example open problems listed.**
   - Can the AES S-box be implemented with fewer than 32 non-linear (AND) gates?
   - What is the maximum MC of symmetric functions on 22 variables?
3. **Tractability.** With current techniques, finding AND-optimal circuits is intractable for most functions with more than 6 inputs.
4. **Publications.** The list runs from Boyar–Peralta 2008 (symmetric functions) to Sönmez Turan 2022 (new bounds).

## Why it matters for NP-FRONTIER

- The project is the most likely source of machine-readable MC data: the 5- and 6-variable classifications and optimal circuits.
- That data supports suggested check 1 in the index: verifying the fresh-variable lemma (a) for all g on ≤ 5 variables.
- Item 3 sets expectations for experiments: exact MC beyond 6 variables needs SAT-based methods (`mc-soeken-2020-sat.md`) and only works for specific functions.

## Limitations

- Content relayed from search summaries.
- It is unverified whether the GitHub repository actually contains the full 6-variable class table with MC values.

## Retrieval

- URL, group, contacts, goals, the two example open problems, the tractability remark and the GitHub link: from WebSearch summaries of csrc.nist.gov/Projects/circuit-complexity and its sub-pages.
- Repository contents: not checked.
