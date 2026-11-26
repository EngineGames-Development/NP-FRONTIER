"""EXP-019: for every HARD codimension-4 instance printed by codim4.c, decide MC(Phi|C) <= 4 by SAT (mc.py, cycle 001),
after reduction modulo affine functions (MC is invariant under adding affine functions). Every circuit found is
re-evaluated. A table without a 4-gate circuit would be a level-5 counterexample (MC = 5, since the formal circuit
has 5 gates) and is reported. Usage: python3 hard_check.py infile [outjson]"""
import sys, os, time, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "EXP-001-mc-exact"))
from mc import mc_le, evaluate
def red_mod_affine(t, n=6):
    a = [(t >> i) & 1 for i in range(1 << n)]
    for i in range(n):
        for x in range(1 << n):
            if (x >> i) & 1: a[x] ^= a[x ^ (1 << i)]
    for x in range(1 << n):
        if bin(x).count('1') <= 1: a[x] = 0
    for i in range(n):
        for x in range(1 << n):
            if (x >> i) & 1: a[x] ^= a[x ^ (1 << i)]
    return sum(a[x] << x for x in range(1 << n))
def _main():
  tabs = set()
  for line in open(sys.argv[1]):
      if line.startswith('HARD'):
          tabs.add(red_mod_affine(int(line.split('tab')[1].split()[0], 16)))
  print("distinct HARD functions mod affine:", len(tabs), flush=True)
  res = []; bad = 0; t00 = time.time()
  for t in sorted(tabs):
      t0 = time.time(); c = mc_le(t, 6, 4)
      ok = c is not None and evaluate(c, 6) == t
      if not ok: bad += 1; print("NO 4-GATE CIRCUIT FOUND:", hex(t), flush=True)
      res.append({"table": hex(t), "mc_le_4": ok, "circuit": c, "sec": round(time.time() - t0, 3)})
  if len(sys.argv) > 2: json.dump(res, open(sys.argv[2], "w"))
  print(f"checked {len(res)}, without a 4-gate circuit: {bad}, {time.time()-t00:.0f}s; max {max(r['sec'] for r in res) if res else 0}s per table")

if __name__ == "__main__":
  _main()
