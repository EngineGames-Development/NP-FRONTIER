# Open questions (ranked; updated in cycle 003)

0. **Novelty of Theorem 4.** Read "Direct Sums for Parity Decision Trees" (arXiv 2412.06552, CCC 2025) when accessible; it may contain or imply D(y·g) = D(g)+1.
1a. **PNE-001 at level 5: codimension 4 (cycle 003).**
- Corollary 33 settles every level whenever dim(g) ≥ 2MC(g) − 3; this is a human proof, AUDIT-004.
- Level 5 is exactly the following question (Corollary 35). Is there a 6-variable g with MC(g) = 5 = MC(y·g)? Equivalently, a formal 5-gate circuit, a 6-dimensional K ⊆ F_2^10 and cosets C0 ≠ C with Φ|C0 affine and MC(Φ|C) = 5?
- Known so far:
  - Lemma 37 covers perturbations of the top two gates.
  - The only configuration not covered by a written argument is NEW-2: dim π(H) = 2, dim H0 = 2, the non-separating t2 eliminates a private variable of gate m−1, and the separating t1 has a lower top gate. The dim π(H) = 1 branch also still needs a write-up.
  - In EXP-019, every sampled instance has a 4-gate circuit, often by rewiring the gates between the top of t1 and gate m−1.
- Two routes:
  - a human proof of NEW-2, which would give codimension 4 for every m and hence level 5;
  - a complete computation over the 35,861 NIST classes that pass Lemma 36, times 64 linear forms. This needs sharper necessary conditions or a large symmetry reduction of formal circuits, using GL(2) per gate and the moves z_i ↦ z_i + A_i.
1b. **Novelty of PNE-001.** A 2016 NIST email claims MC(uv·f) = 1 + MC(v·f) via an unreleased attachment. Was the general fresh-variable lemma known? The s5 question is settled as a normalization: s5 = (63/31) × our count exactly (AUDIT-003 I-7). The slide's convention is still unread.
1. **PNE-001, general case (cycle-001 text; superseded for levels ≤ 4 by 1a).** Level 3 (MC(g) = 3) reduces to 33 explicit orbit representatives on 5 variables (Theorem 16, EXP-006). Level 4 is open: a counterexample needs two cheap directions with halves of MC ≤ 2 (Lemma 12). Lemma 14(a) has no analogue for MC-2 halves, so a new structural idea is needed. Is MC(y·g) = MC(g) + 1 for every non-constant g? It is proved when MC(g) = D(g), which covers every g on ≤ 4 variables. It can fail only where MC(g) > D(g); the first such functions are on 5 variables (g* = 0xfff3d212). Next: certify MC(y·g*) = 4 (SAT UNSAT plus DRAT; see the cycle report), then test every certified 5-variable function with MC > D.
2. **A lower-bound principle that pays for both branches.** Restriction depth charges max(branch), circuits pay roughly sum(branches) (the multiplexer gap behind g*). Precise target, the multiplexer lemma: for P(u), Q(v) on disjoint variables and a fresh selector s, MC((1+s)P + sQ) = MC(P) + MC(Q) + 1. It implies PNE-001 (take P = 0). Iterated as a decision list over hard constant-size blocks, it would give explicit MC ≥ cn for every c. So the general lemma is as strong as PNE-002 and believed hard. Bounded versions, such as P and Q of MC ≤ 2, are tractable test cases.
3. **Explicit MC > n (open problem stated by Chistopolskaya–Podolskii).** Through PNE-001, MC = n needs a certified 6-variable seed with MC 6, and MC > n needs a certified seed with MC(g) ≥ k + 1. Obtain g₆ from ePrint 2018/002, or find one by search with an UNSAT certificate at k = 5, then test MC(g₆·y) = 7.
4. **Classification on 5 variables.** For each of the 48 extended-affine classes of 5-variable functions, determine (MC, D). Which classes have MC > D? EXP-002 has 209+ undecided samples with D = 3 and degree 4.
5. **Lean.** Formalize Lemma 1 and Theorem 4 (XOR-AND circuits, affine restrictions, coordinate changes over 𝔽₂) in core Lean, or set up a Mathlib build. Mathlib's cache host cache.mathlib.org is blocked; allowing it would let us use Mathlib.
6. **PEQ track.** Candidates outside the reach of known proof-system lower bounds. First check: the status of lower bounds for resolution over parities, Res(⊕), and for bounded-width Res(⊕), relevant to propagation plus Gaussian elimination.
7. **Frontier verification.** ECCC TR26-260 (Mishra–Santhanam, Oct 2026) claims 3.5n − o(n) for explicit functions over the full binary basis. Unrefereed and unread (eccc.weizmann.ac.il is blocked here).
