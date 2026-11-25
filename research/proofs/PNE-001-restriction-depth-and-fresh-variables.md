# Restriction depth, multiplicative complexity, and fresh variables

Hypotheses: PNE-001 (fresh-variable lemma), OTH-001 (restriction barrier). Cycle 001, 2026-11-25.
Status of this document: complete proofs written by the chief researcher; independent audit pending (see `audits/`).
Lean status: not formalized (see "Formalization" at the end).

## 1. Definitions

- $\mathbb{F}_2=\{0,1\}$. A Boolean function on $n$ variables is $f:\mathbb{F}_2^n\to\mathbb{F}_2$. It is **affine** if $f(x)=c+\langle v,x\rangle$; constants are affine.
- For an affine subspace $V\subseteq\mathbb{F}_2^n$ of dimension $d$, $f|_V$ denotes $f\circ\varphi$ for an affine bijection $\varphi:\mathbb{F}_2^d\to V$. Different choices of $\varphi$ give affinely equivalent functions; every quantity below is invariant under affine equivalence, so the choice never matters.
- For $v\neq 0$ and $c\in\mathbb{F}_2$: $H(v,c)=\{x:\langle v,x\rangle=c\}$.
- **XOR-AND circuit** with $m$ AND gates: wires $w_0=1$, the inputs $x_1,\dots,x_n$, and gates $z_j=A_j\cdot B_j$ ($j=1..m$), where $A_j,B_j$ are XORs of subsets of $\{w_0,x_1,\dots,x_n,z_1,\dots,z_{j-1}\}$; the output is an XOR of a subset of all wires. **MC(f)** is the least $m$ for which such a circuit computes $f$.
- **Restriction depth** $D(f)$: $D(f)=0$ if $f$ is affine; otherwise
  $$D(f)=1+\min_{v\neq 0}\ \max_{c\in\mathbb{F}_2} D\big(f|_{H(v,c)}\big).$$
  Equivalently, $D(f)$ is the least depth of a parity decision tree (queries $\langle v,x\rangle$) whose leaves are affine functions on the leaf's subspace. Hence $D_\oplus(f)-1\le D(f)\le D_\oplus(f)$, where $D_\oplus$ is ordinary parity decision tree depth.
- A measure $\mu\ge 0$ on Boolean functions is **restriction-robust** if it is invariant under affine equivalence, $\mu(\text{affine})=0$, and
  (P1) for every $f$ on $n\ge1$ variables and every $v\ne0$ there is $c$ with $\mu(f|_{H(v,c)})\ge\mu(f)-1$.

Basic facts (standard; proofs are one line each):
(F1) MC and D are invariant under affine equivalence and under $f\mapsto f+\lambda$ for affine $\lambda$ (XOR is free; restrictions of affine functions are affine).
(F2) Substituting an affine parametrization $x=\varphi(u)$ of an affine subspace $V$ into a circuit for $f$ gives a circuit with the same AND gates for $f|_V$: every input form, affine in $(x,z)$, becomes affine in $(u,z)$.
(F3) Adding a dummy variable changes neither MC nor D (a circuit or tree for $f$ ignores the new variable; conversely restrict the new variable to 0).

## 2. Lemma 1 ($D\le \mathrm{MC}$)

**Lemma 1.** For every $f$, $D(f)\le \mathrm{MC}(f)$.

*Proof.* Induction on $m=\mathrm{MC}(f)$. If $m=0$, $f$ is affine and $D(f)=0$. Let $m\ge1$ and fix a circuit with $m$ AND gates. The first gate is $z_1=A_1B_1$ with $A_1,B_1$ affine in $x$. If $A_1$ were constant, $z_1\in\{0,B_1\}$ would be affine; substituting it into later forms gives a circuit with $m-1$ gates, contradicting minimality. So $A_1=\langle v,x\rangle+e$ with $v\ne0$. For each $c$, on $H(v,c)$ the form $A_1$ equals the constant $c+e$, so by (F2) the restricted circuit computes $f|_{H(v,c)}$ and its first gate is affine; removing it leaves $m-1$ AND gates. Thus $\mathrm{MC}(f|_{H(v,c)})\le m-1$ for both $c$, and by induction $D(f|_{H(v,c)})\le m-1$. By the definition of $D$ (a minimum over $v$), $D(f)\le 1+\max_c D(f|_{H(v,c)})\le m$. $\square$

## 3. Lemma 2 (restriction-robust measures are capped by D, and D by n−1)

**Lemma 2.** (a) $D$ is restriction-robust. (b) Every restriction-robust $\mu$ satisfies $\mu\le D$. (c) $D(f)\le\max(n-1,0)$ for $f$ on $n$ variables. Consequently, a lower bound $\mathrm{MC}(f)\ge\mu(f)$ obtained from any restriction-robust $\mu$ never exceeds $n-1$.

*Proof.* (a) Invariance: an affine bijection maps hyperplanes to hyperplanes and affine functions to affine functions; induct on $n$. (P1): if $f$ is affine, $D(f)-1<0$. Otherwise for every $v$, $D(f)\le1+\max_cD(f|_{H(v,c)})$ by definition.
(b) Induction on $n$. If $f$ is affine (in particular if $n=0$), $\mu(f)=0=D(f)$. Otherwise let $v^*$ attain the minimum in $D(f)$. By (P1) pick $c$ with $\mu(f|_{H(v^*,c)})\ge\mu(f)-1$. Then $\mu(f)\le1+\mu(f|_{H(v^*,c)})\le1+D(f|_{H(v^*,c)})\le D(f)$, using the induction hypothesis on $n-1$ variables.
(c) For $n\le1$ every function is affine. For $n\ge2$ and non-affine $f$, query $v=e_1$: $D(f)\le1+\max_cD(f|_{H(e_1,c)})\le1+(n-2)$ by induction. $\square$

**Lemma 3 (degree is restriction-robust).** For $f$ on $n\ge1$ variables and $v\ne0$, some $c$ has $\deg(f|_{H(v,c)})\ge\deg f-1$. Hence $\mu_{\deg}(f)=\max(\deg f-1,0)$ is restriction-robust, and Lemmas 1–2 give the classical bound $\mathrm{MC}(f)\ge D(f)\ge\deg f-1$.

*Proof.* Degree is invariant under affine bijections, so choose coordinates with $\langle v,x\rangle=x_1$. Write $f=x_1g+h$ with $g,h$ independent of $x_1$ (unique ANF split). Then $f|_{x_1=0}=h$, $f|_{x_1=1}=g+h$, and $\deg f=\max(1+\deg g,\deg h)$ (monomials containing $x_1$ cannot cancel monomials without it). If $\deg h\ge\deg f-1$ take $c=0$. Otherwise $\deg h\le \deg f-2$, so $\deg f=1+\deg g$ and $\deg(g+h)=\deg g=\deg f-1$ because no top-degree monomial of $g$ appears in $h$; take $c=1$. $\square$

## 4. Theorem 4 (fresh variable for restriction depth)

**Theorem 4.** Let $g$ be a non-constant function on $n$ variables and $F(x,y)=y\cdot g(x)$ on $n+1$ variables. Then $D(F)=D(g)+1$.

*Proof.* $F$ is not affine: $g$ has an ANF monomial of degree $\ge1$, so $F$ has one of degree $\ge2$.

*Upper bound.* Query $y$: $F|_{y=0}=0$ is affine and $F|_{y=1}=g$, so $D(F)\le1+D(g)$.

*Lower bound*, by induction on $n$. Since $F$ is not affine, $D(F)=1+\min_{w}\max_c D(F|_{H(w,c)})$ over $w\ne0$ in $\mathbb{F}_2^{n+1}$. Write $w=(v,s)$ with $v\in\mathbb{F}_2^n$, $s\in\mathbb{F}_2$ the coefficient of $y$. It suffices to show $\max_c D(F|_{H(w,c)})\ge D(g)$ for every $w$. If $D(g)=0$ this is trivial, so assume $D(g)\ge1$ ($g$ not affine).

We use one fact twice. (★) For any $v\neq 0$: $\max_c D(g|_{H(v,c)})\ge D(g)-1$ (definition of $D$), and not both $g|_{H(v,0)}$, $g|_{H(v,1)}$ are constant (otherwise $g=c_0+(c_0+c_1)\langle v,x\rangle$ would be affine).

*Case A: $s=0$, so $v\ne0$.* $H(w,c)=H(v,c)\times\mathbb{F}_2$, and in coordinates $(u,y)$ the restriction is $y\cdot g|_{H(v,c)}(u)$, with $y$ still fresh. If $D(g)\ge2$, choose $c$ with $D(g|_{H(v,c)})\ge D(g)-1\ge1$ by (★); then $g|_{H(v,c)}$ is non-constant and the induction hypothesis (on $n-1$ variables) gives $D(y\cdot g|_{H(v,c)})\ge D(g|_{H(v,c)})+1\ge D(g)$. If $D(g)=1$, choose $c$ with $g|_{H(v,c)}$ non-constant by (★); then $y\cdot g|_{H(v,c)}$ is not affine, so its $D$ is $\ge1=D(g)$.

*Case B: $s=1$, $v=0$, so $w=e_y$.* $F|_{y=1}=g$, so the maximum is $\ge D(g)$.

*Case C: $s=1$, $v\ne0$.* $H(w,c)=\{(x,y):y=\langle v,x\rangle+c\}$, parametrized by $x$; the restriction is $G_c(x)=\ell_c(x)\,g(x)$ with $\ell_c=\langle v,x\rangle+c$. Choose an affine bijection $T$ of $\mathbb{F}_2^n$ with $\ell_c(T(u_1,u'))=u_1$. Pointwise, $u_1\,g(T(u_1,u'))=u_1\,g(T(1,u'))$ (both sides vanish when $u_1=0$). Since $u'\mapsto T(1,u')$ is an affine bijection onto $\{\ell_c=1\}=H(v,1+c)$, we get $G_c\sim u_1\cdot R_c(u')$ with $R_c=g|_{H(v,1+c)}$, a fresh-variable product on $n-1$ inner variables. As $c$ ranges over $\mathbb{F}_2$ so does $1+c$; the argument of Case A (with $u_1$ in place of $y$, using (★) and the induction hypothesis) gives $\max_c D(G_c)\ge D(g)$.

Base: for $n=1$ every non-constant $g$ is affine, so $D(g)=0$ and the claim $D(F)\ge1$ holds because $F$ is not affine. The induction hypothesis is only invoked when $D(g)\ge2$, which forces $n\ge3$. $\square$

## 5. Corollaries

**Corollary 5.** For non-constant $g$ and fresh variables $y_1,\dots,y_t$: $\mathrm{MC}(g\,y_1\cdots y_t)\ge D(g)+t$. If $\mathrm{MC}(g)=D(g)$, then $\mathrm{MC}(g\,y_1\cdots y_t)=\mathrm{MC}(g)+t$; in particular $\mathrm{MC}(y\,g)=\mathrm{MC}(g)+1$.
*Proof.* Apply Theorem 4 $t$ times ($g\,y_1\cdots y_{i}$ stays non-constant) and Lemma 1. The upper bound $\mathrm{MC}(g)+t$ multiplies the output by each $y_i$ with one AND gate. $\square$

**Corollary 6 (computer-assisted).** For every non-constant $g$ on at most 4 variables, $\mathrm{MC}(y\,g)=\mathrm{MC}(g)+1$.
*Proof.* EXP-001 computed MC exactly for all $2^{16}$ functions on 4 variables by breadth-first search over circuit spans (no SAT solver). EXP-002 computed $D$ for the same functions. They agree on all 65,536 functions. Functions on fewer variables are covered by (F3). Apply Corollary 5. $\square$
Data: (MC, D) counts are (0,0): 32, (1,1): 1120, (2,2): 31616, (3,3): 32768; MC = 3 exactly for the 32,768 functions of degree 4.

**Corollary 7 (where the question is open).** $\mathrm{MC}(y\,g)=\mathrm{MC}(g)+1$ can fail only if $\mathrm{MC}(g)>D(g)$. By Lemma 2(c) this includes every $g$ on $n$ variables with $\mathrm{MC}(g)\ge n$, for example the 6-variable functions with MC 6 reported by Çalık–Sönmez Turan–Peralta (bibliographic data retrieved via WebSearch; the functions themselves were not seen). For such a base function, product constructions $g\,y_1\cdots y_t$ are certified by Corollary 5 only to have $\mathrm{MC}\ge D(g)+t\le N-1$, where $N=6+t$ is the number of variables.

## 6. Theorem 8 (barrier for one-restriction-per-gate arguments)

**Theorem 8.** Let $\mu$ be restriction-robust. Then $\mu(f)\le D(f)\le n-1$ for every $f$ on $n\ge1$ variables. Hence no lower bound of the form "$\mathrm{MC}(f)\ge\mu(f)$ by induction on gates, killing one AND gate per hyperplane restriction" can certify $\mathrm{MC}(f)\ge n$, for any $f$, explicit or not. (Lemma 2.)

Interpretation. The classical degree bound is of this form (Lemma 3). To prove $\mathrm{MC}(f)\ge n$ for an explicit $f$, an argument must use a different principle, for example: (i) a restriction that provably kills at least two AND gates in every optimal circuit, which needs a structural statement about optimal circuits; (ii) counting or pigeonhole arguments over circuit structures (the literature reports such an argument for the maximum MC over 7-variable functions; not read in full); (iii) exhaustive computation for a fixed base function combined with a composition theorem that is not restriction-based.

## 7. What is not proved here

- The fresh-variable lemma for $g$ with $\mathrm{MC}(g)>D(g)$ (open; PNE-001).
- The AND-direct-sum $\mathrm{MC}(g(x)h(y))=\mathrm{MC}(g)+\mathrm{MC}(h)+1$ (PNE-002). It would imply explicit functions with $\mathrm{MC}\ge cn$, hence circuit size $\ge cn$ over the full binary basis, for every constant $c$ (take a brute-force-hardest function on a constant number of variables and AND together $n/k$ copies). The best refereed explicit bound for circuit size is about $3.1n$, so this statement is at least as hard as a major open problem.
- The multiplexer lemma MC((1+s)P + sQ) = MC(P) + MC(Q) + 1, for P, Q on disjoint variables and a fresh selector s, would imply PNE-001 (take P = 0). It would also imply explicit MC ≥ cn for every c, via a decision list over brute-force-hard constant-size blocks, so in general it is as strong as PNE-002. The first function with MC > D on 5 variables (g* in EXP-002) is a multiplexer, so this is where restriction depth and MC separate.
- Novelty: **Lemma 1 is essentially known.** Chistopolskaya–Podolskii (arXiv 1810.08668 / ECCC TR18-174) prove $D_\oplus(f)\le c_\wedge(f)+1$ by the same induction on AND gates (per search-result summaries; full text not read). Lemma 1 is marginally stronger, since $D\ge D_\oplus-1$, but uses the same argument. Lemma 3 is folklore. Theorem 4 (fresh variable for restriction depth) and Theorem 8 (the cap) were not found in the literature checked (`research/literature/index-multiplicative-complexity.md`). Treat their novelty as unconfirmed.
- Scope of the explicit-bound application: the open problem stated by Chistopolskaya–Podolskii is an explicit $f$ with $c_\wedge(f)>n$ (strict). A 6-variable seed with MC 6, together with PNE-001, would give MC $=n$ exactly: above the known explicit $n-1$, but not $>n$. A strict bound would need a certified seed with $\mathrm{MC}(g)\ge k+1$ on $k$ variables; such seeds exist non-constructively for $k\ge 8$ by counting, but none is certified.

## 8. Formalization

Not formalized in Lean. Formalizing Theorem 4 needs affine subspaces, restrictions and coordinate changes over $\mathbb{F}_2$; the project currently uses core Lean without Mathlib (Mathlib's build cache host is blocked here). What is formalized in this cycle is listed in `research/proofs/lean/README.md`.
