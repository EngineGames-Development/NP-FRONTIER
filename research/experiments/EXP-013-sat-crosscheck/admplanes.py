"""EXP-013 (variant used): SAT cross-check over the admissible planes only.

Admissibility (Lemma 9'): u is admissible for F at level 4 iff both halves F|_{<u,.>=c} have MC <= 3.
Halves are read from the exact 5-variable table EXP-010/mc5.mc5 (4 bits per function, low nibble =
even index).  Any affine parametrisation of a hyperplane preserves MC, so the parametrisation used here
(pivot = highest set bit of u) need not match cert4b's.  Each admissible plane span(u1,u2) is then
tested by mc.py's fixed-first-gate SAT encoding (cycle 001, DRAT-validated), which is independent of
cert4b's second/third-level filters and final test.  MC(F) >= 5 iff every admissible plane is UNSAT
(given MC(F) >= 4, which holds because F|_{y=1} = g has MC 4).
Usage: python3 admplanes.py g_hex
"""
import sys, os, time, mmap
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-001-mc-exact"))
from mc import mc_le_fixed_first
TABLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-010-level4-certificates", "mc5.mc5")

def mc5(mm, f):
    b = mm[f >> 1]
    return (b >> 4) if (f & 1) else (b & 15)

def half(F, u, c):
    p = u.bit_length() - 1; f = 0
    for i in range(32):
        low = i & ((1 << p) - 1); high = (i >> p) << (p + 1)
        pt = high | low
        if (bin(pt & u).count("1") & 1) != c: pt |= 1 << p
        if (F >> pt) & 1: f |= 1 << i
    return f

def main():
    g = int(sys.argv[1], 16)
    F = sum(1 << (32 + p) for p in range(32) if (g >> p) & 1)
    with open(TABLE, "rb") as fh:
        mm = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)
        assert mc5(mm, g) == 4, "g must have MC 4"
        adm = [False] * 64
        for u in range(1, 64):
            adm[u] = all(mc5(mm, half(F, u, c)) <= 3 for c in (0, 1))
    planes = [(v, w) for v in range(1, 64) for w in range(v + 1, 64) if w < (v ^ w) and adm[v] and adm[w] and adm[v ^ w]]
    print(f"g={g:#010x} admissible_dirs={sum(adm)} admissible_planes={len(planes)}", flush=True)
    t0 = time.time()
    for i, (v, w) in enumerate(planes):
        t = time.time()
        st, res = mc_le_fixed_first(F, 6, 4, (v << 1, w << 1))
        print(f"plane {i+1}/{len(planes)} ({v},{w}) {st} {time.time()-t:.1f}s", flush=True)
        if st != "UNSAT":
            print(f"RESULT g={g:#010x} {st} at plane ({v},{w}) circuit={res}", flush=True); return
    print(f"RESULT g={g:#010x} ALL_UNSAT over {len(planes)} admissible planes => MC(yg) >= 5  total={time.time()-t0:.0f}s", flush=True)

if __name__ == "__main__":
    main()
