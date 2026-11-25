/* EXP-008 step 2: orbits of the MC-4 members of F5 under the group preserving F5:
   T(x1,x2,u) = (A(x1,x2)+c, M u + N(x1,x2) + c'), A in GL(2), M in GL(3), N any 3x2 matrix, plus complementation.
   All these are affine bijections of the input space (y untouched), so they preserve MC(g) and MC(y*g).
   Index p = x1 + 2 x2 + 4 u.  Union-find over generators.  Output: orbit count, and representatives with sizes. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef uint32_t u32;
static int cmpu(const void *a, const void *b) { u32 x = *(const u32 *)a, y = *(const u32 *)b; return x < y ? -1 : x > y; }
static int perm[16][32], ngen = 0;
static void addgen(int (*f)(int)) { for (int p = 0; p < 32; p++) perm[ngen][p] = f(p); ngen++; }
#define B(p,i) (((p) >> (i)) & 1)
static int mk(int x1, int x2, int u1, int u2, int u3) { return x1 | x2 << 1 | u1 << 2 | u2 << 3 | u3 << 4; }
static int t0(int p) { return p ^ 1; }  static int t1(int p) { return p ^ 2; }  static int t2(int p) { return p ^ 4; }
static int t3(int p) { return p ^ 8; }  static int t4(int p) { return p ^ 16; }
static int sx(int p) { return mk(B(p,1), B(p,0), B(p,2), B(p,3), B(p,4)); }                 /* swap x1,x2 */
static int ax(int p) { return mk(B(p,0) ^ B(p,1), B(p,1), B(p,2), B(p,3), B(p,4)); }        /* x1 <- x1+x2 */
static int s12(int p) { return mk(B(p,0), B(p,1), B(p,3), B(p,2), B(p,4)); }                /* swap u1,u2 */
static int s13(int p) { return mk(B(p,0), B(p,1), B(p,4), B(p,3), B(p,2)); }                /* swap u1,u3 */
static int au(int p) { return mk(B(p,0), B(p,1), B(p,2) ^ B(p,3), B(p,3), B(p,4)); }        /* u1 <- u1+u2 */
static int sh(int p) { return mk(B(p,0), B(p,1), B(p,2) ^ B(p,0), B(p,3), B(p,4)); }        /* shear u1 <- u1+x1 */
static u32 apply(u32 g, int k) { u32 h = 0; for (int p = 0; p < 32; p++) h |= ((g >> perm[k][p]) & 1u) << p; return h; }
static u32 *A; static u32 *par; static size_t N;
static size_t find(size_t i) { while (par[i] != i) { par[i] = par[par[i]]; i = par[i]; } return i; }
static long long idx(u32 f) { size_t lo = 0, hi = N; while (lo < hi) { size_t m = (lo + hi) / 2; if (A[m] < f) lo = m + 1; else hi = m; } return (lo < N && A[lo] == f) ? (long long)lo : -1; }
int main(void) {
  addgen(t0); addgen(t1); addgen(t2); addgen(t3); addgen(t4); addgen(sx); addgen(ax); addgen(s12); addgen(s13); addgen(au); addgen(sh);
  FILE *fi = fopen("mc4_members.u32", "rb"); fseek(fi, 0, SEEK_END); N = ftell(fi) / 4; rewind(fi);
  A = malloc(N * 4); if (fread(A, 4, N, fi) != N) return 1; fclose(fi);
  qsort(A, N, 4, cmpu);
  par = malloc(N * 4); for (size_t i = 0; i < N; i++) par[i] = (u32)i;
  long long outside = 0;
  for (size_t i = 0; i < N; i++) {
    for (int k = 0; k <= ngen; k++) {
      u32 h = (k < ngen) ? apply(A[i], k) : ~A[i];
      long long j = idx(h); if (j < 0) { outside++; continue; }
      size_t a = find(i), b = find((size_t)j); if (a != b) { if (a < b) par[b] = (u32)a; else par[a] = (u32)b; }
    }
  }
  size_t norb = 0; for (size_t i = 0; i < N; i++) if (find(i) == i) norb++;
  printf("members %zu, images outside MC-4 family (must be 0): %lld, orbits %zu\n", N, outside, norb);
  u32 *sz = calloc(N, 4); for (size_t i = 0; i < N; i++) sz[find(i)]++;
  FILE *fo = fopen("orbit_reps.txt", "w"); for (size_t i = 0; i < N; i++) if (par[i] == i) fprintf(fo, "0x%08x %u\n", A[i], sz[i]); fclose(fo);
  return 0;
}
