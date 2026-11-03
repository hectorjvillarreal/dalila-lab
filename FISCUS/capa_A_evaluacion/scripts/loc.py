#!/usr/bin/env python3
"""Lines of code per Stata file: total, non-blank, non-comment (handles //, *, /* */)."""
import csv, os, re, sys
root, out = sys.argv[1], sys.argv[2]
rows = []
for dp, dn, fn in os.walk(root):
    for f in fn:
        if os.path.splitext(f)[1].lower() not in ('.do', '.ado', '.mata'):
            continue
        p = os.path.join(dp, f)
        try:
            txt = open(p, encoding='utf-8', errors='replace').read()
        except Exception as e:
            print('ERR', p, e); continue
        lines = txt.splitlines()
        total = len(lines); nonblank = sum(1 for l in lines if l.strip())
        # strip block comments
        t2 = re.sub(r'/\*.*?\*/', lambda m: '\n'*m.group(0).count('\n'), txt, flags=re.S)
        code = 0
        for l in t2.splitlines():
            s = l.strip()
            if not s: continue
            if s.startswith('*') or s.startswith('//'): continue
            code += 1
        rows.append((os.path.relpath(p, root), total, nonblank, code))
rows.sort()
with open(out, 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['relpath', 'lines_total', 'lines_nonblank', 'lines_code']); w.writerows(rows)
print(f"{len(rows)} files; total={sum(r[1] for r in rows)} nonblank={sum(r[2] for r in rows)} code={sum(r[3] for r in rows)}")
