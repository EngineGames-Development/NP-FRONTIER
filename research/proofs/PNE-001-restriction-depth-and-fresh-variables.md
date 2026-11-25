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

## 5b. Beyond restriction depth: first-gate certificates

**Lemma 9 (first-gate criterion).** Let $\mathrm{MC}(F)\ge m\ge1$, and suppose $F$ has a circuit with exactly $m$ AND gates. Then there are affine forms $a=\langle v,x\rangle+e$, $b=\langle w,x\rangle+e'$ with $v\ne w$, both nonzero, such that $a\cdot b$ is the first gate of such a circuit, and all four restrictions $F|_{a=c}$, $F|_{b=c}$ ($c\in\mathbb{F}_2$) have $\mathrm{MC}\le m-1$. Call a direction $u$ *admissible* if both $F|_{\langle u,x\rangle=0}$ and $F|_{\langle u,x\rangle=1}$ have $\mathrm{MC}\le m-1$. Then $v,w$ are distinct admissible directions.
*Proof.* The circuit is optimal since $\mathrm{MC}(F)\ge m$. Its first gate has inputs affine in $x$. If either input is constant, or if $w=v$ (then $b\in\{a,a+1\}$ and $ab\in\{a,0\}$), the gate computes an affine function and can be removed, contradicting optimality. Restricting $a$ or $b$ to a constant makes the gate affine. By (F2) this gives an $(m-1)$-gate circuit for each of the four restrictions. $\square$

**Proposition 10 (computer-assisted; first verified case of PNE-001 with MC > D).** Let $g^*$ be the 5-variable function with truth table `0xfff3d212` (ANF in `research/hypotheses/PNE-001-fresh-variable-lemma.md`). Then $D(g^*)=2$, $\mathrm{MC}(g^*)=3$ and $\mathrm{MC}(y\,g^*)=4$.
*Proof.*
- $D(g^*)=2$: computed (EXP-002). The witness is the query $x_2$, whose restrictions both have $D=1$; $D\ge2$ because $\deg g^*=3$ (Lemma 3).
- $\mathrm{MC}(g^*)\le3$: an explicit circuit, independently re-evaluated.
- $\mathrm{MC}(g^*)\ge3$: exhaustive search over all spans $W_1$ (155 classes) and all second products shows no 2-AND circuit (`verify_s2_5.py`, no SAT solver).
- $\mathrm{MC}(y g^*)\ge4$: $\deg(yg^*)=4$ gives $\mathrm{MC}\ge3$, so Lemma 9 applies with $m=3$. The exhaustive test of $\mathrm{MC}\le2$ on all 126 hyperplane restrictions gives exactly two admissible directions, $x_2$ and $x_2+y$ (`pair_test.py`). So the first gate is $(x_2+e)(x_2+y+e')$ for one of 4 choices of $(e,e')$. For each choice, an exhaustive search over all 2,345 distinct second-gate spans and all third products finds no circuit computing $y g^*$ (`first_gate_extension.py`, `first_gate_general.py`; no SAT solver). A positive control, $x_1x_2x_3\cdot y$, correctly finds an extension.
- Independently, a SAT solver (CaDiCaL 1.5.3) reports no 3-AND circuit. Its 767 MB DRAT proof was **verified by drat-trim** (`s VERIFIED`, 617 s; `run_drat_yg_star.sh`, log `drat_trim_yg_star.log`).
- The upper bound $\mathrm{MC}(y g^*)\le4$ is trivial. $\square$

So PNE-001 holds beyond the reach of Theorem 4. Structure: $g^*=(1+x_2)P+x_2Q$ with $P,Q$ rank-2 quadratics, and the admissible directions for $y g^*$ are the selector $s=x_2$ and $s+y$. In every case examined, admissible directions come in pairs $\{v,v+y\}$, which suggests a general multiplexer argument (open).

**Lemma 11 (structure of a minimal counterexample).** Let $m\ge1$. Suppose PNE-001 holds for every non-constant $h$ with $\mathrm{MC}(h)<m$, on any number of variables. Suppose $g$ is non-constant with $\mathrm{MC}(g)=m$ and $\mathrm{MC}(y\,g)=m$. Then $g$ has a direction $v\ne0$ such that each restriction $g|_{\langle v,x\rangle=c}$ is constant or has $\mathrm{MC}\le m-2$. Moreover, for $F=y\,g$ the admissible directions (Lemma 9, with $m$) come in pairs: $(v,0)$ is admissible iff $(v,1)$ is, and $(0,1)$ (the direction $y$) is never admissible.
*Proof.* Note $\mathrm{MC}(F)\ge\mathrm{MC}(g)=m$, because setting $y=1$ in a circuit for $F$ gives a circuit for $g$. So an $m$-gate circuit for $F$ is optimal, and Lemma 9 gives two distinct admissible directions $u=(v,s)$.
- If $v=0$, then $u=e_y$ and $F|_{y=1}=g$ has MC $m>m-1$; not admissible.
- If $s=0$, then $F|_{\langle v,x\rangle=c}\cong y\,g|_{\langle v,x\rangle=c}$.
- If $s=1$, then by the identity in Case C of Theorem 4, $F|_{y=\langle v,x\rangle+c}\cong t\cdot g|_{\langle v,x\rangle=1+c}$ for a fresh variable $t$.
So both $(v,0)$ and $(v,1)$ are admissible iff, for both $c$, $\mathrm{MC}(t\cdot g|_{\langle v,x\rangle=c})\le m-1$. If $g|_{\langle v,x\rangle=c}$ is non-constant, it has $\mathrm{MC}\le m-1<m$, so the hypothesis gives $\mathrm{MC}(t\cdot g|_{\langle v,x\rangle=c})=\mathrm{MC}(g|_{\langle v,x\rangle=c})+1$. Hence $\mathrm{MC}(g|_{\langle v,x\rangle=c})\le m-2$. $\square$

*Remarks.*
1. For $m\le2$ the condition forces $\mathrm{MC}(g)\le1$: if both halves are affine, $g=\tilde g_0+s(\tilde g_0+\tilde g_1)$ needs one AND gate. So it reproves PNE-001 for $\mathrm{MC}(g)\le2$. This was already implied by Theorem 4, since $\mathrm{MC}\le2$ forces $\mathrm{MC}=D$.
2. For $m=3$ the condition says $g$ is a multiplexer of two halves with MC $\le1$. That is equivalent to $D(g)\le2<\mathrm{MC}(g)$, so it adds nothing beyond Theorem 4 at this level.
3. For $m\ge4$ the condition is strictly stronger than $\mathrm{MC}(g)>D(g)$: both halves must have MC $\le m-2$, not merely $D\le m-2$. EXP-004 tests the $m=3$ multiplexers exhaustively on the 5-variable sample.

**Lemma 12 (two distinct cheap directions).** Under the hypotheses of Lemma 11, $g$ has two **distinct** directions $v_1\ne v_2$ with the property of Lemma 11: each restriction $g|_{\langle v_i,x\rangle=c}$ is constant or has $\mathrm{MC}\le m-2$.
*Proof.* Let $a\cdot b$ be the first gate of an optimal $m$-gate circuit for $F=y\,g$, with distinct admissible directions $u_1=(v_1,s_1)$ and $u_2=(v_2,s_2)$ (Lemma 9). By the proof of Lemma 11, $v_1,v_2\ne0$ and both have the property. Suppose $v_1=v_2=v$. Then $s_1\ne s_2$. Substitute $y=1$: the inputs become $\langle v,x\rangle+s_1+e$ and $\langle v,x\rangle+s_2+e'$, which have the same linear part, so their product is affine ($a$ or $0$). By (F2) the circuit restricted to $y=1$ computes $F|_{y=1}=g$ with an affine first gate, hence with $m-1$ AND gates. That contradicts $\mathrm{MC}(g)=m$. $\square$

**Corollary 13.** Let $\mathrm{MC}(g)=3$. If $g$ has at most one direction $v$ for which both restrictions $g|_{\langle v,x\rangle=c}$ have $\mathrm{MC}\le1$, then $\mathrm{MC}(y\,g)=4$.
*Proof.* PNE-001 holds for all non-constant $h$ with $\mathrm{MC}(h)\le2$: Remark 1 after Lemma 11, via Theorem 4. Apply Lemma 12 with $m=3$. $\square$

*Second proof of Proposition 10.* Using the exact MC table for 4-variable functions, $g^*$ has exactly one such direction, $x_2$ (EXP-005). Corollary 13 applies.

*Scope (EXP-005).*
- Of the 38 certified 5-variable functions with $\mathrm{MC}=3>D=2$, 31 have exactly one such direction, so PNE-001 is proved for them by Corollary 13.
- 7 have three such directions; in each case these directions together with $0$ form a 2-dimensional subspace.
- A random search finds many such functions with $\mathrm{MC}\ge3$. So "MC $=3$ ⇒ at most one cheap direction" is **false**, and Corollary 13 alone does not settle PNE-001 at level 3. Those cases are settled by the exhaustive first-gate certificates of EXP-004.

**Lemma 14 (structure of plane-type functions; for the remaining level-3 case).** (a) Every $h$ with $\mathrm{MC}(h)\le1$ is $\alpha\beta+\gamma$ with $\alpha,\beta,\gamma$ affine. If $h$ lives on coordinates $(x_2,x')$, then $h|_{x_2=0}+h|_{x_2=1}$ is affine in $x'$. (b) Suppose $x_1$, $x_2$ and $x_1+x_2$ are all cheap directions of $g$ (both halves of each split have $\mathrm{MC}\le1$). Then the four quarters $g_{ab}=g|_{x_1=a,x_2=b}$ differ pairwise by affine functions of $x'$. So $g=h(x')+\Lambda$ with $h=g_{00}$, $\mathrm{MC}(h)\le1$, and $\Lambda=\lambda_{00}+x_1\ell_1+x_2\ell_2+x_1x_2\ell_3$ for affine $\ell_i$ in $x'$.
*Proof.*
(a) A single AND gate gives $z=\alpha\beta$, and the output is affine in $(x,z)$. Write $\alpha=a_0+a_1x_2$ and $\beta=b_0+b_1x_2$ with $a_0,b_0$ affine in $x'$ and $a_1,b_1$ constants. Then $h|_{x_2=1}+h|_{x_2=0}=a_0b_1+a_1b_0+a_1b_1+(\gamma|_{x_2=1}+\gamma|_{x_2=0})$, which is affine.
(b) Apply (a) to the halves of each of the three splits. The split on $x_1$ gives $g_{00}+g_{01}$ and $g_{10}+g_{11}$ affine. The split on $x_2$ gives $g_{00}+g_{10}$ and $g_{01}+g_{11}$ affine. The split on $x_1+x_2$ gives $g_{00}+g_{11}$ and $g_{01}+g_{10}$ affine. Interpolate over $(x_1,x_2)$. $\square$
This is the starting point for a hand proof of PNE-001 at level 3 in the plane case (open; the next cycle's first target).

**Lemma 14(b′) (two cheap directions suffice).** If $x_1$ and $x_2$ are both cheap directions of $g$, the quarters already differ pairwise by affine functions: the splits on $x_1$ and $x_2$ give four of the six differences, and the other two are sums of these. So $g=g_{00}+x_1\ell_1+x_2\ell_2+x_1x_2\ell_3$ with $\ell_i$ affine in $x'$. The third direction in Lemma 14(b) is not needed.

**Lemma 15.** If $x_1,x_2$ are cheap directions of $g$ and the quarter $g_{00}$ is not affine, then $\mathrm{MC}(g)\le2$.
*Proof.* Write $g_{00}=\alpha\beta+\gamma$ (Lemma 14(a)). Since $g_{00}$ is not affine, $\alpha$ and $\beta$ have linearly independent linear parts; let $U=\mathrm{span}(\alpha_{\rm lin},\beta_{\rm lin})$.
- The quadratic part of any function of $\mathrm{MC}\le1$, i.e. of the form $ab+c$, is a single product of two linear forms, so its symplectic form has rank $\le2$.
- The half $g|_{x_1=0}=g_{00}+x_2\ell_2$ has $\mathrm{MC}\le1$, and its quadratic part is $\alpha_{\rm lin}\beta_{\rm lin}+x_2(\ell_2)_{\rm lin}$. If $(\ell_2)_{\rm lin}\notin U$, coordinates $u_1=\alpha_{\rm lin}$, $u_2=\beta_{\rm lin}$, $u_3=(\ell_2)_{\rm lin}$ turn this into $u_1u_2+x_2u_3$, of rank 4, a contradiction. So $(\ell_2)_{\rm lin}\in U$.
- In the same way, $g|_{x_2=0}=g_{00}+x_1\ell_1$ gives $(\ell_1)_{\rm lin}\in U$.
- And $g|_{x_1=1}=(g_{00}+\ell_1)+x_2(\ell_2+\ell_3)$ gives $(\ell_2+\ell_3)_{\rm lin}\in U$, hence $(\ell_3)_{\rm lin}\in U$.

Therefore $g=G(x_1,x_2,\alpha,\beta)+\gamma$, where $G$ has degree $\le3$ in the four linearly independent affine forms $x_1,x_2,\alpha,\beta$, and $\gamma$ is affine. By an affine change of coordinates and (F1), $\mathrm{MC}(g)=\mathrm{MC}(G)$. Every 4-variable function of degree $\le3$ has $\mathrm{MC}\le2$ (EXP-001, exhaustive). $\square$
Sanity check: in all 12 known MC-3 functions with several cheap directions, the quarters are affine (`EXP-005/check_lemma15.py`).

**Theorem 16 (level 3 reduces to a finite family).** Suppose some $g$ has $\mathrm{MC}(g)=3=\mathrm{MC}(y\,g)$. Then there is a function
$$G'=x_1\ell_1+x_2\ell_2+x_1x_2\ell_3+c+\lambda(u)$$
on the five variables $(x_1,x_2,u_1,u_2,u_3)$, with $\ell_1,\ell_2,\ell_3,\lambda$ affine in $u=(u_1,u_2,u_3)$ and $c\in\mathbb{F}_2$, such that $\mathrm{MC}(G')=3=\mathrm{MC}(y\,G')$. Hence **PNE-001 holds for every $g$ with $\mathrm{MC}(g)\le3$ iff $\mathrm{MC}(y\,G')=4$ for every $G'$ of this form with $\mathrm{MC}(G')=3$.** There are at most $16^3\cdot16=65{,}536$ such $G'$ before symmetry reduction.
*Proof.*
- By Lemma 12 (with PNE-001 below level 3), $g$ has two distinct cheap directions. Choose $x$-coordinates in which they are $x_1,x_2$; this keeps $y$ fresh and does not change $\mathrm{MC}(y\,g)$.
- By Lemma 15, $g_{00}$ is affine. By Lemma 14(b′), $g=g_{00}+x_1\ell_1+x_2\ell_2+x_1x_2\ell_3$.
- Choose coordinates of $x'$ so that the linear parts of $\ell_1,\ell_2,\ell_3$ lie in $\mathrm{span}(u_1,u_2,u_3)$. Write $g_{00}=c+\lambda(u)+\mu$ with $\mu$ linear in the remaining coordinates; if $\mu\ne0$, take $\mu=w_1$ as a coordinate.
- Terms $a_1x_1$ and $a_2x_2$ are absorbed into the constants of $\ell_1,\ell_2$. So $g=G'+w$ with $w\in\{0,w_1\}$, and $w_1$ appears nowhere else.
- Adding a fresh linear variable does not change MC: restrict $w_1=0$ for one direction, XOR it for the other. So $\mathrm{MC}(G')=3$.
- Restricting $w_1=0$ in a circuit for $y\,g$ gives one for $y\,G'$, so $3=\mathrm{MC}(G')\le\mathrm{MC}(y\,G')\le\mathrm{MC}(y\,g)=3$. $\square$
The finite check is the first task of cycle 002. It needs the 5-variable $S_2$ set (vectorized), first-gate certificates on 6 variables (a C implementation, or Python after symmetry reduction under $\mathrm{AGL}(3)$ on $u$ and $\mathrm{GL}(2)$ on $(x_1,x_2)$), and a check that each symmetry preserves the family and both MC values.

## 6. Theorem 8 (barrier for one-restriction-per-gate arguments)

**Theorem 8.** Let $\mu$ be restriction-robust. Then $\mu(f)\le D(f)\le n-1$ for every $f$ on $n\ge1$ variables. Hence no lower bound of the form "$\mathrm{MC}(f)\ge\mu(f)$ by induction on gates, killing one AND gate per hyperplane restriction" can certify $\mathrm{MC}(f)\ge n$, for any $f$, explicit or not. (Lemma 2.)

Interpretation. The classical degree bound is of this form (Lemma 3). To prove $\mathrm{MC}(f)\ge n$ for an explicit $f$, an argument must use a different principle, for example: (i) a restriction that provably kills at least two AND gates in every optimal circuit, which needs a structural statement about optimal circuits; (ii) counting or pigeonhole arguments over circuit structures (the literature reports such an argument for the maximum MC over 7-variable functions; not read in full); (iii) exhaustive computation for a fixed base function combined with a composition theorem that is not restriction-based.

## 7. What is not proved here

- The fresh-variable lemma for $g$ with $\mathrm{MC}(g)>D(g)$ in general (open; PNE-001). Verified for $g^*$ (Proposition 10) and for the 5-variable sample in EXP-004.
- The AND-direct-sum $\mathrm{MC}(g(x)h(y))=\mathrm{MC}(g)+\mathrm{MC}(h)+1$ (PNE-002). It would imply explicit functions with $\mathrm{MC}\ge cn$, hence circuit size $\ge cn$ over the full binary basis, for every constant $c$ (take a brute-force-hardest function on a constant number of variables and AND together $n/k$ copies). The best refereed explicit bound for circuit size is about $3.1n$, so this statement is at least as hard as a major open problem.
- The multiplexer lemma MC((1+s)P + sQ) = MC(P) + MC(Q) + 1, for P, Q on disjoint variables and a fresh selector s, would imply PNE-001 (take P = 0). It would also imply explicit MC ≥ cn for every c, via a decision list over brute-force-hard constant-size blocks, so in general it is as strong as PNE-002. The first function with MC > D on 5 variables (g* in EXP-002) is a multiplexer, so this is where restriction depth and MC separate.
- Novelty: **Lemma 1 is essentially known.** Chistopolskaya–Podolskii (arXiv 1810.08668 / ECCC TR18-174) prove $D_\oplus(f)\le c_\wedge(f)+1$ by the same induction on AND gates (per search-result summaries; full text not read). Lemma 1 is marginally stronger, since $D\ge D_\oplus-1$, but uses the same argument. Lemma 3 is folklore. Theorem 4 (fresh variable for restriction depth) and Theorem 8 (the cap) were not found in the literature checked (`research/literature/index-multiplicative-complexity.md`). However, "Direct Sums for Parity Decision Trees" (arXiv 2412.06552, CCC 2025) studies closely related composition questions for parity decision trees and could not be read here (`research/literature/pdt-2024-direct-sums-parity-decision-trees.md`). Theorem 4 may be known or easily implied there. Treat its novelty as unconfirmed until that paper is read.
- Scope of the explicit-bound application: the open problem stated by Chistopolskaya–Podolskii is an explicit $f$ with $c_\wedge(f)>n$ (strict). A 6-variable seed with MC 6, together with PNE-001, would give MC $=n$ exactly: above the known explicit $n-1$, but not $>n$. A strict bound would need a certified seed with $\mathrm{MC}(g)\ge k+1$ on $k$ variables; such seeds exist non-constructively for $k\ge 8$ by counting, but none is certified.

## 8. Formalization

Not formalized in Lean. Formalizing Theorem 4 needs affine subspaces, restrictions and coordinate changes over $\mathbb{F}_2$; the project currently uses core Lean without Mathlib (Mathlib's build cache host is blocked here). What is formalized in this cycle is listed in `research/proofs/lean/README.md`.
