"""D(f): value of the affine restriction game = min depth of a parity decision tree whose leaves are affine.

D(f) = 0 if deg f <= 1, else 1 + min over nonzero linear v of max over c in {0,1} of D(f restricted to {<v,x> = c}).
D is invariant under affine changes of coordinates, so each hyperplane is identified with F_2^(n-1) via any basis.
Theorem (research/proofs/PNE-001): D(f) <= MC(f) for every f.
"""
import functools, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "EXP-001-mc-exact"))
from mc import degree

@functools.lru_cache(maxsize=None)
def hyperplane_index_lists(n):
    """For each nonzero v: (points with <v,x>=0, points with <v,x>=1), each ordered by coordinates u in F_2^(n-1)."""
    out = []
    for v in range(1, 1 << n):
        piv = v.bit_length() - 1                       # a coordinate where v is 1
        basis = []                                     # basis of ker(v): e_j (j != piv), corrected at piv
        for j in range(n):
            if j == piv: continue
            e = 1 << j
            if (bin(v & e).count("1") & 1): e |= 1 << piv
            basis.append(e)
        lists = []
        for c in (0, 1):
            p0 = (1 << piv) if c else 0
            pts = []
            for u in range(1 << (n - 1)):
                p = p0
                for i, b in enumerate(basis):
                    if u >> i & 1: p ^= b
                pts.append(p)
            lists.append(tuple(pts))
        out.append(tuple(lists))
    return tuple(out)

def restrict(F, pts):
    return sum(((F >> p) & 1) << u for u, p in enumerate(pts))

_tables = {}
def D(F, n):
    if n <= 4 and n in _tables: return _tables[n][F]
    if degree(F, n) <= 1: return 0
    best = None
    for l0, l1 in hyperplane_index_lists(n):
        m = max(D(restrict(F, l0), n - 1), D(restrict(F, l1), n - 1))
        if best is None or m < best: best = m
        if best == 0: break
    return 1 + best

def build_table(n):
    _tables[n] = [D(F, n) for F in range(1 << (1 << n))]

if __name__ == "__main__":
    for n in range(1, 5):
        build_table(n); print(f"n={n}: table built", flush=True)
    mc4 = json.load(open(os.path.join(os.path.dirname(__file__), "..", "EXP-001-mc-exact", "mc4.json")))["mc"]
    from collections import Counter
    pairs = Counter((mc4[F], _tables[4][F]) for F in range(1 << 16))
    print("(MC, D) counts over all 4-variable functions:", sorted(pairs.items()))
    print("MC == D for all 4-variable functions:", all(mc4[F] == _tables[4][F] for F in range(1 << 16)))
    json.dump({"D4": _tables[4]}, open("D4.json", "w"))
