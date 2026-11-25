"""EXP-015 (part 2): PNE-001 for all 5-variable g with MC(g) = m in {3, 4}, checked only against NIST's
classification of 6-variable functions (github.com/usnistgov/circuits, data/mc_dim).

Reduction: MC(y*(g o T + l)) = MC(y*(g + l o T^-1)) because (y*h) o (T x id) = y*(h o T) and adding the affine
y*c is free.  So for every class representative g of MC m (dimension <= 5) it suffices to test F = y*(g + l) for
all 32 linear forms l on 5 variables.  F is a 6-variable function (y = x6).  Claim: MC(F) >= m+1, i.e. F is
not affine-equivalent to any class of MC <= m.  Test: an affine-invariant fingerprint of F (degree, multiset of
|Walsh|, multiset of |autocorrelation|, multiset of degrees of the 63 derivatives) differs from the fingerprint
of every NIST class representative of MC <= m and dimension <= 6.  A collision is reported, not resolved.
Caveat (AUDIT-003 I-4): the derivative-degree component is not affine-invariant for functions with a constant
derivative (adding a linear function can turn a derivative 0 into 1, e.g. x1x2 vs x1x2+x3).  The test is still
sound here: every constant derivative of y*g is 0, and no listed representative of MC <= 4 and dimension <= 6
has a derivative equal to 1 (checked by AUDIT-003), so a fingerprint mismatch still proves non-equivalence.
"""
import sys, os, re, random, itertools
import numpy as np
D = "/home/user/usnistgov/circuits/data/mc_dim" if len(sys.argv) < 2 else sys.argv[1]
N = 6; P = 1 << N

def tt_from_anf(s, n=N):
    t = np.zeros(1 << n, dtype=np.int64)
    idx = np.arange(1 << n)
    for mono in s.strip().split("+"):
        mono = mono.strip()
        if mono in ("", "0"): continue
        if mono == "1": t ^= 1; continue
        m = np.ones(1 << n, dtype=np.int64)
        for i in re.findall(r"x(\d+)", mono): m &= (idx >> (int(i) - 1)) & 1
        t ^= m
    return t

def anf_deg(t):
    a = t.copy()
    for i in range(N):
        b = (np.arange(P) >> i) & 1
        a[b == 1] ^= a[np.arange(P)[b == 1] ^ (1 << i)]
    w = np.array([bin(p).count("1") for p in range(P)])
    return int(w[a == 1].max()) if a.any() else -1

def walsh(t):
    v = (1 - 2 * t).astype(np.int64)
    h = 1
    while h < P:
        v = v.reshape(-1, 2, h); v = np.concatenate([v[:, 0] + v[:, 1], v[:, 0] - v[:, 1]], axis=1).reshape(-1); h *= 2
    return v

def fingerprint(t):
    W = walsh(t)
    s = 1 - 2 * t
    ac = [int(np.sum(s * s[np.arange(P) ^ v])) for v in range(P)]
    dd = sorted(anf_deg(t ^ t[np.arange(P) ^ v]) for v in range(1, P))
    return (anf_deg(t), tuple(sorted(np.abs(W).tolist())), tuple(sorted(abs(a) for a in ac)), tuple(dd))

def random_ea(t, rng):
    while True:
        A = np.array([[rng.getrandbits(1) for _ in range(N)] for _ in range(N)])
        if round(abs(np.linalg.det(A))) % 2 == 1: break
    b = np.array([rng.getrandbits(1) for _ in range(N)]); l = np.array([rng.getrandbits(1) for _ in range(N)]); c = rng.getrandbits(1)
    X = np.array([[(x >> i) & 1 for i in range(N)] for x in range(P)])
    Y = (X @ A.T + b) % 2
    yi = (Y * (1 << np.arange(N))).sum(axis=1)
    return t[yi] ^ ((X @ l) % 2) ^ c

def load_reps(maxmc):
    reps = []
    for fn in sorted(os.listdir(D)):
        m = re.match(r"mc(\d+)_dim(\d+)\.txt$", fn)
        if m and int(m.group(1)) <= maxmc and int(m.group(2)) <= N:
            reps += [(int(m.group(1)), int(m.group(2)), l.strip()) for l in open(os.path.join(D, fn)) if l.strip()]
    return reps

def main():
    rng = random.Random(1)
    # invariance self-test of the fingerprint
    for _ in range(30):
        t = np.array([rng.getrandbits(1) for _ in range(P)])
        assert fingerprint(t) == fingerprint(random_ea(t, rng)), "fingerprint not EA-invariant"
    print("fingerprint EA-invariance self-test passed (30 random functions)")
    reps4 = load_reps(4)
    fp = {}
    for mcv, dim, s in reps4: fp.setdefault(fingerprint(tt_from_anf(s)), []).append((mcv, dim, s))
    print(f"NIST classes with MC <= 4, dim <= 6: {len(reps4)}; distinct fingerprints: {len(fp)}")
    idx = np.arange(P); y = (idx >> 5) & 1
    lin = [((idx & l) != 0) * 0 for l in range(1)]
    for m in (3, 4):
        gs = [(dim, s) for mcv, dim, s in load_reps(m) if mcv == m and dim <= 5]
        tested = coll = 0
        for dim, s in gs:
            g = tt_from_anf(s)                       # on x1..x5 (x6 absent)
            for l in range(32):
                lf = np.array([bin(x & l).count("1") & 1 for x in idx])
                F = y & (g ^ lf)
                f_ = fingerprint(F); tested += 1
                hits = [r for r in fp.get(f_, []) if r[0] <= m]
                if hits: coll += 1; print(f"COLLISION m={m} g={s} l={l}: fingerprint matches {hits[:3]}")
        print(f"level {m}: classes {len(gs)}, functions y*(g+l) tested {tested}, fingerprint collisions with MC<={m} classes: {coll}")

if __name__ == "__main__":
    main()
