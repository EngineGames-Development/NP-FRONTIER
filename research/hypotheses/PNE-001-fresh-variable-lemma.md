# PNE-001: Fresh-variable lemma for multiplicative complexity

**Status:** PROOF ATTEMPT. **Proved (computer-assisted, Theorem 17) for every g with MC(g) ≤ 3, on any number of variables.** Also proved for every g with MC(g) = D(g), which includes every g on ≤ 4 variables. Also proved for every g with MC(g) = 3 and a single cheap direction (Corollary 13). Verified for g* (three independent methods) and for all 38 sampled 5-variable functions with MC 3 > D 2 (EXP-004/005; see the cycle report for the 7 three-direction cases). Open in general. Audit pending.

## Formulation
MC(f) is the least number of AND gates in a circuit over {AND, XOR, 1}. Claim: for every non-constant g: F₂ⁿ → F₂ and a fresh variable y, **MC(y·g) = MC(g) + 1**.
Since MC(g) ≤ MC(y·g) ≤ MC(g)+1 always, the claim says only that multiplying by a new variable is never free.

## Motivation
- For ordinary circuit size the analogue is trivial by gate elimination: setting y = 1 kills a gate fed by y. For MC it is not trivial, because y can enter only through free XOR gates.
- **Explicit lower bounds.** An explicit single-output function with MC > n is called "an important open problem" by Chistopolskaya–Podolskii (arXiv 1810.08668, per search-result abstract). The best explicit single-output bound is n − 1, from the degree. If PNE-001 holds for one explicit 6-variable function g₆ with MC(g₆) = 6 (such functions are reported by Çalık–Sönmez Turan–Peralta, ePrint 2018/002), then f_n = g₆·x₇⋯x_n is an explicit family with MC(f_n) = n. That is one more than the best known explicit n − 1, but not the strict MC > n of the stated open problem. A strict bound needs a certified seed with MC(g) ≥ k+1 on k variables. Counting shows such seeds exist for k ≥ 8, but none is certified. With seeds on log log n variables the bound would be n + Ω(√log n), never n + Ω(n). This is a step past the degree barrier for a restricted measure, not a P ≠ NP result.
- PNE-001 is the one-variable case of PNE-002 (AND-direct sum), which would imply explicit linear circuit lower bounds with every constant.

## Results (research/proofs/PNE-001-restriction-depth-and-fresh-variables.md)
Note after AUDIT-001: D = D⊕ − 1 for non-constant f, where D⊕ is parity decision tree depth. So Theorem 4 says D⊕(y∧g) = D⊕(g) + 1; its novelty is unconfirmed, and it may be folklore in the PDT literature. Lemma 1 is identical to Chistopolskaya–Podolskii's D⊕ ≤ MC + 1.
- Theorem 4: D(y·g) = D(g) + 1, where D is the restriction depth (parity decision tree depth with affine leaves).
- Lemma 1: D ≤ MC. Corollary 5: MC(y·g) ≥ D(g) + 1, so PNE-001 holds whenever MC(g) = D(g).
- Corollary 6 (computer-assisted, exact): MC = D for all 65,536 functions on 4 variables, so PNE-001 holds for all g on ≤ 4 variables.
- Theorem 8: restriction-robust arguments are capped at D ≤ n − 1 (see OTH-001). So PNE-001 for g₆ needs a non-restriction argument.

## Evidence on 5 variables (EXP-002)
- Functions with MC > D exist on 5 variables. Example g* = 0xfff3d212, with ANF x1+x3+x5+x1x2+x2x3+x1x5+x2x5+x3x5+x2x3x4+x1x2x5+x2x4x5. It has deg 3, D = 2 (query x2), and MC = 3: a 3-AND circuit was found, and an exhaustive search with no SAT solver shows no 2-AND circuit exists.
- Structure: g* = (1+x2)·[1+(1+x1+x3)(1+x5)] + x2·MAJ(x3,x4,x5) is a multiplexer of two rank-2 quadratics. The decision tree pays for one branch (depth), while a circuit pays for both branches.
- This is the first open case of PNE-001: is MC(y·g*) equal to 3 or 4? The one-level restriction bound gives only 3, because restricting x2 leaves y·P and y·Q with MC 2 each. EXP-003 runs SAT on "MC(y·g*) ≤ 3" (6 variables).

## Counterexample attempts
- EXP-003 (SAT, 6 variables, k = 3) for g*: see `research/experiments/EXP-002-restriction-depth/fresh_test_*.log` for the result.
- A counterexample circuit must, at its first y-gate, use A = y + α with α non-constant, and must share AND gates between the two halves g·α and g·(1+α). This is shown in the proof document's analysis: if y enters only at the last gate, or with α constant, then MC(g) ≤ MC(y·g) − 1.

## Literature
Not found as a stated result; MC literature agent confidence ≈ 70% that it is unaddressed. See `research/literature/index-multiplicative-complexity.md`.

## Formalization
Lean: only the algebraic identities used in Theorem 4 (`gate_normalize`, `mul_eval_one`) and the degree lemmas. Theorem 4 itself is not formalized.

## Next steps
1. Settle MC(y·g*) (SAT UNSAT plus an independent check, or a counterexample circuit).
2. Classify the 5-variable functions with MC > D (EXP-002 candidates). Test PNE-001 on each.
3. Look for a lower-bound principle that survives the multiplexer gap: a measure that charges for both branches of a split, valid for circuits but not for decision trees.
4. Obtain an explicit g₆ with MC 6 (from ePrint 2018/002, or by search plus an UNSAT certificate). Then test whether MC(g₆·y) = 7.

## Update (cycle 001, after restart)
- Lemma 9 (first-gate criterion) and Lemmas 11–12: a counterexample at level m needs two distinct directions of g whose halves both have MC ≤ m − 2. The admissible directions for y·g come in pairs {(v,0),(v,1)}.
- Corollary 13: at level 3, a single cheap direction suffices for PNE-001. EXP-005: 31 of 38 sampled MC-3 functions have one cheap direction; 7 have three, forming a plane.
- Refuted: "MC = 3 implies one cheap direction" (e.g. 0x47fca912).
- Lemma 14: plane-type functions have the form g = h(x') + Λ with MC(h) ≤ 1. This is the starting point for a hand proof of the plane case.
- Proposition 10: MC(y·g*) = 4, by Corollary 13, by the exhaustive first-gate certificate, and by SAT with a DRAT proof checked by drat-trim.
