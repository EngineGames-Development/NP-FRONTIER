"""Exact MC of all 4-variable Boolean functions by breadth-first search over circuit spans (no SAT).

W_0 = span{1, x1..x4} (affine functions). A circuit with k AND gates yields the space
W_k = W_{k-1} + span{a*b} with a, b in W_{k-1}; every function computable with k ANDs lies in some W_k
(the output is an XOR of wires). S_k = union of all W_k. MC(f) = min{k : f in S_k}.
Truth tables: 16-bit ints, bit p = f(x) with x_j = bit (j-1) of p.
"""
import itertools, json, sys
N = 16
X = [sum(1 << p for p in range(N) if p >> j & 1) for j in range(4)]
ONE = (1 << N) - 1

def span(gens):
    s = {0}
    for g in gens:
        s |= {v ^ g for v in s}
    return frozenset(s)

W0 = span([ONE] + X)
levels = [set(W0)]
frontier = {W0}
for k in range(1, 4):
    nxt = set()
    for W in frontier:
        Wl = sorted(W)
        for a, b in itertools.combinations_with_replacement(Wl, 2):
            z = a & b
            if z in W: continue
            nxt.add(frozenset(W | {v ^ z for v in W}))
    Sk = set().union(*nxt) if nxt else set()
    levels.append(levels[-1] | Sk)
    frontier = nxt
    print(f"k={k}: distinct spaces {len(nxt)}, |S_{k}| = {len(levels[-1])}", flush=True)
    if len(levels[-1]) == 1 << N: break

mc = {}
for f in range(1 << N):
    mc[f] = next(k for k, S in enumerate(levels) if f in S)
json.dump({"mc": [mc[f] for f in range(1 << N)]}, open("mc4.json", "w"))
from collections import Counter
print("MC distribution over all 65536 functions:", sorted(Counter(mc.values()).items()))
