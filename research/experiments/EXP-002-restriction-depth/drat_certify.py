"""Re-solve 'MC(y*g) <= k' with DRAT proof logging; write DIMACS + proof for independent checking by drat-trim.
Usage: python3 drat_certify.py <g-hex> <k> <tag>   then   drat-trim <tag>.cnf <tag>.drat"""
import sys
sys.path.insert(0, "../EXP-001-mc-exact")
from mc import encode
from pysat.solvers import Cadical153
g = int(sys.argv[1], 16); k = int(sys.argv[2]); tag = sys.argv[3]
F6 = sum(1 << p for p in range(64) if (p >> 5) & 1 and (g >> (p & 31)) & 1)
e, *_ = encode(F6, 6, k)
with open(f"{tag}.cnf", "w") as f:
    f.write(f"p cnf {e.nv} {len(e.cl)}\n")
    for c in e.cl: f.write(" ".join(map(str, c)) + " 0\n")
with Cadical153(bootstrap_with=e.cl, with_proof=True) as s:
    r = s.solve(); print("solver result:", "SAT" if r else "UNSAT", flush=True)
    if not r:
        with open(f"{tag}.drat", "w") as f:
            for line in s.get_proof(): f.write(line + "\n")
        print("proof written", flush=True)
