"""EXP-019: parallel version of hard_check.py. Deduplicate HARD tables modulo affine functions, split them into
NPROC chunks, and SAT-check each chunk for a 4-gate circuit in its own process (mc.py; every circuit re-evaluated).
Usage: python3 hard_check_par.py infile outjson [nproc]"""
import sys, os, json, time
from multiprocessing import Pool
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-001-mc-exact"))
from hard_check import red_mod_affine
def work(t):
    from mc import mc_le, evaluate
    t0 = time.time(); c = mc_le(t, 6, 4)
    ok = c is not None and evaluate(c, 6) == t
    return {"table": hex(t), "mc_le_4": ok, "circuit": c, "sec": round(time.time() - t0, 3)}
if __name__ == '__main__':
    tabs = sorted({red_mod_affine(int(l.split('tab')[1].split()[0], 16)) for l in open(sys.argv[1]) if l.startswith('HARD')})
    print("distinct HARD functions mod affine:", len(tabs), flush=True)
    t00 = time.time()
    with Pool(int(sys.argv[3]) if len(sys.argv) > 3 else 4) as pool:
        res = pool.map(work, tabs, chunksize=1)
    bad = [r for r in res if not r["mc_le_4"]]
    for r in bad: print("NO 4-GATE CIRCUIT FOUND:", r["table"], flush=True)
    json.dump(res, open(sys.argv[2], "w"))
    print(f"checked {len(res)}, without a 4-gate circuit: {len(bad)}, {time.time()-t00:.0f}s wall; max {max(r['sec'] for r in res) if res else 0}s per table")
