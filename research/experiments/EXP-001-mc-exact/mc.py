"""Exact multiplicative complexity (MC) of small Boolean functions via SAT.

MC(f) = min number of AND gates in a circuit over {AND, XOR, 1} computing f (XOR and constants free).
A k-AND circuit: wires w_0 = 1, w_1..w_n = inputs, w_{n+i} = z_i (i = 1..k), where
    z_i = A_i * B_i,  A_i, B_i = XOR of a subset of wires w_0 .. w_{n+i-1},
    output = XOR of a subset of wires w_0 .. w_{n+k}.
Truth tables are ints: bit p of F is F(x) where x_j = bit (j-1) of p.
Every circuit returned by the solver is re-checked by `evaluate` (independent of the encoding).
"""
from itertools import count
from pysat.solvers import Cadical153

def evaluate(circ, n):
    """circ = (gates, out): gates[i] = (Amask, Bmask) over wires, out = mask. Returns truth table int."""
    gates, out = circ
    tt = 0
    for p in range(1 << n):
        w = [1] + [(p >> j) & 1 for j in range(n)]
        for (am, bm) in gates:
            a = sum(w[j] for j in range(len(w)) if am >> j & 1) & 1
            b = sum(w[j] for j in range(len(w)) if bm >> j & 1) & 1
            w.append(a & b)
        if sum(w[j] for j in range(len(w)) if out >> j & 1) & 1:
            tt |= 1 << p
    return tt

class _Enc:
    def __init__(self):
        self.nv = 0; self.cl = []
    def new(self):
        self.nv += 1; return self.nv
    def and2(self, a, b):                      # t <-> a & b
        t = self.new(); self.cl += [[-t, a], [-t, b], [t, -a, -b]]; return t
    def xor_list(self, lits, rhs=None):
        """Return a literal equal to XOR(lits) (None if lits empty -> constant 0), or force XOR(lits) = rhs."""
        acc = None
        for l in lits:
            if acc is None: acc = l; continue
            y = self.new()
            self.cl += [[-y, acc, l], [-y, -acc, -l], [y, -acc, l], [y, acc, -l]]
            acc = y
        if rhs is None: return acc
        if acc is None:
            if rhs: self.cl.append([])         # 0 = 1: unsatisfiable
            return None
        self.cl.append([acc] if rhs else [-acc]); return None

def mc_le(F, n, k, solver_cls=Cadical153):
    """Return a k-AND circuit computing F (re-verified), or None if none exists."""
    e, A, B, O = encode(F, n, k)
    with solver_cls(bootstrap_with=e.cl) as s:
        if not s.solve(): return None
        m = set(l for l in s.get_model() if l > 0)
    mask = lambda C: sum(1 << j for j, v in enumerate(C) if v in m)
    circ = ([(mask(A[i]), mask(B[i])) for i in range(k)], mask(O))
    assert evaluate(circ, n) == F, "solver circuit failed independent check"
    return circ

def encode(F, n, k):
    """CNF that is satisfiable iff some k-AND circuit (with non-degenerate gates) computes F."""
    N = 1 << n; e = _Enc()
    A = [[e.new() for _ in range(n + 1 + i)] for i in range(k)]
    B = [[e.new() for _ in range(n + 1 + i)] for i in range(k)]
    O = [e.new() for _ in range(n + 1 + k)]
    for i in range(k):                          # inputs non-constant and distinct (safe: padding argument)
        e.cl.append(A[i][1:]); e.cl.append(B[i][1:])
        e.cl.append([e.and2(A[i][j], -B[i][j]) for j in range(n + 1 + i)] +
                    [e.and2(-A[i][j], B[i][j]) for j in range(n + 1 + i)])
    for p in range(N):
        xv = [(p >> j) & 1 for j in range(n)]
        V = []
        for i in range(k):
            def form(C):
                lits = [C[0]] + [C[1 + j] for j in range(n) if xv[j]]
                lits += [e.and2(C[n + 1 + g], V[g]) for g in range(i)]
                return e.xor_list(lits)
            a, b = form(A[i]), form(B[i])
            v = e.new(); e.cl += [[-v, a], [-v, b], [v, -a, -b]]; V.append(v)
        lits = [O[0]] + [O[1 + j] for j in range(n) if xv[j]] + [e.and2(O[n + 1 + g], V[g]) for g in range(k)]
        e.xor_list(lits, rhs=(F >> p) & 1)
    return e, A, B, O

def mc(F, n, kmax=12):
    for k in count(0):
        if k > kmax: raise ValueError("kmax exceeded")
        if k == 0:
            if _is_affine(F, n): return 0, ([], _affine_mask(F, n))
            continue
        c = mc_le(F, n, k)
        if c is not None: return k, c

def _anf(F, n):
    a = [(F >> p) & 1 for p in range(1 << n)]
    for j in range(n):
        for p in range(1 << n):
            if p >> j & 1: a[p] ^= a[p ^ (1 << j)]
    return a

def degree(F, n):
    a = _anf(F, n); return max((bin(p).count("1") for p in range(1 << n) if a[p]), default=-1)

def _is_affine(F, n): return degree(F, n) <= 1

def _affine_mask(F, n):
    a = _anf(F, n); return (a[0]) | sum((a[1 << j]) << (j + 1) for j in range(n))

def tt(fn, n):
    """Truth table of a Python predicate on a bit list."""
    return sum(1 << p for p in range(1 << n) if fn([(p >> j) & 1 for j in range(n)]))
