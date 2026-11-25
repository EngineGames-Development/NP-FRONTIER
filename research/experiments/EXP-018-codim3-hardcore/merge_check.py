"""EXP-018: test the 'merge' claim of the codimension-3 proof on sampled hard-core pairs (m = 4).
Claim: if dim pi(H) = 2, C0 and C1 lie in different H0-classes, and the top gate k of h0'' is gate m-1 (0-indexed 2),
then Phi|C1 lies in V + s*V, where V = span(1, coordinates, z_1..z_{m-2} restricted to C1) and s is the input of gate
m-1 that keeps its private variable on C1 (A for type 2, B for type 1, either for type 3)."""
import sys; sys.path.insert(0, '.')
from hc_lib import *

def rank_insert(rows, v):
    for r in rows:
        if v ^ r < v: v ^= r
    if v:
        rows.append(v); rows.sort(reverse=True)
        return True
    return False

def in_span(vecs, target):
    rows = []
    for v in vecs: rank_insert(rows, v)
    t = target
    for r in sorted(rows, reverse=True):
        if t ^ r < t: t ^= r
    return t == 0

def check(d):
    al, be, gm = d['al'], d['be'], d['gm']
    pts = coset_points(d['c1'], d['basis'])
    n = len(pts)
    def vec(fn):
        v = 0
        for t, p in enumerate(pts):
            if fn(p): v |= 1 << t
        return v
    zs = [vec(lambda p, i=i: gates(p, al, be)[i]) for i in range(4)]
    A2 = vec(lambda p: gate_inputs(p, al, be)[1][2][0]); B2 = vec(lambda p: gate_inputs(p, al, be)[1][2][1])
    ph = vec(lambda p: phi(p, al, be, gm))
    coords = [sum(1 << t for t in range(n) if (t >> r) & 1) for r in range(len(d['basis']))]
    V = [(1 << n) - 1] + coords + zs[:2]
    res = {}
    for name, s in (('A', A2), ('B', B2)):
        res[name] = in_span(V + [v & s for v in V], ph)
    H = dual(d['basis']); h0 = [h for h in H if (h >> 6) & 3 == 0][0]
    k = max(i for i in range(3) if (h0 >> (2 * i)) & 3); typ = (h0 >> (2 * k)) & 3
    return k, typ, res

if __name__ == '__main__':
    S = [parse(l) for l in open(sys.argv[1] if len(sys.argv) > 1 else 'hc_sample.txt')]
    from collections import Counter
    C = Counter()
    for d in S:
        k, typ, res = check(d)
        if k != 2: continue
        pred = {1: res['B'], 2: res['A'], 3: res['A'] and res['B']}[typ]
        C[(typ, pred, res['A'], res['B'])] += 1
    for x, c in sorted(C.items()): print("type %d  predicted-s works: %s  (A: %s, B: %s): %d" % (x[0], x[1], x[2], x[3], c))
