import re, os
T="_transcription_pages"; out=[]
def norm(line):
    l=line.rstrip()
    l=re.sub(r"^>\s?", "", l)                         # drop blockquote markers
    if re.fullmatch(r"#{1,6}\s*(Economic Policy|Fiscal Policy)\s*", l): return None
    m=re.match(r"^#{1,6}\s*(4\.\d)\s+(.+)$", l)
    if m: return f"## {m.group(1)} {m.group(2)}"
    m=re.match(r"^#{1,6}\s*(4\.\d\.\d)\s+(.+)$", l)
    if m: return f"### {m.group(1)} {m.group(2)}"
    m=re.match(r"^#{1,6}\s*([a-f])\)\s+(.+)$", l)
    if m: return f"#### {m.group(1)}) {m.group(2)}"
    m=re.match(r"^#{1,6}\s*(Notes|References)\s*$", l)
    if m: return f"## {m.group(1)}"
    m=re.match(r"^(?:#{1,6}\s*)?\**\s*(Box 4\.\d+)\**\s*\**\s*([^*]*?)\s*\**\s*$", l)
    if m and m.group(2).strip(): return f"#### {m.group(1)} {m.group(2).strip()}"
    m=re.match(r"^#{1,6}\s+(.+)$", l)
    if m: return f"**{m.group(1).strip()}**"
    if re.fullmatch(r"\**\s*Box 4\.\d+\s*\**", l): return None          # bare box-number continuation marker
    if re.fullmatch(r"[a-f]\) [A-Z][^.]{2,80}", l): return f"#### {l}"      # plain-text sub-heading
    m=re.fullmatch(r"\*\*(.{120,})\*\*", l)                              # whole paragraph wrongly bolded
    if m: return m.group(1)
    return l
chunks=[]
for n in range(148,237):
    s=open(f"{T}/p{n}.md").read()
    s=re.sub(r"<!--.*?-->\s*", "", s, count=1, flags=re.S).strip("\n")
    lines=[]
    if n==148:
        body=s.split("\n")
        toc=True
        for l in body:
            if toc:
                if re.match(r"^# 4 ", l): lines.append("# 4 Fiscal Policy"); lines.append(""); lines.append("**Contents**"); lines.append(""); continue
                m=re.match(r"^#{2,3}\s*(.+)$", l)
                if m: lines.append(f"- **{m.group(1)}**"); continue
                if l.startswith("- "): lines.append("    " + l); continue
                if l.strip()=="" : continue
                toc=False; lines.append(""); lines.append(l)
            else: lines.append(l)
    else:
        in_math=False
        def is_item(x): return bool(re.match(r"^(\s*[-*•]\s|\s*\d+\.\s|\||\s{2,}\S)", x))
        for l in s.split("\n"):
            nl=norm(l)
            if nl is None: continue
            if nl.strip()=="$$": 
                if not in_math and lines and lines[-1].strip(): lines.append("")
                in_math = not in_math; lines.append(nl)
                if not in_math: lines.append("")
                continue
            if in_math: lines.append(nl); continue
            # the model writes one paragraph per line: separate consecutive non-empty lines, except inside lists/tables
            if nl.strip() and lines and lines[-1].strip() and not (is_item(nl) and is_item(lines[-1])): lines.append("")
            lines.append(nl)
    text="\n".join(lines).strip("\n")
    text=re.sub(r"\n{3,}", "\n\n", text)
    chunks.append((n,text))
# join across pages
doc=""
for i,(n,text) in enumerate(chunks):
    marker=f"<!-- p. {n} -->"
    if i==0: doc=marker+"\n\n"+text; continue
    prev_end=doc.rstrip()[-1:] if doc.rstrip() else "."
    first=text.lstrip()[:1]
    cont = prev_end not in ".!?:\"”’)]*|" and (first.islower() or first in "(")
    if cont and not text.lstrip().startswith(("#","**","-","|","$","[","<")):
        doc=doc.rstrip()+" "+marker+" "+text.lstrip()
    else:
        doc=doc.rstrip()+"\n\n"+marker+"\n\n"+text
open("/tmp/claude-1000/-home-hectorjuan/67f74bf9-d8cf-429f-9df8-c3e47d4d699b/scratchpad/merged_body.md","w").write(doc+"\n")
print("merged words:", len(doc.split()))
print("\n".join(l for l in doc.split("\n") if l.startswith("#")))
