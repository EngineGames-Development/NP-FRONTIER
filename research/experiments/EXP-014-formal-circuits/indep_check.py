"""EXP-014 independent re-implementation for k = 6, 7 (numpy; shares no code with formal4.c).

Subspaces K0 of F_2^8 are enumerated as kernels of dual subspaces H (k = 8 - dim H): H = span(h) for k = 7,
H = span(h1,h2) with h1 < h2 < h1^h2 for k = 6.  Cosets are the level sets of (h.p).  Affinity of f on a coset
is tested by affine interpolation from the coset's least point p0 along a nullspace basis.  Degeneracy is
tested in the dual: the functional w_e vanishes on K0 iff e_e^* lies in H.  Wirings are enumerated in full
(no swap symmetry), as an extra check of that reduction.
Prints totals (affine cosets, g-cosets) per k and writes the distinct non-degenerate g tables (mod affine).
"""
import numpy as np, itertools, sys, collections

def nullspace_basis(H):            # H: list of dual vectors (ints); returns basis of {p : h.p = 0 for h in H}
    vecs = [p for p in range(256) if all(bin(p & h).count("1") % 2 == 0 for h in H)]
    basis = []
    span = {0}
    for p in vecs:
        if p not in span:
            basis.append(p); span |= {s ^ p for s in span}
    return basis, vecs

def circuits(full=True):
    W = [np.array([(p >> t) & 1 for p in range(256)], dtype=np.uint8) for t in range(8)]
    for a1, b1 in itertools.product(range(2), repeat=2):
        for a2, b2 in itertools.product(range(4), repeat=2):
            for a3, b3 in itertools.product(range(8), repeat=2):
                al, be = [0, a1, a2, a3], [0, b1, b2, b3]
                z = []
                for i in range(4):
                    A, B = W[2 * i].copy(), W[2 * i + 1].copy()
                    for j in range(i):
                        if (al[i] >> j) & 1: A ^= z[j]
                        if (be[i] >> j) & 1: B ^= z[j]
                    z.append(A & B)
                for gm in range(8):
                    f = z[3].copy()
                    for j in range(3):
                        if (gm >> j) & 1: f ^= z[j]
                    yield (al, be, gm), f

def setup(k):
    if k == 7:
        Hs = [[h] for h in range(1, 256)]
    else:
        Hs = [[h1, h2] for h1 in range(1, 256) for h2 in range(h1 + 1, 256) if h2 < (h1 ^ h2)]
    S = len(Hs); ncos = 2 ** (8 - k); npt = 2 ** k
    PT = np.zeros((S, ncos, npt), dtype=np.int64); BI = np.zeros((S, ncos, k), dtype=np.int64)
    Tm = np.array([[(t >> r) & 1 for r in range(k)] for t in range(npt)], dtype=np.int64)  # npt x k
    for s, H in enumerate(Hs):
        basis, _ = nullspace_basis(H)
        assert len(basis) == k
        labels = {}
        for p in range(256):
            lab = tuple(bin(p & h).count("1") % 2 for h in H)
            labels.setdefault(lab, []).append(p)
        for c, lab in enumerate(sorted(labels)):
            p0 = min(labels[lab])
            for t in range(npt):
                q = p0
                for r in range(k):
                    if (t >> r) & 1: q ^= basis[r]
                PT[s, c, t] = q
            BI[s, c] = [p0 ^ b for b in basis]
            assert sorted(PT[s, c].tolist()) == sorted(labels[lab])
    return Hs, PT, BI, Tm

def in_span(v, H):
    sp = {0}
    for h in H: sp |= {s ^ h for s in sp}
    return v in sp

def degenerate(al, be, H):
    for g in range(4):
        if al[g] == 0 and in_span(1 << (2 * g), H): return True
        if be[g] == 0 and in_span(1 << (2 * g + 1), H): return True
        if al[g] == be[g] and in_span((1 << (2 * g)) | (1 << (2 * g + 1)), H): return True
    return False

def reduce_mod_affine(vals, k):
    a = list(int(x) for x in vals)
    for i in range(k):
        for p in range(1 << k):
            if (p >> i) & 1: a[p] ^= a[p ^ (1 << i)]
    deg = max((bin(p).count("1") for p in range(1 << k) if a[p]), default=0)
    for p in range(1 << k):
        if bin(p).count("1") <= 1: a[p] = 0
    for i in range(k):
        for p in range(1 << k):
            if (p >> i) & 1: a[p] ^= a[p ^ (1 << i)]
    return sum(b << p for p, b in enumerate(a)), deg

for k in (7, 6):
    Hs, PT, BI, Tm = setup(k)
    naff = ng = nnd = 0; distinct = {}
    for (al, be, gm), f in circuits():
        v = f[PT]                                  # S x ncos x npt
        f0 = v[:, :, 0]
        d = f[BI] ^ f0[:, :, None]                 # S x ncos x k
        pred = (f0[:, :, None] + (d.astype(np.int64) @ Tm.T)) % 2
        aff = np.all(v == pred, axis=2)            # S x ncos
        for s in np.nonzero(aff.any(axis=1))[0]:
            for i in np.nonzero(aff[s])[0]:
                naff += 1
                for j in range(aff.shape[1]):
                    if j != i and not aff[s, j]:
                        ng += 1
                        if not degenerate(al, be, Hs[s]):
                            nnd += 1
                            r, dg = reduce_mod_affine(v[s, j], k)
                            distinct.setdefault(r, dg)
    print(f"k={k}: dual subspaces={len(Hs)} affine cosets={naff} g-cosets={ng} nondegenerate={nnd} distinct mod affine={len(distinct)} degrees={dict(collections.Counter(distinct.values()))}", flush=True)
    with open(f"indep_nondeg_k{k}.txt", "w") as fo:
        for r, dg in sorted(distinct.items()): fo.write(f"{r:x} {dg}\n")
