#!/usr/bin/env python3
"""
Stage 1.5 Addendum B — marriage-series identification rerun (Colombia + Costa Rica).

Builds THREE coupling measures per country from the already-extracted split columns
and reruns Q1-Q4 against OBSERVED national TFR:

  1. total              = married + cohabiting        (w = 1.0; baseline)
  2. fertility-weighted = married + w * cohabiting     (w in {0.4, 0.6, 0.8})
  3. marriage-only      = married                      (w = 0.0 limit)

w (cohabiting-vs-married fertility-intensity ratio) is NOT calibrated; we sweep it as
a sensitivity band and report WHERE the identification verdict flips, if it flips.

The aggregate 20-39 of the fertility-weighted measure is a clean linear blend:
  M_fw(w) = M_marriage + w * (M_total - M_marriage)
so one pass over the bands gives every w.

TEMPO CAVEAT (Anne, mandatory): period TFR is tempo-contaminated. If births are being
postponed, period TFR falls faster/earlier than quantum, dating the fertility turn too
early and biasing every lead test TOWARD "coupling lags." So "no lead / lags" is the
expected finding even if a true lead exists; a lead found DESPITE this bias is strong.

Outputs: COL/CRI_identification_bymeasure.csv + COL/CRI_marriage_rerun.png
"""
import csv, os
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
NAT  = os.path.normpath(os.path.join(HERE, "..", "national"))
BANDS = ["20-24", "25-29", "30-34", "35-39"]
W_BAND = [0.4, 0.6, 0.8]               # fertility-weighted sensitivity band
KS = [-2, -1, 0, 1, 2]

COUNTRIES = {
    "COL": dict(coup="COL_coupling_annual.csv", tfr="COL_tfr_national.csv",
                tfr_note="observed DANE EEVV, chart-label rounded 1 decimal, 2015-2024",
                roster="DANE GEIH P6070"),
    "CRI": dict(coup="CRI_coupling_annual.csv", tfr="CRI_tfr_national.csv",
                tfr_note="observed INEC Panorama Demografico Cuadro 2.2, 2 decimals, 2010-2024",
                roster="INEC ENAHO estado conyugal"),
}


def corr(a, b):
    n = len(a)
    if n < 2:
        return 0.0
    ma, mb = sum(a)/n, sum(b)/n
    num = sum((x-ma)*(y-mb) for x, y in zip(a, b))
    da = (sum((x-ma)**2 for x in a))**.5; db = (sum((y-mb)**2 for y in b))**.5
    return num/(da*db) if da*db else 0.0


def yoy(d):
    ys = sorted(d)
    return {ys[i]: d[ys[i]] - d[ys[i-1]] for i in range(1, len(ys))}


def load(country):
    cfg = COUNTRIES[country]
    rows = list(csv.DictReader(open(os.path.join(HERE, cfg["coup"]))))
    years = sorted({int(r["year"]) for r in rows})
    # per-band marriage / cohab shares + n
    marr = {b: {} for b in BANDS}; coh = {b: {} for b in BANDS}; nw = {b: {} for b in BANDS}
    for y in years:
        for b in BANDS:
            r = next(x for x in rows if int(x["year"]) == y and x["age_band"] == b)
            marr[b][y] = float(r["married"]); coh[b][y] = float(r["cohabiting"])
            nw[b][y] = float(r["n_women_weighted"])
    # n-weighted 20-39 aggregates
    M_marr, M_coh, M_tot = {}, {}, {}
    for y in years:
        den = sum(nw[b][y] for b in BANDS)
        M_marr[y] = sum(marr[b][y]*nw[b][y] for b in BANDS)/den
        M_coh[y]  = sum(coh[b][y]*nw[b][y] for b in BANDS)/den
        M_tot[y]  = M_marr[y] + M_coh[y]
    tfr = {int(r["year"]): float(r["value"])
           for r in csv.DictReader(open(os.path.join(NAT, cfg["tfr"])))}
    return years, marr, coh, nw, M_marr, M_coh, M_tot, tfr


def measure_series(M_marr, M_coh, w):
    """fertility-weighted aggregate at weight w (w=1 -> total, w=0 -> marriage)."""
    return {y: M_marr[y] + w*M_coh[y] for y in M_marr}


def q1(series, tfr):
    common = sorted(set(series) & set(tfr))
    dM = yoy({y: series[y] for y in common}); dT = yoy({y: tfr[y] for y in common})
    prof = {}
    best = None
    for k in KS:
        pairs = [(dT[y], dM[y-k]) for y in dT if (y in dT and (y-k) in dM)]
        if len(pairs) < 5:
            prof[k] = None; continue
        r = corr([p[0] for p in pairs], [p[1] for p in pairs])
        prof[k] = (r, len(pairs))
        if best is None or abs(r) > abs(best[1]):
            best = (k, r)
    return prof, best, common


def q2_locus(series, tfr, common):
    """relative decline of coupling vs TFR over the overlap; ratio<0.5 -> map-side."""
    peak = max(common, key=lambda y: series[y])
    last = common[-1]
    coup_pct = 100*(series[last]-series[peak])/series[peak]
    t0 = common[0]
    tfr_pct = 100*(tfr[last]-tfr[t0])/tfr[t0]
    ratio = abs(coup_pct)/abs(tfr_pct) if tfr_pct else float("inf")
    locus = "map-side" if ratio < 0.5 else ("coupling-side" if ratio > 0.85 else "mixed")
    dM = yoy(series); steep = min((y for y in dM), key=lambda y: dM[y])
    return dict(peak=peak, coup_pct=coup_pct, tfr_pct=tfr_pct, ratio=ratio,
                locus=locus, steep_year=steep, steep_val=dM[steep])


def q3_cascade(perband_share):
    """steepest-decline year per band; youngest-first if order increases with age."""
    steep = {}
    for b in BANDS:
        d = yoy(perband_share[b]); steep[b] = min((y for y in d), key=lambda y: d[y])
    order_ok = (steep["20-24"] <= steep["25-29"] <= steep["30-34"] <= steep["35-39"])
    return steep, order_ok


def perband_measure(marr, coh, w):
    return {b: {y: marr[b][y] + w*coh[b][y] for y in marr[b]} for b in BANDS}


def run_country(country):
    cfg = COUNTRIES[country]
    years, marr, coh, nw, M_marr, M_coh, M_tot, tfr = load(country)
    # measures: marriage(w=0), fw band, total(w=1)
    measures = [("marriage_only", 0.0)] + [("fw_%.1f" % w, w) for w in W_BAND] + [("total", 1.0)]
    out_rows = []
    print(f"\n{'='*70}\n{country} — marriage-series rerun ({cfg['tfr_note']})\n{'='*70}")
    print("TEMPO CAVEAT: period-TFR lead tests are biased toward 'coupling lags' "
          "(postponement dates the TFR turn too early). 'Lead despite bias' = strong.")
    for name, w in measures:
        agg = measure_series(M_marr, M_coh, w)
        prof, best, common = q1(agg, tfr)
        loc = q2_locus(agg, tfr, common)
        steep, order_ok = q3_cascade(perband_measure(marr, coh, w))
        ktag = (f"LEADS {best[0]}" if best[0] > 0 else
                "simultaneous" if best[0] == 0 else f"LAGS {-best[0]}")
        prof_s = " ".join(f"k{k:+d}={prof[k][0]:+.2f}" if prof[k] else f"k{k:+d}=na"
                          for k in KS)
        print(f"\n  [{name}] (w={w})  20-39: {agg[common[0]]*100:.1f}% -> "
              f"{agg[common[-1]]*100:.1f}%  (overlap {common[0]}-{common[-1]})")
        print(f"    Q1 lead: best k={best[0]:+d} r={best[1]:+.2f} ({ktag});  {prof_s}")
        print(f"    Q2 locus: coupling {loc['coup_pct']:+.0f}% vs TFR {loc['tfr_pct']:+.0f}% "
              f"(ratio {loc['ratio']:.2f}) -> {loc['locus']};  steepest {loc['steep_year']} "
              f"({loc['steep_val']*100:+.2f} pts)")
        print(f"    Q3 cascade: steepest {steep}  youngest-first={order_ok}")
        out_rows.append(dict(
            country=country, measure=name, w=w,
            overlap=f"{common[0]}-{common[-1]}", n_years=len(common),
            level_start=round(agg[common[0]], 4), level_end=round(agg[common[-1]], 4),
            q1_best_k=best[0], q1_best_r=round(best[1], 3),
            q1_lead1_r=round(prof[1][0], 3) if prof[1] else "",
            q1_simul_r=round(prof[0][0], 3) if prof[0] else "",
            q1_lag1_r=round(prof[-1][0], 3) if prof[-1] else "",
            q2_coup_pct=round(loc["coup_pct"], 1), q2_tfr_pct=round(loc["tfr_pct"], 1),
            q2_ratio=round(loc["ratio"], 2), q2_locus=loc["locus"],
            q2_steepest_year=loc["steep_year"],
            q3_youngest_first=order_ok,
            q3_band_steepest="|".join(f"{b}:{steep[b]}" for b in BANDS),
            q4_independent="yes (%s roster vs vital registration)" % cfg["roster"],
        ))
    # write by-measure CSV
    fields = list(out_rows[0].keys())
    with open(os.path.join(HERE, f"{country}_identification_bymeasure.csv"), "w", newline="") as f:
        wtr = csv.DictWriter(f, fieldnames=fields); wtr.writeheader(); wtr.writerows(out_rows)
    # ---- chart: measures vs TFR + lead-as-function-of-w ----
    common = sorted(set(M_marr) & set(tfr))
    allw = [0.0] + W_BAND + [1.0]
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(8.5, 8),
                                 gridspec_kw=dict(height_ratios=[3, 2], hspace=0.30))
    ax2 = a1.twinx()
    cmap = plt.cm.viridis
    for w in allw:
        agg = measure_series(M_marr, M_coh, w)
        lab = ("marriage (w=0)" if w == 0 else "total (w=1)" if w == 1 else f"fw w={w}")
        a1.plot(years, [agg[y]*100 for y in years], lw=1.8, marker=".",
                color=cmap(w), label=lab)
    ax2.plot(sorted(tfr), [tfr[y] for y in sorted(tfr)], color="#b2182b", lw=2.5,
             marker="s", label="TFR (observed)")
    a1.set_ylabel("women 20-39 coupling (%)"); ax2.set_ylabel("TFR", color="#b2182b")
    a1.set_title(f"{country} — coupling measures (marriage→total) vs observed TFR")
    a1.grid(alpha=.25); a1.legend(fontsize=7, ncol=3, loc="lower left")
    # bottom: best-lead-k and its r as function of w (the flip visual)
    ks_by_w, rs_by_w = [], []
    for w in allw:
        _, best, _ = q1(measure_series(M_marr, M_coh, w), tfr)
        ks_by_w.append(best[0]); rs_by_w.append(best[1])
    a2.axhline(0, color="#888", lw=.8)
    a2.plot(allw, ks_by_w, color="#2166ac", marker="o", label="best lead k (+=coupling leads)")
    a2b = a2.twinx()
    a2b.plot(allw, rs_by_w, color="#1b7837", marker="^", ls="--", label="|r| at best k")
    a2.set_xlabel("w (cohabiting fertility weight; 0=marriage, 1=total union)")
    a2.set_ylabel("best lead k (yrs)", color="#2166ac"); a2b.set_ylabel("r at best k", color="#1b7837")
    a2.set_title("does the lead verdict shift across the w band?")
    a2.grid(alpha=.25)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, f"{country}_marriage_rerun.png"), dpi=130)
    plt.close(fig)
    print(f"\n  wrote {country}_identification_bymeasure.csv + {country}_marriage_rerun.png")
    return out_rows


if __name__ == "__main__":
    for c in ("COL", "CRI"):
        run_country(c)
