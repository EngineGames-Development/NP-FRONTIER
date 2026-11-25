"""EXP-002b: for 5-variable functions, is MC(f) = D(f)?  A circuit with D(f) ANDs certifies MC = D (since D <= MC).
Budget-limited SAT: 'SAT' = certified MC = D; 'UNKNOWN' = no circuit found within the budget (candidate MC > D)."""
import json, os, random, sys, time
from multiprocessing import Pool
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-001-mc-exact"))
import dpdt
from mc import degree, evaluate
import mc as mcmod
from pysat.solvers import Cadical153

dpdt._tables[4] = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "D4.json")))["D4"]
for n in (1, 2, 3): dpdt.build_table(n)

def mc_le_budget(F, n, k, budget):
    orig = Cadical153
    class Budgeted(orig):
        def solve(self, *a, **kw):
            self.conf_budget(budget); r = self.solve_limited()
            if r is None: raise TimeoutError
            return r
    try:
        c = mcmod.mc_le(F, n, k, solver_cls=Budgeted)
        return ("SAT", c) if c else ("UNSAT", None)
    except TimeoutError:
        return ("UNKNOWN", None)

def work(args):
    kind, F = args
    d = dpdt.D(F, 5); deg = degree(F, 5); t = time.time()
    st, c = mc_le_budget(F, 5, d, 300000) if d > 0 else ("SAT", None)
    return {"kind": kind, "F": F, "deg": deg, "D": d, "status_at_D": st, "secs": round(time.time() - t, 2),
            "circuit": c}

def rand_deg_le(r, dmax):
    # random function of degree <= dmax via random ANF on monomials of size <= dmax
    anf = [p for p in range(32) if bin(p).count("1") <= dmax and r.random() < 0.5]
    F = 0
    for x in range(32):
        v = 0
        for p in anf:
            if p & x == p: v ^= 1
        F |= v << x
    return F

if __name__ == "__main__":
    r = random.Random(20261125)
    jobs = [("uniform", r.getrandbits(32)) for _ in range(150)]
    jobs += [("deg<=4", rand_deg_le(r, 4)) for _ in range(150)]
    jobs += [("deg<=3", rand_deg_le(r, 3)) for _ in range(150)]
    out = []
    with Pool(3) as pool:
        for i, res in enumerate(pool.imap_unordered(work, jobs)):
            out.append(res)
            if (i + 1) % 25 == 0:
                print(f"{i+1}/{len(jobs)} done; unknown so far: {sum(o['status_at_D']=='UNKNOWN' for o in out)}", flush=True)
                json.dump(out, open("sample5_results.json", "w"))
    json.dump(out, open("sample5_results.json", "w"))
    from collections import Counter
    print(Counter((o["kind"], o["deg"], o["D"], o["status_at_D"]) for o in out))
