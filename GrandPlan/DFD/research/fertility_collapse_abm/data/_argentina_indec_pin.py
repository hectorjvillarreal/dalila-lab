#!/usr/bin/env python3
"""
Pin Argentina's implied TFR against the REAL INDEC female-15-49 denominator
(replacing the World Bank 5-yr-age reconstruction used in the first pass).

Denominators (INDEC, exact integers, parsed from the .xls/.csv companion files):
  - Censo-2010 base (Cuadro 2, c2_proyecciones_nac_2010_2040.xls): annual 2010-2024.
    This is the SAME vintage INDEC used to publish the official period TGF 2010-2021.
  - Censo-2022 base (proyecciones_nacionales_2022_2040_base.csv): 2022-2024.
    +3.21% higher than the Censo-2010 projection at the 2022 overlap (a real level break).

Method: implied_TFR(t) = TGF_official(2021) * [GFR(t)/GFR(2021)], GFR=births/W1549*1000,
anchored at 2021 (the LAST official year, adjacent to the extension, precise value 1.558).
We report the 2022-2024 extension under BOTH denominator vintages to bracket it.

Births: DEIS open microdata (final 2010-2023; 2024 provisional).
Outputs: data/national/ARG_women1549_indec.csv, ARG_tfr_implied_indec.csv ; charts/ARG_panel_indec.png
"""
import csv, os
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

HERE=os.path.dirname(os.path.abspath(__file__)); NAT=os.path.join(HERE,"national")
WB=os.path.join(HERE,"worldbank"); CHARTS=os.path.join(HERE,"charts")

# DEIS births (from ARG_births_national.csv)
births={2010:756176,2011:758042,2012:738318,2013:754603,2014:777012,2015:770040,
        2016:728035,2017:704609,2018:685394,2019:625441,2020:533299,2021:529794,
        2022:495295,2023:460902,2024:413135}
prov_b={2024}
# INDEC women 15-49 — Censo-2010 vintage (parsed from c2 xls; 2010-2022 match the agent exactly)
w_c2010={2010:10306944,2011:10432273,2012:10552880,2013:10669484,2014:10783268,
         2015:10894899,2016:11004627,2017:11111662,2018:11214540,2019:11311612,
         2020:11401749,2021:11484778,2022:11561088,2023:11631314,2024:11695576}
# INDEC women 15-49 — Censo-2022 vintage (CSV, single ages summed by agent)
w_c2022={2022:11931996,2023:12016973,2024:12101183}
# Official INDEC/AEPA period TGF (Censo-2010 denom); precise endpoints from INDEC Anuario 2023
official={2010:2.383,2011:2.4,2012:2.3,2013:2.3,2014:2.4,2015:2.3,2016:2.2,
          2017:2.1,2018:2.0,2019:1.9,2020:1.6,2021:1.558}
ANCHOR=2021
gfr=lambda y,W: births[y]/W[y]*1000
scale=official[ANCHOR]/gfr(ANCHOR,w_c2010)
print(f"anchor {ANCHOR}: official TGF={official[ANCHOR]}, GFR(c2010)={gfr(ANCHOR,w_c2010):.3f}, scale={scale:.7f}\n")

impl_c2010={y:gfr(y,w_c2010)*scale for y in sorted(w_c2010)}
impl_c2022={y:gfr(y,w_c2022)*scale for y in sorted(w_c2022)}

# WB-based implied (first pass) for comparison: recompute quickly from /tmp wb age files
import json
AGE=["1519","2024","2529","3034","3539","4044","4549"]
def wb_w():
    femtot={}
    for row in csv.DictReader(open(os.path.join(WB,"ARG_pop_female.csv"))):
        femtot[int(row["year"])]=float(row["value"])
    sh={}
    for g in AGE:
        p=f"/tmp/wb_ARG_{g}.json"
        if not os.path.exists(p): return {}
        for x in (json.load(open(p))[1] or []):
            if x.get("value") is not None: sh.setdefault(int(x["date"]),{})[g]=x["value"]
    return {y:femtot[y]*sum(d.values())/100 for y,d in sh.items() if y in femtot and len(d)==len(AGE)}
wbw=wb_w()
scale_wb=official[ANCHOR]/(births[ANCHOR]/wbw[ANCHOR]*1000) if wbw else None
impl_wb={y:births[y]/wbw[y]*1000*scale_wb for y in sorted(wbw) if y in births} if wbw else {}

print(f"{'yr':4s} {'official':>8s} {'INDEC2010':>9s} {'INDEC2022':>9s} {'WB-based':>8s}  W1549(c2010 vs c2022)")
for y in range(2010,2025):
    o=f"{official[y]:.3f}" if y in official else "-"
    a=f"{impl_c2010[y]:.3f}" if y in impl_c2010 else "-"
    b=f"{impl_c2022[y]:.3f}" if y in impl_c2022 else "-"
    c=f"{impl_wb[y]:.3f}" if y in impl_wb else "-"
    w2=f"{w_c2022[y]:,}" if y in w_c2022 else ""
    print(f"{y:4d} {o:>8s} {a:>9s} {b:>9s} {c:>8s}  {w_c2010[y]:,} {w2}")

print(f"\nOverlap 2022: W c2010={w_c2010[2022]:,}  c2022={w_c2022[2022]:,}  (+{100*(w_c2022[2022]/w_c2010[2022]-1):.2f}%)")
print("PINNED 2024 TFR range: {:.3f} (Censo-2022 pop) - {:.3f} (Censo-2010 pop)".format(impl_c2022[2024],impl_c2010[2024]))

# ---- write denominator CSV (provenance) ----
with open(os.path.join(NAT,"ARG_women1549_indec.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["year","value","source","methodology_flag","provisional_flag"])
    for y in sorted(w_c2010):
        w.writerow([y,w_c2010[y],"INDEC Cuadro 2, c2_proyecciones_nac_2010_2040.xls (Censo-2010 base)",
                    "female 15-49, sum of 5-yr groups; mid-year","definitive"])
    for y in sorted(w_c2022):
        w.writerow([y,w_c2022[y],"INDEC proyecciones_nacionales_2022_2040_base.csv (Censo-2022 base)",
                    "female 15-49, sum single ages; +3.21% vs Censo-2010 at 2022","definitive"])

# ---- write pinned implied TFR CSV ----
with open(os.path.join(NAT,"ARG_tfr_implied_indec.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["year","value","source","methodology_flag","provisional_flag"])
    for y in sorted(impl_c2010):
        w.writerow([y,round(impl_c2010[y],3),
                    "implied: DEIS births / INDEC women15-49 (Censo-2010), anchored official TGF 2021=1.558",
                    "vintage-consistent with anchor; stable-age-pattern proxy",
                    "provisional" if y in prov_b else "definitive"])
    for y in sorted(impl_c2022):
        w.writerow([y,round(impl_c2022[y],3),
                    "implied: DEIS births / INDEC women15-49 (Censo-2022), anchored official TGF 2021=1.558",
                    "more accurate pop but +3.21% vintage break vs Censo-2010 anchor",
                    "provisional" if y in prov_b else "definitive"])
print("\nwrote ARG_women1549_indec.csv, ARG_tfr_implied_indec.csv")

# ---- chart: official + INDEC-pinned (both vintages) + WB-based + WB-smoothed ----
wb={int(r["year"]):float(r["value"]) for r in csv.DictReader(open(os.path.join(WB,"ARG_tfr.csv")))}
fig,ax=plt.subplots(figsize=(8.6,5.2))
wy=[y for y in sorted(wb) if 2009<=y<=2025]
ax.plot(wy,[wb[y] for y in wy],color="0.6",ls="--",lw=1.6,label="World Bank/WPP (smoothed)")
if impl_wb:
    iy=sorted(impl_wb); ax.plot(iy,[impl_wb[y] for y in iy],color="#9ecae1",ls=":",lw=1.5,marker="^",ms=4,
                                label="implied (WB age shares, 1st pass)")
oy=sorted(official); ax.plot(oy,[official[y] for y in oy],color="#b2182b",lw=2.4,marker="o",ms=5,
                             label="official INDEC/AEPA TGF (to 2021)")
e10=[2021,2022,2023,2024]; ax.plot(e10,[official[2021]]+[impl_c2010[y] for y in [2022,2023,2024]],
        color="#2166ac",ls="-",lw=2.0,marker="s",ms=5,label="INDEC-pinned ext. (Censo-2010 pop)")
ax.plot([2021,2022,2023,2024],[official[2021]]+[impl_c2022[y] for y in [2022,2023,2024]],
        color="#08519c",ls="--",lw=2.0,marker="D",ms=5,label="INDEC-pinned ext. (Censo-2022 pop)")
ax.annotate(f"{impl_c2010[2024]:.2f}",(2024,impl_c2010[2024]),fontsize=8,color="#2166ac",va="bottom")
ax.annotate(f"{impl_c2022[2024]:.2f}",(2024,impl_c2022[2024]),fontsize=8,color="#08519c",va="top")
ax.annotate(f"WB {wb.get(2024,float('nan')):.2f}",(2024,wb.get(2024,1.5)),fontsize=8,color="0.5",va="bottom")
ax.axhline(2.1,color="0.8",lw=1,ls=":"); ax.text(2009.2,2.12,"replacement 2.1",fontsize=7.5,color="0.5")
ax.set_title("Argentina — implied TFR pinned to INDEC female 15-49 denominator\n"
             "official series ends 2021; INDEC-pinned extension puts 2024 at ~1.15-1.19, far below WB's ~1.50",
             fontsize=9.5)
ax.set_xlabel("year"); ax.set_ylabel("TFR (births per woman)"); ax.grid(alpha=0.25)
ax.set_ylim(0.8,2.6); ax.legend(fontsize=7.5,loc="lower left")
fig.tight_layout(); p=os.path.join(CHARTS,"ARG_panel_indec.png"); fig.savefig(p,dpi=135); plt.close(fig)
print("chart ->",os.path.basename(p))
