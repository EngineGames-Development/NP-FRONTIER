/* EXP-008: scan the cheap-plane family F5 (Corollary 21) for members with MC = 4.
   Coordinates: x1 = bit0, x2 = bit1, u = bits 2..4 of the input index p (p = x1 + 2 x2 + 4 u).
   g = g00(u) + x1 d1(u) + x2 d2(u) + x1 x2 d12(u), g00 arbitrary (8-bit table), d_i of degree <= 2
   (8-bit tables of even weight: the u1u2u3 coefficient equals the weight parity).
   MC(g) <= 3 iff g is in the EXP-007 bitmap.  Output: counts, and the list of MC-4 members (u32 truth tables). */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef uint32_t u32;
static inline int getb(const uint8_t *bm, u32 f) { return (bm[f >> 3] >> (f & 7)) & 1; }
int main(int argc, char **argv) {
  uint8_t *bm = malloc((size_t)1 << 29); FILE *fi = fopen(argv[1], "rb");
  if (!fi || fread(bm, 1, (size_t)1 << 29, fi) != ((size_t)1 << 29)) { fprintf(stderr, "bitmap read failed\n"); return 1; }
  fclose(fi);
  int dl[128], nd = 0; for (int t = 0; t < 256; t++) if (!__builtin_parity(t)) dl[nd++] = t;   /* degree <= 2 on 3 vars */
  FILE *fo = fopen("mc4_members.u32", "wb");
  long long total = 0, mc4 = 0;
  for (int g00 = 0; g00 < 256; g00++) for (int i1 = 0; i1 < nd; i1++) for (int i2 = 0; i2 < nd; i2++) for (int i3 = 0; i3 < nd; i3++) {
    int d1 = dl[i1], d2 = dl[i2], d12 = dl[i3]; u32 g = 0;
    for (int u = 0; u < 8; u++) {
      int a = (g00 >> u) & 1, b1 = (d1 >> u) & 1, b2 = (d2 >> u) & 1, b3 = (d12 >> u) & 1;
      g |= (u32)a << (4*u); g |= (u32)(a ^ b1) << (4*u+1); g |= (u32)(a ^ b2) << (4*u+2); g |= (u32)(a ^ b1 ^ b2 ^ b3) << (4*u+3);
    }
    total++;
    if (!getb(bm, g)) { mc4++; fwrite(&g, sizeof g, 1, fo); }
  }
  fclose(fo);
  printf("family members %lld, with MC = 4: %lld\n", total, mc4);
  return 0;
}
