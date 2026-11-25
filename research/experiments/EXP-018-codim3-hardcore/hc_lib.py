"""EXP-018 helpers: formal 4-gate circuits on F_2^8 (gate i reads bits 2i, 2i+1; i = 0..3), cosets, restrictions.
Wiring convention of formal4.c: al = (0, a1, a2, a3), be = (0, b1, b2, b3) as bitmasks over earlier gates, gm = output mask."""
import itertools

def parse(line):
    t = line.split()
    assert t[0] == 'HC'
    a1, a2, a3, b1, b2, b3, gm = map(int, t[1:8])
    basis = list(map(int, t[8:13]))
    c0, c1 = int(t[13]), int(t[14])
    tab = int(t[15], 16)
    return dict(al=[0, a1, a2, a3], be=[0, b1, b2, b3], gm=gm, basis=basis, c0=c0, c1=c1, tab=tab)

def gates(p, al, be):
    """values (z0..z3) at point p in [0,256)"""
    z = []
    for i in range(4):
        A = (p >> (2 * i)) & 1; B = (p >> (2 * i + 1)) & 1
        for j in range(i):
            if (al[i] >> j) & 1: A ^= z[j]
            if (be[i] >> j) & 1: B ^= z[j]
        z.append(A & B)
    return z

def gate_inputs(p, al, be):
    z = []; ins = []
    for i in range(4):
        A = (p >> (2 * i)) & 1; B = (p >> (2 * i + 1)) & 1
        for j in range(i):
            if (al[i] >> j) & 1: A ^= z[j]
            if (be[i] >> j) & 1: B ^= z[j]
        ins.append((A, B)); z.append(A & B)
    return z, ins

def phi(p, al, be, gm):
    z = gates(p, al, be)
    v = z[3]
    for j in range(3):
        if (gm >> j) & 1: v ^= z[j]
    return v

def coset_points(c, basis):
    k = len(basis)
    pts = []
    for t in range(1 << k):
        q = c
        for r in range(k):
            if (t >> r) & 1: q ^= basis[r]
        pts.append(q)
    return pts

def dual(basis):
    return [h for h in range(1, 256) if all(bin(h & b).count('1') % 2 == 0 for b in basis)]

def par(x): return bin(x).count('1') & 1

def anf(tab, k):
    a = list((tab >> t) & 1 for t in range(1 << k))
    for i in range(k):
        for t in range(1 << k):
            if (t >> i) & 1: a[t] ^= a[t ^ (1 << i)]
    return a

def degree(tab, k):
    a = anf(tab, k)
    return max([bin(t).count('1') for t in range(1 << k) if a[t]] or [-1])
