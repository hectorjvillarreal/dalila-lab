import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qwen_page import run
src, out = sys.argv[1], sys.argv[2]
pages = sorted(f[:-4] for f in os.listdir(src) if f.endswith(".png"))
log = open(os.path.join(out, "_progress.md"), "a")
for p in pages:
    dst = os.path.join(out, p + ".md")
    if os.path.exists(dst) and os.path.getsize(dst) > 200: continue
    try:
        txt, dt = run(os.path.join(src, p + ".png"))
        open(dst, "w").write(f"<!-- {p}: transcribed by qwen3.5:9b (ollama, local) {time.strftime('%Y-%m-%d %H:%M')} ; {len(txt.split())} words ; {dt:.0f}s ; unverified -->\n\n" + txt.strip() + "\n")
        log.write(f"- {p}: ok, {len(txt.split())} words, {dt:.0f}s\n"); log.flush()
        print(p, len(txt.split()), f"{dt:.0f}s", flush=True)
    except Exception as e:
        log.write(f"- {p}: ERROR {e}\n"); log.flush(); print(p, "ERROR", e, flush=True)
print("ALL DONE", flush=True)
