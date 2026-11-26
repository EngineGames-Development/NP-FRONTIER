"""Exhaustive check of Lemma 39 for all formal circuits with j <= 2 gates (on F_2^{2j}) and a random sample with
j = 3: every pair X, Y in L with XY in L satisfies (a), (b) or (c)."""
import itertools, random
def circuit_fns(j, al, be):
    n = 2 * j; N = 1 << n
    z = []; A = []; B = []
    for i in range(j):
        a = [((p >> (2*i)) & 1) for p in range(N)]; b = [((p >> (2*i+1)) & 1) for p in range(N)]
        for q in range(i):
            if (al[i] >> q) & 1: a = [x ^ y for x, y in zip(a, z[q])]
            if (be[i] >> q) & 1: b = [x ^ y for x, y in zip(b, z[q])]
        A.append(a); B.append(b); z.append([x & y for x, y in zip(a, b)])
    tov = lambda f: sum(bit << p for p, bit in enumerate(f))
    gens = [ (1 << N) - 1 ] + [tov([(p >> r) & 1 for p in range(N)]) for r in range(n)] + [tov(f) for f in z]
    return n, N, gens, [tov(f) for f in A], [tov(f) for f in B], [tov(f) for f in z]
def span(g):
    S = {0}
    for v in g: S |= {x ^ v for x in S}
    return S
def check(j, al, be):
    n, N, gens, A, B, Z = circuit_fns(j, al, be)
    L = span(gens); ONE = (1 << N) - 1; bad = 0
    gate_spans = [span([ONE, A[i], B[i], Z[i]]) for i in range(j)]
    Ls = sorted(L)
    for X in Ls:
        for Y in Ls:
            if Y < X: continue
            if (X & Y) not in L: continue
            if X in (0, ONE) or Y in (0, ONE) or (X ^ Y) in (0, ONE): continue
            if any(X in S and Y in S for S in gate_spans): continue
            bad += 1
    return bad
tot = 0; cnt = 0
for j in (1, 2):
    for al in itertools.product(*[range(1 << i) for i in range(j)]):
        for be in itertools.product(*[range(1 << i) for i in range(j)]):
            tot += check(j, list(al), list(be)); cnt += 1
random.seed(1)
for _ in range(6):
    al = [0, random.randrange(2), random.randrange(4)]; be = [0, random.randrange(2), random.randrange(4)]
    tot += check(3, al, be); cnt += 1
print("circuits checked:", cnt, "| pairs violating (a)/(b)/(c):", tot)
