"""EXP-014: exact MC <= 3 test (SAT, mc.py encoding from cycle 001) for the 72 distinct non-degenerate
k=6 survivor functions.  Every SAT answer is re-verified by mc.evaluate (independent of the encoding)."""
import sys, os, time, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-001-mc-exact"))
from mc import mc_le, evaluate
res = []
for line in open(sys.argv[1]):
    h, d = line.split(); t = int(h, 16); t0 = time.time()
    c = mc_le(t, 6, 3)
    ok = c is not None and evaluate(c, 6) == t
    res.append({"table": h, "deg": int(d), "mc_le_3": ok, "circuit": c, "sec": round(time.time() - t0, 2)})
    print(h, d, "MC<=3" if ok else "NO 3-GATE CIRCUIT", res[-1]["sec"], flush=True)
json.dump(res, open(sys.argv[2], "w"), indent=1)
print("all MC<=3:", all(r["mc_le_3"] for r in res), "count", len(res))
