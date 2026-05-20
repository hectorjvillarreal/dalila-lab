#!/usr/bin/env python3
"""Read ge_summary CSVs from baseline and the two experiments, and print
LaTeX-ready table rows for Tables 7 and 8 of Integrated_6_seminar.tex.

Usage:  python3 postprocess_experiments.py

Expects (in current dir):
  ge_summary.csv             (baseline κ=0.50, τ^m=0)
  ge_summary_kappa30.csv     (κ=0.30 reform)
  ge_summary_taum20.csv      (τ^m=-0.20 subsidy)

Outputs to stdout a block of `\\todo{run}` → numeric replacements that can
be sed-applied to Integrated_6_seminar.tex.
"""

import csv
from pathlib import Path
import sys

HERE = Path(__file__).parent


def load(name):
    p = HERE / name
    if not p.exists():
        return None
    out = {}
    with p.open() as fh:
        for row in csv.DictReader(fh):
            v = row["value"].strip().rstrip(")").rstrip("(")
            try:
                out[row["metric"]] = float(v)
            except ValueError:
                pass
    return out


def lifecycle_h_at_age60(name):
    """Mean health stock at age 60 (period 9), unweighted across skill types."""
    p = HERE / name
    if not p.exists():
        return None
    h_vals = []
    with p.open() as fh:
        for row in csv.DictReader(fh):
            if int(row["age_period"]) == 9:
                h_vals.append(float(row["h"]))
    return sum(h_vals) / len(h_vals) if h_vals else None


def pct(x):           return f"{100*x:.2f}\\%"
def num(x, d=3):      return f"{x:.{d}f}"
def signed_pp(x):     return f"{'+' if x >= 0 else ''}{100*x:.2f}~pp"
def signed_pct(x):    return f"{'+' if x >= 0 else ''}{100*x:.2f}\\%"
def signed_num(x, d=3): return f"{'+' if x >= 0 else ''}{x:.{d}f}"


def annual_r(r5y):
    """Convert 5-year rate to annual rate."""
    return (1 + r5y) ** (1 / 5) - 1


def kov_y_annual(K, Y):
    """K/Y in annual units = (K/Y_5yr) / 5."""
    return (K / Y) / 5


def report_kappa(base, reform):
    print("=" * 70)
    print("EXPERIMENT 1: κ = 0.50 → κ = 0.30  (Table 7)")
    print("=" * 70)

    rows = []
    def row(label, b, r, fmt=num):
        d = r - b
        rows.append((label, fmt(b), fmt(r), fmt(d) if not fmt is pct else signed_pp(d)))

    # τ^p
    rows.append(("τ^p", pct(base["taup"]), pct(reform["taup"]),
                 signed_pp(reform["taup"] - base["taup"])))
    # r annual
    rb = annual_r(base["r_5yr"])
    rr = annual_r(reform["r_5yr"])
    rows.append(("r (annual)", pct(rb), pct(rr), signed_pp(rr - rb)))
    # w
    rows.append(("w", num(base["w"], 3), num(reform["w"], 3),
                 signed_num(reform["w"] - base["w"], 3)))
    # K/Y annual
    kyb = kov_y_annual(base["K"], base["Y"])
    kyr = kov_y_annual(reform["K"], reform["Y"])
    rows.append(("K/Y (annual)", pct(kyb), pct(kyr), signed_pp(kyr - kyb)))
    # C/Y
    rows.append(("C/Y", pct(base["C_over_Y"]), pct(reform["C_over_Y"]),
                 signed_pp(reform["C_over_Y"] - base["C_over_Y"])))
    # M/Y
    rows.append(("M/Y", pct(base["M_over_Y"]), pct(reform["M_over_Y"]),
                 signed_pp(reform["M_over_Y"] - base["M_over_Y"])))
    # B/Y
    byb = base["B_debt"] / base["Y"]
    byr = reform["B_debt"] / reform["Y"]
    rows.append(("B/Y", pct(byb), pct(byr), signed_pp(byr - byb)))
    # pension benefit
    rows.append(("pen", num(base["pen"], 3), num(reform["pen"], 3),
                 signed_num(reform["pen"] - base["pen"], 3)))
    # W1
    rows.append(("W1(θ_L)", num(base["W1_theta_L"], 3), num(reform["W1_theta_L"], 3), "---"))
    rows.append(("W1(θ_H)", num(base["W1_theta_H"], 3), num(reform["W1_theta_H"], 3), "---"))
    # CEV — placeholder; CEV requires the lifecycle paths
    # As a rough orientation: under CRRA, Δ ≈ (W^p' / W^p)^(1/(1-γ)) - 1
    # With γ=2.0 and W>0, this gives a usable orientation.
    cev_L, cev_H = None, None  # proper CEV requires GHH lifecycle paths
    rows.append(("ΔW₁/W₁(θ_L)", "---",
                 signed_pct((reform["W1_theta_L"] - base["W1_theta_L"]) / base["W1_theta_L"]), "---"))
    rows.append(("ΔW₁/W₁(θ_H)", "---",
                 signed_pct((reform["W1_theta_H"] - base["W1_theta_H"]) / base["W1_theta_H"]), "---"))

    for label, b, r, d in rows:
        print(f"  {label:30s}  baseline={b:>10s}  reform={r:>10s}  Δ={d}")


def report_taum(base, subsidy):
    print()
    print("=" * 70)
    print("EXPERIMENT 2: τ^m = 0 → τ^m = -0.20  (Table 8)")
    print("=" * 70)

    rows = []
    rows.append(("M/Y", pct(base["M_over_Y"]), pct(subsidy["M_over_Y"]),
                 signed_pp(subsidy["M_over_Y"] - base["M_over_Y"])))
    h60_b = lifecycle_h_at_age60("ge_lifecycle.csv")
    h60_s = lifecycle_h_at_age60("ge_lifecycle_taum20.csv")
    if h60_b is not None and h60_s is not None:
        rows.append(("h̄ at age 60", num(h60_b, 3), num(h60_s, 3),
                     signed_num(h60_s - h60_b, 3)))
    rows.append(("τ^p", pct(base["taup"]), pct(subsidy["taup"]),
                 signed_pp(subsidy["taup"] - base["taup"])))
    rb = annual_r(base["r_5yr"])
    rs = annual_r(subsidy["r_5yr"])
    rows.append(("r (annual)", pct(rb), pct(rs), signed_pp(rs - rb)))
    rows.append(("w", num(base["w"], 3), num(subsidy["w"], 3),
                 signed_num(subsidy["w"] - base["w"], 3)))
    rows.append(("L", num(base["L"], 3), num(subsidy["L"], 3),
                 signed_num(subsidy["L"] - base["L"], 3)))
    rows.append(("Y", num(base["Y"], 3), num(subsidy["Y"], 3),
                 signed_num(subsidy["Y"] - base["Y"], 3)))
    byb = base["B_debt"] / base["Y"]
    bys = subsidy["B_debt"] / subsidy["Y"]
    rows.append(("B/Y", pct(byb), pct(bys), signed_pp(bys - byb)))
    rows.append(("W1(θ_L)", num(base["W1_theta_L"], 3), num(subsidy["W1_theta_L"], 3), "---"))
    rows.append(("W1(θ_H)", num(base["W1_theta_H"], 3), num(subsidy["W1_theta_H"], 3), "---"))
    gamma = 2.0
    cev_L = (subsidy["W1_theta_L"] / base["W1_theta_L"]) ** (1 / (1 - gamma)) - 1
    cev_H = (subsidy["W1_theta_H"] / base["W1_theta_H"]) ** (1 / (1 - gamma)) - 1
    rows.append(("ΔW₁/W₁(θ_L)", "---",
                 signed_pct((subsidy["W1_theta_L"] - base["W1_theta_L"]) / base["W1_theta_L"]), "---"))
    rows.append(("ΔW₁/W₁(θ_H)", "---",
                 signed_pct((subsidy["W1_theta_H"] - base["W1_theta_H"]) / base["W1_theta_H"]), "---"))

    for label, b, r, d in rows:
        print(f"  {label:30s}  baseline={b:>10s}  subsidy={r:>10s}  Δ={d}")


def main():
    base = load("ge_summary.csv")
    kap = load("ge_summary_kappa30.csv")
    tau = load("ge_summary_taum20.csv")

    if base is None:
        print("FATAL: ge_summary.csv missing", file=sys.stderr)
        sys.exit(1)

    if kap is not None:
        report_kappa(base, kap)
    else:
        print("(ge_summary_kappa30.csv not yet present — skipping)")

    if tau is not None:
        report_taum(base, tau)
    else:
        print("(ge_summary_taum20.csv not yet present — skipping)")


if __name__ == "__main__":
    main()
