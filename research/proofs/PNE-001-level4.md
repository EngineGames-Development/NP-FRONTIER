# PNE-001 at level 4: structure of counterexamples, and the 5-variable case

Cycle 002, 2026-11-25. Builds on `PNE-001-restriction-depth-and-fresh-variables.md` (cycle 001), whose numbering continues here.
Status: proofs written by the chief researcher; independent audit AUDIT-003 pending (`audits/`).
**Main result of this document: Theorem 25 — PNE-001 holds at level 4 for every n (computer-assisted). With Theorem 17: MC(y·g) = MC(g)+1 for every non-constant g with MC(g) ≤ 4.** Sections 22–27 below; sections 9′–21 are the earlier structural route, which now serves as an independent check of the case n ≤ 5.

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


---

# Part II (cycle 002, second half): level 4 for all n

Notation. For $f:\mathbb F_2^n\to\mathbb F_2$ let $V(f)=\{v: D_vf\text{ is constant}\}$ (a linear subspace) and $\dim f=n-\dim V(f)$, the *dimension* of $f$. Equivalently, $\dim f$ is the least $r$ with $f=\lambda+h(\ell_1,\dots,\ell_r)$ for an affine $\lambda$ and linear forms $\ell_i$. (Proof of the equivalence: if $D_vf$ is constant on $V(f)$, the map $v\mapsto D_vf$ is linear on $V(f)$; extend it to a linear form $c$; then $f+c$ is $V(f)$-invariant, so it factors through $\mathbb F_2^n/V(f)$. Conversely, if $f=\lambda+h(\ell)$, every $v$ in $\bigcap\ker\ell_i$ has $D_vf=D_v\lambda$ constant.) For an affine subspace $C$ of dimension $k$ and $h:C\to\mathbb F_2$, $\mathrm{MC}(h)$ means $\mathrm{MC}(h\circ\varphi)$ for any affine bijection $\varphi:\mathbb F_2^k\to C$; this does not depend on $\varphi$.

(F4) If $A:\mathbb F_2^n\to C$ is an affine surjection and $\mu$ is affine, then $\mathrm{MC}(h\circ A+\mu)=\mathrm{MC}(h)$. *Proof.* $\le$: substitute $A$ into a circuit for $h$ and add $\mu$ at the output (free). $\ge$: pick an affine section $S$ with $A\circ S=\mathrm{id}_C$; then $h=(h\circ A+\mu)\circ S+\mu\circ S$. $\square$

## Lemma 22 (dimension, and what it gives for PNE-001)

(a) $\mathrm{MC}(f)\ge\lceil\dim f/2\rceil$. **Known:** Çalık–Sönmez Turan–Peralta, *Boolean functions with multiplicative complexity 3 and 4*, Cryptogr. Commun. 2020 (abstract retrieved from csrc.nist.gov this cycle; proof sketch on their BFA 2019 slide: a $k$-gate topology has $2k$ linear inputs).

(b) For non-constant $g$: $\dim(y\,g)\ge\dim g+1$. Hence $\mathrm{MC}(y\,g)\ge\lceil(\dim g+1)/2\rceil$.

(c) Consequences. A level-$m$ counterexample ($\mathrm{MC}(g)=m=\mathrm{MC}(y\,g)$) has $\dim g\le 2m-1$. PNE-001 holds for every $g$ with $\dim g=2\,\mathrm{MC}(g)$. In particular **PNE-001 holds for every quadratic $g$**: a quadratic form of symplectic rank $2s$ has $\dim=2s$ and $\mathrm{MC}=s$ (normal form $\sum_{i\le s}a_ib_i$ + affine for $\le$, part (a) for $\ge$).

*Proof of (a)* (for completeness). In an $m$-gate circuit let $L$ be the span of the linear parts of the $2m$ gate inputs. By induction every gate is a function of the forms in $L$, so the output is affine plus a function of $\le 2m$ forms. $\square$

*Proof of (b).* Let $F=y\,g$ on $\mathbb F_2^{n+1}$ and $w=(w_x,w_y)\in V(F)$. If $w_y=1$ then $D_wF(x,0)=g(x+w_x)$ must be constant, so $g$ is constant: excluded. So $w_y=0$, and then $D_wF=y\,D_{w_x}g$ is constant only if $D_{w_x}g\equiv0$. Thus $V(F)=P(g)\times\{0\}$ with $P(g)=\{v:D_vg\equiv0\}$, a subspace of $V(g)$ of codimension $\le1$ (it is the kernel of the linear map $v\mapsto D_vg$ on $V(g)$). So $\dim F=n+1-\dim P(g)\ge n+1-\dim V(g)=\dim g+1$. $\square$

*Proof of (c).* $m=\mathrm{MC}(y\,g)\ge(\dim g+1)/2$. If $\dim g=2\mathrm{MC}(g)$ then $\mathrm{MC}(y\,g)\ge\mathrm{MC}(g)+\tfrac12$. $\square$

Remark. Part (b) is elementary; we did not find it stated. Part (c) for quadratics may be known (quadratic MC is classical: Mirwald–Schnorr 1992). Lemma 22 alone gives only $\dim g\le7$ at level 4. Lemma 23 removes the dependence on $n$ altogether.

## Lemma 23 (formal-circuit reformulation)

Fix $m\ge1$ and $N=2m$. A **formal $m$-gate circuit** $\Phi$ is a choice of wiring vectors $\alpha_i,\beta_i\in\mathbb F_2^{i-1}$ ($1\le i\le m$) and $\gamma\in\mathbb F_2^{m-1}$. It defines $\Phi:\mathbb F_2^{N}\to\mathbb F_2$ by
$$z_i=\Big(w_{2i-1}+\sum_{j<i}\alpha_{ij}z_j\Big)\Big(w_{2i}+\sum_{j<i}\beta_{ij}z_j\Big),\qquad \Phi=z_m+\sum_{j<m}\gamma_jz_j .$$
(Each gate input has its own formal variable and no constant.)

**Lemma 23.** The following are equivalent.
1. There is a non-constant $g$ (on some number $n$ of variables) with $\mathrm{MC}(g)=m=\mathrm{MC}(y\,g)$.
2. There are a formal $m$-gate circuit $\Phi$, a linear subspace $K\subseteq\mathbb F_2^{N}$ and two distinct cosets $C_0\ne C_1$ of $K$ such that $\Phi|_{C_0}$ is affine and $\mathrm{MC}(\Phi|_{C_1})\ge m$.

Moreover in 2 one may assume $\dim K\ge k_{\min}(m)$, the least $k$ for which some $k$-variable function has MC $\ge m$. One may also assume $\alpha_i\le\beta_i$ in any fixed total order of $\mathbb F_2^{i-1}$, for every $i\ge2$.

*Proof.* (1⇒2) Take a circuit for $F=y\,g$ with $\mathrm{MC}(F)=m$ gates, gate $i$ having inputs $A_i=\ell_{2i-1}(x,y)+c_{2i-1}+\sum_{j<i}\alpha_{ij}z_j$ and $B_i=\ell_{2i}(x,y)+c_{2i}+\sum_{j<i}\beta_{ij}z_j$, with linear forms $\ell_t$ and constants $c_t$, and output $F=\lambda+\sum_j\gamma'_jz_j$ with $\lambda$ affine.
- $\gamma'_m=1$, since otherwise gate $m$ is unused and $\mathrm{MC}(F)<m$.
- Let $w:\mathbb F_2^{n+1}\to\mathbb F_2^{N}$ be the linear map $w(x,y)=(\ell_1(x,y),\dots,\ell_N(x,y))$, let $c=(c_t)$, and let $\Phi$ be the formal circuit with the same $\alpha,\beta,\gamma$ (with $\gamma_j=\gamma'_j$ for $j<m$).
- Induction on $i$ shows that gate $i$ of the real circuit equals $z_i^\Phi(w(x,y)+c)$. So $F(x,y)=\lambda(x,y)+\Phi(w(x,y)+c)$.
- Put $K=w(\mathbb F_2^n\times\{0\})$, $\delta=w(0,1)$, $C_0=K+c$ and $C_1=K+c+\delta$.
- At $y=0$: $\Phi(w(x,0)+c)=\lambda(x,0)$ for all $x$. The map $x\mapsto w(x,0)+c$ is an affine surjection onto $C_0$, so by (F4) applied to an affine section, $\Phi|_{C_0}$ is affine.
- At $y=1$: $g(x)=\lambda(x,1)+\Phi(w(x,0)+c+\delta)$. Here $x\mapsto w(x,0)+c+\delta$ is an affine surjection onto $C_1$, so $\mathrm{MC}(\Phi|_{C_1})=\mathrm{MC}(g)=m$ by (F4).
- If $C_1=C_0$ then $g$ would be affine. So the cosets are distinct.
- $\Phi|_{C_1}$ is a function on $\dim K$ variables with MC $\ge m$, so $\dim K\ge k_{\min}(m)$.

(2⇒1) Let $k=\dim K$. Choose a linear bijection $T:\mathbb F_2^k\to K$, a point $c\in C_0$, and $\delta$ with $C_1=C_0+\delta$ (so $\delta\notin K$). Let $\mu(x)=\Phi(Tx+c)$, which is affine. Define $F(x,y)=\Phi(Tx+c+y\delta)+\mu(x)$ on $\mathbb F_2^{k+1}$.
- $F$ has an $m$-gate circuit: substitute the affine forms $w=Tx+c+y\delta$ into $\Phi$ and add $\mu$.
- $F(x,0)=0$ and $F(x,1)=G(x):=\Phi(Tx+c+\delta)+\mu(x)$, so $F=y\,G$.
- By (F4), $\mathrm{MC}(G)=\mathrm{MC}(\Phi|_{C_1})\ge m\ge \mathrm{MC}(F)\ge\mathrm{MC}(G)$. So $G$ satisfies 1.

Symmetry. Let $\sigma_i$ swap the coordinates $w_{2i-1},w_{2i}$, and let $\Phi'$ be $\Phi$ with $\alpha_i,\beta_i$ exchanged. Gate $i$ is a product, earlier gates do not involve $w_{2i-1},w_{2i}$, and later gates see only $z_i$. Hence $\Phi'=\Phi\circ\sigma_i$. Since $\sigma_i$ maps subspaces and cosets to subspaces and cosets, condition 2 holds for $\Phi'$ iff it holds for $\Phi$. $\square$

Remarks.
- For each $m$, condition 2 is a finite problem, independent of $n$. For $m=4$ there are $2\cdot2\cdot4\cdot4\cdot8\cdot8\cdot8=32768$ formal circuits ($8640$ after the swap reduction), and $k\in\{5,6,7\}$, since every 4-variable function has MC $\le3$ (Sönmez Turan–Peralta 2014; EXP-001). Finally, $\dim K=8$ is impossible because $C_0\neq C_1$.
- Statement 2 is the "skeleton-shift" picture made exact: $\Phi$ on $C_0$ is the zero circuit (up to an affine output), and $C_1$ is its shift.

## Lemma 24 (degenerate gates)

In the setting of Lemma 23(2), suppose some gate $i$ satisfies one of the following:
- (a) $\alpha_i=0$ and the functional $w_{2i-1}$ vanishes on $K$;
- (b) $\beta_i=0$ and $w_{2i}$ vanishes on $K$;
- (c) $\alpha_i=\beta_i$ and $w_{2i-1}+w_{2i}$ vanishes on $K$.

Then $\mathrm{MC}(\Phi|_C)\le m-1$ for **every** coset $C$ of $K$.

*Proof.* On $C$, every $w_t$ is an affine function.
- In case (a), $A_i$ is constant on $C$, so $z_i=A_iB_i\in\{0,B_i\}$.
- In case (c), $B_i=A_i+\epsilon$ for a constant $\epsilon$, so $z_i=A_i(A_i+\epsilon)=(1+\epsilon)A_i$.

Either way $z_i$ is an affine combination of $1$, the restricted $w$'s and $z_j$ with $j<i$. Substituting it into the later gates and the output gives an $(m-1)$-gate circuit on $C$. $\square$

## Theorem 25 (PNE-001 at level 4, every $n$; computer-assisted)

**For every $n$ and every $g:\mathbb F_2^n\to\mathbb F_2$ with $\mathrm{MC}(g)=4$: $\mathrm{MC}(y\,g)=5$.** Together with Theorem 17: **$\mathrm{MC}(y\,g)=\mathrm{MC}(g)+1$ for every non-constant $g$ with $\mathrm{MC}(g)\le4$.**

*Proof.* By Lemma 23, it suffices to show the following. For every formal 4-gate circuit with $\alpha_i\le\beta_i$, every subspace $K\subseteq\mathbb F_2^8$ with $\dim K\in\{5,6,7\}$ and every pair of distinct cosets with $\Phi|_{C_0}$ affine, $\mathrm{MC}(\Phi|_{C_1})\le3$. EXP-014 (`formal4.c`) enumerates all 8640 wirings and all $255+10{,}795+97{,}155$ subspaces (counts equal the Gaussian binomials $\binom{8}{7}_2,\binom86_2,\binom85_2$). Results:

| $\dim K$ | cosets with $\Phi\vert_{C_0}$ affine | pairs $(C_0,C_1)$ | degenerate (Lemma 24) | non-degenerate | distinct modulo affine | 3-gate circuit found |
|---|---|---|---|---|---|---|
| 7 | 1,020 | 840 | 840 | 0 | 0 | — |
| 6 | 297,128 | 509,220 | 489,576 | 19,644 | 72 | 72 / 72 (SAT, re-evaluated) |
| 5 | 17,467,504 | 66,989,104 | 57,400,384 | 9,588,720 | 2,142 | 2,142 / 2,142 (SAT, re-evaluated) |

For $\dim K=5$:
- The exact table (EXP-007/010) gives MC $\le3$ for all 66,989,104 pairs. The MC distribution is 1: 23,017,648; 2: 27,492,928; 3: 16,478,528; 4: 0.
- Table-free check: the non-degenerate ones reduce to 2,142 functions modulo affine functions, and **every one has an explicit 3-gate circuit** (SAT, re-evaluated; EXP-014/`mc3_check_k5.log`). The proof of Theorem 25 therefore does not depend on the 5-variable table.
- MC is unchanged by adding an affine function, so deduplicating modulo affine functions is sound. $\square$ (conditional on the computations; see the verification record)

**Verification record.**
- `formal4.c`:
  - The affinity test passed 1.4 million unit tests (`test_affine.c`).
  - The coset/coordinate indexing self-test is built in.
  - The optimized and the direct restriction code produce identical $\dim K=7$ output.
- Without the swap reduction (`formal4_full`, all 32,768 wirings):
  - $\dim K=7$: 3,072 affine cosets / 2,688 pairs.
  - $\dim K=6$: 908,800 / 1,663,872; the 72,576 non-degenerate pairs give 160 distinct functions modulo affine, and all 160 have 3-gate circuits.
- Independent re-implementation (`indep_check.py`: numpy, subspaces as kernels of dual subspaces, affinity by interpolation, degeneracy tested in the dual, full wirings):
  - $\dim K=7$: 3,072 / 2,688 / 0 non-degenerate, identical to `formal4_full`.
  - $\dim K=6$: see the log.
- The same method for $m\le3$ (`formalm.c`) finds no counterexample at levels 1–3. This re-derives Theorem 17, which cycle 001 proved by DRAT-checked SAT, by an unrelated method.
- A second, independent route via NIST's published class list is Lemma 26 below.

## Lemma 26 (class-list reformulation)

A level-$m$ counterexample exists if and only if the following holds. Some $R$ with $\mathrm{MC}(R)=m$, on $d=\dim R$ variables, has an affine hyperplane $H\subset\mathbb F_2^d$ such that $R|_H$ is affine and $\mathrm{MC}(R|_{\mathbb F_2^d\setminus H})=m$. Since the condition is invariant under affine equivalence (affine maps of the input plus addition of affine functions), $R$ may be taken from any complete list of class representatives.

*Proof.* (⇒) Let $F=y\,g$ with $\mathrm{MC}(F)=m=\mathrm{MC}(g)$ and $d=\dim F$. Write $F=R\circ\Phi+\lambda$ with $R$ on $d$ variables, $\Phi$ an affine surjection $\mathbb F_2^{n+1}\to\mathbb F_2^d$, and $\lambda$ affine.
- Let $E=\{y=0\}$. If $\Phi(E)=\mathbb F_2^d$, then $R\circ\Phi|_E=\lambda|_E$ is affine and (F4) makes $R$ affine, which is impossible.
- So the linear part of $\Phi$ maps $E$ onto a linear hyperplane $E_0$. The image of $(0,1)$ lies outside $E_0$, by surjectivity. Hence $\Phi(E)=H$ and $\Phi(\{y=1\})=\mathbb F_2^d\setminus H$ for an affine hyperplane $H$.
- By (F4), $R|_H$ is affine and $\mathrm{MC}(R|_{H^c})=\mathrm{MC}(g)=m$.

(⇐) Choose coordinates in which $H=\{y'=0\}$. Extend the affine function $R|_H$ to an affine $\mu$ on $\mathbb F_2^d$. Then $R+\mu=y'\cdot G$ with $G=(R+\mu)|_{y'=1}$, and $\mathrm{MC}(y'G)=\mathrm{MC}(R)=m=\mathrm{MC}(G)$ by (F4). $\square$

**Independent verification of Theorems 17 and 25 (EXP-015).** Çalık, Sönmez Turan and Peralta (2020) list all affine classes with MC 3 (24 classes) and MC 4 (1277 classes; dimensions 5–8). The lists are at `github.com/usnistgov/circuits/data/mc_dim` and were cloned this cycle; the counts match the paper. For each representative and each of its $2(2^d-1)$ affine hyperplanes, `nist_hyperplane_check.py` tests affinity of $R|_H$. For every hit it finds an $(m-1)$-gate circuit for $R|_{H^c}$ by SAT, re-evaluated.
- Level 3: 24 classes, 27 hyperplanes with affine restriction, all halves have MC $\le2$. No counterexample, for any $n$.
- **Level 4: all 1277 classes, 186 hyperplanes with affine restriction, and every complementary half has a 3-gate circuit. No counterexample, for any $n$** (`EXP-015/nist_level4.log`).

This route shares no code with EXP-014 except the SAT encoding `mc.py`, which is DRAT-validated in cycle 001. It depends on the correctness and completeness of the published class list.

## Theorem 27 (all functions on at most 5 variables)

**$\mathrm{MC}(y\,g)=\mathrm{MC}(g)+1$ for every non-constant $g$ on $\le5$ variables.** Every 5-variable function has MC $\le4$: by EXP-007, and by Sönmez Turan–Peralta 2014. So this is a special case of Theorems 17 and 25. It also has three further, mutually independent confirmations:
1. The structural route (Lemma 20, Corollary 21, EXP-008 orbits, EXP-010 `cert4b`): all 297 orbit representatives give MC$(y\,g)\ge5$, and all 74 positive controls are correctly accepted.
2. The $\dim K=5$ case of EXP-014.
3. NIST's 6-variable classification (EXP-015 `nist_level_check.py`). Each 5-variable $g$ of MC $m\in\{3,4\}$ is affine-equivalent to a listed representative $g_0$ plus a linear form, and $\mathrm{MC}(y(g_0\circ T+\ell))=\mathrm{MC}(y(g_0+\ell\circ T^{-1}))$. So it suffices to test $y(g_0+\ell)$ for the 32 linear $\ell$. The 544 (level 3) and 832 (level 4) such functions all have affine-invariant fingerprints that differ from every listed class of MC $\le m$, so MC$(y(g_0+\ell))=m+1$.

Our exact 5-variable MC table agrees with NIST's MC for every one of the 48 affine classes of 5-variable functions, and it passed 200,000 random affine-invariance tests (`EXP-015/check_mc5_vs_nist.py`). Open discrepancy: the constant $s_5=1{,}576{,}479{,}744$ in the counting formula for MC-3 functions on NIST's 2019 slide does not match our count of dimension-5 MC-3 functions, 775,728,128. The MC-2 formula on the same slide matches our count exactly (1,801,472 for $n=5$, 31,616 for $n=4$), and our MC-3 total is supported by the class-by-class agreement. The paper text, which would settle the slide's normalization, could not be retrieved (Cloudflare challenge).

## Limits and what remains
- Theorem 25 is computer-assisted. Its correctness rests on the reformulation (Lemma 23) and on the enumeration code. The two independent routes (EXP-014 and EXP-015) reduce, but do not remove, the risk of a coding error.
- No human-readable proof of level 4 is known. The structural lemmas (9′, 18–21) explain the 5-variable case only partly.
- **Level 5** is open. In Lemma 23 it needs $\dim K\in\{6,\dots,9\}$ inside $\mathbb F_2^{10}$. That means $\binom{10}{4}_2\approx5.4\cdot10^7$ subspaces of dimension 6 alone, about $2.3\cdot10^6$ wirings, and MC tests on up to 9 variables. Degeneracy pruning (Lemma 24) and symmetry must cut this down. Lemma 26 would need the full list of MC-5 classes, which NIST reported as incomplete in 2019 (their repository contains dimension 6 and 10 lists only).
- PNE-001 in general, and its AND-direct-sum strengthening PNE-002, remain open. Nothing here bears on P vs NP beyond this restricted measure.
