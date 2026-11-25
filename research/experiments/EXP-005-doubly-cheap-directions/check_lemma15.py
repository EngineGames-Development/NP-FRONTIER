"""Sanity check of Lemma 15: for MC-3 functions g with >= 2 cheap directions v1, v2, every quarter
g|{<v1,x>=a, <v2,x>=b} must be affine (all second derivatives within the quarter vanish)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "EXP-002-restriction-depth"))
import dpdt
mc4 = json.load(open(os.path.join(HERE, "..", "EXP-001-mc-exact", "mc4.json")))["mc"]
L5 = dpdt.hyperplane_index_lists(5)
dot = lambda v, x: bin(v & x).count("1") & 1
def cheap(g): return [v for v, (l0, l1) in zip(range(1, 32), L5) if mc4[dpdt.restrict(g, l0)] <= 1 and mc4[dpdt.restrict(g, l1)] <= 1]
def quarter_affine(g, v1, v2, a, b):
    pts = [x for x in range(32) if dot(v1, x) == a and dot(v2, x) == b]
    lin = [p ^ pts[0] for p in pts]                       # the 3-dim linear part of the quarter
    f = lambda x: (g >> x) & 1
    return all(f(x) ^ f(x ^ u) ^ f(x ^ w) ^ f(x ^ u ^ w) == 0 for x in pts for u in lin for w in lin)
fns = ['0x6e890b2', '0x10dce02c', '0x1383e575', '0x8130e859', '0xddfc6a78', '0xec974362', '0xecf49415',
       '0x47242117', '0xae234098', '0xa4620b32', '0x47fca912', '0x1cce499b']
ok = 0
for h in fns:
    g = int(h, 16); A = cheap(g); v1, v2 = A[0], A[1]
    res = all(quarter_affine(g, v1, v2, a, b) for a in (0, 1) for b in (0, 1))
    ok += res; print(h, "cheap directions", A, "-> all four quarters affine:", res)
print(f"{ok}/{len(fns)} consistent with Lemma 15")
