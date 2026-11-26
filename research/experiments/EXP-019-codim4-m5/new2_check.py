"""EXP-019: test the reduction of NEW-2 (PNE-001-level5.md, Lemma 38 and its corollary) on HARD instances.
On C0 (~ E), write P = p + u*s, Q = q + v*s (s = free input of gate 3, 0-indexed), Ytilde = the eliminated input of
gate 3, X1 = b*p + a*q (a, b = coefficients of z_3 in the last gate's inputs). Express p, q, Ytilde, X1 in the
basis {1, coordinates, z_0, z_1, z_2} of L restricted to C0 and read off the top gate used. Prediction: every HARD
NEW-2 instance has J0 = top(p,q) = k or J1 = top(Ytilde, X1) = k, where k = top gate of the separating t1."""
import sys
from collections import Counter
def parse(line):
    t = line.split()
    al = [0] + list(map(int, t[1:5])); be = [0] + list(map(int, t[5:9])); gm = int(t[9])
    h = list(map(int, t[10:14])); c0 = int(t[15]); c = int(t[17])
    return al, be, gm, h, c0, c
def span(vs):
    S = {0}
    for v in vs: S |= {x ^ v for x in S}
    return S
def top(x): return max(i for i in range(5) if (x >> (2*i)) & 3)
def evalc(w, al, be):
    z = []; ins = []
    for i in range(5):
        A = (w >> (2*i)) & 1; B = (w >> (2*i+1)) & 1
        for j in range(i):
            if (al[i] >> j) & 1: A ^= z[j]
            if (be[i] >> j) & 1: B ^= z[j]
        ins.append((A, B)); z.append(A & B)
    return z, ins
def coset(h, cc):
    P = [(x & -x).bit_length() - 1 for x in h]; free = [q for q in range(10) if q not in P]; pts = []
    for t in range(64):
        x = 0
        for r, q in enumerate(free):
            if (t >> r) & 1: x |= 1 << q
        for i in range(4):
            if (bin((h[i] & ~(1 << P[i])) & x).count('1') & 1) ^ ((cc >> i) & 1): x |= 1 << P[i]
        pts.append(x)
    return pts
def coeffs(target, basis):
    """solve target = sum c_i basis_i over GF(2) (64-bit vectors); return list of c_i or None"""
    n = len(basis); rows = [(basis[i], 1 << i) for i in range(n)]
    piv = []
    for v, tag in rows:
        for pv, ptag in piv:
            if v ^ pv < v: v ^= pv; tag ^= ptag
        if v: piv.append((v, tag)); piv.sort(reverse=True)
    t = target; tag = 0
    for pv, ptag in sorted(piv, reverse=True):
        if t ^ pv < t: t ^= pv; tag ^= ptag
    if t: return None
    return [(tag >> i) & 1 for i in range(n)]
C = Counter(); bad = []
for line in open(sys.argv[1]):
    if not line.startswith('HARD'): continue
    al, be, gm, h, c0, c = parse(line)
    H = span(h); H0 = [x for x in H if x and (x >> 8) & 3 == 0]
    Pv = [(x & -x).bit_length() - 1 for x in h]; off = lambda cc: sum(1 << Pv[i] for i in range(4) if (cc >> i) & 1)
    dlt = off(c0) ^ off(c)
    sep = [x for x in H0 if bin(x & dlt).count('1') % 2]; non = [x for x in H0 if x not in sep]
    t2 = non[0]
    if top(t2) != 3: continue
    low = [x for x in sep if top(x) < 3]
    if not low: C['NEW-1'] += 1; continue
    t1 = low[0]; k = top(t1)
    typ2 = (t2 >> 6) & 3          # 1: bit 6 (A of gate 3) eliminated, 2: bit 7 (B) eliminated, 3: both bits
    pts = coset(h, c0)
    vals = [evalc(w, al, be) for w in pts]
    def vec(fn): return sum(1 << i for i, (z, ins) in enumerate(vals) if fn(z, ins))
    A3 = vec(lambda z, ins: ins[3][0]); B3 = vec(lambda z, ins: ins[3][1])
    if typ2 == 1: s, Yt = B3, A3
    elif typ2 == 2: s, Yt = A3, B3
    else: s, Yt = A3, (A3 ^ B3 ^ ((1 << 64) - 1))
    Pf = vec(lambda z, ins: ins[4][0]); Qf = vec(lambda z, ins: ins[4][1])
    # kappa: direction changing only y within E2 (and u, v as forced)
    y = 6 if typ2 in (2, 3) else 7
    e2 = 7 if typ2 in (2, 3) else 6
    kap = (1 << y) | (((t2 >> y) & 1) << e2)
    # u, v components: choose so that <h,kap> = 0 for all h in H (solve over the two bits 8, 9)
    for uv in range(4):
        kk = kap | (uv << 8)
        if all(bin(x & kk).count('1') % 2 == 0 for x in H): kap = kk; break
    else:
        C['kappa-fail'] += 1; continue
    idx = {w: i for i, w in enumerate(pts)}
    def s_free_part(F):   # F = f0 + f1*s with f0, f1 kappa-invariant: f0(w) = F at the s=0 member of {w, w+kappa}
        out = 0
        for i, w in enumerate(pts):
            j = i if not (s >> i) & 1 else idx[w ^ kap]
            if (F >> j) & 1: out |= 1 << i
        return out
    p = s_free_part(Pf); q = s_free_part(Qf)
    ONE = (1 << 64) - 1
    coords = [sum(1 << t for t in range(64) if (t >> r) & 1) for r in range(6)]
    zr = [vec(lambda z, ins, i=i: z[i]) for i in range(3)]
    basis = [ONE] + coords + zr
    a = (al[4] >> 3) & 1; b = (be[4] >> 3) & 1
    X1 = (p if b else 0) ^ (q if a else 0)
    def topg(F):
        cs = coeffs(F, basis)
        if cs is None: return 'notinL'
        g = [i for i in range(3) if cs[7 + i]]
        return max(g) if g else -1
    J0 = max([topg(p), topg(q)], key=lambda x: -2 if x == 'notinL' else x)
    J1 = max([topg(Yt), topg(X1)], key=lambda x: -2 if x == 'notinL' else x) if (a or b) else 'none'
    pred = (J0 == k) or (J1 == k)
    C[('NEW-2', 'k=%d' % k, 'J0=%s' % J0, 'J1=%s' % J1, 'pred-ok' if pred else 'PRED-FAILS')] += 1
for x, v in sorted(C.items(), key=lambda kv: -kv[1]): print(v, x)
