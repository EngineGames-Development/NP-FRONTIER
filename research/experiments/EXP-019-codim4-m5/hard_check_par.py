"""EXP-019: parallel, resumable SAT check of HARD codimension-4 functions. Deduplicates HARD tables modulo affine
functions, skips tables already present in the output JSON-lines file, and checks the rest for a 4-gate circuit
(mc.py, every circuit re-evaluated), appending one JSON line per table as soon as it is done.
Usage: python3 hard_check_par.py infile out.jsonl [nproc]"""
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
    done = set()
    if os.path.exists(sys.argv[2]):
        for l in open(sys.argv[2]):
            if l.strip(): done.add(int(json.loads(l)["table"], 16))
    todo = [t for t in tabs if t not in done]
    print(f"distinct HARD functions mod affine: {len(tabs)}; already done: {len(done)}; to do: {len(todo)}", flush=True)
    t00 = time.time(); bad = 0; n = 0
    with Pool(int(sys.argv[3]) if len(sys.argv) > 3 else 4) as pool, open(sys.argv[2], "a") as out:
        for r in pool.imap_unordered(work, todo, chunksize=1):
            out.write(json.dumps(r) + "\n"); out.flush(); n += 1
            if not r["mc_le_4"]: bad += 1; print("NO 4-GATE CIRCUIT FOUND:", r["table"], flush=True)
            if n % 200 == 0: print(f"  {n}/{len(todo)} done, {time.time()-t00:.0f}s", flush=True)
    print(f"finished: {n} checked this run, without a 4-gate circuit: {bad}, {time.time()-t00:.0f}s wall", flush=True)
