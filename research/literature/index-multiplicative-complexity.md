# Index: multiplicative complexity (MC) of Boolean functions. Literature map and novelty check

- **Agent:** D (Theory and Literature Researcher).
- **Date:** 2026-11-25.
- **Method:** WebSearch only, about 70 queries. arXiv, ECCC and publisher pages could not be fetched, so every statement below is at abstract or snippet level unless marked otherwise.
- **Scope:** novelty check of
  - (a) the fresh-variable lemma,
  - (b) the AND-direct sum, for MC and for ordinary circuit size,
  - (c) explicit MC lower bounds;
  plus source records for the main MC papers.

## Notation

- **MC(f) = c∧(f):** the minimum number of AND gates in a circuit over {AND, XOR, 1}. XOR gates and constants are free. This equals the minimum over {AND, XOR, NOT}. A circuit of this kind is called an XAG.
- **Vector-valued F = (f_1, …, f_m):** one circuit with m outputs.
- **C(f):** circuit size over the full binary basis B2. Note C(f) ≥ MC(f), because every binary gate is either affine or of AND type (a ⊕ c_1)(b ⊕ c_2) ⊕ c_3.
- **M(n):** the maximum of MC(f) over n-variable f.
- **deg f:** the degree of the GF(2) ANF.
- **"Explicit":** computable in time polynomial in n.

## Correction to the task brief

arXiv 1508.05737, "When Six Gates are Not Enough", is by **Codish, Cruz-Filipe, Frank and Schneider-Kamp** (2015). It is **not** by Find, Smith-Tone and Sönmez Turan. Two independent search results agree.

The Find–Smith-Tone–Sönmez Turan paper is "The Number of Boolean Functions with Multiplicative Complexity 2" (ePrint 2015/1041). See `mc-codish-2015-six-gates.md` and `mc-find-2015-mc-two.md`.

---

## Task 1 conclusions

### (a) Fresh-variable lemma: MC(g(x)·y) = MC(g) + 1 for every non-constant g, with y a new variable

**Status: NOT FOUND in the literature. No source states, proves or refutes it.** To our knowledge it is open and a candidate new statement.

**Trivial facts.** MC(g) ≤ MC(g·y) ≤ MC(g) + 1.
- The lower bound comes from setting y = 1; restriction never increases MC.
- The upper bound comes from one extra AND gate.
- So (a) is equivalent to MC(g·y) ≠ MC(g).

**Closest known results and their exact relationship to (a):**

| Known result | Relationship to (a) |
|---|---|
| Degree bound MC ≥ deg − 1 (`mc-schnorr-1988-degree-bound.md`) | **Implies (a) for every degree-tight g**, i.e. MC(g) = deg g − 1, since deg(g·y) = deg g + 1. Examples: MC ≤ 1 functions; x_1⋯x_n ⊕ q (`mc-selezneva-2015-degree-n-functions.md`). Says nothing when MC(g) ≥ deg g |
| Quadratic forms: MC = (symplectic rank)/2 (`mc-mirwald-1992-quadratic-forms.md`) | Combined with the standard affine-restriction technique, **implies (a) for every quadratic g**. This is Agent D's derivation D4 below; it is not stated in any source seen |
| Twin-variable bound C∧(x_1x_2f_1 + f_2) ≤ 1 + C∧(x_1f_1 + f_2) (`mc-brandao-2019-symmetric-twin-variables.md`) | With f_2 = 0 this is the trivial **upper** half of (a) for g = x_1f_1, y = x_2. (a) says this reduction is tight there. Neither implies nor refutes (a) |
| M(7) ≥ 7 by a dedicated pigeonhole argument (`mc-codish-2015-six-gates.md`). "A counting argument shows" n-variable functions with MC ≥ n for n ≥ 7 (`mc-calik-2018-six-variables.md`) | Circumstantial only. If (a) were a standard tool, M(7) ≥ 7 would follow at once from M(6) = 6, with an explicit witness g6·x_7. The 2018 abstract instead cites counting. This is weak evidence that (a) is not established; the 2015 paper predates M(6) = 6 |
| D⊕(f) ≤ c∧(f) + 1 (`mc-chistopolskaya-2018-parity-decision-trees.md`) | Unrelated as a route to (a): wrong direction, and capped at n |
| Over B2: C(f ∧ y) = C(f) + 1 | Trivial by gate elimination, since setting y = 1 kills a successor of y. Not transferable to MC, because y may enter only through free XOR gates, so no AND input need become constant |

**Consequence if (a) is true** (observation D1): an explicit family with MC(f_n) = n exactly for all n ≥ 6. With larger finite seeds it gives an explicit family with MC ≥ n + c, and even n + Ω(√log n). It can never give more than n + o(n).

**Confidence:** moderate, about 70%, that (a) is not stated as a theorem anywhere in the literature.
- Limits: only abstracts and snippets were seen; the full texts of Çalık et al., Find et al. and Selezneva were not read; Russian-language literature was only lightly searched (two queries).
- A lemma buried in a paper body cannot be excluded.

### (b) AND-direct sum

**(b-MC): MC(g(x)·h(y)) = MC(g) + MC(h) + 1 for disjoint variable sets.**

**Status: NOT FOUND; no source states, proves or refutes it.**

Known special cases:
- If g and h are both degree-tight, (b-MC) holds by the degree bound, since deg(gh) = deg g + deg h.
- h = y is item (a).

Related but different statements:
- Mirwald–Schnorr characterize when L(f_1, f_2) = L(f_1) + L(f_2) for quadratic forms. That is a **two-output** direct sum, not AND-composition.
- Besselman et al. (CCC 2025) prove direct sums for **randomized parity decision trees** with k copies. That is a different model and a different composition.

**Strength of (b-MC)** (observation D2):
- (b-MC) in full generality, even in the weak additive form MC(gh) ≥ MC(g) + MC(h), implies an explicit function in P with superlinear MC, hence superlinear B2 circuit size.
- That is far beyond the explicit frontier of 3.1n − o(n) (`li-2022-3.1n-lower-bound.md`; 3.5n claimed in `mishra-2026-3.5n-lower-bound.md`).
- So (b-MC) is either false in general or a breakthrough-strength statement.
- By analogy with Uhlig's theorem (D3) it plausibly fails for random-like g = h, but **no MC analogue of Uhlig's theorem was found**.

**Even a narrow case would be new.** (b-MC) restricted to disjoint copies of an explicit 6-variable MC-6 function g6 would give MC = 7k − 1 = (7/6)n − 1 on n = 6k variables (D2'). That would be a new explicit single-output bound exceeding n.

**(b-C): C(f ∧ g) = C(f) + C(g) + 1 over B2, for disjoint variables.**

**Status: FALSE in general.** This is Agent D's deduction from published theorems (D3); the deduction itself was not found written down.
1. Uhlig's mass-production theorem (`mc-uhlig-1974-mass-production.md`), as restated by Kretschmer (TQC 2023): for every f on n bits, f(x), f(y) can be computed together with (1 + o(1))·2^n/n gates.
2. Shannon's counting: almost all f have C(f) ≥ (1 − o(1))·2^n/n.
3. Hence for almost all f, C(f(x) ∧ f(y)) ≤ (1 + o(1))·2^n/n + 1 < 2C(f) + 1.

Paul (1976) (`mc-paul-1976-disjoint-variables.md`) apparently shows this kind of failure directly: arbitrarily complex f with two-copy cost within a factor 1 + ε of C(f), including an OR-composition. Every snippet was garbled, so the exact statement is **unverified**.

Two related facts that remain true:
- The fresh-variable case C(f ∧ y) = C(f) + 1 is trivial over B2.
- For De Morgan formula leaf-size, L(f ∧ g) = L(f) + L(g) holds trivially by a restriction argument on leaves. This is recalled, standard, and was not searched.

**Confidence:** high, about 85%, that (b-C) is false in general. It rests on the restatement of Uhlig's theorem with constant 1 + o(1) and on the standard Shannon bound.

### (c) Explicit single-output MC lower bounds

**Best known explicit single-output bound: n − 1**, from the degree bound, e.g. x_1⋯x_n.
- Kojevnikov–Kulikov (CiE 2010) and Demenkov–Kulikov (MFCS 2011) each state that n − 1 is the best known explicit MC lower bound.
- Chistopolskaya–Podolskii (ECCC TR18-174 / arXiv 1810.08668) state that **"providing an explicit function f on n variables with c∧(f) > n is an important open problem."**
- Searches covering 2019–2026 found **no** explicit family with MC(f_n) ≥ n for all large n, and none with > n.

**Finite and non-explicit facts:**
- M(4) = 3 and M(5) = 4 (Sönmez Turan–Peralta 2014).
- M(6) = 6, with **explicit 6-variable functions of MC exactly 6** exhibited by Çalık–Sönmez Turan–Peralta. **These functions were not visible in any snippet**; they must be taken from ePrint 2018/002.
- M(7) ≥ 7, non-constructive (Codish et al. 2015). M(7) ≤ 13 (NIST BFA 2022 slides).
- An 8-variable function with MC > 7 exists by the BPP 2000 counting bound (non-constructive).
- Almost all functions have MC ≥ 2^{n/2} − O(n) (BPP 2000; non-explicit).

**Other explicit single-output bounds, all ≤ n − 1:**
- c∧(MAJ_n) ≥ n − B(n) (Chistopolskaya–Podolskii).
- Affine dispersers for dimension d: MC ≥ n − d − 1 (Demenkov–Kulikov).
- x_1⋯x_n ⊕ q, deg q = 2: MC = n − 1 exactly (Selezneva 2015).

**Best explicit vector-valued bound:**
- The (n, n)-function f_i = ∏_{j≠i} x_j has MC ≥ **2n − 3** (Boyar–Find; arXiv 1407.6169, TCS 2018). It is **exactly 2n − 3** (Häner 2023, arXiv 2307.07424).
- Hamming weight: exactly n − H_N(n) (Boyar–Peralta 2008), which is below n.
- Note D6: m outputs linearly independent modulo affine functions trivially need ≥ m ANDs. So "vector-valued" bounds are interesting only when they exceed max(n, m), as 2n − 3 does for (n, n).

**Why the known techniques stall at n − 1:** see D5.

**Confidence:** fairly high, about 80%, that no explicit single-output family with MC ≥ n for all large n is known in the published literature as of November 2026.
- Support: two independent "best known = n − 1" statements, an "open problem" statement, and no contrary hit in targeted 2019–2026 searches.
- Not exhaustive; snippets only.

---

## Observations derived during this check

**Status:** these are Agent D's own reasoning, **NOT from the literature**, and have **not been independently reviewed**. They must go to Agent F before use.

**D1. (a) gives an explicit family with MC = n.**
- Let g6 be one of Çalık et al.'s explicit 6-variable functions with MC(g6) = 6.
- If (a) holds, f_n := g6(x_1, …, x_6)·x_7⋯x_n has MC(f_n) = n for all n ≥ 6. The proof is induction on n, with the upper bound by construction. f_n is in P.
- More generally, take any m-variable seed s with MC(s) ≥ m + c. Such seeds exist for large m by BPP counting, and a seed on m = log₂log₂ n variables can be found by exhaustive search in poly(n) time.
- Then (a) gives an explicit family with MC ≥ n + c. With the growing seed, the gain is about √(log n), i.e. MC(f_n) ≥ n + Ω(√log n).
- (a) alone cannot give n + Ω(n).

**D2. (b-MC) gives explicit superlinear lower bounds.**
1. Assume MC(g·h) ≥ MC(g) + MC(h) for all non-constant g, h on disjoint variables.
2. Let m = ⌈log₂log₂ n⌉ and T = 2^{m/2} − O(m).
   - Enumerate all XAGs on m inputs with fewer than T AND gates. There are 2^{O(2^m)} = n^{O(1)} of them.
   - Pick a function h not computed by any of them; it exists by BPP 2000 counting.
3. Define f_n := ∏_{i ≤ n/m} h(x^{(i)}) on disjoint blocks. Then f_n is in P.
4. Iterating the assumption, MC(f_n) ≥ (n/m)·T = Ω(n·√(log n)/log log n).
5. Since C ≥ MC, f_n has superlinear B2 circuit size.

The same conclusion holds for any additive variant, e.g. MC(gh) ≥ MC(g) + ε·MC(h).

**D2'. The narrow case of copies of g6.** If (b-MC) holds just for disjoint copies of g6, then MC(∏_{i ≤ k} g6(x^{(i)})) = 7k − 1 = (7/6)n − 1. That beats n − 1 by a constant factor.

**D3. (b-C) is false.** Shown in (b) above, using Uhlig and Shannon.

**D4. Lemma R and the quadratic case of (a).**

*Lemma R* (affine restriction for y·g). Suppose a circuit with k AND gates computes y·g(x). Then there is a non-constant affine B = B(x) (independent of y) such that MC(y·g|_{B=c}) ≤ k − 1 for **both** c ∈ {0, 1}. Here g|_{B=c} is viewed, after an affine change of coordinates, as a function of n − 1 variables.

*Proof of Lemma R.*
1. Take a topologically first AND gate A·B, where A and B are affine in (x, y).
2. If both A and B contain y, replace B by B' := 1 + A + B, which is y-free. This is valid because over GF(2), A·B = A·(1 + A + B).
3. If the resulting y-free input is constant, the gate is affine and can be removed; repeat with the next gate. A genuine gate must exist, because y·g has degree ≥ 2 for non-constant g.
4. Otherwise, restricting x to {B = c} makes the gate equal to c·A, which is affine.

*Quadratic case of (a).* The proof is by induction on n.
- If g is affine and non-constant, y·g has degree 2, so MC(y·g) = 1.
- If g is quadratic with symplectic rank 2r, then MC(g) = r.
  - Any hyperplane restriction keeps rank ≥ 2r − 2, so MC(g|_{B=c}) ≥ r − 1.
  - At least one side is non-constant, since otherwise g would be affine.
  - By induction, MC(y·g|_{B=c}) ≥ r on that side.
  - Lemma R then gives MC(y·g) ≥ r + 1.

*Structure of a minimal counterexample.* Let g be a counterexample to (a) with the fewest variables, and let k = MC(g).
- Then k ≥ 2, because MC ≤ 1 functions are degree-tight.
- There is a non-constant affine B with **MC(g|_{B=0}) ≤ k − 2 and MC(g|_{B=1}) ≤ k − 2**. This follows from Lemma R plus minimality.
- Combined with MC(g) ≤ MC(g|_{B=0}) + MC(g|_{B=1}) + 1, this forces k ≥ 3.
- g must be neither quadratic nor degree-tight.

So counterexample searches should target "multiplexer-like" functions g = (1 + B)h_0 + B·h_1 whose two restrictions are both much simpler than g.

**D5. Why single-output techniques stop at n − 1.**
- Degree: deg ≤ n, so the degree bound is ≤ n − 1.
- Parity decision trees: D⊕ ≤ n, so c∧ ≥ D⊕ − 1 gives ≤ n − 1.
- One-gate-per-affine-restriction arguments (Schnorr; affine dispersers): after n − 1 restrictions the domain is a line, on which every function is affine, so they give ≤ n − 1.
- Dimension: ⌈dim/2⌉ ≤ ⌈n/2⌉.
- Nonlinearity: at most about n/2. This relies on a recalled inequality, unverified.

Beating n − 1 needs an argument that removes more than one AND gate per restriction, or a non-restriction method. (a) would be exactly a "+1 per fresh variable" device.

**D6. Trivial multi-output bound.** If f_1, …, f_m are linearly independent modulo affine functions, then MC(f_1, …, f_m) ≥ m. Every wire is an affine combination of inputs and AND outputs.

---

## Suggested next checks (for Agents A, C, E, F)

1. **Verify (a) for every g on ≤ 5 variables.**
   - Look up MC(g·y), a 6-variable function, in the Çalık et al. 6-variable classification (NIST data; `mc-nist-2026-circuit-complexity-project.md`).
   - g on ≤ 4 variables can also be checked against the 5-variable tables.
   - This needs the class data and an affine-class canonicalizer.
2. **Test whether g6·x_7 has a 6-AND circuit**, for each explicit MC-6 function g6 from ePrint 2018/002, with SAT-based exact synthesis (`mc-soeken-2020-sat.md`).
   - "No" would give the **first explicit 7-variable function with MC 7**; M(7) ≥ 7 is currently known only non-constructively.
   - "Yes" refutes (a).
3. **Counterexample search for (a)** among multiplexer-type g that satisfy the minimal-counterexample conditions of D4.
4. **Small test of (b-MC):** determine MC((x_1x_2 + x_3x_4)(x_5x_6 + x_7x_8)).
   - The dimension bound gives ≥ 4; the naive circuit uses 5.
   - A value of 4 refutes (b-MC).
5. **Fetch the full texts** if any fetch route appears: Paul 1976 (exact theorems), Çalık et al. 2018 (the MC-6 functions), and Uhlig 1992.

---

## Source records (24 files in this directory)

| File | One line |
|---|---|
| `mc-schnorr-1988-degree-bound.md` | Degree bound MC ≥ deg − 1; prototype of the affine-restriction method |
| `mc-mirwald-1992-quadratic-forms.md` | MC of quadratic forms = rank/2; computational independence of pairs |
| `mc-boyar-2000-basis.md` | Boyar–Peralta–Pochuev: generic bounds; random f has MC ≥ 2^{n/2} − O(n); counting bound |
| `mc-boyar-2008-symmetric.md` | Symmetric functions; Hamming weight exactly n − H_N(n) |
| `mc-turan-2014-four-five-variables.md` | M(4) = 3, M(5) = 4 |
| `mc-calik-2018-six-variables.md` | M(6) = 6; explicit MC-6 functions exist (not visible); all 150,357 classes |
| `mc-codish-2015-six-gates.md` | M(7) ≥ 7 by pigeonhole (correct authors of arXiv 1508.05737) |
| `mc-find-2015-mc-two.md` | Count and classification of MC-2 functions |
| `mc-boyar-2014-vector-valued.md` | Boyar–Find: explicit (n, n)-function with MC ≥ 2n − 3; √(m2^n) upper bound |
| `mc-haner-2023-monomials.md` | The Boyar–Find function has MC exactly 2n − 3 |
| `mc-chistopolskaya-2018-parity-decision-trees.md` | D⊕ ≤ c∧ + 1; c∧(MAJ_n) ≥ n − B(n); explicit c∧ > n is open |
| `mc-kojevnikov-2010-circuit-vs-mc.md` | 7n/3 circuit bound via MC; "best explicit MC bound n − 1" |
| `mc-demenkov-2011-affine-dispersers.md` | MC(affine disperser) ≥ n − d − 1; "best explicit MC bound n − 1" |
| `mc-selezneva-2015-degree-n-functions.md` | MC(x_1⋯x_n ⊕ q) = n − 1 exactly |
| `mc-paul-1976-disjoint-variables.md` | Circuit size on disjoint variable sets; naive additivity fails (garbled, unverified) |
| `mc-uhlig-1974-mass-production.md` | r copies of f in (1 + o(1))2^n/n gates; refutes (b-C) via D3 |
| `mc-sonmezturan-2022-new-bounds.md` | Improved counting bound; M(7) ≤ 13 |
| `mc-nist-2026-circuit-complexity-project.md` | NIST project page; open problems; data |
| `mc-brandao-2019-symmetric-twin-variables.md` | Twin-variable reduction; trivial upper half of (a) |
| `mc-morse-2026-polynomial-multiplication.md` | Unrefereed 2026: unrestricted MC(Mul_4) = 9 with a Lean 4 formalization |
| `mc-soeken-2020-sat.md` | SAT-based exact MC; tool for the checks above |
| `mc-calik-2020-mc-three-four.md` | MC-3/4 classification; MC ≥ ⌈dim/2⌉ (retrieved cycle 002; class lists used in EXP-015) |
| `mc-peralta-2016-nist-email-fresh-variable.md` | 2016 NIST email: MC(uv·f) = 1 + MC(v·f), proof attachment not released (novelty of PNE-001 unconfirmed) |
| `mc-boyar-2013-nonlinearity-measures.md` | MC is incomparable with five other nonlinearity measures |
| `mc-find-2014-computing-nonlinearity.md` | Computing MC from a truth table is hard under cryptographic assumptions |

## Other sources seen (no separate record)

- **Besselman, Göös, Guo, Maystre, Yuan, "Direct Sums for Parity Decision Trees".**
  - arXiv 2412.06552; ECCC TR24-203; CCC 2025 (LIPIcs 339).
  - Content: direct sum for randomized PDTs when the lower bound comes from discrepancy or from a product distribution.
  - Relationship: different model and k-copy composition; unrelated to (a) and (b).
  - Retrieval: WebSearch summaries of arXiv, Dagstuhl and ECCC.
- **Kretschmer, "Quantum Mass Production Theorems".**
  - arXiv 2212.14399; TQC 2023 (LIPIcs 266).
  - Used as the secondary source for Uhlig's theorem.
- **arXiv 2611.15992, "The multiplicative complexity of the three-bit low-half multiplier" (2026).**
  - Claims MC(M_3) = 6. Authors not confirmed.
- **Häner, Soeken, "The multiplicative complexity of interval checking".**
  - arXiv 2201.10200; ePrint 2022/091; 2022.
  - Content: the exact AND cost of interval checking never exceeds that of one comparison. Single-output values below n.
- **I. S. Sergeev, "A relation between additive and multiplicative complexity of Boolean functions".**
  - arXiv 1303.4177; 2013.
  - Content: asymptotically tight relation between additive and multiplicative complexity over {⊕, ∧, 1}.
- **Bernasconi et al. (air.unimi.it).** MC of autosymmetric and D-reducible functions. Only the topic was seen.
- **A. S. Kulikov, doctoral dissertation (PDMI RAS).** Has a section "Multiplicative complexity and polynomials over F2". Only the table of contents was seen.
- **MathWorld "MultiplicativeComplexity".** A secondary source. It cites 2026 preprints and a "VibeMathed" page, so treat its recent content with caution.

## Search log (grouped; about 70 WebSearch queries, all in "standard" mode)

| Topic of queries | What the results confirmed | Negative results (relevant to novelty) |
|---|---|---|
| MC + "direct sum" / disjoint variables / f(x)g(y) / f(x) ⊕ g(y) / superadditive (6 queries, incl. one Russian) | Selezneva XOR-of-multiaffine bound; Sergeev; Mirwald–Schnorr computational independence | **No MC AND-direct-sum or XOR-direct-sum result or conjecture found** |
| MC + new variable / x_{n+1} / "f·y" / "MC(f)+1" / dependence lemma (5 queries, incl. one Russian) | Only the twin-variable upper bound (Brandão et al.) | **No fresh-variable lemma found** |
| Explicit MC lower bounds, "best known", "open problem", 2023–2026 (7 queries) | Kojevnikov–Kulikov and Demenkov–Kulikov: best explicit n − 1. Chistopolskaya–Podolskii: explicit c∧ > n is an important open problem. Boyar–Find 2n − 3 (vector-valued) | **No explicit single-output family with MC ≥ n found** |
| Bibliographic queries for each record (about 35 queries) | See each record's Retrieval field | arXiv 1508.05737 authorship differs from the brief |
| Explicit MC-6 functions (3 queries: ANF, "150357", hexadecimal truth table) | Existence of explicit MC-6 functions; slides report 149,426 classes with ≤ 5 ANDs (unverified) | **Functions not visible** |
| Circuit-size direct sum: Paul, Uhlig, Jukna, Wegener, KRW (about 12 queries) | Paul 1976 bibliographic data and garbled abstract; Uhlig's theorem via Kretschmer and MIT notes; Cambridge chapter listing | No source states the (b-C) refutation explicitly; it is deduced (D3) |
| MC analogue of mass production (1 query) | Nothing | **No MC analogue of Uhlig's theorem found** |

## Coverage limits

- Full texts were not read. All theorem statements are abstract or snippet level.
- Paul 1976 is only partly legible.
- The ANF of the 6-variable MC-6 functions was not obtained.
- Russian-language MC literature (Selezneva and others) was only lightly covered.
- 2026 preprints (Morse; arXiv 2611.15992) are unrefereed.
