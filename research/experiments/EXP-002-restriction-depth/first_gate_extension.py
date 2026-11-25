"""SAT-free proof that MC(y*g*) >= 4 for g* = 0xfff3d212 (6 variables: x1..x5 = bits 0..4, y = bit 5).

Argument (see proof doc, Lemma 9): in a 3-AND circuit for F (deg F = 4, so all gates are non-degenerate), the first
gate z1 = a*b has inputs whose directions are distinct and both admissible (both restrictions have MC <= 2).
pair_test.py found exactly two admissible directions, x2 and x2+y, so z1 = (x2+e)(x2+y+e') for some e, e' in {0,1}.
For each such z1 we check exhaustively whether F lies in W2 + span{A'B'} for some W2 = W1 + span{AB},
A, B in W1 = span{1,x,y,z1}, A', B' in W2. If none works, no 3-AND circuit computes F."""
import numpy as np, sys, time
N = 64; M = np.uint64(0xFFFFFFFFFFFFFFFF)
var = [sum(1 << p for p in range(N) if p >> j & 1) for j in range(6)]          # x1..x5, y
ONE = (1 << N) - 1
g = int(sys.argv[1], 16) if len(sys.argv) > 1 else 0xfff3d212
F = sum(1 << p for p in range(N) if (p >> 5) & 1 and (g >> (p & 31)) & 1)

def echelon(gens):
    basis = []                                   # list of (pivot, vector), pivot = highest set bit
    for v in gens:
        for piv, b in basis:
            if v >> piv & 1: v ^= b
        if v:
            piv = v.bit_length() - 1
            basis = [(p, b ^ v if b >> piv & 1 else b) for p, b in basis] + [(piv, v)]
    return basis
def reduce_vec(v, basis):
    for piv, b in basis:
        if v >> piv & 1: v ^= b
    return v
def elements(basis):
    s = [0]
    for _, b in basis: s += [x ^ b for x in s]
    return s
def reduce_np(arr, basis):                        # vectorized reduction modulo span(basis)
    for piv, b in basis:
        bit = (arr >> np.uint64(piv)) & np.uint64(1)
        arr = arr ^ (bit * np.uint64(b))
    return arr

if __name__ == "__main__":
    X2, Y = var[1], var[5]
    found = []
    t0 = time.time()
    for e in (0, 1):
        for e2 in (0, 1):
            a = X2 ^ (ONE if e else 0); b = X2 ^ Y ^ (ONE if e2 else 0)
            z1 = a & b
            B1 = echelon([ONE] + var + [z1]); W1 = elements(B1)
            seen = set(); cand = 0
            for i in range(len(W1)):
                for j in range(i + 1, len(W1)):
                    r = reduce_vec(W1[i] & W1[j], B1)
                    if r == 0 or r in seen: continue
                    seen.add(r)
                    B2 = echelon([v for _, v in B1] + [r]); W2 = np.array(elements(B2), dtype=np.uint64)
                    ii, jj = np.triu_indices(len(W2), 1)
                    prods = W2[ii] & W2[jj]
                    if (reduce_np(prods ^ np.uint64(F), B2) == 0).any() or reduce_vec(F, B2) == 0:
                        found.append((e, e2, r)); break
                if found and found[-1][:2] == (e, e2): break
            print(f"z1=(x2+{e})(x2+y+{e2}): distinct W2 spaces checked: {len(seen)}; extension found: {bool(found and found[-1][:2]==(e,e2))} ({time.time()-t0:.0f}s)", flush=True)
    print("CONCLUSION:", "MC(y*g) >= 4 (no first gate extends to a 3-AND circuit)" if not found else f"3-AND circuit exists: {found}")
