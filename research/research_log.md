# Research log (append-only)

## 2026-11-25 — Cycle 001

- **Setup.** Added hypothesis ID scheme (CLAUDE.md §10), layout (§9), idempotent init rule (§15) and `scripts/setup_env.sh`. Added six role definitions in `.claude/agents/`; they register at the next session start, so this session used general-purpose agents told to adopt them. Lean 4.37.0-rc1 core project at `research/proofs/lean`. Mathlib is unusable here because its cache host is blocked.
- **Literature (two background agents, WebSearch only; arXiv and ECCC full texts unreachable).** 23 records on barriers, the circuit frontier and PEQ no-go theorems; 24 records on MC. Key facts:
  - The best explicit single-output MC bound is n − 1.
  - An explicit f with MC > n is called an important open problem (Chistopolskaya–Podolskii).
  - The fresh-variable lemma was not found stated anywhere.
  - An unrefereed 3.5n circuit lower bound claim exists (ECCC TR26-260).
- **Choice of narrow question.** I scouted MC because exact small cases are computable, proofs are feasible, and the degree barrier at n − 1 is sharp. I selected PNE-001, the fresh-variable lemma MC(y·g) = MC(g) + 1. It is the smallest composition statement that would move explicit bounds past n − 1 (via 6-variable seeds with MC 6). The full composition, PNE-002, implies explicit cn circuit bounds for all c, so I treated it as out of reach.
- **EXP-001.** Exact MC of all 4-variable functions by span BFS: 32/1120/31616/32768 for MC 0..3; MC 3 exactly when the degree is 4. The SAT tool was validated. UNSAT on 5–6 variables is slow.
- **Theory.** Defined the restriction depth D (parity decision tree depth with affine leaves). Proved:
  - D ≤ MC. Later found essentially known: Chistopolskaya–Podolskii prove D⊕ ≤ MC + 1.
  - Restriction-robust measures are ≤ D ≤ n − 1 (the barrier, OTH-001).
  - Theorem 4: D(y·g) = D(g) + 1.
  - Corollary: PNE-001 holds whenever MC(g) = D(g).
  - An earlier attempt, a direct substitution argument on the first y-gate, gave only MC(g) ≤ 2m − t − 1. It fails because the two halves g·α and g·(1+α) need separate gates. Recorded in the proof document's analysis.
- **EXP-002.** MC = D on all 4-variable functions, so PNE-001 holds for all g on ≤ 4 variables. On 5 variables MC > D occurs: g* = 0xfff3d212 (deg 3, D 2, MC 3; no 2-AND circuit, by an exhaustive SAT-free check). Structure: a multiplexer of two rank-2 quadratics.
- **EXP-003.** SAT: no 3-AND circuit computes y·g* (305 s). A DRAT certificate was requested and checked with drat-trim; outcome is in the cycle report. This is the first test of PNE-001 outside Theorem 4's reach.
- **Lean.** Verified theorems, all with standard axioms only:
  - the ANF is correct (`peval_anf`) and linear;
  - the top coefficient equals the weight parity;
  - full degree iff odd weight;
  - degree is subadditive under XOR;
  - Lemma 3 for coordinate hyperplanes; restriction does not increase degree;
  - the two Boolean identities used in Theorem 4.
- **PEQ track.** PEQ-001 (bounded-width propagation) and PEQ-002 (compact LP/SDP) were stated precisely and found DISPROVED by known theorems. Extracted the proof-system simulation principle as a screening test. No new PEQ mathematics this cycle.
- **Review.** Adversarial audit of the proof document requested from a fresh agent; verdict recorded in `research/proofs/audits/AUDIT-001-PNE-001.md`.
