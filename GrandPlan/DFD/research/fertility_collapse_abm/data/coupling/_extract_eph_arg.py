#!/usr/bin/env python3
"""
Stage 2 parallel track — Argentina coupling extractor via INDEC EPH microdata download.

Supersedes the REDATAM route (_extract_redatam_arg.py). Per the Colombia lesson, the
microdata-DOWNLOAD door works where the processing engine does not: INDEC publishes EPH
continua per-quarter microdata as static zips at
  https://www.indec.gob.ar/ftp/cuadros/menusuperior/eph/EPH_usu_{q}_Trim_{year}_txt.zip
no login, no REDATAM. Mapped availability (probed 2026-06): 2017 T2-T4, 2018-2025 all
quarters. (2016 and pre-2016 are on a different path; 2007-2015 is INDEC-intervention-era
and deliberately excluded.)

TARGET SERIES (same schema as CRI/COL_coupling_annual.csv):
  women (CH04==2) aged 20-39, by 5-year band, weighted by PONDERA:
    union_total = cohabiting + married   (CH07 in {1,2})
    cohabiting  = CH07 == 1  (unido/a)
    married     = CH07 == 2  (casado/a)
  CH07 situación conyugal: 1 unido, 2 casado, 3 separado/divorciado, 4 viudo, 5 soltero.
  CH04 sexo: 1 varón, 2 mujer.  CH06 edad (años).  PONDERA = factor de expansión.

EPH is quarterly and URBAN ONLY (31 aglomerados). Each annual value pools all available
quarters of that year (summing PONDERA-weighted counts), mirroring the GEIH monthly pool.
Coverage is urban — flagged in every row; Argentina is ~92% urban, but the rural gap is a
real caveat to carry into any cross-country comparison (CRI/COL are national urban+rural).

Output: data/coupling/ARG_coupling_annual.csv
Columns: year, age_band, union_total, married, cohabiting, n_women_weighted,
         observed_or_interpolated, source, coverage_flag, note
"""
import argparse, csv, io, os, re, sys, time, zipfile, subprocess
import pandas as pd

HOST = "https://www.indec.gob.ar/ftp/cuadros/menusuperior/eph"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_eph_cache")

# (year -> list of available quarters) confirmed live by zip-signature probe 2026-06
PERIODS = {
    2017: [2, 3, 4], 2018: [1, 2, 3, 4], 2019: [1, 2, 3, 4], 2020: [1, 2, 3, 4],
    2021: [1, 2, 3, 4], 2022: [1, 2, 3, 4], 2023: [1, 2, 3, 4], 2024: [1, 2, 3, 4],
    2025: [1, 2, 3, 4],   # provisional (latest year)
}
BANDS = [("20-24", 20, 24), ("25-29", 25, 29), ("30-34", 30, 34), ("35-39", 35, 39)]
COHAB_CODES, MARRIED_CODES = {1}, {2}     # CH07: 1 unido, 2 casado


def url_for(year, q):
    return f"{HOST}/EPH_usu_{q}_Trim_{year}_txt.zip"


def curl(url, out, max_time=300):
    args = ["curl", "-sL", "--fail", "--max-time", str(max_time),
            "-A", "Mozilla/5.0 (research; DFD fertility-collapse coupling extractor)",
            "-o", out, url]
    r = subprocess.run(args, capture_output=True, text=True, timeout=max_time + 30)
    if r.returncode != 0:
        raise RuntimeError(f"curl {url} rc={r.returncode}: {r.stderr[:200]}")
    return out


def individual_frame(zf):
    """Read the EPH person/individual base as a dataframe.

    The base file is usually 'usu_individual_*' but older quarters (e.g. 2020 T4)
    name it 'usu_personas_*'. Match either, exclude the household ('hogar') file.
    """
    cand = [n for n in zf.namelist()
            if any(k in n.lower() for k in ("individual", "personas", "persona"))
            and "hogar" not in n.lower()
            and n.lower().endswith((".txt", ".csv"))]
    if not cand:
        return None
    raw = zf.read(cand[0])
    for sep in (";", ",", "\t", "|"):
        try:
            df = pd.read_csv(io.BytesIO(raw), sep=sep, encoding="latin-1",
                             low_memory=False, dtype=str, on_bad_lines="skip")
            if df.shape[1] > 10 and pick(df.columns, ["ch07"]):
                return df
        except Exception:
            continue
    return None


def pick(cols, cands):
    low = {str(c).lower().strip(): c for c in cols}
    for c in cands:
        if c in low:
            return low[c]
    return None


def accumulate(df, acc):
    cu = pick(df.columns, ["ch07"]); ca = pick(df.columns, ["ch06"])
    cs = pick(df.columns, ["ch04"]); cw = pick(df.columns, ["pondera"])
    if not all([cu, ca, cs, cw]):
        raise RuntimeError(f"missing cols conyugal={cu} age={ca} sex={cs} weight={cw}; "
                           f"have={list(df.columns)[:20]}")
    d = df[[cu, ca, cs, cw]].copy()
    for c in (cu, ca, cs):
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d[cw] = pd.to_numeric(d[cw].astype(str).str.replace(",", ".", regex=False),
                          errors="coerce")
    d = d.dropna(subset=[cu, ca, cs, cw])
    d = d[(d[cs] == 2) & (d[ca] >= 20) & (d[ca] <= 39)]
    for band, lo, hi in BANDS:
        b = d[(d[ca] >= lo) & (d[ca] <= hi)]
        w = b[cw]
        acc[band]["total"] += w.sum()   # all women in band = denominator
        acc[band]["cohab"] += w[b[cu].isin(COHAB_CODES)].sum()
        acc[band]["marr"]  += w[b[cu].isin(MARRIED_CODES)].sum()


def run_year(year, quarters, max_q=None):
    os.makedirs(CACHE, exist_ok=True)
    qs = quarters[:max_q] if max_q else quarters
    acc = {b: {"total": 0.0, "cohab": 0.0, "marr": 0.0} for b, _, _ in BANDS}
    nq = 0
    for q in qs:
        fn = os.path.join(CACHE, f"{year}_T{q}.zip")
        if not (os.path.exists(fn) and os.path.getsize(fn) > 10000):
            try:
                print(f"    downloading {year} T{q} ...")
                curl(url_for(year, q), fn)
            except Exception as e:
                print(f"    ! download failed {year} T{q}: {e}", file=sys.stderr); continue
        try:
            with zipfile.ZipFile(fn) as zf:
                df = individual_frame(zf)
                if df is None:
                    print(f"    ! no individual base {year} T{q}", file=sys.stderr); continue
                accumulate(df, acc); nq += 1
                print(f"    ok {year} T{q}")
        except zipfile.BadZipFile:
            print(f"    ! bad zip {year} T{q}", file=sys.stderr); continue
    if nq == 0:
        raise RuntimeError(f"{year}: no usable quarters")
    return acc, nq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", nargs="*", type=int, default=sorted(PERIODS))
    ap.add_argument("--max-q", type=int, default=None, help="cap quarters/year")
    ap.add_argument("--out", default=os.path.join(HERE, "ARG_coupling_annual.csv"))
    args = ap.parse_args()

    rows = []
    print(f"{'yr':4s} {'band':6s} {'cohab%':>7s} {'marr%':>7s} {'union%':>7s} {'n_women':>11s}")
    for y in args.years:
        if y not in PERIODS:
            print(f"  {y}: no period map; skipping"); continue
        try:
            acc, nq = run_year(y, PERIODS[y], args.max_q)
        except Exception as e:
            print(f"  {y}: ERROR {e}", file=sys.stderr); continue
        proxy = (args.max_q == 1) or (nq < 3)
        note = f"{'partial' if proxy else 'full-year'} pooled ({nq} of {len(PERIODS[y])} quarters)"
        prov = "provisional" if y >= 2025 else "observed"
        for band, _, _ in BANDS:
            t = acc[band]["total"]
            if t <= 0:
                continue
            ch, mr = acc[band]["cohab"] / t, acc[band]["marr"] / t
            ut = ch + mr
            rows.append({
                "year": y, "age_band": band,
                "union_total": round(ut, 4), "married": round(mr, 4),
                "cohabiting": round(ch, 4), "n_women_weighted": int(round(t)),
                "observed_or_interpolated": prov,
                "source": (f"INDEC EPH continua {y} microdata (usu_individual, "
                           f"{nq} quarters pooled); CH07 situación conyugal x CH06 edad, "
                           f"women CH04=2, weighted PONDERA"),
                "coverage_flag": "urban (31 aglomerados)",
                "note": note,
            })
            print(f"  {y} {band:6s} {ch*100:6.1f} {mr*100:6.1f} {ut*100:6.1f} {int(t):11d}")
        time.sleep(0.2)
    if not rows:
        print("\nNO ROWS — nothing downloaded/processed.", file=sys.stderr); sys.exit(1)
    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "age_band", "union_total", "married",
            "cohabiting", "n_women_weighted", "observed_or_interpolated", "source",
            "coverage_flag", "note"])
        w.writeheader(); w.writerows(rows)
    print(f"\nwrote {args.out}  ({len(rows)} rows, {len(rows)//4} years)")


if __name__ == "__main__":
    main()
