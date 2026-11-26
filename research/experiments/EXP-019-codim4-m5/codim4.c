/* EXP-019: codimension-4 coset pairs of formal 5-gate circuits (level 5 of PNE-001, Corollary 35 of PNE-001-codim3.md).
 * For sampled swap-reduced wirings (0-indexed gates 0..4, gate i reads bits 2i, 2i+1) and all 4-dimensional
 * H = span(h1..h4) in RREF (K = H^perp, dim K = 6), find cosets C0 with Phi|C0 affine, and classify every other coset C
 * with Phi|C not affine by the first mechanism that certifies MC(Phi|C) <= 4:
 *   DEG    some gate is Lemma-24-degenerate for K;
 *   UNUSED some gate j < 4 is not read by any later gate or by the output;
 *   RED_j  gate j is triangularly redundant on C: z_j|C in span(1, coords, z_0..z_{j-1}|C)   (j = 4: Phi|C in span(...));
 *   MERGE  Phi|C in V + s*V with V = span(1, coords, z_0, z_1, z_2 |C) and s in {A_3|C, B_3|C};
 *   HARD   none of these; the instance is printed ("HARD ...") for further analysis.
 * Build: gcc -O2 -mbmi2 -fopenmp -o codim4 codim4.c ;  run: ./codim4 samples seed [maxhard]
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <immintrin.h>
typedef uint64_t u64;
#define M 5
#define D 10
#define NP 1024
#define CD 4
#define KD 6
typedef struct { u64 w[16]; } T;
static int getb(const T *t, int p) { return (t->w[p >> 6] >> (p & 63)) & 1; }
static int affine64(u64 t) { static const u64 Mk[6] = {0x5555555555555555ULL,0x3333333333333333ULL,0x0f0f0f0f0f0f0f0fULL,0x00ff00ff00ff00ffULL,0x0000ffff0000ffffULL,0x00000000ffffffffULL};
  for (int i = 0; i < 6; i++) t ^= (t & Mk[i]) << (1 << i);
  const u64 allow = 1ULL | 2ULL | 4ULL | 16ULL | 256ULL | 65536ULL | (1ULL << 32);
  return (t & ~allow) == 0; }
typedef struct { u64 r[64]; int n; } Basis;   /* echelon by highest bit, fully reduced */
static int bred(const Basis *b, u64 *v) { for (int i = 0; i < b->n; i++) { int h = 63 - __builtin_clzll(b->r[i]); if ((*v >> h) & 1) *v ^= b->r[i]; } return *v == 0; }
static void badd(Basis *b, u64 v) { if (bred(b, &v)) return; int h = 63 - __builtin_clzll(v);
  for (int i = 0; i < b->n; i++) if ((b->r[i] >> h) & 1) b->r[i] ^= v; b->r[b->n++] = v; }
static int inspan(const Basis *b, u64 v) { return bred(b, &v); }
int main(int argc, char **argv) {
  long samples = atol(argv[1]); unsigned seed = argc > 2 ? atoi(argv[2]) : 1; long maxhard = argc > 3 ? atol(argv[3]) : 100000;
  /* 4-dim subspaces H of F_2^10 in RREF (pivot = lowest set bit): stored compactly as 4 x 10-bit vectors */
  long cap = 54000000; unsigned short (*HB)[4] = malloc((size_t)cap * sizeof *HB); long nsub = 0;
  for (int p1 = 0; p1 < D; p1++) for (int p2 = p1 + 1; p2 < D; p2++) for (int p3 = p2 + 1; p3 < D; p3++) for (int p4 = p3 + 1; p4 < D; p4++) {
    int P[4] = {p1, p2, p3, p4}; int piv = (1 << p1) | (1 << p2) | (1 << p3) | (1 << p4);
    int fr[4][10], nf[4], tot = 0; for (int i = 0; i < 4; i++) { nf[i] = 0; for (int q = P[i] + 1; q < D; q++) if (!((piv >> q) & 1)) fr[i][nf[i]++] = q; tot += nf[i]; }
    for (long code = 0; code < (1L << tot); code++) { long c = code;
      for (int i = 0; i < 4; i++) { int h = 1 << P[i]; for (int j = 0; j < nf[i]; j++) { if (c & 1) h |= 1 << fr[i][j]; c >>= 1; } HB[nsub][i] = h; }
      nsub++; } }
  fprintf(stderr, "codim-4 subspaces of F_2^10: %ld\n", nsub);
  T Wv[D]; for (int t = 0; t < D; t++) { memset(&Wv[t], 0, sizeof(T)); for (int p = 0; p < NP; p++) if ((p >> t) & 1) Wv[t].w[p >> 6] |= 1ULL << (p & 63); }
  int lim[M] = {1, 2, 4, 8, 16}; long nw = 1; for (int i = 1; i < M; i++) nw *= (long)lim[i] * (lim[i] + 1) / 2; nw *= 1 << (M - 1);
  long nrun = samples <= 0 || samples > nw ? nw : samples;
  long *pick = malloc(nrun * sizeof(long)); srand(seed);
  for (long i = 0; i < nrun; i++) pick[i] = (nrun == nw) ? i : ((((long)rand() << 31) ^ rand()) % nw);
  long n_pairs = 0, n_deg = 0, n_unused = 0, n_red[M] = {0}, n_merge = 0, n_hard = 0, n_affsub = 0;
  #pragma omp parallel for schedule(dynamic, 1) reduction(+:n_pairs,n_deg,n_unused,n_merge,n_hard,n_affsub)
  for (long ii = 0; ii < nrun; ii++) {
    long r = pick[ii]; int al[M] = {0}, be[M] = {0}, gm = r % (1 << (M - 1)); r /= (1 << (M - 1));
    for (int i = M - 1; i >= 1; i--) { int L = lim[i], np = L * (L + 1) / 2, kk = r % np; r /= np; int a = 0; while (kk >= L - a) { kk -= L - a; a++; } al[i] = a; be[i] = a + kk; }
    T z[M], Ain[M], Bin[M];
    for (int i = 0; i < M; i++) { T A = Wv[2 * i], B = Wv[2 * i + 1];
      for (int j = 0; j < i; j++) { if ((al[i] >> j) & 1) for (int q = 0; q < 16; q++) A.w[q] ^= z[j].w[q]; if ((be[i] >> j) & 1) for (int q = 0; q < 16; q++) B.w[q] ^= z[j].w[q]; }
      Ain[i] = A; Bin[i] = B; for (int q = 0; q < 16; q++) z[i].w[q] = A.w[q] & B.w[q]; }
    T Phi = z[M - 1]; for (int j = 0; j < M - 1; j++) if ((gm >> j) & 1) for (int q = 0; q < 16; q++) Phi.w[q] ^= z[j].w[q];
    int used[M] = {0}; for (int i = 1; i < M; i++) for (int j = 0; j < i; j++) if (((al[i] | be[i]) >> j) & 1) used[j] = 1;
    for (int j = 0; j < M - 1; j++) if ((gm >> j) & 1) used[j] = 1;
    int anyunused = 0; for (int j = 0; j < M - 1; j++) if (!used[j]) anyunused = 1;
    long loc_red[M] = {0};
    unsigned short base[64];
    for (long s = 0; s < nsub; s++) {
      int h[4] = {HB[s][0], HB[s][1], HB[s][2], HB[s][3]}, P[4]; for (int i = 0; i < 4; i++) P[i] = __builtin_ctz(h[i]);
      /* H elements and Lemma-24 degeneracy first (cheap) */
      int Hv[16]; for (int l = 0; l < 16; l++) { Hv[l] = 0; for (int i = 0; i < 4; i++) if ((l >> i) & 1) Hv[l] ^= h[i]; }
      int degen = 0;
      for (int g = 0; g < M && !degen; g++) for (int l = 1; l < 16; l++) {
        int x = Hv[l]; if ((al[g] == 0 && x == (1 << (2 * g))) || (be[g] == 0 && x == (1 << (2 * g + 1))) || (al[g] == be[g] && x == ((1 << (2 * g)) | (1 << (2 * g + 1))))) { degen = 1; break; } }
      unsigned fm = ((1u << D) - 1) & ~((1u << P[0]) | (1u << P[1]) | (1u << P[2]) | (1u << P[3]));
      for (int t = 0; t < 64; t++) { unsigned x = _pdep_u32(t, fm), b = x;
        for (int i = 0; i < 4; i++) b |= (unsigned)(__builtin_popcount((h[i] & ~(1 << P[i])) & x) & 1) << P[i];
        base[t] = b; }
      u64 tab[16]; int aff[16], any = 0;
      for (int c = 0; c < 16; c++) { unsigned sh = 0; for (int i = 0; i < 4; i++) if ((c >> i) & 1) sh |= 1u << P[i];
        u64 v = 0; for (int t = 0; t < 64; t++) v |= (u64)getb(&Phi, base[t] ^ sh) << t; tab[c] = v; aff[c] = affine64(v); any |= aff[c]; }
      if (!any) continue;
      int nonaff = 0; for (int c = 0; c < 16; c++) nonaff += !aff[c];
      if (!nonaff) continue;
      n_affsub++;
      for (int c = 0; c < 16; c++) if (!aff[c]) {
        n_pairs++;
        if (degen) { n_deg++; continue; }
        if (anyunused) { n_unused++; continue; }
        unsigned sh = 0; for (int i = 0; i < 4; i++) if ((c >> i) & 1) sh |= 1u << P[i];
        u64 zr[M], Ar[M], Br[M];
        for (int g = 0; g < M; g++) { u64 a = 0, b = 0, zz = 0; for (int t = 0; t < 64; t++) { int p = base[t] ^ sh; zz |= (u64)getb(&z[g], p) << t; a |= (u64)getb(&Ain[g], p) << t; b |= (u64)getb(&Bin[g], p) << t; } zr[g] = zz; Ar[g] = a; Br[g] = b; }
        Basis B; B.n = 0; badd(&B, ~0ULL); for (int rr = 0; rr < KD; rr++) { u64 x = 0; for (int t = 0; t < 64; t++) if ((t >> rr) & 1) x |= 1ULL << t; badd(&B, x); }
        int red = -1; Basis Bk = B;
        for (int g = 0; g < M - 1 && red < 0; g++) { if (inspan(&Bk, zr[g])) red = g; badd(&Bk, zr[g]); }
        if (red < 0 && inspan(&Bk, tab[c])) red = M - 1;
        if (red >= 0) { loc_red[red]++; continue; }
        Basis V = B; for (int g = 0; g < M - 2; g++) badd(&V, zr[g]);
        int merged = 0;
        for (int which = 0; which < 2 && !merged; which++) { u64 sv = which ? Br[M - 2] : Ar[M - 2];
          Basis W = V; u64 gen[64]; int ng = V.n; for (int i = 0; i < ng; i++) gen[i] = V.r[i];
          for (int i = 0; i < ng; i++) badd(&W, gen[i] & sv);
          if (inspan(&W, tab[c])) merged = 1; }
        if (merged) { n_merge++; continue; }
        n_hard++;
        if (n_hard <= maxhard) {
          int c0 = 0; while (!aff[c0]) c0++;
          #pragma omp critical
          printf("HARD %d %d %d %d %d %d %d %d %d  %d %d %d %d  c0 %d c %d tab %016llx\n", al[1], al[2], al[3], al[4], be[1], be[2], be[3], be[4], gm,
                 h[0], h[1], h[2], h[3], c0, c, (unsigned long long)tab[c]);
        }
      }
    }
    for (int g = 0; g < M; g++) {
      #pragma omp atomic
      n_red[g] += loc_red[g]; }
  }
  fprintf(stderr, "wirings_run=%ld (of %ld) subspaces=%ld | (wiring,K) with an affine coset and a non-affine one: %ld\n", nrun, nw, nsub, n_affsub);
  fprintf(stderr, "non-affine C with affine C0: %ld | DEG %ld | UNUSED %ld | RED gate0..4: %ld %ld %ld %ld %ld | MERGE %ld | HARD %ld\n",
          n_pairs, n_deg, n_unused, n_red[0], n_red[1], n_red[2], n_red[3], n_red[4], n_merge, n_hard);
  printf("SUMMARY wirings=%ld pairs=%ld deg=%ld unused=%ld red=%ld,%ld,%ld,%ld,%ld merge=%ld hard=%ld\n", nrun, n_pairs, n_deg, n_unused, n_red[0], n_red[1], n_red[2], n_red[3], n_red[4], n_merge, n_hard);
  return 0;
}
