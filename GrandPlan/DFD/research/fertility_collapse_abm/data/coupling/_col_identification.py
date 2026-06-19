#!/usr/bin/env python3
"""
Stage 1.5 Addendum A -- Colombia identification analysis (Q1-Q4).

Colombia is the gate's decisive case: the ONLY collapse country with an OBSERVED
annual national TFR (DANE EEVV, COL_tfr_national.csv) to pair against the coupling
path, so the Q1 lead test is properly evaluable here (Check B of the addendum).

Inputs
  coupling/COL_coupling_annual.csv          (this work; GEIH 2007-2024, 12-mo pooled)
  national/COL_tfr_national.csv             (Stage 1; DANE EEVV observed, 2015-2024)

Two coupling measures are tested (the marriage-margin refinement, Anne's caution):
  union_total  = cohabiting + married        (any co-residential union)
  married      = marriage-weighted union     (married only; cohabitation excluded)
If modern LAC cohabitation is an increasingly low-/deferred-fertility state, the
fertility-relevant coupling variable is the marriage-weighted one. Colombia's high
baseline cohabitation makes it the sharp test.

Outputs: console verdicts + coupling/COL_identification.csv + COL_coupling_vs_tfr.png
"""
import csv, os
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
NAT  = os.path.normpath(os.path.join(HERE, "..", "national"))
BANDS = ["20-24", "25-29", "30-34", "35-39"]

# ---- load coupling: per band/year shares + n; build 20-39 aggregates ----------
rows = list(csv.DictReader(open(os.path.join(HERE, "COL_coupling_annual.csv"))))
years = sorted({int(r["year"]) for r in rows})
share = {m: {b: {} for b in BANDS} for m in ("union_total", "married", "cohabiting")}
agg = {m: {} for m in ("union_total", "married")}   # n-weighted 20-39 aggregate
for y in years:
    num = {m: 0.0 for m in agg}; den = 0.0
    for b in BANDS:
        r = next(x for x in rows if int(x["year"]) == y and x["age_band"] == b)
        n = float(r["n_women_weighted"]); den += n
        for m in ("union_total", "married", "cohabiting"):
            share[m][b][y] = float(r[m])
        for m in agg:
            num[m] += float(r[m]) * n
    for m in agg:
        agg[m][y] = num[m] / den

# ---- load OBSERVED DANE EEVV TFR (never modeled/World Bank) -- Check B ---------
tfr = {int(r["year"]): float(r["value"])
       for r in csv.DictReader(open(os.path.join(NAT, "COL_tfr_national.csv")))}
tfr_years = sorted(tfr)
common = [y for y in years if y in tfr]   # overlap window for the lead test


def yoy(d):
    ys = sorted(d)
    return {ys[i]: (d[ys[i]] - d[ys[i-1]]) / (ys[i] - ys[i-1]) for i in range(1, len(ys))}

def corr(a, b):
    n = len(a); ma = sum(a)/n; mb = sum(b)/n
    num = sum((x-ma)*(y-mb) for x, y in zip(a, b))
    da = (sum((x-ma)**2 for x in a))**.5; db = (sum((y-mb)**2 for y in b))**.5
    return num/(da*db) if da*db else 0

def turn_year(d):
    """Year of the series peak (last local max) -- the down-turn point."""
    ys = sorted(d); peak = max(ys, key=lambda y: d[y]); return peak


print("=== Colombia coupling (20-39 aggregate, %) vs OBSERVED DANE TFR ===")
print(f"{'yr':4} {'union%':>7} {'marr%':>6} {'TFR':>5}")
for y in years:
    t = f"{tfr[y]:.2f}" if y in tfr else "  . "
    print(f"{y} {agg['union_total'][y]*100:7.1f} {agg['married'][y]*100:6.1f} {t:>5}")

# ---- Q1: lead-lag against OBSERVED TFR, for BOTH coupling measures -------------
print("\n=== Q1 LEAD TEST (corr of differenced series; coupling leads if best k>0) ===")
print(f"    overlap window: {common[0]}-{common[-1]} (observed TFR)")
dt = yoy({y: tfr[y] for y in common})
q1 = {}
for meas in ("union_total", "married"):
    dc = yoy({y: agg[meas][y] for y in common})
    best = None
    print(f"  [{meas}]")
    for k in (-2, -1, 0, 1, 2):
        pairs = [(dt[y], dc[y-k]) for y in dt if (y in dt and (y-k) in dc)]
        if len(pairs) < 5:
            continue
        c = corr([p[0] for p in pairs], [p[1] for p in pairs])
        tag = (f"coupling LEADS by {k}" if k > 0 else
               "simultaneous" if k == 0 else f"coupling LAGS by {-k}")
        print(f"    k={k:+d}: r={c:+.2f}  ({tag}; n={len(pairs)})")
        if best is None or abs(c) > abs(best[1]):
            best = (k, c)
    q1[meas] = best
    print(f"    -> best alignment k={best[0]:+d} (r={best[1]:+.2f})")

# turn-point comparison (robust to the 1-decimal TFR rounding)
print("\n  turn-point (series peak) comparison:")
print(f"    union_total peaks {turn_year(agg['union_total'])}, "
      f"married peaks {turn_year(agg['married'])}, TFR peaks {turn_year(tfr)}")

# ---- Q2: nonlinearity locus -- coupling-side vs map-side -----------------------
print("\n=== Q2 nonlinearity locus (coupling-side vs map-side) ===")
for meas in ("union_total", "married"):
    dc = yoy(agg[meas]); steep = min(dc, key=lambda y: dc[y])
    pk = turn_year(agg[meas])   # peak year -> robust decline magnitude (ignores odd first year)
    print(f"  [{meas}] steepest annualized drop ~{steep} ({dc[steep]*100:+.2f} pts/yr); "
          f"peak {pk} {agg[meas][pk]*100:.1f}% -> {years[-1]} {agg[meas][years[-1]]*100:.1f}% "
          f"({(agg[meas][years[-1]]-agg[meas][pk])*100:+.1f} pts)")
print("  (coupling-side = accelerating partnership decline [Mexico-like]; "
      "map-side = smooth coupling but sudden TFR [Costa-Rica-like])")

# ---- Q3: cascade -- youngest-first? -------------------------------------------
print("\n=== Q3 cascade: steepest annualized-decline interval per band (youngest-first?) ===")
for b in BANDS:
    d = yoy(share["union_total"][b]); ay = min(d, key=lambda y: d[y])
    print(f"  {b}: steepest~{ay} ({d[ay]*100:+.2f}/yr); "
          f"level {share['union_total'][b][years[0]]*100:.0f}%->{share['union_total'][b][years[-1]]*100:.0f}%")

# ---- Q4: independence ----------------------------------------------------------
print("\n=== Q4 independence ===")
print("  Coupling = DANE GEIH household-roster estado civil (P6070, survey).")
print("  TFR = DANE EEVV vital registration (births). Different instruments -> NO circularity.")

# ---- write summary csv ---------------------------------------------------------
with open(os.path.join(HERE, "COL_identification.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["year", "coupling_union_20_39", "coupling_married_20_39", "tfr_observed"])
    for y in years:
        w.writerow([y, round(agg["union_total"][y], 4), round(agg["married"][y], 4),
                    tfr.get(y, "")])

# ---- charts --------------------------------------------------------------------
fig, (a1, a2) = plt.subplots(2, 1, figsize=(8.5, 7.5),
                             gridspec_kw=dict(height_ratios=[3, 2], hspace=0.28))
ax2 = a1.twinx()
a1.plot(years, [agg["union_total"][y]*100 for y in years], color="#2166ac", lw=2.3,
        marker="o", label="union total 20-39 (%)")
a1.plot(years, [agg["married"][y]*100 for y in years], color="#5aae61", lw=2.0,
        marker="^", label="married only 20-39 (%)")
ax2.plot(tfr_years, [tfr[y] for y in tfr_years], color="#b2182b", lw=2.3,
         marker="s", label="TFR (observed DANE EEVV)")
a1.set_ylabel("women 20-39 in union (%)"); ax2.set_ylabel("TFR", color="#b2182b")
a1.set_title("Colombia -- coupling (total vs marriage-weighted) vs observed TFR, "
             f"{years[0]}-{years[-1]}")
a1.grid(alpha=.25); a1.legend(loc="lower left", fontsize=8)
for b in BANDS:
    a2.plot(years, [share["union_total"][b].get(y, float('nan'))*100 for y in years],
            marker=".", label=b)
a2.set_title("coupling by age band (%) -- cascade check"); a2.set_xlabel("year")
a2.legend(fontsize=7, ncol=4); a2.grid(alpha=.25)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "COL_coupling_vs_tfr.png"), dpi=130)
plt.close(fig)
print("\nwrote COL_identification.csv + COL_coupling_vs_tfr.png")
