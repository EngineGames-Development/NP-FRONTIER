"""Computational check of Lemma 18 on 5 variables (independent of the circuit enumeration).
Prediction: S_2 = {deg <= 2} ∪ {f : for some direction v and c, f|<v,x>=c is affine and MC(f|<v,x>=1+c) <= 1}.
On 5 variables every quadratic form has rank <= 4, so type (Q) is exactly degree <= 2."""
import json, os, sys, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "EXP-002-restriction-depth"))
import dpdt
mc4 = json.load(open(os.path.join(HERE, "..", "EXP-001-mc-exact", "mc4.json")))["mc"]
S2 = np.load(os.path.join(HERE, "..", "EXP-006-level3-finite-check", "S2_5vars.npy"))
# degree <= 2 functions on 5 vars: span of monomials of size <= 2
mons = [sum(1 << p for p in range(32) if (p & m) == m) for m in range(32) if bin(m).count("1") <= 2]
Q = {0}
for mtt in mons: Q |= {v ^ mtt for v in Q}
aff4 = [f for f in range(1 << 16) if mc4[f] == 0]; mc1_4 = [f for f in range(1 << 16) if mc4[f] <= 1]
C = set()
for (l0, l1) in dpdt.hyperplane_index_lists(5):
    for lo, hi in ((l0, l1), (l1, l0)):          # affine half on 'lo', MC<=1 half on 'hi'
        for a in aff4:
            base = 0
            for u, p in enumerate(lo):
                if (a >> u) & 1: base |= 1 << p
            for q in mc1_4:
                f = base
                for u, p in enumerate(hi):
                    if (q >> u) & 1: f |= 1 << p
                C.add(f)
pred = Q | C
s2 = set(int(x) for x in S2)
print(f"|deg<=2| = {len(Q)}, |type C| = {len(C)}, |prediction| = {len(pred)}, |S_2| = {len(s2)}, equal: {pred == s2}")
