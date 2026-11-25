"""SAT-free lower bound MC(F) >= 4 for F = y*g* via the two-direction criterion.

If MC(F) <= 3 (and F has degree 4, so every 3-AND circuit is non-degenerate), the first gate a*b has input forms
with distinct directions v_a != v_b, and restricting either form to a constant kills the gate. Hence all four
restrictions F|{<v_a,x>=c}, F|{<v_b,x>=c} have MC <= 2. So if at most one direction v has MC(F|{<v,x>=c}) <= 2
for both c, then MC(F) >= 4. MC <= 2 on 5 variables is decided exhaustively by verify_s2_5.in_S2 (no SAT)."""
import sys, time
sys.path.insert(0, ".")
import dpdt
from verify_s2_5 import in_S2
g = int(sys.argv[1], 16)
F6 = sum(1 << p for p in range(64) if (p >> 5) & 1 and (g >> (p & 31)) & 1)
admissible = []
t = time.time()
for v, (l0, l1) in zip(range(1, 64), dpdt.hyperplane_index_lists(6)):
    r0, r1 = in_S2(dpdt.restrict(F6, l0)), in_S2(dpdt.restrict(F6, l1))
    if r0 is not None and r1 is not None:
        admissible.append((v, r0, r1))
print(f"g={g:#010x}: directions v (bit j = x_(j+1), bit 5 = y) with both restrictions in S_2: {admissible} ({time.time()-t:.0f}s)")
print("CONCLUSION:", "MC(y*g) >= 4 (at most one admissible direction)" if len(admissible) <= 1 else "criterion inconclusive")
