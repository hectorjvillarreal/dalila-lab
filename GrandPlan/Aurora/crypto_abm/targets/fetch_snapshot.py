#!/usr/bin/env python3
"""Fetch the Coinbase snapshot behind design note B0 §1 (stdlib only).

Writes CSVs to targets/data/ and a SHA256SUMS file. Run once; the committed CSVs,
not this script, are the source of truth for targets (note Appendix A).
  daily : BTC-USD, ETH-USD, 2019-01-01 .. 2026-11-16 (UTC days, closed)
  hourly: BTC-USD, 2024-01-10 .. 2026-11-16 23:00 UTC
"""
import json, sys, time, hashlib, urllib.request, datetime as dt
from pathlib import Path
OUT = Path(__file__).resolve().parent / "data"
UA = {"User-Agent": "Mozilla/5.0"}
END_DAY = dt.datetime(2026, 11, 17, tzinfo=dt.timezone.utc)   # exclusive

def candles(product, gran, start, end):
    rows = {}
    step = dt.timedelta(seconds=gran * 299)
    t = start
    while t < end:
        u = min(t + step, end)
        url = (f"https://api.exchange.coinbase.com/products/{product}/candles?granularity={gran}"
               f"&start={t:%Y-%m-%dT%H:%M:%SZ}&end={u:%Y-%m-%dT%H:%M:%SZ}")
        for attempt in range(5):
            try:
                data = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read())
                break
            except Exception as e:
                time.sleep(2 + 2 * attempt)
        else:
            raise SystemExit(f"failed: {url}")
        for c in data:
            if start.timestamp() <= c[0] < end.timestamp():
                rows[int(c[0])] = c  # [time, low, high, open, close, volume]
        t = u
        time.sleep(0.35)
    return [rows[k] for k in sorted(rows)]

def write(name, rows):
    p = OUT / name
    with open(p, "w") as f:
        f.write("time_utc,unix,low,high,open,close,volume\n")
        for c in rows:
            ts = dt.datetime.fromtimestamp(c[0], dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            f.write(f"{ts},{c[0]},{c[1]},{c[2]},{c[3]},{c[4]},{c[5]}\n")
    print(name, len(rows), rows[0][0], rows[-1][0])

OUT.mkdir(exist_ok=True)
d0 = dt.datetime(2019, 1, 1, tzinfo=dt.timezone.utc)
for prod in ("BTC-USD", "ETH-USD"):
    write(f"{prod}_daily.csv", candles(prod, 86400, d0, END_DAY))
write("BTC-USD_hourly.csv", candles("BTC-USD", 3600, dt.datetime(2024, 1, 10, tzinfo=dt.timezone.utc), END_DAY))
with open(OUT / "SHA256SUMS", "w") as f:
    for p in sorted(OUT.glob("*.csv")):
        f.write(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n")
print((OUT / "SHA256SUMS").read_text())
