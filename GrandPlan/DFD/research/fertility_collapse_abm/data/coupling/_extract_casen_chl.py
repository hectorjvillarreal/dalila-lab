#!/usr/bin/env python3
"""
Stage 2 parallel track — Chile coupling extractor via CASEN microdata download.

Supersedes the REDATAM route. Per the Colombia/Argentina lesson, the microdata-DOWNLOAD
door works where the ECLAC REDATAM host (which carried only old CASEN waves) does not: the
MDS Observatorio Social publishes CASEN national microdata as static .dta.zip files at
  https://observatorio.ministeriodesarrollosocial.gob.cl/storage/docs/casen/{year}/...
no login. CASEN is NATIONAL (urban+rural) — better coverage than Argentina's urban EPH —
but PERIODIC (one cross-section every 2-3 years), so this yields a periodic series, not
annual.

TARGET SERIES (same schema as CRI/COL/ARG_coupling_annual.csv):
  women (sexo==2) aged 20-39, by 5-year band, weighted by the national expansion factor
  (expr):
    union_total = cohabiting + married
    married     = ecivil "Casado(a)"
    cohabiting  = ecivil "Conviviente / pareja" (with OR without acuerdo de unión civil)

ROBUSTNESS — classify ecivil BY LABEL, not numeric code. The numeric coding drifts across
waves (the "Conviviente civil con acuerdo de unión civil" category only exists from 2015,
when Chile's AUC took effect; older waves renumber). Matching the value-label string
("casado" / "conviviente"|"pareja") is wave-stable; raw codes are not.

CIVIL-UNION NOTE: the AUC ("conviviente civil con acuerdo de unión civil") is a legal civil
union distinct from marriage; it is grouped with COHABITING here (the married/cohabiting
split is about formal marriage vs consensual/registered partnership). It is a small share;
flagged in the sidecar.

Output: data/coupling/CHL_coupling_annual.csv  (year = wave year; periodic)
Columns: year, age_band, union_total, married, cohabiting, n_women_weighted,
         observed_or_interpolated, source, coverage_flag, note
"""
import argparse, csv, os, re, sys, time, zipfile, subprocess
import pandas as pd

HOST = "https://observatorio.ministeriodesarrollosocial.gob.cl/storage/docs/casen"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_casen_cache")

# wave -> download URL (resolved live 2026-06; all national STATA .dta.zip)
WAVES = {
    2006: f"{HOST}/2006/casen_2006.dta.zip",
    2009: f"{HOST}/2009/casen_2009.dta.zip",
    2011: f"{HOST}/2011/casen_2011.dta.zip",
    2013: f"{HOST}/2013/casen_2013.dta.zip",
    2015: f"{HOST}/2015/casen_2015.dta.zip",
    2017: f"{HOST}/2017/casen_2017.dta.zip",
    2020: f"{HOST}/2020/casen_en_pandemia_2020.dta.zip",
    2022: f"{HOST}/2022/Base%20de%20datos%20Casen%202022%20STATA_18%20marzo%202024.dta.zip",
}
BANDS = [("20-24", 20, 24), ("25-29", 25, 29), ("30-34", 30, 34), ("35-39", 35, 39)]
WEIGHT_CANDS = ["expr", "expr_osig", "exp", "factor_expansion", "expp"]


def curl_resume(url, out, max_time=1800):
    """Download with resume (-C -); the observatorio server is slow and drops."""
    args = ["curl", "-sL", "-C", "-", "--max-time", str(max_time),
            "-A", "Mozilla/5.0 (research; DFD fertility-collapse coupling extractor)",
            "-o", out, url]
    r = subprocess.run(args, capture_output=True, text=True, timeout=max_time + 60)
    # rc 33 = server can't resume (already complete or no range) — tolerate if file ok
    if r.returncode not in (0, 33):
        raise RuntimeError(f"curl {url} rc={r.returncode}: {r.stderr[:200]}")
    return out


def pick(cols, cands):
    low = {str(c).lower().strip(): c for c in cols}
    for c in cands:
        if c in low:
            return low[c]
    return None


def classify_ecivil(label_series):
    """Map ecivil labels -> 'married' / 'cohab' / 'other'. Wave-stable by string."""
    s = label_series.astype(str).str.lower()
    married = s.str.contains("casad", na=False)
    cohab = s.str.contains("convivi", na=False) | s.str.contains("pareja", na=False)
    return married, cohab


def find_dta(zf):
    cand = [n for n in zf.namelist()
            if n.lower().endswith(".dta") and not n.startswith("__MACOSX")]
    return cand[0] if cand else None


def stata_columns(dpath):
    """Column names, robust to latin-1 .dta that breaks pandas' utf-8 assumption."""
    try:
        return list(pd.io.stata.StataReader(dpath).read(nrows=50).columns)
    except (UnicodeDecodeError, ValueError):
        import pyreadstat
        _, meta = pyreadstat.read_dta(dpath, metadataonly=True, encoding="LATIN1")
        return list(meta.column_names)


def read_labeled(dpath, cols):
    """Read `cols` with value labels applied; pyreadstat LATIN1 fallback for 2020-style
    files where pandas read_stata raises UnicodeDecodeError on the value labels."""
    try:
        return pd.read_stata(dpath, columns=cols, convert_categoricals=True)
    except (UnicodeDecodeError, ValueError):
        import pyreadstat
        df, _ = pyreadstat.read_dta(dpath, usecols=cols, apply_value_formats=True,
                                    formats_as_category=False, encoding="LATIN1")
        return df


def process_wave(year, url, force_dl=False):
    os.makedirs(CACHE, exist_ok=True)
    dpath = os.path.join(CACHE, f"{year}.dta")
    # use the extracted .dta if already cached; else download (resume) + unzip
    if force_dl or not (os.path.exists(dpath) and os.path.getsize(dpath) > 1_000_000):
        zpath = os.path.join(CACHE, f"{year}.zip")
        if force_dl or not (os.path.exists(zpath) and os.path.getsize(zpath) > 1_000_000):
            print(f"    downloading CASEN {year} ...", flush=True)
            curl_resume(url, zpath)
        for attempt in (1, 2):       # validate zip; one resume retry if truncated
            try:
                with zipfile.ZipFile(zpath) as zf:
                    dta = find_dta(zf)
                    if not dta:
                        raise RuntimeError(f"{year}: no .dta in zip")
                    with open(dpath, "wb") as f:
                        f.write(zf.read(dta))
                break
            except zipfile.BadZipFile:
                if attempt == 2:
                    raise
                print(f"    {year}: truncated zip, resuming ...", flush=True)
                curl_resume(url, zpath)
    # detect variables + read labeled columns, robust to latin-1 .dta (e.g. CASEN 2020,
    # where pandas mis-decodes strings as utf-8). Fall back to pyreadstat with LATIN1.
    import warnings; warnings.filterwarnings("ignore")
    cols = stata_columns(dpath)
    wv = pick(cols, WEIGHT_CANDS)
    sv = pick(cols, ["sexo", "sex"])
    av = pick(cols, ["edad", "edadp", "edad_anos"])
    ev = pick(cols, ["ecivil", "e_civil"])
    if not all([wv, sv, av, ev]):
        raise RuntimeError(f"{year}: missing vars sex={sv} age={av} ecivil={ev} weight={wv}; "
                           f"have sample {list(cols)[:15]}")
    df = read_labeled(dpath, [sv, av, ev, wv])   # ecivil/sexo as label strings
    age = pd.to_numeric(df[av], errors="coerce")
    w = pd.to_numeric(df[wv], errors="coerce")
    sexlab = df[sv].astype(str).str.lower()
    female = sexlab.str.contains("mujer", na=False) | (sexlab.str.strip() == "2")
    married, cohab = classify_ecivil(df[ev])
    keep = female & age.between(20, 39) & w.notna()
    acc = {}
    for band, lo, hi in BANDS:
        m = keep & age.between(lo, hi)
        tot = w[m].sum()
        acc[band] = dict(total=tot,
                         marr=w[m & married].sum(),
                         cohab=w[m & cohab].sum())
    return acc, (sv, av, ev, wv)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", nargs="*", type=int, default=sorted(WAVES))
    ap.add_argument("--out", default=os.path.join(HERE, "CHL_coupling_annual.csv"))
    args = ap.parse_args()
    rows = []
    print(f"{'wave':5s} {'band':6s} {'cohab%':>7s} {'marr%':>7s} {'union%':>7s} {'n_women':>11s}")
    for y in args.years:
        if y not in WAVES:
            print(f"  {y}: no wave URL; skipping"); continue
        try:
            acc, vars_ = process_wave(y, WAVES[y])
        except Exception as e:
            print(f"  {y}: ERROR {e}", file=sys.stderr); continue
        sv, av, ev, wv = vars_
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
                "observed_or_interpolated": "observed",
                "source": (f"MDS CASEN {y} microdata; ecivil (by label: casado=married, "
                           f"conviviente=cohab) x {av}, women {sv}=mujer, weighted {wv}"),
                "coverage_flag": "national (urban+rural)",
                "note": "CASEN periodic wave (single cross-section)",
            })
            print(f"  {y} {band:6s} {ch*100:6.1f} {mr*100:6.1f} {ut*100:6.1f} {int(t):11d}")
        time.sleep(0.2)
    if not rows:
        print("\nNO ROWS produced.", file=sys.stderr); sys.exit(1)
    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "age_band", "union_total", "married",
            "cohabiting", "n_women_weighted", "observed_or_interpolated", "source",
            "coverage_flag", "note"])
        w.writeheader(); w.writerows(rows)
    print(f"\nwrote {args.out}  ({len(rows)} rows, {len(rows)//4} waves)")


if __name__ == "__main__":
    main()
