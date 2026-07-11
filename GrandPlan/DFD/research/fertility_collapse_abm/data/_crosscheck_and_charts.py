#!/usr/bin/env python3
"""
Stage 1 — Check 4 (births vs TFR independent cross-check) + summary charts.

Cross-check logic: reconstruct women 15-49 from World Bank 5-year female-age shares
x female total population, then compute an implied general fertility rate
GFR* = national_births / women_15_49 * 1000. If the national TFR collapse were a pure
denominator/migration artifact, births (a raw count) would NOT fall in step with TFR.
We compare the % decline in the raw birth COUNT against the % decline in TFR over a
common window. Concordance => behavioral; large divergence => denominator artifact.
Full ASFR-based implied-births reconciliation is deferred to Stage 2 (needs ASFR).

Outputs:
  data/STAGE1_crosscheck_check4.csv   (machine-readable)
  data/charts/{ISO}_tfr.png           (one per country, provisional/break annotated)
"""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
WB = os.path.join(HERE, "worldbank")
NAT = os.path.join(HERE, "national")
CHARTS = os.path.join(HERE, "charts"); os.makedirs(CHARTS, exist_ok=True)

def read_csv(path):
    out = {}
    if not os.path.exists(path): return out
    with open(path) as f:
        for row in csv.DictReader(f):
            try: out[int(row["year"])] = float(row["value"])
            except (ValueError, KeyError): pass
    return out

def read_full(path):
    rows = []
    if not os.path.exists(path): return rows
    with open(path) as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows

COUNTRIES = {"COL":"Colombia","ARG":"Argentina","CHL":"Chile","CRI":"Costa Rica","MEX":"Mexico"}
AGE = ["1519","2024","2529","3034","3539","4044","4549"]

# ---- reconstruct women 15-49 (WB 5Y shares are % of female pop) ----
def women_1549(iso):
    import json
    femtot = read_csv(os.path.join(WB, f"{iso}_pop_female.csv"))
    out = {}
    shares = {}
    for g in AGE:
        p = f"/tmp/wb_{iso}_{g}.json"
        if not os.path.exists(p): continue
        d = json.load(open(p))
        rows = d[1] or []
        for x in rows:
            if x.get("value") is not None:
                shares.setdefault(int(x["date"]), {})[g] = x["value"]
    for yr, gd in shares.items():
        if yr in femtot and len(gd) == len(AGE):
            out[yr] = femtot[yr] * sum(gd.values())/100.0
    return out

def pct_change(series, y0, y1):
    if y0 in series and y1 in series and series[y0]:
        return 100.0*(series[y1]-series[y0])/series[y0]
    return None

# national TFR file names per country (headline national series)
NAT_TFR = {"COL":"COL_tfr_national.csv","ARG":"ARG_tfr_national.csv","CHL":"CHL_tfr_national.csv",
           "CRI":"CRI_tfr_national.csv","MEX":"MEX_tfr_conapo_modeled.csv"}
NAT_BIRTHS = {"COL":"COL_births_national.csv","ARG":"ARG_births_national.csv","CHL":"CHL_births_national.csv",
              "CRI":"CRI_births_national.csv","MEX":"MEX_births_registered_inegi.csv"}

rows_out = []
print("=== Check 4: births vs TFR cross-check ===\n")
print(f"{'cty':4s} {'window':11s} {'TFR%':>8s} {'births%':>9s} {'W15-49%':>9s} {'implGFR%':>9s}  verdict")
for iso, name in COUNTRIES.items():
    tfr = read_csv(os.path.join(NAT, NAT_TFR[iso]))
    births = read_csv(os.path.join(NAT, NAT_BIRTHS[iso]))
    w = women_1549(iso)
    # common window: overlapping years of national tfr & births
    common = sorted(set(tfr) & set(births))
    if not common:
        # MEX/ARG: tfr and births may not overlap cleanly; use births window
        common = sorted(births)
    y0, y1 = common[0], common[-1]
    # for MEX use occurrence-clean window avoiding 2020 COVID & 2024 prov: 2014-2019
    if iso == "MEX":
        y0, y1 = 2014, 2019
    tfr_pc = pct_change(tfr, y0, y1) if (y0 in tfr and y1 in tfr) else pct_change(tfr, min(tfr), max(tfr))
    b_pc = pct_change(births, y0, y1)
    w_pc = pct_change(w, y0, y1)
    # implied GFR* trend
    gfr = {yr: births[yr]/w[yr]*1000 for yr in births if yr in w}
    g_pc = pct_change(gfr, y0, y1)
    # verdict: births fall comparable to TFR fall AND not explained by women15-49 change
    verdict = "n/a"
    if b_pc is not None and tfr_pc is not None:
        # behavioral if raw birth count fell substantially and women15-49 did NOT fall as much
        if b_pc < -10 and (w_pc is None or w_pc > b_pc + 8):
            verdict = "BEHAVIORAL (raw births fell; denom did not)"
        elif w_pc is not None and abs(w_pc) > abs(b_pc)*0.6:
            verdict = "DENOM-SENSITIVE (check migration)"
        else:
            verdict = "behavioral (raw births fell)"
    print(f"{iso:4s} {f'{y0}-{y1}':11s} "
          f"{(f'{tfr_pc:+.1f}' if tfr_pc is not None else 'n/a'):>8s} "
          f"{(f'{b_pc:+.1f}' if b_pc is not None else 'n/a'):>9s} "
          f"{(f'{w_pc:+.1f}' if w_pc is not None else 'n/a'):>9s} "
          f"{(f'{g_pc:+.1f}' if g_pc is not None else 'n/a'):>9s}  {verdict}")
    rows_out.append({"country":name,"iso3":iso,"window":f"{y0}-{y1}",
                     "tfr_pct_change":round(tfr_pc,1) if tfr_pc is not None else "",
                     "births_pct_change":round(b_pc,1) if b_pc is not None else "",
                     "women1549_pct_change":round(w_pc,1) if w_pc is not None else "",
                     "implied_gfr_pct_change":round(g_pc,1) if g_pc is not None else "",
                     "verdict":verdict})

with open(os.path.join(HERE,"STAGE1_crosscheck_check4.csv"),"w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=["country","iso3","window","tfr_pct_change",
        "births_pct_change","women1549_pct_change","implied_gfr_pct_change","verdict"])
    w.writeheader(); w.writerows(rows_out)
print("\n-> data/STAGE1_crosscheck_check4.csv")

# ---------------- charts: national TFR vs WB TFR, provisional years marked ----------------
print("\n=== charts ===")
for iso, name in COUNTRIES.items():
    natrows = read_full(os.path.join(NAT, NAT_TFR[iso]))
    wb = read_csv(os.path.join(WB, f"{iso}_tfr.csv"))
    if not natrows: continue
    yrs = [int(r["year"]) for r in natrows]
    vals = [float(r["value"]) for r in natrows]
    prov = [r["provisional_flag"].strip().lower().startswith("prov") for r in natrows]
    fig, ax = plt.subplots(figsize=(8,4.8))
    # WB smoothed series for contrast
    wyrs = sorted(y for y in wb if y >= min(yrs)-1)
    ax.plot(wyrs, [wb[y] for y in wyrs], color="0.6", ls="--", lw=1.6,
            label="World Bank/WPP (model-smoothed)")
    # national series
    ax.plot(yrs, vals, color="#b2182b", lw=2.2, marker="o", ms=5,
            label=f"National source (collapse tail)")
    # mark provisional points hollow
    for x,yv,p in zip(yrs,vals,prov):
        if p:
            ax.plot(x,yv, marker="o", ms=9, mfc="white", mec="#b2182b", mew=1.8, zorder=5)
    ax.axhline(2.1, color="0.75", lw=1, ls=":", zorder=0)
    ax.text(min(yrs), 2.12, "replacement 2.1", fontsize=8, color="0.5")
    note = {"COL":"DANE TFR 1.7->1.1 (not 2.0->1.06); 2016-24 definitive",
            "CHL":"INE: 2010-21 chart-only (gap); 2023/24 prov, observed-births break",
            "ARG":"AEPA/INDEC Censo-2010 denom; 2022-24 period TGF NOT published",
            "CRI":"INEC Cuadro 2.2; 2024 from news release; Censo-2022 rebasing",
            "MEX":"CONAPO modeled (>=2020 projection); comparator, not collapse"}[iso]
    ax.set_title(f"{name} — period TFR (national vs World Bank)\n{note}", fontsize=10)
    ax.set_xlabel("year"); ax.set_ylabel("TFR (births per woman)")
    ax.legend(fontsize=8, loc="upper right"); ax.grid(alpha=0.25)
    ax.set_ylim(0.8, max(2.6, max(vals)+0.2))
    fig.tight_layout()
    p = os.path.join(CHARTS, f"{iso}_tfr.png")
    fig.savefig(p, dpi=130); plt.close(fig)
    print(f"  {os.path.basename(p)}  (hollow markers = provisional)")
print("\n-> data/charts/")
