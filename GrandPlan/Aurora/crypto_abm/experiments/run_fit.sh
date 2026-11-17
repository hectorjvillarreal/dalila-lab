#!/usr/bin/env bash
# Launch the B1a rough fit inside a Zellij session (CLAUDE.md: jobs > 5 min), sleep inhibited.
set -uo pipefail
cd "$(dirname "$0")/.."
LOG=experiments/results/fit_$(date +%Y%m%d_%H%M).log
systemd-inhibit --what=sleep:idle --why="crypto ABM B1a fit" \
  julia -t 16 --project=. experiments/fit.jl search "${1:-2000}" > "$LOG" 2>&1
echo "exit $? $(date)" >> "$LOG"
