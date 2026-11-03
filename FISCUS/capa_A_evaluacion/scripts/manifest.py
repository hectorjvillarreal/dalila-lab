#!/usr/bin/env python3
"""Write manifest.csv (relpath,size,sha256,ext) and inventory.csv (by extension) for a source tree."""
import csv, hashlib, os, sys
from collections import defaultdict
root, out_manifest, out_inv = sys.argv[1], sys.argv[2], sys.argv[3]
rows = []
for dp, dn, fn in os.walk(root):
    for f in fn:
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, root)
        h = hashlib.sha256()
        with open(p, 'rb') as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b''):
                h.update(chunk)
        ext = os.path.splitext(f)[1].lower() or '(none)'
        rows.append((rel, os.path.getsize(p), h.hexdigest(), ext))
rows.sort()
with open(out_manifest, 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['relpath', 'size_bytes', 'sha256', 'ext']); w.writerows(rows)
agg = defaultdict(lambda: [0, 0])
for rel, sz, _, ext in rows:
    agg[ext][0] += 1; agg[ext][1] += sz
with open(out_inv, 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['ext', 'n_files', 'total_bytes'])
    for ext, (n, sz) in sorted(agg.items(), key=lambda kv: -kv[1][1]):
        w.writerow([ext, n, sz])
print(f"{len(rows)} files, {sum(r[1] for r in rows)/1e6:.1f} MB")
