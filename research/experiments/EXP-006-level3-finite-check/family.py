"""EXP-006 step 1: the finite family of Theorem 16 and its symmetry orbits.
Variables (5): x1 = bit0, x2 = bit1, u1..u3 = bits 2..4. G' = x1*l1 + x2*l2 + x1*x2*l3 + lam(u), with l_i affine in u
and lam linear in u (constant 0 WLOG: MC(y*(G'+1)) = MC(y*G' + y) = MC(y*G')).
Symmetries used (they preserve MC(G') and MC(y*G')): affine bijections of the 5-variable input space that act
separately on (x1,x2) and on u, plus complementation. Orbits are computed by union-find over truth tables."""
import itertools, json, os, sys
import numpy as np
ALL = (1 << 32) - 1
bit = lambda p, j: (p >> j) & 1
def tt(fn): return sum(1 << p for p in range(32) if fn(p))
def aff_u(code):                               # code 0..15: bits 0..2 = linear coeffs of u1..u3, bit 3 = constant
    return lambda p: ((bit(code,0) & bit(p,2)) ^ (bit(code,1) & bit(p,3)) ^ (bit(code,2) & bit(p,4)) ^ bit(code,3))
family = {}
for c1, c2, c3, cl in itertools.product(range(16), range(16), range(16), range(8)):
    l1, l2, l3, lam = aff_u(c1), aff_u(c2), aff_u(c3), aff_u(cl)
    g = tt(lambda p: (bit(p,0) & l1(p)) ^ (bit(p,1) & l2(p)) ^ (bit(p,0) & bit(p,1) & l3(p)) ^ lam(p))
    family[min(g, g ^ ALL)] = (c1, c2, c3, cl)
print("distinct functions in family (mod complement):", len(family))
# generators: point maps on F_2^5 (affine, separately on x-part and u-part)
def perm_from(pointmap): return [pointmap(p) for p in range(32)]
def xor_bits(p, mask): return p ^ mask
gens = [perm_from(lambda p, m=m: p ^ m) for m in (1, 2, 4, 8, 16)]                       # translations
gens.append(perm_from(lambda p: (p & ~3) | ((p & 1) << 1) | ((p >> 1) & 1)))              # swap x1,x2
gens.append(perm_from(lambda p: p ^ ((p & 2) >> 1)))                                      # x1 <- x1 + x2
gens.append(perm_from(lambda p: (p & 3) | (((p >> 2) & 1) << 3) | (((p >> 3) & 1) << 2) | (p & 16)))  # swap u1,u2
gens.append(perm_from(lambda p: (p & 3) | (((p >> 2) & 1) << 4) | (((p >> 4) & 1) << 2) | (p & 8)))   # swap u1,u3
gens.append(perm_from(lambda p: p ^ (((p >> 3) & 1) << 2)))                               # u1 <- u1 + u2
def apply(g, perm): return sum(((g >> perm[p]) & 1) << p for p in range(32))
keys = list(family); idx = {g: i for i, g in enumerate(keys)}; parent = list(range(len(keys)))
def find(i):
    while parent[i] != i: parent[i] = parent[parent[i]]; i = parent[i]
    return i
outside = 0
for g in keys:
    for perm in gens:
        h = apply(g, perm); h = min(h, h ^ ALL)
        if h not in idx: outside += 1; continue
        a, b = find(idx[g]), find(idx[h])
        if a != b: parent[a] = b
orbits = {}
for g in keys: orbits.setdefault(find(idx[g]), []).append(g)
print("images outside the family (should be 0):", outside)
print("orbits:", len(orbits))
json.dump({"reps": [min(v) for v in orbits.values()], "sizes": [len(v) for v in orbits.values()]}, open("orbits.json", "w"))
