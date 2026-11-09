import sys, numpy as np
from PIL import Image, ImageOps, ImageFilter
from scipy import ndimage as ndi
src, out = sys.argv[1], sys.argv[2]
spreads = {148:'64651',150:'64652',152:'64667',154:'64668',156:'64655',158:'64656',160:'64657'}
first = {64581:64622,64583:64623,64589:64624,64593:64625,64596:64626,64603:64627,64605:64628,64610:64629,64613:64630,64615:64634}
for i in range(37): n=64579+i; spreads[162+2*i]=str(first.get(n,n))

def otsu(g):
    h,_ = np.histogram(g, bins=256, range=(0,256)); h = h.astype(float); p = h/h.sum()
    w0 = np.cumsum(p); m = np.cumsum(p*np.arange(256)); mt = m[-1]
    var = (mt*w0 - m)**2 / np.maximum(w0*(1-w0), 1e-9)
    return int(np.argmax(var))

def book_box(im):
    """bounding box of the largest bright blob (the open book) on a downsampled copy, exposure-adaptive threshold"""
    small = im.resize((im.width//8, im.height//8))
    g = np.asarray(small.convert("L")); t = otsu(g)
    mask = g > t
    mask = ndi.binary_opening(mask, iterations=3)
    lab, n = ndi.label(mask)
    if n == 0: return 0,0,im.width,im.height
    sizes = ndi.sum(mask, lab, range(1,n+1)); k = int(np.argmax(sizes))+1
    ys, xs = np.where(lab==k)
    return xs.min()*8, ys.min()*8, (xs.max()+1)*8, (ys.max()+1)*8

import os
GW = float(os.environ.get('GUTTER_WIN', '0.15'))
ONLY = os.environ.get('ONLY_PAGES')
def gutter_x(g):
    H,W = g.shape; r0,r1 = int(H*0.2), int(H*0.8); c0,c1 = int(W*(0.5-GW)), int(W*(0.5+GW))
    p = np.percentile(g[r0:r1, c0:c1], 85, axis=0)
    p = ndi.uniform_filter1d(p, 21)
    return c0 + int(p.argmin())

def flatten(g):
    """divide by a heavily blurred background to remove curvature shading, then stretch contrast"""
    g = g.astype(np.float32)
    bg = ndi.gaussian_filter(g, 60); bg = np.maximum(bg, 1)
    f = g / bg * 255.0
    lo, hi = np.percentile(f, 1), np.percentile(f, 99.5)
    f = np.clip((f - lo) / max(hi-lo, 1) * 255, 0, 255)
    return Image.fromarray(f.astype(np.uint8))

def trim_raw(g, pad=25):
    """tighten a raw-gray half to its paper: rows/cols that are mostly bright"""
    t = otsu(g)
    bright = ndi.uniform_filter(g.astype(np.float32), 15) > t
    cols = np.where(bright.mean(0) > 0.55)[0]; rows = np.where(bright.mean(1) > 0.55)[0]
    if len(cols)<50 or len(rows)<50: return g
    return g[max(rows[0]-pad,0):min(rows[-1]+pad, g.shape[0]), max(cols[0]-pad,0):min(cols[-1]+pad, g.shape[1])]

def paper_mask(g):
    """largest bright connected region of a raw-gray half = the page; holes (text) filled"""
    t = otsu(g)
    sm = ndi.uniform_filter(g.astype(np.float32), 9)
    m = sm > t
    m = ndi.binary_opening(m, iterations=6)
    lab, n = ndi.label(m)
    if n == 0: return np.ones_like(g, bool)
    sizes = ndi.sum(m, lab, range(1, n+1)); m = lab == (int(np.argmax(sizes)) + 1)
    m = ndi.binary_fill_holes(m)
    m = ndi.binary_closing(m, iterations=10)
    return m

def fit_line(pts):
    """pts: array of (x,y); returns (a,b,c) for ax+by+c=0 via PCA"""
    c = pts.mean(0); u,s_,vt = np.linalg.svd(pts-c); d = vt[0]
    n = np.array([-d[1], d[0]]); return n[0], n[1], -(n@c)
def intersect(l1, l2):
    a1,b1,c1 = l1; a2,b2,c2 = l2; D = a1*b2-a2*b1
    return np.array([(b1*c2-b2*c1)/D, (c1*a2-c2*a1)/D])

def text_quad(f, m):
    """corners of the text block (UL, LL, LR, UR) from ink in the flattened page"""
    ink = (f < 100) & m
    ink = ndi.binary_opening(ink, iterations=1)
    blobs = ndi.binary_dilation(ink, iterations=12)
    lab, n = ndi.label(blobs)
    if n == 0: return None
    sizes = ndi.sum(blobs, lab, range(1,n+1)); big = sizes >= 0.03*sizes.max()
    keep = np.isin(lab, np.where(big)[0]+1) & ink
    ys, xs = np.where(keep)
    if len(ys) < 2000: return None
    H, W = f.shape
    # robust edge points: per-row extremes in several bands
    def band_pts(axis_vals, other_vals, lo, hi, q, nb=6):
        pts = []
        edges = np.linspace(lo, hi, nb+1)
        for i in range(nb):
            sel = (axis_vals >= edges[i]) & (axis_vals < edges[i+1])
            if sel.sum() < 50: continue
            pts.append((np.percentile(other_vals[sel], q), (edges[i]+edges[i+1])/2))
        return np.array(pts)
    y_lo, y_hi = np.percentile(ys, 1), np.percentile(ys, 99); x_lo, x_hi = np.percentile(xs, 1), np.percentile(xs, 99)
    L = band_pts(ys, xs, y_lo, y_hi, 1.0);  R = band_pts(ys, xs, y_lo, y_hi, 99.0)
    T = band_pts(xs, ys, x_lo, x_hi, 1.0);  B = band_pts(xs, ys, x_lo, x_hi, 99.0)
    if min(len(L),len(R),len(T),len(B)) < 3: return None
    lL, lR = fit_line(L), fit_line(R)
    lT, lB = fit_line(T[:, ::-1]), fit_line(B[:, ::-1])   # back to (x,y)
    UL, LL, LR, UR = intersect(lL,lT), intersect(lL,lB), intersect(lR,lB), intersect(lR,lT)
    return np.array([UL, LL, LR, UR])

def expand_quad(q, fx=0.07, fy=0.05):
    c = q.mean(0); out = []
    w = (np.linalg.norm(q[3]-q[0]) + np.linalg.norm(q[2]-q[1]))/2
    h = (np.linalg.norm(q[1]-q[0]) + np.linalg.norm(q[2]-q[3]))/2
    for p_ in q:
        d = p_ - c; out.append(c + d * np.array([1 + fx*w/abs(d[0]+1e-9) if abs(d[0])>1 else 1, 1 + fy*h/abs(d[1]+1e-9) if abs(d[1])>1 else 1]))
    return np.array(out)

def finish(g, pad=20):
    m = paper_mask(g)
    ys, xs = np.where(m)
    y0, y1 = max(ys.min()-pad, 0), min(ys.max()+pad, g.shape[0]); x0, x1 = max(xs.min()-pad, 0), min(xs.max()+pad, g.shape[1])
    g, m = g[y0:y1, x0:x1], m[y0:y1, x0:x1]
    f = np.asarray(flatten(g)).copy()
    f[~m] = 255
    img = Image.fromarray(f)
    q = None
    if q is not None:
        q = expand_quad(q)
        H, W = f.shape
        q[:,0] = np.clip(q[:,0], 0, W-1); q[:,1] = np.clip(q[:,1], 0, H-1)
        w = int((np.linalg.norm(q[3]-q[0]) + np.linalg.norm(q[2]-q[1]))/2)
        h = int((np.linalg.norm(q[1]-q[0]) + np.linalg.norm(q[2]-q[3]))/2)
        if w > 400 and h > 600:
            img = img.transform((w, h), Image.QUAD, tuple(q.flatten()), Image.BICUBIC, fillcolor=255)
    return img.filter(ImageFilter.UnsharpMask(radius=2, percent=80, threshold=3))

for a,f in sorted(spreads.items()):
    if ONLY and str(a) not in ONLY.split(','): continue
    im = ImageOps.exif_transpose(Image.open(f"{src}/{f}.jpg")).rotate(90, expand=True)
    x0,y0,x1,y1 = book_box(im); book = im.crop((x0,y0,x1,y1))
    g = np.asarray(book.convert("L"))
    gx = gutter_x(g)
    for pg, sl in ((a, slice(0, gx-8)), (a+1, slice(gx+8, g.shape[1]))):
        page = finish(g[:, sl])
        page.save(f"{out}/p{pg:03d}.png")
    print(a, f, "box", (x0,y0,x1,y1), "gutter", gx, "/", x1-x0)
if not ONLY:
    im = ImageOps.exif_transpose(Image.open(f"{src}/64616.jpg"))
    g = np.asarray(im.convert("L"))
    finish(g[:, int(g.shape[1]*0.12):]).save(f"{out}/p236.png"); print(236, "single page")
