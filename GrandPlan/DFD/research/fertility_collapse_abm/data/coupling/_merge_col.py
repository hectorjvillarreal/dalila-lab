#!/usr/bin/env python3
"""Merge corrected 2022-2024 rows into the validated 2007-2021 GEIH coupling rows.

The first full pass produced correct 2007-2021 rows but broken 2022 (Marco/March
month collision -> 3 months) and 2023/2024 (nested-zip months unread -> ~6 months).
The fix-run regenerated 2022-2024 correctly. This merge keeps 2007-2021 from the
original and replaces 2022-2024 from the fix-run.
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(HERE, "COL_coupling_annual.csv")
FIX  = os.path.join(HERE, "COL_fix_222324.csv")
BAND_ORDER = {"20-24": 0, "25-29": 1, "30-34": 2, "35-39": 3}
REPLACE = {2022, 2023, 2024}

main = list(csv.DictReader(open(MAIN)))
fix  = list(csv.DictReader(open(FIX)))
fields = list(main[0].keys())

kept = [r for r in main if int(r["year"]) not in REPLACE]
new  = [r for r in fix if int(r["year"]) in REPLACE]
rows = kept + new

# annotate 2020 coverage caveat (national, but pandemic-reduced sample / FEX_C base)
for r in rows:
    if int(r["year"]) == 2020 and "pandemic" not in r["note"]:
        r["note"] += "; 2020 pandemic-reduced GEIH sample (national urban+rural confirmed via CLASE)"

rows.sort(key=lambda r: (int(r["year"]), BAND_ORDER.get(r["age_band"], 9)))
with open(MAIN, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader(); w.writerows(rows)

yrs = sorted({int(r["year"]) for r in rows})
print(f"merged -> {len(rows)} rows, {len(yrs)} years: {yrs[0]}-{yrs[-1]}")
print(f"  kept {len({int(r['year']) for r in kept})} yrs from main, "
      f"replaced {sorted(REPLACE)} from fix-run")
