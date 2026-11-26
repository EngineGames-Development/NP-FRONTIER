# PNE-001 at level 5: reductions, a general perturbation lemma, and the codimension-4 residue

Cycle 003, 2026-11-26. Continues `PNE-001-codim3.md` (Lemma 32, Corollaries 33–35) and `PNE-001-level4.md`. Same notation.
Status: written by the chief researcher; not yet audited. Level 5 remains **open**.

**Where level 5 stands.** By Corollary 35, a level-5 counterexample ($\mathrm{MC}(g)=5=\mathrm{MC}(y\,g)$) has $\dim g=6$. In Lemma 23 this is codimension 4 in $\mathbb F_2^{10}$. This document proves two further results:
- **Lemma 36**, a necessary condition. Combined with NIST's classification, it leaves 35,861 of the 148,483 affine classes of 6-variable MC-5 functions as candidates.
- **Lemma 37**, a general "top-two perturbation" lemma. It re-proves the merge case of Lemma 32 and settles one of the two sub-cases that block a codimension-4 proof.

The other sub-case (NEW-2 below) is open. Every sampled instance of it has MC $\le4$.

## Lemma 36 (necessary conditions for a level-5 counterexample)

Let $g$ be non-constant with $\mathrm{MC}(g)=5=\mathrm{MC}(y\,g)$. Then:
- (a) $\dim g=6$;
- (b) $\deg g\le5$;
- (c) $g$ has a **cheap plane**: linearly independent $v_1,v_2$ such that for every nonzero $v\in\mathrm{span}(v_1,v_2)$ and each $c\in\mathbb F_2$, the half $g|_{\langle v,x\rangle=c}$ has MC $\le3$.

*Proof.*
- (a) is Corollary 35.
- (b) uses the degree bound $\mathrm{MC}(F)\ge\deg F-1$ (Schnorr's degree bound; recalled, not re-derived here). Since $\deg(y\,g)=\deg g+1$, $\deg g\ge6$ would force $\mathrm{MC}(y\,g)\ge6$.
- (c) is the argument of Lemma 20 one level up.
  - Take an optimal 5-gate circuit for $F=y\,g$ with first gate $a\cdot b$ of directions $u_1=(v_1,s_1)$ and $u_2=(v_2,s_2)$.
  - By Lemma 9′, $u_1$, $u_2$ and $u_1+u_2$ are admissible: both restrictions of $F$ have MC $\le4$.
  - $e_y$ is not admissible, because $F|_{y=1}=g$ has MC 5. So $v_1,v_2$ are linearly independent.
  - For admissible $(v,s)$ with $v\ne0$, the identity of Lemma 11 gives $\mathrm{MC}(t\cdot g|_{\langle v,x\rangle=c})\le4$ for both $c$, where $t$ is a fresh variable.
  - If the half is non-constant, it has MC $\le4$ (set $t=1$). PNE-001 at levels $\le4$ (Theorems 17 and 25) then gives $\mathrm{MC}(\text{half})+1\le4$. $\square$

All three conditions are invariant under affine equivalence: an affine change of input variables, plus the addition of an affine function. For (c), the halves transform into halves, and MC is unchanged by adding affine functions. So the conditions can be tested on class representatives.

Note on the reduction to representatives.
- In (c), directions outside $\mathrm{span}(\ell_1,\dots,\ell_6)$ are never cheap, because their halves have MC 5. Here $g=h(\ell_1,\dots,\ell_6)+\lambda$ with $\dim g=6$.
- So the condition passes to the 6-variable function $h$, and from $h$ to its NIST representative.

**Computation (EXP-019, `cheapplane6.c`).**
- Input: NIST's list of all affine classes of 6-variable functions with MC 5 (`github.com/usnistgov/circuits`, `data/mc_dim/mc5_dim6.txt`, 148,483 representatives, all of dimension 6).
- For each representative, every half is looked up in our exact table of the 5-variable set $S_3=\{\mathrm{MC}\le3\}$ (EXP-007). Self-test: MC(AND$_5$) = 4, MC($x_1x_2x_3x_4$) = 3, MC($x_1x_2+x_3x_4$) = 2.
- **Result: 35,861 representatives have a cheap plane** (287,734 cheap planes in total). The other 112,622 are excluded by (c).
- (b) excludes none of the survivors: their degrees are 3: 3, 4: 1,702, 5: 34,156.

So, **conditional on NIST's list** (complete and correctly labelled; the total of 150,357 classes in dimension $\le6$ matches the published count), a level-5 counterexample is affine-equivalent to $R+\ell$ for one of the 35,861 surviving representatives $R$ and a linear form $\ell$. The linear form matters because $y\cdot\ell$ is not affine. Deciding these $35{,}861\times64$ cases by SAT (7 variables, 5 gates) is beyond current resources; EXP-013 measured fixed-first-gate SAT at about 700 s per plane already at 5 variables. Sharper necessary conditions are needed.

## Lemma 37 (top-two perturbation) — any circuit, any domain

Let $S$ be an affine space, and let $\mathcal C$ be an $m$-gate XOR-AND circuit on $S$ ($m\ge2$):
- gate inputs $A_i,B_i$ are affine combinations of coordinates and earlier gates;
- the output is $\mathcal C=z_m+\Gamma$ with $\Gamma\in\mathrm{span}(\text{affine},z_{<m})$.

Let $\mathcal C'$ be obtained by adding constants $\varepsilon_1,\varepsilon_2$ to the inputs of gate $m-1$ and constants $\delta_1,\delta_2$ to the inputs of gate $m$. Gate $m$ and the output are recomputed from the perturbed $z_{m-1}$. **If $\mathcal C$ is affine on $S$, then $\mathrm{MC}(\mathcal C')\le m-1$.**

*Proof.* Let $L_0=\mathrm{span}(1,\text{coordinates},z_1,\dots,z_{m-2})$. Then $A_{m-1},B_{m-1}\in L_0$.
- The perturbed gate $m-1$ is $z'_{m-1}=z_{m-1}+W$ with $W=\varepsilon_2A_{m-1}+\varepsilon_1B_{m-1}+\varepsilon_1\varepsilon_2\in L_0$.
- Write $A_m=p+az_{m-1}$, $B_m=q+bz_{m-1}$ and $\Gamma=\Gamma_0+\gamma z_{m-1}$, with $p,q,\Gamma_0\in L_0$ and $a,b,\gamma\in\mathbb F_2$.
- Then $\mathcal C'=(A_m+aW+\delta_1)(B_m+bW+\delta_2)+\Gamma+\gamma W$. Expanding, the two terms $ab\,z_{m-1}W$ cancel, leaving
$$\mathcal C'=\mathcal C+W(bp+aq)+(a\delta_2+b\delta_1)\,z_{m-1}+\delta_2p+\delta_1q+(aW+\delta_1)(bW+\delta_2)+\gamma W .$$
- Since $\mathcal C$ is affine and $W^2=W$, this gives $\mathcal C'\in L_0+\kappa\,A_{m-1}B_{m-1}+W\cdot X$, with $X=bp+aq\in L_0$ and $\kappa=a\delta_2+b\delta_1$.
- Now $W$ is an affine combination of $A_{m-1}$ and $B_{m-1}$. So $\kappa A_{m-1}B_{m-1}+WX$ is a quadratic form, plus affine terms, in the three elements $A_{m-1},B_{m-1},X$ of $L_0$.
- Over $\mathbb F_2$, a quadratic form in three variables has symplectic rank $\le2$, so it equals $\ell_1\ell_2+(\text{affine})$ with $\ell_1,\ell_2$ affine in $A_{m-1},B_{m-1},X$ (Dickson normal form).
- Hence $\mathcal C'\in L_0+\ell_1\ell_2$, computed by $z_1,\dots,z_{m-2}$ and one more gate. $\square$

The identities used were checked by brute force over all values of the 10 parameters (`EXP-019/lemma37_check.py`).

**Consequences.**
- **A simpler proof of Lemma 32 (b1).** In case (b1), translating by $\tau$ changes only gate $m-1$'s input, by (P1). The coset change alters only the constants of gate $m$'s inputs. Both perturb only the top two gates, so Lemma 37 applies directly.
- **In general:** if $C_0$ is affine and the difference $C-C_0$ has a representative supported on the private coordinates of gates $m-1$ and $m$, then $\mathrm{MC}(\Phi|_C)\le m-1$, in every codimension.

## Codimension 4 at $m=5$: mechanisms and the residue (EXP-019)

`codim4.c` samples swap-reduced formal 5-gate circuits and takes all 53,743,987 codimension-4 subspaces of $\mathbb F_2^{10}$. Each non-affine coset $C$ with an affine $C_0$ is classified by the first mechanism that certifies $\mathrm{MC}\le4$:
- DEG: a Lemma-24-degenerate gate;
- UNUSED: an unused gate;
- RED: a triangularly redundant gate;
- MERGE: $\Phi|_C\in V_0+s\cdot V_0$, with $s$ an input of gate 4.

In a first sample of 4 wirings:
- 934,015 cosets: DEG 852,576; RED 23,695; MERGE 36,528.
- **HARD 21,216** (2.3%).

Structure of 600 sampled HARD instances (`hard_struct*.py`):
- All have $\dim\pi(H)=2$ and $\dim H_0=2$, with $C$ and $C_0$ in different $H_0$-classes.
- The non-separating element $t_2$ of $H_0''$ always has its top gate at gate $m-1$. So on the hyperplane $\{\langle t_2,\cdot\rangle=\text{const}\}$, which contains both cosets, gate $m-1$ loses a private variable. This is exactly what blocks the argument of Lemma 32 (b2).
- **NEW-1** (200 of 600): the separating elements also have their top gate at $m-1$. Gate $m-1$ is then fully determined on $C_0$, and the coset difference touches only gates $m-1$ and $m$. **Lemma 37 settles this sub-case.** All 200 satisfy the test TOP1, $\Phi|_C\in L_0+X\cdot L_0$ (`top1_check.py`).
- **NEW-2** (400 of 600): one separating element has its top gate $k_1<m-1$, so the perturbation touches a lower gate. None of the 400 satisfies TOP1, so these need circuits that rewire the gates between $k_1$ and $m-1$.
  - Example, decoded by hand (`decode1.py`): on $C_0$, $\Phi=w_2+w_6$. On $C$, $\Phi=s+w_3+(B_1+z_1)\,A_2\,(1+s)$, where $s=A_3$ is gate 3's free input.
  - Gates $z_0$ and $z_1$ are kept, and a shared product $\Pi=(B_1+z_1)A_2$ replaces gates 2–4: 4 gates. SAT confirms that MC is exactly 4.
- **No counterexample.** The 131 distinct HARD functions (modulo affine) of this sample all have verified 4-gate circuits (`hard_check.py`, SAT via `mc.py`, re-evaluated; at most 126 s per function).

## Lemma 38 (redundant products persist away from the separating gate)

Setting:
- (P1) and (P2) of `PNE-001-codim3.md` hold for a formal circuit with gates $1,\dots,j$.
- $t\ne0$, $k=\mathrm{top}(t)\le j$, $E=\{\langle t,\cdot\rangle=c\}$, and the translation $\tau$ of (P1). Gate $k$ is non-degenerate, i.e. $\tilde A$ is not constant on $E$.
- $L=\mathrm{span}(1,\text{linear forms},z_1,\dots,z_j)$.

Let $X,Y\in L$ with $XY\in L$ on $E$, and let $J$ be the largest gate index occurring in $X$ or $Y$ ($J=0$ if both are affine). **If $J\ne k$, then $(X^\tau+\delta_1)(Y^\tau+\delta_2)\in L^\tau$ on $E$ for all constants $\delta_1,\delta_2$.** Here $L^\tau=\mathrm{span}(1,\text{linear forms},z_i^\tau)$, with translates taken on expressions as in Lemma 32.

*Proof.* Write $XY=\Lambda+\sum_ic_iz_i$ on $E$, with $\Lambda$ affine, and let $I=\max(\{J\}\cup\mathrm{supp}\,c)$ be the top gate occurring anywhere in this relation.

(An earlier draft claimed $\mathrm{supp}\,c\subseteq[1,J]$. That is false. A product can duplicate a higher gate: if $X,Y$ are the two inputs of gate $i$, then $XY=z_i$ with $i>J$. The case analysis below uses $I$ instead.)
- **$I<k$.** Every gate in the relation is below $k$, so it is unchanged by $\tau$, and linear forms shift by constants. Hence, pointwise on $E$, $X^\tau Y^\tau=XY+\epsilon_YX+\epsilon_XY+\epsilon_X\epsilon_Y\in\mathrm{span}(\text{affine},z_i:i<k)\subseteq L^\tau$.
- **$I=k$.** Since $J\ne k$, this means $J<k$ and $c_k=1$. Again $X^\tau Y^\tau=XY+(\text{affine in }X,Y)$ pointwise on $E$. On $E$, $z_k=\tilde As_k=z_k^\tau+s_k$, and $s_k\in L^\tau$. So $X^\tau Y^\tau\in L^\tau$.
- **$I>k$.** Gate $I$ has both private variables free on $E$, and no gate above $I$ occurs. Run the top-gate analysis of Lemma 32 (b2) with gate $I$ in the role of gate $m-1$, with $X,Y$ in the role of $P+c_1,Q+c_2$, and with $\sum_ic_iz_i$ in the role of $\Gamma$.
  - Case (i) ($z_I$ occurs in neither $X$ nor $Y$, so $c_I=1$) forces the $s$-free parts $p,q$ to be constant. Then $X,Y\in\mathrm{span}(1,X_I,Y_I)$: the product duplicates gate $I$.
  - In cases (ii)–(iv), either $X$ or $Y$ is constant on $E$, or $X+Y$ is, or $p$ and $q$ are constant.
  - By (P2), applied to expressions in gates $<I$ with gate $k$ non-degenerate, each of these is a formal identity: zero gate coefficients, and linear part in $\{0,t\}$. So it survives the translation.
  - Hence $(X^\tau+\delta_1)(Y^\tau+\delta_2)$ is a function of $(X_I^\tau,Y_I^\tau)$ alone, or a multiple of an element of $L^\tau$, and lies in $\mathrm{span}(1,X_I^\tau,Y_I^\tau,z_I^\tau)+L^\tau=L^\tau$. $\square$

**Corollary 38a (NEW-2 reduces to a double merge).** Take the NEW-2 configuration at codimension 4:
- $t_2$ is non-separating with $\mathrm{top}(t_2)=m-1$;
- $t_1$ is separating with $k=\mathrm{top}(t_1)<m-1$.

On $E$, let $s$ be gate $m-1$'s free input, $\tilde Y$ its other input, and write $P+c_1=p+\mathsf u s$, $Q+c_2=q+\mathsf v s$, $X_1=bp+aq$, where $a,b$ are the coefficients of $z_{m-1}$ in the last gate's inputs. As in Lemma 32 (b1),
$$F=R_0+R_1s,\qquad R_0=pq+\Gamma_0,\qquad R_1=(\text{affine combination of }p,q,\tilde Y,1)+\tilde Y X_1 .$$
Affinity of $F$ forces $pq\in L_0$ and $\tilde YX_1\in L_0$ on $E$.

Lemma 38 applies to the sub-circuit of gates $1..m-2$. Restricted to its coordinates, $E$ and $E'$ are the two sides of the hyperplane $\{\langle t_1,\cdot\rangle=\text{const}\}$, and the translation acts as $e_{e_1}$. So, **if neither product has top gate $k$**:
- on the other coset $\Phi|_C\cong R_0'+R_1's'$ with $R_0',R_1'\in L_0^\tau$, where $s'$ is the translated free input of gate $m-1$;
- hence $\mathrm{MC}(\Phi|_C)\le(m-2)+1=m-1$.

The open sub-case is therefore the **merge at $k$**: at least one of $pq$, $\tilde YX_1$ has top gate exactly $k$. By the argument of Lemma 32 (b1), each such product lies in $L_{<k}+s_k\cdot L_{<k}$ on the other side, where $s_k$ is gate $k$'s free input.

**Data (`new2_check.py`).** In all 400 NEW-2 HARD instances of the 4-wiring sample, **both** products have top gate exactly $k$:
- $k=1$ (0-indexed), i.e. $k=m-3$: 200 instances;
- $k=2$ (0-indexed), i.e. $k=m-2$: 200 instances.

This matches Corollary 38a: no instance escapes it.

**The remaining question (double merge).** For $k=m-2$, write the two merged products with $s_k$-coefficients $N_0$ and $N_1$ in $L_{<k}$. Then
$$\Phi|_C=M_0+N_0s_k+(M_1+N_1s_k)\,s',\qquad M_i,N_i\in L_{<k}.$$
- In general this costs $k+2=m$ gates.
- If $N_0+N_1$ is constant, a single product $\Pi=N_1s_k$ serves both, and the cost is $k+1=m-1$. This is what happens in the decoded example: $N_0=N_1=B_1+z_1$.
- For $k=m-3$ the gates $k+1,\dots,m-2$ must also be accounted for.

A proof of codimension 4 must show that the constraints from $C_0$ force such sharing, or find another saving.

**Plan for the double merge (cycle 004; analysis so far, not yet a proof).** Take $k=m-2$. Every $X\in L_0$ decomposes as $X=X_0+(\xi+\eta_X\tilde A)s_k$ with $X_0\in L_{<k}$, where $\eta_X$ is the coefficient of $z_k$.

On the other side, the translation replaces $\tilde A$ by $\tilde A+1$ inside these coefficients and adds constants. Let $N_0,N_1$ be the $s_k$-coefficients of $R_0,R_1$, and $N_0',N_1'$ those of $R_0',R_1'$. The constraints from $C_0$ are:
- $R_1$ is constant on $E$, so $N_1=0$;
- $R_0\in L_0$, so $N_0\in\mathrm{span}(1,\tilde A)$.

A direct expansion then gives
$$N_0'\in\mathrm{span}(1,\tilde A,p_0,q_0),\qquad N_1'\in\mathrm{span}(1,\tilde A,\tilde Y_0,X_{1,0}).$$
Both are *linear* in elements of $L_{<k}$, which is why each product merges.

The saving needed is $N_0'+N_1'\in\mathrm{span}(1)$. That is a linear identity among $p_0,q_0,\tilde Y_0,\tilde A$, namely
$$p_0(\eta_q+b\eta_{\tilde Y})+q_0(\eta_p+a\eta_{\tilde Y})+\tilde Y_0(b\eta_p+a\eta_q)+c\,\tilde A\in\mathrm{span}(1).$$
It must follow from the constraints $N_1=0$ and $N_0\in\mathrm{span}(1,\tilde A)$.

Those constraints are quadratic: they involve products such as $\tilde A\cdot(\chi_1\tilde Y_0+\upsilon_1X_{1,0})$. They hold on the whole domain of gates $<k$, because $E$ does not constrain those coordinates.

So the next step is a **product-closure lemma on the full domain**. For a formal circuit, find all pairs $X,Y\in L$ with $XY\in L$. Expected answer: only trivial ones. Either $X$ or $Y$ is constant, or $X+Y$ is constant, or $X,Y\in\mathrm{span}(1,A_I,B_I)$ for some gate $I$ (a duplicate), applied recursively. The top-gate analysis of Lemma 32 (b2) with no hyperplane should prove it. The case $k<m-2$ must also account for gates $k+1,\dots,m-2$.

## Lemma 39 (product closure on the full domain)

Let $\Psi$ be a formal $j$-gate circuit on $\mathbb F_2^{2j}$, and let $L=\mathrm{span}(1,w_1,\dots,w_{2j},z_1,\dots,z_j)$. If $X,Y\in L$ and $XY\in L$ as functions on $\mathbb F_2^{2j}$, then:
- (a) $X$ or $Y$ is constant; or
- (b) $X+Y$ is constant; or
- (c) $X,Y\in\mathrm{span}(1,A_I,B_I,z_I)$, i.e. both are functions of gate $I$'s inputs, where $I$ is the largest gate index such that $z_I$, $w_{2I-1}$ or $w_{2I}$ occurs in $X$, $Y$ or in a representation $XY=\Lambda+\sum c_iz_i$.

*Proof.* If no gate and no private variable of any gate occurs, then $X$ and $Y$ are affine. Linearly independent affine forms have a non-affine product, so (a) or (b) holds.

Otherwise $I\ge1$, and gate $I$'s private variables are free and occur nowhere above. Expand in $(A_I,B_I)$ exactly as in Lemma 32 (b2), with $\Gamma=\sum c_iz_i$ and no hyperplane, so that independence holds on the whole space:
- $\pi_z=\rho_z=c_I=0$.
  - If $(\pi_x,\pi_y)=0$, then $F_X$ or $F_Y$ makes $p$ constant: (a).
  - If $(\pi_x,\pi_y)=(\rho_x,\rho_y)\ne0$, then $p+q$ is constant, so $X+Y$ is constant: (b).
- $\pi_z=\rho_z=0$, $c_I=1$: $p$ and $q$ are constant, which gives (c), the duplicate.
- (ii)/(iii): one input is constant (a), or $p,q$ are constant (c).
- (iv): $X+Y$ is constant (b), or $p,q$ are constant (c).

"Constant" here means identically constant on $\mathbb F_2^{2I}$, so it is a formal identity by the independence fact. $\square$

**Use.** In the double merge, the four constraints coming from $C_0$ are:
- $p_0q_0\in L_{<k}$;
- $\tilde Y_0X_{1,0}\in L_{<k}$;
- the two conditions on $N_0$ and $N_1$, which are of the form $\tilde A\cdot W\in L_{<k}$.

They involve only functions of gates $<k$. On $E$ these coordinates are free, so the constraints hold on the full domain of gates $<k$, and Lemma 39 classifies each of them. Because $\tilde A$ is non-constant, each $\tilde A\cdot W$ relation leaves: $W$ constant, $\tilde A+W$ constant, or $\tilde A,W$ both functions of one gate's inputs. The codimension-4 proof would finish by checking, case by case, that the saving $N_0'+N_1'\in\mathrm{span}(1)$ (or another saving) follows. This is finite and mechanical, but not yet done.

**Test of the plan (`dmerge_check.py`, the 200 sampled double-merge instances with $k=m-2$).** On $C$ write
$$\Phi|_C=M_0+N_0s_k+M_1s'+N_1s_ks'$$
with $M_i,N_i$ functions of the gates below $k$. These are computed as derivatives along directions that move only gate $k$'s, respectively gate $m-1$'s, free coordinate, and the decomposition is consistent in all 200 cases.

Any one of the following gives a 2-gate completion on top of the lower gates, hence MC $\le m-1$:
- $N_1$ constant;
- $M_1$ constant;
- $N_0$ constant;
- $N_0+N_1$ constant (the shared product).

Observed:
- $M_1$ constant: 49 instances;
- $N_0+N_1$ constant: 25;
- both of these: 11;
- $N_0$ constant: 10;
- $M_1$ and $N_0$ constant: 6;
- **none of the four: 99.**

All 200 nonetheless have MC $\le4$ by SAT. So about half the double merges need circuits that also restructure the gates below $k$. **Keeping the lower gates and merging above them is not enough, and the plan above is incomplete as it stands.** A full treatment of NEW-2 needs a further idea. One candidate is applying Lemma 39 to the lower gates themselves, which may let them be rewired as well.

**What a codimension-4 proof needs.** Lemmas 28, 30, 32 and 37 cover every configuration seen except NEW-2:
- $\dim\pi(H)=2$ and $\dim H_0=2$;
- $t_2$ eliminates a private variable of gate $m-1$;
- the separating $t_1$ has a lower top gate $k_1$.

In the decoded example, the two "slice" functions $R_0',R_1'$ in $\Phi|_C=R_0'+R_1's$ share a single product. A proof of NEW-2 would have to explain that sharing in general. The $\dim\pi(H)=1$ branch at codimension 4 also needs a written argument. Its recursion hits the merge and unused sub-cases of Lemma 32 for the sub-circuit $\Psi$; no HARD instance of this branch appeared in the sample.

## Status
- Level 5 of PNE-001 is **open**. No counterexample has been found.
- Proved here:
  - Lemmas 36, 37 and 38;
  - Lemma 32 (b1) as a corollary of Lemma 37;
  - the NEW-1 sub-case of codimension 4;
  - the reduction of NEW-2 to the double-merge sub-case (Corollary 38a).
- Computed, conditional on NIST: 35,861 candidate classes remain. Sampled: the codimension-4 residue NEW-2, with every sampled case of MC $\le4$.
- Nothing here bears on P vs NP.
