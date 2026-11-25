/* Exact MC of every 5-variable function, stored as one byte per function (4 GiB would be too much), so we store
   a 2-bit code per function in a 1 GiB array: code = min(MC,3) ... no: MC in {0..4}; store 0..4 in 4 bits (2 GiB).
   Simpler and smaller: we only need MC5(f) for f; computed from: affine test, S1 (rebuilt here), S2 = W2 elements
   (rebuilt here), S3 bitmap (EXP-007).  Output mc5.mc5: 4-bit values, two functions per byte (2 GiB). */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef uint32_t u32;
static const u32 X[5] = {0xAAAAAAAAu, 0xCCCCCCCCu, 0xF0F0F0F0u, 0xFF00FF00u, 0xFFFF0000u};
typedef struct { int k; u32 v[12]; } Basis;
static int badd(Basis *B, u32 v) { for (int i = 0; i < B->k; i++) { int p = 31 - __builtin_clz(B->v[i]); if ((v >> p) & 1) v ^= B->v[i]; }
  if (!v) return 0; int p = 31 - __builtin_clz(v); for (int i = 0; i < B->k; i++) if ((B->v[i] >> p) & 1) B->v[i] ^= v; B->v[B->k++] = v; return 1; }
static u32 bred(const Basis *B, u32 v) { for (int i = 0; i < B->k; i++) { int p = 31 - __builtin_clz(B->v[i]); if ((v >> p) & 1) v ^= B->v[i]; } return v; }
static void span(const u32 *g, int k, u32 *o) { o[0] = 0; for (int i = 0; i < k; i++) { int n = 1 << i; for (int j = 0; j < n; j++) o[n + j] = o[j] ^ g[i]; } }
static uint8_t *mc;  /* 4 bits per function */
static void setmin(u32 f, int v) { uint8_t *b = &mc[f >> 1]; int sh = (f & 1) * 4; int cur = (*b >> sh) & 15; if (v < cur) *b = (uint8_t)((*b & ~(15 << sh)) | (v << sh)); }
int main(void) {
  mc = malloc((size_t)1 << 31); memset(mc, 0x44, (size_t)1 << 31);            /* default MC = 4 */
  uint8_t *s3 = malloc((size_t)1 << 29); FILE *fi = fopen("../EXP-007-s3-five-variables/s3_5vars.bitmap", "rb");
  if (fread(s3, 1, (size_t)1 << 29, fi) != ((size_t)1 << 29)) return 1; fclose(fi);
  for (uint64_t f = 0; f < ((uint64_t)1 << 32); f++) if ((s3[f >> 3] >> (f & 7)) & 1) setmin((u32)f, 3);
  u32 gen0[6] = {0xFFFFFFFFu, X[0], X[1], X[2], X[3], X[4]}, W0[64]; span(gen0, 6, W0);
  for (int i = 0; i < 64; i++) setmin(W0[i], 0);
  for (int l1 = 1; l1 < 32; l1++) for (int l2 = l1 + 1; l2 < 32; l2++) if ((l1 ^ l2) > l2) {
    u32 a = 0, b = 0; for (int j = 0; j < 5; j++) { if ((l1 >> j) & 1) a ^= X[j]; if ((l2 >> j) & 1) b ^= X[j]; }
    u32 z1 = a & b; Basis B1 = {0}; for (int i = 0; i < 6; i++) badd(&B1, gen0[i]); badd(&B1, z1);
    for (int i = 0; i < 64; i++) setmin(W0[i] ^ z1, 1);
    u32 q1[6] = {X[0], X[1], X[2], X[3], X[4], z1}, e1[64]; span(q1, 6, e1);
    for (int x = 1; x < 64; x++) for (int y = x + 1; y < 64; y++) if ((x ^ y) > y) {
      u32 r = bred(&B1, e1[x] & e1[y]); if (!r) continue;
      u32 g8[8] = {0xFFFFFFFFu, X[0], X[1], X[2], X[3], X[4], z1, r}, w2[256]; span(g8, 8, w2);
      for (int k = 0; k < 256; k++) setmin(w2[k], 2);
    }
  }
  uint64_t cnt[5] = {0}; for (uint64_t f = 0; f < ((uint64_t)1 << 32); f++) cnt[(mc[f >> 1] >> ((f & 1) * 4)) & 15]++;
  printf("MC distribution on 5 variables: 0:%llu 1:%llu 2:%llu 3:%llu 4:%llu\n", (unsigned long long)cnt[0], (unsigned long long)cnt[1], (unsigned long long)cnt[2], (unsigned long long)cnt[3], (unsigned long long)cnt[4]);
  FILE *fo = fopen("mc5.mc5", "wb"); fwrite(mc, 1, (size_t)1 << 31, fo); fclose(fo);
  return 0;
}
