"""EXP-014 triage of the k=6,7 survivor cosets written by formal4.

For each line 'G k=.. wiring a1 a2 a3 b1 b2 b3 gm basis b0..b6 c0 c1 tab HI LO':
 - degenerate(K): some gate i has an input whose formal variable vanishes on K and which takes no earlier gate,
   or w_{2i}+w_{2i+1} vanishes on K with alpha_i = beta_i.  Then the restricted circuit has an affine gate,
   so MC(g) <= 3 (Lemma 9 mechanism, the same on every coset of K).
 - otherwise the table g (2^k bits, index t over the RREF basis) is reduced modulo affine functions
   (ANF terms of degree <= 1 dropped) and deduplicated; degree is recorded.
Writes nondeg_k{6,7}.txt with distinct reduced tables (hex) for the exact MC <= 3 test.
"""
import sys, collections

def anf(t, n):
    a = list((t >> p) & 1 for p in range(1 << n))
    for i in range(n):
        for p in range(1 << n):
            if (p >> i) & 1: a[p] ^= a[p ^ (1 << i)]
    return a

def reduce_mod_affine(t, n):
    a = anf(t, n)
    for p in range(1 << n):
        if bin(p).count("1") <= 1: a[p] = 0
    deg = max((bin(p).count("1") for p in range(1 << n) if a[p]), default=0)
    # back to truth table (Moebius is an involution)
    for i in range(n):
        for p in range(1 << n):
            if (p >> i) & 1: a[p] ^= a[p ^ (1 << i)]
    return sum(b << p for p, b in enumerate(a)), deg

def vanishes(mask_bit, basis):           # does the formal coordinate functional vanish on K?
    return all(((b >> mask_bit) & 1) == 0 for b in basis)

def vanishes2(i, j, basis):
    return all((((b >> i) ^ (b >> j)) & 1) == 0 for b in basis)

def degenerate(al, be, basis):
    for g in range(4):
        a, b = al[g], be[g]
        if a == 0 and vanishes(2 * g, basis): return True
        if b == 0 and vanishes(2 * g + 1, basis): return True
        if a == b and vanishes2(2 * g, 2 * g + 1, basis): return True
    return False

