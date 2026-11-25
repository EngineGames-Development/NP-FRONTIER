"""EXP-005. For 5-variable g with MC(g) = 3: A_g = {v != 0 : both restrictions g|<v,x>=c have MC <= 1} (exact 4-variable
MC table, EXP-001). Lemma 12: if MC(y*g) = 3 then |A_g| >= 2. So |A_g| <= 1 proves MC(y*g) = 4 = MC(g)+1.
Part 1: the 38 certified MC-3 functions of EXP-002. Part 2: random search for MC-3 functions with |A_g| >= 2
(MC >= 3 certified by the exhaustive SAT-free S_2 test)."""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "EXP-002-restriction-depth")); sys.path.insert(0, os.path.join(HERE, "..", "EXP-001-mc-exact"))
import dpdt
from verify_s2_5 import in_S2
mc4 = json.load(open(os.path.join(HERE, "..", "EXP-001-mc-exact", "mc4.json")))["mc"]
L5 = dpdt.hyperplane_index_lists(5)
def A(g): return [v for v, (l0, l1) in zip(range(1, 32), L5) if mc4[dpdt.restrict(g, l0)] <= 1 and mc4[dpdt.restrict(g, l1)] <= 1]
d = json.load(open(os.path.join(HERE, "..", "EXP-002-restriction-depth", "sample5_results.json")))
gs = sorted({o["F"] for o in d if o["status_at_D"] == "UNSAT"})
sizes = {g: A(g) for g in gs}
from collections import Counter
print("Part 1: |A_g| distribution over the 38 certified MC-3 functions:", sorted(Counter(len(a) for a in sizes.values()).items()))
print("  functions with |A_g| >= 2:", [hex(g) for g, a in sizes.items() if len(a) >= 2])
# Part 2: random multiplexers along x1 with MC<=1 halves; keep those with MC >= 3 and |A| >= 2
r = random.Random(7); mc1 = [f for f in range(1 << 16) if mc4[f] <= 1]
hits, tried, mc3 = [], 0, 0
while tried < 4000 and len(hits) < 5:
    tried += 1
    p, q = r.choice(mc1), r.choice(mc1)
    g = 0
    for x in range(32):                     # x1 = bit 0 is the selector; halves act on bits 1..4
        h = q if x & 1 else p
        g |= ((h >> (x >> 1)) & 1) << x
    a = A(g)
    if len(a) >= 2 and in_S2(g) is None:
        hits.append((hex(g), a))
    if in_S2(g) is None: mc3 += 1
print(f"Part 2: {tried} random multiplexers; with MC >= 3: {mc3}; with MC >= 3 and |A| >= 2: {len(hits)} {hits}")
