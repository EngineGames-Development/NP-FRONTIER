#!/usr/bin/env bash
# Idempotent environment setup for NP-FRONTIER. Every step checks first and skips work already done,
# so it is safe to run at the start of every session.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLCHAIN="$(tr -d '[:space:]' < "$ROOT/research/proofs/lean/lean-toolchain")"   # e.g. leanprover/lean4:v4.37.0-rc1
V="${TOOLCHAIN##*:v}"
export PATH="$HOME/.elan/bin:$PATH"
say() { printf '[setup] %s\n' "$*"; }

# 1. elan (installer script and GitHub release assets are reachable)
if command -v elan >/dev/null 2>&1; then say "elan present: $(elan --version 2>/dev/null | head -1)"
else say "installing elan"; curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --default-toolchain none; fi

# 2. Lean toolchain. `elan toolchain install` fails behind this network policy (release.lean-lang.org is
#    blocked), so download the release asset from GitHub into the directory elan expects.
D="$HOME/.elan/toolchains/leanprover--lean4---v$V"
if [ -x "$D/bin/lean" ]; then say "toolchain $V present"
else
  command -v zstd >/dev/null 2>&1 || { say "installing zstd"; apt-get update -q >/dev/null && apt-get install -y -q zstd >/dev/null; }
  say "downloading Lean $V"; mkdir -p "$D"
  curl -sSfL "https://github.com/leanprover/lean4/releases/download/v$V/lean-$V-linux.tar.zst" | tar --zstd -xf - -C "$D" --strip-components=1
fi
elan default "$TOOLCHAIN" >/dev/null 2>&1 || true

# 3. Python packages for experiments (pip skips anything already satisfied).
REQ="$ROOT/research/experiments/requirements.txt"
if [ -f "$REQ" ]; then
  if python3 -m pip install -q -r "$REQ" 2>/dev/null || python3 -m pip install -q --break-system-packages -r "$REQ"; then say "python requirements satisfied"; fi
fi

# 4. drat-trim (independent DRAT proof checker for SAT-solver UNSAT claims).
DRAT_BIN="$HOME/.local/bin/drat-trim"
if [ -x "$DRAT_BIN" ]; then say "drat-trim present"
else
  say "building drat-trim"; mkdir -p "$HOME/.local/bin"
  curl -sSfL https://raw.githubusercontent.com/marijnheule/drat-trim/master/drat-trim.c -o "$HOME/.local/bin/drat-trim.c"
  gcc -O2 -o "$DRAT_BIN" "$HOME/.local/bin/drat-trim.c"
fi

# 5. Report state (does not modify anything).
say "lean: $(lean --version 2>/dev/null || echo MISSING)"
[ -f "$ROOT/research/current_state.md" ] && say "research state exists: continue from research/current_state.md (CLAUDE.md Section 13)" \
                                        || say "no research state yet: first session (CLAUDE.md Section 15)"
