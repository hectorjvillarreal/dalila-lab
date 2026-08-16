#!/usr/bin/env python
"""Pharma back-office ratio panel — deliberately crude, and meant to stay that way.

Build instruction: 20260816_AURORA_BUILD_pharma-ratio-panel_v1.0 (pharma_board/).
Companion doc: PANEL.md.

Standard ratios over the human-supplied roster, each expressed twice — against
the roster cross-sectional median and against the firm's own trailing band of
annual vintages. Deviations only; no composite, no verdict, no forecast.

Boundary: roster.md is human-owned (read allowed, write refused). readings.md
has NO tool access at all — neither read nor write; the panel must not
condition on prior readings. NA is not zero and is excluded from every median.
"""

import os
import re
import csv
import sys
import time
import datetime
import statistics

import yaml

RATIOS_DIR = os.path.realpath(
    os.environ.get("PHARMA_RATIOS_DIR", os.path.dirname(os.path.abspath(__file__)))
)
NO_ACCESS = {"readings.md"}   # no read, no write, ever
NO_WRITE = {"roster.md"}      # read-only to the tool
CURRENT_YEAR = None           # set at runtime from the retrieval date

WARNING = """\
**Two distortions that make these ratios lie in pharma** (printed in every
report by construction; both bite hard in this industry).

**Trailing earnings overstate durable earnings near a patent cliff.** A firm two
years from a major loss of exclusivity has earnings that are scheduled to fall.
Its low P/E is not cheapness — it is the market pricing a known extinction. This
is the single most common way a pharma ratio screen misleads, and it will
misfire in exactly the cases the Aurora board cares most about.

**R&D is expensed, not capitalised.** Book value, margins, and ROIC are
therefore not comparable across firms with different R&D intensity. A
research-heavy firm looks less profitable and less asset-rich than a scale
player running the same economics. Do not compare P/B across firms whose
R&D/sales differ by more than roughly half.

The `years_to_major_LOE` column beside the valuation ratios is human-supplied
in roster.md, not estimated by the tool. It is a column, not a model. Its only
job is to sit next to the P/E so the cliff is visible at the moment the P/E is
read. Values still marked `?` in roster.md are unverified approximations."""


class BoundaryError(Exception):
    pass


# ---------------------------------------------------------------- file layer

def _guard(relpath, mode):
    rp = os.path.realpath(os.path.join(RATIOS_DIR, relpath))
    base = os.path.basename(rp)
    if base in NO_ACCESS:
        raise BoundaryError(f"refused: {base} is off-limits to the tool in every mode")
    if not (rp == RATIOS_DIR or rp.startswith(RATIOS_DIR + os.sep)):
        raise BoundaryError(f"refused: {relpath} resolves outside the ratios directory")
    if any(c in mode for c in "wxa+"):
        if base in NO_WRITE:
            raise BoundaryError(f"refused: {base} is human-owned (read-only to the tool)")
        parent = os.path.basename(os.path.dirname(rp))
        if parent in ("history", "_reports") and "x" not in mode:
            raise BoundaryError(f"refused: {parent}/ is append-only (create-new only)")
    return rp


def guarded_open(relpath, mode):
    return open(_guard(relpath, mode), mode)


# ---------------------------------------------------------------- roster

def parse_roster():
    """Rows like: | 1 | `LLY` | Eli Lilly | 2033? | why |. The tool never adds
    a firm; the roster is whatever Héctor put in it."""
    with guarded_open("roster.md", "r") as f:
        text = f.read()
    roster = []
    for line in text.splitlines():
        m = re.match(r"\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|", line)
        if m:
            roster.append({"ticker": m.group(1), "firm": m.group(2), "loe_major": m.group(3)})
    return roster


def years_to_loe(loe, year):
    """Arithmetic on the human-supplied date only. Blank/n-a stays as-is;
    a `?` (unverified in roster.md) is carried through, never resolved."""
    loe = (loe or "").strip()
    if not loe or loe.lower() == "n/a":
        return loe or ""
    m = re.match(r"(\d{4})(\?)?", loe)
    if not m:
        return loe
    return f"{int(m.group(1)) - year}{m.group(2) or ''}"


# ---------------------------------------------------------------- retrieval

INC_ITEMS = {
    "revenue": ["Total Revenue", "Operating Revenue"],
    "gross_profit": ["Gross Profit"],
    "op_income": ["Operating Income", "Total Operating Income As Reported"],
    "net_income": ["Net Income", "Net Income Common Stockholders"],
    "ebitda": ["EBITDA", "Normalized EBITDA"],
    "ebit": ["EBIT", "Operating Income"],
    "interest_exp": ["Interest Expense"],
    "rnd": ["Research And Development"],
    "tax_provision": ["Tax Provision"],
    "pretax_income": ["Pretax Income"],
    "eps_diluted": ["Diluted EPS"],
}
BS_ITEMS = {
    "equity": ["Stockholders Equity", "Common Stock Equity"],
    "total_debt": ["Total Debt"],
    "cash": ["Cash Cash Equivalents And Short Term Investments", "Cash And Cash Equivalents"],
    "cur_assets": ["Current Assets"],
    "cur_liab": ["Current Liabilities"],
    "shares": ["Ordinary Shares Number", "Share Issued"],
}
CF_ITEMS = {
    "ocf": ["Operating Cash Flow"],
    "capex": ["Capital Expenditure"],
    "dividends_paid": ["Cash Dividends Paid", "Common Stock Dividend Paid"],
}


def _rows(df, spec):
    """{key: {year: value}} for the first matching row label per key."""
    out, src = {}, {}
    for key, names in spec.items():
        for name in names:
            if df is not None and name in df.index:
                s = df.loc[name]
                if hasattr(s, "iloc") and getattr(s, "ndim", 1) > 1:
                    s = s.iloc[0]
                vals = {}
                for col, v in s.items():
                    try:
                        fv = float(v)
                        if fv == fv:  # not NaN
                            vals[col.year] = fv
                    except (TypeError, ValueError):
                        pass
                if vals:
                    out[key], src[key] = vals, name
                    break
        out.setdefault(key, {})
        src.setdefault(key, None)
    return out, src


def fetch(ticker):
    import yfinance as yf
    t = yf.Ticker(ticker)
    raw = {"ticker": ticker, "retrieved_at": datetime.datetime.now().isoformat(timespec="seconds")}
    inc, src_i = _rows(t.income_stmt, INC_ITEMS)
    bs, src_b = _rows(t.balance_sheet, BS_ITEMS)
    cf, src_c = _rows(t.cashflow, CF_ITEMS)
    raw["fundamentals"] = {**inc, **bs, **cf}
    raw["source_fields"] = {**src_i, **src_b, **src_c}
    info = t.info or {}
    raw["info"] = {k: info.get(k) for k in
                   ["trailingPE", "forwardPE", "priceToBook", "enterpriseToEbitda",
                    "enterpriseToRevenue", "enterpriseValue", "marketCap",
                    "currency", "financialCurrency", "currentPrice"]}
    h = t.history(period="6y", auto_adjust=False)
    if not any(raw["fundamentals"][k] for k in raw["fundamentals"]) and not len(h):
        raise RuntimeError("no data returned for symbol (invalid, delisted, or renamed ticker?)")
    raw["last_close"] = float(h["Close"].iloc[-1]) if len(h) else None
    if len(h):
        cutoff = h.index[-1] - datetime.timedelta(days=365)
        raw["div_ttm"] = float(h.loc[h.index >= cutoff, "Dividends"].sum())
    else:
        raw["div_ttm"] = None
    raw["yearend_close"] = {}
    for y in bs.get("equity", {}):
        upto = h.loc[:f"{y}-12-31"]
        if len(upto):
            raw["yearend_close"][y] = float(upto["Close"].iloc[-1])
    return raw


# ---------------------------------------------------------------- ratios

def _series_ratio(f, num, den, transform=lambda a, b: a / b):
    out = {}
    for y in sorted(set(f[num]) & set(f[den]), reverse=True):
        try:
            if f[den][y]:
                out[y] = transform(f[num][y], f[den][y])
        except ZeroDivisionError:
            pass
    return out


def compute_ratios(raw):
    """Each ratio -> {current, band, source, na_reason}. band = historical
    annual values excluding the year the current value belongs to."""
    f = raw["fundamentals"]
    info = raw["info"]
    cur_mismatch = (info.get("currency") and info.get("financialCurrency")
                    and info["currency"] != info["financialCurrency"])
    out = {}

    def fundamental(name, series, source):
        years = sorted(series, reverse=True)
        if not years:
            out[name] = {"current": None, "band": [], "source": source,
                         "na_reason": "inputs missing from source statements"}
        else:
            out[name] = {"current": series[years[0]], "band": [series[y] for y in years[1:]],
                         "source": source, "na_reason": None}

    # profitability
    fundamental("gross_margin", _series_ratio(f, "gross_profit", "revenue"),
                "computed: Gross Profit / Total Revenue")
    fundamental("operating_margin", _series_ratio(f, "op_income", "revenue"),
                "computed: Operating Income / Total Revenue")
    fundamental("net_margin", _series_ratio(f, "net_income", "revenue"),
                "computed: Net Income / Total Revenue")
    fundamental("roe", _series_ratio(f, "net_income", "equity"),
                "computed: Net Income / Stockholders Equity")
    roic = {}
    for y in f["ebit"]:
        cap = f["total_debt"].get(y, 0) + f["equity"].get(y, 0)
        if cap and y in f["tax_provision"] and f["pretax_income"].get(y):
            tax = min(max(f["tax_provision"][y] / f["pretax_income"][y], 0.0), 0.5)
            roic[y] = f["ebit"][y] * (1 - tax) / cap
    fundamental("roic", roic, "computed: EBIT*(1-effective tax) / (Total Debt + Equity)")

    # leverage and liquidity
    nde = {}
    for y in f["ebitda"]:
        if f["ebitda"][y]:
            nde[y] = (f["total_debt"].get(y, 0) - f["cash"].get(y, 0)) / f["ebitda"][y]
    fundamental("net_debt_ebitda", nde, "computed: (Total Debt - Cash) / EBITDA")
    fundamental("interest_coverage",
                _series_ratio(f, "ebit", "interest_exp", lambda a, b: a / abs(b)),
                "computed: EBIT / |Interest Expense|")
    fundamental("current_ratio", _series_ratio(f, "cur_assets", "cur_liab"),
                "computed: Current Assets / Current Liabilities")

    # intensity
    fundamental("rnd_sales", _series_ratio(f, "rnd", "revenue"),
                "computed: Research And Development / Total Revenue")
    fundamental("capex_sales", _series_ratio(f, "capex", "revenue", lambda a, b: abs(a) / b),
                "computed: |Capital Expenditure| / Total Revenue")
    fcf = {y: f["ocf"][y] + f["capex"].get(y, 0) for y in f["ocf"]}
    conv = {y: fcf[y] / f["net_income"][y] for y in fcf
            if f["net_income"].get(y) and f["net_income"][y] > 0}
    fundamental("fcf_conversion", conv, "computed: (OCF + Capital Expenditure) / Net Income; NA when net income <= 0")
    if not conv and f["ocf"]:
        out["fcf_conversion"]["na_reason"] = "net income non-positive in all years"

    # growth (3y CAGR needs y and y-3 both present)
    def cagr3(series, positive_only=True):
        vals = {}
        for y in series:
            if (y - 3) in series and series[y - 3] and series[y] is not None:
                if positive_only and (series[y] <= 0 or series[y - 3] <= 0):
                    continue
                vals[y] = (series[y] / series[y - 3]) ** (1 / 3) - 1
        return vals
    fundamental("revenue_cagr_3y", cagr3(f["revenue"]), "computed: (rev_t / rev_t-3)^(1/3) - 1")
    fundamental("eps_growth_3y", cagr3(f["eps_diluted"]), "computed: (dilutedEPS_t / _t-3)^(1/3) - 1; NA when either <= 0")

    # valuation — current from Yahoo info fields; band reconstructed from
    # year-end close x shares vs statements, only when currencies match
    mcap_hist = {}
    if not cur_mismatch:
        for y, px in raw["yearend_close"].items():
            if f["shares"].get(y):
                mcap_hist[y] = px * f["shares"][y]

    # Yahoo's EV- and book-based fields mix price currency with statement
    # currency for ADR/cross-listed firms; wrong is worse than NA.
    MISMATCH_UNRELIABLE = {"enterpriseToEbitda", "enterpriseToRevenue", "priceToBook"}

    def valuation(name, info_key, band_fn, source):
        cur = info.get(info_key)
        mismatch_bad = cur_mismatch and info_key in MISMATCH_UNRELIABLE
        if mismatch_bad:
            cur = None
        band = []
        for y in sorted(mcap_hist, reverse=True)[1:]:  # exclude latest fiscal year
            try:
                v = band_fn(y, mcap_hist[y])
                if v is not None:
                    band.append(v)
            except (ZeroDivisionError, KeyError, TypeError):
                pass
        reason = None
        if mismatch_bad:
            reason = "price/statement currency mismatch (ADR); Yahoo EV/book fields unreliable"
        elif cur is None:
            reason = f"Yahoo field {info_key} absent"
        out[name] = {"current": cur, "band": band, "source": f"info.{info_key}; band {source}",
                     "na_reason": reason,
                     "band_na_reason": "price/statement currency mismatch (ADR)" if cur_mismatch else None}

    def ev(y, mc):
        return mc + f["total_debt"].get(y, 0) - f["cash"].get(y, 0)

    valuation("pe_trailing", "trailingPE",
              lambda y, mc: mc / f["net_income"][y] if f["net_income"].get(y, 0) > 0 else None,
              "mcap/Net Income")
    out["pe_forward"] = {"current": info.get("forwardPE"), "band": [],
                         "source": "info.forwardPE", "na_reason": None if info.get("forwardPE") is not None else "Yahoo field forwardPE absent",
                         "band_na_reason": "no historical forward estimates exist"}
    valuation("ev_ebitda", "enterpriseToEbitda",
              lambda y, mc: ev(y, mc) / f["ebitda"][y] if f["ebitda"].get(y) else None, "EV/EBITDA")
    valuation("ev_sales", "enterpriseToRevenue",
              lambda y, mc: ev(y, mc) / f["revenue"][y] if f["revenue"].get(y) else None, "EV/Sales")
    valuation("price_book", "priceToBook",
              lambda y, mc: mc / f["equity"][y] if f["equity"].get(y, 0) > 0 else None, "mcap/Equity")

    # EV/FCF and dividend yield: fully computed
    evfcf_cur = None
    evfcf_reason = None
    years = sorted(fcf, reverse=True)
    if cur_mismatch:
        evfcf_reason = "price/statement currency mismatch (ADR)"
    elif not info.get("enterpriseValue"):
        evfcf_reason = "Yahoo field enterpriseValue absent"
    elif not years or fcf[years[0]] <= 0:
        evfcf_reason = "free cash flow non-positive or missing"
    else:
        evfcf_cur = info["enterpriseValue"] / fcf[years[0]]
    out["ev_fcf"] = {"current": evfcf_cur,
                     "band": [ev(y, mcap_hist[y]) / fcf[y] for y in sorted(mcap_hist, reverse=True)[1:]
                              if fcf.get(y, 0) > 0],
                     "source": "computed: info.enterpriseValue / (OCF + Capital Expenditure)",
                     "na_reason": evfcf_reason}
    dy_cur = None
    if raw.get("div_ttm") is not None and raw.get("last_close"):
        dy_cur = raw["div_ttm"] / raw["last_close"]
    out["dividend_yield"] = {
        "current": dy_cur if dy_cur else None,
        "band": [abs(f["dividends_paid"][y]) / mcap_hist[y] for y in sorted(mcap_hist, reverse=True)[1:]
                 if f["dividends_paid"].get(y)],
        "source": "computed: trailing-365d dividends / last close; band |Cash Dividends Paid|/mcap",
        "na_reason": None if dy_cur else "no dividend"}
    return out


RATIO_ORDER = ["pe_trailing", "pe_forward", "ev_ebitda", "ev_sales", "ev_fcf",
               "price_book", "dividend_yield",
               "gross_margin", "operating_margin", "net_margin", "roe", "roic",
               "net_debt_ebitda", "interest_coverage", "current_ratio",
               "rnd_sales", "capex_sales", "fcf_conversion",
               "revenue_cagr_3y", "eps_growth_3y"]


# ---------------------------------------------------------------- comparisons

def median_ex_na(values):
    """The one rule that matters: NA is not zero. Median over defined values
    only; None when fewer than two are defined."""
    defined = [v for v in values if v is not None]
    return statistics.median(defined) if len(defined) >= 2 else None


def build_panel(all_ratios):
    medians = {r: median_ex_na([all_ratios[t][r]["current"] for t in all_ratios])
               for r in RATIO_ORDER}
    panel = {}
    for t, ratios in all_ratios.items():
        row = {}
        for r in RATIO_ORDER:
            cur, band = ratios[r]["current"], ratios[r]["band"]
            xs = None
            if cur is not None and medians[r] not in (None, 0):
                xs = (cur - medians[r]) / abs(medians[r]) * 100
            z = sd = None
            if cur is not None and len(band) >= 3:
                sd = statistics.pstdev(band)
                if sd > 0:
                    z = (cur - statistics.median(band)) / sd
            row[r] = {"value": cur, "xs_dev_pct": xs, "oh_z": z, "oh_std": sd,
                      "oh_n": len(band)}
        panel[t] = row
    return panel, medians


# ---------------------------------------------------------------- restatements

def detect_restatements(raws):
    """Compare this fetch's statement values to the most recent raw vintage.
    Both vintages stay in history/ — restatements are informative."""
    prior_files = sorted(f for f in os.listdir(os.path.join(RATIOS_DIR, "history"))
                         if f.endswith("_raw.yaml"))
    if not prior_files:
        return [], None
    with guarded_open(f"history/{prior_files[-1]}", "r") as fh:
        prior = yaml.safe_load(fh)
    prior_by_ticker = {p["ticker"]: p for p in prior}
    diffs = []
    for raw in raws:
        old = prior_by_ticker.get(raw["ticker"])
        if not old:
            continue
        for item, series in raw["fundamentals"].items():
            for y, v in series.items():
                ov = old.get("fundamentals", {}).get(item, {}).get(y)
                if ov is not None and v is not None and ov != 0 and abs(v - ov) / abs(ov) > 0.005:
                    diffs.append(f"{raw['ticker']} {item} FY{y}: {ov:.6g} -> {v:.6g}")
    return diffs, prior_files[-1]


# ---------------------------------------------------------------- output

def write_outputs(roster, panel, all_ratios, raws, failures):
    now = datetime.datetime.now()
    stamp = f"{now:%Y%m%d_%H%M}"
    header = ["ticker", "loe_major", "years_to_major_LOE"]
    for r in RATIO_ORDER:
        header += [r, f"{r}_xs_dev_pct", f"{r}_oh_z", f"{r}_oh_std", f"{r}_oh_n"]
    rows = []
    for firm in roster:
        t = firm["ticker"]
        row = [t, firm["loe_major"], years_to_loe(firm["loe_major"], now.year)]
        for r in RATIO_ORDER:
            cell = panel.get(t, {}).get(r, {})
            for k in ("value", "xs_dev_pct", "oh_z", "oh_std"):
                v = cell.get(k)
                row.append("NA" if v is None else f"{v:.4f}")
            row.append(cell.get("oh_n", "NA"))
        rows.append(row)
    with guarded_open("panel.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    with guarded_open(f"history/{stamp}_panel.csv", "x") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    with guarded_open(f"history/{stamp}_raw.yaml", "x") as f:
        yaml.safe_dump(raws, f, sort_keys=False, allow_unicode=True, width=120)

    restatements, prior_vintage = detect_restatements(raws)

    # NA inventory, grouped per ratio
    na_lines = []
    for r in RATIO_ORDER:
        nas = []
        for t in panel:
            if panel[t][r]["value"] is None:
                reason = all_ratios[t][r].get("na_reason") or "undefined for this firm"
                nas.append(f"{t} ({reason})")
        if nas:
            na_lines.append(f"- {r}: {'; '.join(nas)}")
    notable = [f"- {t}: {r} (own-history |z| >= 2, window std {panel[t][r]['oh_std']:.3g}, n={panel[t][r]['oh_n']})"
               for t in panel for r in RATIO_ORDER
               if panel[t][r]["oh_z"] is not None and abs(panel[t][r]["oh_z"]) >= 2]

    lines = [
        f"# Ratio panel report — {now:%Y-%m-%d %H:%M}",
        "",
        "Machine-authored by panel.py. Deviations only; no composite, no verdict.",
        "",
        f"## Roster ({len(roster)} firms)",
        "",
        ", ".join(f"`{x['ticker']}`" for x in roster),
        "",
    ]
    if len(roster) < 8:
        lines += ["**Roster below eight firms — the cross-sectional median is close to "
                  "meaningless at this size.**", ""]
    lines += [
        f"Retrieval: {min(r['retrieved_at'] for r in raws)} to {max(r['retrieved_at'] for r in raws)}, "
        "source yfinance (Yahoo Finance). Per-value source field names in "
        f"`history/{stamp}_raw.yaml`.",
        "",
        "## Warning — print in full, every report",
        "",
        WARNING,
        "",
        "## Retrieval failures",
        "",
    ]
    lines += [f"- {t}: {e}" for t, e in failures] or ["- none"]
    lines += ["", "## NA fields (excluded from medians, never zero-filled)", ""]
    lines += na_lines or ["- none"]
    lines += ["", "## Restatements since last refresh", ""]
    if prior_vintage is None:
        lines += ["- first vintage; nothing to compare against"]
    else:
        lines += ([f"- vs {prior_vintage}:"] + [f"  - {d}" for d in restatements]
                  if restatements else [f"- none vs {prior_vintage}"])
    lines += ["", "## Notable (own-history deviation beyond 2 sigma — no direction attached)", ""]
    lines += notable or ["- none"]
    lines += ["", "Own-history bands are annual statement vintages (typically 3-4 "
              "observations); z-scores over so few points are coarse by construction — "
              "read them with the printed std and n.", ""]
    with guarded_open(f"_reports/{stamp}_panel.md", "x") as f:
        f.write("\n".join(lines))
    return f"_reports/{stamp}_panel.md"


# ---------------------------------------------------------------- run

def run(tickers=None):
    roster = parse_roster()
    if tickers:
        roster = [x for x in roster if x["ticker"] in tickers]
    if len(roster) < 8:
        print(f"note: roster has {len(roster)} firms; cross-sectional median is weak below 8")
    raws, all_ratios, failures = [], {}, []
    for firm in roster:
        t = firm["ticker"]
        try:
            raw = fetch(t)
            raws.append(raw)
            all_ratios[t] = compute_ratios(raw)
            print(f"fetched {t}")
        except Exception as e:
            failures.append((t, f"{type(e).__name__}: {e}"))
            print(f"FAILED {t}: {type(e).__name__}: {e}")
        time.sleep(1.0)
    if not all_ratios:
        print("no data retrieved; aborting without writing panel")
        return
    panel, _ = build_panel(all_ratios)
    report = write_outputs(roster, panel, all_ratios, raws, failures)
    print(f"panel written: panel.csv ({len(all_ratios)} firms, {len(failures)} failures); report {report}")


# ---------------------------------------------------------------- selftests

def selftest_boundary():
    ok = True
    for target, mode, label in [
        ("roster.md", "w", "write to roster.md"),
        ("readings.md", "r", "READ readings.md"),
        ("readings.md", "w", "write readings.md"),
        ("../feed/items.yaml", "w", "write outside ratios dir"),
    ]:
        try:
            guarded_open(target, mode)
            print(f"FAIL — {label} was permitted")
            ok = False
        except (BoundaryError, FileNotFoundError) as e:
            if isinstance(e, FileNotFoundError):
                print(f"FAIL — {label} reached the filesystem")
                ok = False
            else:
                print(f"refused as required — {label}: {e}")
    print(("roster.md writable on disk — FAIL" if os.access(os.path.join(RATIOS_DIR, "roster.md"), os.W_OK)
           else "roster.md is chmod read-only on disk — confirmed"))
    return ok


def selftest_na():
    vals = [10.0, None, 12.0, None, 14.0]
    med = median_ex_na(vals)
    zero_filled = statistics.median([0 if v is None else v for v in vals])
    print(f"values {vals}: median_ex_na = {med} (correct: 12.0); "
          f"zero-filled median would be {zero_filled} — not used anywhere")
    assert med == 12.0
    assert median_ex_na([None, None, 5.0]) is None, "single defined value must not form a median"
    print("median over [None, None, 5.0] -> None (no median from one defined value)")
    print("PASS — NA excluded from medians, never zero-filled")
    return True


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "run":
        run(tickers=sys.argv[2].split(",") if len(sys.argv) > 2 else None)
    elif cmd == "selftest-boundary":
        sys.exit(0 if selftest_boundary() else 1)
    elif cmd == "selftest-na":
        sys.exit(0 if selftest_na() else 1)
    else:
        print("usage: panel.py run [T1,T2,...] | selftest-boundary | selftest-na")
