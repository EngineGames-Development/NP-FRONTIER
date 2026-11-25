#!/usr/bin/env bash
# Independent cross-check of the two EXP-006 certificates: SAT (CaDiCaL) on "MC(y*G') <= 3" with a DRAT proof,
# checked by drat-trim. Expected: UNSAT and "s VERIFIED" for both orbit representatives.
set -euo pipefail
cd "$(dirname "$0")/../EXP-002-restriction-depth"
DRAT="${DRAT:-$HOME/.local/bin/drat-trim}"
for g in 0x01234567 0x0167abcd; do
  echo "== G' = $g"
  timeout 3000 python3 -u drat_certify.py "$g" 3 "level3_$g"
  timeout 7000 "$DRAT" "level3_$g.cnf" "level3_$g.drat" -t 7000 | grep -E "^s |verification time"
done
