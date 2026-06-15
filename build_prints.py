#!/usr/bin/env python3
"""Generate printable wall-art SVG sets for Quiet Press.
Output: products/<set>/print-XX.svg  (4:5 ratio, 1600x2000, print-ready vector)."""
import os, math

W, H = 1600, 2000  # 4:5 ratio

def svg(body, bg):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">\n'
            f'  <rect width="{W}" height="{H}" fill="{bg}"/>\n{body}</svg>\n')

def write(folder, idx, body, bg):
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/print-{idx:02d}.svg", "w") as f:
        f.write(svg(body, bg))

def circle(cx, cy, r, fill): return f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>\n'
def rect(x, y, w, h, fill): return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>\n'

def arc(cx, cy, r, start, end, fill, stroke=None, sw=0):
    """Filled circular sector / arc (degrees)."""
    sa, ea = math.radians(start), math.radians(end)
    x1, y1 = cx + r*math.cos(sa), cy + r*math.sin(sa)
    x2, y2 = cx + r*math.cos(ea), cy + r*math.sin(ea)
    large = 1 if (end - start) % 360 > 180 else 0
    d = f"M {cx} {cy} L {x1:.1f} {y1:.1f} A {r} {r} 0 {large} 1 {x2:.1f} {y2:.1f} Z"
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'  <path d="{d}" fill="{fill}"{s}/>\n'

def semi(cx, cy, r, fill, up=True):
    """Half-disc (flat side horizontal)."""
    if up:
        d = f"M {cx-r} {cy} A {r} {r} 0 0 1 {cx+r} {cy} Z"
    else:
        d = f"M {cx-r} {cy} A {r} {r} 0 0 0 {cx+r} {cy} Z"
    return f'  <path d="{d}" fill="{fill}"/>\n'

def tri(pts, fill):
    p = " ".join(f"{x},{y}" for x, y in pts)
    return f'  <polygon points="{p}" fill="{fill}"/>\n'

def line(x1, y1, x2, y2, stroke, sw):
    return f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"/>\n'

def frame():
    """Thin inner keyline used across all prints."""
    return f'  <rect x="80" y="80" width="{W-160}" height="{H-160}" fill="none" stroke="#00000015" stroke-width="2"/>\n'

# ----------------------------------------------------------------------------
# SET 1 — BAUHAUS SHAPES (cream + primary)
# ----------------------------------------------------------------------------
CREAM = "#F2EBDD"
RED, BLUE, YEL, BLK = "#D14B3D", "#2E5A8C", "#E7B23C", "#1C1A17"
S1 = "products/bauhaus-shapes"

b1 = frame() + circle(800, 760, 360, RED) + rect(440, 1180, 720, 240, BLUE)
write(S1, 1, b1, CREAM)

b2 = frame() + tri([(800,360),(1180,1180),(420,1180)], BLUE) + circle(800, 1320, 200, YEL)
write(S1, 2, b2, CREAM)

b3 = frame() + arc(800, 1300, 520, 180, 360, RED) + arc(800, 1300, 360, 180, 360, YEL) + arc(800, 1300, 200, 180, 360, BLUE)
write(S1, 3, b3, CREAM)

b4 = frame()
for i, c in enumerate([RED, BLUE, YEL, BLK]):
    x = 360 + (i % 2) * 440
    y = 560 + (i // 2) * 480
    b4 += rect(x, y, 360, 360, c)
write(S1, 4, b4, CREAM)

b5 = frame() + tri([(80,80),(1520,80),(80,1920)], BLUE) + circle(1080, 1320, 260, YEL)
write(S1, 5, b5, CREAM)

b6 = frame()
for i, c in enumerate([RED, YEL, BLUE]):
    b6 += rect(360, 460 + i*380, 880, 240, c)
write(S1, 6, b6, CREAM)

# ----------------------------------------------------------------------------
# SET 2 — MID-CENTURY MODERN (muted retro)
# ----------------------------------------------------------------------------
MC_BG = "#EDE5D4"
MUST, TERRA, SAGE, NAVY = "#C8913D", "#B5573E", "#7E8F6E", "#2C3E4C"
S2 = "products/mid-century-modern"

# sunburst
m1 = frame()
for k in range(12):
    ang = math.radians(k*30)
    m1 += line(800, 1000, 800+560*math.cos(ang), 1000+560*math.sin(ang), TERRA, 14)
m1 += circle(800, 1000, 150, MUST)
write(S2, 1, m1, MC_BG)

# overlapping circles (transparency via opacity)
m2 = frame()
m2 += f'  <circle cx="640" cy="900" r="320" fill="{SAGE}" opacity="0.85"/>\n'
m2 += f'  <circle cx="960" cy="1100" r="320" fill="{NAVY}" opacity="0.75"/>\n'
write(S2, 2, m2, MC_BG)

# rolling hills (arcs)
m3 = frame()
m3 += semi(560, 1400, 380, SAGE)
m3 += semi(1080, 1400, 300, MUST)
m3 += circle(1120, 760, 150, TERRA)
write(S2, 3, m3, MC_BG)

# atomic diamond
m4 = frame()
m4 += tri([(800,420),(1120,1000),(800,1580)], NAVY)
m4 += tri([(800,420),(480,1000),(800,1580)], TERRA)
write(S2, 4, m4, MC_BG)

# leaf shapes (two opposing arcs forming a leaf)
m5 = frame()
m5 += f'  <path d="M 800 480 Q 1120 1000 800 1520 Q 480 1000 800 480 Z" fill="{SAGE}"/>\n'
m5 += line(800, 520, 800, 1480, MC_BG, 8)
write(S2, 5, m5, MC_BG)

# stacked bars + circle
m6 = frame()
for i, c in enumerate([TERRA, MUST, SAGE]):
    m6 += rect(360, 560 + i*300, 880, 180, c)
m6 += circle(1140, 540, 110, NAVY)
write(S2, 6, m6, MC_BG)

# ----------------------------------------------------------------------------
# SET 3 — BOHO ARCHES (warm neutral / terracotta)
# ----------------------------------------------------------------------------
BOHO_BG = "#E7DAC6"
RUST, SAND, CHAR, CLAY = "#C26B4A", "#D9A777", "#3A352F", "#9C5C44"
S3 = "products/boho-arches"

# arch + sun
def arch(cx, top, w, h, fill):
    r = w/2
    bottom = top + h
    d = (f"M {cx-r} {bottom} L {cx-r} {top+r} A {r} {r} 0 0 1 {cx+r} {top+r} "
         f"L {cx+r} {bottom} Z")
    return f'  <path d="{d}" fill="{fill}"/>\n'

a1 = frame() + arch(800, 520, 760, 1080, RUST) + circle(800, 820, 180, SAND)
write(S3, 1, a1, BOHO_BG)

# stacked arches
a2 = frame() + arch(800, 460, 820, 1180, CLAY) + arch(800, 700, 540, 940, SAND) + arch(800, 940, 280, 700, BOHO_BG)
write(S3, 2, a2, BOHO_BG)

# half sun with rays
a3 = frame()
a3 += semi(800, 1300, 360, RUST, up=True)
for k in range(7):
    ang = math.radians(180 + k*30)
    a3 += line(800, 1300, 800+520*math.cos(ang), 1300+520*math.sin(ang), CLAY, 10)
write(S3, 3, a3, BOHO_BG)

# mountains
a4 = frame()
a4 += tri([(420,1480),(760,760),(1100,1480)], CHAR)
a4 += tri([(820,1480),(1120,920),(1420,1480)], RUST)
a4 += circle(560, 640, 110, SAND)
write(S3, 4, a4, BOHO_BG)

# dunes (waves)
a5 = frame()
a5 += f'  <path d="M 80 1200 Q 480 980 880 1200 T 1520 1200 V 1920 H 80 Z" fill="{SAND}"/>\n'
a5 += f'  <path d="M 80 1420 Q 520 1220 960 1420 T 1520 1420 V 1920 H 80 Z" fill="{RUST}"/>\n'
a5 += circle(1120, 720, 150, CLAY)
write(S3, 5, a5, BOHO_BG)

# circle within arch
a6 = frame() + arch(800, 500, 720, 1100, SAND)
a6 += f'  <circle cx="800" cy="1020" r="220" fill="none" stroke="{CHAR}" stroke-width="14"/>\n'
a6 += line(800, 800, 800, 1240, CHAR, 14)
write(S3, 6, a6, BOHO_BG)

print("Generated 18 prints across 3 sets.")
