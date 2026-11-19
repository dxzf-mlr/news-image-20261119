#!/usr/bin/env python3
"""Draw the 1024x1024 front-page image for news-image-20261119.

All five stories were verified against Reuters / AP / Al Jazeera / NDTV
reporting of Thursday 19 November 2026. Run: python3 draw_image.py
Writes assets/entry.png (PNG, 1024x1024, deterministic bytes).
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
NAVY = (20, 33, 61)
RED = (178, 34, 34)
GREY = (90, 90, 90)
LIGHT_GREY = (200, 196, 186)

FONT_DIR = "/usr/share/fonts/truetype"


def font(name, size):
    for path in (
        os.path.join(FONT_DIR, "liberation", name),
        os.path.join(FONT_DIR, "dejavu", name),
    ):
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


SERIF_B = lambda s: font("LiberationSerif-Bold.ttf", s)
SERIF = lambda s: font("LiberationSerif-Regular.ttf", s)
SANS_B = lambda s: font("LiberationSans-Bold.ttf", s)
SANS = lambda s: font("LiberationSans-Regular.ttf", s)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def flag_us(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], outline=INK, width=2)
    for i in range(7):
        d.rectangle([x, y + i * h / 7, x + w, y + (i + 1) * h / 7],
                    fill=(178, 34, 34) if i % 2 == 0 else PAPER)
    d.rectangle([x, y, x + w * 0.4, y + h * 4 / 7], fill=(20, 33, 61))
    for r in range(3):
        for c in range(4):
            cx, cy = x + 6 + c * 9, y + 5 + r * 8
            d.ellipse([cx - 1, cy - 1, cx + 1, cy + 1], fill=PAPER)


def flag_cn(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16), outline=INK, width=2)
    for cx, cy, r in [(x + 12, y + 10, 5), (x + 26, y + 7, 2),
                      (x + 30, y + 14, 2), (x + 28, y + 22, 2), (x + 20, y + 25, 2)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 222, 0))


def flag_ru(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], outline=INK, width=2)
    for i, col in enumerate([(255, 255, 255), (0, 57, 166), (213, 0, 50)]):
        d.rectangle([x, y + i * h / 3, x + w, y + (i + 1) * h / 3], fill=col)


def icon_tanker(d, x, y, s):
    d.rectangle([x, y + s * 0.55, x + s, y + s * 0.8], fill=(30, 30, 30))
    d.rectangle([x + s * 0.62, y + s * 0.3, x + s * 0.78, y + s * 0.55],
                fill=(30, 30, 30))
    d.polygon([(x + s * 0.2, y + s * 0.5), (x + s * 0.38, y),
               (x + s * 0.56, y + s * 0.5)], fill=(230, 90, 20))
    d.polygon([(x + s * 0.45, y + s * 0.55), (x + s * 0.58, y + s * 0.15),
               (x + s * 0.72, y + s * 0.55)], fill=(240, 140, 30))
    d.line([x, y + s * 0.85, x + s, y + s * 0.85], fill=(40, 90, 140), width=4)


def icon_scales(d, x, y, s):
    d.line([x + s / 2, y + 2, x + s / 2, y + s * 0.85], fill=INK, width=4)
    d.line([x + 4, y + s * 0.22, x + s - 4, y + s * 0.22], fill=INK, width=4)
    for cx in (x + 8, x + s - 8):
        d.polygon([(cx - 12, y + s * 0.22), (cx + 12, y + s * 0.22),
                   (cx, y + s * 0.55)], outline=INK, width=3)
    d.line([x + 4, y + s * 0.9, x + s - 4, y + s * 0.9], fill=INK, width=4)


def icon_eu(d, x, y, s):
    import math
    d.ellipse([x, y, x + s, y + s], fill=(0, 51, 153))
    for i in range(12):
        a = math.pi * 2 * i / 12 - math.pi / 2
        cx = x + s / 2 + math.cos(a) * s * 0.32
        cy = y + s / 2 + math.sin(a) * s * 0.32
        d.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=(255, 204, 0))


def icon_vi(d, x, y, s):
    d.rounded_rectangle([x, y, x + s, y + s], radius=10,
                        fill=(20, 20, 20), outline=(255, 180, 0), width=3)
    d.text((x + s / 2, y + s / 2), "VI", font=SANS_B(int(s * 0.52)),
           fill=(255, 180, 0), anchor="mm")


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 40

    # ---- masthead ----
    d.text((W // 2, 30), "THE WORLD", font=SERIF_B(96), fill=NAVY, anchor="ma")
    d.line([mx, 138, W - mx, 138], fill=INK, width=3)
    d.text((W // 2, 150), "T H U R S D A Y   1 9   N O V E M B E R   2 0 2 6",
           font=SANS_B(30), fill=RED, anchor="ma")
    d.line([mx, 196, W - mx, 196], fill=INK, width=3)

    # ---- lead story: summit ----
    y = 210
    d.text((mx, y), "DIPLOMACY  •  SHENZHEN, CHINA", font=SANS_B(20), fill=RED)
    d.text((mx, 240), "TRUMP, XI AND PUTIN MEET", font=SANS_B(40), fill=INK)
    d.text((mx, 286), "IN FIRST TRILATERAL SUMMIT", font=SANS_B(40), fill=INK)
    flag_us(d, 700, 246, 76, 50)
    flag_cn(d, 786, 246, 76, 50)
    flag_ru(d, 872, 246, 76, 50)
    d.text((700, 302), "USA  •  CHINA  •  RUSSIA", font=SANS_B(16), fill=GREY)
    lead = ("Leaders of the world's three nuclear powers meet face to face "
            "for the first time. Nuclear arms control tops the agenda, "
            "but hopes of a breakthrough are low.")
    draw_lines(d, wrap(d, lead, SANS(21), 944), mx, 348, SANS(21), INK, 28)
    d.line([mx, 412, W - mx, 412], fill=LIGHT_GREY, width=2)

    # ---- four stories, 2x2 grid ----
    stories = [
        ("ENERGY  •  STRAIT OF HORMUZ",
         "THREE TANKERS ABLAZE\nAFTER 'HITTING MINES'",
         "Iran says the ships struck mines east of the strait; "
         "the claims are unverified as the US\u2013Iran war widens.",
         icon_tanker),
        ("CULTURE  •  WORLDWIDE",
         "GTA VI LAUNCHES\nWORLDWIDE",
         "Rockstar's blockbuster arrives after a 13-year wait, "
         "to near-perfect reviews.",
         icon_vi),
        ("JUSTICE  •  THE HAGUE",
         "WORLD COURT RULES\nON MYANMAR",
         "The ICJ delivers its landmark judgment on the Rohingya "
         "genocide case brought by Gambia.",
         icon_scales),
        ("EUROPE  •  BERLIN",
         "ALLIES RALLY FOR\nUKRAINE IN BERLIN",
         "Europe's 'coalition of the willing' meets as the EU "
         "proposes a \u20ac45bn loan for Kyiv.",
         icon_eu),
    ]
    gx, gy = mx, 430
    cw, ch = 462, 252
    for i, (tag, head, body, icon) in enumerate(stories):
        x = gx + (i % 2) * (cw + 20)
        yy = gy + (i // 2) * (ch + 16)
        d.rectangle([x, yy, x + cw, yy + ch], outline=LIGHT_GREY, width=2)
        d.rectangle([x, yy, x + 8, yy + ch], fill=RED)
        tx = x + 24
        d.text((tx, yy + 14), tag, font=SANS_B(17), fill=RED)
        hy = yy + 42
        for ln in head.split("\n"):
            d.text((tx, hy), ln, font=SANS_B(29), fill=INK)
            hy += 34
        by = hy + 8
        draw_lines(d, wrap(d, body, SANS(19), cw - 110), tx, by, SANS(19),
                   (60, 60, 60), 26)
        icon(d, x + cw - 78, yy + ch - 78, 58)

    # ---- footer ----
    fy = 972
    d.line([mx, fy - 12, W - mx, fy - 12], fill=INK, width=2)
    d.text((W // 2, fy), "Sources: Reuters, AP, Al Jazeera, NDTV  •  "
           "All events reported on 19 November 2026",
           font=SANS(16), fill=GREY, anchor="ma")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "assets", "entry.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
