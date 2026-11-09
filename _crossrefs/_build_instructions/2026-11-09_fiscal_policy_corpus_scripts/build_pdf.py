import sys, os
from PIL import Image, ImageOps, ImageDraw, ImageFont
src, out = sys.argv[1], sys.argv[2]
# first page of each spread -> photo stem (None = not photographed)
spreads = {148:'64651', 150:'64652', 152:'64667', 154:'64668', 156:'64655', 158:'64656', 160:'64657'}
first = {64581:64622, 64583:64623, 64589:64624, 64593:64625, 64596:64626, 64603:64627, 64605:64628, 64610:64629, 64613:64630, 64615:64634}
for i in range(37):                      # 64579..64615 = pp. 162-163 .. 234-235
    n = 64579 + i; spreads[162 + 2*i] = str(first.get(n, n))
single = {236: 'p236_page'}  # re-shot 2026-11-09 (64691.jpg), rotated and cropped                  # last page, shot upright on its own
W = 3000
F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 70)
Fs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 44)
def text_page(lines, bg="white"):
    im = Image.new("RGB", (W, 2250), bg); d = ImageDraw.Draw(im); y = 300
    for i, l in enumerate(lines):
        d.text((200, y), l, fill="black", font=F if i == 0 else Fs); y += 130 if i == 0 else 70
    return im
gaps = [f"{a}–{a+1}" for a, f in sorted(spreads.items()) if f is None]
pages = [text_page([
    "Bénassy-Quéré, Cœuré, Jacquet & Pisani-Ferry",
    "Economic Policy: Theory and Practice (2nd ed.)",
    "Chapter 4 · Fiscal Policy — photographed pages 148–236",
    "",
    "Working copy for class use (MEK_FP2026). Assembled 2026-11-09 from phone photos (four batches).",
    "Each PDF page is a two-page spread of the book, rotated upright.",
    "",
    ("MISSING (not photographed): pp. " + ", ".join(gaps) + ".") if gaps else "Complete: pp. 148–236, no gaps.",
])]
for a, f in sorted(spreads.items()):
    label = f"pp. {a}–{a+1}"
    if f is None:
        im = Image.new("RGB", (W, 2250), (235, 235, 235))
        ImageDraw.Draw(im).text((W//2 - 500, 1000), f"{label}  —  MISSING (not photographed)", fill="black", font=F)
        pages.append(im); print("placeholder", label); continue
    im = ImageOps.exif_transpose(Image.open(os.path.join(src, f + ".jpg"))).rotate(90, expand=True)
    im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    pages.append(im.convert("RGB")); print("page", f, label)
for a, f in sorted(single.items()):
    im = ImageOps.exif_transpose(Image.open(os.path.join(src, f + ".jpg")))
    im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    pages.append(im.convert("RGB")); print("page", f, f"p. {a}")
pages[0].save(out, "PDF", resolution=300, save_all=True, append_images=pages[1:], quality=82)
print("wrote", out, os.path.getsize(out)//1_000_000, "MB,", len(pages), "pages")
