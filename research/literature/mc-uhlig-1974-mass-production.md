# Uhlig (1974): mass production of Boolean functions (computing f on several inputs)

| Field | Value |
|---|---|
| Title | On the synthesis of self-correcting schemes from functional elements with a small number of reliable elements (Russian title translated; the result on multiple inputs is reportedly contained in this paper). Exact English wording **unverified** |
| Authors | D. Uhlig (Dietmar Uhlig; first name recalled, unverified) |
| Year | 1974 |
| Venue | Matematicheskie Zametki 15 (1974), 937–944 (Russian), as cited in a 1989 paper by Albrecht and relayed by a search summary. English translation in Mathematical Notes (pages **unverified**) |
| Later exposition | "Networks computing Boolean functions for multiple input values", in *Boolean Function Complexity* (ed. M. S. Paterson), London Mathematical Society Lecture Note Series 169, Cambridge University Press, 1992 |
| Secondary sources used | W. Kretschmer, "Quantum Mass Production Theorems", arXiv 2212.14399, TQC 2023 (LIPIcs vol. 266); MIT lecture notes at people.csail.mit.edu/rrw/week2.pdf |
| Group | Circuit size of direct products/sums. Index: `index-multiplicative-complexity.md`, item (b) |

**Chapter authorship conflict.** The Cambridge listing returned by search attributes the 1992 chapter to "M. S. Paterson (University of Warwick)". Paterson is the volume editor. Agent D believes, from memory, that the chapter author is D. Uhlig. The listing's abstract says the efficiency was "already shown in Uhlig (1974)". **Unresolved.**

## Relevant theorem (as restated by the secondary sources)

**Uhlig's mass-production theorem.** For every Boolean function f: {0,1}^n → {0,1} and every r = 2^{o(n/log n)}, the r-output function (x^1, …, x^r) ↦ (f(x^1), …, f(x^r)) has circuit size **(1 + o(1))·2^n/n**.
- The leading constant does not grow with r.
- The r = 2 construction splits the input into a k-bit prefix and uses XOR-decompositions f_i = ⊕ g_ℓ whose pieces g_ℓ are shared between the two copies. Size ≈ (2^k + 1)·2^{n−k}/(n − k).
- Larger r follows by recursion.

## Why it matters for NP-FRONTIER (index item (b), circuit-size part)

**Deduction by Agent D; not found stated in any source.**
- Shannon's counting bound: almost all f ∈ B_n have C(f) ≥ (1 − o(1))·2^n/n.
- Uhlig: C(f(x), f(y)) ≤ (1 + o(1))·2^n/n.
- Hence C(f(x) ∧ f(y)) ≤ (1 + o(1))·2^n/n + 1 < 2C(f) + 1 for almost all f and large n.

So the **AND-direct sum C(f ∧ g) = C(f) + C(g) + 1 is false in general** over B2 (take g = f on fresh variables).

The fresh-variable special case C(f ∧ y) = C(f) + 1 remains trivially true over B2 by gate elimination.

No MC analogue of this theorem was found (one search). Whether MC(f(x)·f(y)) < 2MC(f) + 1 for random f is open as far as Agent D found. Index observation D2 shows that a general MC AND-direct sum would imply explicit superlinear circuit lower bounds.

## Limitations

- The primary source was not seen.
- The exact r-range and constants are taken from Kretschmer's restatement.
- The Mat. Zametki page range comes from a citation inside another paper.

## Retrieval

- Theorem statement, r = 2^{o(n/log n)}, constant not growing with r, and the r = 2 construction with size (2^k + 1)·2^{n−k}/(n − k): from WebSearch summaries of Kretschmer, arXiv 2212.14399 (ar5iv HTML and PDF).
- "O(2^n/n) for k copies, k up to 2^{o(n/log n)}": from a WebSearch summary of the MIT notes (rrw/week2.pdf; author presumably R. Williams, unverified).
- 1974 citation (Mat. Zametki 15, 937–944, Russian): from a WebSearch summary of a 1989 paper on "simultaneous realizations" (Albrecht).
- 1992 chapter and abstract: from a WebSearch summary of the Cambridge Core listing.
- A search summary says Wegener's *The Complexity of Boolean Functions* (the "blue book", hosted as blaues_book.pdf on Jukna's site) has a section "Mass production" (§10.2). The summary attributed the book to Jukna, presumably an error. Unverified.
- Shannon's counting bound: standard, recalled.
