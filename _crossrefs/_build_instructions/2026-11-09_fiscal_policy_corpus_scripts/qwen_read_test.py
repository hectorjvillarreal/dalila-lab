import json, time, urllib.request, sys
doc = open("/home/hectorjuan/Dalila/_crossrefs/corpus/fiscal_policy/foundational/benassy-quere_2019_ch4_fiscal_policy.md").read()
body_start = doc.find("## Transcription")
text = doc[body_start:]
print("chars:", len(text), "~tokens:", len(text)//4, flush=True)
QS = [
 ("Q1 recall", "According to Box 4.5, what is the formula for the primary deficit that stabilizes the debt-to-GDP ratio, and what does each symbol mean? Cite the equation label."),
 ("Q2 recall", "What growth assumption did the Maastricht Treaty's 3% deficit and 60% debt limits rest on, according to the chapter? Show the arithmetic the chapter gives."),
 ("Q3 calculation", "Using equation (B4.5.5) from the chapter, suppose the debt ratio is 60% of GDP, the nominal interest rate is 5% and nominal GDP growth is 3%. What primary balance (surplus or deficit, in % of GDP) keeps the debt ratio constant? Show the steps."),
 ("Q4 concept", "Explain Ricardian equivalence as presented in Box 4.11, and list the reasons the chapter gives for why it may fail in practice."),
 ("Q5 locate", "Which box discusses Sutherland (1997), and what is its main result about the fiscal multiplier at high debt levels?"),
 ("Q6 synthesis", "Summarize in 5 sentences the chapter's conclusion (section 4.3.4) on the old and new views of fiscal policy."),
 ("Q7 trap", "What is the title of Box 4.17 in this chapter? If there is no box with that number, say so and explain what the text does with that reference."),
]
SYS = ("You are answering questions about a textbook chapter whose full text is provided. Answer only from the text. "
       "Quote equation labels and page markers (<!-- p. NNN -->) when you can. If the text does not contain the answer, say so.")
for tag, q in QS:
    prompt = f"{SYS}\n\n=== CHAPTER TEXT ===\n{text}\n=== END ===\n\nQuestion: {q}\nAnswer:"
    body = {"model": "qwen3.5:9b", "prompt": prompt, "stream": False, "think": False,
            "options": {"temperature": 0, "num_predict": 700, "num_ctx": 98304}}
    t = time.time()
    req = urllib.request.Request("http://localhost:11434/api/generate", data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req, timeout=3000).read())
    print(f"\n##### {tag}  [{time.time()-t:.0f}s; prompt tokens {r.get('prompt_eval_count')}]\n{q}\n---\n{r['response'].strip()}", flush=True)
