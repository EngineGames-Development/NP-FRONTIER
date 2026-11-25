"""EXP-015 (part 3): PNE-001 at level m for ALL n from NIST's class lists (github.com/usnistgov/circuits/data/mc_dim).

Lemma (proved in research/proofs/PNE-001-level4.md, Lemma 26): a level-m counterexample exists iff some
function R0 of MC m (on d = dim R0 variables; up to affine equivalence, a listed class representative) has an
affine hyperplane H0 such that R0|H0 is affine and MC(R0|complement) = m.
For each listed representative and each of the 2(2^d - 1) affine hyperplanes: test affinity of R0|H0; for each
hit compute g = R0|complement (d-1 variables), its dimension, and decide MC(g) <= m-1 by SAT (mc.py, cycle 001;
the circuit is re-verified by evaluation).  dim(g) >= 2m-1 would already force MC(g) >= m (a counterexample).
Usage: python3 nist_hyperplane_check.py m [files...]
"""
import sys, os, re, time
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-001-mc-exact"))
from mc import mc_le, evaluate
D = "/home/user/usnistgov/circuits/data/mc_dim"

def tt(s, n):
    idx = np.arange(1 << n); t = np.zeros(1 << n, dtype=np.uint8)
    for mono in s.strip().split("+"):
        mono = mono.strip()
        if mono in ("", "0"): continue
        if mono == "1": t ^= 1; continue
        m = np.ones(1 << n, dtype=np.uint8)
        for i in re.findall(r"x(\d+)", mono): m &= ((idx >> (int(i) - 1)) & 1).astype(np.uint8)
        t ^= m
    return t

def anf(t, n):
    a = t.copy(); idx = np.arange(1 << n)
    for i in range(n):
        sel = ((idx >> i) & 1) == 1
        a[sel] ^= a[idx[sel] ^ (1 << i)]
    return a

WT = {}
def deg(t, n):
    if n not in WT: WT[n] = np.array([bin(p).count("1") for p in range(1 << n)])
    a = anf(t, n); return int(WT[n][a == 1].max()) if a.any() else -1

def restrict(t, n, u, c):
    """restriction of t to {z : u.z = c} as a function on n-1 variables (pivot = lowest set bit of u)."""
    p = (u & -u).bit_length() - 1
    out = np.zeros(1 << (n - 1), dtype=np.uint8)
    for i in range(1 << (n - 1)):
        z = ((i >> p) << (p + 1)) | (i & ((1 << p) - 1))
        if (bin(z & u).count("1") & 1) != c: z |= 1 << p
        out[i] = t[z]
    return out

def dimension(t, n):
    """n minus dim of {v : D_v t constant}."""
    idx = np.arange(1 << n); cnt = 0
    for v in range(1 << n):
        d = t ^ t[idx ^ v]
        if d.min() == d.max(): cnt += 1
    return n - int(round(np.log2(cnt)))

def main():
    m = int(sys.argv[1])
    files = sys.argv[2:] or sorted(f for f in os.listdir(D) if re.match(rf"mc{m}_dim\d+\.txt$", f) and "all" not in f)
    tot_reps = hits = cex = 0; t0 = time.time()
    for fn in files:
        dim = int(re.search(r"dim(\d+)", fn).group(1))
        reps = [l.strip() for l in open(os.path.join(D, fn)) if l.strip()]
        fh = 0
        for s in reps:
            tot_reps += 1
            R = tt(s, dim)
            assert dimension(R, dim) == dim if dim <= 8 else True
            for u in range(1, 1 << dim):
                for c in (0, 1):
                    h = restrict(R, dim, u, c)
                    if deg(h, dim - 1) > 1: continue
                    hits += 1; fh += 1
                    g = restrict(R, dim, u, 1 - c)
                    gd = dimension(g, dim - 1)
                    if 2 * (m - 1) < gd:
                        cex += 1; print(f"COUNTEREXAMPLE (dimension) {fn}: {s} u={u} c={c} dim(g)={gd}", flush=True); continue
                    gi = int("".join(str(int(b)) for b in g[::-1]), 2)
                    circ = mc_le(gi, dim - 1, m - 1)
                    if circ is None or evaluate(circ, dim - 1) != gi:
                        cex += 1; print(f"NO {m-1}-GATE CIRCUIT {fn}: {s} u={u} c={c} dim(g)={gd}", flush=True)
        print(f"{fn}: reps {len(reps)}, affine-hyperplane hits {fh}  [{time.time()-t0:.0f}s]", flush=True)
    print(f"level {m}: representatives {tot_reps}, hyperplanes with affine restriction {hits}, counterexamples {cex}")

if __name__ == "__main__":
    main()
