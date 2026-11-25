/* EXP-010: exact decision of "MC(F) <= 4" for 6-variable F with MC(F) >= 4 (here F = y*g, MC(g) = 4).
   Inputs: x1..x5 = bits 0..4 of the point index, y = bit 5.  Exact MC tables: mc5.mc5 (all 5-variable functions,
   EXP-007/010) and mc4.bin (all 4-variable functions, EXP-001).
   Search (all filters are NECESSARY conditions for an optimal 4-gate circuit; the last step is exact):
   1. first gate: a plane {u1,u2,u1+u2} of directions, each with both restrictions of MC <= 3 (Lemma 9');
      z1 = L(u1)L(u2) modulo affine terms (W1 depends only on the plane);
   2. second gate z2 = A*B, one pair per 2-dim subspace of W1/<1>.  For each first-gate restriction r with
      MC(F|r) = 3 the restricted circuit is optimal, so z2|r must be non-degenerate and its direction plane
      admissible for F|r at level 3 (restrictions of MC <= 2);
   3. third gate z3, one pair per 2-dim subspace of W2/<1>; on each double restriction r & {w = c'} (w in the
      plane of z2|r) with MC(F|..) = 2, z3 restricted must be non-degenerate with plane admissible at level 2;
   4. fourth gate: exact test F in W3 + span(A*B) over all 2-dim subspaces of W3/<1>.
   Output: FOUND (with witness) or NONE (= MC(F) >= 5).  Build: gcc -O2 -o cert4 cert4.c */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
typedef uint64_t u64; typedef uint32_t u32; typedef uint16_t u16;
static uint8_t *mc5tab, mc4tab[65536];
static int MC5(u32 f) { return (mc5tab[f >> 1] >> ((f & 1) * 4)) & 15; }
static int MC4(u16 f) { return mc4tab[f]; }
static int MC3(uint8_t f) { return mc4tab[(u16)(f | (f << 8))]; }          /* dummy 4th variable */
static u64 X6[6];
static int pts6[64][2][32], pts5[32][2][16], pts4[16][2][8];
static void mkpts(int n, int u, int c, int *out) {
  int piv = 31 - __builtin_clz(u), bas[8], nb = 0;
  for (int j = 0; j < n; j++) if (j != piv) { int b = 1 << j; if ((u >> j) & 1) b |= 1 << piv; bas[nb++] = b; }
  int p0 = c ? (1 << piv) : 0;
  for (int t = 0; t < (1 << (n - 1)); t++) { int p = p0; for (int i = 0; i < nb; i++) if ((t >> i) & 1) p ^= bas[i]; out[t] = p; }
}
static u32 r6(u64 f, int u, int c) { u32 r = 0; for (int t = 0; t < 32; t++) r |= (u32)((f >> pts6[u][c][t]) & 1) << t; return r; }
static u16 r5(u32 f, int w, int c) { u16 r = 0; for (int t = 0; t < 16; t++) r |= (u16)((f >> pts5[w][c][t]) & 1) << t; return r; }
static uint8_t r4(u16 f, int q, int c) { uint8_t r = 0; for (int t = 0; t < 8; t++) r |= (uint8_t)((f >> pts4[q][c][t]) & 1) << t; return r; }
/* direction of an affine function on k variables; returns -1 if not affine */
static int adir(u64 f, int k) { int f0 = f & 1, d = 0; for (int j = 0; j < k; j++) d |= (int)(((f >> (1 << j)) & 1) ^ f0) << j;
  for (int t = 0; t < (1 << k); t++) if ((int)((f >> t) & 1) != (f0 ^ __builtin_parity(d & t))) return -1; return d; }
typedef struct { int k; u64 v[12]; } Basis;
static int badd(Basis *B, u64 v) { for (int i = 0; i < B->k; i++) { int p = 63 - __builtin_clzll(B->v[i]); if ((v >> p) & 1) v ^= B->v[i]; }
  if (!v) return 0; int p = 63 - __builtin_clzll(v); for (int i = 0; i < B->k; i++) if ((B->v[i] >> p) & 1) B->v[i] ^= v; B->v[B->k++] = v; return 1; }
static u64 bred(const Basis *B, u64 v) { for (int i = 0; i < B->k; i++) { int p = 63 - __builtin_clzll(B->v[i]); if ((v >> p) & 1) v ^= B->v[i]; } return v; }
static void span(const u64 *g, int k, u64 *o) { o[0] = 0; for (int i = 0; i < k; i++) { int n = 1 << i; for (int j = 0; j < n; j++) o[n + j] = o[j] ^ g[i]; } }
static u64 L6(int u) { u64 t = 0; for (int j = 0; j < 6; j++) if ((u >> j) & 1) t ^= X6[j]; return t; }
static long long stat_planes, stat_s2, stat_s3, stat_final;
/* restriction data */
typedef struct { int u, c, mc; u32 Fr; } R1;
static int check(u64 F, u64 wit[8]) {
  int adm[64]; for (int u = 1; u < 64; u++) adm[u] = MC5(r6(F, u, 0)) <= 3 && MC5(r6(F, u, 1)) <= 3;
  for (int u1 = 1; u1 < 64; u1++) for (int u2 = u1 + 1; u2 < 64; u2++) {
    int u3 = u1 ^ u2; if (u3 < u2 || !adm[u1] || !adm[u2] || !adm[u3]) continue;
    stat_planes++; if (getenv("MAXPLANES") && stat_planes > atoi(getenv("MAXPLANES"))) return 0;
    if (getenv("PROGRESS")) fprintf(stderr, "plane %lld (%d,%d) cum z2=%lld z3=%lld t=%.0fs\n", stat_planes, u1, u2, stat_s2, stat_s3, (double)clock()/CLOCKS_PER_SEC);
    u64 z1 = L6(u1) & L6(u2);
    Basis B1 = {0}; badd(&B1, ~0ull); for (int j = 0; j < 6; j++) badd(&B1, X6[j]); badd(&B1, z1);
    u64 q1[7]; for (int j = 0; j < 6; j++) q1[j] = X6[j]; q1[6] = z1; u64 e1[128]; span(q1, 7, e1);
    R1 rr[6]; int dirs[3] = {u1, u2, u3}, nr = 0;
    for (int i = 0; i < 3; i++) for (int c = 0; c < 2; c++) { rr[nr].u = dirs[i]; rr[nr].c = c; rr[nr].Fr = r6(F, dirs[i], c); rr[nr].mc = MC5(rr[nr].Fr); nr++; }
    /* tables for the level-3 filter: restricted directions of W1 elements, admissible directions of F|r */
    static int dir1[6][128]; static char adm3[6][32];
    for (int i = 0; i < nr; i++) { if (rr[i].mc != 3) continue;
      for (int a = 0; a < 128; a++) { dir1[i][a] = adir(r6(e1[a], rr[i].u, rr[i].c), 5); if (dir1[i][a] < 0) { fprintf(stderr, "BUG L2\n"); exit(2); } }
      for (int w = 1; w < 32; w++) adm3[i][w] = MC4(r5(rr[i].Fr, w, 0)) <= 2 && MC4(r5(rr[i].Fr, w, 1)) <= 2; }
    for (int a = 1; a < 128; a++) for (int b = a + 1; b < 128; b++) {
      if ((a ^ b) < b) continue;
      u64 A = e1[a], Bv = e1[b]; u64 r2 = bred(&B1, A & Bv); if (!r2) continue;
      int ok = 1, pl[6][3];
      for (int i = 0; i < nr && ok; i++) {
        if (rr[i].mc != 3) continue;
        int wa = dir1[i][a], wb = dir1[i][b];
        if (wa == 0 || wb == 0 || wa == wb || !adm3[i][wa] || !adm3[i][wb] || !adm3[i][wa ^ wb]) { ok = 0; break; }
        pl[i][0] = wa; pl[i][1] = wb; pl[i][2] = wa ^ wb;
      }
      if (!ok) continue;
      stat_s2++;
      Basis B2 = B1; badd(&B2, r2);
      u64 q2[8]; memcpy(q2, q1, sizeof q1); q2[7] = A & Bv; u64 e2[256]; span(q2, 8, e2);
      int nr2 = 0; static int ru[36], rc[36], rw[36], rc2[36]; static u16 Frr[36];
      for (int i = 0; i < nr; i++) { if (rr[i].mc != 3) continue;
        for (int k = 0; k < 3; k++) for (int c2 = 0; c2 < 2; c2++) { u16 f = r5(rr[i].Fr, pl[i][k], c2);
          if (MC4(f) == 2) { ru[nr2] = rr[i].u; rc[nr2] = rr[i].c; rw[nr2] = pl[i][k]; rc2[nr2] = c2; Frr[nr2] = f; nr2++; } } }
      static int dir2[36][256]; static char adm2[36][16];
      for (int j = 0; j < nr2; j++) {
        for (int a3 = 0; a3 < 256; a3++) { dir2[j][a3] = adir(r5(r6(e2[a3], ru[j], rc[j]), rw[j], rc2[j]), 4); if (dir2[j][a3] < 0) { fprintf(stderr, "BUG L3\n"); exit(2); } }
        for (int q = 1; q < 16; q++) adm2[j][q] = MC3(r4(Frr[j], q, 0)) <= 1 && MC3(r4(Frr[j], q, 1)) <= 1; }
      for (int a3 = 1; a3 < 256; a3++) for (int b3 = a3 + 1; b3 < 256; b3++) {
        if ((a3 ^ b3) < b3) continue;
        int ok3 = 1;
        for (int j = 0; j < nr2; j++) { int qa = dir2[j][a3], qb = dir2[j][b3];
          if (qa == 0 || qb == 0 || qa == qb || !adm2[j][qa] || !adm2[j][qb] || !adm2[j][qa ^ qb]) { ok3 = 0; break; } }
        if (!ok3) continue;
        u64 A3 = e2[a3], B3 = e2[b3]; u64 r3 = bred(&B2, A3 & B3); if (!r3) continue;
        stat_s3++;
        Basis B3b = B2; badd(&B3b, r3);
        u64 t = bred(&B3b, F);
        u64 q3[9]; memcpy(q3, q2, sizeof q2); q3[8] = A3 & B3; static u64 e3[512]; span(q3, 9, e3);
        stat_final++; if (getenv("COUNTONLY")) continue;
        if (t == 0) { wit[0] = L6(u1); wit[1] = L6(u2); wit[2] = A; wit[3] = Bv; wit[4] = A3; wit[5] = B3; wit[6] = 0; wit[7] = 0; return 1; }
        for (int a4 = 1; a4 < 512; a4++) for (int b4 = a4 + 1; b4 < 512; b4++) {
          if ((a4 ^ b4) < b4) continue;
          if (bred(&B3b, e3[a4] & e3[b4]) == t) { wit[0] = L6(u1); wit[1] = L6(u2); wit[2] = A; wit[3] = Bv; wit[4] = A3; wit[5] = B3; wit[6] = e3[a4]; wit[7] = e3[b4]; return 1; }
        }
      }
    }
  }
  return 0;
}
int main(int argc, char **argv) {
  for (int j = 0; j < 6; j++) { X6[j] = 0; for (int p = 0; p < 64; p++) if ((p >> j) & 1) X6[j] |= 1ull << p; }
  for (int u = 1; u < 64; u++) for (int c = 0; c < 2; c++) mkpts(6, u, c, pts6[u][c]);
  for (int u = 1; u < 32; u++) for (int c = 0; c < 2; c++) mkpts(5, u, c, pts5[u][c]);
  for (int u = 1; u < 16; u++) for (int c = 0; c < 2; c++) mkpts(4, u, c, pts4[u][c]);
  mc5tab = malloc((size_t)1 << 31); FILE *f = fopen("mc5.mc5", "rb"); if (fread(mc5tab, 1, (size_t)1 << 31, f) != ((size_t)1 << 31)) return 1; fclose(f);
  f = fopen("mc4.bin", "rb"); if (fread(mc4tab, 1, 65536, f) != 65536) return 1; fclose(f);
  /* args: mode g_hex ...  mode "yg": F = y*g for 5-variable g;  mode "F": F given as 64-bit hex */
  for (int i = 2; i < argc; i++) {
    u64 F;
    if (!strcmp(argv[1], "yg")) { u32 g = (u32)strtoul(argv[i], 0, 16); F = 0; for (int p = 32; p < 64; p++) if ((g >> (p - 32)) & 1) F |= 1ull << p; }
    else F = strtoull(argv[i], 0, 16);
    stat_planes = stat_s2 = stat_s3 = stat_final = 0; u64 wit[8];
    int r = check(F, wit);
    printf("%s %s planes=%lld z2_survivors=%lld z3_survivors=%lld -> %s", argv[1], argv[i], stat_planes, stat_s2, stat_s3, r ? "FOUND" : "NONE");
    if (r) printf(" witness gates: (%016llx)(%016llx) (%016llx)(%016llx) (%016llx)(%016llx) (%016llx)(%016llx)", (unsigned long long)wit[0], (unsigned long long)wit[1], (unsigned long long)wit[2], (unsigned long long)wit[3], (unsigned long long)wit[4], (unsigned long long)wit[5], (unsigned long long)wit[6], (unsigned long long)wit[7]);
    printf("\n"); fflush(stdout);
  }
  return 0;
}
