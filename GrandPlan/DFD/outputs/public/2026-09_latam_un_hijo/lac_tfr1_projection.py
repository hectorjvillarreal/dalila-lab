"""lac_tfr1_projection.py — LAC theoretical scenario (see README.md): every country's TFR moves linearly from its UN 2025 level to 1.0 in 2030,
then stays at 1.0. Cohort-component, 5-yr ages x 5-yr steps, 2025-2100. Mortality, net migration,
age pattern of fertility: UN WPP 2024 medium. Base 2025: UN WPP 2024, except Mexico = INEGI EIC 2025. Starting TFR: latest registry values where available.
Method = ../2026-09_mexico_2050/mex2050_projection.py. Validation column un_method vs un_published."""
import pandas as pd, os
HERE = os.path.dirname(os.path.abspath(__file__))
# UN WPP 2024 CSVs cached (git-ignored) by ../2026-09_mexico_2050/mex2050_projection.py; run that once first
D = os.path.join(HERE, "..", "2026-09_mexico_2050", "data") + "/"
RES = os.path.join(HERE, "results")
SRB = 1.05; AGES = list(range(0, 101, 5))
MIGPROF = {0:.03,5:.03,10:.03,15:.10,20:.20,25:.20,30:.14,35:.10,40:.07,45:.04,50:.03,55:.02,60:.01}
def rd(f, cols):
    it = pd.read_csv(D+f, usecols=cols, chunksize=500_000, encoding="utf-8-sig", low_memory=False)
    return pd.concat(c[c.LocID.isin(IDS)] for c in it)
tot = pd.read_csv(D+"WPP2024_TotalPopulationBySex.csv.gz", usecols=["LocID","ISO3_code","Location","LocTypeID","ParentID","Variant","Time","PopTotal"], encoding="utf-8-sig", low_memory=False)
ctry = tot[(tot.LocTypeID==4)&tot.ParentID.isin([915,916,931])&(tot.Variant=="Medium")]
IDS = set(ctry.LocID) | {904}
names = ctry.drop_duplicates("LocID").set_index("LocID")[["ISO3_code","Location"]]
untot = tot[tot.LocID.isin(IDS)&(tot.Variant=="Medium")].set_index(["LocID","Time"]).PopTotal/1000
pop = rd("WPP2024_PopulationByAge5GroupSex_Medium.csv.gz", ["LocID","Time","AgeGrpStart","PopMale","PopFemale"])
asf = rd("WPP2024_Fertility_by_Age5.csv.gz", ["LocID","Variant","Time","AgeGrpStart","PASFR"]); asf = asf[asf.Variant=="Medium"]
ind = rd("WPP2024_Demographic_Indicators_Medium.csv.gz", ["LocID","Time","TFR","NetMigrations"]).set_index(["LocID","Time"])
lt = rd("WPP2024_Life_Table_Abridged_Medium_2024-2100.csv.gz", ["LocID","Sex","Time","AgeGrpStart","Lx"]); lt = lt[lt.Sex!="Total"]
LT = {k: g.set_index("AgeGrpStart").Lx.to_dict() for k, g in lt.groupby(["LocID","Time","Sex"])}
PA = {k: (g.set_index("AgeGrpStart").PASFR/100).to_dict() for k, g in asf.groupby(["LocID","Time"])}
PP = {k: g for k, g in pop[pop.Time==2025].groupby("LocID")}

def surv(L):
    G = {0: L[0]+L[1], **{a: L[a] for a in range(5,101,5)}}; T = sum(v for a,v in L.items() if a>=100)
    S = {a: G[a+5]/G[a] for a in range(0,95,5)}; S[95] = T/(G[95]+T); S["b"] = G[0]/5e5; return S
def base(loc):
    g = PP[loc]; m = {a:0.0 for a in AGES}; f = dict(m)
    for _, r in g.iterrows(): a = min(int(r.AgeGrpStart),100); m[a]+=r.PopMale; f[a]+=r.PopFemale
    return m, f
EIC_TOTAL, EIC_SHARES = 130_911.314, {"young": .216, "old": .101}
def eic_base(loc):
    m, f = base(loc); grp = lambda a: "young" if a < 15 else ("old" if a >= 65 else "work")
    tot = {"young": 0.0, "work": 0.0, "old": 0.0}
    for a in m: tot[grp(a)] += m[a] + f[a]
    tgt = {g: EIC_SHARES[g]*EIC_TOTAL for g in EIC_SHARES}; tgt["work"] = EIC_TOTAL - sum(tgt.values())
    k = {g: tgt[g]/tot[g] for g in tot}
    return {a: m[a]*k[grp(a)] for a in m}, {a: f[a]*k[grp(a)] for a in f}
def project(loc, tfr_fn, end=2100, current=False):
    m, f = eic_base(loc) if (current and names.ISO3_code[loc] == "MEX") else base(loc); y = 2025; out = {y: sum(m.values())+sum(f.values())}; kids = {y: sum(m[a]+f[a] for a in (0,5,10))}
    old = {y: sum(m[a]+f[a] for a in AGES if a>=65)}; births = {}
    while y < end:
        t = min(y+2, 2100); Sm, Sf = surv(LT[(loc,t,"Male")]), surv(LT[(loc,t,"Female")]); P = PA[(loc,t)]
        tfr = (tfr_fn(y)+tfr_fn(y+5))/2
        nm = {a+5: m[a]*Sm[a] for a in range(0,95,5)}; nf = {a+5: f[a]*Sf[a] for a in range(0,95,5)}
        nm[100] = (m[95]+m[100])*Sm[95]; nf[100] = (f[95]+f[100])*Sf[95]
        B = sum(tfr*P[a]*(f[a]+nf.get(a,0))/2 for a in P)
        nm[0] = B*SRB/(1+SRB)*Sm["b"]; nf[0] = B/(1+SRB)*Sf["b"]
        M = sum(ind.NetMigrations.get((loc,y+k),0) for k in range(1,6))
        for a,p in MIGPROF.items(): nm[a]=nm.get(a,0)+M*p*.55; nf[a]=nf.get(a,0)+M*p*.45
        m, f = nm, nf; y += 5
        out[y] = sum(m.values())+sum(f.values()); kids[y] = sum(m[a]+f[a] for a in (0,5,10)); old[y] = sum(m[a]+f[a] for a in AGES if a>=65); births[y] = B/5
    return out, kids, old, births
un_tfr = lambda loc: (lambda y: ind.TFR[(loc, min(y,2100))])
# Observed national 2025 TFR replaces UN estimate where Dalila has it: INEGI EIC 2025 (MEX), civil registry 2025 (CHL)
# Latest national-registry TFR (Fernandez-Villaverde 2026-09-15 deck, slide 8; corpus observations/2026-09-15_fernandez-villaverde-slides-latam.md);
# Mexico = INEGI EIC 2025 (1.23), replacing the deck's extrapolated 1.51. Vintages 2022-2025, treated as the 2025 level.
OBS = {"PRI": .87, "CHL": .99, "COL": 1.01, "CRI": 1.12, "BHS": 1.15, "URY": 1.19, "JAM": 1.22, "ARG": 1.23, "CUB": 1.30,
       "MEX": 1.23, "BRA": 1.52, "DOM": 1.61, "BLZ": 1.63, "PER": 1.67, "PAN": 1.79, "NIC": 1.80, "GTM": 1.91, "BOL": 2.06}
t25 = lambda loc: OBS.get(names.ISO3_code[loc], ind.TFR[(loc,2025)])
def tfr1(loc):
    t0 = t25(loc)
    return lambda y: t0 if y<=2025 else 1.0     # 2025 level -> 1.0 at 2030 (linear within the step), 1.0 after
rows = []; val = {}
for loc in names.index:
    u = project(loc, un_tfr(loc)); s = project(loc, tfr1(loc), current=True)
    for y in u[0]:
        rows.append(dict(LocID=loc, ISO3=names.ISO3_code[loc], country=names.Location[loc], year=y,
            un_published=untot.get((loc,y)), un_method=u[0][y]/1000, tfr1=s[0][y]/1000,
            tfr1_0_14=s[1][y]/1000, tfr1_65p=s[2][y]/1000, un_0_14=u[1][y]/1000, un_65p=u[2][y]/1000,
            tfr2025=t25(loc), tfr2025_un=ind.TFR[(loc,2025)]))
R = pd.DataFrame(rows); R.to_csv(os.path.join(RES, "lac_tfr1_results.csv"), index=False)
A = R.groupby("year")[["un_published","un_method","tfr1","tfr1_0_14","tfr1_65p","un_0_14","un_65p"]].sum()
A["un_lac_aggregate"] = [untot.get((904,y)) for y in A.index]
A.to_csv(os.path.join(RES, "lac_tfr1_aggregate.csv")); print(A.round(1).to_string())
