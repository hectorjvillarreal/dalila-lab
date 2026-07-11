#!/usr/bin/env python3
"""
Stage 1 — Check 5 inputs (ASFR by age) + coupling endpoint series, both as data products.
All values verified against primary sources by the country verification pass (June 2026).

ASFR (age-specific fertility rate, births per 1,000 women in the group). Files:
  data/national/{ISO}_asfr.csv   columns: year, age_group, value, source, methodology_flag, provisional_flag
Coupling (share of women partnered/in union — ENDPOINTS only; annual path deferred to Stage 2):
  data/national/{ISO}_coupling.csv  columns: year, age_band, value, status_def, source, methodology_flag

Also computes the tempo proxy: share of total ASFR decline contributed by ages <30
(a high share => decline concentrated in young ages => postponement/tempo signature).
Writes data/STAGE1_check5_tempo_quantum.csv.
"""
import csv, os
HERE=os.path.dirname(os.path.abspath(__file__)); NAT=os.path.join(HERE,"national")
AGES=["15-19","20-24","25-29","30-34","35-39","40-44","45-49"]

# ---------------- ASFR (per 1,000 women) ----------------
# Argentina: OBSERVED (DEIS births / INDEC-2013 proj), AEPA 2023 (Bathory, Muhafra & Grushka) Tabla 1
ARG_ASFR={
 2010:[66.0,112.1,111.5,103.6,62.4,18.1,1.4],
 2014:[65.9,111.1,108.6,101.9,62.6,18.5,1.3],
 2015:[63.5,109.3,106.6,99.1,64.0,18.8,1.4],
 2019:[41.3,84.5,87.5,81.9,55.8,16.6,1.4],
 2020:[30.9,70.1,75.7,71.7,49.2,15.0,1.3],
 2021:[27.5,67.4,75.6,73.6,50.4,15.2,1.1],
}
# Mexico: ENADID survey (2023 = trienio 2020-2022), read from ENADID23 presentation chart
MEX_ASFR={
 2014:[77.0,126.0,113.1,77.2,38.1,10.0,0.6],
 2018:[70.6,118.2,108.8,72.4,34.4,9.4,0.6],
 2023:[45.2,85.5,84.3,63.7,32.4,9.0,0.5],
}
# Chile: TEF from INE provisional bulletins Gráfico 4 (2023, 2024)
CHL_ASFR={
 2023:[11.0,43.7,59.7,60.7,42.9,12.8,1.0],
 2024:[9.3,38.5,53.4,54.6,38.7,11.3,0.8],
}
SRC={"ARG":"AEPA 2023 (Bathory, Muhafra & Grushka) Tabla 1 — OBSERVED (DEIS births / INDEC-2013 proj)",
     "MEX":"INEGI ENADID 2023 presentation, 'Tasas especificas de fecundidad' chart",
     "CHL":"INE Chile provisional bulletins EV2023/EV2024, Grafico 4 (TEF)"}
METH={"ARG":"observed period ASFR; per 1,000 women","MEX":"survey ASFR; 2023=trienio 2020-2022; per 1,000",
      "CHL":"provisional TEF; per 1,000; 2023/24 observed-births basis"}
PROV={"ARG":set(),"MEX":set(),"CHL":{2023,2024}}

def write_asfr(iso,data):
    p=os.path.join(NAT,f"{iso}_asfr.csv")
    with open(p,"w",newline="") as f:
        w=csv.writer(f); w.writerow(["year","age_group","value","source","methodology_flag","provisional_flag"])
        for yr in sorted(data):
            for ag,v in zip(AGES,data[yr]):
                w.writerow([yr,ag,v,SRC[iso],METH[iso],"provisional" if yr in PROV[iso] else "definitive"])
    print(f"  {os.path.basename(p)}  years={sorted(data)}")

print("ASFR files:")
write_asfr("ARG",ARG_ASFR); write_asfr("MEX",MEX_ASFR); write_asfr("CHL",CHL_ASFR)

# ---------------- tempo vs quantum proxy ----------------
def tempo(iso,data,y0,y1):
    a0,a1=data[y0],data[y1]
    dec=[a0[i]-a1[i] for i in range(7)]           # decline per group (per 1000)
    tot=sum(dec)
    young=sum(dec[:3])                             # 15-29
    return dict(iso=iso,y0=y0,y1=y1,total_decline_per1000=round(tot,1),
                young_under30_share_pct=round(100*young/tot,1) if tot else None,
                tfr_proxy_y0=round(sum(a0)*5/1000,3),tfr_proxy_y1=round(sum(a1)*5/1000,3))
rows=[tempo("ARG",ARG_ASFR,2010,2021),tempo("MEX",MEX_ASFR,2014,2023),tempo("CHL",CHL_ASFR,2023,2024)]
print("\nCheck 5 — tempo proxy (share of ASFR decline from ages <30):")
for r in rows:
    print(f"  {r['iso']} {r['y0']}->{r['y1']}: decline {r['total_decline_per1000']}/1000, "
          f"<30 share = {r['young_under30_share_pct']}%  (TFR proxy {r['tfr_proxy_y0']}->{r['tfr_proxy_y1']})")
with open(os.path.join(HERE,"STAGE1_check5_tempo_quantum.csv"),"w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("  -> data/STAGE1_check5_tempo_quantum.csv")

# ---------------- coupling endpoints ----------------
# (year, age_band, pct_partnered, status_definition, source, methodology_flag)
COUP={
 "MEX":[(2018,"women 15-49",57.5,"casada+union libre","INEGI ENADID 2018 (via ENADID2023 boletin)","VERIFIED; 34.2 casada+23.3 union"),
        (2023,"women 15-49",53.3,"casada+union libre","INEGI ENADID 2023 boletin","VERIFIED; 28.5 casada+24.8 union; soltera now modal 35.3")],
 "CRI":[(1990,"persons 20-59",12.0,"union libre (cohabitation only)","CCP-UCR Patrones historicos nupcialidad","graph-read; cohabitation only = lower bound"),
        (2019,"persons 20-59",20.0,"union libre (cohabitation only)","CCP-UCR Patrones historicos nupcialidad","graph-read; peak 30-34 ~25%")],
 "CHL":[(2015,"women/persons 15-29 married",4.9,"married only","CASEN 2015 (via ICSO-UDP)","married-only; dated; not 20-39 cut"),
        (2011,"persons cohabiting",15.0,"cohabitation only","CASEN/Censo (via ICSO-UDP)","cohabitation only; from 6.3% in 1990")],
 "ARG":[(2024,"persons 25-34 (CABA only)",45.9,"unidas+casadas","Direccion Estadistica CABA, indicator c13","CABA CITY ONLY; not national; 34.6 unidas+11.3 casada"),
        (2024,"persons 35-44 (CABA only)",70.6,"unidas+casadas","Direccion Estadistica CABA","CABA CITY ONLY")],
}
print("\nCoupling endpoint files (ENDPOINTS only; annual path = Stage 2 microdata):")
for iso,recs in COUP.items():
    p=os.path.join(NAT,f"{iso}_coupling.csv")
    with open(p,"w",newline="") as f:
        w=csv.writer(f); w.writerow(["year","age_band","pct_partnered","status_definition","source","methodology_flag"])
        for r in recs: w.writerow(list(r))
    print(f"  {os.path.basename(p)}  n={len(recs)}")
print("\nNOTE: Colombia ASFR (DANE Grafico 6) and Colombia/full coupling NOT extracted -> Stage 2.")
