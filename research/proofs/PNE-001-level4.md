# PNE-001 at level 4: structure of counterexamples, and the 5-variable case

Cycle 002, 2026-11-25. Builds on `PNE-001-restriction-depth-and-fresh-variables.md` (cycle 001), whose numbering continues here.
Status: proofs written by the chief researcher; independent audit pending (`audits/`).

**Question.** For non-constant $g$ with $\mathrm{MC}(g)=4$, is $\mathrm{MC}(y\,g)=5$? Since $\mathrm{MC}(g)\le\mathrm{MC}(y\,g)\le\mathrm{MC}(g)+1$, a *level-4 counterexample* is a $g$ with $\mathrm{MC}(g)=4=\mathrm{MC}(y\,g)$.

Notation and facts from cycle 001:
- (F1)–(F3), the restriction $f|_{\langle v,x\rangle=c}$, and Lemma 9.
- Lemma 11: for $F=y\,g$, $(v,0)$ is admissible iff $(v,1)$ is, by the Case C identity of Theorem 4.
- Theorem 17: PNE-001 holds for every non-constant $h$ with $\mathrm{MC}(h)\le3$.

A direction $v$ is **cheap at level $m$** for $g$ if each half $g|_{\langle v,x\rangle=c}$ is constant or has $\mathrm{MC}\le m-2$.

## Lemma 9′ (strong first-gate criterion)

Let $\mathrm{MC}(F)=m\ge1$. Take an $m$-gate circuit for $F$ whose first gate is $a\cdot b$, with $a=\langle u_1,x\rangle+e$ and $b=\langle u_2,x\rangle+e'$. Then $u_1,u_2\ne0$ and $u_1\ne u_2$. For each $u\in\{u_1,u_2,u_1+u_2\}$ and each $c$, $\mathrm{MC}(F|_{\langle u,x\rangle=c})\le m-1$.

*Proof.* Optimality excludes degenerate first gates, which gives $u_1,u_2\ne0$ and $u_1\ne u_2$. On $\langle u_1,x\rangle=c$ the form $a$ is constant, and on $\langle u_2,x\rangle=c$ the form $b$ is constant. On $\langle u_1+u_2,x\rangle=c$ we have $b=a+c''$ for a constant $c''$, so $ab=a(1+c'')\in\{0,a\}$. In each case the first gate becomes affine. Substitute it into later forms (F2), which leaves $m-1$ gates. $\square$ (AUDIT-002 noted this strengthening, I-4.)

## Lemma 18 (structure of MC ≤ 2)

$\mathrm{MC}(f)\le2$ iff $f$ is of one of two types:
- **(Q)** $\deg f\le2$, and the symplectic form of $f$ has rank $\le4$;
- **(C)** $f=\ell\cdot q+\lambda$ with $\ell,\lambda$ affine and $\mathrm{MC}(q)\le1$, i.e. $q=ab+\alpha$ with $a,b,\alpha$ affine.

*Proof.* (⇐) Type (Q) has the symplectic normal form $a_1b_1+a_2b_2+$ affine, so 2 gates suffice. Type (C) is computed by $z_1=ab$, $z_2=\ell\,(z_1+\alpha)$, with output $z_2+\lambda$.

(⇒) Take a 2-gate circuit: $z_1=ab$, $z_2=AB$ with $A,B\in\mathrm{span}(1,x,z_1)$, and output $f=\lambda+c_1z_1+c_2z_2$. If $c_2=0$, then $\mathrm{MC}(f)\le1$, which is type (Q) of rank $\le2$. Otherwise:
- *Neither $A$ nor $B$ contains $z_1$.* Then $f=\lambda+c_1ab+AB$ has degree $\le2$ and rank $\le4$: type (Q).
- *Exactly one contains $z_1$*, say $A=z_1+\alpha$ with $\alpha$ affine, $B$ affine. Then $f=\lambda+c_1ab+B(ab+\alpha)=(B+c_1)(ab+\alpha)+(c_1\alpha+\lambda)$: type (C).
- *Both contain $z_1$*: $A=z_1+\alpha$, $B=z_1+\beta$. Since $z_1^2=z_1$, $AB=z_1(1+\alpha+\beta)+\alpha\beta$. Put $\ell=1+c_1+\alpha+\beta$. Then $f=\ell\,ab+\alpha\beta+\lambda$. Now $\alpha\beta=\alpha(\ell+1+c_1+\alpha)=\alpha\ell+c_1\alpha$, using $\alpha^2=\alpha$. So $f=\ell(ab+\alpha)+(c_1\alpha+\lambda)$: type (C). $\square$

Remarks.
- Up to affine equivalence and adding affine functions, the nonzero cases are $x_1x_2$ (MC 1), $x_1x_2+x_3x_4$, $x_1x_2x_3$ and $x_3(x_1x_2+x_4)$ (MC 2). This is consistent with the "three representative forms" for MC 2 attributed to Find–Smith-Tone–Sönmez Turan (ePrint 2015/1041). That attribution comes from a search summary only; the representatives were not seen.
- Any type-(C) function of degree 3 has top-degree part $\ell_{\rm lin}a_{\rm lin}b_{\rm lin}$, a product of three linear forms.

## Lemma 19 (derivatives of MC ≤ 2 functions)

If $\mathrm{MC}(f)\le2$, then for every direction $e$ the derivative $D_ef(x)=f(x)+f(x+e)$ has degree $\le2$, and its symplectic rank is $\le4$. More precisely:
- if $f$ is of type (Q), $D_ef$ is affine;
- if $f=\ell q+\lambda$ with $\ell_{\rm lin}(e)=0$, then $D_ef=\ell\,\delta+{\rm const}$;
- if $f=\ell q+\lambda$ with $\ell_{\rm lin}(e)=1$, then $D_ef=q+\ell\,\delta+{\rm affine}$.

Here $\delta=D_eq$ is affine.

*Proof.*
- A function of degree $\le2$ has affine derivatives.
- For type (C), write $\ell(x+e)=\ell+\varepsilon$ with $\varepsilon=\ell_{\rm lin}(e)$, and $q(x+e)=q+\delta$ with $\delta=D_eq$. The derivative $\delta$ is affine because $\deg q\le2$. Then
$$D_e(\ell q)=(\ell+\varepsilon)(q+\delta)+\ell q=\ell\delta+\varepsilon q+\varepsilon\delta.$$
- The rank bound follows: $\ell\delta$ has rank $\le2$, and $q$ has rank $\le2$. $\square$

## Lemma 20 (a level-4 counterexample has a cheap plane with quadratic cross terms)

Let $g$ be non-constant with $\mathrm{MC}(g)=4=\mathrm{MC}(y\,g)$. Then there are linearly independent $v_1,v_2$ such that every nonzero $v\in\mathrm{span}(v_1,v_2)$ is cheap at level 4. In coordinates with $\langle v_1,x\rangle=x_1$ and $\langle v_2,x\rangle=x_2$, write
$$g=g_{00}+x_1d_1+x_2d_2+x_1x_2d_{12},$$
with $g_{ab}=g|_{x_1=a,x_2=b}$, $d_1=g_{00}+g_{10}$, $d_2=g_{00}+g_{01}$ and $d_{12}=\sum_{a,b}g_{ab}$, all functions of $x'=(x_3,\dots)$. Then $\deg d_1,\deg d_2,\deg d_{12}\le2$. Every quarter $g_{ab}$ is constant or has $\mathrm{MC}\le2$.

*Proof.*
- Let $F=y\,g$, and take an optimal 4-gate circuit for it, with first gate $a\cdot b$ of directions $u_1=(v_1,s_1)$ and $u_2=(v_2,s_2)$ ($s_i$ is the $y$-coefficient). By Lemma 9′, $u_1$, $u_2$ and $u_1+u_2$ are admissible at level 4.
- The direction $(0,1)=e_y$ is not admissible, because $F|_{y=1}=g$ has MC 4. So $v_1\ne0$, $v_2\ne0$ and $v_1\ne v_2$.
- For an admissible $(v,s)$ with $v\ne0$, Lemma 11's identity gives $\mathrm{MC}(t\cdot g|_{\langle v,x\rangle=c})\le3$ for both $c$, where $t$ is a fresh variable.
- If $g|_{\langle v,x\rangle=c}$ is non-constant, it has $\mathrm{MC}\le3$ (set $t=1$). Theorem 17 then gives $\mathrm{MC}(g|_{\langle v,x\rangle=c})+1\le3$. So $v_1$, $v_2$ and $v_1+v_2$ are cheap.
- The halves along $x_1$ are $H_0=g_{00}+x_2d_2$ and $H_1=(g_{00}+d_1)+x_2(d_2+d_{12})$, functions of $(x_2,x')$. Each is constant or has MC $\le2$. Their derivatives in the $x_2$-direction are $d_2$ and $d_2+d_{12}$, which have degree $\le2$ by Lemma 19 (a constant has derivative 0).
- The halves along $x_2$ give in the same way that $d_1$ and $d_1+d_{12}$ have degree $\le2$.
- Quarters are restrictions of halves, so their MC is $\le2$. $\square$

## Corollary 21 (level 4 on 5 variables is a finite family)

On 5 variables, use coordinates $(x_1,x_2,u_1,u_2,u_3)$. Every level-4 counterexample is, after an affine change of coordinates that does not touch $y$, a member of
$$\mathcal F_5=\{\,g_{00}(u)+x_1d_1(u)+x_2d_2(u)+x_1x_2d_{12}(u)\ :\ g_{00}\text{ arbitrary},\ \deg d_i\le2\,\},$$
a set of $2^8\cdot(2^7)^3=2^{29}$ functions. Conversely, in every member of $\mathcal F_5$ the directions $x_1$, $x_2$ and $x_1+x_2$ are cheap at level 4. The reason: the halves are 4-variable functions of degree $\le3$, and on 4 variables MC $\le2$ holds exactly for degree $\le3$ (EXP-001).

*Proof.* Lemma 20 applies, with $x'=u$ of dimension 3. The converse holds because each half has the form $h+x\,d$ with $\deg h\le3$ and $\deg d\le2$. $\square$

Affine changes of $x$-coordinates preserve both $\mathrm{MC}(g)$ and $\mathrm{MC}(y\,g)$, because $(y\,g)\circ(T\times{\rm id})=y\,(g\circ T)$. So it suffices to test the members of $\mathcal F_5$ with $\mathrm{MC}=4$. This is EXP-008, which uses the exact MC ≤ 3 set from EXP-007.

## Computational results so far (EXP-007, EXP-008)

**Exact MC of all 5-variable functions (EXP-007).** The span enumeration is exhaustive and uses no SAT solver. The first gate runs over 155 classes; there are 77,035 spaces $W_2$ and 150,409,210 third-gate cosets. Distribution:

| MC | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| number of 5-variable functions | 64 | 9,920 | 1,801,472 | 777,759,744 | 3,515,396,096 |

Checks:
- $|S_2|=1{,}811{,}456$ reproduces the cycle-001 value, which AUDIT-002 confirmed independently.
- No degree-5 function lies in $S_3$, as the degree bound requires.
- The orbit computation below found no affine image leaving $S_3$ across about $4\cdot10^9$ generator applications, so $S_3$ is affine-invariant, as it must be.
- Lemma 18 holds exactly on 5 variables. The predicted set, 65,536 quadratics together with the type-(C) functions, equals $S_2$ element for element (`EXP-007/lemma18_check.py`). The check uses only restrictions and the 4-variable table.

**Level-4 candidates on 5 variables (EXP-008).**
- Of the $2^{29}$ members of $\mathcal F_5$, **337,784,832 have MC 4**. So Lemma 20's necessary condition is weak on 5 variables.
- The group that preserves $\mathcal F_5$ consists of $T(x_1,x_2,u)=(A(x_1,x_2)+c,\ Mu+N(x_1,x_2)+c')$ with $A\in GL(2)$, $M\in GL(3)$ and $N$ an arbitrary $3\times2$ matrix (the shears), together with complementation. Every element preserves $\mathrm{MC}(g)$ and $\mathrm{MC}(y\,g)$. Under it the candidates fall into **297 orbits**, recorded with their sizes in `EXP-008/orbit_reps.txt`.
- Consequently, **PNE-001 holds for every $g$ on $\le5$ variables iff $\mathrm{MC}(y\,g)=5$ for these 297 representatives.** The reason: Theorem 17 covers MC $\le3$, every 5-variable function has MC $\le4$, and Corollary 21 together with the orbit reduction covers MC 4.
