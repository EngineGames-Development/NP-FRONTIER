"""EXP-014: table-free MC <= 3 test (SAT via mc.py, cycle 001; every circuit re-verified by mc.evaluate).
Usage: python3 mc3_check_n.py N infile outjson   (infile lines: 'hex_table other')"""
import sys, os, time, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-001-mc-exact"))
from mc import mc_le, evaluate
n = int(sys.argv[1]); res = []; bad = 0; t00 = time.time()
for line in open(sys.argv[2]):
    h = line.split()[0]; t = int(h, 16); t0 = time.time()
    c = mc_le(t, n, 3)
    ok = c is not None and evaluate(c, n) == t
    bad += not ok
    res.append({"table": h, "mc_le_3": ok, "circuit": c, "sec": round(time.time() - t0, 3)})
    if not ok: print("NO 3-GATE CIRCUIT:", h, flush=True)
json.dump(res, open(sys.argv[3], "w"))
print(f"n={n} checked {len(res)} tables, without 3-gate circuit: {bad}, total {time.time()-t00:.0f}s")
