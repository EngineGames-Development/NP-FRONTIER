"""EXP-014 exploration: for the non-degenerate dim-6 pairs (C0 affine, C1 not), test 'triangular redundancy':
some gate i with z_i|C in span(affine functions on C, z_j|C for j<i).  Such a gate can be removed (its value is
substituted), so MC(Phi|C) <= 3.  Tested on C1 and on C0, and on whether it holds on every coset of K."""
import sys, collections
sys.path.insert(0, ".")
from triage_lib import degenerate

def gates(al, be):
    W = [[(p >> t) & 1 for p in range(256)] for t in range(8)]
    z = []
    for i in range(4):
        A = W[2*i][:]; B = W[2*i+1][:]
        for j in range(i):
            if (al[i] >> j) & 1: A = [a ^ b for a, b in zip(A, z[j])]
            if (be[i] >> j) & 1: B = [a ^ b for a, b in zip(B, z[j])]
        z.append([a & b for a, b in zip(A, B)])
    return z

def restrict(vec, basis, c, k):
    out = []
    for t in range(1 << k):
        q = c
        for r in range(k):
            if (t >> r) & 1: q ^= basis[r]
        out.append(vec[q])
    return sum(b << i for i, b in enumerate(out))

def rank_insert(basis_rows, v):
    for r in basis_rows:
        v = min(v, v ^ r)
    return v

def span_reduce(vectors):
    rows = []
    for v in vectors:
        v2 = v
        for r in sorted(rows, reverse=True):
            v2 = min(v2, v2 ^ r)
        if v2: rows.append(v2)
    return rows

def in_span(rows, v):
    for r in sorted(rows, reverse=True):
        v = min(v, v ^ r)
    return v == 0

def redundant_gate(z, basis, c, k):
    aff = [(1 << (1 << k)) - 1] + [sum(((t >> r) & 1) << t for t in range(1 << k)) for r in range(k)]
    rows = span_reduce(aff)
    for i in range(4):
        zi = restrict(z[i], basis, c, k)
        if in_span(rows, zi): return i
        rows = span_reduce(rows + [zi])
    return None

if __name__ == "__main__":
    k = 6; stats = collections.Counter(); seen = 0
    for line in open("out_k6.txt"):
        f = line.split()
        w = list(map(int, f[3:10])); basis = list(map(int, f[11:18]))[:k]
        al = [0, w[0], w[1], w[2]]; be = [0, w[3], w[4], w[5]]
        if degenerate(al, be, basis): continue
        c0, c1 = int(f[19]), int(f[21])
        z = gates(al, be)
        r1 = redundant_gate(z, basis, c1, k)
        stats["C1 redundant gate " + str(r1)] += 1
        seen += 1
    print("non-degenerate pairs analysed:", seen)
    for kk, v in sorted(stats.items()): print(kk, v)
