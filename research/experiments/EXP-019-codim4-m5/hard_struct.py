import sys
from collections import Counter
def parse(line):
    t = line.split()
    al = [0] + list(map(int, t[1:5])); be = [0] + list(map(int, t[5:9])); gm = int(t[9])
    h = list(map(int, t[10:14])); c0 = int(t[15]); c = int(t[17])
    return al, be, gm, h, c0, c
def span(vs):
    S = {0}
    for v in vs: S |= {x ^ v for x in S}
    return S
def rank(vs):
    rows = []
    for v in vs:
        for r in rows:
            if v ^ r < v: v ^= r
        if v: rows.append(v); rows.sort(reverse=True)
    return len(rows)
def top(x):  # 0-indexed gate of highest set coordinate
    return max(i for i in range(5) if (x >> (2*i)) & 3)
C = Counter()
for line in open(sys.argv[1]):
    if not line.startswith('HARD'): continue
    al, be, gm, h, c0, c = parse(line)
    H = span(h)
    pi = {((x >> 8) & 3) for x in H}
    dpi = {1: 0, 2: 1, 4: 2}[len(pi)]
    H0 = [x for x in H if (x >> 8) & 3 == 0 and x]
    # class difference: which h in H0 separate c0 and c (via coset offsets in pivot coordinates)
    P = [ (x & -x).bit_length() - 1 for x in h]
    def off(cc): return sum(1 << P[i] for i in range(4) if (cc >> i) & 1)
    o0, o1 = off(c0), off(c)
    sep = [x for x in H0 if bin(x & (o0 ^ o1)).count('1') % 2]   # H0 functionals that differ between C0 and C
    tops_H0 = sorted({top(x) for x in H0})
    mintop_sep = min(top(x) for x in sep) if sep else None
    C[(dpi, len(H0) and rank(H0), 'sep' if sep else 'same', mintop_sep)] += 1
for k, v in sorted(C.items(), key=lambda kv: -kv[1]): print(v, "dim pi=%d dimH0=%d class=%s min-top-of-separating=%s" % k)
