"""EXP-006 step 2: for each of the 33 orbit representatives G' (Theorem 16 family):
 (a) MC(G') = 3?  (G' is never in S_2 iff MC >= 3; MC <= 3 holds by construction: z1 = x1*l3, z2 = x2*(l2 + z1), z3 = x1*l1)
 (b) if so, decide MC(y*G') >= 4 by the first-gate certificate (Lemma 9), skipping first gates whose two directions
     share their x-part (Lemma 12). 'NONE' proves MC(y*G') = 4; 'FOUND' would be a counterexample to PNE-001.
S_2 for 5 variables is precomputed exhaustively as a sorted array (all W2 = W1 + span{A*B}, A,B in W1, over all W1)."""
import itertools, json, os, sys, time
import numpy as np
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); EXP2 = os.path.join(HERE, "..", "EXP-002-restriction-depth")
sys.path.insert(0, EXP2)
import dpdt
from first_gate_extension import echelon, reduce_vec, elements, reduce_np
X5 = [sum(1 << p for p in range(32) if p >> j & 1) for j in range(5)]; ONE5 = (1 << 32) - 1
def build_S2():
    W0 = elements(echelon([ONE5] + X5))
    W1s = {}
    for a, b in itertools.combinations(W0, 2):
        z = a & b
        B1 = echelon([ONE5] + X5 + [z])
        if len(B1) == 7: W1s[tuple(sorted(elements(B1)))] = 1
    chunks = [np.array(W0, dtype=np.uint32)]
    for W1 in W1s:
        w = np.array(W1, dtype=np.uint32); chunks.append(w)
        ii, jj = np.triu_indices(len(w), 1)
        z2 = np.unique(w[ii] & w[jj])
        chunks.append((w[None, :] ^ z2[:, None]).ravel())
    return np.unique(np.concatenate(chunks))
S2 = None
def in_S2_fast(f): i = np.searchsorted(S2, f); return i < len(S2) and S2[i] == f
N6 = 64; ONE6 = (1 << 64) - 1; var6 = [sum(1 << p for p in range(N6) if p >> j & 1) for j in range(6)]
def lin6(v): r = 0; [r := r ^ var6[j] for j in range(6) if v >> j & 1]; return r
def extends(F, z1):
    B1 = echelon([ONE6] + var6 + [z1]); W1 = elements(B1); seen = set()
    for i, j in itertools.combinations(range(len(W1)), 2):
        r = reduce_vec(W1[i] & W1[j], B1)
        if r == 0 or r in seen: continue
        seen.add(r)
        B2 = echelon([v for _, v in B1] + [r]); W2 = np.array(elements(B2), dtype=np.uint64)
        ii, jj = np.triu_indices(len(W2), 1)
        if (reduce_np((W2[ii] & W2[jj]) ^ np.uint64(F), B2) == 0).any() or reduce_vec(F, B2) == 0: return True
    return False
def work(g):
    t = time.time()
    if in_S2_fast(g): return {"g": g, "mc": "<=2", "result": "not MC 3"}
    F = sum(1 << p for p in range(N6) if (p >> 5) & 1 and (g >> (p & 31)) & 1)
    adm = [v for v, (l0, l1) in zip(range(1, 64), dpdt.hyperplane_index_lists(6))
           if in_S2_fast(dpdt.restrict(F, l0)) and in_S2_fast(dpdt.restrict(F, l1))]
    gates = 0
    for v, w in itertools.combinations(adm, 2):
        if (v & 31) == (w & 31): continue                      # Lemma 12
        for e, e2 in itertools.product((0, 1), repeat=2):
            gates += 1
            z1 = (lin6(v) ^ (ONE6 if e else 0)) & (lin6(w) ^ (ONE6 if e2 else 0))
            if extends(F, z1): return {"g": g, "mc": 3, "admissible": adm, "result": "FOUND", "gate": [v, e, w, e2]}
    return {"g": g, "mc": 3, "admissible": adm, "first_gates_checked": gates, "result": "NONE", "secs": round(time.time() - t)}
def init(s2):
    global S2; S2 = s2
if __name__ == "__main__":
    t = time.time(); s2 = build_S2(); np.save(os.path.join(HERE, "S2_5vars.npy"), s2)
    print(f"|S_2| (5 variables, MC <= 2) = {len(s2)} ({time.time()-t:.0f}s)", flush=True)
    reps = json.load(open(os.path.join(HERE, "orbits.json")))["reps"]
    out = []
    with Pool(int(sys.argv[1]) if len(sys.argv) > 1 else 3, initializer=init, initargs=(s2,)) as pool:
        for r in pool.imap_unordered(work, reps):
            out.append(r); print(f"{len(out)}/{len(reps)} g={r['g']:#010x} -> {r['result']} {r.get('admissible','')} {r.get('first_gates_checked','')} {r.get('secs','')}", flush=True)
            json.dump(out, open(os.path.join(HERE, "results.json"), "w"))
    from collections import Counter
    print("SUMMARY:", Counter(r["result"] for r in out), flush=True)
