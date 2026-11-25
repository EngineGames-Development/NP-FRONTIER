"""Data check of Lemma 30's case analysis (m = 4, codimension 2), on every pair in out_k6_full.txt (all wirings).
For each pair: H = K^perp; dim pi(H) where pi = (bit 6, bit 7) = (u, v) of the last gate.
 case 2 -> last gate must be triangularly redundant on C1;
 case 1 -> with h0 in H_0, h1 = other basis vector: the gate named by the proof must be degenerate for K;
 case 0 -> must not occur."""
import sys, collections
from redundancy import gates, restrict, span_reduce, in_span
from triage_lib import degenerate
k = 6; stats = collections.Counter(); cache = {}
def dual(basis):
    return [h for h in range(256) if all(bin(h & b).count("1") % 2 == 0 for b in basis)]
def gate_degenerate(g, al, be, H):
    Hs = set(H)
    return ((al[g] == 0 and (1 << (2*g)) in Hs) or (be[g] == 0 and (1 << (2*g+1)) in Hs)
            or (al[g] == be[g] and ((1 << (2*g)) | (1 << (2*g+1))) in Hs))
for line in open(sys.argv[1]):
    f = line.split()
    w = tuple(map(int, f[3:10])); basis = list(map(int, f[11:18]))[:k]
    al = [0, w[0], w[1], w[2]]; be = [0, w[3], w[4], w[5]]; c1 = int(f[21])
    H = dual(basis); assert len(H) == 4
    pis = {((h >> 6) & 1, (h >> 7) & 1) for h in H}
    d = {1: 0, 2: 1, 4: 2}[len(pis)]
    if d == 0: stats["case0 (impossible!)"] += 1; continue
    if d == 2:
        if w not in cache: cache[w] = gates(al, be)
        z = cache[w]
        aff = [(1 << 64) - 1] + [sum(((t >> r) & 1) << t for t in range(64)) for r in range(k)]
        rows = span_reduce(aff + [restrict(z[j], basis, c1, k) for j in range(3)])
        ok = in_span(rows, restrict(z[3], basis, c1, k))
        stats["case2 last-gate-redundant" if ok else "case2 VIOLATION"] += 1
    else:
        h0 = next(h for h in H if h and ((h >> 6) & 3) == 0)
        h1 = next(h for h in H if ((h >> 6) & 3) != 0)
        pq = ((h1 >> 6) & 1, (h1 >> 7) & 1)
        coef = al[3] if pq == (1, 0) else be[3] if pq == (0, 1) else al[3] ^ be[3]
        if coef == 0: target = 3
        else: target = coef.bit_length() - 1          # j* = max of support
        ok = gate_degenerate(target, al, be, H)
        stats[f"case1 predicted gate {target} degenerate" if ok else "case1 VIOLATION"] += 1
for kk, v in sorted(stats.items()): print(kk, v)
