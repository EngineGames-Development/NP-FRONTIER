"""EXP-013: independent SAT cross-check of cert4b's NONE verdicts (no MC tables, no admissibility filters).

For F = y*g on 6 variables (index bit j = x_{j+1} for j<5, bit 5 = y), MC(F) <= 4 iff some 4-gate circuit
has first gate l1*l2 with (l1,l2) the canonical basis (v<w<v^w) of a 2-dim space of linear forms.
Justification (elementary): (a+c)(b+c') = ab + affine, and ab depends on span(a,b) only up to affine terms;
affine terms are absorbed by later gates and the output.  A degenerate first gate is affine, and a circuit
with <= 3 gates can be padded with an unused first gate.  So MC(F) >= 5 iff all 651 planes are UNSAT.
Usage: python3 allplanes.py g_hex [--drat DIR]
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-001-mc-exact"))
from mc import mc_le_fixed_first, encode

def yg_table(g):
    return sum(1 << (32 + p) for p in range(32) if (g >> p) & 1)

def planes(n):
    for v in range(1, 1 << n):
        for w in range(v + 1, 1 << n):
            if w < (v ^ w):
                yield v, w

def main():
    g = int(sys.argv[1], 16); F = yg_table(g); n, k = 6, 4
    drat_dir = sys.argv[sys.argv.index("--drat") + 1] if "--drat" in sys.argv else None
    t0 = time.time(); cnt = 0; sat = []
    for v, w in planes(n):
        first = (v << 1, w << 1)
        st, res = mc_le_fixed_first(F, n, k, first, proof=bool(drat_dir))
        cnt += 1
        if st == "SAT":
            sat.append((v, w, res)); print("SAT", hex(g), v, w, res, flush=True); break
        if st != "UNSAT":
            print("UNEXPECTED", st, v, w, flush=True); sys.exit(2)
        if drat_dir:
            e, A, B, O = encode(F, n, k)
            for j, x in enumerate(A[0]): e.cl.append([x] if ((first[0] >> j) & 1) else [-x])
            for j, x in enumerate(B[0]): e.cl.append([x] if ((first[1] >> j) & 1) else [-x])
            base = os.path.join(drat_dir, f"{g:08x}_{v}_{w}")
            with open(base + ".cnf", "w") as f:
                f.write(f"p cnf {e.nv} {len(e.cl)}\n" + "".join(" ".join(map(str, c)) + " 0\n" for c in e.cl))
            with open(base + ".drat", "w") as f:
                f.write("\n".join(res) + "\n")
    print(f"g={g:#010x} planes_checked={cnt} result={'MC(yg)<=4' if sat else 'ALL_UNSAT => MC(yg)>=5'} time={time.time()-t0:.1f}s", flush=True)

if __name__ == "__main__":
    main()
