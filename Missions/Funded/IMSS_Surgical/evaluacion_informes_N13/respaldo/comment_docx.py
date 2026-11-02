import sys, json, docx, re
src, dst, anchors_json = sys.argv[1], sys.argv[2], sys.argv[3]
anchors = json.load(open(anchors_json, encoding='utf-8'))  # list of {id, anchor, texto}
d = docx.Document(src)
def norm(s): return re.sub(r'\s+',' ',s).replace('−','-').lower()
# collect all paragraphs including tables
def all_pars(doc):
    for p in doc.paragraphs: yield p
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs: yield p
pars=list(all_pars(d))
done=[]; missing=[]
for a in anchors:
    key=norm(a['anchor'])
    hit=None
    for p in pars:
        if key in norm(p.text):
            hit=p; break
    if hit is None or not hit.runs:
        missing.append(a['id']); continue
    d.add_comment(runs=hit.runs, text=f"[{a['id']}] {a['texto']}", author='Evaluación N13 (ITED)', initials='EV')
    done.append(a['id'])
d.save(dst)
print('comentarios insertados', len(done), 'sin ancla', missing)
