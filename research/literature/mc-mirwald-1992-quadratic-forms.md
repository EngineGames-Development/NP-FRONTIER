# Mirwald, Schnorr (1992): The multiplicative complexity of quadratic Boolean forms

| Field | Value |
|---|---|
| Title | The multiplicative complexity of quadratic Boolean forms |
| Authors | R. Mirwald, C. P. Schnorr |
| Year | 1992 (journal); conference version 1987 |
| Venue | Theoretical Computer Science 102(2), 307–328 (1992). Conference version: 28th IEEE FOCS (1987), pp. 141–150 |
| DOI | 10.1016/0304-3975(92)90235-8 |
| Group | MC: exact results for structured classes. Index: `index-multiplicative-complexity.md` |

## Relevant theorems (abstract level, relayed by search summaries)

1. **Single quadratic form.** For a quadratic Boolean form f, the multiplicative complexity L(f) = MC(f) equals **half the rank of an associated matrix**.
   - Recalled, standard: this is the alternating (symplectic) matrix of the quadratic part.
   - Equivalently, by Dickson's normal form, f is affinely equivalent to x_1x_2 + x_3x_4 + ⋯ + x_{2r−1}x_{2r} plus an affine function, and MC(f) = r.
2. **Isomorphism.** As relayed: "two forms have the same complexity exactly when a linear isomorphism maps one to the other". The exact formulation is **unverified**. As relayed it looks stronger than the rank statement, so check the paper before using it.
3. **Computational independence.** The paper characterizes when two quadratic forms f_1, f_2 satisfy L(f_1, f_2) = L(f_1) + L(f_2). This is a two-output direct-sum property.
4. **Sets of forms.** The complexity of sets of quadratic forms is related to the rank of corresponding tensors (relayed).

## Why it matters for NP-FRONTIER

- Quadratic forms are the main nontrivial class where MC is known exactly in the unrestricted XAG model.
- Item 3 is a **multi-output** direct-sum statement for quadratic forms. It is not the AND-composition MC(g·h) of index item (b), and not the XOR-composition MC(g ⊕ h).
- **Fresh-variable lemma (item (a)).** Combining the rank characterization with the affine-restriction technique proves (a) for all quadratic g. See observation D4 in the index. This derivation is Agent D's own and is **not** stated in any source seen.
- **Open question.** Boyar and Find (2018) asked whether every quadratic map has an optimal circuit whose intermediate values are all quadratic (per MathWorld). A 2026 preprint (`mc-morse-2026-polynomial-multiplication.md`) states that Mirwald–Schnorr settles this for one and two outputs.

## Limitations

- Restricted to quadratic forms.
- Content is known to Agent D only at abstract level.
- The recalled Dickson normal form and the identification of "the associated matrix" are standard, but not checked against this paper.

## Retrieval

- Journal volume, issue and pages: from a WebSearch summary of the Utah TCS bibliography entry (Mirwald:1992:MCQ).
- DOI: from a WebSearch summary.
- FOCS 1987, pp. 141–150: from WebSearch summaries of researchr (MirwaldS87) and dblp (conf/focs/MirwaldS87).
- Abstract content (items 1–4): from a WebSearch summary of a bohrium.com record of the paper.
- "Quadratic circuits optimal for one- and two-output quadratic functions": attributed to this paper in a WebSearch summary of arXiv 2608.30238 (Morse, 2026), which cites Boyar–Find for the context. Not checked.
- Dickson normal form and symplectic-rank interpretation: recalled, standard, unverified against this paper.
