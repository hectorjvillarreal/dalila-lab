#!/usr/bin/env python3
"""
Stage 2 parallel track — Argentina & Chile identification (Q1-Q4), heavily caveated.

Both countries pair coupling against an IMPLIED/reconstructed TFR (not observed
registration), so every lead verdict inherits BOTH:
  (a) the Mexico caveat — modeled/anchored TFR, lead test weak (as for MEX); and
  (b) the Addendum-B tempo caveat — period TFR dates the turn too early, biasing
      lead tests toward "coupling lags / no lead".
Chile is additionally PERIODIC (8 CASEN waves over 16 yrs, irregular spacing), so its
lead test is coarse. Treat Q1 here as exploratory, not evidential. The robust outputs
are the trajectory, the Q2 locus (decline-ratio), and the cohabitation-regime path.

Inputs:  coupling/ARG_coupling_annual.csv + national/ARG_tfr_implied.csv
         coupling/CHL_coupling_annual.csv + national/CHL_tfr_implied.csv
Outputs: coupling/ARG_identification.csv, CHL_identification.csv, ARG_CHL_identification.png
"""
import csv, os
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
NAT  = os.path.normpath(os.path.join(HERE, "..", "national"))
BANDS = ["20-24", "25-29", "30-34", "35-39"]

COUNTRIES = {
    "ARG": dict(coup="ARG_coupling_annual.csv", tfr="ARG_tfr_implied.csv",
                kind="annual (urban)", roster="INDEC EPH"),
    "CHL": dict(coup="CHL_coupling_annual.csv", tfr="CHL_tfr_implied.csv",
                kind="periodic (national)", roster="MDS CASEN"),
}


def load(country):
    cfg = COUNTRIES[country]
    rows = list(csv.DictReader(open(os.path.join(HERE, cfg["coup"]))))
    years = sorted({int(r["year"]) for r in rows})
    share = {m: {b: {} for b in BANDS} for m in ("union_total", "married", "cohabiting")}
    agg = {m: {} for m in ("union_total", "married", "cohabiting")}
    for y in years:
        num = {m: 0.0 for m in agg}; den = 0.0
        for b in BANDS:
            r = next(x for x in rows if int(x["year"]) == y and x["age_band"] == b)
            n = float(r["n_women_weighted"]); den += n
            for m in agg:
                share[m][b][y] = float(r[m]); num[m] += float(r[m]) * n
        for m in agg:
            agg[m][y] = num[m] / den
    tfr = {int(r["year"]): float(r["value"])
           for r in csv.DictReader(open(os.path.join(NAT, cfg["tfr"])))}
    return years, share, agg, tfr


def yoy_annualized(d):
    ys = sorted(d)
    return {ys[i]: (d[ys[i]] - d[ys[i-1]]) / (ys[i] - ys[i-1]) for i in range(1, len(ys))}

def corr(a, b):
    n = len(a)
    if n < 2: return 0.0
    ma, mb = sum(a)/n, sum(b)/n
    num = sum((x-ma)*(y-mb) for x, y in zip(a, b))
    da = (sum((x-ma)**2 for x in a))**.5; db = (sum((y-mb)**2 for y in b))**.5
    return num/(da*db) if da*db else 0.0

def turn(d):
    return max(sorted(d), key=lambda y: d[y])


def run(country):
    cfg = COUNTRIES[country]
    years, share, agg, tfr = load(country)
    common = [y for y in years if y in tfr]
    print(f"\n{'='*72}\n{country} — {cfg['kind']}; coupling {cfg['roster']} vs IMPLIED TFR\n{'='*72}")
    print("⚠ Q1 lead is EXPLORATORY: implied/reconstructed TFR (Mexico caveat) + tempo bias"
          + ("" if country == "ARG" else " + periodic/coarse spacing"))
    print(f"\n{'yr':5} {'union%':>7} {'marr%':>7} {'cohab-sh':>8} {'TFR':>6}")
    for y in years:
        cs = agg['cohabiting'][y] / agg['union_total'][y] if agg['union_total'][y] else 0
        t = f"{tfr[y]:.2f}" if y in tfr else "  .  "
        print(f"  {y} {agg['union_total'][y]*100:6.1f} {agg['married'][y]*100:6.1f} "
              f"{cs*100:7.0f}% {t:>6}")

    # Q1 (exploratory) — annualized differenced corr over the TFR overlap
    print("\nQ1 (lead, EXPLORATORY): corr(dTFR(t), dUnion(t-k)), annualized")
    dt = yoy_annualized({y: tfr[y] for y in common})
    best = {}
    for meas in ("union_total", "married"):
        dc = yoy_annualized({y: agg[meas][y] for y in common})
        bk = None
        for k in (-2, -1, 0, 1, 2):
            pairs = [(dt[y], dc[y-k]) for y in dt if (y in dt and (y-k) in dc)]
            if len(pairs) < 4: continue
            r = corr([p[0] for p in pairs], [p[1] for p in pairs])
            if bk is None or abs(r) > abs(bk[1]): bk = (k, r, len(pairs))
        best[meas] = bk
        if bk:
            tag = (f"leads {bk[0]}" if bk[0] > 0 else "simultaneous" if bk[0] == 0 else f"lags {-bk[0]}")
            print(f"   [{meas:11}] best k={bk[0]:+d} r={bk[1]:+.2f} ({tag}; n={bk[2]})")

    # Q2 locus (robust) — relative decline of coupling vs TFR, BOTH within the TFR overlap
    print("\nQ2 locus (decline ratio |dCoupling%|/|dTFR%| over overlap):")
    t0, t1 = common[0], common[-1]   # endpoints that both coupling and TFR have
    for meas in ("union_total", "married"):
        pk = max(common, key=lambda y: agg[meas][y])   # peak within overlap
        cpct = 100*(agg[meas][t1]-agg[meas][pk])/agg[meas][pk]
        tpct = 100*(tfr[t1]-tfr[t0])/tfr[t0]
        ratio = abs(cpct)/abs(tpct) if tpct else float('inf')
        loc = "map-side" if ratio < 0.5 else "coupling-side" if ratio > 0.85 else "mixed"
        print(f"   [{meas:11}] coupling {cpct:+.0f}% vs TFR {tpct:+.0f}% "
              f"-> ratio {ratio:.2f} ({loc})  [overlap {t0}-{t1}]")

    # Q3 cascade
    print("\nQ3 cascade (steepest annualized union decline per band; youngest-first?):")
    for b in BANDS:
        d = yoy_annualized(share['union_total'][b]); ay = min(d, key=lambda y: d[y])
        print(f"   {b}: steepest~{ay} ({d[ay]*100:+.2f}/yr); "
              f"{share['union_total'][b][years[0]]*100:.0f}%->{share['union_total'][b][years[-1]]*100:.0f}%")

    # Q4 independence
    print(f"\nQ4 independence: coupling = {cfg['roster']} roster; TFR = vital-registry-based "
          "reconstruction. Different instruments -> no circularity (TFR still implied, not observed).")

    # cohab-regime trajectory (the headline for this track)
    cs0 = agg['cohabiting'][years[0]]/agg['union_total'][years[0]]
    cs1 = agg['cohabiting'][years[-1]]/agg['union_total'][years[-1]]
    print(f"\nCohab-share-of-unions: {cs0*100:.0f}% ({years[0]}) -> {cs1*100:.0f}% ({years[-1]})")

    with open(os.path.join(HERE, f"{country}_identification.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "union_20_39", "married_20_39", "cohab_share_of_unions", "tfr_implied"])
        for y in years:
            cs = agg['cohabiting'][y]/agg['union_total'][y] if agg['union_total'][y] else ""
            w.writerow([y, round(agg['union_total'][y], 4), round(agg['married'][y], 4),
                        round(cs, 3) if cs != "" else "", tfr.get(y, "")])
    return years, agg, tfr


def main():
    res = {c: run(c) for c in ("ARG", "CHL")}
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    for ax, c in zip(axes, ("ARG", "CHL")):
        years, agg, tfr = res[c]
        ax2 = ax.twinx()
        ax.plot(years, [agg['union_total'][y]*100 for y in years], color="#2166ac",
                marker="o", lw=2, label="union total")
        ax.plot(years, [agg['married'][y]*100 for y in years], color="#5aae61",
                marker="^", lw=2, label="married")
        ax.plot(years, [agg['cohabiting'][y]*100 for y in years], color="#9970ab",
                marker="s", lw=1.6, label="cohabiting")
        ty = sorted(tfr)
        ax2.plot(ty, [tfr[y] for y in ty], color="#b2182b", marker="D", lw=2, label="TFR (implied)")
        ax.set_title(f"{c} — coupling vs implied TFR ({COUNTRIES[c]['kind']})")
        ax.set_ylabel("women 20-39 (%)"); ax2.set_ylabel("TFR", color="#b2182b")
        ax.grid(alpha=.25); ax.legend(fontsize=7, loc="lower left")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "ARG_CHL_identification.png"), dpi=130)
    print("\nwrote ARG_identification.csv, CHL_identification.csv, ARG_CHL_identification.png")


if __name__ == "__main__":
    main()
