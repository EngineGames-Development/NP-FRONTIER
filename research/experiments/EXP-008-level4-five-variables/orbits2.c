/* EXP-008 step 2 (BFS version): orbits of the MC-4 members of F5 under the group preserving F5
   (AGL(2) on (x1,x2), AGL(3) on u, shears u <- u + N(x1,x2), complementation; all preserve MC(g) and MC(y*g)).
   For every family member with MC 4 that is not yet visited, BFS its orbit with the generators, using a 2^32-bit
   visited bitmap.  Output: orbit representatives (first member found) with orbit sizes. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef uint32_t u32;
static inline int getb(const uint8_t *bm, u32 f) { return (bm[f >> 3] >> (f & 7)) & 1; }
static inline void setb(uint8_t *bm, u32 f) { bm[f >> 3] |= (uint8_t)(1u << (f & 7)); }
static int perm[16][32], ngen = 0;
#define B(p,i) (((p) >> (i)) & 1)
static int mk(int x1, int x2, int u1, int u2, int u3) { return x1 | x2 << 1 | u1 << 2 | u2 << 3 | u3 << 4; }
static void addgen(int k) { for (int p = 0; p < 32; p++) { int q;
  switch (k) { case 0: q = p ^ 1; break; case 1: q = p ^ 2; break; case 2: q = p ^ 4; break; case 3: q = p ^ 8; break; case 4: q = p ^ 16; break;
    case 5: q = mk(B(p,1), B(p,0), B(p,2), B(p,3), B(p,4)); break;            /* swap x1,x2 */
    case 6: q = mk(B(p,0) ^ B(p,1), B(p,1), B(p,2), B(p,3), B(p,4)); break;   /* x1 <- x1+x2 */
    case 7: q = mk(B(p,0), B(p,1), B(p,3), B(p,2), B(p,4)); break;            /* swap u1,u2 */
    case 8: q = mk(B(p,0), B(p,1), B(p,4), B(p,3), B(p,2)); break;            /* swap u1,u3 */
    case 9: q = mk(B(p,0), B(p,1), B(p,2) ^ B(p,3), B(p,3), B(p,4)); break;   /* u1 <- u1+u2 */
    default: q = mk(B(p,0), B(p,1), B(p,2) ^ B(p,0), B(p,3), B(p,4)); break;  /* shear u1 <- u1+x1 */
  } perm[ngen][p] = q; } ngen++; }
static u32 apply(u32 g, int k) { u32 h = 0; for (int p = 0; p < 32; p++) h |= ((g >> perm[k][p]) & 1u) << p; return h; }
int main(int argc, char **argv) {
  for (int k = 0; k <= 10; k++) addgen(k);
  uint8_t *s3 = malloc((size_t)1 << 29), *vis = calloc((size_t)1 << 29, 1);
  FILE *fi = fopen(argv[1], "rb"); if (!fi || fread(s3, 1, (size_t)1 << 29, fi) != ((size_t)1 << 29)) return 1; fclose(fi);
  int dl[128], nd = 0; for (int t = 0; t < 256; t++) if (!__builtin_parity(t)) dl[nd++] = t;
  u32 *queue = malloc(sizeof(u32) * 20000000); long long norb = 0, covered = 0, bad = 0;
  FILE *fo = fopen("orbit_reps.txt", "w");
  for (int g00 = 0; g00 < 256; g00++) for (int i1 = 0; i1 < nd; i1++) for (int i2 = 0; i2 < nd; i2++) for (int i3 = 0; i3 < nd; i3++) {
    int d1 = dl[i1], d2 = dl[i2], d12 = dl[i3]; u32 g = 0;
    for (int u = 0; u < 8; u++) { int a = (g00 >> u) & 1, b1 = (d1 >> u) & 1, b2 = (d2 >> u) & 1, b3 = (d12 >> u) & 1;
      g |= (u32)a << (4*u) | (u32)(a ^ b1) << (4*u+1) | (u32)(a ^ b2) << (4*u+2) | (u32)(a ^ b1 ^ b2 ^ b3) << (4*u+3); }
    if (getb(s3, g) || getb(vis, g)) continue;
    long long qh = 0, qt = 0; queue[qt++] = g; setb(vis, g);
    while (qh < qt) { u32 f = queue[qh++];
      for (int k = 0; k <= ngen; k++) { u32 h = (k < ngen) ? apply(f, k) : ~f;
        if (getb(vis, h)) continue;
        if (getb(s3, h)) { bad++; continue; }                  /* would mean the group does not preserve MC: must stay 0 */
        setb(vis, h); queue[qt++] = h; } }
    norb++; covered += qt; fprintf(fo, "0x%08x %lld\n", g, qt);
  }
  fclose(fo);
  printf("orbits %lld, members covered %lld (expected 337784832), MC-violating images %lld\n", norb, covered, bad);
  return 0;
}
