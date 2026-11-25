"""EXP-015: cross-check of our exact 5-variable MC table (EXP-010/mc5.mc5, built from EXP-007) against the
NIST classification (github.com/usnistgov/circuits, data/mc_dim: representatives of every affine
equivalence class with MC <= 4 by dimension; the 48 classes of dimension <= 5 are all 5-variable classes).
(1) every representative of dimension <= 5 must get the NIST MC value from our table;
(2) our table must be invariant under random affine transformations x -> Ax+b plus addition of affine
    functions (MC is invariant under these), tested on random functions.
Usage: python3 check_mc5_vs_nist.py /path/to/usnistgov/circuits/data/mc_dim"""
import sys, os, mmap, random, re
TABLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-010-level4-certificates", "mc5.mc5")

def tt_from_anf(s, n):
    t = 0
    for p in range(1 << n):
        v = 0
        for mono in s.strip().split("+"):
            mono = mono.strip()
            if mono == "0": continue
            if mono == "1": v ^= 1; continue
            vars_ = [int(x) for x in re.findall(r"x(\d+)", mono)]
            v ^= all((p >> (i - 1)) & 1 for i in vars_)
        t |= v << p
    return t

def mc5(mm, f): b = mm[f >> 1]; return (b >> 4) if (f & 1) else (b & 15)

def main():
    d = sys.argv[1]
    mm = mmap.mmap(os.open(TABLE, os.O_RDONLY), 0, prot=mmap.PROT_READ)
    total = bad = 0
    for fn in sorted(os.listdir(d)):
        m = re.match(r"mc(\d+)_dim(\d+)\.txt$", fn)
        if not m: continue
        mcv, dim = int(m.group(1)), int(m.group(2))
        if dim > 5: continue
        for line in open(os.path.join(d, fn)):
            if not line.strip(): continue
            f = tt_from_anf(line, 5); ours = mc5(mm, f); total += 1
            if ours != mcv: bad += 1; print("MISMATCH", fn, line.strip(), "ours", ours)
    print(f"(1) representatives of dimension <= 5 checked: {total}, mismatches: {bad}")
    # (2) random affine-invariance test
    rng = random.Random(2026); viol = 0; N = 200000
    for _ in range(N):
        f = rng.getrandbits(32)
        while True:
            A = [rng.getrandbits(5) for _ in range(5)]
            # invertibility over F2
            rows = A[:]; r = 0
            for c in range(5):
                piv = next((i for i in range(r, 5) if (rows[i] >> c) & 1), None)
                if piv is None: break
                rows[r], rows[piv] = rows[piv], rows[r]
                for i in range(5):
                    if i != r and (rows[i] >> c) & 1: rows[i] ^= rows[r]
                r += 1
            if r == 5: break
        b = rng.getrandbits(5); lin = rng.getrandbits(5); c0 = rng.getrandbits(1)
        g = 0
        for x in range(32):
            y = b
            for i in range(5):
                if (x >> i) & 1: y ^= A[i]
            v = ((f >> y) & 1) ^ (bin(x & lin).count("1") & 1) ^ c0
            g |= v << x
        if mc5(mm, f) != mc5(mm, g): viol += 1
    print(f"(2) random affine-invariance tests: {N}, violations: {viol}")

if __name__ == "__main__":
    main()
