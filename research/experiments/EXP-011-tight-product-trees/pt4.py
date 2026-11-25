"""EXP-011: is every degree-tight function (MC = deg - 1) a product tree plus an affine function?
P_1 = affine functions; P_k = {P*Q + lam : P in P_k1, Q in P_k2, k1+k2 = k, lam affine} restricted to degree exactly k.
Claim to test on 4 variables: P_k = {f : deg f = k and MC f = k-1} for k = 2, 3, 4."""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-001-mc-exact"))
from mc import degree
n = 4; N = 1 << n; ONE = (1 << N) - 1
X = [sum(1 << p for p in range(N) if p >> j & 1) for j in range(n)]
aff = {0}
for v in [ONE] + X: aff |= {a ^ v for a in aff}
aff = sorted(aff)
mc4 = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-001-mc-exact", "mc4.json")))["mc"]
deg = [degree(f, n) for f in range(1 << N)]
P = {1: set(aff)}
for k in range(2, n + 1):
    prods = set()
    for k1 in range(1, k // 2 + 1):
        k2 = k - k1
        for a in P[k1]:
            for b in P[k2]:
                prods.add(a & b)
    Pk = {p ^ l for p in prods for l in aff if deg[p ^ l] == k}
    P[k] = Pk
    tight = {f for f in range(1 << N) if deg[f] == k and mc4[f] == k - 1}
    print(f"k={k}: |P_k| = {len(Pk)}, |tight of degree k| = {len(tight)}, equal: {Pk == tight}", flush=True)
