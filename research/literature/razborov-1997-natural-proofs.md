# Razborov, Rudich (1997): Natural Proofs

| Field | Value |
|---|---|
| Title | Natural Proofs |
| Authors | Alexander A. Razborov, Steven Rudich |
| Year | 1997 (journal); conference version 1994 |
| Venue | Journal of Computer and System Sciences 55(1):24–35, 1997. Conference version: 26th ACM STOC (Montréal), 1994, pp. 204–213 |
| DOI | 10.1006/jcss.1997.1494 |
| Award | 2007 Gödel Prize |
| Group | Barrier (natural proofs) |

## Definitions

**Setup.**
- F_n is the set of all Boolean functions f: {0,1}^n → {0,1}. Each f is identified with its truth table, of length N = 2^n.
- A combinatorial property is a sequence C = {C_n} with C_n ⊆ F_n.
- Γ and Λ are complexity classes; typically Γ ∈ {P, P/poly} and Λ = P/poly.

**The three conditions.**
- **Constructivity (Γ-constructive).** Given the truth table of f_n (input length N = 2^n), membership "f_n ∈ C_n" is decidable in Γ. For Γ = P this means time poly(N) = 2^{O(n)}.
- **Largeness.** |C_n| ≥ 2^{−O(n)} · |F_n| for all sufficiently large n. In other words, at least a 1/N^{O(1)} fraction of all functions have the property.
- **Usefulness against Λ.** Every sequence (f_n) with f_n ∈ C_n lies outside Λ. For Λ = P/poly, RR's version (recalled; a secondary source notes RR use "almost every n") reads: for every constant k and all sufficiently large n, every f_n ∈ C_n has circuit size > n^k.

**Natural property and natural proof.**
- C is **Γ-natural** if it contains a subproperty C* ⊆ C that is both Γ-constructive and large.
- A lower-bound proof is **Γ-natural against Λ** if it defines, explicitly or implicitly, a Γ-natural property useful against Λ.

## Relevant theorem

**Main theorem (shape recalled from memory; corroborated by secondary sources).** If there exists a P/poly-natural property useful against P/poly, then there is no strong pseudorandom generator computable in P/poly. Here "strong" means hardness at least 2^{k^ε} for some ε > 0 on seed length k. Equivalently, via GGM-style constructions, no pseudorandom function family secure against circuits of size 2^{n^ε}.

**Proof idea (recalled).**
1. From a 2^{k^ε}-hard PRG, build a pseudorandom function family {f_s} with polynomial-size circuits. Choose the seed length k = n^{O(1)} so that 2^{O(n)} ≪ 2^{k^ε}.
2. The constructive, large subproperty C* accepts a ≥ 2^{−O(n)} fraction of truly random functions.
3. C* rejects every f_s, because C* ⊆ C is useful against P/poly and each f_s has small circuits.
4. Testing C* therefore distinguishes f_s from a random function in time 2^{O(n)} with non-negligible advantage, contradicting the PRG's hardness.

**Parameterized form (from a later paper, as summarized by WebSearch).** A 2^{k^ε}-hard PRG in SIZE(k^c) implies there is no P/poly-natural property of density > 2^{−n^d} useful against SIZE(n^e), for suitable e depending on c, d and ε.

## What it rules out or limits

Assume the standard cryptographic hypothesis that 2^{n^ε}-hard PRGs / PRFs exist; for example, it follows from sufficiently strong hardness assumptions on factoring or discrete log. Under that hypothesis, **no proof of NP ⊄ P/poly can have the following form:**
1. Exhibit a property Φ of truth tables.
2. Φ holds for at least a 2^{−O(n)} fraction of all functions (largeness).
3. Φ, or a large subproperty, can be checked in time poly(2^n) (constructivity).
4. Φ(f) implies f needs superpolynomial circuits (usefulness).

Typical casualties: efficiently computable "complexity measures" of truth tables, such as rank-type measures, random-restriction shrinkage measures, Fourier/spectral concentration measures, or approximation degree, if they are large for random functions and imply hardness. RR observe that known lower bounds for restricted classes are natural or can be naturalized; secondary sources report this for the AC0 parity bound and Razborov–Smolensky AC0[p].

## Why it matters for NP-FRONTIER

- A P ≠ NP attempt via circuit lower bounds must break at least one of constructivity or largeness, and must say which one and why.
- Otherwise the attempt also implies that strong PRGs do not exist. That is a separate cryptographic breakthrough, and it should be treated as evidence the argument is wrong.
- For P = NP hunters: P = NP itself implies no PRGs secure against polynomial-time adversaries. That is consistent, but does not help.

## Limitations

- The barrier is **conditional** on strong PRGs or PRFs. It is unconditional only for self-defeating cases. For example (recalled), a natural proof that discrete log needs 2^{n^ε}-size circuits would yield PRGs and thus refute itself.
- It applies only to lower bounds against classes rich enough to compute PRFs:
  - P/poly.
  - Also TC0, under a factoring assumption via Naor–Reingold PRFs (secondary: Williams's 2018 lecture notes, surfaced by WebSearch).
  - It does **not** block lower bounds for AC0, AC0[p] or monotone circuits.
- It concerns **non-uniform** lower bounds. A proof of P ≠ NP need not prove NP ⊄ P/poly; uniform arguments are not directly covered, though they face relativization and algebrization instead.
- The barrier is sensitive to the largeness parameter. "Almost-natural" useful properties with slightly weakened largeness provably exist (arXiv 0805.1385, "Almost-natural proofs", 2008; author not confirmed in my searches, recalled as Timothy Y. Chow).
- Converse direction:
  - Williams, "Natural Proofs Versus Derandomization" (SIAM J. Comput. 45(2):497–529, 2016; STOC 2013; arXiv 1212.1891). For "typical" classes C ∈ {AC0, ACC0, TC0, NC1, NC, P/poly}, NEXP ⊄ C iff there is a **constructive** (polynomial-time) property useful against C. **Largeness is not required.** For NEXP-type lower bounds, largeness is the ingredient the barrier exploits.
  - Natural proofs against a class C yield learning algorithms for C (ECCC TR16-008, as summarized by WebSearch; recalled as Carmosino–Impagliazzo–Kabanets–Kolokolova 2016, unverified).

## Check to apply to a hypothesis

1. Does the argument assign to each Boolean function a property or measure Φ such that Φ(f) ⇒ f ∉ SIZE(n^k)?
2. Is Φ (or a subproperty) decidable from the truth table in 2^{O(n)} time, or even in quasi-polynomial time in N?
3. Is Φ satisfied by a ≥ 2^{−O(n)} fraction of random functions?

If 1–3 all hold and the target class is P/poly (or TC0), reject: the argument contradicts standard cryptography. Otherwise, record which condition fails and verify that failure carefully.

## Retrieval

- Journal (JCSS 55(1), 1997, pp. 24–35), DOI 10.1006/jcss.1997.1494, STOC 1994 pp. 204–213 and the 2007 Gödel Prize: confirmed by WebSearch (result summary citing Wikipedia, the SIGACT 2007 Gödel Prize page and the bibtex.github.io STOC-1994 entry).
- Three-condition definitions (constructivity: decidable in 2^{O(n)} from the truth table; largeness: ≥ 2^{−O(n)} fraction; usefulness), the "natural = contains a large constructive subproperty" convention, and the conditional shape of the theorem ("no natural proofs unless 2^{n^ε}-hard PRGs do not exist"): confirmed only from secondary sources via WebSearch summaries (UT Austin scribe notes, Wikipedia, Williams's 2018 lecture notes, Princeton COS598B notes, Regan–Sivakumar–Cai). Not checked against the paper.
- Exact theorem numbering and quantifiers: not checked. The proof idea, the self-defeating discrete-log remark and the list of naturalizable proofs: recalled from memory.
- Williams 2016 bibliographic data and the "NEXP ⊄ C iff constructive useful property" equivalence: confirmed via WebSearch (SIAM special-section page and arXiv 1212.1891 summaries).
