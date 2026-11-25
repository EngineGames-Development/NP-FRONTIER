"""Test of the 'last-gate redundancy' conjecture on all (C0, C1) pairs of a formal4 output file:
if Phi|C0 is affine, then z_m|C1 lies in span(affine functions on C1, z_j|C1 for j < m)."""
import sys, collections
from redundancy import gates, restrict, span_reduce, in_span
k = int(sys.argv[2]); fn = sys.argv[1]
ok = bad = 0; cache = {}
for line in open(fn):
    f = line.split()
    w = tuple(map(int, f[3:10])); basis = tuple(map(int, f[11:18]))[:k]
    al = [0, w[0], w[1], w[2]]; be = [0, w[3], w[4], w[5]]
    c1 = int(f[21])
    if w not in cache: cache[w] = gates(al, be)
    z = cache[w]
    aff = [(1 << (1 << k)) - 1] + [sum(((t >> r) & 1) << t for t in range(1 << k)) for r in range(k)]
    rows = span_reduce(aff + [restrict(z[j], basis, c1, k) for j in range(3)])
    if in_span(rows, restrict(z[3], basis, c1, k)): ok += 1
    else:
        bad += 1
        if bad <= 5: print("VIOLATION", line.strip()[:120])
print(f"{fn}: pairs {ok+bad}, last gate redundant on C1: {ok}, violations: {bad}")
