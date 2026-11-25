/* unit test for is_affine() of formal4.c: compare with a direct ANF computation on random and structured tables */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint64_t u64;
#define main formal4_main
#include "formal4.c"
#undef main
static int ref_affine(u64 lo, u64 hi, int k) {
  int a[128]; for (int p = 0; p < (1 << k); p++) a[p] = p < 64 ? (lo >> p) & 1 : (hi >> (p - 64)) & 1;
  for (int i = 0; i < k; i++) for (int p = 0; p < (1 << k); p++) if ((p >> i) & 1) a[p] ^= a[p ^ (1 << i)];
  for (int p = 0; p < (1 << k); p++) if (a[p] && __builtin_popcount(p) >= 2) return 0;
  return 1;
}
int main(void) {
  srand(7); long bad = 0, naff = 0, tot = 0;
  for (int k = 1; k <= 7; k++) for (int it = 0; it < 200000; it++) {
    u64 lo, hi = 0;
    if (it % 2) { /* random affine function */
      int c = rand() & 1; u64 L = 0, H = 0; int coef = rand() & ((1 << k) - 1);
      for (int p = 0; p < (1 << k); p++) { int v = c ^ (__builtin_popcount(p & coef) & 1); if (v) { if (p < 64) L |= 1ULL << p; else H |= 1ULL << (p - 64); } }
      lo = L; hi = H;
      if (it % 4 == 1) { int p = rand() % (1 << k); if (p < 64) lo ^= 1ULL << p; else hi ^= 1ULL << (p - 64); } /* perturb */
    } else { lo = ((u64)rand() << 33) ^ ((u64)rand() << 2) ^ rand(); hi = ((u64)rand() << 33) ^ rand(); }
    if (k < 6) lo &= (1ULL << (1 << k)) - 1;
    if (k < 7) hi = 0;
    int a = is_affine(lo, hi, k), r = ref_affine(lo, hi, k);
    tot++; naff += r; if (a != r) bad++;
  }
  printf("tested %ld tables, %ld affine by reference, mismatches %ld\n", tot, naff, bad);
  return bad != 0;
}
