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

**What a codimension-4 proof needs.** Lemmas 28, 30, 32 and 37 cover every configuration seen except NEW-2:
- $\dim\pi(H)=2$ and $\dim H_0=2$;
- $t_2$ eliminates a private variable of gate $m-1$;
- the separating $t_1$ has a lower top gate $k_1$.

In the decoded example, the two "slice" functions $R_0',R_1'$ in $\Phi|_C=R_0'+R_1's$ share a single product. A proof of NEW-2 would have to explain that sharing in general. The $\dim\pi(H)=1$ branch at codimension 4 also needs a written argument. Its recursion hits the merge and unused sub-cases of Lemma 32 for the sub-circuit $\Psi$; no HARD instance of this branch appeared in the sample.

## Status
- Level 5 of PNE-001 is **open**. No counterexample has been found.
- Proved here: Lemma 36; Lemma 37; Lemma 32 (b1) as a corollary of Lemma 37; the NEW-1 sub-case of codimension 4.
- Computed, conditional on NIST: 35,861 candidate classes remain. Sampled: the codimension-4 residue NEW-2, with every sampled case of MC $\le4$.
- Nothing here bears on P vs NP.
