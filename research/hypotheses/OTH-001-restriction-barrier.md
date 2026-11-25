# OTH-001: One-restriction-per-gate arguments cannot prove MC ≥ n

**Status:** REVIEWED (AUDIT-001). The formal statement survives but is **elementary**. The original framing was **overclaimed** and has been corrected below.

**Correction after AUDIT-001.**
1. The restriction depth D equals D⊕ − 1, where D⊕ is ordinary parity decision tree depth. So the cap reads: restriction-robust (P1) measures are at most D⊕ − 1 ≤ n − 1.
2. The cap applies only to measures with property (P1). It does **not** apply to every one-AND-gate-per-restriction induction. Witness: the pair measure from Lemma 9 gives 3 > D = 2 on g*. For general one-gate-per-restriction inductions, only the folklore dimension count (≤ n − 1) applies.
3. The real content is the folklore dimension count, plus a precise description of which arguments stop at the PDT bound. Related prior work: Golovnev–Hirsch–Knop–Kulikov, "On the limits of gate elimination".

## Statement
Call μ restriction-robust if it is affine-invariant, μ(affine) = 0, and for every f and every hyperplane direction v, some restriction f|_{⟨v,x⟩=c} has μ ≥ μ(f) − 1. Then μ ≤ D ≤ n − 1, where D is the restriction depth. Also D ≤ MC.
Hence every MC lower bound proved by eliminating one AND gate per hyperplane restriction is at most n − 1. This includes the classical degree bound MC ≥ deg − 1. Proofs: Lemma 2 and Theorem 8 in `research/proofs/PNE-001-restriction-depth-and-fresh-variables.md`.

## Relevance
It explains why explicit single-output MC lower bounds stop at n − 1. The literature agent found every known single-output technique (degree, parity decision trees, affine restrictions, dimension, nonlinearity) capped at n − 1 or lower. It also says what a proof of MC ≥ n must contain:
(i) restrictions that provably kill ≥ 2 AND gates in every optimal circuit;
(ii) counting or pigeonhole over circuit structures (the non-constructive M(7) ≥ 7 of Codish–Cruz-Filipe–Frank–Schneider-Kamp, arXiv 1508.05737, per search results);
(iii) exhaustive computation on a fixed base function plus a composition theorem such as PNE-001.
This is the MC analogue of known limits of gate elimination for full-basis circuits (Golovnev–Hirsch–Knop–Kulikov; see `research/literature/golovnev-2016-gate-elimination-limits.md`).

## Barriers
Linear lower bounds in a restricted measure. Relativization, natural proofs and algebrization are not the binding constraints at this scale: natural proofs concern superpolynomial bounds. The binding constraint is the restriction cap proved here.

## Novelty
Lemma 1 is essentially known: Chistopolskaya–Podolskii (arXiv 1810.08668) prove D_⊕(f) ≤ c∧(f) + 1 by the same induction (per search summaries). The cap statement and its use for the fresh-variable question were not found.
