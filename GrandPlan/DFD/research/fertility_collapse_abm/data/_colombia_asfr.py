#!/usr/bin/env python3
"""
Colombia ASFR (Check 5) from DANE EEVV Boletin Isem-2025pr, Grafico 6 (TEFE per 1,000,
years 2015/2020/2023/2024). Extracted via pdftotext -layout. The grouped 4-year x 8-age
bar chart does NOT yield all 32 bars cleanly (~24 resolved), so we encode ONLY confidently
anchored values and flag extraction confidence. The qualitative tempo/quantum read rests on
DANE's own prose, which is unambiguous. NO values are guessed.

Confident:
  2015 peak vector (tallest bar per group) + 2024 anchors:
   - 20-24 2024 ≈ 38.6  (DANE prose: "reduccion de 55,6 puntos" from 94,2; flagged derived)
   - 40-44 2024 = 6.9   (DANE prose: "-20,4%" vs 2015 -> 8.7*0.796 = 6.93; self-validating)
   - 45+   2024 = 0.3
DANE prose: largest RELATIVE decreases = 10-14 and 15-19; smallest = 45+ then 40-44 (-20.4%).
"""
import csv, os
HERE=os.path.dirname(os.path.abspath(__file__)); NAT=os.path.join(HERE,"national")
SRC="DANE EEVV Boletin Isem-2025pr (25-sep-2025), Grafico 6 [pdftotext -layout]"
# (year, age_group, value, confidence_flag)
rows=[
 (2015,"10-14",3.1,"chart-read (2015 peak bar)"),
 (2015,"20-24",94.2,"chart-read (2015 peak bar; series peak)"),
 (2015,"25-29",81.2,"chart-read (2015 peak bar)"),
 (2015,"30-34",66.1,"chart-read (2015 peak bar)"),
 (2015,"35-39",36.6,"chart-read (2015 peak bar)"),
 (2015,"40-44",8.7,"chart-read (2015 peak bar)"),
 (2015,"45+",0.4,"chart-read (2015 peak bar)"),
 (2024,"20-24",38.6,"DERIVED from DANE prose (-55.6 pts vs 2015); approximate"),
 (2024,"40-44",6.9,"DERIVED from DANE prose (-20.4% vs 2015); self-validating"),
 (2024,"45+",0.3,"chart-read (2024 bar)"),
 # 15-19 2015 not separable from 30-34 cluster (62.6/60.1); 2024 vector for 10-14/15-19/25-29/30-34/35-39 not cleanly resolved
]
p=os.path.join(NAT,"COL_asfr.csv")
with open(p,"w",newline="") as f:
    w=csv.writer(f); w.writerow(["year","age_group","value","source","methodology_flag","provisional_flag"])
    for yr,ag,v,flag in rows:
        w.writerow([yr,ag,v,SRC,f"per 1,000 women; {flag}","definitive"])
print(f"wrote {os.path.basename(p)}  n={len(rows)} (partial: see flags; full 2024 vector unresolved -> Stage 2 DANE anexo)")
print("Check 5 qualitative read (DANE prose): decline concentrated in YOUNG ages")
print("  20-24: 94.2 -> ~38.6 (-55.6 pts, largest absolute)")
print("  40-44:  8.7 ->  6.9 (-20.4%, near-smallest)   45+: 0.4->0.3")
print("  10-14 & 15-19: largest RELATIVE decreases (DANE) -> postponement/tempo signature, as ARG/MEX")
