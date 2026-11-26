"""Brute-force check (all 2^10 parameter values, all inputs) of the expansion in the proof of Lemma 37:
C' = (A_m + aW + d1)(B_m + bW + d2) + Gamma + gW, with A_m = p + a z, B_m = q + b z, Gamma = G0 + g z, z = A B (gate m-1),
W = e2 A + e1 B + e1 e2, equals C + W(bp + aq) + (a d2 + b d1) z + d2 p + d1 q + (aW + d1)(bW + d2) + gW,
and kappa*A*B + W*X (X = bp + aq) has rank <= 2 as a quadratic form in (A, B, X): it equals l1*l2 + affine."""
import itertools
bad = 0
for A, B, p, q, G0, a, b, g, d1, d2, e1, e2 in itertools.product((0, 1), repeat=12):
    z = A & B; W = (e2 & A) ^ (e1 & B) ^ (e1 & e2)
    Am, Bm, Gam = p ^ (a & z), q ^ (b & z), G0 ^ (g & z)
    C = (Am & Bm) ^ Gam
    Cp = ((Am ^ (a & W) ^ d1) & (Bm ^ (b & W) ^ d2)) ^ Gam ^ (g & W)
    rhs = C ^ (W & ((b & p) ^ (a & q))) ^ (((a & d2) ^ (b & d1)) & z) ^ (d2 & p) ^ (d1 & q) ^ (((a & W) ^ d1) & ((b & W) ^ d2)) ^ (g & W)
    bad += Cp != rhs
# rank <= 2: for every (kappa, e1, e2) the function Q(A,B,X) = kappa*A*B + W*X is l1*l2 + affine for some affine l1, l2
def tab(f): return tuple(f(A, B, X) for A, B, X in itertools.product((0, 1), repeat=3))
aff = [lambda A, B, X, c=c: (c[0] & A) ^ (c[1] & B) ^ (c[2] & X) ^ c[3] for c in itertools.product((0, 1), repeat=4)]
affset = {tab(f) for f in aff}
prods = {tuple(x ^ y for x, y in zip(tab(lambda A, B, X: l1(A, B, X) & l2(A, B, X)), t)) for l1 in aff for l2 in aff for t in affset}
for kappa, e1, e2 in itertools.product((0, 1), repeat=3):
    Q = tab(lambda A, B, X: (kappa & A & B) ^ ((((e2 & A) ^ (e1 & B) ^ (e1 & e2))) & X))
    bad += Q not in prods
print("Lemma 37 checks: mismatches =", bad)
