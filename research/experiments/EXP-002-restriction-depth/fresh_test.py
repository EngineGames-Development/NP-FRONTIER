"""EXP-003: fresh-variable test in the open regime (MC(g) > D(g)). Decide MC(y*g) <= MC(g) by SAT (no budget).
SAT => counterexample to the fresh-variable lemma (circuit re-verified). UNSAT => MC(y*g) = MC(g)+1 (solver result,
unverified by an independent method)."""
import sys, time
sys.path.insert(0, "../EXP-001-mc-exact")
from mc import mc_le, evaluate
g = int(sys.argv[1], 16); k = int(sys.argv[2])
F6 = sum(1 << p for p in range(64) if (p >> 5) & 1 and (g >> (p & 31)) & 1)   # y = x6
t = time.time(); c = mc_le(F6, 6, k)
print(f"g={g:#010x}: MC(y*g) <= {k}? ->", "SAT (COUNTEREXAMPLE)" if c else "UNSAT", f"{time.time()-t:.0f}s", flush=True)
if c: print("circuit:", c, "verified:", evaluate(c, 6) == F6)
