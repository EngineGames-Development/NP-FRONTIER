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
def top(x): return max(i for i in range(5) if (x >> (2*i)) & 3)
def typ(x):  # pattern of x on its top gate: 1 = A-bit only, 2 = B-bit only, 3 = both
    k = top(x); return (x >> (2*k)) & 3
C = Counter()
for line in open(sys.argv[1]):
    if not line.startswith('HARD'): continue
    al, be, gm, h, c0, c = parse(line)
    H = span(h); H0 = [x for x in H if x and (x >> 8) & 3 == 0]
    P = [(x & -x).bit_length() - 1 for x in h]
    off = lambda cc: sum(1 << P[i] for i in range(4) if (cc >> i) & 1)
    dlt = off(c0) ^ off(c)
    sep = [x for x in H0 if bin(x & dlt).count('1') % 2]; non = [x for x in H0 if x not in sep]
    t2 = non[0]
    C[(top(t2), typ(t2), tuple(sorted((top(x), typ(x)) for x in sep)))] += 1
for k, v in sorted(C.items(), key=lambda kv: -kv[1]): print(v, "nonsep t2: top=%d type=%d | separating (top,type): %s" % k)
