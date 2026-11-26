import sys, os
sys.path.insert(0, os.path.join("..", "EXP-001-mc-exact"))
from mc import mc_le, evaluate
# instance: HARD 0 1 1 5 1 3 6 8 11  132 392 48 960  c0 7 c 11
al = [0, 0, 1, 1, 5]; be = [0, 1, 3, 6, 8]; gm = 11
def circuit(w):
    z = []
    for i in range(5):
        A = w[2*i]; B = w[2*i+1]
        for j in range(i):
            if (al[i] >> j) & 1: A ^= z[j]
            if (be[i] >> j) & 1: B ^= z[j]
        z.append(A & B)
    out = z[4]
    for j in range(4):
        if (gm >> j) & 1: out ^= z[j]
    return out, z
def coset_fn(d1, d3, d_tb):
    # free coords w0,w1,w2,w3,w4,w6 ; t_a: w7 = w2+1 ; t_b: w5 = w4 + d_tb ; h1: w8 = d1 + w3 + w7 ; h3: w9 = d3 + w6 + w7 + w8
    tab = 0
    for x in range(64):
        w0, w1, w2, w3, w4, w6 = [(x >> i) & 1 for i in range(6)]
        w7 = w2 ^ 1; w5 = w4 ^ d_tb; w8 = d1 ^ w3 ^ w7; w9 = d3 ^ w6 ^ w7 ^ w8
        w = [w0, w1, w2, w3, w4, w5, w6, w7, w8, w9]
        if circuit(w)[0]: tab |= 1 << x
    return tab
def anf(t, n=6):
    a = [(t >> i) & 1 for i in range(1 << n)]
    for i in range(n):
        for x in range(1 << n):
            if (x >> i) & 1: a[x] ^= a[x ^ (1 << i)]
    names = ['w0', 'w1', 'w2', 'w3', 'w4', 'w6']
    mons = [''.join(names[i] for i in range(n) if (x >> i) & 1) or '1' for x in range(1 << n) if a[x]]
    return ' + '.join(mons)
t0 = coset_fn(1, 0, 1); t1 = coset_fn(1, 1, 0)
print("C0:", anf(t0)); print("C :", anf(t1))
c = mc_le(t1, 6, 4); print("4-gate circuit for Phi|C:", c, "verified:", c is not None and evaluate(c, 6) == t1)
c3 = mc_le(t1, 6, 3); print("3-gate circuit:", c3)
