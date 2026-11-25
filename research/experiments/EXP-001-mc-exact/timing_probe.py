import sys, time; sys.path.insert(0, ".")
from mc import mc_le, tt
probes = [("AND5 k=3", tt(lambda x: all(x), 5), 5, 3),
          ("x1x2x3*y + x1x4*y (5 vars) k=2", tt(lambda x: ((x[0]&x[1]&x[2]) ^ (x[0]&x[3])) & x[4], 5), 5, 2),
          ("IP6 k=2", tt(lambda x: (x[0]&x[1]) ^ (x[2]&x[3]) ^ (x[4]&x[5]), 6), 6, 2)]
for name, F, n, k in probes:
    t = time.time(); c = mc_le(F, n, k); print(f"{name}: {'SAT' if c else 'UNSAT'} {time.time()-t:.1f}s", flush=True)
