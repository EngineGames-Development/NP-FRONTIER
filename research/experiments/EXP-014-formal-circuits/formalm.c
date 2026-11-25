/* EXP-014 generalisation: formal M-gate circuits (M = 1..4) on D = 2M formal inputs, all subspaces K of
 * F_2^D of dimension k (kmin..D-1), all coset pairs (C0 affine, C1 not).  For k <= 5 the MC of g = Phi|C1 is
 * read from the exact tables (mc4.bin for k <= 4, padded; mc5.mc5 for k = 5); larger k are written out.
 * Prints the MC distribution of g per k.  A level-M counterexample is a g with MC(g) = M.
 * Build: gcc -O2 -fopenmp -o formalm formalm.c     Run: ./formalm M k */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
typedef uint64_t u64; typedef uint32_t u32;
static int D, NPT;
typedef struct { u64 w[4]; } T;
static T tand(T a, T b) { T r; for (int i = 0; i < 4; i++) r.w[i] = a.w[i] & b.w[i]; return r; }
static T txor(T a, T b) { T r; for (int i = 0; i < 4; i++) r.w[i] = a.w[i] ^ b.w[i]; return r; }
static int bit(const T *t, int p) { return (t->w[p >> 6] >> (p & 63)) & 1; }
static int nsub; static unsigned char (*bases)[8]; static unsigned char *pivmask;
static void gen_subspaces(int k) {
  bases = malloc(200000 * 8); pivmask = malloc(200000); nsub = 0;
  for (int P = 0; P < (1 << D); P++) {
    if (__builtin_popcount(P) != k) continue;
    int piv[8], r = 0; for (int q = 0; q < D; q++) if ((P >> q) & 1) piv[r++] = q;
    int nfree[8], tot = 0, freepos[8][8];
    for (int i = 0; i < k; i++) { nfree[i] = 0; for (int q = piv[i] + 1; q < D; q++) if (!((P >> q) & 1)) freepos[i][nfree[i]++] = q; tot += nfree[i]; }
    for (long code = 0; code < (1L << tot); code++) { long c = code;
      for (int i = 0; i < k; i++) { unsigned char b = 1 << piv[i]; for (int j = 0; j < nfree[i]; j++) { if (c & 1) b |= 1 << freepos[i][j]; c >>= 1; } bases[nsub][i] = b; }
      pivmask[nsub++] = P; }
  }
}
static u64 anf(u64 t, int k) { static const u64 M[6] = {0x5555555555555555ULL,0x3333333333333333ULL,0x0f0f0f0f0f0f0f0fULL,0x00ff00ff00ff00ffULL,0x0000ffff0000ffffULL,0x00000000ffffffffULL};
  for (int i = 0; i < k; i++) t ^= (t & M[i]) << (1 << i); return t; }
static int is_affine_small(u64 t, int k) { /* k <= 6 */ t = anf(t, k); if (k < 6) t &= (1ULL << (1 << k)) - 1;
  u64 allow = 1; for (int i = 0; i < k; i++) allow |= 1ULL << (1 << i); return (t & ~allow) == 0; }
int main(int argc, char **argv) {
  int Mg = atoi(argv[1]), k = atoi(argv[2]); D = 2 * Mg; NPT = 1 << D;
  if (k > 6) { fprintf(stderr, "use formal4 for k=7\n"); return 1; }
  unsigned char *mc4 = malloc(65536); FILE *f4 = fopen("../EXP-010-level4-certificates/mc4.bin", "rb"); if (fread(mc4, 1, 65536, f4) != 65536) return 2; fclose(f4);
  unsigned char *mc5 = 0;
  if (k == 5) { int fd = open("../EXP-010-level4-certificates/mc5.mc5", O_RDONLY); struct stat st; fstat(fd, &st); mc5 = mmap(0, st.st_size, PROT_READ, MAP_SHARED, fd, 0); }
  gen_subspaces(k);
  T W[8]; for (int t = 0; t < D; t++) { memset(&W[t], 0, sizeof(T)); for (int p = 0; p < NPT; p++) if ((p >> t) & 1) W[t].w[p >> 6] |= 1ULL << (p & 63); }
  /* wirings: alpha_i <= beta_i for i >= 1, gamma over gates 0..M-2 */
  int nw = 0; static int wir[20000][9];
  int lim[4] = {1, 2, 4, 8};
  int al[4] = {0}, be[4] = {0};
  for (int a1 = 0; a1 < (Mg > 1 ? lim[1] : 1); a1++) for (int b1 = a1; b1 < (Mg > 1 ? lim[1] : 1); b1++)
  for (int a2 = 0; a2 < (Mg > 2 ? lim[2] : 1); a2++) for (int b2 = a2; b2 < (Mg > 2 ? lim[2] : 1); b2++)
  for (int a3 = 0; a3 < (Mg > 3 ? lim[3] : 1); a3++) for (int b3 = a3; b3 < (Mg > 3 ? lim[3] : 1); b3++)
  for (int gm = 0; gm < (1 << (Mg - 1)); gm++) { int *w = wir[nw++]; w[0]=a1; w[1]=a2; w[2]=a3; w[3]=b1; w[4]=b2; w[5]=b3; w[6]=gm; }
  (void)al; (void)be;
  long mcd[16] = {0}, nsurv = 0, ng = 0, nout = 0;
  int ncos = 1 << (D - k);
  #pragma omp parallel for schedule(dynamic, 4) reduction(+:nsurv,ng,nout)
  for (int wi = 0; wi < nw; wi++) {
    int *w = wir[wi]; int A_[4] = {0, w[0], w[1], w[2]}, B_[4] = {0, w[3], w[4], w[5]};
    T z[4];
    for (int i = 0; i < Mg; i++) { T A = W[2*i], B = W[2*i+1];
      for (int j = 0; j < i; j++) { if ((A_[i] >> j) & 1) A = txor(A, z[j]); if ((B_[i] >> j) & 1) B = txor(B, z[j]); }
      z[i] = tand(A, B); }
    T Phi = z[Mg - 1]; for (int j = 0; j < Mg - 1; j++) if ((w[6] >> j) & 1) Phi = txor(Phi, z[j]);
    for (int s = 0; s < nsub; s++) {
      u64 tab[64]; memset(tab, 0, sizeof(tab)); int P = pivmask[s];
      int reps[64], nr = 0; for (int c = 0; c < NPT; c++) if (!(c & P)) reps[nr++] = c;
      for (int ci = 0; ci < nr; ci++) for (int t = 0; t < (1 << k); t++) { int q = reps[ci]; for (int r = 0; r < k; r++) if ((t >> r) & 1) q ^= bases[s][r]; if (bit(&Phi, q)) tab[ci] |= 1ULL << t; }
      int aff[64]; for (int c = 0; c < ncos; c++) aff[c] = is_affine_small(tab[c], k);
      for (int i = 0; i < ncos; i++) if (aff[i]) { nsurv++;
        for (int j = 0; j < ncos; j++) if (j != i && !aff[j]) { ng++;
          int m;
          if (k <= 4) { u32 g = (u32)tab[j]; for (int kk = k; kk < 4; kk++) g |= g << (1 << kk); m = mc4[g & 0xffff]; }
          else if (k == 5) { u32 g = (u32)tab[j]; m = (mc5[g >> 1] >> ((g & 1) * 4)) & 15; }
          else { m = 15; nout++; }
          #pragma omp atomic
          mcd[m]++;
        } }
    }
  }
  printf("M=%d k=%d wirings=%d subspaces=%d survivors=%ld g=%ld  MC(g) dist:", Mg, k, nw, nsub, nsurv, ng);
  for (int m = 0; m < 6; m++) printf(" %d:%ld", m, mcd[m]); if (nout) printf(" (k=6 not evaluated: %ld)", nout);
  printf("  -> level-%d counterexamples here: %ld\n", Mg, k <= 5 ? mcd[Mg] + mcd[Mg+1] : -1L);
  return 0;
}
