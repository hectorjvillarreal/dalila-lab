#!/usr/bin/env bash
# B1b timing gate inside Zellij, sleep inhibited.
set -uo pipefail
cd "$(dirname "$0")/.."
LOG=experiments/results/b1b_timing_$(date +%Y%m%d_%H%M).log
FL=$(ls -t experiments/results/fit_linear_*.txt | head -1); FS=$(ls -t experiments/results/fit_sqrt_*.txt | head -1)
systemd-inhibit --what=sleep:idle --why="crypto ABM B1b gate" \
  julia -t 16 --project=. experiments/b1b_timing.jl "$FL" "$FS" > "$LOG" 2>&1
echo "exit $? $(date)" >> "$LOG"
