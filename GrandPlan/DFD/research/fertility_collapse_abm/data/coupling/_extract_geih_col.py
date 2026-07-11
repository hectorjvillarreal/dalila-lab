#!/usr/bin/env python3
"""
Stage 1.5 -- Colombia coupling extractor from DANE GEIH person-level microdata.

Colombia has NO public REDATAM server for GEIH (unlike Costa Rica's INEC), so this
extractor downloads the raw GEIH microdata directly from DANE's NADA catalog
(microdatos.dane.gov.co), no login required, and computes the weighted shares
locally with pandas.

TARGET SERIES (mirrors CRI_coupling_annual.csv):
  For women (P6020 == 2) aged 20-39, by 5-year band (20-24,25-29,30-34,35-39):
    union_total = share in a co-residential union (partnered)
    married     = share married (estado civil "casado")
    cohabiting  = share in union libre (free union)
  weighted by the GEIH expansion factor (fex_c / fex_c_2011).

UNION VARIABLE -- P6070 (estado civil), person module
  "Caracteristicas generales, seguridad social en salud y educacion":
    1 = union libre  < 2 anios     -> cohabiting
    2 = union libre >= 2 anios     -> cohabiting
    3 = casado(a)                  -> married
    4 = soltero/separado/divorciado (post-2018 redesign collapses some codes)
    5 = viudo(a)
    6 = soltero(a)
  partnered = {1,2,3}; cohabiting = {1,2}; married = {3}.
  (DANE's published P6070 labels: 1 "No esta casado y vive en pareja hace menos de
   dos anios", 2 "No esta casado y vive en pareja hace dos anios o mas",
   3 "Esta casado(a)", 4 "Esta separado(a) o divorciado(a)", 5 "Esta viudo(a)",
   6 "Esta soltero(a)".  We treat 1,2 as cohabiting, 3 as married.)

AGE VARIABLE -- P6040 (anios cumplidos), person module.
SEX VARIABLE -- P6020 (1 hombre, 2 mujer), person module.
WEIGHT       -- fex_c / fex_c_2011 (factor de expansion), person module.
              The variable name changed across redesigns; we auto-detect among a
              small candidate list.

GEIH is CONTINUOUS: one set of files per MONTH. We pool all available months in a
year to an annual series. The person module file inside each monthly zip is the
one whose name contains "Caracteristicas generales" (a.k.a. "Personas").

REPRODUCIBILITY
  * The DANE NADA download endpoint is /index.php/catalog/<CAT>/download/<ID>.
  * The per-file numeric <ID>s are scraped at runtime from the catalog's
    get-microdata page, so we do not hard-code brittle IDs. (If DANE changes the
    page markup, update the scrape regex in discover_downloads().)
  * Catalog IDs per year are in CATALOGS below (confirmed live 2026-06):
        2024 -> 819,  2023 -> 782,  2022 -> 771,  2021 -> 701,  2007 -> 317.
    Add more years by adding {year: catalog_id}.

2022 'MARCO 2018' CAVEAT
  DANE re-based the GEIH sample/weights on the 2018 Census ("Marco 2018") and
  redesigned the questionnaire effective ~2021-2022. Pre- and post-redesign weights
  and some variable codings are NOT strictly comparable; P6070's free-union split
  wording was also refined. We carry coverage as "national" throughout but the
  source string records the year so the redesign break is auditable. Treat the
  2007-vs-2024 *level* difference with that caveat in mind.

Output: data/coupling/COL_coupling_annual.csv
Columns: year, age_band, union_total, married, cohabiting, n_women_weighted,
         observed_or_interpolated, source, coverage_flag, note
(shares are fractions 0-1 of women in that age band.)

Usage:
  source ~/miniforge3/etc/profile.d/conda.sh && conda activate dalila
  python _extract_geih_col.py                 # all years in CATALOGS, full pooling
  python _extract_geih_col.py --years 2024    # one year
  python _extract_geih_col.py --years 2024 --max-months 1   # single-month proxy
"""
import argparse, csv, io, os, re, sys, time, zipfile, subprocess
import pandas as pd

HOST = "https://microdatos.dane.gov.co"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_geih_cache")

# year -> NADA catalog id (confirmed live June 2026)
CATALOGS = {
    2007: 317,
    2021: 701,
    2022: 771,
    2023: 782,
    2024: 819,
}

BANDS = [("20-24", 20, 24), ("25-29", 25, 29), ("30-34", 30, 34), ("35-39", 35, 39)]
COHAB_CODES = {1, 2}      # union libre (free union), both duration brackets
MARRIED_CODES = {3}       # casado(a)

# candidate column names (case-insensitive) for each role across GEIH vintages
UNION_CANDS  = ["p6070"]
AGE_CANDS    = ["p6040"]
SEX_CANDS    = ["p6020"]
WEIGHT_CANDS = ["fex_c_2011", "fex_c", "fex_dpto", "factor"]


def curl(url, out=None, max_time=600):
    args = ["curl", "-sL", "--fail", "--max-time", str(max_time),
            "-A", "Mozilla/5.0 (research; DFD fertility-collapse coupling extractor)"]
    if out:
        args += ["-o", out, url]
        r = subprocess.run(args, capture_output=True, text=True, timeout=max_time + 30)
        if r.returncode != 0:
            raise RuntimeError(f"curl {url} rc={r.returncode}: {r.stderr[:200]}")
        return out
    r = subprocess.run(args + [url], capture_output=True, timeout=max_time + 30)
    if r.returncode != 0:
        raise RuntimeError(f"curl {url} rc={r.returncode}: {r.stderr[:200]}")
    return r.stdout.decode("utf-8", "replace")


def discover_downloads(catalog_id):
    """Scrape (filename, download_url) pairs from the get-microdata page.

    DANE's NADA renders a table of data files; each row links to
    /index.php/catalog/<id>/download/<resource_id>. We pair each download link
    with the nearest preceding human file label.
    """
    html = curl(f"{HOST}/index.php/catalog/{catalog_id}/get-microdata")
    pairs = []
    # links look like: href="/index.php/catalog/819/download/23300?..."
    for m in re.finditer(rf'/index\.php/catalog/{catalog_id}/download/(\d+)', html):
        dl_id = m.group(1)
        # look back a window for a nearby filename-ish token
        ctx = html[max(0, m.start() - 600): m.start()]
        name = ""
        nm = re.findall(r'>([^<>]{3,80}?\.(?:zip|csv|sav|dta|txt|rar))<', ctx, re.I)
        if nm:
            name = nm[-1].strip()
        else:
            nm2 = re.findall(r'>([A-Za-zÁÉÍÓÚáéíóúÑñ_][^<>]{2,60})<', ctx)
            if nm2:
                name = nm2[-1].strip()
        pairs.append((name, f"{HOST}/index.php/catalog/{catalog_id}/download/{dl_id}"))
    # de-dup by url, keep first label
    seen, out = set(), []
    for name, url in pairs:
        if url in seen:
            continue
        seen.add(url)
        out.append((name, url))
    return out


def is_month_data(name):
    """A monthly GEIH data resource (zip) -- exclude docs/dictionaries/manuals."""
    n = name.lower()
    if not n.endswith((".zip", ".rar", ".csv", ".sav", ".dta", ".txt")):
        # NADA sometimes omits the extension in the label; fall back on month names
        pass
    months = ("ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep",
              "oct", "nov", "dic")
    has_month = any(mo in n for mo in months)
    is_doc = any(k in n for k in ("manual", "dicc", "ddi", "metad", "ficha",
                                  "anexo", "cuestion", "boletin", ".pdf"))
    return has_month and not is_doc


def find_person_csv(zf):
    """Inside a monthly GEIH zip, find the person-level 'Caracteristicas generales'
    file (csv/sav/dta/txt). Returns (name, dataframe)."""
    cand = []
    for n in zf.namelist():
        ln = n.lower()
        if any(k in ln for k in ("caracteristicas generales", "caracteristicas_generales",
                                 "personas", "caract")):
            cand.append(n)
    # fallback: any tabular file that contains the union column once read
    targets = cand or [n for n in zf.namelist()
                       if n.lower().endswith((".csv", ".txt", ".sav", ".dta"))]
    for n in targets:
        df = read_tabular(zf, n)
        if df is not None and pick(df.columns, UNION_CANDS):
            return n, df
    return None, None


def read_tabular(zf, name):
    raw = zf.read(name)
    ln = name.lower()
    bio = io.BytesIO(raw)
    try:
        if ln.endswith((".csv", ".txt")):
            for sep in (";", ",", "\t", "|"):
                bio.seek(0)
                try:
                    df = pd.read_csv(bio, sep=sep, encoding="latin-1",
                                     low_memory=False, dtype=str, on_bad_lines="skip")
                    if df.shape[1] > 3:
                        return df
                except Exception:
                    continue
            return None
        if ln.endswith(".sav"):
            import pyreadstat, tempfile
            with tempfile.NamedTemporaryFile(suffix=".sav", delete=False) as tf:
                tf.write(raw); tmp = tf.name
            df, _ = pyreadstat.read_sav(tmp); os.unlink(tmp); return df
        if ln.endswith(".dta"):
            bio.seek(0)
            return pd.read_stata(bio, convert_categoricals=False)
    except Exception as e:
        print(f"      ! could not read {name}: {e}", file=sys.stderr)
    return None


def pick(cols, cands):
    low = {c.lower().strip(): c for c in cols}
    for cand in cands:
        if cand in low:
            return low[cand]
    return None


def accumulate(df, acc):
    """Add this monthly person frame's weighted counts into acc (per band)."""
    cu = pick(df.columns, UNION_CANDS)
    ca = pick(df.columns, AGE_CANDS)
    cs = pick(df.columns, SEX_CANDS)
    cw = pick(df.columns, WEIGHT_CANDS)
    if not all([cu, ca, cs, cw]):
        raise RuntimeError(f"missing cols: union={cu} age={ca} sex={cs} weight={cw}; "
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
        acc[band]["total"] += w.sum()
        acc[band]["cohab"] += w[b[cu].isin(COHAB_CODES)].sum()
        acc[band]["marr"]  += w[b[cu].isin(MARRIED_CODES)].sum()
    return (cu, ca, cs, cw)


def run_year(year, catalog_id, max_months=None):
    os.makedirs(CACHE, exist_ok=True)
    pairs = discover_downloads(catalog_id)
    months = [(n, u) for n, u in pairs if is_month_data(n)]
    if not months:
        # last resort: take every .zip resource and let find_person_csv filter
        months = [(n, u) for n, u in pairs if n.lower().endswith((".zip", ".rar"))]
    if max_months:
        months = months[:max_months]
    print(f"  {year}: {len(months)} monthly resources to pool")
    acc = {band: {"total": 0.0, "cohab": 0.0, "marr": 0.0} for band, _, _ in BANDS}
    used_cols, n_months_ok = None, 0
    for name, url in months:
        fn = os.path.join(CACHE, f"{year}_" + re.sub(r"[^A-Za-z0-9_.-]", "_", name or url.split("/")[-1]))
        if not fn.endswith((".zip", ".rar")):
            fn += ".zip"
        if not (os.path.exists(fn) and os.path.getsize(fn) > 10000):
            print(f"    downloading {name or url} ...")
            try:
                curl(url, out=fn)
            except Exception as e:
                print(f"    ! download failed: {e}", file=sys.stderr); continue
        try:
            with zipfile.ZipFile(fn) as zf:
                pn, df = find_person_csv(zf)
                if df is None:
                    print(f"    ! no person module in {name}", file=sys.stderr); continue
                used_cols = accumulate(df, acc); n_months_ok += 1
                print(f"    ok {name}  (person file: {pn})")
        except zipfile.BadZipFile:
            print(f"    ! bad zip {name}", file=sys.stderr); continue
    if n_months_ok == 0:
        raise RuntimeError(f"{year}: no usable monthly files")
    return acc, n_months_ok, used_cols


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", nargs="*", type=int, default=sorted(CATALOGS))
    ap.add_argument("--max-months", type=int, default=None,
                    help="cap months per year (1 = single-month proxy)")
    args = ap.parse_args()

    out = os.path.join(HERE, "COL_coupling_annual.csv")
    rows = []
    print(f"{'year':5s} {'band':6s} {'cohab%':>7s} {'marr%':>7s} {'union%':>7s} {'n_women':>12s}")
    for y in args.years:
        if y not in CATALOGS:
            print(f"  {y}: no catalog id known; skipping"); continue
        try:
            acc, nmo, cols = run_year(y, CATALOGS[y], args.max_months)
        except Exception as e:
            print(f"  {y}: ERROR {e}", file=sys.stderr); continue
        proxy = (args.max_months == 1) or (nmo < 6)
        note = (f"single-month-proxy ({nmo} mo)" if proxy
                else f"full-year pooled ({nmo} mo)")
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
                "source": (f"DANE GEIH {y} microdata (catalog {CATALOGS[y]}); "
                           f"P6070 estado civil x P6040 edad, women P6020=2, "
                           f"weighted {cols[3] if cols else 'fex_c'}; pooled {nmo} mo"),
                "coverage_flag": "national",
                "note": note,
            })
            print(f"  {y} {band:6s} {ch*100:6.1f} {mr*100:6.1f} {ut*100:6.1f} {int(t):12d}")
        time.sleep(0.5)
    if not rows:
        print("\nNO ROWS COMPUTED -- nothing downloaded/processed.", file=sys.stderr)
        sys.exit(1)
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "age_band", "union_total", "married",
            "cohabiting", "n_women_weighted", "observed_or_interpolated", "source",
            "coverage_flag", "note"])
        w.writeheader(); w.writerows(rows)
    print(f"\nwrote {out}  ({len(rows)} rows, {len(rows)//4} years)")


if __name__ == "__main__":
    main()
