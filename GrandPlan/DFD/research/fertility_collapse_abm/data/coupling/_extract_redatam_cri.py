#!/usr/bin/env python3
"""
Stage 1.5 — Costa Rica coupling extractor via INEC's REDATAM (RedatamX) web engine.

Drives RpWebStats.exe/CrossTab to produce, for each ENAHO year 2010-2024, a WEIGHTED
crosstab of estado conyugal (POBLACIO.A6) x 5-year age band (POBLACIO.EDADQ), filtered
to women (POBLACIO.A4 = 2), weighted by the expansion factor (VIVIENDA.FACTOR). Parses
the result and computes the share of women partnered (unión libre + casado) by age band
20-24 / 25-29 / 30-34 / 35-39 — the Stage 1.5 target series, with the married-vs-cohabiting
split preserved.

No login required (REDATAM online processing is public). Server-side tabulation: we never
download microdata. Reproducible — re-run to refresh.

Output: data/coupling/CRI_coupling_annual.csv
Columns: year, age_band, union_total, married, cohabiting, n_women_weighted,
         observed_or_interpolated, source, coverage_flag
(union_total/married/cohabiting are SHARES, fraction 0-1, of women in that age band.)
"""
import csv, os, re, time, html, subprocess

HOST = "https://sistemas.inec.cr:8443"
XTAB = HOST + "/bininec/RpWebStats.exe/CrossTab?"
HERE = os.path.dirname(os.path.abspath(__file__))

YEARS = list(range(2010, 2025))
TARGET_BANDS = {"de 20 a 24 años": "20-24", "de 25 a 29 años": "25-29",
                "de 30 a 34 años": "30-34", "de 35 a 39 años": "35-39"}
COHAB_LABEL = "unión libre"   # "En unión libre o juntado(a)"
MARRIED_LABEL = "casado"      # "Casado(a)"

def post(params):
    # Use curl: this RedatamX server 500s on urllib's POST but accepts curl's
    # --data-urlencode identically. -k: server cert is not in the default trust store.
    args = ["curl", "-sk", "--max-time", "90", "-X", "POST", XTAB]
    for k, v in params.items():
        args += ["--data-urlencode", f"{k}={v}"]
    r = subprocess.run(args, capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError(f"curl failed rc={r.returncode}: {r.stderr[:200]}")
    return r.stdout

def get(url):
    r = subprocess.run(["curl", "-sk", "--max-time", "60", url],
                       capture_output=True, text=True, timeout=90)
    if r.returncode != 0:
        raise RuntimeError(f"curl failed rc={r.returncode}: {r.stderr[:200]}")
    return r.stdout

def num(s):
    s = s.replace("\xa0", " ").strip()
    if s in ("-", "", "–"): return 0.0
    return float(re.sub(r"[^\d.]", "", s.replace(" ", "")))

def conyugal_var(year):
    """Find the estado-conyugal variable code (e.g. A6 from 2013, A26 in 2010-2012)."""
    html_dic = get(f"{HOST}/bininec/RpWebStats.exe/Dictionary?BASE=ENAHO{year}&ITEM=DICPOB&lang=ESP")
    m = re.search(r'<td[^>]*>([A-Za-z0-9_]{1,15})</td>\s*<td[^>]*>[^<]*[Cc]onyugal', html_dic)
    if not m:
        raise RuntimeError(f"ENAHO{year}: estado-conyugal variable not found in DICPOB")
    return m.group(1)

def run_year(year):
    base = f"ENAHO{year}"
    cony = conyugal_var(year)
    params = {
        "BASE": base, "CODIGO": "XXUSUARIOXX", "ITEM": "CSociodemograficos",
        "LANG": "ESP", "MAIN": "WebServerMain.inl", "MODE": "RUN",
        "ROW": f"POBLACIO.{cony}", "COLUMN": "POBLACIO.EDADQ", "WEIGHT": "VIVIENDA.FACTOR",
        "PERCENT": "OFF", "FORMAT": "HTML", "TEXT_FILTER": "POBLACIO.A4 = 2",
        "inputTitle": f"coupling{year}", "Submit": "Submit",  # no '_': engine rejects it
    }
    resp = post(params)
    m = re.search(r'(RpWebUtilities\.exe/Text\?LFN=[^"\']+?TYPE=TMP)', resp)
    if not m:
        raise RuntimeError(f"{base}: no result temp file in response (len {len(resp)})")
    t = get(HOST + "/bininec/" + html.unescape(m.group(1)))
    big = max(re.findall(r"<table.*?</table>", t, re.S | re.I), key=len)
    grid = []
    for r in re.findall(r"<tr.*?</tr>", big, re.S | re.I):
        cells = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", c))).strip()
                 for c in re.findall(r"<t[dh].*?</t[dh]>", r, re.S | re.I)]
        if any(cells): grid.append(cells)
    # header = row with the target band labels. Align by POSITION: in data rows the
    # status label occupies the first non-empty cell, then values follow in age order
    # (the header's leading age column sits one cell left of the data values otherwise).
    hdr_idx = next(i for i, c in enumerate(grid) if any(b in " ".join(c) for b in TARGET_BANDS))
    ages_seq = [c for c in grid[hdr_idx] if c.strip()]          # 20 age bands + 'Total'
    cohab = {b: 0.0 for b in TARGET_BANDS.values()}
    married = {b: 0.0 for b in TARGET_BANDS.values()}
    total = {b: 0.0 for b in TARGET_BANDS.values()}
    for row in grid[hdr_idx + 1:]:
        ne = [c for c in row if c.strip()]
        if len(ne) < 2: continue
        label = ne[0].lower()
        vals = dict(zip(ages_seq, ne[1:]))                      # age label -> value string
        target = cohab if COHAB_LABEL in label else married if MARRIED_LABEL in label else None
        is_total = label.startswith("total")
        for age_label, band in TARGET_BANDS.items():
            if age_label in vals:
                v = num(vals[age_label])
                if target is not None: target[band] += v
                if is_total: total[band] += v
    if sum(total.values()) == 0:
        raise RuntimeError(f"{base}: zero totals parsed")
    return cohab, married, total

def main():
    out = os.path.join(HERE, "CRI_coupling_annual.csv")
    rows_out = []
    print(f"{'year':5s} {'band':6s} {'cohab%':>7s} {'marr%':>7s} {'union%':>7s} {'n_women':>10s}")
    for y in YEARS:
        try:
            cohab, married, total = run_year(y)
        except Exception as e:
            print(f"  {y}: ERROR {e}")
            continue
        for b in ["20-24", "25-29", "30-34", "35-39"]:
            n = total[b]
            ch, mr = cohab[b] / n, married[b] / n
            ut = ch + mr
            rows_out.append({
                "year": y, "age_band": b,
                "union_total": round(ut, 4), "married": round(mr, 4),
                "cohabiting": round(ch, 4), "n_women_weighted": int(round(n)),
                "observed_or_interpolated": "observed",
                "source": f"INEC ENAHO {y} via REDATAM RpWebStats CrossTab (A6 x EDADQ, women A4=2, weighted VIVIENDA.FACTOR)",
                "coverage_flag": "national (urban+rural)",
            })
            print(f"  {y} {b:6s} {ch*100:6.1f} {mr*100:6.1f} {ut*100:6.1f} {int(n):10d}")
        time.sleep(1.0)  # be polite to the server
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "age_band", "union_total", "married",
            "cohabiting", "n_women_weighted", "observed_or_interpolated", "source", "coverage_flag"])
        w.writeheader(); w.writerows(rows_out)
    print(f"\nwrote {out}  ({len(rows_out)} rows, {len(rows_out)//4} years)")

if __name__ == "__main__":
    main()
