# Chen, Hirahara, Oliveira, Pich, Rajgopal, Santhanam (2020): Beyond Natural Proofs: Hardness Magnification and Locality

| Field | Value |
|---|---|
| Title | Beyond Natural Proofs: Hardness Magnification and Locality |
| Authors | Lijie Chen, Shuichi Hirahara, Igor C. Oliveira, Ján Pich, Ninad Rajgopal, Rahul Santhanam |
| Year | 2020 (conference); 2022 (journal) |
| Venues | 11th ITCS (2020), LIPIcs vol. 151, pp. 70:1–70:48, DOI 10.4230/LIPIcs.ITCS.2020.70. Journal of the ACM, 2022: volume/issue/article number **not confirmed** (recalled as 69(4), unverified); MIT DSpace record hdl 1721.1/146303 |
| Preprints | ECCC TR19-168 (20 Nov 2019); arXiv 1911.08297 |
| Group | Barrier (locality barrier for hardness magnification) |

## Background: hardness magnification

Hardness magnification (term introduced by Oliveira–Santhanam, FOCS 2018): for certain problems Q, a barely non-trivial lower bound for Q against a weak model already implies a strong separation. Typical examples (recalled; the specific problem/model/separation pairings are unverified, except EXP ⊄ NC¹, which appears in this paper's abstract as summarized by WebSearch):
- Q: gap versions of the Minimum Circuit Size Problem (MCSP) and of time-bounded Kolmogorov complexity (MKtP).
- Barely non-trivial bound: size N^{1+ε} against formulas or circuits, where N is the input length.
- Strong separation: NP ⊄ NC¹, EXP ⊄ NC¹, NP ⊄ P/poly.

Background references:
- Oliveira–Santhanam: ECCC TR18-139, DOI 10.1109/FOCS.2018.00016 (confirmed via WebSearch).
- Follow-ups: Oliveira–Pich–Santhanam ("Hardness Magnification near State-Of-The-Art Lower Bounds", Theory of Computing 2021, via WebSearch summary), and others.

## Relevant results

Confirmed at abstract level; quantitative parameters not checked.

**(a) Magnification can go beyond natural proofs.** Slightly superlinear-size circuit lower bounds for certain versions of MCSP imply that natural proofs do not exist. Two consequences:
- Such a lower bound cannot itself have a natural proof (that would be self-defeating).
- Such magnification theorems also rule out efficient learning algorithms, because the non-existence of natural proofs implies the non-existence of efficient learners.

**(b) Locality barrier.** Two facts collide:
- Existing magnification theorems show **unconditionally** that the problems Q they use have highly efficient circuits in the weak model once the model is extended with **oracle gates of small fan-in** (the oracle gates may compute arbitrary functions).
- Lower-bound techniques against weak models (random restrictions and shrinkage for formulas, polynomial approximation, many communication-style arguments) usually **extend to circuits with such small-fan-in oracle gates**.

So such a technique, applied to Q, would also give a lower bound for the oracle-augmented model. That lower bound is false, because efficient oracle circuits for Q exist. Direct adaptations of these techniques therefore cannot reach the magnification threshold.

## What it rules out or limits

It rules out a specific P ≠ NP (or NP ⊄ P/poly, EXP ⊄ NC¹) strategy: prove the slightly superlinear lower bound for a magnification target Q with a technique that **localizes**, meaning it remains valid when the circuit may contain arbitrary oracle gates of small fan-in. Any successful technique must be sensitive to non-local, global features of the computation.

## Why it matters for NP-FRONTIER

Magnification looks attractive because the needed lower bounds look "almost known". This record explains why the obvious adaptations fail. A hypothesis in the magnification program must state why its technique does **not** extend to small-fan-in oracle gates.

## Limitations

- The barrier is shown for specific magnification theorems and specific techniques. The authors state they believe it applies more broadly (via WebSearch summary); it is not a theorem about all proofs.
- It is a meta-barrier against adapting known techniques, not an impossibility result.
- Follow-ups extend the analysis: "Localizability of the approximation method" (arXiv 2212.09285; title seen via WebSearch, authors not confirmed) applies it to the monotone approximation method.

## Check to apply to a hypothesis

If a hypothesis claims a lower bound for MCSP, MKtP or another magnification target via technique T, ask: does T prove the same lower bound for circuits augmented with arbitrary oracle gates of fan-in N^{o(1)} (or polylog N)? If yes, T cannot succeed, because the magnification theorems provide efficient circuits of that kind. Reject or redesign.

## Retrieval

- Author list, ITCS 2020 venue with LIPIcs pages 70:1–70:48 and DOI, ECCC TR19-168 (dated 20 Nov 2019) and arXiv 1911.08297: confirmed by WebSearch (Dagstuhl/LIPIcs BibTeX, ECCC listing, arXiv PDF link; result summaries).
- JACM 2022: confirmed by WebSearch summary of the MIT DSpace record (ISSN 0004-5411, date 2022-08-23). Volume, issue and article number not confirmed.
- Statements (a) and (b): confirmed at abstract level via WebSearch summaries of the ECCC, arXiv and Dagstuhl abstracts. The exact MCSP parameters, oracle fan-in bounds and circuit models were not checked.
- Oliveira–Santhanam (FOCS 2018) data: confirmed via WebSearch (ECCC TR18-139 page and UK REF 2021 record).
