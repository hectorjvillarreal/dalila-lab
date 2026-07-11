#!/usr/bin/env python3
"""
Stage 1.5 Addendum A -- Colombia coupling extractor v2 (DANE GEIH microdata).

Supersedes _extract_geih_col.py. Built after a forensic pass on real DANE files
(2024 Ene + 2007 Ene), which exposed three structural breaks the v1 extractor got
wrong. This v2 handles all three explicitly and leaves an audit trail.

WHAT v1 GOT WRONG (and v2 fixes)
  1. Download discovery. DANE NADA puts the filename in an onclick="mostrarModal(
     'NAME.zip','.../download/<id>')" handler, NOT in anchor text. v1's regex
     scraped empty names, so its month filter matched nothing. v2 parses
     mostrarModal() directly.
  2. Sex variable renamed across the 2021-2022 redesign. Pre-redesign person files
     use P6020 (1 Hombre / 2 Mujer); the post-redesign (Marco 2018) files use
     P3271. v1 hard-assumed P6020 and would have dropped every post-2021 year.
     v2 auto-detects sex among {P6020, P3271}.
  3. Weight variable renamed. Pre-redesign weight = Fex_c_2011; post-redesign =
     FEX_C18. v1's candidate list had neither spelling reliably. v2 auto-detects.
  Plus: geographic-domain double-count. Pre-redesign monthly zips split the person
     module into three representation domains -- Cabecera (urban), Resto (rural),
     and Area/metro (a redundant SUBSET already inside Cabecera). v1 read only the
     first match and mislabelled it "national". v2 pools Cabecera+Resto (the
     non-overlapping national partition) and DROPS Area.
  Plus: per-month format de-duplication. For 2007 and 2021 each month is published
     in several formats (.csv.zip/.spss.zip/.dta.zip) as separate catalog
     resources; pooling all of them triple-weights those months. v2 keeps exactly
     one resource per month.

CHECK A RESULT (the load-bearing one, from DANE's own value labels):
  P6070 "estado civil" is IDENTICALLY coded on both sides of the redesign --
    1 = vive en pareja < 2 anios   -> cohabiting (union libre)
    2 = vive en pareja >= 2 anios  -> cohabiting (union libre)
    3 = casado(a)                  -> married
    4 = separado/divorciado, 5 = viudo, 6 = soltero
  The UNION definition does not move across the break. Only the sex var (P6020->
  P3271) and the weight var (Fex_c_2011->FEX_C18) were renamed. So a coupling
  discontinuity at the redesign would be REAL, not a recoding artifact.

TARGET SERIES (same schema as CRI_coupling_annual.csv):
  women (sex==2) aged 20-39, by 5-year band, weighted by the expansion factor:
    union_total = cohabiting + married   (P6070 in {1,2,3})
    married     = P6070 == 3
    cohabiting  = P6070 in {1,2}

Usage:
  source ~/miniforge3/etc/profile.d/conda.sh && conda activate dalila
  python _extract_geih_col_v2.py                      # all years, full 12-mo pool
  python _extract_geih_col_v2.py --years 2024 2007    # selected years
  python _extract_geih_col_v2.py --max-months 1       # fast single-month proxy
"""
import argparse, csv, io, os, re, sys, time, zipfile, subprocess, tempfile
import pandas as pd

HOST  = "https://microdatos.dane.gov.co"
HERE  = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_geih_cache")

# year -> NADA national-annual catalog id (resolved live 2026-06 from the catalog
# search API; only the bare "GEIH - YYYY" national operations, never the Ciudades
# Intermedias / Nuevos Departamentos / San Andres supplementary samples).
CATALOGS = {
    2007: 317, 2008: 206, 2009: 207, 2010: 205, 2011: 182, 2012: 77,
    2013: 68,  2014: 328, 2015: 356, 2016: 427, 2017: 458, 2018: 547,
    2019: 599, 2020: 780, 2021: 701, 2022: 771, 2023: 782, 2024: 819,
}
REDESIGN_YEARS = {2021, 2022}   # GEIH "Marco 2018" redesign / splice window

BANDS = [("20-24", 20, 24), ("25-29", 25, 29), ("30-34", 30, 34), ("35-39", 35, 39)]
COHAB_CODES, MARRIED_CODES = {1, 2}, {3}

SEX_CANDS    = ["p6020", "p3271"]
AGE_CANDS    = ["p6040"]
UNION_CANDS  = ["p6070"]
WEIGHT_CANDS = ["fex_c_2011", "fex_c18", "fex_c_18", "fex_18", "fex_c",
                "fex_dpto", "fex_dp", "factor", "fex"]

MONTHS = {  # canonical month number -> name tokens that may appear in a resource name
    1: ["enero", "ene"], 2: ["febrero", "feb"], 3: ["marzo", "mar"],
    4: ["abril", "abr"], 5: ["mayo", "may"], 6: ["junio", "jun"],
    7: ["julio", "jul"], 8: ["agosto", "ago"], 9: ["septiembre", "sept", "sep"],
    10: ["octubre", "oct"], 11: ["noviembre", "nov"], 12: ["diciembre", "dic"],
}
FMT_TOKENS = [".csv", ".dta", ".spss", ".sav", ".txt"]   # format suffixes in names
AGG_TOKENS = ["semestre", "proyeccion", "fex proy", "total_", "total ",
              "consolid", "anual", "marco-2018(i", "marco_2018(i"]


def curl(url, out=None, max_time=900):
    base = ["curl", "-sL", "--fail", "--max-time", str(max_time),
            "-A", "Mozilla/5.0 (research; DFD fertility-collapse coupling extractor)"]
    if out:
        r = subprocess.run(base + ["-o", out, url], capture_output=True,
                           text=True, timeout=max_time + 60)
        if r.returncode != 0:
            raise RuntimeError(f"curl {url} rc={r.returncode}: {r.stderr[:200]}")
        return out
    r = subprocess.run(base + [url], capture_output=True, timeout=max_time + 60)
    if r.returncode != 0:
        raise RuntimeError(f"curl {url} rc={r.returncode}: {r.stderr[:200]}")
    return r.stdout.decode("utf-8", "replace")


def discover_downloads(catalog_id):
    """(name, url) for every data resource, parsed from the mostrarModal() handler."""
    html = curl(f"{HOST}/index.php/catalog/{catalog_id}/get-microdata")
    pairs, seen = [], set()
    for name, dl_id in re.findall(
            r"mostrarModal\('([^']+)'\s*,\s*'[^']*?/download/(\d+)\s*'\)", html):
        if dl_id in seen:
            continue
        seen.add(dl_id)
        pairs.append((name.strip(), f"{HOST}/index.php/catalog/{catalog_id}/download/{dl_id}"))
    return pairs


_FULL = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
         7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre",
         12: "diciembre"}
_ABBR = {1: "ene", 2: "feb", 3: "mar", 4: "abr", 5: "may", 6: "jun", 7: "jul",
         8: "ago", 9: "sep", 10: "oct", 11: "nov", 12: "dic"}

def month_of(name):
    # Strip the GEIH frame name "Marco 2018" first: it collides with the "mar"
    # (marzo) abbreviation and would mis-tag every 2022 file as March.
    n = re.sub(r"marco[\s_-]*20?1?8?", " ", name.lower())
    for num, full in _FULL.items():        # full names are unambiguous; check first
        if full in n:
            return num
    for num, ab in _ABBR.items():          # abbreviations only if no full name
        if re.search(rf"(?<![a-z]){ab}(?![a-z])", n):
            return num
    return None


def is_aggregate(name):
    n = name.lower()
    return any(tok in n for tok in AGG_TOKENS)


def fmt_rank(name):
    """Lower rank = preferred. Generic (no format suffix) beats spss/sav/csv/dta."""
    n = name.lower()
    if not any(tok in n for tok in FMT_TOKENS):
        return 0                       # generic monthly zip (bundles formats or sav)
    order = [".spss", ".sav", ".csv", ".dta", ".txt"]
    for i, tok in enumerate(order, start=1):
        if tok in n:
            return i
    return 9


def select_monthly(pairs):
    """One resource per month: drop aggregates, keep best-format per calendar month."""
    by_month = {}
    for name, url in pairs:
        if is_aggregate(name):
            continue
        m = month_of(name)
        if m is None:
            continue
        cur = by_month.get(m)
        if cur is None or fmt_rank(name) < fmt_rank(cur[0]):
            by_month[m] = (name, url)
    return [by_month[m] for m in sorted(by_month)]


# ---- reading person modules out of a monthly zip -------------------------------

def _is_person_member(member):
    n = member.lower()
    if n.endswith("/"):
        return False
    looks_person = (("aracter" in n and "general" in n) or "personas" in n)
    is_other = any(k in n for k in ("hogar", "vivienda", "ocupad", "desocup",
                                    "inactiv", "fuerza", "migrac", "ingreso",
                                    "otras", "otros", "trabajo infantil"))
    return looks_person and not is_other


def _domain(member):
    n = member.lower()
    if "cabecera" in n:
        return "cab"
    if "resto" in n:
        return "resto"
    return "other"   # area/metro (redundant) OR a single national file


def _inner_zip_rank(name):
    ln = name.lower()
    if "csv" in ln:  return 0
    if "sav" in ln or "spss" in ln: return 1
    if "dta" in ln:  return 2
    return 3

def _frames_from_zip(zf):
    """Person frames found directly inside this ZipFile (no recursion)."""
    members = [m for m in zf.namelist() if _is_person_member(m)]
    if not members:
        return []
    for fmt in (".csv", ".sav", ".dta", ".txt"):
        sel = [m for m in members if m.lower().endswith(fmt)]
        if sel:
            break
    else:
        sel = members
    domains = {_domain(m) for m in sel}
    if "cab" in domains or "resto" in domains:
        keep = [m for m in sel if _domain(m) in ("cab", "resto")]
    else:
        keep = sel
    out = []
    for m in keep:
        df = read_tabular(zf, m)
        if df is not None and pick(df.columns, UNION_CANDS):
            out.append((m, df))
    return out


def person_frames(zf):
    """Return list of (member_name, dataframe) for the national person module.

    Picks one format, then pools Cabecera+Resto when the file is domain-split
    (dropping the redundant Area/metro cut), else uses the single national file.

    Some 2023/2024 months package data as NESTED zips (CSV.zip / DTA.zip / SAV.zip)
    rather than CSV/ DTA/ SAV/ folders; when no person module is found at the top
    level we recurse into the nested format zips (preferring CSV, then SAV, DTA).
    """
    out = _frames_from_zip(zf)
    if out:
        return out
    inner = sorted((m for m in zf.namelist() if m.lower().endswith(".zip")),
                   key=_inner_zip_rank)
    for iz in inner:
        try:
            with zipfile.ZipFile(io.BytesIO(zf.read(iz))) as zin:
                out = _frames_from_zip(zin)
        except zipfile.BadZipFile:
            continue
        if out:
            return out
    return []


def read_tabular(zf, name):
    raw = zf.read(name)
    ln = name.lower()
    try:
        if ln.endswith((".csv", ".txt")):
            for sep in (";", ",", "\t", "|"):
                try:
                    df = pd.read_csv(io.BytesIO(raw), sep=sep, encoding="latin-1",
                                     low_memory=False, dtype=str, on_bad_lines="skip")
                    if df.shape[1] > 3:
                        return df
                except Exception:
                    continue
            return None
        if ln.endswith(".sav"):
            import pyreadstat
            with tempfile.NamedTemporaryFile(suffix=".sav", delete=False) as tf:
                tf.write(raw); tmp = tf.name
            try:
                df, _ = pyreadstat.read_sav(tmp, encoding="LATIN1")
            finally:
                os.unlink(tmp)
            return df
        if ln.endswith(".dta"):
            return pd.read_stata(io.BytesIO(raw), convert_categoricals=False)
    except Exception as e:
        print(f"      ! could not read {name}: {e}", file=sys.stderr)
    return None


def pick(cols, cands):
    low = {str(c).lower().strip(): c for c in cols}
    for cand in cands:
        if cand in low:
            return low[cand]
    return None


def accumulate(df, acc):
    cu, ca = pick(df.columns, UNION_CANDS), pick(df.columns, AGE_CANDS)
    cs, cw = pick(df.columns, SEX_CANDS),   pick(df.columns, WEIGHT_CANDS)
    if not all([cu, ca, cs, cw]):
        raise RuntimeError(f"missing cols union={cu} age={ca} sex={cs} weight={cw}; "
                           f"have={list(df.columns)[:25]}")
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
    return (cs, cw)   # report which sex/weight vars were used


def run_year(year, catalog_id, max_months=None):
    os.makedirs(CACHE, exist_ok=True)
    months = select_monthly(discover_downloads(catalog_id))
    if max_months:
        months = months[:max_months]
    print(f"  {year}: {len(months)} monthly resources selected "
          f"({', '.join(month_of(n) and n or n for n, _ in months[:3])}...)")
    acc = {band: {"total": 0.0, "cohab": 0.0, "marr": 0.0} for band, _, _ in BANDS}
    n_ok, sexvar, wvar, domains_seen = 0, set(), set(), set()
    for name, url in months:
        safe = re.sub(r"[^A-Za-z0-9_.-]", "_", name) or url.split("/")[-1]
        fn = os.path.join(CACHE, f"{year}_{safe}")
        if not fn.lower().endswith((".zip", ".rar")):
            fn += ".zip"
        if not (os.path.exists(fn) and os.path.getsize(fn) > 10000):
            print(f"    downloading {name} ...")
            try:
                curl(url, out=fn)
            except Exception as e:
                print(f"    ! download failed {name}: {e}", file=sys.stderr); continue
        try:
            with zipfile.ZipFile(fn) as zf:
                frames = person_frames(zf)
                if not frames:
                    print(f"    ! no person module in {name}", file=sys.stderr); continue
                for mem, df in frames:
                    cs, cw = accumulate(df, acc)
                    sexvar.add(cs); wvar.add(cw); domains_seen.add(_domain(mem))
                n_ok += 1
                doms = "+".join(sorted({_domain(m) for m, _ in frames}))
                print(f"    ok {name}  [{len(frames)} frame(s): {doms}]")
        except zipfile.BadZipFile:
            print(f"    ! bad zip {name}", file=sys.stderr); continue
    if n_ok == 0:
        raise RuntimeError(f"{year}: no usable monthly files")
    return acc, n_ok, sorted(sexvar), sorted(wvar), sorted(domains_seen)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", nargs="*", type=int, default=sorted(CATALOGS))
    ap.add_argument("--max-months", type=int, default=None,
                    help="cap months per year (1 = single-month proxy)")
    ap.add_argument("--out", default=os.path.join(HERE, "COL_coupling_annual.csv"))
    args = ap.parse_args()

    rows = []
    print(f"{'yr':4s} {'band':6s} {'cohab%':>7s} {'marr%':>7s} {'union%':>7s} "
          f"{'n_women':>11s}  sex/weight")
    for y in args.years:
        if y not in CATALOGS:
            print(f"  {y}: no catalog id; skipping"); continue
        try:
            acc, nmo, sexv, wv, doms = run_year(y, CATALOGS[y], args.max_months)
        except Exception as e:
            print(f"  {y}: ERROR {e}", file=sys.stderr); continue
        proxy = (args.max_months == 1) or (nmo < 6)
        note = f"{'single/partial' if proxy else 'full-year'} pooled ({nmo} mo)"
        cov = "national-splice" if y in REDESIGN_YEARS else "national"
        sexw = f"sex={'/'.join(sexv)} w={'/'.join(wv)} dom={'+'.join(doms)}"
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
                           f"P6070 estado civil x P6040 edad, women {'/'.join(sexv)}=2, "
                           f"weighted {'/'.join(wv)}; pooled {nmo} mo; "
                           f"domains {'+'.join(doms)}"),
                "coverage_flag": cov,
                "note": note,
            })
            print(f"  {y} {band:6s} {ch*100:6.1f} {mr*100:6.1f} {ut*100:6.1f} "
                  f"{int(t):11d}  {sexw if band=='20-24' else ''}")
        time.sleep(0.3)
    if not rows:
        print("\nNO ROWS COMPUTED.", file=sys.stderr); sys.exit(1)
    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "age_band", "union_total", "married",
            "cohabiting", "n_women_weighted", "observed_or_interpolated", "source",
            "coverage_flag", "note"])
        w.writeheader(); w.writerows(rows)
    print(f"\nwrote {args.out}  ({len(rows)} rows, {len(rows)//4} years)")


if __name__ == "__main__":
    main()
