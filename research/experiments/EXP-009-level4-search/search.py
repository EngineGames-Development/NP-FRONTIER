"""EXP-009: counterexample search for PNE-001 at level 4 on 5 variables.
For an orbit representative g (MC(g) = 4, from EXP-008) and F = y*g on 6 variables (y = x6):
 - cheap directions of g at level 4: v with both halves of MC <= 2 (exact 4-variable table);
 - cheap planes: span(v,w) with v, w, v^w cheap;
 - by Lemma 9' + Lemma 20, any 4-gate circuit for F has first gate (l1 + s1*y)(l2 + s2*y) modulo affine terms,
   where span(l1,l2) is a cheap plane and (s1,s2) in F_2^2 (the 4 lifts);
 - for each such first gate, SAT asks for a completion with 3 more gates (conflict budget).
SAT => counterexample (circuit re-verified by mc.evaluate).  UNSAT => no circuit with that first gate.
UNKNOWN => budget exhausted.  Usage: python3 search.py <rep_file> <start> <count> <budget>"""
import json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "EXP-001-mc-exact")); sys.path.insert(0, os.path.join(HERE, "..", "EXP-002-restriction-depth"))
import dpdt
from mc import mc_le_fixed_first, evaluate
mc4 = json.load(open(os.path.join(HERE, "..", "EXP-001-mc-exact", "mc4.json")))["mc"]
L5 = dpdt.hyperplane_index_lists(5)
def cheap_dirs(g): return [v for v, (l0, l1) in zip(range(1, 32), L5) if mc4[dpdt.restrict(g, l0)] <= 2 and mc4[dpdt.restrict(g, l1)] <= 2]
def cheap_planes(A):
    S = set(A); planes = set()
    for v in A:
        for w in A:
            if v < w and (v ^ w) in S: planes.add(tuple(sorted((v, w, v ^ w))))
    return sorted(planes)
def run(g, budget):
    F = sum(1 << p for p in range(64) if (p >> 5) & 1 and (g >> (p & 31)) & 1)
    A = cheap_dirs(g); P = cheap_planes(A); res = []
    for (v, w, _) in P:
        for s1 in (0, 1):
            for s2 in (0, 1):
                am = (v << 1) | (s1 << 6); bm = (w << 1) | (s2 << 6)       # wire masks: bit0 = 1, bits1..5 = x1..x5, bit6 = y
                t = time.time(); st, c = mc_le_fixed_first(F, 6, 4, (am, bm), budget=budget)
                res.append({"plane": [v, w], "lift": [s1, s2], "status": st, "secs": round(time.time() - t, 1), "circuit": c if st == "SAT" else None})
                if st == "SAT":
                    assert evaluate(c, 6) == F
                    return {"g": g, "cheap_dirs": A, "planes": P, "results": res, "COUNTEREXAMPLE": True}
    return {"g": g, "cheap_dirs": A, "planes": P, "results": res, "COUNTEREXAMPLE": False}
if __name__ == "__main__":
    reps = [int(l.split()[0], 16) for l in open(sys.argv[1])]
    start, count, budget = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    out = []
    for g in reps[start:start + count]:
        r = run(g, budget); out.append(r)
        sts = [x["status"] for x in r["results"]]
        print(f"g={g:#010x} planes={len(r['planes'])} SAT={sts.count('SAT')} UNSAT={sts.count('UNSAT')} UNKNOWN={sts.count('UNKNOWN')}"
              + ("  *** COUNTEREXAMPLE ***" if r["COUNTEREXAMPLE"] else ""), flush=True)
        json.dump(out, open(os.path.join(HERE, f"results_{start}_{count}.json"), "w"))
