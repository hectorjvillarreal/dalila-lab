import sys, json, base64, time, urllib.request
from PIL import Image
import io
PROMPT = ("You are transcribing one page of an economics textbook from a photograph. "
          "Output the page text verbatim as Markdown. Rules: keep paragraphs; keep section headings as Markdown headings; "
          "render boxes as a blockquote starting with the box title in bold; write all equations in LaTeX ($...$ inline, $$...$$ display) "
          "and keep equation labels like (B4.5.2); keep footnote markers as [^n]; for a figure or chart, write **Figure x.y** followed by its caption, then one or two sentences describing what the chart shows (axes, series, approximate values); never repeat a line you have already written; "
          "ignore the running header and the page number; ignore any text from a neighbouring page cut at the edge; write [illegible] for words you cannot read. "
          "Do not summarize, do not add commentary.")
def run(path, max_side=1600, model="qwen3.5:9b"):
    im = Image.open(path).convert("RGB"); im.thumbnail((max_side, max_side))
    buf = io.BytesIO(); im.save(buf, "PNG"); b64 = base64.b64encode(buf.getvalue()).decode()
    body = {"model": model, "prompt": PROMPT, "images": [b64], "stream": False, "think": False,
            "options": {"temperature": 0, "num_predict": 3000, "num_ctx": 8192}}
    t = time.time()
    req = urllib.request.Request("http://localhost:11434/api/generate", data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req, timeout=900).read())
    return r["response"], time.time()-t
if __name__ == "__main__":
    for p in sys.argv[1:]:
        txt, dt = run(p); print(f"### {p}  [{dt:.0f}s, {len(txt.split())} words]\n{txt}\n")
