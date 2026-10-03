#!/usr/bin/env python3
"""NVDA watch — Nvidia's financial bets, as an EDGAR filings alarm (Aurora).

WHAT THIS IS (and is not). A filings watch on NVIDIA Corp (CIK 1045810) as a
node of the SPCX Interconnections web: GPU supplier to Colossus, SPCX holder,
and investor in SpaceX's main compute customer (Anthropic). It records what
Nvidia files and re-reads the variables that measure how far Nvidia finances
its own demand. It does NOT classify, score, or forecast; there is no price
target and no directional field. Escalation is an analyst action on the SPCX
monitor, never this tool's.

DISCIPLINE. No fabricated numbers: a variable the extractor cannot find is
recorded as null and printed "unset / manual". Every value carries its
accession number. Digests are written only when something new is filed.

USAGE.
  python3 nvda_watch.py run       # daily: poll EDGAR, write digest if new, render tracker
  python3 nvda_watch.py baseline  # one-time: mark current filings as seen and
                                  # extract the latest 13F + 10-Q as the baseline
  python3 nvda_watch.py render    # rebuild tracker.md from ledger.json
"""
import datetime as dt
import gzip
import html
import json
import re
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

CIK = "1045810"
SPCX_CUSIP = "84615Q103"
HERE = Path(__file__).resolve().parent
LEDGER = HERE / "ledger.json"
DIGESTS = HERE / "digests"
TRACKER = HERE / "tracker.md"
UA = "Dalila research hectorj.villarreal@gmail.com"

# Forms worth a digest line. Form 4 / 144 are counted, not itemised (Huang's
# 10b5-1 sales would otherwise flood the digest).
MAJOR = ("10-Q", "10-K", "8-K", "13F-HR", "SC 13D", "SC 13G", "SCHEDULE 13D",
         "SCHEDULE 13G", "S-3", "S-4", "424B", "DEF 14A", "SD")
COUNTED = ("4", "4/A", "144", "3", "5")

# 10-Q / 10-K variables (all $ millions unless noted). Each regex captures the
# CURRENT-period figure, which these filings print first. Keyed to the text of
# the 10-Q for the quarter ended 2026-07-26; if Nvidia rewords a caption the
# variable goes null and the digest says so — fix the regex, never guess.
TENQ_VARS = {
    "non_marketable_securities": r"Non-marketable securities \$? ?([\d,]+)",
    "non_marketable_equity_end": r"Balance at end of period \$ ([\d,]+)",
    "marketable_equity_securities": r"Marketable equity securities \$? ?([\d,]+)",
    "accounts_receivable": r"Accounts receivable, net \$? ?([\d,]+)",
    "inventories": r"Inventories \$? ?([\d,]+) \$? ?[\d,]+ Prepaid",
    "gains_equity_securities_ytd": r"Gains from equity securities, net \( ?([\d,]+) ?\)",
    "lps_guarantees_ai_clouds": r"Land, power, and shell guarantees for AI clouds \(1\) \$ ([\d,]+)",
    "public_company_warrants": r"Public company warrants \$ ([\d,]+)",
    "equity_method_infra_financiers_bn": r"\$ ([\d.]+) billion of investments in infrastructure financiers",
}
# "Future commitments by fiscal year" table ($ billions): the row TOTAL is the
# last of its seven cells (five fiscal years, "thereafter", total).
COMMIT_ROWS = ("Supply and capacity", "Cloud service agreements",
               "Data center leases not commenced", "Equity investments",
               "Capital expenditures", "Total")
TENQ_SENTENCES = {
    "capped_guarantees": r"[^.]*capped at a total of \$ ?[\d.]+ billion[^.]*\.",
    "direct_customer_concentration": r"For the (?:second|third|fourth|first) quarter of fiscal year \d{4}, [^.]*direct customers? represented[^.]*\.",
    "infra_financiers": r"[^.]*infrastructure financiers[^.]*\.",
}


def get(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    return data if binary else data.decode("utf-8", errors="ignore")


def text_of(htm):
    t = re.sub(r"<[^>]+>", " ", htm)
    return re.sub(r"\s+", " ", html.unescape(t))


def load_ledger():
    if LEDGER.exists():
        return json.loads(LEDGER.read_text())
    return {"seen": [], "holdings": {}, "tenq": {}, "counted": {}, "last_poll": None}


def save_ledger(L):
    LEDGER.write_text(json.dumps(L, indent=2, ensure_ascii=False) + "\n")


def filings():
    """Recent filings from the issuer submissions feed, newest first."""
    r = json.loads(get(f"https://data.sec.gov/submissions/CIK{CIK.zfill(10)}.json"))["filings"]["recent"]
    keys = ("accessionNumber", "filingDate", "reportDate", "form", "primaryDocument", "items")
    return [dict(zip(keys, row)) for row in zip(*(r[k] for k in keys))]


def folder(acc):
    return f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}"


def parse_13f(acc):
    idx = json.loads(get(folder(acc) + "/index.json"))["directory"]["item"]
    name = next(i["name"] for i in idx if i["name"].endswith(".xml") and "primary" not in i["name"])
    root = ET.fromstring(get(f"{folder(acc)}/{name}", binary=True))
    ns = re.match(r"\{.*\}", root.tag).group(0)
    out = {}
    for t in root.findall(ns + "infoTable"):
        g = lambda p: t.find(".//" + ns + p).text.strip()
        out[g("cusip")] = {"issuer": g("nameOfIssuer"), "shares": int(g("sshPrnamt")),
                           "value_usd": int(g("value"))}
    return out


def parse_tenq(f):
    t = text_of(get(f"{folder(f['accessionNumber'])}/{f['primaryDocument']}"))
    vals = {}
    for k, rx in TENQ_VARS.items():
        m = re.search(rx, t)
        vals[k] = float(m.group(1).replace(",", "")) if m else None
    i = t.find("Future commitments by fiscal year")
    table = t[i:i + 1200] if i >= 0 else ""
    cell = r"\$? ?(?:[\d,]+|—)"
    for row in COMMIT_ROWS:
        m = re.search(re.escape(row) + r" ((?:" + cell + r" ){6}" + cell + r")", table)
        last = m.group(1).split()[-1].replace(",", "") if m else None
        vals["commit_" + row.lower().replace(" ", "_") + "_bn"] = (
            float(last) if last and last != "—" else (0.0 if last == "—" else None))
    sents = {}
    for k, rx in TENQ_SENTENCES.items():
        ms = [m.group(0).strip() for m in re.finditer(rx, t)]
        sents[k] = list(dict.fromkeys(ms))[:3] or None
    sents["mentions"] = {w: len(re.findall(w, t)) for w in ("OpenAI", "Anthropic", "xAI", "SpaceX", "CoreWeave")}
    return {"period": f["reportDate"], "form": f["form"], "acc": f["accessionNumber"],
            "filed": f["filingDate"], "vars": vals, "text": sents}


def diff_holdings(prev, cur):
    lines = []
    for cusip in sorted(set(prev) | set(cur), key=lambda c: -(cur.get(c) or prev.get(c))["value_usd"]):
        p, c = prev.get(cusip), cur.get(cusip)
        name = (c or p)["issuer"]
        tag = " **[SPCX]**" if cusip == SPCX_CUSIP else ""
        if p and not c:
            lines.append(f"- EXITED {name}{tag}: was {p['shares']:,} sh")
        elif c and not p:
            lines.append(f"- NEW {name}{tag}: {c['shares']:,} sh, ${c['value_usd']/1e9:.2f}B")
        elif c["shares"] != p["shares"]:
            d = c["shares"] - p["shares"]
            lines.append(f"- CHANGED {name}{tag}: {p['shares']:,} -> {c['shares']:,} sh ({d:+,}), ${c['value_usd']/1e9:.2f}B")
        else:
            lines.append(f"- unchanged {name}{tag}: {c['shares']:,} sh, ${c['value_usd']/1e9:.2f}B")
    return lines


def fmt(v, k):
    if v is None:
        return "unset / manual"
    return f"${v:.1f}B" if k.endswith("_bn") else f"${v:,.0f}M"


def tenq_lines(cur, prev):
    out = [f"{cur['form']} for period {cur['period']} (filed {cur['filed']}, acc. {cur['acc']}):"]
    for k, v in cur["vars"].items():
        pv = prev["vars"].get(k) if prev else None
        delta = f" (prior {fmt(pv, k)})" if prev else ""
        out.append(f"- {k}: {fmt(v, k)}{delta}")
    for k, ss in cur["text"].items():
        if k == "mentions":
            out.append(f"- mentions: {ss}")
        else:
            for s in ss or ["unset / manual (sentence not found)"]:
                out.append(f"- {k}: \"{s[:600]}\"")
    return out


def notify(msg):
    try:
        subprocess.run(["notify-send", "-a", "NVDA watch", "NVDA watch", msg], timeout=10, check=False)
    except Exception:
        pass


def process(L, f, notes):
    form, acc = f["form"], f["accessionNumber"]
    if form.startswith("13F-HR"):
        cur = parse_13f(acc)
        prev = L["holdings"].get("positions", {})
        notes.append(f"### 13F-HR, period {f['reportDate']} (acc. {acc})")
        notes += diff_holdings(prev, cur) if prev else [f"- baseline: {len(cur)} positions"]
        L["holdings"] = {"period": f["reportDate"], "acc": acc, "positions": cur}
        s = cur.get(SPCX_CUSIP)
        if prev and (s or {}).get("shares") != (prev.get(SPCX_CUSIP) or {}).get("shares"):
            notify(f"Nvidia 13F {f['reportDate']}: SPCX position changed -> {(s or {}).get('shares', 0):,} sh")
    elif form in ("10-Q", "10-K"):
        cur = parse_tenq(f)
        notes.append(f"### {form}, period {f['reportDate']}")
        notes += tenq_lines(cur, L["tenq"] or None)
        L["tenq"] = cur
        notify(f"Nvidia {form} filed ({f['reportDate']}) — digest written")
    else:
        extra = f" items {f['items']}" if f.get("items") else ""
        notes.append(f"- {f['filingDate']} {form}{extra} — {folder(acc)}/{f['primaryDocument']}")
        if form.startswith(("SC 13", "SCHEDULE 13", "8-K")):
            notify(f"Nvidia filed {form}{extra}")


def run(baseline=False):
    L = load_ledger()
    seen = set(L["seen"])
    fs = filings()
    new = [f for f in fs if f["accessionNumber"] not in seen]
    today = dt.date.today().isoformat()
    notes, counted = [], {}
    if baseline:
        # Mark everything seen; extract only the latest 13F and 10-Q/10-K.
        for form_prefix in ("13F-HR", ("10-Q", "10-K")):
            f = next(x for x in fs if x["form"].startswith(form_prefix))
            process(L, f, notes)
        L["seen"] = [f["accessionNumber"] for f in fs]
    else:
        for f in reversed(new):  # oldest first
            if f["form"] in COUNTED:
                counted[f["form"]] = counted.get(f["form"], 0) + 1
            elif f["form"].startswith(MAJOR):
                process(L, f, notes)
            L["seen"].append(f["accessionNumber"])
    for k, v in counted.items():
        L["counted"][k] = L["counted"].get(k, 0) + v
    L["last_poll"] = dt.datetime.now().isoformat(timespec="seconds")
    if notes or counted:
        DIGESTS.mkdir(exist_ok=True)
        body = [f"# NVDA watch digest {today}", "",
                "_Alarm, not a classification. Values are as extracted from EDGAR; "
                "'unset / manual' means the extractor did not find it._", ""] + notes
        if counted:
            body += ["", "Section 16 / 144 paper (counted, not itemised): " +
                     ", ".join(f"{k}: {v}" for k, v in counted.items())]
        p = DIGESTS / f"{today}.md"
        mode = "a" if p.exists() else "w"
        with p.open(mode) as fh:
            fh.write("\n".join(body) + "\n")
        print(f"digest -> {p}")
    else:
        print("no new Nvidia filings")
    save_ledger(L)
    render(L)


def render(L=None):
    L = L or load_ledger()
    h, q = L.get("holdings") or {}, L.get("tenq") or {}
    out = ["# NVDA watch — tracker", "",
           "_Generated by `nvda_watch.py render` — do not edit by hand. "
           "Alarm only; analyst readings live in the SPCX monitor state._", "",
           f"Last poll: {L.get('last_poll')}", ""]
    if h:
        out += [f"## 13F holdings, period {h['period']} (acc. {h['acc']})", "",
                "| Issuer | CUSIP | Shares | Value |", "| --- | --- | ---: | ---: |"]
        for c, p in sorted(h["positions"].items(), key=lambda kv: -kv[1]["value_usd"]):
            name = f"**{p['issuer']}**" if c == SPCX_CUSIP else p["issuer"]
            out.append(f"| {name} | {c} | {p['shares']:,} | ${p['value_usd']/1e9:.2f}B |")
        out.append("")
    if q:
        out += [f"## Latest {q['form']}, period {q['period']} (acc. {q['acc']})", ""]
        out += tenq_lines(q, None)[1:]
        out.append("")
    if L.get("counted"):
        out += ["## Section 16 / 144 paper since baseline", "",
                ", ".join(f"{k}: {v}" for k, v in L["counted"].items()), ""]
    TRACKER.write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "run"
    {"run": lambda: run(False), "baseline": lambda: run(True), "render": render}[cmd]()
