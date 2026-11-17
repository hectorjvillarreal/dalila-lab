#!/usr/bin/env bash
# Rerun every B1a result after the Cath/Fina sign-off fixes (2026-11-17), sleep inhibited.
set -uo pipefail
cd "$(dirname "$0")/.."
LOG=experiments/results/b1a_rerun_$(date +%Y%m%d_%H%M).log
inh() { systemd-inhibit --what=sleep:idle --why="crypto ABM B1a rerun" "$@"; }
{
echo "== linear fit $(date)";   ABM_IMPACT=linear inh julia -t 16 --project=. experiments/fit.jl search 2000
FL=$(ls -t experiments/results/fit_linear_*.txt | head -1)
echo "== linear ablations $(date)"; ABM_IMPACT=linear inh julia -t 16 --project=. experiments/ablations_bestfit.jl "$FL"
echo "== linear recovery $(date)";  ABM_IMPACT=linear inh julia -t 16 --project=. experiments/fit.jl recover 8 "$FL"
echo "== sqrt fit $(date)";     ABM_IMPACT=sqrt inh julia -t 16 --project=. experiments/fit.jl search 2000
FS=$(ls -t experiments/results/fit_sqrt_*.txt | head -1)
echo "== sqrt ablations $(date)";   ABM_IMPACT=sqrt inh julia -t 16 --project=. experiments/ablations_bestfit.jl "$FS"
echo "== null and timing $(date)";  ABM_IMPACT=linear inh julia -t 1 --project=. experiments/null_and_timing.jl "$FL"
echo "== first run (defaults) $(date)"; inh julia -t 1 --project=. experiments/first_run.jl
echo "exit 0 $(date)"
} > "$LOG" 2>&1
