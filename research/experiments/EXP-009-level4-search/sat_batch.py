"""EXP-009b: counterexample search over all 297 orbit representatives (EXP-008): SAT "MC(y*g) <= 4" on 6 variables,
no fixed first gate, conflict budget per instance. SAT = counterexample (circuit re-verified by mc.evaluate);
UNKNOWN = budget exhausted (inconclusive); UNSAT = no 4-AND circuit (solver claim; not used as a proof here)."""
import json, os, sys, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "EXP-001-mc-exact"))
import mc as mcmod
from pysat.solvers import Cadical153
BUDGET = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
def work(g):
    F = sum(1 << p for p in range(64) if (p >> 5) & 1 and (g >> (p & 31)) & 1)
    e, A, B, O = mcmod.encode(F, 6, 4); t = time.time()
    with Cadical153(bootstrap_with=e.cl) as s:
        s.conf_budget(BUDGET); r = s.solve_limited()
        if r is None: return {"g": g, "status": "UNKNOWN", "secs": round(time.time() - t, 1)}
        if not r: return {"g": g, "status": "UNSAT", "secs": round(time.time() - t, 1)}
        m = set(l for l in s.get_model() if l > 0)
    mask = lambda C: sum(1 << j for j, v in enumerate(C) if v in m)
    circ = ([(mask(A[i]), mask(B[i])) for i in range(4)], mask(O))
    ok = mcmod.evaluate(circ, 6) == F
    return {"g": g, "status": "SAT" if ok else "BUG", "circuit": circ, "secs": round(time.time() - t, 1)}
if __name__ == "__main__":
    reps = [int(l.split()[0], 16) for l in open(os.path.join(HERE, "..", "EXP-008-level4-five-variables", "orbit_reps.txt"))]
    out = []
    with Pool(3) as pool:
        for r in pool.imap_unordered(work, reps):
            out.append(r); print(f"{len(out)}/{len(reps)} g={r['g']:#010x} {r['status']} {r['secs']}s" + ("  *** COUNTEREXAMPLE ***" if r["status"] == "SAT" else ""), flush=True)
            json.dump(out, open(os.path.join(HERE, f"sat_batch_{BUDGET}.json"), "w"))
    from collections import Counter
    print("SUMMARY:", Counter(r["status"] for r in out), flush=True)
