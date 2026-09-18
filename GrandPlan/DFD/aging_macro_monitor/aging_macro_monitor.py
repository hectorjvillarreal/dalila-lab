#!/usr/bin/env python3
"""Aging × Macro paper monitor — local weekly alarm for new top papers.

DFD project · GrandPlan/DFD/aging_macro_monitor/ · companion doc: README.md

WHAT IT DOES. Pulls new working papers and articles from NBER, RePEc NEP lists,
arXiv (econ.GN) and OpenAlex; scores each against the interest profile in
profile.json (aging/demographic core terms required; macro terms, geography,
author and venue boosts); writes a dated digest to digests/ with ALERT and WATCH
tiers; appends a line to run_log.md; fires a desktop notification when there is
at least one alert. Every item is recorded once in state/seen.json so a paper is
never re-alerted.

WHAT IT DOES NOT DO. It never writes into the demographics corpus, the
acquisition queue, or any endorsed artifact. Digest lines are formatted to paste
into _crossrefs/corpus/demographics/_acquisition_queue.md by hand, in-session,
under the drafter's own authorship (PROTO-RAG-001). It never fabricates
metadata: a missing abstract renders as "(no abstract in feed)".

OPTIONAL LOCAL-LLM RE-RANK. If ollama is reachable at profile.ollama.url with the
named model, candidates above the watch threshold are re-scored 0–10 by the
model against the interest profile and the two scores are combined. If ollama is
absent the stage is skipped and logged; keyword ranking stands alone.

USAGE.
  python aging_macro_monitor.py run            # full cycle (fetch, score, digest, notify)
  python aging_macro_monitor.py run --dry      # score and print, no state/digest writes
  python aging_macro_monitor.py run --no-llm   # skip the ollama stage
  python aging_macro_monitor.py status         # last run, ledger size, next timer fire

Stdlib only — no third-party dependencies.
"""

import html
import json
import re
import sys
import subprocess
import time
import urllib.parse
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROFILE = ROOT / "profile.json"
STATE_DIR = ROOT / "state"
SEEN = STATE_DIR / "seen.json"
DIGESTS = ROOT / "digests"
RUN_LOG = ROOT / "run_log.md"
UA = "Mozilla/5.0 (Dalila aging-macro monitor; hectorj.villarreal@gmail.com)"
TIMEOUT = 40


# --------------------------------------------------------------------------- #
# Fetch helpers
# --------------------------------------------------------------------------- #
def get(url, retries=2):
    last = None
    for i in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return r.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
            last = e
            time.sleep(2 + 3 * i)
    raise RuntimeError(f"fetch failed {url}: {last}")


def local(tag):
    return tag.split("}", 1)[-1] if "}" in tag else tag


def strip_html(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


# --------------------------------------------------------------------------- #
# Source parsers — each yields dicts {title, authors, abstract, link, date, source, venue}
# --------------------------------------------------------------------------- #
def parse_rss_lenient(raw, source, venue):
    """Regex fallback for feeds that are not well-formed XML."""
    txt = raw.decode("utf-8", "replace")
    out = []
    for blk in re.findall(r"<item>(.*?)</item>", txt, flags=re.S):
        def g(tag):
            m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", blk, flags=re.S)
            return strip_html(re.sub(r"^<!\[CDATA\[|\]\]>$", "", (m.group(1) or "").strip())) if m else ""
        d = {"title": g("title"), "authors": [strip_html(a) for a in re.findall(r"<dc:creator>(.*?)</dc:creator>", blk, flags=re.S)],
             "abstract": g("description"), "link": g("link"), "date": g("pubDate")[:40] or g("dc:date")[:40],
             "source": source, "venue": venue, "subjects": ""}
        if d["title"]:
            out.append(d)
    return out


def parse_rss(raw, source, venue):
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return parse_rss_lenient(raw, source, venue)
    items = [el for el in root.iter() if local(el.tag) == "item"]
    out = []
    for it in items:
        d = {"title": "", "authors": [], "abstract": "", "link": "", "date": "", "source": source, "venue": venue, "subjects": ""}
        for ch in it:
            t = local(ch.tag)
            txt = (ch.text or "").strip()
            if t == "title":
                d["title"] = strip_html(txt)
            elif t == "link" and not d["link"]:
                d["link"] = txt
            elif t == "description":
                d["abstract"] = strip_html(txt)
            elif t == "creator":
                d["authors"].append(strip_html(txt))
            elif t in ("date", "pubDate") and not d["date"]:
                d["date"] = txt[:40]
            elif t == "subject":
                d["subjects"] += " " + strip_html(txt)
        if d["title"]:
            out.append(d)
    return out


def fetch_nber(cfg):
    items = parse_rss(get(cfg["sources"]["nber_new"]), "nber", "NBER Working Paper")
    for it in items:
        m = re.match(r"^(.*?)\s+--\s+by\s+(.*)$", it["title"])
        if m:
            it["title"] = m.group(1).strip()
            it["authors"] = [a.strip() for a in re.split(r",|\band\b|&", m.group(2)) if a.strip()] or it["authors"]
    return items


def fetch_nep(cfg):
    out = []
    for lst in cfg["sources"]["nep"]:
        try:
            out += parse_rss(get(f"https://nep.repec.org/rss/{lst}.rss.xml"), lst, f"RePEc {lst.upper()}")
        except Exception as e:
            log_line(f"WARN {lst}: {e}")
    return out


def fetch_arxiv(cfg):
    q = urllib.parse.quote(cfg["sources"]["arxiv_query"])
    raw = get(f"https://export.arxiv.org/api/query?search_query={q}&max_results=60&sortBy=submittedDate&sortOrder=descending")
    root = ET.fromstring(raw)
    out = []
    for e in root.iter():
        if local(e.tag) != "entry":
            continue
        d = {"title": "", "authors": [], "abstract": "", "link": "", "date": "", "source": "arxiv", "venue": "arXiv econ.GN", "subjects": ""}
        for ch in e:
            t = local(ch.tag)
            if t == "title":
                d["title"] = strip_html(ch.text)
            elif t == "summary":
                d["abstract"] = strip_html(ch.text)
            elif t == "id":
                d["link"] = (ch.text or "").strip()
            elif t == "published":
                d["date"] = (ch.text or "")[:10]
            elif t == "author":
                for n in ch:
                    if local(n.tag) == "name":
                        d["authors"].append((n.text or "").strip())
        if d["title"]:
            out.append(d)
    return out


def openalex_abstract(inv):
    if not inv:
        return ""
    pos = {}
    for w, idxs in inv.items():
        for i in idxs:
            pos[i] = w
    return " ".join(pos[i] for i in sorted(pos))


def fetch_openalex(cfg, since):
    out = []
    sel = "id,doi,title,publication_date,authorships,primary_location,cited_by_count,abstract_inverted_index,type"
    for q in cfg["sources"]["openalex_queries"]:
        url = ("https://api.openalex.org/works?filter=from_publication_date:" + since +
               ",type:article|preprint&search=" + urllib.parse.quote(q) +
               "&per-page=50&sort=publication_date:desc&select=" + sel +
               "&mailto=hectorj.villarreal@gmail.com")
        try:
            data = json.loads(get(url))
        except Exception as e:
            log_line(f"WARN openalex '{q}': {e}")
            continue
        for w in data.get("results", []):
            loc = w.get("primary_location") or {}
            src = (loc.get("source") or {}).get("display_name") or ""
            out.append({
                "title": strip_html(w.get("title") or ""),
                "authors": [a["author"]["display_name"] for a in w.get("authorships", []) if a.get("author")],
                "abstract": openalex_abstract(w.get("abstract_inverted_index")),
                "link": w.get("doi") or w.get("id") or "",
                "date": w.get("publication_date") or "",
                "source": "openalex", "venue": src or w.get("type", ""), "subjects": "",
            })
    return out


# --------------------------------------------------------------------------- #
# Scoring
# --------------------------------------------------------------------------- #
def count_hits(terms, text):
    hits = []
    low = text.lower()
    for t in terms:
        if re.search(r"(?<![a-z])" + re.escape(t.lower()) + r"(?![a-z])", low):
            hits.append(t)
    return hits


def score(item, cfg):
    title = item["title"]
    body = " ".join([item["abstract"], item.get("subjects", "")])
    core_t = count_hits(cfg["core_terms"], title)
    core_b = count_hits(cfg["core_terms"], body)
    if not core_t and not core_b:
        return None
    if count_hits(cfg.get("exclude_terms", []), title + " " + body):
        return None
    macro_t = count_hits(cfg["macro_terms"], title)
    macro_b = count_hits(cfg["macro_terms"], body)
    geo = count_hits(cfg["geography_terms"], title + " " + body)
    auth_txt = " ".join(item["authors"]).lower()
    auth = [a for a in cfg["authors"] if re.search(r"(?<!\w)" + re.escape(a.lower()) + r"(?!\w)", auth_txt)]
    venue_low = (item["venue"] or "").lower()
    venue_hit = any(v.lower() in venue_low for v in cfg["top_venues"])
    venue_bad = any(v.lower() in venue_low for v in cfg.get("low_venues", []))
    s = 0
    s += min(3 * len(core_t), 6) + min(len(core_b), 4)
    s += min(2 * len(macro_t), 4) + min(len(macro_b), 3)
    s += 3 if geo else 0
    s += 3 if auth else 0
    s += 3 if venue_hit else 0
    s += cfg["source_prior"].get(item["source"], 0)
    s -= 4 if venue_bad else 0
    # Alert gate: a paper reaches ALERT only with a macro dimension AND one quality signal
    # (known series, top venue, tracked author, or LAC geography). Otherwise it is capped at WATCH.
    weak = set(t.lower() for t in cfg.get("weak_core_terms", []))
    strong_core = [t for t in core_t + core_b if t.lower() not in weak]
    quality = item["source"] in ("nber", "nep-age", "nep-dge", "nep-dem", "nep-pbe", "nep-gro", "nep-lam", "nep-mac") \
        or venue_hit or auth or geo
    # A tracked author waives the macro-term requirement (Diamond on pension design, 2026-09-17).
    if (not (macro_t or macro_b) and not auth) or not quality or not strong_core:
        s = min(s, cfg["alert_threshold"] - 1)
    return {"score": s, "core": sorted(set(core_t + core_b))[:6], "macro": sorted(set(macro_t + macro_b))[:5],
            "geo": geo[:3], "authors_hit": auth, "venue_hit": venue_hit}


# --------------------------------------------------------------------------- #
# Optional ollama re-rank
# --------------------------------------------------------------------------- #
def ollama_available(o):
    try:
        raw = get(o["url"].rstrip("/") + "/api/tags", retries=0)
        names = [m.get("name", "") for m in json.loads(raw).get("models", [])]
        return any(n.startswith(o["model"].split(":")[0]) for n in names)
    except Exception:
        return False


def ollama_score(o, item, cfg):
    prompt = (
        "You rank research papers for an academic economist working on population aging and macroeconomics "
        "(OLG/DSGE fiscal models, pensions, fertility decline, longevity, demographic dividend, fiscal sustainability, "
        "health-system financing, Latin America and Mexico). Rate relevance 0-10 for a 'must read' alarm. "
        "Answer with a single integer only.\n\n"
        f"Title: {item['title']}\nAuthors: {', '.join(item['authors'])}\nVenue: {item['venue']}\n"
        f"Abstract: {item['abstract'][:1800]}\n"
    )
    body = json.dumps({"model": o["model"], "prompt": prompt, "stream": False, "options": {"temperature": 0}}).encode()
    req = urllib.request.Request(o["url"].rstrip("/") + "/api/generate", data=body,
                                 headers={"Content-Type": "application/json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        txt = json.loads(r.read()).get("response", "")
    m = re.search(r"\d+", txt)
    return min(int(m.group()), 10) if m else None


# --------------------------------------------------------------------------- #
# State, digest, log, notify
# --------------------------------------------------------------------------- #
def load_seen():
    if SEEN.exists():
        return json.loads(SEEN.read_text())
    return {"last_run": None, "items": {}}


def log_line(msg):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    RUN_LOG.parent.mkdir(parents=True, exist_ok=True)
    if not RUN_LOG.exists():
        RUN_LOG.write_text("# Aging × Macro monitor — run log\n\nOne line per run or warning; newest last.\n\n")
    with RUN_LOG.open("a") as f:
        f.write(f"- {stamp} — {msg}\n")
    print(msg)


def queue_line(it, today):
    auth = ", ".join(it["authors"][:3]) + (" et al." if len(it["authors"]) > 3 else "")
    ind = ", ".join(it["sc"]["core"][:3]) or "composite"
    geo = "/".join(it["sc"]["geo"]) if it["sc"]["geo"] else "WLD"
    return f"- {today} — {auth} ({it['date'][:4] or 'n.d.'}), \"{it['title']}\", {it['venue']} — {ind} — {geo} — {it['link']}"


def write_digest(today, alerts, watch, counts, llm_note):
    p = DIGESTS / f"{today}_digest.md"
    L = [f"# Aging × Macro digest — {today}", "",
         f"Sources polled: {', '.join(f'{k} {v}' for k, v in counts.items())}. "
         f"Above watch threshold: {len(alerts) + len(watch)}. {llm_note}", "",
         "Lines under each ALERT item are formatted for `_acquisition_queue.md`; paste by hand, in session, "
         "under your own `added_by`. Nothing here has touched the corpus.", "",
         f"## ALERT ({len(alerts)})", ""]
    if not alerts:
        L.append("_None this run._")
    for it in alerts:
        sc = it["sc"]
        L += [f"### {it['title']}",
              f"- **Authors:** {', '.join(it['authors']) or '(not in feed)'}",
              f"- **Where:** {it['venue']} · {it['date'] or 'n.d.'} · {it['link']}",
              f"- **Score:** {sc['score']}" + (f" (keyword {sc['kw']}, model {sc['llm']}/10)" if 'llm' in sc else "") +
              f" · core: {', '.join(sc['core'])} · macro: {', '.join(sc['macro']) or '—'}" +
              (f" · geo: {', '.join(sc['geo'])}" if sc['geo'] else "") +
              (f" · author boost: {', '.join(sc['authors_hit'])}" if sc['authors_hit'] else "") +
              (" · top venue" if sc['venue_hit'] else ""),
              f"- **Abstract:** {(it['abstract'][:700] + '…') if len(it['abstract']) > 700 else (it['abstract'] or '(no abstract in feed)')}",
              "", "```", queue_line(it, today), "```", ""]
    L += [f"## WATCH ({len(watch)})", ""]
    if not watch:
        L.append("_None this run._")
    for it in watch:
        sc = it["sc"]
        L.append(f"- [{sc['score']}] {it['title']} — {', '.join(it['authors'][:3]) or '?'} — {it['venue']} — {it['link']}")
    L.append("")
    p.write_text("\n".join(L))
    return p


def notify(title, body):
    try:
        subprocess.run(["notify-send", "-a", "Dalila", "-u", "normal", title, body], timeout=10, check=False)
    except Exception:
        pass


# --------------------------------------------------------------------------- #
# Main cycle
# --------------------------------------------------------------------------- #
def run(dry=False, use_llm=True):
    cfg = json.loads(PROFILE.read_text())
    seen = load_seen()
    today = date.today().isoformat()
    since = (date.fromisoformat(seen["last_run"]) - timedelta(days=3)).isoformat() if seen["last_run"] \
        else (date.today() - timedelta(days=cfg["lookback_days_first_run"])).isoformat()

    fetched, counts = [], {}
    for name, fn in [("nber", lambda: fetch_nber(cfg)), ("nep", lambda: fetch_nep(cfg)),
                     ("arxiv", lambda: fetch_arxiv(cfg)), ("openalex", lambda: fetch_openalex(cfg, since))]:
        try:
            items = fn()
        except Exception as e:
            log_line(f"WARN {name}: {e}")
            items = []
        counts[name] = len(items)
        fetched += items

    # Dedupe within run (by normalised title), then against ledger
    cand, keys = [], set()
    for it in fetched:
        it["authors"] = [a.strip(" ,;") for a in it["authors"] if a and a.strip(" ,;")]
        k = norm_title(it["title"])
        if not k or k in keys:
            continue
        keys.add(k)
        if k in seen["items"]:
            continue
        sc = score(it, cfg)
        if sc is None:
            seen["items"][k] = {"first_seen": today, "tier": "drop", "src": it["source"]}
            continue
        it["sc"] = sc
        cand.append(it)

    # Optional LLM re-rank on the keyword-eligible set above watch threshold
    o = cfg.get("ollama", {})
    llm_note = "LLM re-rank: skipped (disabled)."
    if use_llm and o.get("enabled"):
        if ollama_available(o):
            pool = sorted([c for c in cand if c["sc"]["score"] >= cfg["watch_threshold"]],
                          key=lambda c: -c["sc"]["score"])[:o.get("max_candidates", 25)]
            n = 0
            for c in pool:
                try:
                    v = ollama_score(o, c, cfg)
                except Exception as e:
                    log_line(f"WARN ollama on '{c['title'][:50]}': {e}")
                    continue
                if v is not None:
                    c["sc"]["kw"] = c["sc"]["score"]
                    c["sc"]["llm"] = v
                    c["sc"]["score"] = round(0.5 * c["sc"]["score"] + 1.2 * v)
                    n += 1
            llm_note = f"LLM re-rank: {o['model']} scored {n} candidates (combined = 0.5·keyword + 1.2·model)."
        else:
            llm_note = f"LLM re-rank: skipped ({o.get('model')} not reachable at {o.get('url')})."

    cand.sort(key=lambda c: -c["sc"]["score"])
    alerts = [c for c in cand if c["sc"]["score"] >= cfg["alert_threshold"]]
    watch = [c for c in cand if cfg["watch_threshold"] <= c["sc"]["score"] < cfg["alert_threshold"]]

    if dry:
        print(f"[dry] fetched {counts}, eligible {len(cand)}, alerts {len(alerts)}, watch {len(watch)}; {llm_note}")
        for c in alerts:
            print(f"  ALERT [{c['sc']['score']}] {c['title']} — {c['venue']}")
        for c in watch[:15]:
            print(f"  watch [{c['sc']['score']}] {c['title']} — {c['venue']}")
        return

    for c in cand:
        tier = "alert" if c in alerts else ("watch" if c in watch else "low")
        seen["items"][norm_title(c["title"])] = {"first_seen": today, "tier": tier, "src": c["source"], "score": c["sc"]["score"]}
    seen["last_run"] = today
    STATE_DIR.mkdir(exist_ok=True)
    DIGESTS.mkdir(exist_ok=True)
    SEEN.write_text(json.dumps(seen, indent=0, ensure_ascii=False))
    p = write_digest(today, alerts, watch, counts, llm_note)
    log_line(f"run {today}: fetched {sum(counts.values())} ({', '.join(f'{k} {v}' for k, v in counts.items())}), "
             f"eligible {len(cand)}, ALERT {len(alerts)}, watch {len(watch)} -> {p.relative_to(ROOT)}. {llm_note}")
    if alerts:
        top = "\n".join(f"• {c['title'][:90]}" for c in alerts[:cfg["max_alerts_in_notification"]])
        notify(f"Aging × Macro: {len(alerts)} new paper alert(s)", top + f"\n{p}")


def status():
    seen = load_seen()
    print(f"last run: {seen['last_run']}; ledger: {len(seen['items'])} items; digests: {len(list(DIGESTS.glob('*_digest.md')))}")
    subprocess.run(["systemctl", "--user", "list-timers", "aging-macro-monitor.timer", "--no-pager"], check=False)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] not in ("run", "status"):
        print(__doc__)
        sys.exit(1)
    if args[0] == "status":
        status()
    else:
        run(dry="--dry" in args, use_llm="--no-llm" not in args)
