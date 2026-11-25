#!/usr/bin/env bash
# Reproduce the DRAT certificate for "no 3-AND circuit computes y*g*" (g* = 0xfff3d212). Needs drat-trim on PATH or $DRAT.
set -euo pipefail
cd "$(dirname "$0")"
timeout 3000 python3 -u drat_certify.py 0xfff3d212 3 yg_star_k3
timeout 6000 "${DRAT:-drat-trim}" yg_star_k3.cnf yg_star_k3.drat -t 6000 | tail -5
