# Murray, Williams (2018): Circuit lower bounds for nondeterministic quasi-polytime

| Field | Value |
|---|---|
| Title (STOC) | Circuit Lower Bounds for Nondeterministic Quasi-Polytime: An Easy Witness Lemma for NP and NQP |
| Title (journal) | Circuit Lower Bounds for Nondeterministic Quasi-polytime from a New Easy Witness Lemma |
| Authors | Cody Murray, R. Ryan Williams |
| Year | 2018 (conference); 2020 (journal) |
| Venues | 50th ACM STOC (2018), pp. 890–901. SIAM Journal on Computing 49(5), 2020 (page range **not confirmed**) |
| Preprint | ECCC TR17-188 (December 2017) |
| Group | Circuit lower bound frontier (restricted model: ACC0 ∘ THR) |

## Definitions

- **NQP** = NTIME[n^{(log n)^{O(1)}}] (nondeterministic quasi-polynomial time). NQP ⊇ NP.
- **ACC0 ∘ THR:** ACC0 circuits whose bottom layer consists of linear threshold gates (recalled).

## Relevant theorems

Confirmed at abstract level.
1. **Easy Witness Lemma for NP.** If NP has circuits of size n^k for a fixed constant k, then every yes-instance of every NP verifier has a witness that is the truth table of a circuit of size n^{O(k^3)}.
2. **Analogous lemma for NQP.**
3. **Lower bound (corollary).** For every fixed k, NQP does not have ACC0 ∘ THR circuits of size n^{log^k n}.

The corollary is obtained by combining the lemma with known non-trivial satisfiability algorithms for ACC0 ∘ THR circuits, in Williams's algorithmic method.

Context: the easy witness lemma of Impagliazzo, Kabanets and Wigderson held only for larger classes such as NEXP. Bringing it down to NP and NQP is what allows the uniform class in the lower bound to drop from NEXP to NQP.

## What it rules out or limits

Frontier calibration:
- The strongest uniform-class lower bound against ACC0-type circuits is for NQP. Even **NP ⊄ ACC0** is open.
- A hypothesis whose corollaries include NP ⊄ ACC0 (or NP ⊄ ACC0∘THR) is claiming an open result.

## Why it matters for NP-FRONTIER

- It shows how far the algorithmic method has come (NEXP → NQP) and how far it is from NP vs P/poly.
- The easy witness lemma for NP is a useful structural tool. If NP has small circuits, NP witnesses are compressible. Hypotheses on either side can use it, but must cite the exact parameters, n^{O(k^3)}.

## Limitations

- Restricted circuit model.
- Lower bound for NQP, not NP.
- SICOMP page range not confirmed.
- Subsequent strengthenings of this line exist (e.g. average-case and almost-everywhere versions); they are not checked here.

## Retrieval

- STOC 2018 pp. 890–901, ECCC TR17-188 (Dec 2017) and the SICOMP 49(5) (2020) journal version with its changed title: confirmed by WebSearch (MIT DSpace records, IAS page, researchr; result summaries). SICOMP pages not found.
- Theorem statements (n^{O(k^3)} witness circuits; NQP analogue; NQP ⊄ ACC∘THR of size n^{log^k n}): confirmed via WebSearch summary of the abstract.
- Definition of ACC0∘THR: recalled.
