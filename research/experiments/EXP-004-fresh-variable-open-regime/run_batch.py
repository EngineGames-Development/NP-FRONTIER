"""EXP-004: test PNE-001 on every sampled 5-variable g with MC(g) = 3 > D(g) = 2 (EXP-002, all 38 independently
confirmed). For each g: (1) find a 3-AND circuit for g (re-verified) so MC(g) = 3; (2) run the SAT-free first-gate
certificate on F = y*g: 'NONE' proves MC(y*g) = 4 = MC(g)+1; 'FOUND' would refute PNE-001; timeout = inconclusive."""
import json, os, subprocess, sys
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); EXP2 = os.path.join(HERE, "..", "EXP-002-restriction-depth")
sys.path.insert(0, os.path.join(HERE, "..", "EXP-001-mc-exact"))
from mc import mc_le, evaluate
def work(F):
    c = mc_le(F, 5, 3)
    if c is None: return {"g": F, "mc_g": ">3", "result": "skip"}
    assert evaluate(c, 5) == F
    try:
        out = subprocess.run([sys.executable, "-u", "first_gate_general.py", hex(F)], cwd=EXP2, capture_output=True,
                             text=True, timeout=900).stdout.strip().splitlines()
        res = out[-1].split(":")[0] if out else "error"
        adm = out[0].split("admissible directions ")[1].split(" (")[0] if out else ""
    except subprocess.TimeoutExpired:
        res, adm = "TIMEOUT", ""
    return {"g": F, "mc_g": 3, "circuit_g": c, "admissible": adm, "result": res}
if __name__ == "__main__":
    d = json.load(open(os.path.join(EXP2, "sample5_results.json")))
    gs = sorted({o["F"] for o in d if o["status_at_D"] == "UNSAT"})
    res = []
    with Pool(3) as pool:
        for r in pool.imap_unordered(work, gs):
            res.append(r); print(f"{len(res)}/{len(gs)} g={r['g']:#010x} admissible={r.get('admissible')} -> {r['result']}", flush=True)
            json.dump(res, open(os.path.join(HERE, "results.json"), "w"))
    from collections import Counter
    print("SUMMARY:", Counter(r["result"] for r in res))
