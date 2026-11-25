"""Positive controls for cert4 in the tight regime: random 6-variable product trees with 5 leaves whose linear
parts are independent (degree 5, so MC >= 4), built with 4 AND gates (MC <= 4): every one must give FOUND.
Also y*g for random 5-variable g with MC 3 and degree 4 (MC(y*g) = 4 by Theorem 17)."""
import random, struct, sys
sys.path.insert(0, "../EXP-001-mc-exact")
from mc import degree
r = random.Random(2026)
N = 64; ONE = (1 << N) - 1; X = [sum(1 << p for p in range(N) if p >> j & 1) for j in range(6)]
def lin(v): t = 0; [t := t ^ X[j] for j in range(6) if v >> j & 1]; return t
def aff(): return lin(r.randrange(64)) ^ (ONE if r.randrange(2) else 0)
def rank(vs):
    rows = []
    for v in vs:
        for b in rows: v = min(v, v ^ b)
        if v: rows.append(v)
    return len(rows)
out = []
while len(out) < 12:
    leaves = [r.randrange(1, 64) for _ in range(5)]
    if rank(leaves) < 5: continue
    L = [lin(v) ^ (ONE if r.randrange(2) else 0) for v in leaves]
    shape = r.choice(["chain", "2+3", "1+(2+2)", "(1+1)+(1+2)"])
    if shape == "chain": t = L[0]; [t := (t ^ aff()) & (l ^ aff()) for l in L[1:]]
    elif shape == "2+3": t = ((L[0] & L[1]) ^ aff()) & ((((L[2] & L[3]) ^ aff()) & L[4]) ^ aff())
    elif shape == "1+(2+2)": t = (L[0] ^ aff()) & ((((L[1] & L[2]) ^ aff()) & ((L[3] & L[4]) ^ aff())) ^ aff())
    else: t = ((L[0] & L[1]) ^ aff()) & ((L[2] ^ aff()) & (((L[3] & L[4]) ^ aff())) ^ aff())
    F = t ^ aff()
    if degree(F, 6) == 5: out.append((shape, F))
print(" ".join(f"{F:#018x}" for _, F in out)); print("# shapes:", [s for s, _ in out], file=sys.stderr)
