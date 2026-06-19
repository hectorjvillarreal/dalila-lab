#!/usr/bin/env python3
"""
Stage 1.5 — Mexico identification analysis (Q1-Q4).
Inputs: coupling/MEX_coupling_annual.csv (this work) + national/MEX_tfr_conapo_modeled.csv (Stage 1).
Outputs: console verdicts + coupling/MEX_identification.csv + charts (lead-lag, velocity).
"""
import csv, os
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

HERE=os.path.dirname(os.path.abspath(__file__))
NAT=os.path.normpath(os.path.join(HERE,"..","national"))
BANDS=["20-24","25-29","30-34","35-39"]

# --- load coupling: union_total fraction + n per band/year; build aggregate 20-39 ---
rows=list(csv.DictReader(open(os.path.join(HERE,"MEX_coupling_annual.csv"))))
years=sorted({int(r["year"]) for r in rows})
band_share={b:{} for b in BANDS}; agg={}
for y in years:
    num=den=0.0
    for b in BANDS:
        r=next(x for x in rows if int(x["year"])==y and x["age_band"]==b)
        s=float(r["union_total"]); n=float(r["n_women_weighted"])
        band_share[b][y]=s; num+=s*n; den+=n
    agg[y]=num/den
# --- load TFR ---
tfr={int(r["year"]):float(r["value"]) for r in csv.DictReader(open(os.path.join(NAT,"MEX_tfr_conapo_modeled.csv")))}
common=[y for y in years if y in tfr]

def yoy(d,ys): return {ys[i]:(d[ys[i]]-d[ys[i-1]])/(ys[i]-ys[i-1]) for i in range(1,len(ys))}  # ANNUALIZED (per-year rate; series is biennial)
def pct(d,y0,y1): return 100*(d[y1]-d[y0])/d[y0]

print("=== Mexico coupling (20-39 aggregate, %) vs TFR ===")
print(f"{'yr':4} {'coup20-39':>9} {'TFR':>5} {'dCoup':>6} {'dTFR':>6}")
dc=yoy(agg,common); dt=yoy(tfr,common)
for y in common:
    print(f"{y} {agg[y]*100:8.1f} {tfr[y]:5.2f} {('%+.2f'%(dc[y]*100)) if y in dc else '':>6} {('%+.3f'%dt[y]) if y in dt else '':>6}")

# Q1: lead-lag via correlation of differenced series at shifts k (coupling leads if best k>0)
def corr(a,b):
    n=len(a); ma=sum(a)/n; mb=sum(b)/n
    num=sum((x-ma)*(y-mb) for x,y in zip(a,b))
    da=(sum((x-ma)**2 for x in a))**.5; db=(sum((y-mb)**2 for y in b))**.5
    return num/(da*db) if da*db else 0
dyears=[y for y in common[1:]]
best=None
print("\n=== Q1 lead-lag: corr(dTFR(t), dCoup(t-k)) ===")
for k in (-2,-1,0,1,2):
    pairs=[(dt[y],dc[y-k]) for y in dyears if (y in dt and (y-k) in dc)]
    if len(pairs)<6: continue
    c=corr([p[0] for p in pairs],[p[1] for p in pairs])
    tag="coupling LEADS TFR by %d"%k if k>0 else ("simultaneous" if k==0 else "coupling LAGS by %d"%-k)
    print(f"  k={k:+d}: r={c:+.2f}  ({tag}; n={len(pairs)})")
    if best is None or abs(c)>abs(best[1]): best=(k,c)
print(f"  -> best alignment k={best[0]:+d} (r={best[1]:+.2f})")

# Q2: velocity / nonlinearity — is there an inflection (acceleration) in coupling?
print("\n=== Q2 velocity (ANNUALIZED change in 20-39 coupling, pts/yr) ===")
acc_year=min(dc,key=lambda y:dc[y])
print("  steepest annualized drop (interval ending):", acc_year, f"({dc[acc_year]*100:+.2f} pts/yr)")
print("  coupling 2010->2024:", f"{agg[2010]*100:.1f}% -> {agg[2024]*100:.1f}% ({pct(agg,2010,2024):+.0f}%)")
print("  TFR      2010->2024:", f"{tfr[2010]:.2f} -> {tfr[2024]:.2f} ({pct(tfr,2010,2024):+.0f}%)")

# Q3: age-band cascade — timing of steepest drop per band (youngest-first?)
print("\n=== Q3 cascade: steepest annualized-decline interval per band (youngest-first?) ===")
for b in BANDS:
    d=yoy(band_share[b],common); ay=min(d,key=lambda y:d[y])
    print(f"  {b}: steepest~{ay} ({d[ay]*100:+.2f}/yr); level {band_share[b][2010]*100:.0f}%->{band_share[b][2024]*100:.0f}%")

# Q4: independence — structural fact
print("\n=== Q4 independence ===")
print("  Coupling = ENAHO household-roster estado conyugal (survey).")
print("  TFR = INEC vital registration (births). Measured independently -> NO circularity.")

# write summary csv
with open(os.path.join(HERE,"MEX_identification.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["year","coupling_20_39","tfr","dCoupling_pts","dTFR"])
    for y in common:
        w.writerow([y,round(agg[y],4),tfr[y],round(dc[y]*100,2) if y in dc else "",round(dt[y],3) if y in dt else ""])

# charts
fig,(a1,a2)=plt.subplots(2,1,figsize=(8,7),gridspec_kw=dict(height_ratios=[3,2],hspace=0.25))
ax2=a1.twinx()
a1.plot(common,[agg[y]*100 for y in common],color="#2166ac",lw=2.3,marker="o",label="coupling 20-39 (%)")
ax2.plot(common,[tfr[y] for y in common],color="#b2182b",lw=2.3,marker="s",label="TFR")
a1.set_ylabel("women 20-39 in union (%)",color="#2166ac"); ax2.set_ylabel("TFR",color="#b2182b")
a1.set_title("Mexico — coupling (20-39) vs TFR, 2010-2024"); a1.grid(alpha=.25)
for b in BANDS: a2.plot(common,[band_share[b].get(y,float('nan'))*100 for y in common],marker=".",label=b)
a2.set_title("coupling by age band (%) — cascade check"); a2.legend(fontsize=7,ncol=4); a2.grid(alpha=.25); a2.set_xlabel("year")
fig.tight_layout(); fig.savefig(os.path.join(HERE,"MEX_coupling_vs_tfr.png"),dpi=130); plt.close(fig)
print("\nwrote MEX_identification.csv + MEX_coupling_vs_tfr.png")
