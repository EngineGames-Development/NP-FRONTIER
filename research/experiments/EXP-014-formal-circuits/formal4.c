/* EXP-014: level 4 of PNE-001 for ALL n, via formal 4-gate circuits.
 *
 * Reformulation (proof in research/proofs/PNE-001-level4.md, Lemma 23):
 *   a level-4 counterexample exists  <=>  there are a constant-free formal circuit Phi (gate i:
 *   z_i = (w_{2i} + sum_{j<i} alpha_ij z_j)(w_{2i+1} + sum_{j<i} beta_ij z_j), output z_3 + sum_{j<3} gamma_j z_j,
 *   formal inputs w_0..w_7 = bits of p in [0,256)), a linear subspace K of F_2^8 of dimension k in {5,6,7},
 *   and two distinct cosets C0 = c0+K, C1 = c1+K such that Phi|C0 is affine and MC(Phi|C1) = 4.
 * Gate-input swaps (w_{2i} <-> w_{2i+1}, alpha_i <-> beta_i) are coordinate permutations, so only
 * wirings with alpha_i <= beta_i (i = 1,2,3) are enumerated.
 * For every survivor (Phi|C0 affine) and every other coset C1, g = Phi|C1 is written out (k = 6,7) or
 * looked up in the exact 5-variable table mc5.mc5 (k = 5).  Points of c+K are indexed by t in F_2^k:
 * point(t) = c ^ sum_r t_r b_r with b_r the RREF basis (pivot = lowest set bit).
 * Build: gcc -O2 -fopenmp -o formal4 formal4.c      Run: ./formal4 K [mc5path] > out   (K in {5,6,7})
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
typedef uint64_t u64; typedef uint32_t u32;

typedef struct { u64 w[4]; } T256;
static inline int bit(const T256 *t, int p) { return (t->w[p >> 6] >> (p & 63)) & 1; }
static T256 tand(T256 a, T256 b) { T256 r; for (int i = 0; i < 4; i++) r.w[i] = a.w[i] & b.w[i]; return r; }
static T256 txor(T256 a, T256 b) { T256 r; for (int i = 0; i < 4; i++) r.w[i] = a.w[i] ^ b.w[i]; return r; }

/* subspaces of F_2^8 of dim k in RREF (pivot = lowest set bit of each basis vector) */
static int nsub; static unsigned char (*bases)[8]; static unsigned char *pivmask;
static void gen_subspaces(int k) {
  int cap = 200000; bases = malloc(cap * 8); pivmask = malloc(cap); nsub = 0;
  for (int P = 0; P < 256; P++) {
    if (__builtin_popcount(P) != k) continue;
    int piv[8], r = 0; for (int q = 0; q < 8; q++) if ((P >> q) & 1) piv[r++] = q;
    int nfree[8], tot = 0, freepos[8][8];
    for (int i = 0; i < k; i++) { nfree[i] = 0; for (int q = piv[i] + 1; q < 8; q++) if (!((P >> q) & 1)) freepos[i][nfree[i]++] = q; tot += nfree[i]; }
    for (long code = 0; code < (1L << tot); code++) {
      long c = code;
      for (int i = 0; i < k; i++) { unsigned char b = 1 << piv[i]; for (int j = 0; j < nfree[i]; j++) { if (c & 1) b |= 1 << freepos[i][j]; c >>= 1; } bases[nsub][i] = b; }
      pivmask[nsub] = P; nsub++;
    }
  }
}
/* Moebius transform in place on a 2^k-bit table stored in up to 2 words; returns 1 iff degree <= 1 */
static int is_affine(u64 lo, u64 hi, int k) {
  static const u64 M[6] = {0x5555555555555555ULL,0x3333333333333333ULL,0x0f0f0f0f0f0f0f0fULL,0x00ff00ff00ff00ffULL,0x0000ffff0000ffffULL,0x00000000ffffffffULL};
  int kk = k < 6 ? k : 6;
  for (int i = 0; i < kk; i++) { lo ^= (lo & M[i]) << (1 << i); hi ^= (hi & M[i]) << (1 << i); }
  if (k == 7) hi ^= lo;
  if (k < 6) lo &= (1ULL << (1 << k)) - 1;
  /* allowed monomials: index 0 and powers of two */
  u64 allow = 1; for (int i = 0; i < kk; i++) allow |= 1ULL << (1 << i);
  if (k == 7) { if (lo & ~allow) return 0; if (hi & ~1ULL) return 0; return 1; }
  return (lo & ~allow) == 0;
}
static void restrict_tab(const T256 *T, const unsigned char *b, int k, int c, u64 *lo, u64 *hi) {
  u64 L = 0, H = 0;
  for (int t = 0; t < (1 << k); t++) {
    int q = c; for (int r = 0; r < k; r++) if ((t >> r) & 1) q ^= b[r];
    if (bit(T, q)) { if (t < 64) L |= 1ULL << t; else H |= 1ULL << (t - 64); }
  }
  *lo = L; *hi = H;
}
static unsigned char *cidx, *tidx; /* per subspace: coset number and t-index of each point q */
static int crep_of[1 << 8];
static void precompute(int k) {
  cidx = malloc((size_t)nsub * 256); tidx = malloc((size_t)nsub * 256);
  for (int s = 0; s < nsub; s++) {
    int P = pivmask[s], cnt = 0; int num[256];
    for (int c = 0; c < 256; c++) if (!(c & P)) num[c] = cnt++;
    for (int q = 0; q < 256; q++) {
      int rep = q, t = 0;
      for (int r = 0; r < k; r++) { int pr = __builtin_ctz(bases[s][r]); if ((q >> pr) & 1) { rep ^= bases[s][r]; t |= 1 << r; } }
      cidx[(size_t)s * 256 + q] = num[rep]; tidx[(size_t)s * 256 + q] = t;
    }
  }
  (void)crep_of;
}
int main(int argc, char **argv) {
  int k = atoi(argv[1]);
  unsigned char *mc5 = 0;
  if (k == 5) { int fd = open(argc > 2 ? argv[2] : "../EXP-010-level4-certificates/mc5.mc5", O_RDONLY); struct stat st; fstat(fd, &st);
    mc5 = mmap(0, st.st_size, PROT_READ, MAP_SHARED, fd, 0); if (mc5 == MAP_FAILED) { perror("mmap"); return 1; } }
  gen_subspaces(k); precompute(k);
  fprintf(stderr, "k=%d subspaces=%d\n", k, nsub);
  /* self-test of the coset/t indexing against the direct definition point(t) = c ^ sum t_r b_r */
  for (int s = 0; s < nsub; s += 97) { int P = pivmask[s];
    for (int c = 0; c < 256; c++) if (!(c & P)) for (int t = 0; t < (1 << k); t++) {
      int q = c; for (int r = 0; r < k; r++) if ((t >> r) & 1) q ^= bases[s][r];
      if (tidx[(size_t)s * 256 + q] != t) { fprintf(stderr, "INDEX BUG\n"); return 3; } } }
  T256 W[8]; for (int t = 0; t < 8; t++) { memset(&W[t], 0, sizeof(T256)); for (int p = 0; p < 256; p++) if ((p >> t) & 1) W[t].w[p >> 6] |= 1ULL << (p & 63); }
  int wir[8640][7], nw = 0;
  for (int a1 = 0; a1 < 2; a1++) for (int b1 = a1; b1 < 2; b1++)
  for (int a2 = 0; a2 < 4; a2++) for (int b2 = a2; b2 < 4; b2++)
  for (int a3 = 0; a3 < 8; a3++) for (int b3 = a3; b3 < 8; b3++)
  for (int gm = 0; gm < 8; gm++) { int *w = wir[nw++]; w[0]=a1; w[1]=a2; w[2]=a3; w[3]=b1; w[4]=b2; w[5]=b3; w[6]=gm; }
  long nsurv = 0, ng = 0, ncex = 0, mcdist[16] = {0};
  int ncos = 1 << (8 - k);
  #pragma omp parallel for schedule(dynamic, 8) reduction(+:nsurv,ng,ncex)
  for (int wi = 0; wi < nw; wi++) {
    int *w = wir[wi];
    int al[4] = {0, w[0], w[1], w[2]}, be[4] = {0, w[3], w[4], w[5]}, gm = w[6];
    T256 z[4];
    for (int i = 0; i < 4; i++) {
      T256 A = W[2 * i], B = W[2 * i + 1];
      for (int j = 0; j < i; j++) { if ((al[i] >> j) & 1) A = txor(A, z[j]); if ((be[i] >> j) & 1) B = txor(B, z[j]); }
      z[i] = tand(A, B);
    }
    T256 Phi = z[3]; for (int j = 0; j < 3; j++) if ((gm >> j) & 1) Phi = txor(Phi, z[j]);
    int pts[256], np = 0; for (int q = 0; q < 256; q++) if (bit(&Phi, q)) pts[np++] = q;
    for (int s = 0; s < nsub; s++) {
      u64 lo[128], hi[128]; memset(lo, 0, ncos * 8); memset(hi, 0, ncos * 8);
      const unsigned char *ci = cidx + (size_t)s * 256, *ti = tidx + (size_t)s * 256;
      for (int i = 0; i < np; i++) { int q = pts[i], t = ti[q]; if (t < 64) lo[ci[q]] |= 1ULL << t; else hi[ci[q]] |= 1ULL << (t - 64); }
      int aff[128], any = 0;
      for (int c = 0; c < ncos; c++) { aff[c] = is_affine(lo[c], hi[c], k); any |= aff[c]; }
      if (!any) continue;
      int reps[128], nr = 0; for (int c = 0; c < 256; c++) if (!(c & pivmask[s])) reps[nr++] = c;
      for (int i = 0; i < ncos; i++) if (aff[i]) {
        nsurv++;
        for (int j = 0; j < ncos; j++) if (j != i && !aff[j]) {
          ng++;
          if (k == 5) {
            u32 g = (u32)lo[j]; int m = (mc5[g >> 1] >> ((g & 1) * 4)) & 15;
            #pragma omp atomic
            mcdist[m]++;
            if (m >= 4) { ncex++;
              #pragma omp critical
              printf("CEX k=5 wiring %d %d %d %d %d %d %d sub %d c0 %d c1 %d table %08x\n", w[0], w[1], w[2], w[3], w[4], w[5], gm, s, reps[i], reps[j], g); }
          } else {
            const unsigned char *b = bases[s];
            #pragma omp critical
            printf("G k=%d wiring %d %d %d %d %d %d %d basis %d %d %d %d %d %d %d c0 %d c1 %d tab %016llx %016llx\n", k, w[0], w[1], w[2], w[3], w[4], w[5], gm,
                   b[0], b[1], b[2], b[3], b[4], k > 5 ? b[5] : 0, k > 6 ? b[6] : 0, reps[i], reps[j], (unsigned long long)hi[j], (unsigned long long)lo[j]);
          }
        }
      }
    }
  }
  fprintf(stderr, "k=%d wirings=%d subspaces=%d affine-coset survivors=%ld g-cosets=%ld k5-MC>=4: %ld\n", k, nw, nsub, nsurv, ng, ncex);
  if (k == 5) { fprintf(stderr, "MC distribution of g over k=5 survivor cosets:"); for (int m = 0; m < 6; m++) fprintf(stderr, " %d:%ld", m, mcdist[m]); fprintf(stderr, "\n"); }
  return 0;
}
