/* EXP-016: Lemma 23 restricted to codimension-1 subspaces K (hyperplanes of F_2^{2m}), m = 4 or 5.
 * For every formal m-gate circuit (alpha_i <= beta_i, all gamma) and every hyperplane K = ker(h),
 * test whether Phi is affine on a coset {h.p = c}; for each such (Phi, h, c) print the table of Phi on the
 * other coset (as a 2m-variable function that ignores the pivot bit q = lowest set bit of h).
 * Also prints counts.  Validation: m = 4 must reproduce formal4's dim K = 7 counts (1020 affine cosets,
 * 840 pairs).  Build: gcc -O2 -fopenmp -o hyper hyper.c ; run: ./hyper m > out */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u64;
static int M, D, NW; /* gates, formal inputs, 64-bit words */
typedef struct { u64 w[16]; } T;
static T Wv[10], Zq[10], Par[1024][2]; static u64 ALLOW[16];
static void flip(const T *a, int q, T *r) {
  if (q < 6) { u64 m = 0; for (int p = 0; p < 64; p++) if (!((p >> q) & 1)) m |= 1ULL << p; int s = 1 << q;
    for (int i = 0; i < NW; i++) r->w[i] = ((a->w[i] & m) << s) | ((a->w[i] >> s) & m); }
  else { int s = 1 << (q - 6); for (int i = 0; i < NW; i++) r->w[i] = a->w[i ^ s]; }
}
static int affine(const T *a) { /* Moebius on 2^D bits; degree <= 1 */
  T t = *a; static const u64 Mk[6] = {0x5555555555555555ULL,0x3333333333333333ULL,0x0f0f0f0f0f0f0f0fULL,0x00ff00ff00ff00ffULL,0x0000ffff0000ffffULL,0x00000000ffffffffULL};
  for (int i = 0; i < 6 && i < D; i++) for (int j = 0; j < NW; j++) t.w[j] ^= (t.w[j] & Mk[i]) << (1 << i);
  for (int i = 6; i < D; i++) { int s = 1 << (i - 6); for (int j = 0; j < NW; j++) if (j & s) t.w[j] ^= t.w[j ^ s]; }
  /* allowed positions: 0 and 2^i */
  for (int j = 0; j < NW; j++) if (t.w[j] & ~ALLOW[j]) return 0;
  return 1;
}
int main(int argc, char **argv) {
  M = atoi(argv[1]); D = 2 * M; NW = (1 << D) / 64;
  for (int t = 0; t < D; t++) { memset(&Wv[t], 0, sizeof(T)); memset(&Zq[t], 0, sizeof(T));
    for (int p = 0; p < (1 << D); p++) { if ((p >> t) & 1) Wv[t].w[p >> 6] |= 1ULL << (p & 63); else Zq[t].w[p >> 6] |= 1ULL << (p & 63); } }
  for (int h = 1; h < (1 << D); h++) for (int c = 0; c < 2; c++) { memset(&Par[h][c], 0, sizeof(T));
    for (int p = 0; p < (1 << D); p++) if ((__builtin_popcount(p & h) & 1) == c) Par[h][c].w[p >> 6] |= 1ULL << (p & 63); }
  for (int j = 0; j < NW; j++) { ALLOW[j] = 0; for (int b = 0; b < 64; b++) { int p = j * 64 + b; if (p == 0 || (p & (p - 1)) == 0) ALLOW[j] |= 1ULL << b; } }
  /* wirings */
  int lim[5] = {1, 2, 4, 8, 16};
  long nw = 1; for (int i = 1; i < M; i++) nw *= (long)lim[i] * (lim[i] + 1) / 2; nw *= 1 << (M - 1);
  fprintf(stderr, "m=%d D=%d wirings=%ld\n", M, D, nw);
  long naff = 0, npairs = 0, ndeg = 0;
  #pragma omp parallel for schedule(dynamic, 64) reduction(+:naff,npairs,ndeg)
  for (long wi = 0; wi < nw; wi++) {
    long r = wi; int al[5] = {0}, be[5] = {0}, gm;
    gm = r % (1 << (M - 1)); r /= (1 << (M - 1));
    for (int i = M - 1; i >= 1; i--) { int L = lim[i], np = L * (L + 1) / 2, k = r % np; r /= np;
      int a = 0; while (k >= L - a) { k -= L - a; a++; } al[i] = a; be[i] = a + k; }
    T z[5];
    for (int i = 0; i < M; i++) { T A = Wv[2 * i], B = Wv[2 * i + 1];
      for (int j = 0; j < i; j++) { if ((al[i] >> j) & 1) for (int q = 0; q < NW; q++) A.w[q] ^= z[j].w[q]; if ((be[i] >> j) & 1) for (int q = 0; q < NW; q++) B.w[q] ^= z[j].w[q]; }
      for (int q = 0; q < NW; q++) z[i].w[q] = A.w[q] & B.w[q]; }
    T Phi = z[M - 1]; for (int j = 0; j < M - 1; j++) if ((gm >> j) & 1) for (int q = 0; q < NW; q++) Phi.w[q] ^= z[j].w[q];
    for (int h = 1; h < (1 << D); h++) {
      int q = __builtin_ctz(h); T F, Tc[2]; flip(&Phi, q, &F);
      for (int c = 0; c < 2; c++) { T x, y;
        for (int i = 0; i < NW; i++) x.w[i] = ((Phi.w[i] & Par[h][c].w[i]) | (F.w[i] & ~Par[h][c].w[i])) & Zq[q].w[i];
        flip(&x, q, &y); for (int i = 0; i < NW; i++) Tc[c].w[i] = x.w[i] | y.w[i]; }
      int a0 = affine(&Tc[0]), a1 = affine(&Tc[1]);
      naff += a0 + a1;
      int degen = 0; for (int i = 0; i < M; i++) {
        if (al[i] == 0 && h == (1 << (2 * i))) degen = 1;
        if (be[i] == 0 && h == (1 << (2 * i + 1))) degen = 1;
        if (al[i] == be[i] && h == ((1 << (2 * i)) | (1 << (2 * i + 1)))) degen = 1; }
      for (int c = 0; c < 2; c++) if ((c ? a1 : a0) && !(c ? a0 : a1)) { npairs++; if (degen) { ndeg++; continue; }
        #pragma omp critical
        { printf("P m=%d al", M); for (int i = 1; i < M; i++) printf(" %d", al[i]); printf(" be"); for (int i = 1; i < M; i++) printf(" %d", be[i]);
          printf(" gm %d h %d c0 %d tab", gm, h, c); for (int i = NW - 1; i >= 0; i--) printf(" %016llx", (unsigned long long)Tc[1 - c].w[i]); printf("\n"); } }
    }
  }
  fprintf(stderr, "m=%d affine cosets=%ld pairs=%ld degenerate=%ld non-degenerate=%ld\n", M, naff, npairs, ndeg, npairs - ndeg);
  return 0;
}
