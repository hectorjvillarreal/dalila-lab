#!/usr/bin/env python3
"""assemble_calibrated.py — build the §§4-5 comparison + welfare-change tables.

Reads the per-run summary/welfare CSVs produced by run1prime.jl and the
calibrated_lib.jl writers (run2/run3/run4), and emits:

  results/calibrated_comparison.csv     — one column per run (Run 1', κ=0.30,
                                           τm=−0.20, aging C1); rows = the §6
                                           aggregate metrics + 4 welfare cells.
  results/calibrated_welfare_change.csv — %ΔW vs Run 1' by (g,θ) for Runs 2-4
                                           (the §5 incidence content).

It also prints a readable table and evaluates the cross-run §5 gates.

Welfare-change metric: proportional change in the lifetime welfare object,
%ΔW = (W − W_run1prime)/|W_run1prime| × 100. Positive = welfare gain (W is the
GHH-CRRA expected lifetime utility at birth, negative-valued; a less-negative W
is an improvement, so the sign works). This is NOT a calibrated consumption-
equivalent variation — an exact CEV is not closed-form here because the additive
health-amenity term breaks the homogeneity of the GHH composite. The formal CEV
transform (if wanted for the paper) is a §5 LaTeX-session decision; this metric
gives the correct incidence DIRECTION for gates 6 (regressive) and 8 (progressive).
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")

RUNS = [
    ("run1prime", "Run 1' (baseline)"),
    ("run2_kappa30", "Run 2 (κ=0.30)"),
    ("run3_taum20", "Run 3 (τm=−0.20)"),
    ("run4_agingC1", "Run 4 (aging C1)"),
]

SUMMARY_ROWS = ["K", "L", "Y", "r_annual_pct", "r_5yr", "w", "tau_p", "pen",
                "B", "B_over_Y", "C_over_Y", "M_over_Y", "N_W", "N_R", "dep_ratio"]
WELFARE_CELLS = [("M", "theta_L"), ("M", "theta_H"),
                 ("F", "theta_L"), ("F", "theta_H")]


def load_summary(tag):
    path = os.path.join(RESULTS, f"{tag}_summary.csv")
    if not os.path.isfile(path):
        return None
    d = {}
    with open(path) as f:
        r = csv.reader(f)
        next(r, None)  # header
        for row in r:
            if len(row) == 2:
                d[row[0]] = float(row[1])
    return d


def load_welfare(tag):
    path = os.path.join(RESULTS, f"{tag}_welfare.csv")
    if not os.path.isfile(path):
        return None
    d = {}
    with open(path) as f:
        r = csv.reader(f)
        next(r, None)  # header
        for row in r:
            if len(row) == 3:
                d[(row[0], row[1])] = float(row[2])
    return d


def main():
    summ, welf, missing = {}, {}, []
    for tag, _ in RUNS:
        s, w = load_summary(tag), load_welfare(tag)
        if s is None or w is None:
            missing.append(tag)
        summ[tag], welf[tag] = s, w
    if missing:
        print(f"MISSING (not finished?): {', '.join(missing)}", file=sys.stderr)
        print("Aborting — rerun once all four runs have written their CSVs.",
              file=sys.stderr)
        sys.exit(1)

    labels = [lab for _, lab in RUNS]
    tags = [t for t, _ in RUNS]

    # ── comparison CSV ────────────────────────────────────────────────────
    comp_path = os.path.join(RESULTS, "calibrated_comparison.csv")
    with open(comp_path, "w", newline="") as f:
        wtr = csv.writer(f)
        wtr.writerow(["metric"] + labels)
        for m in SUMMARY_ROWS:
            wtr.writerow([m] + [f"{summ[t][m]:.6f}" for t in tags])
        for (g, th) in WELFARE_CELLS:
            wtr.writerow([f"W1_{g}_{th}"] +
                         [f"{welf[t][(g, th)]:.6f}" for t in tags])
    print(f"Wrote {comp_path}")

    # ── welfare-change CSV (%ΔW vs Run 1') ────────────────────────────────
    base = welf["run1prime"]
    wc_path = os.path.join(RESULTS, "calibrated_welfare_change.csv")
    with open(wc_path, "w", newline="") as f:
        wtr = csv.writer(f)
        wtr.writerow(["sex", "skill"] + labels[1:])  # runs 2-4
        for (g, th) in WELFARE_CELLS:
            b = base[(g, th)]
            pcts = [(welf[t][(g, th)] - b) / abs(b) * 100 for t in tags[1:]]
            wtr.writerow([g, th] + [f"{p:.4f}" for p in pcts])
    print(f"Wrote {wc_path}")

    # ── readable table ────────────────────────────────────────────────────
    def line(name, key, fmt="{:>14.4f}", scale=1.0):
        cells = "".join(fmt.format(summ[t][key] * scale) for t in tags)
        print(f"  {name:<22}{cells}")

    print("\n" + "=" * 78)
    print("  CALIBRATED COMPARISON — §§4-5 (harmonized baseline + 3 experiments)")
    print("=" * 78)
    print(f"  {'':<22}" + "".join(f"{lab:>14}" for lab in
          ["Run1'", "κ=0.30", "τm=-0.20", "agingC1"]))
    line("K (capital)", "K")
    line("L (labor)", "L")
    line("Y (output)", "Y")
    line("r (annual %)", "r_annual_pct")
    line("w (wage)", "w")
    line("τp (%)", "tau_p", "{:>14.2f}", 100.0)
    line("pen", "pen")
    line("B", "B")
    line("B/Y (%)", "B_over_Y", "{:>14.2f}", 100.0)
    line("C/Y (%)", "C_over_Y", "{:>14.2f}", 100.0)
    line("M/Y (%)", "M_over_Y", "{:>14.3f}", 100.0)
    line("N_W", "N_W")
    line("N_R", "N_R")
    line("dep_ratio", "dep_ratio")
    print("\n  Welfare at birth W₁(g,θ):")
    for (g, th) in WELFARE_CELLS:
        cells = "".join(f"{welf[t][(g, th)]:>14.4f}" for t in tags)
        print(f"    {g},{th:<18}{cells}")

    print("\n  Proportional welfare change vs Run 1' (%ΔW, + = gain):")
    print(f"    {'':<20}" + "".join(f"{lab:>14}" for lab in
          ["κ=0.30", "τm=-0.20", "agingC1"]))
    for (g, th) in WELFARE_CELLS:
        b = base[(g, th)]
        cells = "".join(f"{(welf[t][(g, th)] - b) / abs(b) * 100:>13.3f}%"
                        for t in tags[1:])
        print(f"    {g},{th:<18}{cells}")

    # ── cross-run §5 gates ────────────────────────────────────────────────
    def ok(b):
        return "PASS" if b else "⚠ CHECK"

    s1, s2, s3, s4 = (summ[t] for t in tags)
    w_base = base

    def dW(tag, g, th):
        b = w_base[(g, th)]
        return (welf[tag][(g, th)] - b) / abs(b) * 100

    print("\n  Cross-run §5 gates:")
    print(f"    [R2-5] κ=0.30 → τp falls : "
          f"{100*s1['tau_p']:.2f}% → {100*s2['tau_p']:.2f}%  "
          f"{ok(s2['tau_p'] < s1['tau_p'] - 1e-4)}")
    r2_reg = dW("run2_kappa30", "M", "theta_L") < dW("run2_kappa30", "M", "theta_H") \
        and dW("run2_kappa30", "F", "theta_L") < dW("run2_kappa30", "F", "theta_H")
    print(f"    [R2-6] κ regressive (θ_L loses more, both sexes) : {ok(r2_reg)}")
    print(f"    [R3-7] τm=−0.20 → M/Y rises : "
          f"{100*s1['M_over_Y']:.3f}% → {100*s3['M_over_Y']:.3f}%  "
          f"{ok(s3['M_over_Y'] > s1['M_over_Y'])}")
    r3_prog = dW("run3_taum20", "M", "theta_L") > dW("run3_taum20", "M", "theta_H") \
        and dW("run3_taum20", "F", "theta_L") > dW("run3_taum20", "F", "theta_H")
    print(f"    [R3-8] τm progressive (θ_L gains more, both sexes) : {ok(r3_prog)}")
    print(f"    [R3-9] τm → τp rises (survival) : "
          f"{100*s1['tau_p']:.2f}% → {100*s3['tau_p']:.2f}%  "
          f"{ok(s3['tau_p'] >= s1['tau_p'] - 1e-4)}")
    print(f"    [R4-10] aging dep_ratio ~doubles : "
          f"{s1['dep_ratio']:.4f} → {s4['dep_ratio']:.4f}  "
          f"(×{s4['dep_ratio']/s1['dep_ratio']:.2f})")
    print(f"    [R4-11] aging → τp rises substantially : "
          f"{100*s1['tau_p']:.2f}% → {100*s4['tau_p']:.2f}%  "
          f"{ok(s4['tau_p'] > s1['tau_p'] + 1e-3)}")
    print(f"    [R4-12] aging → K rises, r falls : "
          f"K {s1['K']:.3f}→{s4['K']:.3f} {ok(s4['K'] > s1['K'])} | "
          f"r {100*s1['r_annual_pct']/100:.3f}→{s4['r_annual_pct']:.3f}% "
          f"{ok(s4['r_annual_pct'] < s1['r_annual_pct'])}")


if __name__ == "__main__":
    main()
