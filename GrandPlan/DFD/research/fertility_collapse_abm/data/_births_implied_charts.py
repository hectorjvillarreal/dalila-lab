#!/usr/bin/env python3
"""
Stage 1 addendum — implied TFR from births + dual-panel (TFR / births) charts.

Implied TFR is back-derived from the raw birth count and the reconstructed female
15-49 denominator, then rescaled to TFR units by anchoring to the published national
TFR in one clean (definitive) year:

    implied_TFR(t) = TFR_national(anchor) * [ GFR(t) / GFR(anchor) ]
    where GFR(t) = births(t) / women_15_49(t) * 1000

ASSUMPTION: the age-pattern of fertility (the GFR->TFR ratio) is approximately stable
over the window. Tempo shifts (postponement) make the ratio drift, so implied TFR is a
CONSISTENCY CHECK and an EXTENSION where official TFR is missing (Argentina >=2022,
Chile <=2021) — NOT a replacement for the official series. Women 15-49 is reconstructed
from World Bank 5-yr female-age shares x WB female total and is itself model-based.

Outputs:
  data/national/{ISO}_tfr_implied.csv     (year, value, source, methodology_flag, provisional_flag)
  data/charts/{ISO}_panel.png             (top: TFR national/WB/implied; bottom: births)
"""
import csv, json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
WB = os.path.join(HERE, "worldbank"); NAT = os.path.join(HERE, "national")
CHARTS = os.path.join(HERE, "charts"); os.makedirs(CHARTS, exist_ok=True)
AGE = ["1519","2024","2529","3034","3539","4044","4549"]
COUNTRIES = {"COL":"Colombia","ARG":"Argentina","CHL":"Chile","CRI":"Costa Rica","MEX":"Mexico"}

# headline national TFR + births file per country, plus the anchor year (clean definitive)
CFG = {
 "COL": dict(tfr="COL_tfr_national.csv",     births="COL_births_national.csv",          anchor=2018),
 "ARG": dict(tfr="ARG_tfr_national.csv",     births="ARG_births_national.csv",          anchor=2015),
 "CHL": dict(tfr="CHL_tfr_national.csv",     births="CHL_births_national.csv",          anchor=2022),
 "CRI": dict(tfr="CRI_tfr_national.csv",     births="CRI_births_national.csv",          anchor=2015),
 "MEX": dict(tfr="MEX_tfr_conapo_modeled.csv", births="MEX_births_registered_inegi.csv", anchor=2018),
}

def read_csv(path):
    out={}
    if not os.path.exists(path): return out
    for row in csv.DictReader(open(path)):
        try: out[int(row["year"])]=float(row["value"])
        except (ValueError,KeyError): pass
    return out

def read_full(path):
    return list(csv.DictReader(open(path))) if os.path.exists(path) else []

def women_1549(iso):
    femtot=read_csv(os.path.join(WB,f"{iso}_pop_female.csv")); shares={}
    for g in AGE:
        p=f"/tmp/wb_{iso}_{g}.json"
        if not os.path.exists(p): continue
        d=json.load(open(p))
        for x in (d[1] or []):
            if x.get("value") is not None:
                shares.setdefault(int(x["date"]),{})[g]=x["value"]
    return {yr:femtot[yr]*sum(gd.values())/100.0
            for yr,gd in shares.items() if yr in femtot and len(gd)==len(AGE)}

for iso,name in COUNTRIES.items():
    cfg=CFG[iso]
    tfr=read_csv(os.path.join(NAT,cfg["tfr"]))
    births=read_csv(os.path.join(NAT,cfg["births"]))
    w=women_1549(iso)
    gfr={y:births[y]/w[y]*1000 for y in births if y in w}
    anchor=cfg["anchor"]
    if anchor not in gfr or anchor not in tfr:
        # fall back to nearest year present in both
        cand=sorted(set(gfr)&set(tfr))
        anchor=min(cand,key=lambda y:abs(y-cfg["anchor"])) if cand else None
    implied={}
    if anchor is not None:
        scale=tfr[anchor]/gfr[anchor]
        implied={y:gfr[y]*scale for y in sorted(gfr)}
    # write implied TFR CSV
    births_rows=read_full(os.path.join(NAT,cfg["births"]))
    prov_b={int(r["year"]):r["provisional_flag"].strip().lower().startswith("prov") for r in births_rows}
    outp=os.path.join(NAT,f"{iso}_tfr_implied.csv")
    with open(outp,"w",newline="") as f:
        wcsv=csv.writer(f); wcsv.writerow(["year","value","source","methodology_flag","provisional_flag"])
        src=f"implied from {cfg['births']} / WB women 15-49, anchored to national TFR {anchor}"
        for y in sorted(implied):
            mf="stable-age-pattern assumption; extension/consistency proxy"
            if iso=="MEX": mf="REGISTERED-births basis (registration lag); 2020 = COVID artifact; proxy only"
            wcsv.writerow([y,round(implied[y],3),src,mf,"provisional" if prov_b.get(y) else "definitive"])
    print(f"{iso}: implied TFR n={len(implied)} anchor={anchor} -> {os.path.basename(outp)}")

    # ---------------- dual panel ----------------
    wb=read_csv(os.path.join(WB,f"{iso}_tfr.csv"))
    natrows=read_full(os.path.join(NAT,cfg["tfr"]))
    nyrs=[int(r["year"]) for r in natrows]; nval=[float(r["value"]) for r in natrows]
    nprov=[r["provisional_flag"].strip().lower().startswith("prov") for r in natrows]

    fig,(ax1,ax2)=plt.subplots(2,1,figsize=(8.4,7.4),sharex=True,
                               gridspec_kw=dict(height_ratios=[3,2],hspace=0.12))
    allyrs=sorted(set(nyrs)|set(implied)|set(births))
    xmin,xmax=min(allyrs)-0.5,max(allyrs)+0.5
    # --- top: TFR ---
    wy=sorted(y for y in wb if xmin<=y<=xmax)
    ax1.plot(wy,[wb[y] for y in wy],color="0.6",ls="--",lw=1.6,label="World Bank/WPP (smoothed)")
    iy=sorted(implied)
    ax1.plot(iy,[implied[y] for y in iy],color="#2166ac",ls=":",lw=1.8,marker="s",ms=4,
             label=f"Implied TFR (from births, anchor {anchor})")
    ax1.plot(nyrs,nval,color="#b2182b",lw=2.3,marker="o",ms=5,label="National published TFR")
    for x,yv,p in zip(nyrs,nval,nprov):
        if p: ax1.plot(x,yv,marker="o",ms=9,mfc="white",mec="#b2182b",mew=1.8,zorder=5)
    ax1.axhline(2.1,color="0.8",lw=1,ls=":"); ax1.text(xmin+0.2,2.12,"replacement 2.1",fontsize=7.5,color="0.5")
    ax1.set_ylabel("TFR (births per woman)"); ax1.grid(alpha=0.25)
    ax1.set_ylim(0.8,max(2.6,max(nval+list(implied.values()))+0.15))
    ax1.legend(fontsize=7.5,loc="upper right")
    ext={"ARG":"implied TFR extends the official series past 2021",
         "CHL":"implied TFR fills the 2010-21 official gap",
         "MEX":"implied uses REGISTERED births: 2020 dip = COVID artifact, not fertility",
         "COL":"implied tracks DANE 1.7->1.1 (denominator rose, births fell)",
         "CRI":"implied tracks INEC 1.83->1.12"}[iso]
    ax1.set_title(f"{name} — period TFR & registered births\n{ext}",fontsize=10)
    # --- bottom: births ---
    by=sorted(births)
    colors=["#cccccc" if prov_b.get(y) else "#777777" for y in by]
    ax2.bar(by,[births[y]/1000 for y in by],color=colors,width=0.7)
    ax2.set_ylabel("births (thousands)"); ax2.set_xlabel("year"); ax2.grid(alpha=0.2,axis="y")
    b0,b1=by[0],by[-1]
    ax2.annotate(f"{births[b0]:,.0f}",(b0,births[b0]/1000),fontsize=7.5,ha="center",va="bottom")
    ax2.annotate(f"{births[b1]:,.0f}",(b1,births[b1]/1000),fontsize=7.5,ha="center",va="bottom")
    pc=100*(births[b1]-births[b0])/births[b0]
    ax2.text(0.02,0.90,f"births {b0}->{b1}: {pc:+.0f}%   (grey=definitive, light=provisional)",
             transform=ax2.transAxes,fontsize=8,color="0.25")
    fig.tight_layout()
    p=os.path.join(CHARTS,f"{iso}_panel.png"); fig.savefig(p,dpi=130); plt.close(fig)
    print(f"     panel -> {os.path.basename(p)}")
print("\ndone.")
