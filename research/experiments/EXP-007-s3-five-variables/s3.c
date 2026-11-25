/* EXP-007: exact set S_3 = {5-variable Boolean functions with MC <= 3}, as a 2^32-bit bitmap. No SAT solver.
   A k-AND circuit computes exactly the functions in span(W0, z1..zk), z_i = A_i*B_i with A_i,B_i in span(W0,z_<i).
   Gate i's product modulo W_{i-1} depends only on the 2-dim subspace span(A_i,B_i) of W_{i-1}/<1>
   ((A+1)B = AB+B, A(A+B) = AB+A), so one representative pair per 2-dim subspace suffices.
   Truth tables: bit p = f(x), x_j = bit (j-1) of p.  Output: s3_5vars.bitmap (bit f set iff MC(f) <= 3),
   plus S_2 count for validation.  Build: gcc -O2 -fopenmp -o s3 s3.c */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>
typedef uint32_t u32; typedef uint64_t u64;
static const u32 X[5] = {0xAAAAAAAAu, 0xCCCCCCCCu, 0xF0F0F0F0u, 0xFF00FF00u, 0xFFFF0000u};
static const u32 ONE = 0xFFFFFFFFu;
typedef struct { int k; u32 v[12]; } Basis;          /* fully reduced echelon; pivot = highest set bit */
static int badd(Basis *B, u32 v) {
  for (int i = 0; i < B->k; i++) { int p = 31 - __builtin_clz(B->v[i]); if ((v >> p) & 1) v ^= B->v[i]; }
  if (!v) return 0;
  int p = 31 - __builtin_clz(v);
  for (int i = 0; i < B->k; i++) if ((B->v[i] >> p) & 1) B->v[i] ^= v;
  B->v[B->k++] = v; return 1;
}
static u32 bred(const Basis *B, u32 v) {
  for (int i = 0; i < B->k; i++) { int p = 31 - __builtin_clz(B->v[i]); if ((v >> p) & 1) v ^= B->v[i]; }
  return v;
}
static int span_elems(const u32 *gen, int k, u32 *out) {   /* all 2^k XOR-combinations */
  out[0] = 0; for (int i = 0; i < k; i++) { int n = 1 << i; for (int j = 0; j < n; j++) out[n + j] = out[j] ^ gen[i]; }
  return 1 << k;
}
static int cmpu(const void *a, const void *b) { u32 x = *(const u32 *)a, y = *(const u32 *)b; return x < y ? -1 : x > y; }
static int uniq(u32 *a, int n) { qsort(a, n, sizeof(u32), cmpu); int m = 0; for (int i = 0; i < n; i++) if (!m || a[m-1] != a[i]) a[m++] = a[i]; return m; }
static inline void mark(uint8_t *bm, u32 f) { bm[f >> 3] |= (uint8_t)(1u << (f & 7)); }
static inline int getb(const uint8_t *bm, u32 f) { return (bm[f >> 3] >> (f & 7)) & 1; }

int main(void) {
  u32 z1s[200]; int nz1 = 0;
  for (int l1 = 1; l1 < 32; l1++) for (int l2 = l1 + 1; l2 < 32; l2++) if ((l1 ^ l2) > l2) {
    u32 a = 0, b = 0; for (int j = 0; j < 5; j++) { if ((l1 >> j) & 1) a ^= X[j]; if ((l2 >> j) & 1) b ^= X[j]; }
    z1s[nz1++] = a & b; }
  int T = omp_get_max_threads();
  uint8_t **bm = malloc(T * sizeof(uint8_t *));
  for (int t = 0; t < T; t++) { bm[t] = calloc((size_t)1 << 29, 1); if (!bm[t]) { fprintf(stderr, "alloc\n"); return 1; } }
  u32 **s2list = malloc(T * sizeof(u32 *)); size_t *s2n = calloc(T, sizeof(size_t));
  for (int t = 0; t < T; t++) s2list[t] = malloc(sizeof(u32) * 200 * 700 * 256 / T + 1000000);
  long long cosets3 = 0, w2count = 0;
  #pragma omp parallel for schedule(dynamic, 1) reduction(+:cosets3, w2count)
  for (int i1 = 0; i1 < nz1; i1++) {
    int t = omp_get_thread_num();
    Basis B1 = {0}; badd(&B1, ONE); for (int j = 0; j < 5; j++) badd(&B1, X[j]); badd(&B1, z1s[i1]);
    u32 q1[6]; for (int j = 0; j < 5; j++) q1[j] = X[j]; q1[5] = z1s[i1];
    u32 e1[64]; span_elems(q1, 6, e1);
    u32 R2[700]; int n2 = 0;
    for (int a = 1; a < 64; a++) for (int b = a + 1; b < 64; b++) if ((a ^ b) > b) { u32 r = bred(&B1, e1[a] & e1[b]); if (r) R2[n2++] = r; }
    n2 = uniq(R2, n2);
    for (int i2 = 0; i2 < n2; i2++) {
      w2count++;
      u32 q2[7]; memcpy(q2, q1, sizeof q1); q2[6] = R2[i2];
      Basis B2 = B1; badd(&B2, R2[i2]);
      u32 e2[128]; span_elems(q2, 7, e2);
      u32 w2[256]; u32 gen8[8]; gen8[0] = ONE; memcpy(gen8 + 1, q2, sizeof q2); span_elems(gen8, 8, w2);
      for (int k = 0; k < 256; k++) { mark(bm[t], w2[k]); s2list[t][s2n[t]++] = w2[k]; }
      u32 R3[2700]; int n3 = 0;
      for (int a = 1; a < 128; a++) for (int b = a + 1; b < 128; b++) if ((a ^ b) > b) { u32 r = bred(&B2, e2[a] & e2[b]); if (r) R3[n3++] = r; }
      n3 = uniq(R3, n3); cosets3 += n3;
      for (int i3 = 0; i3 < n3; i3++) { u32 r = R3[i3]; for (int k = 0; k < 256; k++) mark(bm[t], w2[k] ^ r); }
    }
  }
  for (int t = 1; t < T; t++) { u64 *d = (u64 *)bm[0], *s = (u64 *)bm[t]; for (size_t i = 0; i < ((size_t)1 << 26); i++) d[i] |= s[i]; }
  /* S_2 count from the collected W2 elements */
  size_t tot = 0; for (int t = 0; t < T; t++) tot += s2n[t];
  u32 *all = malloc(sizeof(u32) * tot); size_t pos = 0; for (int t = 0; t < T; t++) { memcpy(all + pos, s2list[t], sizeof(u32) * s2n[t]); pos += s2n[t]; }
  int ns2 = uniq(all, (int)tot);
  u64 s3 = 0, s3odd = 0; for (u64 f = 0; f < ((u64)1 << 32); f++) if (getb(bm[0], (u32)f)) { s3++; if (__builtin_parity((u32)f)) s3odd++; }
  printf("z1 classes %d, W2 spaces %lld, third-gate cosets %lld\n", nz1, w2count, cosets3);
  printf("|S_2| = %d   |S_3| = %llu   odd-weight (degree-5) members of S_3: %llu\n", ns2, (unsigned long long)s3, (unsigned long long)s3odd);
  FILE *fo = fopen("s3_5vars.bitmap", "wb"); fwrite(bm[0], 1, (size_t)1 << 29, fo); fclose(fo);
  return 0;
}
