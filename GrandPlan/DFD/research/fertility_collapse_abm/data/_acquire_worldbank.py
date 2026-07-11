#!/usr/bin/env python3
"""
Stage 1 — World Bank WDI acquisition backbone for the fertility-collapse ABM paper.

Pulls the LONG, consistent annual series that World Bank serves programmatically.
NOTE (forensic): World Bank fertility/vital series are WPP-derived, model-smoothed,
and lag 1-2 years. They do NOT capture the 2020-2024 national-registry collapse tail.
That tail is acquired separately from national statistics offices and documented in
the forensic memo. WB series here are the consistent historical backbone + covariates.

Output: one tidy long CSV per (country, series-category) under data/worldbank/,
plus a machine-readable fetch log data/worldbank/_fetch_log.csv.
Columns: year, value, source, methodology_flag, provisional_flag
"""
import csv, json, os, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, "worldbank")
os.makedirs(OUTDIR, exist_ok=True)

COUNTRIES = {"COL": "Colombia", "ARG": "Argentina", "CHL": "Chile",
             "CRI": "Costa Rica", "MEX": "Mexico"}

# indicator code -> (short_name, category)
INDICATORS = {
    "SP.DYN.TFRT.IN":    ("tfr",            "fertility"),
    "SP.DYN.CBRT.IN":    ("crude_birth_rate","fertility"),
    "SP.POP.TOTL":       ("pop_total",      "denominator"),
    "SP.POP.TOTL.FE.IN": ("pop_female",     "denominator"),
    "SM.POP.NETM":       ("net_migration",  "migration"),
    "SP.URB.TOTL.IN.ZS": ("urban_pct",      "covariate"),
    "SL.TLF.CACT.FE.ZS": ("female_lfp_pct", "covariate"),
    "SL.AGR.EMPL.ZS":    ("agri_emp_pct",   "covariate"),
    "NV.AGR.TOTL.ZS":    ("agri_va_pct_gdp","covariate"),
    # female educational attainment (share of female pop 25+ with that level completed)
    "SE.SEC.CUAT.UP.FE.ZS": ("fem_attain_uppersec_pct", "covariate_education"),
    "SE.TER.CUAT.BA.FE.ZS": ("fem_attain_bachelors_pct", "covariate_education"),
    "SE.PRM.CUAT.FE.ZS":    ("fem_attain_primary_pct",   "covariate_education"),
}

BASE = "https://api.worldbank.org/v2/country/{iso}/indicator/{ind}?format=json&per_page=400"

def fetch(iso, ind):
    url = BASE.format(iso=iso, ind=ind)
    req = urllib.request.Request(url, headers={"User-Agent": "DFD-Stage1/1.0"})
    with urllib.request.urlopen(req, timeout=40) as r:
        data = json.load(r)
    meta = data[0] if isinstance(data, list) and data else {}
    rows = data[1] if isinstance(data, list) and len(data) > 1 and data[1] else []
    return meta, rows, url

fetch_log = []
# collect: category -> iso -> short -> {year: value}; we write one CSV per (iso, category)
for ind, (short, cat) in INDICATORS.items():
    for iso, cname in COUNTRIES.items():
        try:
            meta, rows, url = fetch(iso, ind)
            lastupdated = meta.get("lastupdated", "")
            recs = [(int(x["date"]), x["value"]) for x in rows if x.get("value") is not None]
            recs.sort()
            n = len(recs)
            yr_min = recs[0][0] if recs else ""
            yr_max = recs[-1][0] if recs else ""
            # write tidy long csv per (iso, short)
            fname = f"{iso}_{short}.csv"
            fpath = os.path.join(OUTDIR, fname)
            src = f"World Bank WDI [{ind}], lastupdated {lastupdated}"
            with open(fpath, "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["year", "value", "source", "methodology_flag", "provisional_flag"])
                for yr, val in recs:
                    w.writerow([yr, val, src, "", ""])
            fetch_log.append({
                "country": cname, "iso3": iso, "indicator_code": ind,
                "short_name": short, "category": cat, "file": fname,
                "n_obs": n, "year_min": yr_min, "year_max": yr_max,
                "lastupdated": lastupdated, "url": url, "status": "ok" if n else "empty",
            })
            print(f"{iso} {ind:24s} {short:28s} n={n:3d} {yr_min}-{yr_max}")
        except Exception as e:
            fetch_log.append({
                "country": cname, "iso3": iso, "indicator_code": ind,
                "short_name": short, "category": cat, "file": "",
                "n_obs": 0, "year_min": "", "year_max": "",
                "lastupdated": "", "url": BASE.format(iso=iso, ind=ind),
                "status": f"ERROR: {e}",
            })
            print(f"{iso} {ind:24s} ERROR {e}")
        time.sleep(0.15)

logpath = os.path.join(OUTDIR, "_fetch_log.csv")
with open(logpath, "w", newline="") as f:
    cols = ["country","iso3","indicator_code","short_name","category","file",
            "n_obs","year_min","year_max","lastupdated","url","status"]
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(fetch_log)
print("\nfetch log ->", logpath)
print("files written ->", OUTDIR)
