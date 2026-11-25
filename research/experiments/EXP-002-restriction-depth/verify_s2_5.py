"""Independent exhaustive check (no SAT): is f computable with <= 2 AND gates on 5 variables?
f in S_2  <=>  exists W_1 = span{1,x} + span{a*b} (a,b affine) and z2 = A*B (A,B in W_1) with f in W_1 + span{z2}."""
import itertools, json, sys
N = 32; ONE = (1 << N) - 1
X = [sum(1 << p for p in range(N) if p >> j & 1) for j in range(5)]
def span(gens):
    s = {0}
    for g in gens: s |= {v ^ g for v in s}
    return frozenset(s)
W0 = span([ONE] + X)
W1s = {frozenset(W0 | {v ^ (a & b) for v in W0}) for a, b in itertools.combinations(sorted(W0), 2) if (a & b) not in W0}
def in_S2(f):
    if f in W0: return "S0"
    for W1 in W1s:
        if f in W1: return "S1"
    for W1 in W1s:
        L = sorted(W1)
        for a, b in itertools.combinations(L, 2):
            if (f ^ (a & b)) in W1: return "S2"
    return None
if __name__ == "__main__":
    print("distinct W1 spaces:", len(W1s))
    d = json.load(open("sample5_results.json"))
    for o in d:
        if o["status_at_D"] == "UNSAT":
            r = in_S2(o["F"]); print(f"F={o['F']:#010x} deg={o['deg']} D={o['D']}: exhaustive S_2 membership -> {r}")
