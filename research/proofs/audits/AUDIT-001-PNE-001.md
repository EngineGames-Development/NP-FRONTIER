# AUDIT-001: PNE-001, restriction depth, multiplicative complexity and fresh variables

- Auditor: Agent F (adversarial reviewer). Fresh context, independent of the author. Date: 2026-11-25.
- Audited file: `research/proofs/PNE-001-restriction-depth-and-fresh-variables.md`.
- Edits during the audit: the file was edited twice (106 → 136 → 180 lines). Final version sha256 `a961a8dac371abca535ebb354a1428dd45f98bdf0b6b39328497aafa20753577`.
  - The requested claims (Definitions, Lemmas 1–3, Theorem 4, Corollaries 5–7, Lemma 9, Proposition 10, Theorem 8, §7 remarks) are textually unchanged across the three versions, with two exceptions: the DRAT bullet of Proposition 10 changed from "submitted" to "verified", and a CCC 2025 reference was added to the §7 novelty bullet.
  - Lemmas 11–15 and Theorems 16–17 were added during the audit and are outside the requested scope. §5 reports a bounded check of them, not a full audit.
- Read:
  - the document;
  - `EXP-001-mc-exact/mc.py` and `bfs4.py`;
  - `EXP-002-restriction-depth/dpdt.py`, `verify_s2_5.py`, `pair_test.py`, `first_gate_extension.py`, `first_gate_general.py`;
  - the logs of these scripts;
  - the data files `mc4.json`, `D4.json` and `yg_star_k3.cnf`, used only for comparison.
- Not read: no other research notes. The scratch directory already held files I did not create (`indep/`, `rerun/`, `repo_*.json`); I did not read or use them.

## 1. Verdicts

| Claim | Verdict | Note |
|---|---|---|
| Lemma 1 (D ≤ MC) | SURVIVES | Not new. Equivalent, not "marginally stronger", to Chistopolskaya–Podolskii's $D_\oplus\le c_\wedge+1$ (I-1). |
| Lemma 2 (a), (b), (c) | SURVIVES | (c) is $D_\oplus\le n$ in disguise (I-1). |
| Lemma 3 | SURVIVES | Folklore; equivalent to the classical $D_\oplus\ge\deg_2$. |
| Theorem 4 ($D(yg)=D(g)+1$) | SURVIVES | Every step checked (V-1); exhaustive at n=4, sampled at n=5 (V-4). Equivalent to $D_\oplus(y\wedge g)=D_\oplus(g)+1$; novelty unconfirmed (I-1). |
| Corollary 5 | SURVIVES | |
| Corollary 6 and its computational basis | SURVIVES | MC and D tables recomputed independently; identical per function (V-2, V-3). |
| Corollary 7 | BROKEN as literally stated (degenerate case only, Low) | False for constant $g$; the non-constant case follows from Corollary 5 (I-3). |
| Theorem 8, formal statement | SURVIVES | Correct but trivial. |
| Theorem 8, "Hence …" and the "barrier" framing | GAP / OVERCLAIMED | Does not follow from the theorem for the class of arguments it names. Witness: a Lemma 9-type measure beats D (I-2). |
| Lemma 9 | SURVIVES | |
| Proposition 10 | SURVIVES | All numerical claims recomputed with independent code, including a full exhaustive search that does not use Lemma 9 (V-6). Both proofs check out. |
| §7 novelty remarks | Partly incorrect | I-1, I-2. |
| §7 multiplexer identity (stated as open) | False as written in the degenerate case | I-4. |

No Critical or High severity issue was found in the requested claims.

## 2. Issues

### I-1. Medium (novelty, framing). Location: §1, "Hence $D_\oplus(f)-1\le D(f)\le D_\oplus(f)$"; §7, novelty bullet.

Restriction depth is exactly $D_\oplus-1$: $D(f)=D_\oplus(f)-1$ for every non-constant $f$, and $D=D_\oplus=0$ on constants.

Proof. $D_\oplus\le D+1$ is in the document. Conversely, take a constant-leaf parity decision tree for $f$ of depth $d=D_\oplus(f)\ge1$. Every internal node at depth $d-1$ has two leaf children. On that node's subspace, $f=c_0+(c_0+c_1)\ell$, which is affine. Replacing these nodes by affine leaves gives an affine-leaf tree of depth $d-1$.

Computational confirmation (coordinate-free code computing both measures): all non-constant 4-variable functions, and 28 sampled 5-variable functions.

Consequences:
- (a) The remark "Lemma 1 is marginally stronger, since $D\ge D_\oplus-1$" is false. Lemma 1 and the Chistopolskaya–Podolskii inequality are the same statement.
- (b) Theorem 4 is the deterministic parity-decision-tree identity $D_\oplus(y\cdot g)=D_\oplus(g)+1$ for non-constant $g$. Its novelty has to be judged against the PDT literature under that formulation. I found no source stating it, but only ran short searches. The newly cited CCC 2025 paper (arXiv 2412.06552) is, by its abstract summary, about direct sums for randomised PDTs, so it is inconclusive here.
- (c) The cap $D\le n-1$ in Lemma 2(c) and Theorem 8 is just $D_\oplus\le n$.
- (d) "Restriction depth" is not a new complexity measure. Presenting it as one hides (a)–(c).

### I-2. Medium (overclaim). Location: §6, Theorem 8's "Hence …" sentence; the section title "barrier"; OTH-001.

The formal theorem ("restriction-robust $\mu\le D\le n-1$") is correct. It is a two-line induction plus $D_\oplus\le n$. The "Hence" sentence applies it to every lower bound "by induction on gates, killing one AND gate per hyperplane restriction". The theorem does not cover that class.

Witness. Define the pair measure $\mu'(f)=0$ for affine $f$, and otherwise
$\mu'(f)=1+\min_{v\ne w}\max_{u\in\{v,w\},\,c}\mu'(f|_{H(u,c)})$.
- By Lemma 9 and induction on MC, $\mathrm{MC}\ge\mu'$. Each step kills exactly one AND gate with one hyperplane restriction.
- On 4 variables, $D\le\mu'\le\mathrm{MC}=D$, so $\mu'=D$ there.
- For $g^*$ (`0xfff3d212`), the only direction whose two halves have $D\le1$ is $x_2$. All 30 other directions have $D=2$ on both halves (computed). Hence $\mu'(g^*)=3>D(g^*)=2$.
- $\mu'$ violates (P1) at $(g^*,x_2)$.

So "$\mu\le D$" is not a barrier for the class the sentence names. The document's own Lemma 12 and Corollary 13 are arguments of exactly this kind, and they beat $D$.

What does hold for that class is only a dimension count: each step removes one variable and adds one to the bound, and every function on at most one variable is affine. That gives $\le n-1$. It is folklore and is not a consequence of Theorem 8. Prior work on limits of gate elimination is relevant and should be cited: Golovnev, Hirsch, Knop, Kulikov, "On the limits of gate elimination", MFCS 2016 / JCSS 96 (2018), ECCC TR16-119. Retrieved via WebSearch: title, venue and abstract summary only.

### I-3. Low. Location: Corollary 7, first sentence.

"$\mathrm{MC}(yg)=\mathrm{MC}(g)+1$ can fail only if $\mathrm{MC}(g)>D(g)$" is false for constant $g$.
- Witness $g=0$: $\mathrm{MC}(0)=D(0)=0$, but $\mathrm{MC}(y\cdot0)=0\ne1$.
- Witness $g=1$: $\mathrm{MC}(y)=0$.

The non-constant hypothesis is carried by Corollary 5 but missing here.

### I-4. Low. Location: §7, multiplexer lemma $\mathrm{MC}((1+s)P+sQ)=\mathrm{MC}(P)+\mathrm{MC}(Q)+1$.

False when $P$ and $Q$ are both constant. Witness: $P=Q=0$ gives $0\ne1$. The implication "take $P=0$" fails in the same way for constant $Q$.

Exhaustive test on 5 variables, selector $x_5$, 1,280 pairs: $P$ on $\{x_1,x_2\}$ with $Q$ on $\{x_3,x_4\}$, and $P$ on $\{x_1,x_2,x_3\}$ with $Q$ on $\{x_4\}$. The only violations are the 8 pairs where both are constant. The non-degenerate cases agree with the identity at this size.

### I-5. Low (presentation). Location: Proposition 10, fourth bullet.

The "4 choices of $(e,e')$" are not four cases. For all four, $(x_2+e)(x_2+y+e')\equiv x_2y$ modulo affine functions. So $W_1=\mathrm{span}\{1,x,y,x_2y\}$ is the same space every time, and the four "exhaustive searches" are one search repeated; the log shows identical counts of 2,345. This is not an error, but the text presents one check as four.

### I-6. Low (self-containedness). Location: Proposition 10, bullets 1–2.

The ANF of $g^*$ and its 3-AND circuit are only referenced, not given. I found and certified them independently:
- ANF: $g^*=x_1+x_1x_2+x_3+x_2x_3+x_2x_3x_4+x_5+x_1x_5+x_2x_5+x_1x_2x_5+x_3x_5+x_2x_4x_5$.
- Circuit: $z_1=(x_1+x_3)x_5$, $z_2=(x_3+x_4)(x_3+x_5)$, $z_3=x_2(x_1+x_5+z_1+z_2)$, output $g^*=x_1+x_3+x_5+z_1+z_3$.
- Halves: $g^*|_{x_2=0}=x_1+x_3+x_5+x_1x_5+x_3x_5$ and $g^*|_{x_2=1}=x_3x_4+x_3x_5+x_4x_5$. Both are rank-2 quadratics, which matches the structure remark.
- These halves share $x_3$ and $x_5$. They are on disjoint variables only after an affine change of the four non-selector variables.

### I-7. Low (rigor). Location: §1 definition of $D$, and (F3).

- (i) $D$ is defined through arbitrary parametrizations before its affine invariance is proved (Lemma 2(a)), so the order of presentation is circular. It is repairable by canonical parametrizations or by the coordinate-free PDT characterization. In practice it is harmless:
  - my coordinate-free implementation agrees with parametrized ones on all 65,536 4-variable functions and on 81 sampled 5-variable functions;
  - 20,000 random affine-invariance tests at $n=5$ and 300 at $n=6$ found no mismatch.
- (ii) For $D$, (F3)'s "conversely restrict the new variable to 0" needs monotonicity of $D$ under restriction, which is not stated. It is true: restrict the tree.

### I-8. Info. Location: Proposition 10, DRAT bullet.

The CNF that drat-trim checked (`yg_star_k3.cnf`: 2,794 variables, 10,201 clauses) has a clause multiset identical to `mc.encode(y·g*, 6, 3)`, regenerated from a copy of `mc.py`.

I reviewed that encoding. Its non-degeneracy clauses (each gate input contains a non-constant wire, and the two input masks differ) are satisfied by every optimal circuit. So UNSAT does imply $\mathrm{MC}\ge4$.

I did not re-run drat-trim. The log reports `s VERIFIED`.

### I-9. Info (outside the requested scope). Location: Lemma 14(b).

$\Lambda=\lambda_{00}+\dots$ has a stray term: with $h=g_{00}$, $\lambda_{00}=0$.

## 3. What I verified independently, and how

All audit code was written from scratch in `/tmp/claude-0/-home-user-NP-FRONTIER/196c3dd4-a9e1-53fa-ac27-a84315fa91b8/scratchpad/review/`. That directory is ephemeral; the methods are described here so the checks can be reproduced. No repository code was used as evidence. Repository code was run only to regenerate the CNF (I-8) and to re-run the author's scripts on copies (V-10).

**V-1. Proofs read line by line.**
- Lemma 1; Lemma 2 (a)–(c); Lemma 3.
- Theorem 4: Cases A, B and C, and the base case. In Case C I checked that $G_c\circ T=u_1\,g(T(1,u'))$ and that $u'\mapsto T(1,u')$ is a bijection onto $H(v,1+c)$.
- Corollary 5; Lemma 9.
- For the second proof of Proposition 10: Lemma 11, Lemma 12 and Corollary 13.

Apart from I-3 and I-7, I found no gap. The inductions are well founded: Lemma 1 uses strong induction on MC; Lemma 2 and Theorem 4 use induction on $n$, and Theorem 4 invokes its hypothesis only when $D(g)\ge2$. The edge cases (constants, $n\le2$, restrictions that become constant) are handled.

**V-2. MC of all 4-variable functions** (`s4.c`, C).
- Method: enumerate all first-gate classes modulo $W_0$ (35), all second-gate spaces (2,975 visits) and all third-gate cosets (839,300), and mark every function reached. Products are taken over spans of the non-constant generators. This is justified because $(A+1)B\equiv AB \bmod W$.
- Result: counts 32 / 1,120 / 31,616 / 32,768; identical per function to `mc4.json`; $\mathrm{MC}=3$ exactly when $\deg=4$.

**V-3. D of all 4-variable functions** (coordinate-free Python).
- Method: subspaces are represented as point sets, and affineness on a subspace is tested by $f(p_0)+f(p_0+u)+f(p_0+u')+f(p_0+u+u')=0$.
- Result: identical per function to `D4.json`. $\mathrm{MC}=D$ on all 65,536 functions, with the stated (MC, D) counts. Also $D=D_\oplus-1$ for all non-constant functions (I-1).

**V-4. Theorem 4 by computation** (`dtest.c`).
- $D(yg)=D(g)+1$ for all 65,534 non-constant $g$ on 4 variables.
- Also for 60,000 random draws on 5 variables (59,555 non-constant, with $D(g)\in\{2,3,4\}$). There were 0 failures.
- Spot value: $D(y\,g^*)=3$.

**V-5. Exhaustive XOR-AND circuit searcher** (`mcs.c` / `mcsb.c`, $k\le3$, $n\le6$).
- What it enumerates: every first-gate class modulo $W_0$ (651 at $n=6$) and every second-gate class modulo $W_1$.
- How it decides the third gate exactly: with $W=\mathrm{span}\{1,u_1..u_d\}$, the class of $AB$ is $\sum_{i<j}(\alpha_i\beta_j+\alpha_j\beta_i)[u_iu_j]$. For each $\alpha$ the searcher tests whether $[F]\in\mathrm{span}\{c_j(\alpha)\}$, where $c_j(\alpha)=\sum_{i\ne j}\alpha_i[u_iu_j]$.
- What it does not use: Lemma 9, admissible directions, or any symmetry.
- Validation:
  - agrees with V-2 on all 65,536 4-variable functions, for every $k\le3$;
  - agrees with an explicit-set brute force of $S_2$ on 151 5-variable functions (71 with MC 2, 3 with MC 1, 77 outside $S_2$);
  - finds each of 24 random "deep" 3-AND circuits on 6 variables (later gates forced to use earlier outputs) at level 3, and none at level ≤ 2;
  - finds $x_1x_2x_3\,y$, with a certificate;
  - rejects $x_1\cdots x_5$ (degree 5).
- Every circuit it reports is re-checked by a separate span-membership checker.

**V-6. Proposition 10.**
- $\deg g^*=3$ and $D(g^*)=2$; $x_2$ is the unique direction with both halves at $D\le1$.
- $g^*\notin S_2$: all 155 first-gate classes checked.
- A 3-AND circuit for $g^*$ was found and certified (I-6).
- $y\,g^*$: the full search over 651 first-gate classes and 1,526,595 second-level spaces finds no 3-AND circuit, so $\mathrm{MC}(y\,g^*)=4$. This takes about 90 s of CPU and does not rely on Lemma 9.
- Also reproduced, with my own restriction parametrization and $S_2$ test:
  - the admissible directions of $y\,g^*$ are exactly $\{x_2,\;x_2+y\}$;
  - there are 2,345 second-gate classes for each first gate.

**V-7. Second proof of Proposition 10, and Corollary 13.**
- Its inputs are confirmed: $\mathrm{MC}(g^*)=3$, and $g^*$ has exactly one cheap direction.
- Adversarial probe: three random 5-variable multiplexers with $\mathrm{MC}=3$, $D=2$ and exactly one cheap direction (`0x28be9cc9`, `0xed21871e`, `0x33009c9c`). A full search gives $\mathrm{MC}(yg)\ge4$ for each, so no counterexample to Corollary 13.

**V-8.** DRAT CNF identity (I-8).

**V-9.** Multiplexer test (I-4).

**V-10. Re-run of the author's scripts** on copies in scratch (repository untouched). They reproduce the logs: positive control FOUND; $g^*$ admissible directions [2, 34]; NONE.

**V-11. Literature** (WebSearch summaries only; arXiv and ECCC full texts are blocked).
- Chistopolskaya–Podolskii, arXiv 1810.08668 / ECCC TR18-174. Retrieved: title, IDs, and that they derive $\mathrm{MC}(\mathrm{MAJ}_n)\ge n-B(n)$ from $D_\oplus(\mathrm{MAJ}_n)=n-B(n)+1$. This is consistent with $c_\wedge\ge D_\oplus-1$.
- Çalık–Sönmez Turan–Peralta, "The multiplicative complexity of 6-variable Boolean functions", Cryptogr. Commun. 2019, IACR ePrint 2018/002. Retrieved: the maximum MC on 6 variables is 6, with explicit examples, which supports Corollary 7's example. The same search reported MC ≤ n−1 for n ≤ 5, consistent with Corollary 6's data.
- Golovnev–Hirsch–Knop–Kulikov (see I-2).
- Besselman–Göös–Guo–Maystre–Yuan, arXiv 2412.06552 (CCC 2025): the abstract summary concerns randomised PDT direct sums.
- No source found stating $D_\oplus(y\wedge g)=D_\oplus(g)+1$.

## 4. What I could not check

- **drat-trim**: not re-run. There is no binary here and the proof is 767 MB; only the CNF's identity was checked.
- **Cited papers**: their full texts. In particular I could not confirm:
  - that Chistopolskaya–Podolskii state the open problem as $c_\wedge(f)>n$;
  - that $n-1$ is the best known explicit MC lower bound;
  - the contents of arXiv 2412.06552.
  The "about 3.1n" circuit bound is recalled, not retrieved.
- **Novelty of Theorem 4** in its PDT form: only short searches were run.
- **Theorem 4 beyond $n=4$**: only sampled at $n=5$, not exhaustive.
- **EXP-004 and EXP-005 claims** in the "Scope" bullets (31 of 38; 7 functions with three directions; the random search): their code was not provided.
- **Lemmas 11–15 and Theorems 16–17**: outside the requested scope; see §5.

## 5. Bounded check of Lemmas 14(b′)–15 and Theorems 16–17 (added mid-audit; not a full audit)

- **Logic, by reading.** Lemma 14(a) and (b′), Lemma 15 (the rank argument and the use of "degree ≤ 3 on 4 variables ⇒ MC ≤ 2") and Theorem 16: no error found. One sentence in Theorem 16's proof, "Terms $a_1x_1$ and $a_2x_2$ are absorbed …", refers to terms that cannot occur, since $g_{00}$ depends only on $x'$. It is harmless.
- **Finite family, recomputed independently.**
  - The family has 65,536 distinct members $G'$.
  - Orbits: I used my own generators of AGL(2) on $(x_1,x_2)$, AGL(3) on $u$, and complementation. Each generator preserves the family (checked on 300 random members) and preserves both $\mathrm{MC}(G')$ and $\mathrm{MC}(yG')$. They give 33 orbits.
  - No orbit mixes members inside and outside $S_2$.
  - Exactly 2 orbits lie outside $S_2$, with 10,752 members each. They contain `0x01234567` and `0x0167abcd` respectively. The other 44,032 members are in $S_2$ by my own test.
- **Searches.** For each of the two orbits outside $S_2$, I ran the full, Lemma-9-free search on $y\cdot G'$ for the orbit minimum and two random members: `0x01234567`, `0xf5397db1`, `0x63271450` and `0x0167abcd`, `0x8cbf5162`, `0xfc658b12`. None has a 3-AND circuit.
- **Outcome.** This agrees with Theorem 17's finite step.
- **Not checked:** EXP-006's own code, its DRAT runs, and whether my generators produce exactly the author's group. Orbit invariance only requires that each generator preserves MC, which holds.

## 6. Summary

The core mathematics survives: Lemmas 1–3, Theorem 4, Corollaries 5–6, Lemma 9 and Proposition 10 are correct.

All computational claims behind Corollary 6 and Proposition 10 reproduce with independent code. This includes a full exhaustive search, not using Lemma 9, showing $\mathrm{MC}(y\,g^*)=4$, and an explicit certified 3-AND circuit for $g^*$.

The main problems concern novelty and framing:
- "Restriction depth" equals $D_\oplus-1$ exactly on non-constant functions. So Lemma 1 is precisely the known Chistopolskaya–Podolskii bound (not "marginally stronger"), Theorem 4 is a plain parity-decision-tree identity of unconfirmed novelty, and the cap in Lemma 2(c) is $D_\oplus\le n$.
- Theorem 8 is correct but trivial. Its "barrier" sentence does not follow for the class it names: the Lemma 9-type pair measure gives $\mu'(g^*)=3>D(g^*)=2$. Only the folklore dimension count ($\le n-1$) remains for that class.
- Corollary 7 and the §7 multiplexer identity are false as literally stated in degenerate (constant) cases.

Nothing here touches P versus NP. These are statements about multiplicative complexity on at most 6 variables and about the $n-1$ regime.
