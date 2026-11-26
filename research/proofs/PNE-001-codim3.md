# PNE-001: the codimension-3 case, every level (Lemma 32)

Cycle 003, 2026-11-25. Continues the numbering of `PNE-001-level4.md` (Lemmas 22–30, Corollaries 29, 31), whose notation is used throughout.
Status: proof written by the chief researcher. Independent audit **AUDIT-004** (`audits/AUDIT-004-PNE-001-codim3.md`) found no fatal or serious issue: Lemma 32 survives for every $m$, Corollaries 33 and 35 survive, and Corollary 34 survives after a citation fix. Corrections I-1 to I-8 are applied in this version. Checks: EXP-018 (exhaustive at $m=4$, sampled at $m=5$), plus the auditor's own harness (all 32,768 wirings at $m=4$; samples at $m=5,6$; 0 violations).

**Results.**
- **Lemma 32 (human proof, every $m$).** A formal $m$-gate circuit that is affine on one coset of a subspace of codimension 3 has $\mathrm{MC}\le m-1$ on every coset.
- **Corollary 33.** PNE-001 holds for every non-constant $g$ with $\dim g\ge2\,\mathrm{MC}(g)-3$. A level-$m$ counterexample has $\dim g\le2m-4$.
- **Corollary 34.** Theorem 25 (level 4, every $n$) follows from Lemmas 23, 24, 28, 30 and 32 together with the classical fact that every 4-variable function has MC $\le3$. No other computation is needed.
- **Corollary 35.** A level-5 counterexample $g$ has $\dim g=6$ exactly. Equivalently, it lives in codimension 4 of $\mathbb F_2^{10}$ in Lemma 23.

## Setting and notation

$\Phi$ is a formal $m$-gate circuit (Lemma 23):
$$z_i=A_iB_i,\quad A_i=w_{2i-1}+\alpha_i\cdot z,\quad B_i=w_{2i}+\beta_i\cdot z,\qquad\Phi=z_m+\Gamma,\quad\Gamma=\gamma\cdot z,$$
where $\alpha_i\cdot z=\sum_{j<i}\alpha_{ij}z_j$. As in Lemma 28, write
- $u=w_{2m-1}$, $v=w_{2m}$, $w''=(w_1,\dots,w_{2m-2})$;
- $a=\alpha_m\cdot z$, $b=\beta_m\cdot z$.

So $\Phi=(u+a)(v+b)+\Gamma$, with $a$, $b$ and $\Gamma$ functions of $w''$ alone.

$K\subseteq\mathbb F_2^{2m}$ is a linear subspace and $H=K^\perp$. A coset of $K$ is $\{w:\langle h,w\rangle=d(h)\ \forall h\in H\}$ for a linear functional $d$ on $H$. Let $\pi:H\to\mathbb F_2^2$, $h\mapsto(h_u,h_v)$, and $H_0=\ker\pi$. For $h\in H$ write $h=(h'',h_u,h_v)$. The map $h\mapsto h''$ is injective on $H_0$.

**Three exits.** Each gives $\mathrm{MC}(\Phi|_C)\le m-1$ for a coset $C$.
- (X1) *A degenerate gate* (Lemma 24). This one works on every coset.
- (X2) *An unused gate.* Some gate $j<m$ appears in no later gate input and not in $\Gamma$. Then $\Phi$ is computed without it, on every coset.
- (X3) *A redundant gate on $C$.* For some $j$, $z_j|_C\in\mathrm{span}(1,\ \text{affine functions on }C,\ z_i|_C\ (i<j))$. Substituting this expression for $z_j$ into the later gates and the output leaves $m-1$ gates. In particular this holds if $\Phi|_C\in\mathrm{span}(\text{affine},z_1|_C,\dots,z_{m-1}|_C)$; we then say *the last gate is redundant on $C$*.

**Top gate of a vector.** For $0\ne h''\in\mathbb F_2^{2m-2}$, $\mathrm{top}(h'')$ is the largest $i$ such that $h''$ has a nonzero coordinate in $\{2i-1,2i\}$.

**(P1) Restriction to a hyperplane of $w''$-space.** Let $0\ne t\in\mathbb F_2^{2m-2}$, $k=\mathrm{top}(t)$, $c\in\mathbb F_2$ and $E=\{w'':\langle t,w''\rangle=c\}$. Write $t=t_k+t_{<k}$, where $t_k$ is supported on $\{2k-1,2k\}$ and $t_{<k}$ on coordinates $<2k-1$. Choose a coordinate $e\in\{2k-1,2k\}$ and a gate input $s\in\{A_k,B_k\}$ as follows:
- *type 1* ($t_k=e_{2k-1}$): $e=2k-1$, $s=B_k$;
- *type 2* ($t_k=e_{2k}$): $e=2k$, $s=A_k$;
- *type 3* ($t_k=e_{2k-1}+e_{2k}$): $e=2k$, $s=A_k$.

Use all coordinates of $w''$ except $w_e$ as coordinates of $E$; on $E$, $w_e$ is the affine function $w_e=c+\langle t-e_e,w''\rangle$. Let $\tau=e_e$, so $\langle t,\tau\rangle=1$ and $E'=\{\langle t,w''\rangle=c+1\}=E+\tau$. Let $L_{<k}=\mathrm{span}(1,w_1,\dots,w_{2k-2},z_1,\dots,z_{k-1})$, functions of the first $2k-2$ coordinates, all of which are coordinates of $E$.

Then:
- gates $j<k$ are unchanged on $E$, and also by the translation $w''\mapsto w''+\tau$, since they do not read $w_{2k-1}$ or $w_{2k}$;
- $s=(\text{a coordinate of }E)+(\text{an element of }L_{<k})$;
- on $E$, $z_k=\tilde A\,s$ with $\tilde A\in L_{<k}$, and $z_k(w''+\tau)=(\tilde A+1)\,s$.

*Proof.*
- Type 1: on $E$, $A_k=c+\langle t_{<k},w''\rangle+\alpha_k\cdot z=:\tilde A\in L_{<k}$. Translation by $e_{2k-1}$ adds 1 to $A_k$ and fixes $B_k=s$.
- Type 2 is symmetric.
- Type 3: on $E$, $w_{2k}=w_{2k-1}+c+\langle t_{<k},w''\rangle$, so $B_k=A_k+D$ with $D=c+\langle t_{<k},w''\rangle+(\alpha_k+\beta_k)\cdot z\in L_{<k}$. Hence $z_k=A_k(A_k+D)=A_k(1+D)$, using $A_k^2=A_k$. Translation by $e_{2k}$ adds 1 to $B_k$: $z_k(w''+\tau)=A_k(A_k+D+1)=A_kD$. Take $\tilde A=1+D$. $\square$

**(P2) Independence on $E$.** In the setting of (P1), suppose $\tilde A$ is not constant on $E$. If $\ell+\sum_{j\le m-1}c_jz_j$ is constant on $E$ for a linear form $\ell$ on $\mathbb F_2^{2m-2}$, then $c=0$ and $\ell\in\{0,t\}$.

*Proof.* Suppose $c\ne0$ and let $j=\max\mathrm{supp}\,c$. Work in the coordinates of $E$.
- *$j\ne k$.* The private variables $w_{2j-1},w_{2j}$ of gate $j$ are coordinates of $E$. In the expression, they occur only in $\ell$ and in $z_j$:
  - gates $i<j$ do not read them;
  - if $j<k$, the substitution for $w_e$ does not touch gates $\le j$;
  - if $j>k$, $w_e$ is not one of them.
  Since $z_j=(w_{2j-1}+\cdots)(w_{2j}+\cdots)$, the monomial $w_{2j-1}w_{2j}$ has coefficient 1. So the expression is not affine, and in particular not constant.
- *$j=k$.* The coordinate of $E$ inside $s$ occurs only in $z_k$ and in $\ell$. The derivative in that coordinate is $\tilde A+(\text{const})$, which is not constant.

So $c=0$. Finally, a linear form is constant on the affine hyperplane $E$ iff it lies in $\{0,t\}$. $\square$

**Non-degeneracy gives the hypothesis of (P2).** Let $h_0=(t,0,0)\in H$. The function $\tilde A$ is constant on $E$ iff:
- type 1: $\alpha_k=0$ and $t_{<k}=0$, i.e. $t=e_{2k-1}$;
- type 2: $\beta_k=0$ and $t=e_{2k}$;
- type 3: $\alpha_k=\beta_k$ and $t=e_{2k-1}+e_{2k}$.

In each case gate $k$ is degenerate for $K$, by Lemma 24(a), (b) or (c). These equivalences follow from the independence fact of Lemma 28 for the formal circuit on $w_1,\dots,w_{2k-2}$.

**Lemma 30′ (structural form of Lemma 30; stated for citation, AUDIT-004 I-3).** Let $\Psi$ be a formal $j$-gate circuit, let $K\subseteq\mathbb F_2^{2j}$ have codimension 2 with $H=K^\perp$, and suppose $\Psi$ is affine on some coset of $K$. Then at least one of the following holds:
- (i) some gate $i\le j$ is degenerate for $K$ in the sense of Lemma 24, i.e. its degeneracy vector ($e_{2i-1}$ with $\alpha_i=0$, $e_{2i}$ with $\beta_i=0$, or $e_{2i-1}+e_{2i}$ with $\alpha_i=\beta_i$) lies in $H$;
- (ii) on every coset $C$ of $K$, $\Psi|_C\in\mathrm{span}(\text{affine},z_1|_C,\dots,z_{j-1}|_C)$.

*Proof.* This is exactly what the written proof of Lemma 30 establishes.
- $\dim\pi(H)=0$ is impossible.
- $\dim\pi(H)=2$ is Case II, which gives (ii).
- In $\dim\pi(H)=1$, every sub-case ends in a condition of Lemma 24 whose degeneracy vector lies in $H$: $e_u$, $e_v$, $e_u+e_v$, or, via (IF′), the normal $h_0\in H$. That is (i).

AUDIT-003 §1 and AUDIT-004 §1 checked this. $\square$

Lemma 28 and (IF′) already name their degeneracy vectors in their statements.

## Lemma 32 (codimension 3) — every $m$

**Lemma 32.** Let $\Phi$ be a formal $m$-gate circuit, $K\subseteq\mathbb F_2^{2m}$ a linear subspace of codimension 3, and $C_0$ a coset of $K$ with $\Phi|_{C_0}$ affine. Then $\mathrm{MC}(\Phi|_C)\le m-1$ for every coset $C$ of $K$.

*Proof.* $C=C_0$ is trivial, so let $C\ne C_0$, and assume (X1) and (X2) do not apply. We split on $\dim\pi(H)$.

### Case $\dim\pi(H)=0$
Then $u,v$ are free on $C_0$, and $D_uD_v\Phi|_{C_0}=1$. Impossible.

### Case $\dim\pi(H)=1$
Then $\dim H_0=2$ and $H=H_0\oplus\mathrm{span}(h_1)$, with $\pi(h_1)=(p,q)\ne0$. For a coset $C'$ with functional $d'$, let $E_{d'}=\{w'':\langle h'',w''\rangle=d'(h)\ \forall h\in H_0\}$, a coset of a codimension-2 subspace of $\mathbb F_2^{2m-2}$. Then $C'$ consists of the points with $w''\in E_{d'}$ and $\langle h_1'',w''\rangle+pu+qv=d'(h_1)$.

*Sub-case $(p,q)=(1,0)$.* On $C_0$, $u=d_0(h_1)+\langle h_1'',w''\rangle$ and $v$ is free. So $D_v\Phi|_{C_0}=u+a$, and this must be constant on $E_{d_0}$.
- If $\alpha_m=0$, then $\langle h_1'',\cdot\rangle$ is constant on $E_{d_0}$. So $h_1''=h''$ for some $h\in H_0$, and $e_u=h_1+h\in H$: (X1) by Lemma 24(a).
- Otherwise $\Psi:=\alpha_m\cdot z$ is affine on $E_{d_0}$. Let $j^*=\max\mathrm{supp}\,\alpha_m$. Then $\Psi$ is the output of the formal $j^*$-gate circuit on $w_1,\dots,w_{2j^*}$ formed by gates $1..j^*$, and it depends on those coordinates only.
  - Let $H^*=\{h''\,:\,h\in H_0,\ \mathrm{supp}\,h''\subseteq[2j^*]\}$ and $K^*=(H^*)^\perp\subseteq\mathbb F_2^{2j^*}$.
  - The projection of $E_{d_0}$ to $\mathbb F_2^{2j^*}$ is a coset $E^*$ of $K^*$.
  - $\Psi|_{E^*}$ is affine: compose with an affine section of the projection, as in (IF′).
  - More generally, every coset of $K$ projects into a single coset of $K^*$, because each $h\in H$ with $h''\in H^*$ and $h_u=h_v=0$ fixes $\langle h'',w''\rangle$ on it.

  Now split on $\dim H^*$:
  - $\dim H^*=0$: $\Psi$ is affine on $\mathbb F_2^{2j^*}$, which contradicts the independence fact.
  - $\dim H^*=1$: Lemma 28 makes gate $j^*$ degenerate for $\ker h^*$, where $H^*=\{0,h^*\}$. Since $(h^*,0,0)\in H$, gate $j^*$ is degenerate for $K$: (X1).
  - $\dim H^*=2$: apply Lemma 30′ to $\Psi$ and $K^*$.
    - Alternative (i) gives a gate degenerate for $K^*$ whose degeneracy vector lies in $H^*$. Hence that vector, padded with zeros, lies in $H$, and the gate is degenerate for $K$: (X1).
    - Alternative (ii) gives $\Psi|_{C^*}\in\mathrm{span}(\text{affine},z_1,\dots,z_{j^*-1})|_{C^*}$, hence $z_{j^*}|_{C^*}\in\mathrm{span}(\text{affine},z_{<j^*})|_{C^*}$, on **every** coset $C^*$ of $K^*$. Pull this back along the affine projection $C\to C^*$, where $C^*$ is the coset containing the image of $C$. Then gate $j^*$ is redundant on $C$: (X3).

*Sub-case $(p,q)=(0,1)$* is symmetric, with $\beta_m$ and Lemma 24(b).

*Sub-case $(p,q)=(1,1)$.* On $C_0$, $v=u+e$ with $e=d_0(h_1)+\langle h_1'',w''\rangle$, and $u$ is free. Using $u^2=u$, $D_u\Phi|_{C_0}=1+a+b+e$, which is constant on $E_{d_0}$.
- If $\alpha_m=\beta_m$, then $e=D_u\Phi|_{C_0}+1$ is constant on $E_{d_0}$. As in sub-case $(1,0)$, $h_1''=h''$ for some $h\in H_0$, so $e_u+e_v=h_1+h\in H$: (X1) by Lemma 24(c).
- Otherwise run the same argument with $\Psi=(\alpha_m+\beta_m)\cdot z$.

### Case $\dim\pi(H)=2$
Then $H_0=\{0,h_0\}$ with $h_0=(t,0,0)$, $t\ne0$. Choose $h_1,h_2\in H$ with $\pi(h_1)=(1,0)$ and $\pi(h_2)=(0,1)$. A coset $C'$ is given by $(d'_0,d'_1,d'_2)=(d'(h_0),d'(h_1),d'(h_2))$. The map $C'\to E_{d'_0}:=\{\langle t,w''\rangle=d'_0\}$, $w\mapsto w''$, is an affine bijection, and on $C'$
$$u=d'_1+f,\quad v=d'_2+g,\qquad f=\langle h_1'',w''\rangle,\ g=\langle h_2'',w''\rangle,$$
$$\Phi|_{C'}\cong(P+d'_1)(Q+d'_2)+\Gamma\ \text{ on }E_{d'_0},\qquad P=f+a,\ Q=g+b .$$
Let $C_0\leftrightarrow(c_0,c_1,c_2)$ and $C\leftrightarrow(d_0,d_1,d_2)$.

**(a) Same class, $d_0=c_0$.** On the common $E_{c_0}$,
$$\Phi|_C-\Phi|_{C_0}=(c_1+d_1)Q+(c_2+d_2)P+c_1c_2+d_1d_2\in\mathrm{span}(\text{affine},z_{<m}).$$
So the last gate is redundant on $C$: (X3). This is Case II of Lemma 30.

**(b) Different classes, $d_0=c_0+1$.** Let $E=E_{c_0}$ and $E'=E_{c_0+1}$, let $k=\mathrm{top}(t)$, and take $e,\tau,s,\tilde A$ from (P1) for this $t$ and $c=c_0$. Since (X1) fails, $\tilde A$ is not constant on $E$ and (P2) applies.

Translating by $\tau$ identifies $E'$ with $E$. Every linear form $\ell$ becomes $\ell+\ell(\tau)$: the same form plus a constant. Hence, as functions on $E$,
$$\Phi|_C(w''+\tau)=(P^\tau+d_1)(Q^\tau+d_2)+\Gamma^\tau.$$
Here $X^\tau$ is computed on expressions (AUDIT-004 I-4). Each of $P$, $Q$, $\Gamma$ is read as a function on all of $\mathbb F_2^{2m-2}$, with linear forms taken on the whole $w''$-space, and is translated pointwise: $X^\tau(w''):=X(w''+\tau)$. So $z_j^\tau=z_j(\cdot+\tau)$, and each linear form $\ell$ becomes $\ell+\ell(\tau)$. Two expressions that agree on $E$ can have translates that differ, for example $\ell$ and $\ell+\langle t,\cdot\rangle+c$. That is why the translation is applied to the expressions. By (P1), $z_j^\tau=z_j$ for $j<k$ and $z_k^\tau=(\tilde A+1)s$. Put $F=(P+c_1)(Q+c_2)+\Gamma$, which is affine on $E$.

**(b1) $k=m-1$: the last two gates merge.**
- Let $y$ be the coordinate of $E$ inside $s$, and let $L_0=\mathrm{span}(1,\ \text{coordinates of }E\text{ other than }y,\ z_1,\dots,z_{m-2})$. Its elements do not involve $y$.
- With $s=y+B_0$, $B_0\in L_0$, and $\tilde A\in L_0$, the elements $P+c_1$, $Q+c_2$, $\Gamma$ take the forms
$$P+c_1=p+\mathsf u\,s,\quad Q+c_2=q+\mathsf v\,s,\quad\Gamma=\Gamma_0+\gamma_{m-1}\tilde A\,s,$$
with $p,q,\Gamma_0\in L_0$, $\mathsf u=f_y+\alpha_{m,m-1}\tilde A$, and $\mathsf v=g_y+\beta_{m,m-1}\tilde A$, where $f_y,g_y$ are the coefficients of $y$ in $f|_E$ and $g|_E$, written in the coordinates of $E$ after substituting for $w_e$ (AUDIT-004 I-2).
  - In types 1 and 2 this is the coefficient of $y$ in $f$.
  - In type 3 ($e=2m-2$, $y=w_{2m-3}$) it is $f_y=(h_1'')_{2m-3}+(h_1'')_{2m-2}$, and $g_y$ likewise with $h_2''$.
  - With the plain coefficient of $w_{2m-3}$ in $f$ instead, $p\notin L_0$ in general.
- Using $s^2=s$:
$$F=(pq+\Gamma_0)+\big(p\mathsf v+q\mathsf u+\mathsf u\mathsf v+\gamma_{m-1}\tilde A\big)\,s .$$
  $F$ is affine, say $F=\lambda_0+\lambda_y y$ with $\lambda_0$ affine and free of $y$, and $D_yF$ is constant. So $p\mathsf v+q\mathsf u+\mathsf u\mathsf v+\gamma_{m-1}\tilde A=\lambda_y$ is a constant. Substituting $s=y+B_0$ gives $pq+\Gamma_0=\lambda_0+\lambda_yB_0\in L_0$.
- On the translated side, $z_{m-1}^\tau=(\tilde A+1)s$ and $L_0$ is unchanged. So $P^\tau+d_1=p+\delta_1+\mathsf u's$ and $Q^\tau+d_2=q+\delta_2+\mathsf v's$, with constants $\delta_1,\delta_2$, $\mathsf u'=\mathsf u+\alpha_{m,m-1}$ and $\mathsf v'=\mathsf v+\beta_{m,m-1}$.
- So $\Phi|_C(w''+\tau)=R_0+R_1\,s$, with
$$R_0=(p+\delta_1)(q+\delta_2)+\Gamma_0=(pq+\Gamma_0)+\delta_2p+\delta_1q+\delta_1\delta_2\in L_0,$$
$$R_1=(p+\delta_1)\mathsf v'+(q+\delta_2)\mathsf u'+\mathsf u'\mathsf v'+\gamma_{m-1}(\tilde A+1)=\lambda_y+\beta_{m,m-1}p+\alpha_{m,m-1}q+(\delta_1+\alpha_{m,m-1})\mathsf v+(\delta_2+\beta_{m,m-1})\mathsf u+\text{const}\in L_0 .$$
  The last equality is a direct expansion. It uses the constancy of $p\mathsf v+q\mathsf u+\mathsf u\mathsf v+\gamma_{m-1}\tilde A$, and $\mathsf u,\mathsf v\in\mathrm{span}(1,\tilde A)\subseteq L_0$.
- **Circuit.** Gates $z_1,\dots,z_{m-2}$ are restricted to $C$ via the affine bijection $C\to E'\to E$. One more gate computes $R_1\cdot s$; both factors are affine combinations of computed values. The output is $R_0+R_1s$. That is $m-1$ gates.

**(b2) $k<m-1$: the last gate is redundant on $C$.**
- Gate $m-1$'s private variables $x=w_{2m-3}$ and $y=w_{2m-2}$ are coordinates of $E$, untouched by the substitution and by $\tau$. Let $X=A_{m-1}=x+\alpha_{m-1}\cdot z$ and $Y=B_{m-1}=y+\beta_{m-1}\cdot z$, so $z_{m-1}=XY$.
- Let $L_1=\mathrm{span}(1,\ \text{coordinates of }E\text{ other than }x,y,\ z_1,\dots,z_{m-2})$. For fixed values of the other coordinates, $(x,y)\mapsto(X,Y)$ is a bijection of $\mathbb F_2^2$. So every function on $E$ has a unique expansion $\sum_{S}F_SX^S$ over $S\subseteq\{X,Y\}$, with coefficients that are functions of the other coordinates.
- Write
$$P+c_1=p+\pi_xX+\pi_yY+\pi_zXY,\quad Q+c_2=q+\rho_xX+\rho_yY+\rho_zXY,\quad\Gamma=\Gamma_1+\gamma_{m-1}XY,$$
  with $p,q,\Gamma_1\in L_1$, $\pi_x=f_x$, $\pi_y=f_y$, $\pi_z=\alpha_{m,m-1}$ (and likewise for $\rho$). Concretely, $p=f_{\rm rest}+c_1+(\alpha_m|_{\le m-2}+f_x\alpha_{m-1}+f_y\beta_{m-1})\cdot z$, where $f_{\rm rest}$ is the linear form $f$ on $\mathbb F_2^{2m-2}$ with its $x,y$ terms removed. It is taken on the whole $w''$-space, not as its restriction to $E$, because it is translated later (AUDIT-004 I-4). $q$ is formed likewise.
- $F$ is affine. Writing the affine function as $\lambda_1+\lambda_xx+\lambda_yy$ and substituting $x=X+\alpha_{m-1}\cdot z$, $y=Y+\beta_{m-1}\cdot z$ shows: $F_{XY}=0$, and $F_X$, $F_Y$ are constants. From the product rule for multilinear expansions,
$$F_{XY}=\pi_z(\rho_z+\rho_x+\rho_y+q)+\pi_x(\rho_z+\rho_y)+\pi_y(\rho_z+\rho_x)+p\rho_z+\gamma_{m-1},$$
$$F_X=\pi_x\rho_x+\pi_xq+\rho_xp,\qquad F_Y=\pi_y\rho_y+\pi_yq+\rho_yp .$$

Cases:
- *(i) $\pi_z=\rho_z=0$.*
  - If $\gamma_{m-1}=0$, gate $m-1$ is unused: (X2), excluded.
  - Otherwise $F_{XY}=0$ gives $\pi_x\rho_y+\pi_y\rho_x=1$. The two conditions $F_X,F_Y\in\mathbb F_2$ form an invertible linear system in $(q,p)$, so $p$ and $q$ are constant on $E$.
- *(ii) $\pi_z=1,\rho_z=0$.* $F_{XY}=0$ makes $q$ constant.
  - If $\rho_x=\rho_y=0$, then $Q+c_2=q$ is constant on $E$. (P2) applied to $q=g_{\rm rest}+c_2+\beta_m|_{\le m-2}\cdot z$ gives $\beta_m=0$ and $g\in\{0,t\}$. So $e_v\in H$: (X1).
  - Otherwise $F_X$ or $F_Y$ makes $p$ constant.
- *(iii) $\pi_z=0,\rho_z=1$.* Symmetric.
- *(iv) $\pi_z=\rho_z=1$.* $F_{XY}=0$ gives $p+q=\kappa$, a constant. Then $F_X=(\pi_x+\rho_x)q+\text{const}$ and $F_Y=(\pi_y+\rho_y)q+\text{const}$.
  - If $(\pi_x,\pi_y)\ne(\rho_x,\rho_y)$, then $q$ and $p$ are constant.
  - Otherwise $(P+c_1)+(Q+c_2)=\kappa$ on $E$. By (P2), $\alpha_m=\beta_m$ and $f+g\in\{0,t\}$, so $e_u+e_v\in H$: (X1).

In every remaining case $p$ and $q$ are constant on $E$.
- By (P2), their $z$-coefficient vectors vanish, and their linear parts lie in $\{0,t\}$ plus constants.
- Hence $p^\tau$ and $q^\tau$ are again constants. On the translated side, $P^\tau+d_1$ and $Q^\tau+d_2$ are functions of $(X^\tau,Y^\tau)$ alone, where $z_{m-1}^\tau=X^\tau Y^\tau$.
- So the last gate of $\Phi|_C$ lies in $\mathrm{span}(1,X^\tau,Y^\tau,X^\tau Y^\tau)$, which is contained in $\mathrm{span}(\text{affine},z_{\le m-1})$: (X3).

This exhausts all cases. $\square$

## Corollaries

**Corollary 33 (every level).** PNE-001 holds for every non-constant $g$ with $\dim g\ge2\,\mathrm{MC}(g)-3$. Equivalently, a level-$m$ counterexample has $\dim g\le2m-4$.

*Proof.* As in Corollaries 29 and 31: $\dim g\le\dim K\le2m-1$. If $\dim g\ge2m-3$, then $K$ has codimension 1, 2 or 3. Lemma 28 (with 24), Lemma 30 or Lemma 32 then gives $\mathrm{MC}(g)=\mathrm{MC}(\Phi|_{C_1})\le m-1$. (For $m=1$ the codimension-3 case cannot occur. $\mathrm{MC}(g)=0$ is trivial.) $\square$

**Corollary 34 (level 4).** Theorem 25 holds with the following proof.
- By Lemma 23, a level-4 counterexample gives $(\Phi,K,C_0,C_1)$ with $\dim K\le7$.
- If $\dim K\le4$, then $\Phi|_{C_1}$ is a function of at most 4 variables, so its MC is $\le3$. This is the classical fact that every 4-variable function has MC $\le3$. Its sources:
  - Sönmez Turan–Peralta (literature, recalled);
  - EXP-001 (`bfs4.py`, cycle 001), which computes the exact MC of all 65,536 functions;
  - AUDIT-003 V-6, a verified circuit with at most 3 gates for each NIST class of dimension $\le4$;
  - AUDIT-004 V-9, an independent exhaustive span search.

  An earlier version cited AUDIT-002 V-2, which does not check this bound (AUDIT-004 I-1).
- If $\dim K\in\{5,6,7\}$, then $K$ has codimension 3, 2 or 1, and Lemmas 32, 30 and 28 exclude it.

Hence Theorem 25 needs no enumeration beyond the 4-variable fact. The earlier computations (EXP-014, EXP-015, AUDIT-003 V-3) are now independent confirmations of the codimension-3 step. $\square$

**Corollary 35 (level 5 reduces to six variables).** If $g$ is a level-5 counterexample, then $\dim g=6$. In Lemma 23 the subspace has $\dim K=6$, codimension 4 in $\mathbb F_2^{10}$.
- $\dim g\le6$ by Corollary 33.
- $\dim g\ge6$ because every function on $\le5$ variables has MC $\le4$ (Sönmez Turan–Peralta 2014; AUDIT-003 V-6).
- Similarly, $\dim K\ge\dim g=6$. And $\dim K\le6$, since codimensions 1–3 are excluded. $\square$

So the fresh-variable lemma at level 5 is equivalent to the following finite statement. *For every formal 5-gate circuit, every 6-dimensional $K\subseteq\mathbb F_2^{10}$ and every pair of cosets $C_0\ne C_1$ with $\Phi|_{C_0}$ affine, $\mathrm{MC}(\Phi|_{C_1})\le4$.* Equivalently: *no 6-variable $g$ with $\mathrm{MC}(g)=5$ has $\mathrm{MC}(y\,g)=5$.*

## Verification (EXP-018)

`EXP-018-codim3-hardcore/codim3.c` checks the *conclusion* of every case of the proof and counts violations (AUDIT-004 I-5).
- It uses the first affine coset as $C_0$.
- Its merge space contains $y$.
- It does not test (P1), (P2), the (b2) exits, the constancy of $p$ and $q$, or the exact $R_0$/$R_1$ formulas.

AUDIT-004's independent harness tests all of these on every pair $(C_0,C)$, with 0 violations. It ran over all 32,768 wirings and all subspaces at $m=4$, on about 52.6 million pairs at $m=5$, and on about 13.3 million at $m=6$. For each formal circuit, each codimension-3 $K$ and each non-affine coset $C$, where some coset $C_0$ is affine, it checks:
- (X1) via Lemma 24;
- the impossibility claims;
- gate $j^*$ redundant (case $\dim\pi=1$);
- last gate redundant (case 2a);
- $\Phi|_C\in V_0+s\cdot V_0$ with $V_0=\mathrm{span}(1,\text{coordinates},z_1..z_{m-2})|_C$ (case 2b1);
- gate $m-1$ unused, or last gate redundant (case 2b2).

| $m$ | wirings | subspaces | non-affine $C$ with affine $C_0$ | (X1) | $\dim\pi=1$: $j^*$ redundant | 2a: last redundant | 2b1: merge | 2b2: unused / last redundant | violations |
|---|---|---|---|---|---|---|---|---|---|
| 4 | all 8,640 | 97,155 | 24,282,232 | 18,787,840 | 561,600 | 2,167,708 | 1,690,160 | 1,012,800 / 62,124 | **0** |
| 5 | random 300 of 2,350,080 (seed 2026) | 6,347,715 | 1,839,901 | 1,762,553 | 5,279 | 34,026 | 21,530 | 15,649 / 864 | **0** |

Earlier data agrees with this picture:
- The "hard core" of cycle 002 (2,152,192 pairs with no redundant gate in the given circuit) lies exactly in cases 2b1 and (X2).
- In a random sample of 1,084 of them (`hc_sample.txt`), 770 have an unused gate and the other 314 have $\mathrm{top}(t)=m-1$.
- All 531 sampled pairs with $\mathrm{top}(t)=m-1$ satisfy the merge identity with the predicted input $s$ (`merge_check.py`).

## Novelty and limits
- The statements are about one restricted measure (MC) and say nothing about P vs NP.
- Novelty is unconfirmed. The 2016 NIST email (Peralta) claims the special case $\mathrm{MC}(uv\,f)=1+\mathrm{MC}(v\,f)$ with an unreleased attachment. We know of no published statement of these codimension results.
- Level 5 is now exactly the codimension-4 question at $m=5$ (Corollary 35). A human proof of codimension 4 for every $m$ would settle level 5 and give PNE-001 whenever $\dim g\ge2\,\mathrm{MC}(g)-4$. The codimension-3 proof suggests the shape of such an argument:
  - recursion through the sub-circuit $\Psi$ when $\dim\pi(H)=1$;
  - analysis of the top two gates when $\dim\pi(H)=2$.

  Two new phenomena must be handled. The sub-circuit $\Psi$ can itself be in the merge case 2b1, and in that case the merge does not transfer to $\Phi$ directly. And when $\dim\pi(H)=2$, $E$ becomes a codimension-2 subspace of $w''$-space.
