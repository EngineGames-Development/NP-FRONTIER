"""General first-gate extension test: does F = y*g (6 vars) have a 3-AND circuit?
Step 1: admissible directions = those v with MC(F|<v,x>=c) <= 2 for both c (exhaustive, no SAT).
Step 2: every non-degenerate first gate is (<v,x>+e)(<w,x>+e') with v != w admissible; for each, test exhaustively
whether two more AND gates finish F. Stops at the first extension found. Used as positive control (expect FOUND)
and as the certificate for g* (expect NONE)."""
import sys, time, itertools
import numpy as np
sys.path.insert(0, ".")
import dpdt
from verify_s2_5 import in_S2
from first_gate_extension import echelon, reduce_vec, elements, reduce_np   # module guard below
N = 64; ONE = (1 << N) - 1
var = [sum(1 << p for p in range(N) if p >> j & 1) for j in range(6)]
def form(v): return sum((var[j] for j in range(6) if v >> j & 1), 0) if v else 0
def lin(v):
    r = 0
    for j in range(6):
        if v >> j & 1: r ^= var[j]
    return r
def extends(F, z1):
    B1 = echelon([ONE] + var + [z1]); W1 = elements(B1); seen = set()
    for i, j in itertools.combinations(range(len(W1)), 2):
        r = reduce_vec(W1[i] & W1[j], B1)
        if r == 0 or r in seen: continue
        seen.add(r)
        B2 = echelon([v for _, v in B1] + [r]); W2 = np.array(elements(B2), dtype=np.uint64)
        ii, jj = np.triu_indices(len(W2), 1)
        if (reduce_np((W2[ii] & W2[jj]) ^ np.uint64(F), B2) == 0).any() or reduce_vec(F, B2) == 0: return True
    return False
g = int(sys.argv[1], 16)
F = sum(1 << p for p in range(N) if (p >> 5) & 1 and (g >> (p & 31)) & 1)
t = time.time()
adm = [v for v, (l0, l1) in zip(range(1, 64), dpdt.hyperplane_index_lists(6))
       if in_S2(dpdt.restrict(F, l0)) is not None and in_S2(dpdt.restrict(F, l1)) is not None]
print(f"g={g:#010x}: admissible directions {adm} ({time.time()-t:.0f}s)", flush=True)
DISTINCT_X = "--distinct-x" in sys.argv   # Lemma 12: first-gate directions have distinct x-parts (bits 0..4)
for v, w in itertools.combinations(adm, 2):
    if DISTINCT_X and (v & 31) == (w & 31): continue
    for e, e2 in itertools.product((0, 1), repeat=2):
        z1 = (lin(v) ^ (ONE if e else 0)) & (lin(w) ^ (ONE if e2 else 0))
        if extends(F, z1):
            print(f"FOUND: first gate (<{v}>+{e})(<{w}>+{e2}) extends to a 3-AND circuit ({time.time()-t:.0f}s)"); sys.exit(0)
print(f"NONE: no first gate extends; MC(y*g) >= 4 ({time.time()-t:.0f}s)")
