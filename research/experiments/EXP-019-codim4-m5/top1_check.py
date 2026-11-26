"""EXP-019: on each HARD codimension-4 instance, test TOP1: Phi|C in L0 + X*L0 for some X in L0,
where L0 = span(1, coordinates of C, z_0, z_1, z_2 restricted to C) (the first m-2 = 3 original gates).
TOP1 gives MC(Phi|C) <= 4 with the first three gates kept and one new gate."""
import sys
from collections import Counter
def parse(line):
    t = line.split()
    al = [0] + list(map(int, t[1:5])); be = [0] + list(map(int, t[5:9])); gm = int(t[9])
    h = list(map(int, t[10:14])); c0 = int(t[15]); c = int(t[17]); tab = int(t[19], 16)
    return al, be, gm, h, c0, c, tab
def gates(w, al, be):
    z = []; ins = []
    for i in range(5):
        A = (w >> (2*i)) & 1; B = (w >> (2*i+1)) & 1
        for j in range(i):
            if (al[i] >> j) & 1: A ^= z[j]
            if (be[i] >> j) & 1: B ^= z[j]
        ins.append((A, B)); z.append(A & B)
    return z, ins
def coset_pts(h, cc):
    P = [(x & -x).bit_length() - 1 for x in h]
    free = [q for q in range(10) if q not in P]
    pts = []
    for t in range(64):
        x = 0
        for r, q in enumerate(free):
            if (t >> r) & 1: x |= 1 << q
        for i in range(4):
            par = (bin((h[i] & ~(1 << P[i])) & x).count('1') & 1) ^ ((cc >> i) & 1)
            if par: x |= 1 << P[i]
        pts.append(x)
    return pts
def reduce_basis(vecs):
    rows = []
    for v in vecs:
        for r in rows:
            if v ^ r < v: v ^= r
        if v:
            rows.append(v); rows.sort(reverse=True)
            # keep fully reduced-ish: fine for membership with re-reduction
    return rows
def in_span(rows, v):
    for r in sorted(rows, reverse=True):
        if v ^ r < v: v ^= r
    return v == 0
def span_elems(basis):
    S = [0]
    for b in basis: S += [x ^ b for x in S]
    return S
stats = Counter(); out = []
for line in open(sys.argv[1]):
    if not line.startswith('HARD'): continue
    al, be, gm, h, c0, c, tab = parse(line)
    pts = coset_pts(h, c)
    Z = [[0]*5 for _ in range(1)]
    zt = [0]*5; At = [0]*5; Bt = [0]*5; ph = 0
    for t, p in enumerate(pts):
        z, ins = gates(p, al, be)
        for i in range(5):
            if z[i]: zt[i] |= 1 << t
            if ins[i][0]: At[i] |= 1 << t
            if ins[i][1]: Bt[i] |= 1 << t
        v = z[4]
        for j in range(4):
            if (gm >> j) & 1: v ^= z[j]
        if v: ph |= 1 << t
    assert ph == tab, "table mismatch"
    ONE = (1 << 64) - 1
    coords = [sum(1 << t for t in range(64) if (t >> r) & 1) for r in range(6)]
    L0 = reduce_basis([ONE] + coords + zt[:3])
    L0el = span_elems(L0)
    ok = False
    for X in L0el:
        if X == 0: continue
        rows = reduce_basis(L0 + [X & b for b in L0])
        if in_span(rows, ph): ok = True; break
    stats['TOP1' if ok else 'not TOP1'] += 1
print(dict(stats))
