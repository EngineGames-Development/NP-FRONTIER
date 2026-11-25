"""Positive controls for cert4b (EXP-010).

(a) F-mode: F = output of a random 4-gate XOR-AND circuit on 6 variables (index bit j = x_{j+1}; bit 5 = y).
    MC(F) <= 4, so cert4b must answer FOUND.
(b) yg-mode: g = output of a random 3-gate circuit on 5 variables; MC(y*g) <= 4, so cert4b must answer FOUND.
Usage: python3 gen_circuit_controls.py SEED COUNT  -> prints two lines: 'F <hex...>' and 'yg <hex...>'.
"""
import random, sys

def var_tables(n):
    N = 1 << n
    return [sum(1 << p for p in range(N) if (p >> j) & 1) for j in range(n)]

def random_circuit(n, k, rng):
    N = 1 << n; full = (1 << N) - 1
    xs = var_tables(n)
    def affine():
        t = full if rng.random() < 0.5 else 0
        for j in range(n):
            if rng.random() < 0.5: t ^= xs[j]
        return t
    gates = []
    for i in range(k):
        def inp():
            t = affine()
            for z in gates:
                if rng.random() < 0.5: t ^= z
            return t
        gates.append(inp() & inp())
    out = affine() ^ gates[-1]
    for z in gates[:-1]:
        if rng.random() < 0.5: out ^= z
    return out

if __name__ == "__main__":
    seed, count = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    F = [random_circuit(6, 4, rng) for _ in range(count)]
    G = [random_circuit(5, 3, rng) for _ in range(count)]
    print("F " + " ".join(hex(f) for f in F))
    print("yg " + " ".join(hex(g) for g in G))
