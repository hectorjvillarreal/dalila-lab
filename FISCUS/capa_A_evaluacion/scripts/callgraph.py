#!/usr/bin/env python3
"""Build a call graph among the Stata files: edges from `do/run/include` and from calls to
programs defined in shipped .ado files (command at start of a line, optionally after noisily/quietly/capture)."""
import os, re, sys, csv
root, out_csv = sys.argv[1], sys.argv[2]
files = {}
for dp, dn, fn in os.walk(root):
    for f in fn:
        if os.path.splitext(f)[1].lower() in ('.do', '.ado'):
            p = os.path.join(dp, f)
            files[os.path.relpath(p, root)] = open(p, encoding='utf-8', errors='replace').read()
ado_names = {os.path.splitext(os.path.basename(p))[0]: p for p in files if p.endswith('.ado')}
# programs defined inside files
prog_def = {}
for p, txt in files.items():
    for m in re.finditer(r'^\s*(?:capture\s+)?program\s+(?:define\s+)?(?!drop\b)([A-Za-z_][\w]*)', txt, re.M):
        prog_def.setdefault(m.group(1), []).append(p)
prefix = r'^\s*(?:(?:noisily|noi|quietly|qui|capture|cap|nois)\s+)*'
edges = []
for p, txt in files.items():
    t2 = re.sub(r'/\*.*?\*/', lambda m: '\n'*m.group(0).count('\n'), txt, flags=re.S)
    for i, line in enumerate(t2.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith('*') or s.startswith('//'): continue
        m = re.match(prefix + r'(do|run|include)\s+(.+)$', s)
        if m:
            target = m.group(2).strip().split('//')[0].strip()
            edges.append((p, i, m.group(1), target)); continue
        m = re.match(prefix + r'([A-Za-z_]\w*)\b', s)
        if m:
            cmd = m.group(1)
            if cmd in ado_names and ado_names[cmd] != p:
                edges.append((p, i, 'cmd', cmd))
            elif cmd in prog_def and p not in prog_def[cmd]:
                edges.append((p, i, 'cmd', cmd))
with open(out_csv, 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['caller', 'line', 'kind', 'target']); w.writerows(edges)
print('program definitions:')
for k, v in sorted(prog_def.items()):
    print(f'  {k}: {v}')
print(f'{len(edges)} edges')
