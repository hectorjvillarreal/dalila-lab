#!/usr/bin/env bash
# Launch the B1a parameter-recovery test inside Zellij, sleep inhibited.
set -uo pipefail
cd "$(dirname "$0")/.."
LOG=experiments/results/recover_$(date +%Y%m%d_%H%M).log
systemd-inhibit --what=sleep:idle --why="crypto ABM B1a recovery" \
  julia -t 16 --project=. experiments/fit.jl recover "${1:-8}" "$2" > "$LOG" 2>&1
echo "exit $? $(date)" >> "$LOG"
