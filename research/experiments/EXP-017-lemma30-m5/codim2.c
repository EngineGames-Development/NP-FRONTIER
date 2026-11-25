/* EXP-017: falsification test of Lemma 30 (codimension 2) at m = 5 (and validation at m = 4).
 * For formal m-gate circuits (swap-reduced wirings; all of them for m = 4, a random sample for m = 5) and every
 * codimension-2 subspace K = ker h1 ∩ ker h2 of F_2^{2m}: find cosets C0 with Phi|C0 affine; for every other coset C1
 * with Phi|C1 not affine, check the prediction of Lemma 30's proof:
 *   dim pi(H) = 0 -> impossible;  dim pi(H) = 2 -> last gate redundant on C1 (z_m|C1 in span(affine, z_1..z_{m-1}|C1));
 *   dim pi(H) = 1 -> the gate named by the proof (m if the relevant coefficient vanishes, else j* = max support) is
 *   degenerate for K (its degeneracy vector lies in H = K^perp).
 * Build: gcc -O2 -mbmi2 -fopenmp -o codim2 codim2.c ;  run: ./codim2 m samples seed */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <immintrin.h>
typedef uint64_t u64;
static int M, D, NP; /* gates, dims, points */
typedef struct { u64 w[16]; } T;   /* up to 1024 bits */
typedef struct { u64 w[4]; } R;    /* 256-bit restricted table (2^{D-2} <= 256) */
static int nsub; static int (*hh)[2]; static unsigned short (*base)[256]; static int *p1s, *p2s;
static int getb(const T *t, int p) { return (t->w[p >> 6] >> (p & 63)) & 1; }
static void gen(void) {
  int cap = 200000; hh = malloc(cap * sizeof *hh); base = malloc((size_t)cap * sizeof *base); p1s = malloc(cap * 4); p2s = malloc(cap * 4); nsub = 0;
  for (int h1 = 1; h1 < (1 << D); h1++) for (int h2 = h1 + 1; h2 < (1 << D); h2++) {
    if (!(h2 < (h1 ^ h2))) continue;
    int a = h1, b = h2; int p1 = __builtin_ctz(a); if ((b >> p1) & 1) b ^= a; int p2 = __builtin_ctz(b); if ((a >> p2) & 1) a ^= b;
    unsigned fm = ((1u << D) - 1) & ~((1u << p1) | (1u << p2));
    for (int t = 0; t < (1 << (D - 2)); t++) { unsigned x = _pdep_u32(t, fm);
      int b1 = __builtin_popcount(a & x) & 1, b2 = __builtin_popcount(b & x) & 1;
      base[nsub][t] = x | (b1 << p1) | (b2 << p2); }
    hh[nsub][0] = h1; hh[nsub][1] = h2; p1s[nsub] = p1; p2s[nsub] = p2; nsub++; }
}
static void gather(const T *t, int s, int c1, int c2, R *r) {
  memset(r, 0, sizeof *r); unsigned sh = (c1 << p1s[s]) | (c2 << p2s[s]);
  for (int i = 0; i < (1 << (D - 2)); i++) if (getb(t, base[s][i] ^ sh)) r->w[i >> 6] |= 1ULL << (i & 63);
}
static int affine(const R *a, int k) { R t = *a; static const u64 Mk[6] = {0x5555555555555555ULL,0x3333333333333333ULL,0x0f0f0f0f0f0f0f0fULL,0x00ff00ff00ff00ffULL,0x0000ffff0000ffffULL,0x00000000ffffffffULL};
  int nw = (1 << k) > 64 ? (1 << k) / 64 : 1;
  for (int i = 0; i < 6 && i < k; i++) for (int j = 0; j < nw; j++) t.w[j] ^= (t.w[j] & Mk[i]) << (1 << i);
  for (int i = 6; i < k; i++) { int s = 1 << (i - 6); for (int j = 0; j < nw; j++) if (j & s) t.w[j] ^= t.w[j ^ s]; }
  if (k < 6) t.w[0] &= (1ULL << (1 << k)) - 1;
  for (int j = 0; j < nw; j++) { u64 allow = 0; for (int b = 0; b < 64; b++) { int p = j * 64 + b; if (p < (1 << k) && (p == 0 || !(p & (p - 1)))) allow |= 1ULL << b; }
    if (t.w[j] & ~allow) return 0; }
  return 1; }
/* GF(2) span test on 256-bit vectors */
static int reduce(R *rows, int nr, R v) { for (int i = 0; i < nr; i++) { int hb = -1; for (int j = 3; j >= 0 && hb < 0; j--) if (rows[i].w[j]) hb = j * 64 + 63 - __builtin_clzll(rows[i].w[j]);
    if ((v.w[hb >> 6] >> (hb & 63)) & 1) for (int j = 0; j < 4; j++) v.w[j] ^= rows[i].w[j]; }
  int z = 1; for (int j = 0; j < 4; j++) if (v.w[j]) z = 0; return z; }
static int addrow(R *rows, int nr, R v) { for (int i = 0; i < nr; i++) { int hb = -1; for (int j = 3; j >= 0 && hb < 0; j--) if (rows[i].w[j]) hb = j * 64 + 63 - __builtin_clzll(rows[i].w[j]);
    if ((v.w[hb >> 6] >> (hb & 63)) & 1) for (int j = 0; j < 4; j++) v.w[j] ^= rows[i].w[j]; }
  int z = 1; for (int j = 0; j < 4; j++) if (v.w[j]) z = 0; if (z) return nr;
  /* insert keeping decreasing highest bit */
  int hv = -1; for (int j = 3; j >= 0 && hv < 0; j--) if (v.w[j]) hv = j * 64 + 63 - __builtin_clzll(v.w[j]);
  int pos = nr; while (pos > 0) { int hp = -1; for (int j = 3; j >= 0 && hp < 0; j--) if (rows[pos-1].w[j]) hp = j * 64 + 63 - __builtin_clzll(rows[pos-1].w[j]); if (hp >= hv) break; rows[pos] = rows[pos-1]; pos--; }
  rows[pos] = v; return nr + 1; }
static int inH(int s, int vec) { int a = hh[s][0], b = hh[s][1]; return vec == a || vec == b || vec == (a ^ b); }
int main(int argc, char **argv) {
  M = atoi(argv[1]); long samples = atol(argv[2]); unsigned seed = argc > 3 ? atoi(argv[3]) : 1; D = 2 * M; NP = 1 << D; int k = D - 2;
  gen(); fprintf(stderr, "m=%d codim-2 subspaces=%d\n", M, nsub);
  T Wv[10]; for (int t = 0; t < D; t++) { memset(&Wv[t], 0, sizeof(T)); for (int p = 0; p < NP; p++) if ((p >> t) & 1) Wv[t].w[p >> 6] |= 1ULL << (p & 63); }
  int lim[5] = {1, 2, 4, 8, 16}; long nw = 1; for (int i = 1; i < M; i++) nw *= (long)lim[i] * (lim[i] + 1) / 2; nw *= 1 << (M - 1);
  long nrun = samples <= 0 || samples > nw ? nw : samples;
  long ordered = 0, pairs = 0, c0 = 0, c2ok = 0, c2bad = 0, c1ok = 0, c1bad = 0, NW = NP / 64;
  srand(seed);
  long *pick = malloc(nrun * sizeof(long)); for (long i = 0; i < nrun; i++) pick[i] = (nrun == nw) ? i : (((long)rand() << 31) ^ rand()) % nw;
  #pragma omp parallel for schedule(dynamic, 1) reduction(+:ordered,pairs,c0,c2ok,c2bad,c1ok,c1bad)
  for (long ii = 0; ii < nrun; ii++) {
    long r = pick[ii]; int al[5] = {0}, be[5] = {0}, gm = r % (1 << (M - 1)); r /= (1 << (M - 1));
    for (int i = M - 1; i >= 1; i--) { int L = lim[i], np = L * (L + 1) / 2, kk = r % np; r /= np; int a = 0; while (kk >= L - a) { kk -= L - a; a++; } al[i] = a; be[i] = a + kk; }
    T z[5];
    for (int i = 0; i < M; i++) { T A = Wv[2 * i], B = Wv[2 * i + 1];
      for (int j = 0; j < i; j++) { if ((al[i] >> j) & 1) for (int q = 0; q < NW; q++) A.w[q] ^= z[j].w[q]; if ((be[i] >> j) & 1) for (int q = 0; q < NW; q++) B.w[q] ^= z[j].w[q]; }
      for (int q = 0; q < NW; q++) z[i].w[q] = A.w[q] & B.w[q]; }
    T Phi = z[M - 1]; for (int j = 0; j < M - 1; j++) if ((gm >> j) & 1) for (int q = 0; q < NW; q++) Phi.w[q] ^= z[j].w[q];
    for (int s = 0; s < nsub; s++) {
      R tab[4]; int aff[4], any = 0;
      for (int c = 0; c < 4; c++) { gather(&Phi, s, c & 1, c >> 1, &tab[c]); aff[c] = affine(&tab[c], k); any |= aff[c]; }
      if (!any) continue;
      int nonaff = 0; for (int c = 0; c < 4; c++) nonaff += !aff[c];
      if (!nonaff) continue;
      ordered += (long)(4 - nonaff) * nonaff;
      int u = D - 2, v = D - 1, a = hh[s][0], b = hh[s][1];
      int pis = 0; int Hv[3] = {a, b, a ^ b}; int seenpi[4] = {0};
      for (int q = 0; q < 3; q++) seenpi[((Hv[q] >> u) & 1) | (((Hv[q] >> v) & 1) << 1)] = 1;
      int npi = seenpi[1] + seenpi[2] + seenpi[3]; int dpi = npi == 0 ? 0 : npi == 1 ? 1 : 2;
      for (int c = 0; c < 4; c++) if (!aff[c]) {
        pairs++;
        if (dpi == 0) { c0++; continue; }
        if (dpi == 2) {
          R rows[16]; int nr = 0; R one; memset(&one, 0, sizeof one); for (int i = 0; i < (1 << k); i++) one.w[i >> 6] |= 1ULL << (i & 63);
          nr = addrow(rows, nr, one);
          for (int rr = 0; rr < k; rr++) { R x; memset(&x, 0, sizeof x); for (int i = 0; i < (1 << k); i++) if ((i >> rr) & 1) x.w[i >> 6] |= 1ULL << (i & 63); nr = addrow(rows, nr, x); }
          for (int j = 0; j < M - 1; j++) { R zr; gather(&z[j], s, c & 1, c >> 1, &zr); nr = addrow(rows, nr, zr); }
          R zl; gather(&z[M - 1], s, c & 1, c >> 1, &zl);
          if (reduce(rows, nr, zl)) c2ok++; else c2bad++;
        } else {
          int h0 = -1, h1 = -1; for (int q = 0; q < 3; q++) { int pq = ((Hv[q] >> u) & 1) | (((Hv[q] >> v) & 1) << 1); if (pq == 0) h0 = Hv[q]; else h1 = Hv[q]; }
          int pq = ((h1 >> u) & 1) | (((h1 >> v) & 1) << 1);
          int coef = pq == 1 ? al[M - 1] : pq == 2 ? be[M - 1] : (al[M - 1] ^ be[M - 1]);
          int g = coef == 0 ? M - 1 : 31 - __builtin_clz(coef);
          int dg = (al[g] == 0 && inH(s, 1 << (2 * g))) || (be[g] == 0 && inH(s, 1 << (2 * g + 1))) || (al[g] == be[g] && inH(s, (1 << (2 * g)) | (1 << (2 * g + 1))));
          if (dg) c1ok++; else c1bad++;
          (void)h0;
        }
      }
    }
  }
  printf("m=%d wirings_run=%ld (of %ld) ordered(C0,C1)=%ld pairs(C1)=%ld | case0=%ld | case2 last-gate-redundant=%ld violations=%ld | case1 predicted-degenerate=%ld violations=%ld\n",
         M, nrun, nw, ordered, pairs, c0, c2ok, c2bad, c1ok, c1bad);
  return 0;
}
