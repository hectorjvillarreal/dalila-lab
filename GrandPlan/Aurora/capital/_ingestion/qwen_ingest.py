import json, sys, time, urllib.request
src, out = sys.argv[1], sys.argv[2]
paper = open(src, encoding="utf-8").read()
q = """You have the full text of an economics paper above. Answer each question precisely, citing section/equation/table numbers from the text. If the text does not say something, answer "NOT IN TEXT".
Q1. State the production structure: what is the task aggregator, what is sigma, how are tasks split between labor and machines, and which parameters govern automation (name them as in the paper).
Q2. What is the closure of the model: closed or open economy? Is the interest rate determined domestically or given from the world? Quote the sentence.
Q3. Verify the headline: the growth rate with optimal saving vs fixed saving, the fixed saving rate used, and the value of sigma at which these numbers hold. Cite the table.
Q4. State the paper's claim about why the saving rate rises (capital share vs patience). Give the accounting identity.
Q5. What happens to the 10-year real yield and the real interest rate along the transition?
Q6. Describe every tax or public-finance instrument analysed in the paper (type of tax, who receives the revenue, peak rate, growth cost, incidence).
Q7. Does the paper discuss open economies, emerging markets, 'bystander' economies, government debt, or energy/power plants? For each, quote or say NOT IN TEXT.
Q8. What happens to wages and to hand-to-mouth households?"""
body = {"model": "qwen3.5:9b", "stream": False, "think": False,
        "options": {"num_ctx": 65536, "temperature": 0.1},
        "messages": [{"role": "user", "content": "PAPER TEXT:\n\n" + paper + "\n\n" + q}]}
t = time.time()
req = urllib.request.Request("http://localhost:11434/api/chat", data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
r = json.load(urllib.request.urlopen(req, timeout=7200))
with open(out, "w") as f:
    f.write(f"# qwen3.5:9b whole-document ingestion — {time.time()-t:.0f}s, prompt_eval_count={r.get('prompt_eval_count')}, eval_count={r.get('eval_count')}\n\n")
    f.write(r["message"]["content"])
print("done", time.time()-t, r.get("prompt_eval_count"))
