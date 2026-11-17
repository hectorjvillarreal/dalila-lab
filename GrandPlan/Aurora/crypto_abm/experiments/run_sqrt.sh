#!/usr/bin/env bash
# Clearing-rule alternative (note §6.3, criterion 10): refit under square-root impact, then ablations.
set -uo pipefail
cd "$(dirname "$0")/.."
export ABM_IMPACT=sqrt
LOG=experiments/results/fit_sqrt_$(date +%Y%m%d_%H%M).log
systemd-inhibit --what=sleep:idle --why="crypto ABM sqrt-impact fit" \
  julia -t 16 --project=. experiments/fit.jl search 2000 > "$LOG" 2>&1
FIT=$(ls -t experiments/results/fit_sqrt_*.txt | head -1)
systemd-inhibit --what=sleep:idle --why="crypto ABM sqrt ablations" \
  julia -t 16 --project=. experiments/ablations_bestfit.jl "$FIT" >> "$LOG" 2>&1
echo "exit $? $(date)" >> "$LOG"
