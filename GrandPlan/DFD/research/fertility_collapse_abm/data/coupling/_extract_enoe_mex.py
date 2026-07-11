#!/usr/bin/env python3
"""
Stage 1.5 — Mexico coupling extractor from INEGI ENOE microdata.

Sibling of the Costa Rica extractor (_extract_redatam_cri.py). Mexico has NO REDATAM
server for ENOE, so this script downloads the ENOE quarterly MICRODATA zips directly
from INEGI (free, no login) and computes the WEIGHTED share of women 20-39 in a
co-residential union, by 5-year band (20-24 / 25-29 / 30-34 / 35-39), with the
married-vs-cohabiting split preserved.

Variable map (SDEMT sociodemographic table):
  E_CON  estado conyugal: 1=union libre, 2=separado, 3=divorciado, 4=viudo,
                          5=casado, 6=soltero
           -> partnered  = {1,5}
           -> cohabiting = {1}
           -> married    = {5}
  EDA    edad (single year of age; some old quarters store as string, coerce)
  SEX    sexo: 1=hombre, 2=mujer  -> women = 2
  FAC    quarterly expansion weight   (quarters BEFORE the 2020-T3 redesign)
  FAC_TRI quarterly expansion weight  (quarters FROM the 2020-T3 redesign onward)

2020 REDESIGN BREAK (handled automatically by detect_columns):
  - Table/file prefix:  SDEMT*  ->  ENOEN_SDEMT*  (we glob both inside the zip)
  - Weight column:      FAC     ->  FAC_TRI       (we pick whichever is present)
  - 2020-T2 was NOT fielded as a normal ENOE (COVID); the telephone ETOE replaced it.
    We skip 2020 entirely for the annual series and rely on 2019 + 2021+ instead.

URL templates (confirmed against the importinegi CRAN package, R/enoe.R):
  >= 2020-T3 :  https://www.inegi.org.mx/contenidos/programas/enoe/15ymas/microdatos/enoe_n_{YYYY}_trim{Q}_{fmt}.zip
  <= 2020-T1 :  https://www.inegi.org.mx/contenidos/programas/enoe/15ymas/microdatos/{YYYY}trim{Q}_{fmt}.zip
  (fmt = 'csv' or 'dbf'; we try csv first, fall back to dbf)

Output: data/coupling/MEX_coupling_annual.csv
Columns: year, age_band, union_total, married, cohabiting, n_women_weighted,
         observed_or_interpolated, source, coverage_flag
(union_total/married/cohabiting are SHARES, fraction 0-1, of women in that age band.)

ANTI-FABRICATION: every number is computed from a real ENOE file downloaded and parsed
here. Nothing is estimated or interpolated. Years with no successfully processed quarter
are simply omitted (no placeholder rows).

Run from anywhere:
    source ~/miniforge3/etc/profile.d/conda.sh && conda activate dalila
    python _extract_enoe_mex.py
Optional flags:
    --years 2005,2010,2015,2019,2021,2023,2024   (default subset; endpoints+midpoints)
    --quarters all      (pool all available quarters of each year; default = single rep quarter)
    --keep-zips         (do not delete downloaded zips after parsing)
"""
import argparse
import csv
import glob
import io
import os
import subprocess
import sys
import tempfile
import zipfile

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://www.inegi.org.mx/contenidos/programas/enoe/15ymas/microdatos"

# Default subset: endpoints + midpoints spanning the ENOE range (2005-2024).
# 2020 deliberately excluded (COVID: T2 not fielded; redesign mid-year).
DEFAULT_YEARS = [2005, 2010, 2015, 2019, 2021, 2023, 2024]

BANDS = {(20, 24): "20-24", (25, 29): "25-29", (30, 34): "30-34", (35, 39): "35-39"}
COHAB_CODES = {1}        # union libre
MARRIED_CODES = {5}      # casado
PARTNERED_CODES = {1, 5}


def url_for(year, q, fmt):
    """Build the INEGI microdata zip URL for a given year/quarter/format.

    The 2020-T3 redesign changed the filename prefix to 'enoe_n_'. INEGI applies the
    new prefix from 2020-T3 onward; 2020-T1 and everything <=2019 use the old prefix.
    """
    if (year > 2020) or (year == 2020 and q >= 3):
        return f"{BASE}/enoe_{year}_trim{q}_{fmt}.zip"  # confirmed live: enoe_2024_trim1_csv.zip (37MB)
    return f"{BASE}/{year}trim{q}_{fmt}.zip"


def download(url, dest):
    """Download via curl (-L follow redirects, -f fail on HTTP error). Returns True on success."""
    r = subprocess.run(
        ["curl", "-fsSL", "--max-time", "600", "-o", dest, url],
        capture_output=True, text=True,
    )
    ok = r.returncode == 0 and os.path.exists(dest) and os.path.getsize(dest) > 10_000
    if not ok and os.path.exists(dest):
        os.remove(dest)
    return ok


def find_sdemt_member(zf):
    """Return the SDEMT table member name inside the zip, pre- or post-redesign.

    Pre-2020-T3 : SDEMT<qq><yy>.dbf / .csv  (e.g. SDEMT124.dbf)
    Post        : ENOEN_SDEMT<qq><yy>.dbf / .csv
    Match defensively on 'SDEMT' anywhere in the basename.
    """
    names = zf.namelist()
    cands = [n for n in names if "SDEMT" in os.path.basename(n).upper()
             and n.lower().endswith((".dbf", ".csv"))]
    if not cands:
        raise FileNotFoundError(f"no SDEMT member in zip; members: {names[:20]}")
    # Prefer CSV if both formats happen to be present.
    cands.sort(key=lambda n: (not n.lower().endswith(".csv"), len(n)))
    return cands[0]


def read_sdemt(zip_path):
    """Read the SDEMT table from a downloaded zip into a DataFrame (uppercase cols)."""
    with zipfile.ZipFile(zip_path) as zf:
        member = find_sdemt_member(zf)
        raw = zf.read(member)
    if member.lower().endswith(".csv"):
        # ENOE CSVs are UTF-8 or latin-1 depending on vintage; try utf-8 then latin-1.
        for enc in ("utf-8", "latin-1"):
            try:
                df = pd.read_csv(io.BytesIO(raw), encoding=enc, low_memory=False)
                break
            except UnicodeDecodeError:
                continue
    else:
        # DBF: write to temp file, read with simpledbf or dbfread.
        with tempfile.NamedTemporaryFile(suffix=".dbf", delete=False) as tf:
            tf.write(raw)
            tmp = tf.name
        try:
            df = read_dbf(tmp)
        finally:
            os.remove(tmp)
    df.columns = [c.upper().strip() for c in df.columns]
    return df


def read_dbf(path):
    """Read a DBF into a DataFrame, trying simpledbf then dbfread."""
    try:
        from simpledbf import Dbf5
        return Dbf5(path, codec="latin-1").to_dataframe()
    except Exception:
        pass
    from dbfread import DBF
    return pd.DataFrame(iter(DBF(path, encoding="latin-1", char_decode_errors="ignore")))


def weight_col(df):
    """Pick the quarterly weight column, handling the FAC -> FAC_TRI redesign break."""
    for c in ("FAC_TRI", "FAC"):
        if c in df.columns:
            return c
    raise KeyError(f"no weight column (FAC/FAC_TRI) in {list(df.columns)[:30]}")


def compute_quarter(df):
    """Weighted partnered/married/cohabiting counts by band for women 20-39.

    Returns dict band -> (cohab_w, married_w, total_w).
    """
    w = weight_col(df)
    # Coerce types: old DBF vintages store EDA / E_CON / SEX as strings.
    for c in ("EDA", "E_CON", "SEX"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df[w] = pd.to_numeric(df[w], errors="coerce")
    # EDA in ENOE uses sentinel codes 97/98/99 (no especificado / 100+). Keep 20-39 only,
    # which excludes all sentinels naturally.
    sub = df[(df["SEX"] == 2) & (df["EDA"] >= 20) & (df["EDA"] <= 39)].copy()
    out = {}
    for (lo, hi), label in BANDS.items():
        band = sub[(sub["EDA"] >= lo) & (sub["EDA"] <= hi)]
        total = band[w].sum()
        cohab = band[band["E_CON"].isin(COHAB_CODES)][w].sum()
        marr = band[band["E_CON"].isin(MARRIED_CODES)][w].sum()
        out[label] = (float(cohab), float(marr), float(total))
    return out


def process_year(year, quarters_mode, tmpdir, keep_zips):
    """Download + compute one year. Returns (band_results, quarters_used, weight_name, fmt_used)."""
    if quarters_mode == "all":
        qlist = [1, 2, 3, 4]
    else:
        # Single representative quarter: prefer T2 (mid-year), then T1, T3, T4.
        # 2005 ENOE began in T1, so T1 is the only guaranteed early quarter; we still
        # try T2 first and fall back. 2020 is excluded upstream.
        qlist = [2, 1, 3, 4]

    accum = {label: [0.0, 0.0, 0.0] for label in BANDS.values()}
    quarters_used = []
    weight_name = None
    fmt_used = None

    for q in qlist:
        if year == 2020 and q == 2:
            continue  # not fielded (COVID / ETOE)
        got = None
        for fmt in ("csv", "dbf"):
            url = url_for(year, q, fmt)
            dest = os.path.join(tmpdir, f"enoe_{year}_t{q}_{fmt}.zip")
            if download(url, dest):
                try:
                    df = read_sdemt(dest)
                    res = compute_quarter(df)
                    weight_name = weight_col(df)
                    got = (q, res, fmt)
                    fmt_used = fmt
                    print(f"    {year} T{q} [{fmt}] weight={weight_name} OK", flush=True)
                except Exception as e:
                    print(f"    {year} T{q} [{fmt}] parse FAILED: {e}", flush=True)
                finally:
                    if not keep_zips and os.path.exists(dest):
                        os.remove(dest)
                if got:
                    break
            else:
                # silent: many (year,quarter,fmt) combos simply do not exist
                pass
        if got:
            _, res, _ = got
            for label, (ch, mr, tot) in res.items():
                accum[label][0] += ch
                accum[label][1] += mr
                accum[label][2] += tot
            quarters_used.append(got[0])
            if quarters_mode != "all":
                break  # single representative quarter is enough

    if not quarters_used:
        return None, [], None, None
    return accum, quarters_used, weight_name, fmt_used


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", default=",".join(map(str, DEFAULT_YEARS)),
                    help="comma-separated years")
    ap.add_argument("--quarters", choices=["rep", "all"], default="rep",
                    help="'rep' = one representative quarter; 'all' = pool all available")
    ap.add_argument("--keep-zips", action="store_true")
    ap.add_argument("--tmpdir", default=None)
    args = ap.parse_args()

    years = [int(y) for y in args.years.split(",") if y.strip()]
    tmpdir = args.tmpdir or tempfile.mkdtemp(prefix="enoe_")
    os.makedirs(tmpdir, exist_ok=True)

    print(f"ENOE -> MEX coupling. years={years} quarters={args.quarters} tmp={tmpdir}")
    rows = []
    for y in years:
        print(f"  year {y} ...", flush=True)
        accum, quarters_used, weight_name, fmt_used = process_year(
            y, args.quarters, tmpdir, args.keep_zips)
        if accum is None:
            print(f"  year {y}: NO QUARTER PROCESSED (skipped)", flush=True)
            continue
        nq = len(quarters_used)
        qtag = ("4q-avg" if nq == 4 else f"{nq}q-avg" if nq > 1
                else f"single-quarter(T{quarters_used[0]})")
        src = (f"INEGI ENOE microdata SDEMT (E_CON x EDA, women SEX=2, "
               f"weighted {weight_name}, {fmt_used}); quarters T{','.join(map(str,quarters_used))}; {qtag}")
        for label in ["20-24", "25-29", "30-34", "35-39"]:
            ch, mr, tot = accum[label]
            if tot <= 0:
                continue
            cohab_sh = ch / tot
            marr_sh = mr / tot
            union = cohab_sh + marr_sh
            rows.append({
                "year": y, "age_band": label,
                "union_total": round(union, 4), "married": round(marr_sh, 4),
                "cohabiting": round(cohab_sh, 4),
                "n_women_weighted": int(round(tot / max(nq, 1))),  # avg per-quarter weighted n
                "observed_or_interpolated": "observed",
                "source": src,
                "coverage_flag": "national",
            })
            print(f"    {y} {label}: union={union:.3f} marr={marr_sh:.3f} "
                  f"cohab={cohab_sh:.3f} n={int(tot/max(nq,1))}", flush=True)

    if not rows:
        print("\nNO ROWS PRODUCED. Likely the network is blocked (curl could not reach "
              "INEGI). Re-run in an environment with outbound HTTPS to inegi.org.mx.",
              file=sys.stderr)
        sys.exit(2)

    out = os.path.join(HERE, "MEX_coupling_annual.csv")
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "age_band", "union_total", "married",
            "cohabiting", "n_women_weighted", "observed_or_interpolated", "source",
            "coverage_flag"])
        w.writeheader()
        w.writerows(rows)
    print(f"\nwrote {out}  ({len(rows)} rows, {len(rows)//4} years)")

    # Validation sanity-check: partnered share must rise with age band within each year.
    print("\nSANITY CHECK (union_total monotone non-decreasing across bands per year):")
    by_year = {}
    for r in rows:
        by_year.setdefault(r["year"], {})[r["age_band"]] = r["union_total"]
    order = ["20-24", "25-29", "30-34", "35-39"]
    for y, d in sorted(by_year.items()):
        seq = [d.get(b) for b in order if b in d]
        mono = all(seq[i] <= seq[i + 1] + 1e-9 for i in range(len(seq) - 1))
        print(f"  {y}: {['%.3f'%v for v in seq]}  {'OK' if mono else 'CHECK'}")


if __name__ == "__main__":
    main()
