"""EXP-019: in the double-merge sub-case of NEW-2 with k = m-2 (0-indexed gate 2), compute on C the slice functions
R1' = D_{kappa'} Phi|C (kappa' moves only gate 3's free coordinate), R0' = Phi + R1'*s', and their s_k-coefficients
N_i = D_{kappa_k} R_i' (kappa_k moves only gate 2's free coordinate). Report which saving occurs."""
import sys
from collections import Counter
from new2_check import parse, span, top, evalc, coset
C = Counter()
def solve_uv(base, H):
    for uv in range(4):
        kk = base | (uv << 8)
        if all(bin(x & kk).count('1') % 2 == 0 for x in H): return kk
    return None
for line in open(sys.argv[1]):
    if not line.startswith('HARD'): continue
    al, be, gm, h, c0, c = parse(line)
    H = span(h); H0 = [x for x in H if x and (x >> 8) & 3 == 0]
    Pv = [(x & -x).bit_length() - 1 for x in h]; off = lambda cc: sum(1 << Pv[i] for i in range(4) if (cc >> i) & 1)
    dlt = off(c0) ^ off(c)
    sep = [x for x in H0 if bin(x & dlt).count('1') % 2]; non = [x for x in H0 if x not in sep]
    t2 = non[0]
    if top(t2) != 3: continue
    low = [x for x in sep if top(x) < 3]
    if not low or top(low[0]) != 2: continue
    t1 = low[0]
    typ2 = (t2 >> 6) & 3; typ1 = (t1 >> 4) & 3
    y = 6 if typ2 in (2, 3) else 7; e2 = 7 if typ2 in (2, 3) else 6
    yk = 4 if typ1 in (2, 3) else 5; e1 = 5 if typ1 in (2, 3) else 4
    kp = (1 << y) | (((t2 >> y) & 1) << e2)
    kk = (1 << yk) | (((t1 >> yk) & 1) << e1)
    if bin(t2 & kk).count('1') % 2: kk |= 1 << e2
    kp = solve_uv(kp, H); kk = solve_uv(kk, H)
    if kp is None or kk is None: C['kappa-fail'] += 1; continue
    pts = coset(h, c); idx = {w: i for i, w in enumerate(pts)}
    vals = [evalc(w, al, be) for w in pts]
    phi = []
    for z, ins in vals:
        v = z[4]
        for j in range(4):
            if (gm >> j) & 1: v ^= z[j]
        phi.append(v)
    s3 = [ins[3][0] if typ2 in (2, 3) else ins[3][1] for z, ins in vals]
    R1 = [phi[i] ^ phi[idx[w ^ kp]] for i, w in enumerate(pts)]
    R0 = [phi[i] ^ (R1[i] & s3[i]) for i in range(64)]
    N1 = [R1[i] ^ R1[idx[w ^ kk]] for i, w in enumerate(pts)]
    N0 = [R0[i] ^ R0[idx[w ^ kk]] for i, w in enumerate(pts)]
    ok_inv = all(R1[i] == R1[idx[w ^ kp]] for i, w in enumerate(pts)) and all(N0[i] == N0[idx[w ^ kk]] and N1[i] == N1[idx[w ^ kk]] for i, w in enumerate(pts))
    const = lambda f: len(set(f)) == 1
    sk = [ins[2][1] if typ1 == 1 else ins[2][0] for z, ins in vals]
    M1 = [R1[i] ^ (N1[i] & sk[i]) for i in range(64)]
    M0 = [R0[i] ^ (N0[i] & sk[i]) for i in range(64)]
    sav = []
    if const(N1): sav.append('N1c')
    if const(M1): sav.append('M1c')
    if const(N0): sav.append('N0c')
    if const([a ^ b for a, b in zip(N0, N1)]): sav.append('N0+N1c')
    key = ('consistent' if ok_inv else 'INCONSISTENT', '+'.join(sav) if sav else 'NO SIMPLE SAVING')
    C[key] += 1
for x, v in sorted(C.items(), key=lambda kv: -kv[1]): print(v, x)
