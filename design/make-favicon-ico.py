"""Render the Dataframe mark (19-unit grid) at 16, 32 and 48 px and pack it into favicon.ico.

Pure Python, no dependencies. Usage: python3 design/make-favicon-ico.py docs/favicon.ico
"""
import struct, sys, zlib

NAVY = (0x0E, 0x28, 0x41)
CELL = (0xDA, 0xE9, 0xF8)
CELLS = [(2, 5), (6, 9), (10, 13), (14, 17)]
DOTS = [(3, 4), (7, 8), (11, 12), (15, 16)]

def inside(v, spans):
    return any(a <= v < b for a, b in spans)

def colour(x, y):
    if inside(x, CELLS) and inside(y, CELLS):
        return NAVY if (inside(x, DOTS) and inside(y, DOTS)) else CELL
    return NAVY

to_lin = lambda c: (c / 255) / 12.92 if c / 255 <= 0.04045 else ((c / 255 + 0.055) / 1.055) ** 2.4
to_srgb = lambda l: round(255 * (12.92 * l if l <= 0.0031308 else 1.055 * l ** (1 / 2.4) - 0.055))
LIN = {NAVY: tuple(map(to_lin, NAVY)), CELL: tuple(map(to_lin, CELL))}

def render(n, ss=16):
    rows = []
    step = 19 / n
    for j in range(n):
        row = bytearray([0])  # PNG filter: none
        for i in range(n):
            acc = [0.0, 0.0, 0.0]
            for sj in range(ss):
                y = (j + (sj + 0.5) / ss) * step
                for si in range(ss):
                    c = LIN[colour((i + (si + 0.5) / ss) * step, y)]
                    acc[0] += c[0]; acc[1] += c[1]; acc[2] += c[2]
            k = ss * ss
            row += bytes([to_srgb(acc[0] / k), to_srgb(acc[1] / k), to_srgb(acc[2] / k), 255])
        rows.append(bytes(row))
    raw = b"".join(rows)
    chunk = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", n, n, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))

sizes = [16, 32, 48]
pngs = [render(n) for n in sizes]
offset = 6 + 16 * len(sizes)
out = struct.pack("<HHH", 0, 1, len(sizes))
for n, p in zip(sizes, pngs):
    out += struct.pack("<BBBBHHII", n, n, 0, 0, 1, 32, len(p), offset)
    offset += len(p)
out += b"".join(pngs)
open(sys.argv[1], "wb").write(out)
print(len(out), "bytes")
