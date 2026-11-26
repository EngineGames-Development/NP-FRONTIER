/* EXP-019 (part 2): necessary condition for a level-5 counterexample, tested on NIST's complete list of 6-variable
 * classes of MC 5 (github.com/usnistgov/circuits, data/mc_dim/mc5_dim6.txt).
 *
 * Claim (Lemma 36 of PNE-001-codim3.md): if MC(g) = 5 = MC(y*g), then dim g = 6 (Corollary 35) and g has a "cheap plane":
 * linearly independent directions v1, v2 such that for every nonzero v in span(v1, v2) both halves g|<v,x>=c have
 * MC <= 3. The property is invariant under affine equivalence (input maps and addition of affine functions), so it can be
 * tested on class representatives.
 * A direction v is cheap iff both halves (5-variable functions; any affine parametrisation of the hyperplane) lie in
 * S_3 = {MC <= 3}, read from the exact table mc5.mc5 of EXP-007/EXP-010 (4 bits per 5-variable function; values <= 3
 * are exact, 4 means "not in S_3").
 * Output: number of representatives with a cheap plane; those representatives (ANF lines) on stdout with "CHEAP".
 * Build: gcc -O2 -o cheapplane6 cheapplane6.c ;  run: ./cheapplane6 mc5_dim6.txt mc5.mc5
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
typedef uint64_t u64; typedef uint32_t u32;
static unsigned char *mc5;
static int mc_of(u32 g) { return (mc5[g >> 1] >> ((g & 1) * 4)) & 15; }
static u64 parse_anf(const char *s) { /* "x1x2+x3..." over x1..x6, "0"/"1" constants; returns truth table (bit p = f(p), x_i = bit i-1 of p) */
  u64 tt = 0; const char *p = s;
  while (*p && *p != '\n') {
    int mono = 0; int isone = 0;
    while (*p && *p != '+' && *p != '\n') { if (*p == 'x') { p++; int v = 0; while (*p >= '0' && *p <= '9') v = v * 10 + (*p++ - '0'); mono |= 1 << (v - 1); }
      else if (*p == '1') { isone = 1; p++; } else if (*p == '0') { p++; mono = -1; } else p++; }
    if (mono > 0 || isone) { for (int x = 0; x < 64; x++) if ((x & mono) == mono) tt ^= 1ULL << x; }
    if (*p == '+') p++;
  }
  return tt;
}
static u32 half(u64 f, int v, int c) { /* restriction of f to <v,x> = c, parametrised by the 5 coordinates other than pivot */
  int piv = __builtin_ctz(v); u32 r = 0;
  for (int t = 0; t < 32; t++) { int lo = t & ((1 << piv) - 1), hi = t >> piv; int x = lo | (hi << (piv + 1));
    int par = __builtin_popcount(x & v) & 1; if (par != c) x |= 1 << piv; /* now <v,x> = c */
    if ((f >> x) & 1) r |= 1u << t; }
  return r;
}
int main(int argc, char **argv) {
  FILE *in = fopen(argv[1], "r"); int fd = open(argv[2], O_RDONLY); struct stat st; fstat(fd, &st);
  mc5 = mmap(0, st.st_size, PROT_READ, MAP_SHARED, fd, 0); if (mc5 == MAP_FAILED) { perror("mmap"); return 1; }
  /* self-test of the table on a few known functions: AND of 5 has MC 4; x1x2x3x4 has MC 3; x1x2+x3x4 has MC 2 */
  u32 and5 = 1u << 31, and4 = 0, q = 0; for (int x = 0; x < 32; x++) { if ((x & 15) == 15) and4 |= 1u << x; if (((x & 1) & ((x >> 1) & 1)) ^ (((x >> 2) & 1) & ((x >> 3) & 1))) q |= 1u << x; }
  fprintf(stderr, "self-test: MC(AND5)=%d (4), MC(x1x2x3x4)=%d (3), MC(x1x2+x3x4)=%d (2)\n", mc_of(and5), mc_of(and4), mc_of(q));
  char line[4096]; long nrep = 0, ncheap = 0, hist[64] = {0}; long nplanes_tot = 0;
  while (fgets(line, sizeof line, in)) {
    if (line[0] == '\n' || line[0] == 0) continue;
    u64 f = parse_anf(line); nrep++;
    u64 cheapdirs = 0; int ncd = 0;
    for (int v = 1; v < 64; v++) { if (mc_of(half(f, v, 0)) <= 3 && mc_of(half(f, v, 1)) <= 3) { cheapdirs |= 1ULL << v; ncd++; } }
    hist[ncd]++;
    int planes = 0;
    for (int v1 = 1; v1 < 64; v1++) if ((cheapdirs >> v1) & 1) for (int v2 = v1 + 1; v2 < 64; v2++) if ((cheapdirs >> v2) & 1) { int v3 = v1 ^ v2; if (v3 > v2 && ((cheapdirs >> v3) & 1)) planes++; }
    if (planes) { ncheap++; nplanes_tot += planes; printf("CHEAP planes=%d cheapdirs=%d %s", planes, ncd, line); }
  }
  fprintf(stderr, "representatives: %ld | with a cheap plane: %ld (total cheap planes %ld)\n", nrep, ncheap, nplanes_tot);
  fprintf(stderr, "histogram of #cheap directions:"); for (int i = 0; i < 64; i++) if (hist[i]) fprintf(stderr, " %d:%ld", i, hist[i]); fprintf(stderr, "\n");
  return 0;
}
