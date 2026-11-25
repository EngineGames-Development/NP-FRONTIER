# Morse (2026): Unrestricted Boolean multiplicative complexity of four-term binary polynomial multiplication (UNREFEREED)

| Field | Value |
|---|---|
| Title | Unrestricted Boolean Multiplicative Complexity of Four-Term Binary Polynomial Multiplication: Rational Places, Hasse Jets, and the Failure of Nonlinear Feedback |
| Authors | Gregory Morse (single author, per search summary) |
| Year | 2026 (posted 31 August 2026 per Emergent Mind) |
| Venue | arXiv preprint 2608.30238. **Unrefereed** |
| Group | MC: exact values for explicit vector-valued quadratic maps; Lean 4 formalization precedent. Index: `index-multiplicative-complexity.md` |

## Claimed results (abstract level; NOT verified)

1. **Mul_4.** The map Mul_4 multiplies two four-term binary polynomials; its 7 outputs are the product coefficients. Its **unrestricted** XOR-AND multiplicative complexity is **exactly 9**.
   - "Unrestricted" means intermediate wires may have any degree and nonlinear values may be reused.
2. **Mul_3.** The same argument gives MC 6 for three-term multiplication.
3. **Quadratic circuits.** The result answers, for this map, the Boyar–Find question whether quadratic circuits are optimal for quadratic maps.
   - The abstract says the method "isolates the multi-defect obstruction for five terms".
   - Mul_n for n ≥ 5 remains open (MathWorld).
4. **Formalization.** The author reports a **complete Lean 4 formalization**: Boolean-ANF semantics, the unrestricted circuit model and the exact theorem, with no project-specific axiom or native decision procedure.
5. A search snippet attributes to the paper the statement that every circuit for Mul_n uses at least 2n − 1 AND gates. Unverified.

**Related 2026 preprint.** arXiv 2611.15992, "The multiplicative complexity of the three-bit low-half multiplier", claims MC(M_3) = 6 for the low three bits of a 3-bit product. It cites an earlier SAT-based search by one of its authors. Its authors were **not confirmed** by search.

## Why it matters for NP-FRONTIER

- For the Proof Engineer (Agent E): a reported precedent for **formalizing an unrestricted-XAG MC lower bound in Lean 4**. Worth locating, if the Lean source is public, as reusable infrastructure: XAG semantics and MC definitions.
- For index items (a)–(c): vector-valued and quadratic, so it does not bear directly on single-output bounds or on (a)/(b).

## Limitations

- Very recent and unrefereed.
- The abstract was seen only through search summaries.
- The MathWorld entry that cites it also cites a "VibeMathed" page, which suggests AI-assisted material in the citation chain. Treat with caution until checked.

## Retrieval

- Title, author, arXiv ID, posting date and items 1–4: from WebSearch summaries of arxiv.org/pdf/2608.30238 and emergentmind.com/papers/2608.30238.
- Mul_n for n ≥ 5 open and the VibeMathed citation: from a WebSearch summary of the MathWorld "MultiplicativeComplexity" entry.
- Item 5: from one WebSearch summary; unverified.
- 2611.15992 details: from a WebSearch summary of its PDF; authors not visible.
