# Chistopolskaya, Podolskii (2018): Parity decision tree complexity is greater than granularity

| Field | Value |
|---|---|
| Title | Parity Decision Tree Complexity is Greater Than Granularity |
| Authors | Anastasiya Chistopolskaya, Vladimir V. Podolskii (HSE University; Steklov Institute, per search summary) |
| Year | 2018 (ECCC TR18-174 dated 19 October 2018; two revisions) |
| Venue | ECCC TR18-174 and arXiv 1810.08668. A refereed venue was **not confirmed** by search |
| Group | MC: lower bounds via parity decision trees; statement of the open problem. Index: `index-multiplicative-complexity.md` |

## Relevant statements (relayed by search summaries)

1. **Main theorem.** D⊕(f) ≥ gran(f) + 1.
   - D⊕ is deterministic parity decision tree depth.
   - gran(f) is the smallest k such that all Fourier coefficients of f: {0,1}^n → {−1, 1} are integer multiples of 1/2^k.
   - This improves the sparsity-based lower bound.
2. **Majority.** D⊕(MAJ_n) = n − B(n) + 1, where B(n) is the number of ones in the binary representation of n. The paper also determines D⊕ exactly for recursive majority. A MOD3 section was removed in revision 2.
3. **Link to MC.** By induction on c∧(f), a parity decision tree with at most c∧(f) + 1 queries exists, i.e. D⊕(f) ≤ c∧(f) + 1. The base case is a linear function, which needs one parity query. The exact lemma statement and number were **not seen** in full.
   - Corollary: **c∧(MAJ_n) ≥ n − B(n)**.
   - This improves an earlier bound, which was previously known only for n = 2^k (relayed).
4. **Open problem (verbatim sense, from snippet).** The paper says that providing an **explicit function f on n variables with c∧(f) > n is an important open problem**.

## Why it matters for NP-FRONTIER

- Item 4 is the most direct published confirmation that index item (c) is open. Note the problem is stated with ">" n.
- The D⊕ route can never give more than n − 1 for single-output functions, since D⊕(f) ≤ n.
- **Consequence of (a).** If the fresh-variable lemma holds, the problem would be solved at the level n + O(1) via finite seeds (index observation D1). With the known explicit 6-variable seeds it would give only MC = n, not > n.

## Limitations

- Snippet-level access only.
- The open-problem sentence was seen only in a search summary, not in context.

## Retrieval

- Title, authors, ECCC number and date, arXiv ID, affiliations and items 1–2: from WebSearch summaries of ECCC (report/2018/174, revisions 1 and 2), arXiv/ar5iv, DeepAI and Emergent Mind.
- Item 3 (definition of c∧, inductive argument, majority corollary): from WebSearch summaries of the arXiv PDF and ECCC revision 2.
- Item 4: from a WebSearch summary that quoted the paper as saying an explicit f with c∧(f) > n is an (important) open problem.
- Publication venue: one search found none.
