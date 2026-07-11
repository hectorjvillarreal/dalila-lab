#!/usr/bin/env python3
"""
Stage 1.5 — Argentina coupling extractor via INDEC/ECLAC REDATAM web engine.

Mirrors the Costa Rica extractor (_extract_redatam_cri.py). Drives
RpWebStats.exe/CrossTab on INDEC's REDATAM server to produce, per EPH period, a
WEIGHTED crosstab of situación conyugal (person var CH07) x 5-year age band
(recode of age CH06), filtered to women (CH04 = 2), weighted by the expansion
factor (PONDERA). Computes the share of women in a co-residential union
(unido + casado) by age band 20-24 / 25-29 / 30-34 / 35-39, married-vs-cohabiting
split preserved.

CH07 situación conyugal codes (standard EPH design): 1=unido, 2=casado,
3=separado/divorciado, 4=viudo, 5=soltero  ->  partnered (co-residential) = {1,2}.
CH04 sexo: 1=varón, 2=mujer.  CH06 edad: years (integer).

REDATAM is public (no login). Server-side tabulation: no microdata download.

>>> HARD-WON LESSONS reused from the CRI extractor <<<
  (a) curl via subprocess, NOT urllib (this RedatamX server 500s on urllib POST).
  (b) inputTitle must be ALPHANUMERIC (engine rejects '_').
  (c) parse the result table by POSITION: status label = first non-empty cell, then
      values in age order — avoids the off-by-one from a leading header age column.
  (d) introspect the actual variable codes / entity names per base from the
      dictionary (DICALL/DICPOB) rather than blindly hardcoding.

>>> ARGENTINA-SPECIFIC, confirmed via reconnaissance 2026-06-18 <<<
  HOST  = https://redatam.indec.gob.ar
  ENGINE PATH = /argbin/RpWebEngine.exe (portal) ; /argbin/RpWebStats.exe (tabs)
  BASE  = EPH_BASE_FINAL  (pooled EPH 2003q3-2014, "EPH continua"); a shorter
          alias BASE=EPH was also seen exposing DICALL.
  COVERAGE = URBAN ONLY — EPH covers 31 urban agglomerations (aglomerados).
  PERIOD  = EPH is quarterly; the pooled base is expected to carry a year var
          (ANO4) and a quarter var (TRIMESTRE). This script RESOLVES them from the
          dictionary and iterates years, picking ONE quarter per year for an annual
          point (prefer q3/q4 — the historically continuous quarters). If the base
          turns out to be single-period, resolve_period() returns ([None],None) and
          we run a single pooled tabulation labelled with the base's span.

CRITICAL: every number comes from the engine. If the engine cannot be reached or a
year fails, that year is skipped and reported — no estimation, no fabrication.

Output: data/coupling/ARG_coupling_annual.csv
Columns: year, age_band, union_total, married, cohabiting, n_women_weighted,
         observed_or_interpolated, source, coverage_flag
(union_total/married/cohabiting are SHARES, fraction 0-1, of women in that band.)
"""
import csv, os, re, time, html, subprocess

HOST = "https://redatam.indec.gob.ar"
BIN  = HOST + "/argbin/"
XTAB = BIN + "RpWebStats.exe/CrossTab?"
DICT = BIN + "RpWebStats.exe/Dictionary?"
HERE = os.path.dirname(os.path.abspath(__file__))

BASE = "EPH_BASE_FINAL"          # pooled EPH continua base on the INDEC portal

# Candidate years for the pooled EPH continua base (2003q3 onward, through 2014).
YEARS = list(range(2003, 2015))

# Target 20-39 in 5-year bands. We recode CH06 (age in years) ourselves into bands
# via RECODE in the COLUMN spec, so we don't depend on a pre-built quinquennial var.
TARGET_BANDS = ["20-24", "25-29", "30-34", "35-39"]
AGE_RECODE = ("CH06 (20-24=1, 25-29=2, 30-34=3, 35-39=4)")  # see column_spec()

# situación conyugal CH07 value labels we key on (lowercased substring match)
COHAB_LABELS   = ("unido", "unión", "union")     # 1 = unido/a (cohabiting)
MARRIED_LABELS = ("casado",)                       # 2 = casado/a (married)


def post(params):
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
    if s in ("-", "", "–"):
        return 0.0
    return float(re.sub(r"[^\d.]", "", s.replace(" ", "")))


# ---------------------------------------------------------------------------
# Dictionary introspection (lesson d): resolve entity + variable codes for this
# base instead of hardcoding. EPH variable names are stable (CH04/CH06/CH07/
# PONDERA) but the *entity prefix* (e.g. PERSONA. / POBLACIO. / MIEMBRO.) and the
# year/quarter variable names vary between REDATAM dictionary builds.
# ---------------------------------------------------------------------------
def fetch_dictionary():
    for item in ("DICALL", "DICPOB", "DICPER"):
        try:
            h = get(f"{DICT}BASE={BASE}&ITEM={item}&lang=ESP")
            if h and "<" in h:
                return h
        except Exception:
            continue
    raise RuntimeError(f"{BASE}: could not fetch dictionary (DICALL/DICPOB/DICPER)")


def resolve_var(dic_html, names, what):
    """Find the fully-qualified ENTITY.VAR for any of `names` (case-insensitive)."""
    for nm in names:
        # REDATAM dictionaries render var rows as ENTITY.CODE then a label cell.
        m = re.search(rf'([A-Za-z][A-Za-z0-9_]*\.{re.escape(nm)})\b', dic_html, re.I)
        if m:
            return m.group(1)
        # bare code (no entity prefix shown) — fall back, caller prefixes entity.
        if re.search(rf'\b{re.escape(nm)}\b', dic_html, re.I):
            return nm
    raise RuntimeError(f"{BASE}: {what} variable not found among {names}")


def resolve_person_entity(dic_html):
    for ent in ("PERSONA", "POBLACIO", "POBLACION", "MIEMBRO", "INDIVIDU", "PER"):
        if re.search(rf'\b{ent}\b', dic_html, re.I):
            return ent
    return "PERSONA"


def resolve_period(dic_html):
    """Return (year_var_or_None, quarter_var_or_None)."""
    yv = qv = None
    for cand in ("ANO4", "ANIO", "ANO", "AÑO", "YEAR"):
        if re.search(rf'[A-Za-z0-9_]*\.?{re.escape(cand)}\b', dic_html, re.I):
            yv = resolve_var(dic_html, (cand,), "year"); break
    for cand in ("TRIMESTRE", "TRIM", "QUARTER", "PERIODO"):
        if re.search(rf'[A-Za-z0-9_]*\.?{re.escape(cand)}\b', dic_html, re.I):
            qv = resolve_var(dic_html, (cand,), "quarter"); break
    return yv, qv


def column_spec(age_var):
    """RECODE of the age variable into the four target bands, as a REDATAM COLUMN.

    RedatamX CrossTab accepts an inline recode in the COLUMN expression. Exact
    grammar varies by build; we send the canonical form and the parser keys on the
    band *labels* by position, so a slightly different bin order still parses.
    """
    return (f"{age_var} RECODE (20-24=1 LABEL '20-24', 25-29=2 LABEL '25-29', "
            f"30-34=3 LABEL '30-34', 35-39=4 LABEL '35-39')")


def parse_crosstab(t):
    """Position-based parse (lesson c). Returns (cohab, married, total) dicts band->wsum."""
    tables = re.findall(r"<table.*?</table>", t, re.S | re.I)
    if not tables:
        raise RuntimeError("no <table> in result")
    big = max(tables, key=len)
    grid = []
    for r in re.findall(r"<tr.*?</tr>", big, re.S | re.I):
        cells = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", c))).strip()
                 for c in re.findall(r"<t[dh].*?</t[dh]>", r, re.S | re.I)]
        if any(cells):
            grid.append(cells)
    # header row = the one carrying the band labels
    hdr_idx = next((i for i, c in enumerate(grid)
                    if any(b in " ".join(c) for b in TARGET_BANDS)), None)
    if hdr_idx is None:
        raise RuntimeError("band header row not found")
    ages_seq = [c for c in grid[hdr_idx] if c.strip()]   # bands (+ maybe Total)
    cohab   = {b: 0.0 for b in TARGET_BANDS}
    married = {b: 0.0 for b in TARGET_BANDS}
    total   = {b: 0.0 for b in TARGET_BANDS}
    for row in grid[hdr_idx + 1:]:
        ne = [c for c in row if c.strip()]
        if len(ne) < 2:
            continue
        label = ne[0].lower()
        vals = dict(zip(ages_seq, ne[1:]))               # band label -> value string
        if any(k in label for k in COHAB_LABELS):
            tgt = cohab
        elif any(k in label for k in MARRIED_LABELS):
            tgt = married
        else:
            tgt = None
        is_total = label.startswith("total")
        for band in TARGET_BANDS:
            if band in vals:
                v = num(vals[band])
                if tgt is not None:
                    tgt[band] += v
                if is_total:
                    total[band] += v
    if sum(total.values()) == 0:
        raise RuntimeError("zero totals parsed")
    return cohab, married, total


def run_period(person_ent, cony, sex, age, weight, year_var, year, quarter_var, quarter):
    title = f"argcoupling{year if year else 'pooled'}"
    text_filter = f"{sex} = 2"
    if year_var and year is not None:
        text_filter += f" AND {year_var} = {year}"
    if quarter_var and quarter is not None:
        text_filter += f" AND {quarter_var} = {quarter}"
    params = {
        "BASE": BASE, "CODIGO": "XXUSUARIOXX", "ITEM": "DICALL",
        "LANG": "ESP", "MAIN": "WebServerMain.inl", "MODE": "RUN",
        "ROW": cony, "COLUMN": column_spec(age), "WEIGHT": weight,
        "PERCENT": "OFF", "FORMAT": "HTML",
        "TEXT_FILTER": text_filter,
        "inputTitle": title, "Submit": "Submit",   # no '_': engine rejects it
    }
    resp = post(params)
    m = re.search(r'(RpWebUtilities\.exe/Text\?LFN=[^"\']+?TYPE=TMP)', resp)
    if not m:
        raise RuntimeError(f"{year}: no result temp file in response (len {len(resp)})")
    t = get(BIN + html.unescape(m.group(1)))
    return parse_crosstab(t)


def main():
    out = os.path.join(HERE, "ARG_coupling_annual.csv")
    dic = fetch_dictionary()
    person_ent = resolve_person_entity(dic)
    def q(name_options):
        v = resolve_var(dic, name_options, "/".join(name_options))
        return v if "." in v else f"{person_ent}.{v}"
    cony   = q(("CH07",))
    sex    = q(("CH04",))
    age    = q(("CH06",))
    weight = q(("PONDERA", "PONDIH", "PONDERA_"))
    year_var, quarter_var = resolve_period(dic)
    if year_var and "." not in year_var:
        year_var = f"{person_ent}.{year_var}"
    if quarter_var and "." not in quarter_var:
        quarter_var = f"{person_ent}.{quarter_var}"

    print(f"BASE={BASE} entity={person_ent}")
    print(f"  conyugal={cony} sex={sex} age={age} weight={weight}")
    print(f"  year_var={year_var} quarter_var={quarter_var}")

    iter_years = YEARS if year_var else [None]
    prefer_q = [3, 4, 2, 1] if quarter_var else [None]

    rows_out = []
    print(f"\n{'year':6s} {'band':6s} {'cohab%':>7s} {'marr%':>7s} {'union%':>7s} {'n_women':>10s}")
    for y in iter_years:
        cohab = married = total = None
        used_q = None
        for qtr in prefer_q:
            try:
                cohab, married, total = run_period(person_ent, cony, sex, age, weight,
                                                   year_var, y, quarter_var, qtr)
                used_q = qtr
                break
            except Exception as e:
                last = e
        if total is None:
            print(f"  {y}: SKIP (no data) — {last}")
            continue
        for b in TARGET_BANDS:
            n = total[b]
            if n == 0:
                print(f"  {y} {b:6s}  band empty — skipped")
                continue
            ch, mr = cohab[b] / n, married[b] / n
            ut = ch + mr
            qlbl = f" q{used_q}" if used_q else ""
            rows_out.append({
                "year": y if y is not None else BASE,
                "age_band": b,
                "union_total": round(ut, 4), "married": round(mr, 4),
                "cohabiting": round(ch, 4), "n_women_weighted": int(round(n)),
                "observed_or_interpolated": "observed",
                "source": (f"INDEC EPH {y}{qlbl} via REDATAM RpWebStats CrossTab "
                           f"({cony} x age-band recode of {age}, women {sex}=2, "
                           f"weighted {weight})"),
                "coverage_flag": "urban (31 agglomerates)",
            })
            print(f"  {y} {b:6s} {ch*100:6.1f} {mr*100:6.1f} {ut*100:6.1f} {int(n):10d}")
        time.sleep(1.0)  # be polite

    if not rows_out:
        raise SystemExit("NO ROWS produced — engine unreachable or all periods failed. "
                         "Not writing a CSV (no fabrication).")
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "age_band", "union_total", "married",
            "cohabiting", "n_women_weighted", "observed_or_interpolated", "source",
            "coverage_flag"])
        w.writeheader(); w.writerows(rows_out)
    print(f"\nwrote {out}  ({len(rows_out)} rows)")


if __name__ == "__main__":
    main()
