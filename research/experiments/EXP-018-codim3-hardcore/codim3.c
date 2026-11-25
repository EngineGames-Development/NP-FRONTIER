/* EXP-018: falsification test of the codimension-3 lemma (Lemma 32) of PNE-001-level4.md, at m = 4 (exhaustive) and
 * m = 5 (random sample of wirings, all codimension-3 subspaces).
 *
 * For a formal m-gate circuit Phi (0-indexed gates 0..m-1, gate i reads bits 2i, 2i+1; swap-reduced wirings
 * al[i] <= be[i]) and every codimension-3 subspace K = H^perp of F_2^{2m} (H = span(h1,h2,h3) in RREF, pivot = lowest
 * set bit): if some coset C0 has Phi|C0 affine, then for every other coset C with Phi|C not affine the proof predicts:
 *   (deg)  some gate is Lemma-24-degenerate for K                                 -> counted, not examined further;
 *   otherwise, with pi = projection of H onto the last gate's private bits (D-2, D-1) and H0 = ker pi:
 *   dim pi(H) = 0                                                                  -> impossible (violation);
 *   dim pi(H) = 1: psi = alpha_m, beta_m or alpha_m+beta_m (by pi(H) = (1,0),(0,1),(1,1)); psi = 0 -> violation;
 *       j* = max supp psi; H* = {h in H0 : supp h within bits 0..2j*+1}; dim H* < 2 -> violation;
 *       dim pi*(H*) on bits (2j*, 2j*+1) < 2 -> violation; else gate j* is redundant on C:
 *       z_{j*}|C in span(1, coords, z_0..z_{j*-1}|C)                                -> checked;
 *   dim pi(H) = 2, H0 = {0,h0}, C and C0 in the same H0-class -> last gate redundant on C:
 *       Phi|C in span(1, coords, z_0..z_{m-2}|C)                                    -> checked;
 *   dim pi(H) = 2, different classes, k = top gate of h0:
 *       k = m-2 (top gate below the last): Phi|C in V0 + s*V0, V0 = span(1, coords, z_0..z_{m-3}|C),
 *                s = input B of gate k if h0 meets only bit 2k, input A if it meets bit 2k+1  -> checked;
 *       k < m-2: gate m-2 unused, or the last gate redundant on C                   -> checked.
 * Every prediction implies MC(Phi|C) <= m-1.
 * Build: gcc -O2 -mbmi2 -fopenmp -o codim3 codim3.c ;  run: ./codim3 m samples seed   (samples <= 0: all wirings) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <immintrin.h>
typedef uint64_t u64;
#define MAXM 5
#define TW 16          /* 1024-bit full tables (D <= 10) */
#define RW 2           /* 128-bit restricted tables (k = D-3 <= 7) */
static int M, D, NP, KD; /* gates, dims, points, restricted dim */
typedef struct { u64 w[TW]; } T;
typedef struct { u64 w[RW]; } R;
static int getb(const T *t, int p) { return (t->w[p >> 6] >> (p & 63)) & 1; }
static int nrw(void) { return (1 << KD) > 64 ? (1 << KD) / 64 : 1; }
static int affine(const R *a) {
  R t = *a; static const u64 Mk[6] = {0x5555555555555555ULL,0x3333333333333333ULL,0x0f0f0f0f0f0f0f0fULL,0x00ff00ff00ff00ffULL,0x0000ffff0000ffffULL,0x00000000ffffffffULL};
  int nw = nrw();
  for (int i = 0; i < 6 && i < KD; i++) for (int j = 0; j < nw; j++) t.w[j] ^= (t.w[j] & Mk[i]) << (1 << i);
  for (int i = 6; i < KD; i++) { int s = 1 << (i - 6); for (int j = 0; j < nw; j++) if (j & s) t.w[j] ^= t.w[j ^ s]; }
  if (KD < 6) t.w[0] &= (1ULL << (1 << KD)) - 1;
  for (int j = 0; j < nw; j++) { u64 allow = 0; for (int b = 0; b < 64; b++) { int p = j * 64 + b; if (p < (1 << KD) && (p == 0 || !(p & (p - 1)))) allow |= 1ULL << b; }
    if (t.w[j] & ~allow) return 0; }
  return 1; }
/* GF(2) elimination on R vectors */
static int hib(const R *v) { for (int j = RW - 1; j >= 0; j--) if (v->w[j]) return j * 64 + 63 - __builtin_clzll(v->w[j]); return -1; }
typedef struct { R r[64]; int h[64]; int n; } Basis;
static void binit(Basis *b) { b->n = 0; }
static int bred(const Basis *b, R *v) { for (int i = 0; i < b->n; i++) if ((v->w[b->h[i] >> 6] >> (b->h[i] & 63)) & 1) for (int j = 0; j < RW; j++) v->w[j] ^= b->r[i].w[j]; return hib(v) < 0; }
static void badd(Basis *b, R v) { if (bred(b, &v)) return; int h = hib(&v);
  for (int i = 0; i < b->n; i++) if ((b->r[i].w[h >> 6] >> (h & 63)) & 1) for (int j = 0; j < RW; j++) b->r[i].w[j] ^= v.w[j];
  b->r[b->n] = v; b->h[b->n] = h; b->n++; }
static int binspan(const Basis *b, R v) { return bred(b, &v); }
static R rand_and(R a, R b) { R r; for (int j = 0; j < RW; j++) r.w[j] = a.w[j] & b.w[j]; return r; }

static long cnt_pairs, cnt_deg, cnt_viol, c1_red, c2s_red, c2d_merge, c2d_low_unused, c2d_low_red, viol_kind[8];
int main(int argc, char **argv) {
  M = atoi(argv[1]); long samples = atol(argv[2]); unsigned seed = argc > 3 ? atoi(argv[3]) : 1;
  D = 2 * M; NP = 1 << D; KD = D - 3;
  if (M < 3 || M > MAXM) { fprintf(stderr, "m in 3..5\n"); return 1; }
  /* codimension-3 subspaces: H = span(h1,h2,h3), RREF with pivot = lowest set bit */
  long cap = 7000000; int (*HB)[3] = malloc(cap * sizeof *HB); long nsub = 0;
  for (int p1 = 0; p1 < D; p1++) for (int p2 = p1 + 1; p2 < D; p2++) for (int p3 = p2 + 1; p3 < D; p3++) {
    int piv = (1 << p1) | (1 << p2) | (1 << p3); int P[3] = {p1, p2, p3};
    int fr[3][16], nf[3]; for (int i = 0; i < 3; i++) { nf[i] = 0; for (int q = P[i] + 1; q < D; q++) if (!((piv >> q) & 1)) fr[i][nf[i]++] = q; }
    for (long c0 = 0; c0 < (1L << nf[0]); c0++) for (long c1 = 0; c1 < (1L << nf[1]); c1++) for (long c2 = 0; c2 < (1L << nf[2]); c2++) {
      long cc[3] = {c0, c1, c2}; int h[3];
      for (int i = 0; i < 3; i++) { h[i] = 1 << P[i]; for (int j = 0; j < nf[i]; j++) if ((cc[i] >> j) & 1) h[i] |= 1 << fr[i][j]; }
      HB[nsub][0] = h[0]; HB[nsub][1] = h[1]; HB[nsub][2] = h[2]; nsub++; } }
  fprintf(stderr, "m=%d codim-3 subspaces=%ld\n", M, nsub);
  T Wv[2 * MAXM]; for (int t = 0; t < D; t++) { memset(&Wv[t], 0, sizeof(T)); for (int p = 0; p < NP; p++) if ((p >> t) & 1) Wv[t].w[p >> 6] |= 1ULL << (p & 63); }
  int lim[MAXM] = {1, 2, 4, 8, 16}; long nw = 1; for (int i = 1; i < M; i++) nw *= (long)lim[i] * (lim[i] + 1) / 2; nw *= 1 << (M - 1);
  long nrun = samples <= 0 || samples > nw ? nw : samples;
  long *pick = malloc(nrun * sizeof(long)); srand(seed);
  for (long i = 0; i < nrun; i++) pick[i] = (nrun == nw) ? i : ((((long)rand() << 31) ^ rand()) % nw);
  int NW = NP / 64 > 0 ? NP / 64 : 1, u = D - 2, v = D - 1;
  #pragma omp parallel for schedule(dynamic, 1) reduction(+:cnt_pairs,cnt_deg,cnt_viol,c1_red,c2s_red,c2d_merge,c2d_low_unused,c2d_low_red)
  for (long ii = 0; ii < nrun; ii++) {
    long r = pick[ii]; int al[MAXM] = {0}, be[MAXM] = {0}, gm = r % (1 << (M - 1)); r /= (1 << (M - 1));
    for (int i = M - 1; i >= 1; i--) { int L = lim[i], np = L * (L + 1) / 2, kk = r % np; r /= np; int a = 0; while (kk >= L - a) { kk -= L - a; a++; } al[i] = a; be[i] = a + kk; }
    T z[MAXM], Ain[MAXM], Bin[MAXM];
    for (int i = 0; i < M; i++) { T A = Wv[2 * i], B = Wv[2 * i + 1];
      for (int j = 0; j < i; j++) { if ((al[i] >> j) & 1) for (int q = 0; q < NW; q++) A.w[q] ^= z[j].w[q]; if ((be[i] >> j) & 1) for (int q = 0; q < NW; q++) B.w[q] ^= z[j].w[q]; }
      Ain[i] = A; Bin[i] = B; for (int q = 0; q < NW; q++) z[i].w[q] = A.w[q] & B.w[q]; }
    T Phi = z[M - 1]; for (int j = 0; j < M - 1; j++) if ((gm >> j) & 1) for (int q = 0; q < NW; q++) Phi.w[q] ^= z[j].w[q];
    int used[MAXM] = {0}; for (int i = 1; i < M; i++) for (int j = 0; j < i; j++) if (((al[i] | be[i]) >> j) & 1) used[j] = 1;
    for (int j = 0; j < M - 1; j++) if ((gm >> j) & 1) used[j] = 1;
    unsigned short base[128];
    for (long s = 0; s < nsub; s++) {
      int h[3] = {HB[s][0], HB[s][1], HB[s][2]}; int P[3]; for (int i = 0; i < 3; i++) P[i] = __builtin_ctz(h[i]);
      unsigned fm = ((1u << D) - 1) & ~((1u << P[0]) | (1u << P[1]) | (1u << P[2]));
      for (int t = 0; t < (1 << KD); t++) { unsigned x = _pdep_u32(t, fm); unsigned b = x;
        for (int i = 0; i < 3; i++) b |= (unsigned)(__builtin_popcount((h[i] & ~(1 << P[i])) & x) & 1) << P[i];
        base[t] = b; }
      R tab[8]; int aff[8], any = 0;
      for (int c = 0; c < 8; c++) { unsigned sh = 0; for (int i = 0; i < 3; i++) if ((c >> i) & 1) sh |= 1u << P[i];
        memset(&tab[c], 0, sizeof(R)); for (int t = 0; t < (1 << KD); t++) if (getb(&Phi, base[t] ^ sh)) tab[c].w[t >> 6] |= 1ULL << (t & 63);
        aff[c] = affine(&tab[c]); any |= aff[c]; }
      if (!any) continue;
      int nonaff = 0; for (int c = 0; c < 8; c++) nonaff += !aff[c];
      if (!nonaff) continue;
      /* H elements */
      int Hv[8]; for (int l = 1; l < 8; l++) { Hv[l] = 0; for (int i = 0; i < 3; i++) if ((l >> i) & 1) Hv[l] ^= h[i]; }
      #define INH(vec) ({ int _f = 0; for (int _l = 1; _l < 8; _l++) if (Hv[_l] == (vec)) _f = 1; _f; })
      int degen = 0; for (int g = 0; g < M; g++) {
        if (al[g] == 0 && INH(1 << (2 * g))) degen = 1; if (be[g] == 0 && INH(1 << (2 * g + 1))) degen = 1;
        if (al[g] == be[g] && INH((1 << (2 * g)) | (1 << (2 * g + 1)))) degen = 1; }
      int c0 = -1; for (int c = 0; c < 8; c++) if (aff[c]) { c0 = c; break; }
      for (int c = 0; c < 8; c++) if (!aff[c]) {
        cnt_pairs++;
        if (degen) { cnt_deg++; continue; }
        int seen[4] = {0}; for (int l = 1; l < 8; l++) seen[((Hv[l] >> u) & 1) | (((Hv[l] >> v) & 1) << 1)] = 1;
        int npi = seen[1] + seen[2] + seen[3]; int dpi = npi == 0 ? 0 : npi == 1 ? 1 : 2;
        unsigned sh = 0; for (int i = 0; i < 3; i++) if ((c >> i) & 1) sh |= 1u << P[i];
        /* restricted gate tables and inputs on C */
        R zr[MAXM], Ar[MAXM], Br[MAXM], ph = tab[c];
        for (int g = 0; g < M; g++) { memset(&zr[g], 0, sizeof(R)); memset(&Ar[g], 0, sizeof(R)); memset(&Br[g], 0, sizeof(R));
          for (int t = 0; t < (1 << KD); t++) { int p = base[t] ^ sh;
            if (getb(&z[g], p)) zr[g].w[t >> 6] |= 1ULL << (t & 63);
            if (getb(&Ain[g], p)) Ar[g].w[t >> 6] |= 1ULL << (t & 63);
            if (getb(&Bin[g], p)) Br[g].w[t >> 6] |= 1ULL << (t & 63); } }
        Basis Aff; binit(&Aff); { R one; memset(&one, 0, sizeof one); for (int t = 0; t < (1 << KD); t++) one.w[t >> 6] |= 1ULL << (t & 63); badd(&Aff, one);
          for (int rr = 0; rr < KD; rr++) { R x; memset(&x, 0, sizeof x); for (int t = 0; t < (1 << KD); t++) if ((t >> rr) & 1) x.w[t >> 6] |= 1ULL << (t & 63); badd(&Aff, x); } }
        if (dpi == 0) { cnt_viol++; viol_kind[0]++; continue; }
        if (dpi == 1) {
          int pq = 0; for (int l = 1; l < 8; l++) { int q = ((Hv[l] >> u) & 1) | (((Hv[l] >> v) & 1) << 1); if (q) pq = q; }
          int psi = pq == 1 ? al[M - 1] : pq == 2 ? be[M - 1] : (al[M - 1] ^ be[M - 1]);
          if (!psi) { cnt_viol++; viol_kind[1]++; continue; }
          int js = 31 - __builtin_clz(psi); int lowmask = (1 << (2 * js + 2)) - 1;
          int Hs[8], nhs = 0; for (int l = 1; l < 8; l++) { int q = ((Hv[l] >> u) & 1) | (((Hv[l] >> v) & 1) << 1); if (!q && !(Hv[l] & ~lowmask)) Hs[nhs++] = Hv[l]; }
          if (nhs < 3) { cnt_viol++; viol_kind[2]++; continue; }   /* dim H* < 2 */
          int sp[4] = {0}; for (int q = 0; q < nhs; q++) sp[(Hs[q] >> (2 * js)) & 3] = 1;
          int np2 = sp[1] + sp[2] + sp[3]; if (np2 < 2) { cnt_viol++; viol_kind[3]++; continue; }
          Basis Bs = Aff; for (int g = 0; g < js; g++) badd(&Bs, zr[g]);
          if (binspan(&Bs, zr[js])) c1_red++; else { cnt_viol++; viol_kind[4]++; }
          continue; }
        /* dpi == 2 */
        int h0 = 0; for (int l = 1; l < 8; l++) if (!(((Hv[l] >> u) & 1) | ((Hv[l] >> v) & 1))) h0 = Hv[l];
        int same = (__builtin_popcount(h0 & (base[0] ^ ({ unsigned s0 = 0; for (int i = 0; i < 3; i++) if ((c0 >> i) & 1) s0 |= 1u << P[i]; s0; }))) & 1)
                == (__builtin_popcount(h0 & (base[0] ^ sh)) & 1);
        if (same) { Basis Bs = Aff; for (int g = 0; g < M - 1; g++) badd(&Bs, zr[g]);
          if (binspan(&Bs, ph)) c2s_red++; else { cnt_viol++; viol_kind[5]++; } continue; }
        int k = -1; for (int g = 0; g < M - 1; g++) if ((h0 >> (2 * g)) & 3) k = g;
        if (k == M - 2) {
          int typ = (h0 >> (2 * k)) & 3; R sv = (typ == 1) ? Br[k] : Ar[k];
          Basis V0 = Aff; for (int g = 0; g < M - 2; g++) badd(&V0, zr[g]);
          Basis Bs = V0; int n0 = V0.n; R gen[64]; for (int i = 0; i < n0; i++) gen[i] = V0.r[i];
          for (int i = 0; i < n0; i++) badd(&Bs, rand_and(gen[i], sv));
          if (binspan(&Bs, ph)) c2d_merge++; else { cnt_viol++; viol_kind[6]++; }
        } else {
          if (!used[M - 2]) { c2d_low_unused++; continue; }
          Basis Bs = Aff; for (int g = 0; g < M - 1; g++) badd(&Bs, zr[g]);
          if (binspan(&Bs, ph)) c2d_low_red++; else { cnt_viol++; viol_kind[7]++; }
        }
      }
    }
  }
  printf("m=%d wirings_run=%ld (of %ld) subspaces=%ld | non-affine C with an affine C0: %ld | Lemma-24 degenerate: %ld\n", M, nrun, nw, nsub, cnt_pairs, cnt_deg);
  printf("  dim pi=1: gate j* redundant: %ld\n  dim pi=2 same class: last gate redundant: %ld\n  dim pi=2 different class, k=m-1: merge V0+s*V0 holds: %ld\n  dim pi=2 different class, k<m-1: gate m-1 unused: %ld, last gate redundant: %ld\n",
         c1_red, c2s_red, c2d_merge, c2d_low_unused, c2d_low_red);
  printf("  VIOLATIONS: %ld  (by kind: pi0 %ld, psi0 %ld, dimH*<2 %ld, dimpi*<2 %ld, j*-not-red %ld, same-not-red %ld, merge-fails %ld, low-not-red %ld)\n",
         cnt_viol, viol_kind[0], viol_kind[1], viol_kind[2], viol_kind[3], viol_kind[4], viol_kind[5], viol_kind[6], viol_kind[7]);
  return 0;
}
