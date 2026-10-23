#!/usr/bin/env python3
"""Draw an explaining Excalidraw diagram from a JSON spec.

    python3 draw.py spec.json out.excalidraw     # draw
    python3 draw.py --check file.excalidraw      # validate an existing file
    python3 draw.py --png file.excalidraw out.png  # rough preview, to look at it

Spec (everything except nodes is optional):

    {
      "title": "Your own network: call containers by name",
      "subtitle": "Docker keeps a phone book for every network you create",
      "nodes": [
        {"id": "web", "label": "web", "detail": "Node app\\nlistens on 3000",
         "color": "green", "pos": [100, 120]},
        {"id": "db", "label": "db", "detail": "Redis", "color": "red", "at": [2, 0]},
        {"id": "door", "label": "8080", "color": "yellow", "size": "small"}
      ],
      "edges": [
        {"from": "web", "to": "db", "label": "INCR visits", "step": 1,
         "color": "green", "via": [[400, 300]], "dashed": false, "both": false}
      ],
      "areas": [
        {"label": "Network: counter-net", "detail": "172.18.0.0/16",
         "nodes": ["web", "db"], "color": "blue", "dashed": true}
      ],
      "notes": [
        {"text": "localhost inside a container means the container itself.",
         "pos": [600, 400], "w": 320, "style": "callout"},
        {"text": "docker network create counter-net", "pos": [0, 500], "style": "code"},
        {"text": "a quiet remark", "at": [1, 1]}
      ]
    }

Placement: `pos` is [x, y] in pixels (top-left of the box). `at` is [column,
row] on a loose grid (fractions are fine). Nodes with neither go in a line
(left to right, or top to bottom with "direction": "down").

Nodes: `label` is the name (big), `detail` is extra lines (smaller, under it;
use \\n for line breaks). Boxes grow to fit; `w`/`h` force a size. `size:
"small"` for ports ("doors"). `font: "mono"` for code-like labels. Shapes: box
(default), ellipse, diamond.

Colours (nodes, areas, edges): white, blue, green, yellow, red, violet, gray.
Areas are tinted boxes behind the nodes they list, label top-left, `detail`
under it. Areas nest: one that lists all of another's nodes wraps around it.

Edges: `label` (\\n allowed), `color` (green = works, red = fails), `dashed`,
`both` (arrowheads on both ends), `step` (a numbered badge), `via` (bend
points, pixels). An edge from a node to itself needs `via`.

Notes: `style` plain (default), callout (yellow sticky note) or code (grey
box, monospace). `w` sets the wrap width; `size`, `color`, `align` for plain.
"""
import json
import random
import subprocess
import sys
import time
from xml.sax.saxutils import escape

BOX_W, BOX_H = 180, 80
COL_GAP, ROW_GAP = 170, 90
SMALL_W, SMALL_H = 110, 56
HAND, MONO = 1, 3  # Excalidraw font families: 1 = Virgil (hand-drawn), 3 = Cascadia
TITLE_SIZE, SUBTITLE_SIZE, LABEL_SIZE, DETAIL_SIZE, NOTE_SIZE, EDGE_SIZE = 32, 20, 22, 16, 18, 16
INK = "#1e1e1e"
SOFT = "#495057"
AREA_PAD, AREA_TOP = 30, 56  # room around the nodes, and above them for the label

# fill for nodes, fill for areas, stroke (areas, edges, badges)
PALETTE = {
    "white": ("#ffffff", "transparent", INK),
    "blue": ("#a5d8ff", "#e7f5ff", "#1971c2"),
    "green": ("#b2f2bb", "#ebfbee", "#2f9e44"),
    "yellow": ("#ffec99", "#fff9db", "#f08c00"),
    "red": ("#ffc9c9", "#fff5f5", "#e03131"),
    "violet": ("#d0bfff", "#f3f0ff", "#6741d9"),
    "gray": ("#e9ecef", "#f8f9fa", "#495057"),
}
SHAPES = {"box": "rectangle", "rectangle": "rectangle", "ellipse": "ellipse", "diamond": "diamond"}
MAX_SHAPES = 60

_rng = random.Random(7)


def _id():
    return "".join(_rng.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(12))


def _color(name, where):
    if name not in PALETTE:
        sys.exit(f"{where}: unknown color {name!r}; use one of {', '.join(PALETTE)}")
    return PALETTE[name]


def _base(kind, x, y, w, h, **extra):
    el = {
        "id": _id(), "type": kind, "x": x, "y": y, "width": w, "height": h, "angle": 0,
        "strokeColor": INK, "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "solid", "roughness": 1, "opacity": 100,
        "groupIds": [], "frameId": None, "roundness": None, "seed": _rng.randint(1, 2**31),
        "version": 1, "versionNonce": _rng.randint(1, 2**31), "isDeleted": False,
        "boundElements": [], "updated": int(time.time() * 1000), "link": None, "locked": False,
    }
    el.update(extra)
    return el


def _text_size(text, size, font=HAND):
    lines = text.split("\n")
    per_char = 0.6 if font == MONO else 0.58
    return max(len(l) for l in lines) * size * per_char, len(lines) * size * 1.25


def _wrap(text, size, max_w, font=HAND):
    """Break each paragraph onto lines that fit max_w, at spaces only."""
    out = []
    for para in text.split("\n"):
        lines = []
        for word in para.split(" "):
            if lines and _text_size(f"{lines[-1]} {word}", size, font)[0] <= max_w:
                lines[-1] += f" {word}"
            else:
                lines.append(word)
        out += lines or [""]
    return "\n".join(out)


def _text(text, x, y, size, font=HAND, align="center", container=None, color=INK, anchor="center"):
    """A text element. With anchor "center", (x, y) is its middle; with "topleft", its corner."""
    w, h = _text_size(text, size, font)
    if anchor == "center":
        x, y = x - w / 2, y - h / 2
    return _base(
        "text", x, y, w, h, strokeColor=color,
        text=text, originalText=text, fontSize=size, fontFamily=font,
        textAlign=align, verticalAlign="middle" if container else "top", containerId=container,
        autoResize=True, lineHeight=1.25,
    )


def _edge_point(node, tx, ty, gap=8):
    """Where the line from node's centre towards (tx, ty) leaves the node."""
    cx, cy = node["x"] + node["width"] / 2, node["y"] + node["height"] / 2
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    hw, hh = node["width"] / 2 + gap, node["height"] / 2 + gap
    s = min(hw / abs(dx) if dx else float("inf"), hh / abs(dy) if dy else float("inf"))
    return cx + dx * s, cy + dy * s


def _grid(at):
    col, row = at
    return col * (BOX_W + COL_GAP), row * (BOX_H + ROW_GAP)


def _node(n, i, down):
    small = n.get("size") == "small"
    font = MONO if n.get("font") == "mono" else HAND
    size = DETAIL_SIZE + 2 if small else LABEL_SIZE
    label, detail = n["label"], n.get("detail", "")
    lw, lh = _text_size(label, size, font)
    dw, dh = _text_size(detail, DETAIL_SIZE) if detail else (0, 0)
    w = n.get("w") or max(SMALL_W if small else BOX_W, lw + 40, dw + 40)
    h = n.get("h") or max(SMALL_H if small else BOX_H, lh + dh + (36 if detail else 30))

    if "pos" in n:
        x, y = n["pos"]
    else:
        gx, gy = _grid(n.get("at") or ((0, i) if down else (i, 0)))
        x, y = gx + (BOX_W - w) / 2, gy + (BOX_H - h) / 2  # centred in its grid cell

    fill, _, _ = _color(n.get("color", "white"), f"node {n['id']}")
    shape = SHAPES.get(n.get("shape", "box"))
    if not shape:
        sys.exit(f"node {n['id']}: unknown shape {n['shape']!r}; use box, ellipse or diamond")
    box = _base(shape, x, y, w, h, backgroundColor=fill,
                roundness={"type": 3} if shape == "rectangle" else {"type": 2})
    if not detail:
        text = _text(label, x + w / 2, y + h / 2, size, font, container=box["id"])
        box["boundElements"].append({"type": "text", "id": text["id"]})
        return box, [box, text]

    # Name and detail as two texts grouped with the box, so they move together.
    group = _id()
    box["groupIds"] = [group]
    top = y + (h - lh - dh - 6) / 2
    name = _text(label, x + w / 2, top + lh / 2, size, font)
    more = _text(detail, x + w / 2, top + lh + 6 + dh / 2, DETAIL_SIZE, color=SOFT)
    name["groupIds"] = more["groupIds"] = [group]
    return box, [box, name, more]


def _midpoint(points):
    """Where Excalidraw puts an arrow's label: the middle point, or the middle of the middle segment."""
    if len(points) % 2:
        return points[len(points) // 2]
    a, b = points[len(points) // 2 - 1], points[len(points) // 2]
    return (a[0] + b[0]) / 2, (a[1] + b[1]) / 2


def _edge(e, by_id):
    a, b = by_id.get(e["from"]), by_id.get(e["to"])
    if not a or not b:
        sys.exit(f"edge {e['from']} -> {e['to']}: unknown node id")
    via = [tuple(p) for p in e.get("via") or []]
    if a is b and not via:
        sys.exit(f"edge {e['from']} -> itself needs 'via' points")
    centre = lambda n: (n["x"] + n["width"] / 2, n["y"] + n["height"] / 2)
    start = _edge_point(a, *(via[0] if via else centre(b)))
    end = _edge_point(b, *(via[-1] if via else centre(a)))
    pts = [start, *via, end]
    sx, sy = start
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    _, _, stroke = _color(e.get("color", "white"), f"edge {e['from']} -> {e['to']}")
    arrow = _base(
        "arrow", min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys),
        strokeColor=stroke, strokeStyle="dashed" if e.get("dashed") else "solid",
        roundness={"type": 2}, points=[[px - sx, py - sy] for px, py in pts],
        lastCommittedPoint=None, startArrowhead="arrow" if e.get("both") else None, endArrowhead="arrow",
        startBinding={"elementId": a["id"], "focus": 0, "gap": 8},
        endBinding={"elementId": b["id"], "focus": 0, "gap": 8},
    )
    arrow["x"], arrow["y"] = sx, sy
    a["boundElements"].append({"type": "arrow", "id": arrow["id"]})
    if b is not a:
        b["boundElements"].append({"type": "arrow", "id": arrow["id"]})
    out = [arrow]

    mx, my = _midpoint(pts)
    label_w = 0
    if e.get("label"):
        label = _text(e["label"], mx, my, EDGE_SIZE, container=arrow["id"], color=stroke if stroke != INK else INK)
        arrow["boundElements"].append({"type": "text", "id": label["id"]})
        label_w = label["width"]
        out.append(label)
    if "step" in e:
        out += _badge(e["step"], mx - label_w / 2 - 22 if label_w else mx, my, stroke)
    return out


def _badge(number, cx, cy, stroke):
    """A small filled circle with a step number, so a reader can follow 1, 2, 3."""
    group = _id()
    r = 16
    color = stroke if stroke != INK else "#1971c2"
    dot = _base("ellipse", cx - r, cy - r, 2 * r, 2 * r, backgroundColor=color, strokeColor=color,
                roundness={"type": 2}, groupIds=[group])
    num = _text(str(number), cx, cy, 18, color="#ffffff")
    num["groupIds"] = [group]
    return [dot, num]


def _note(note):
    style = note.get("style", "plain")
    if "pos" in note:
        x, y = note["pos"]
    else:
        gx, gy = _grid(note.get("at", [0, 1]))
        x, y = gx, gy + BOX_H / 2
    if style == "plain":
        size, font = note.get("size", NOTE_SIZE), HAND
        text = _wrap(note["text"], size, note["w"]) if note.get("w") else note["text"]
        _, _, stroke = _color(note.get("color", "gray"), "note")
        align = note.get("align", "left" if "pos" in note else "center")
        if "pos" in note:
            return [_text(text, x, y, size, align=align, color=stroke, anchor="topleft")]
        return [_text(text, x + BOX_W / 2, y, size, align=align, color=stroke)]

    code = style == "code"
    if style not in ("callout", "code"):
        sys.exit(f"note: unknown style {style!r}; use plain, callout or code")
    font, size = (MONO, 16) if code else (HAND, NOTE_SIZE)
    pad = 18
    text = _wrap(note["text"], size, note["w"] - 2 * pad, font) if note.get("w") else note["text"]
    tw, th = _text_size(text, size, font)
    w, h = note.get("w") or tw + 2 * pad, th + 2 * pad
    fill, stroke = ("#f1f3f5", "#868e96") if code else ("#fff3bf", "#f08c00")
    box = _base("rectangle", x, y, w, h, backgroundColor=fill, strokeColor=stroke,
                roundness={"type": 3}, strokeWidth=1)
    label = _text(text, x + pad, y + pad, size, font, align="left", container=box["id"], anchor="topleft")
    box["boundElements"].append({"type": "text", "id": label["id"]})
    return [box, label]


def draw(spec):
    nodes = spec.get("nodes") or []
    if not nodes:
        sys.exit("spec needs at least one node")
    down = spec.get("direction") == "down"
    elements, by_id = [], {}

    for i, n in enumerate(nodes):
        box, els = _node(n, i, down)
        by_id[n["id"]] = box
        elements += els
    for e in spec.get("edges") or []:
        elements += _edge(e, by_id)
    for note in spec.get("notes") or []:
        elements += _note(note)

    elements = _areas(spec.get("areas") or [], by_id) + elements
    elements = _title(spec, elements) + elements
    return {
        "type": "excalidraw", "version": 2, "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None},
        "files": {},
    }


def _title(spec, elements):
    if not spec.get("title"):
        return []
    x0 = min(e["x"] for e in elements)
    y0 = min(e["y"] for e in elements)
    out = []
    sub = spec.get("subtitle")
    sub_h = _text_size(sub, SUBTITLE_SIZE)[1] if sub else 0
    top = y0 - 40 - sub_h - TITLE_SIZE * 1.25
    out.append(_text(spec["title"], x0, top, TITLE_SIZE, align="left", anchor="topleft"))
    if sub:
        out.append(_text(sub, x0, top + TITLE_SIZE * 1.25 + 6, SUBTITLE_SIZE, align="left", color=SOFT, anchor="topleft"))
    return out


def _areas(areas, by_id):
    """Big labelled boxes behind the nodes they hold. Inner areas are sized
    first, so an outer area can wrap around them; outer ones are drawn first,
    so they sit behind."""
    sized = []
    for a in sorted(areas, key=lambda a: len(a["nodes"])):
        members = set(a["nodes"])
        missing = members - by_id.keys()
        if missing:
            sys.exit(f"area {a['label']!r}: unknown node ids {', '.join(sorted(missing))}")
        _, fill, stroke = _color(a.get("color", "white"), f"area {a['label']!r}")
        pad = a.get("pad", AREA_PAD)
        top = AREA_TOP + (_text_size(a["detail"], DETAIL_SIZE)[1] + 4 if a.get("detail") else 0)
        rects = [(n["x"], n["y"], n["x"] + n["width"], n["y"] + n["height"]) for n in (by_id[m] for m in members)]
        rects += [r for inner, r, *_ in sized if inner <= members]  # sorted by size, so these are inner ones
        x0 = min(r[0] for r in rects) - pad
        y0 = min(r[1] for r in rects) - pad - top + AREA_PAD
        x1 = max(r[2] for r in rects) + pad
        y1 = max(r[3] for r in rects) + pad
        label_w = _text_size(a["label"], LABEL_SIZE)[0]
        x1 = max(x1, x0 + label_w + 40)
        sized.append((members, (x0, y0, x1, y1), a, fill, stroke))

    elements = []
    for members, (x0, y0, x1, y1), a, fill, stroke in reversed(sized):
        group = _id()
        box = _base("rectangle", x0, y0, x1 - x0, y1 - y0, backgroundColor=fill, strokeColor=stroke,
                    strokeStyle="dashed" if a.get("dashed") else "solid",
                    roundness={"type": 3}, groupIds=[group])
        label = _text(a["label"], x0 + 16, y0 + 12, LABEL_SIZE, align="left", color=stroke, anchor="topleft")
        label["groupIds"] = [group]
        elements += [box, label]
        if a.get("detail"):
            more = _text(a["detail"], x0 + 16, y0 + 14 + LABEL_SIZE * 1.25, DETAIL_SIZE, align="left",
                         color=SOFT, anchor="topleft")
            more["groupIds"] = [group]
            elements.append(more)
    return elements


def check(path):
    """Return a list of problems with an .excalidraw file (empty means fine)."""
    try:
        with open(path) as f:
            scene = json.load(f)
    except (OSError, json.JSONDecodeError) as err:
        return [f"not valid JSON: {err}"]
    if scene.get("type") != "excalidraw" or not isinstance(scene.get("elements"), list):
        return ["not an Excalidraw scene (needs type 'excalidraw' and an elements list)"]
    live = [e for e in scene["elements"] if not e.get("isDeleted")]
    ids = {e.get("id") for e in live}
    problems = []
    for e in live:
        for key in ("id", "type", "x", "y"):
            if key not in e:
                problems.append(f"element {e.get('id', '?')} is missing {key!r}")
        if e.get("containerId") and e["containerId"] not in ids:
            problems.append(f"text {e['id']} points at missing container {e['containerId']}")
        for b in e.get("boundElements") or []:
            if b.get("id") not in ids:
                problems.append(f"{e['id']} lists missing bound element {b.get('id')}")
        for side in ("startBinding", "endBinding"):
            ref = (e.get(side) or {}).get("elementId")
            if ref and ref not in ids:
                problems.append(f"arrow {e['id']} {side} points at missing {ref}")
    shapes = [e for e in live if e.get("type") in ("rectangle", "ellipse", "diamond")]
    if len(shapes) > MAX_SHAPES:
        problems.append(f"{len(shapes)} shapes: too much for one diagram (max {MAX_SHAPES}); split it")
    return problems


def preview(path, out_png):
    """Render a rough PNG (no hand-drawn wobble) so the layout can be checked by eye."""
    with open(path) as f:
        live = [e for e in json.load(f)["elements"] if not e.get("isDeleted")]
    xs, ys = [], []
    for e in live:
        if e["type"] == "arrow":  # x, y is the first point, not the corner, so use the points
            xs += [e["x"] + px for px, _ in e["points"]]
            ys += [e["y"] + py for _, py in e["points"]]
        else:
            xs += [e["x"], e["x"] + e["width"]]
            ys += [e["y"], e["y"] + e["height"]]
    ox, oy = min(xs) - 30, min(ys) - 30
    W, H = max(xs) - ox + 30, max(ys) - oy + 30
    by_id = {e["id"]: e for e in live}
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="{ox} {oy} {W} {H}">',
           f'<rect x="{ox}" y="{oy}" width="{W}" height="{H}" fill="white"/>',
           '<defs><marker id="h" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto-start-reverse">'
           '<path d="M0,0 L12,6 L0,12" fill="none" stroke="context-stroke" stroke-width="2"/></marker></defs>']
    for e in live:
        common = (f'stroke="{e["strokeColor"]}" stroke-width="{e["strokeWidth"]}" '
                  f'fill="{e["backgroundColor"] if e["backgroundColor"] != "transparent" else "none"}"'
                  + (' stroke-dasharray="8 6"' if e.get("strokeStyle") == "dashed" else ""))
        x, y, w, h = e["x"], e["y"], e["width"], e["height"]
        if e["type"] == "rectangle":
            svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" {common}/>')
        elif e["type"] == "ellipse":
            svg.append(f'<ellipse cx="{x + w / 2}" cy="{y + h / 2}" rx="{w / 2}" ry="{h / 2}" {common}/>')
        elif e["type"] == "diamond":
            svg.append(f'<polygon points="{x + w / 2},{y} {x + w},{y + h / 2} {x + w / 2},{y + h} {x},{y + h / 2}" {common}/>')
        elif e["type"] == "arrow":
            pts = " ".join(f'{x + px},{y + py}' for px, py in e["points"])
            start = ' marker-start="url(#h)"' if e.get("startArrowhead") else ""
            svg.append(f'<polyline points="{pts}" {common.replace("fill=", "data-fill=")} fill="none"'
                       f' marker-end="url(#h)"{start}/>')
    for e in live:
        if e["type"] != "text":
            continue
        family = "DejaVu Sans Mono" if e["fontFamily"] == MONO else "Comic Neue"
        size = e["fontSize"]
        lines = e["text"].split("\n")
        x, y, w = e["x"], e["y"], e["width"]
        owner = by_id.get(e.get("containerId") or "")
        if owner and owner["type"] == "arrow":
            svg.append(f'<rect x="{x - 4}" y="{y - 2}" width="{w + 8}" height="{e["height"] + 4}" fill="white"/>')
        anchor, tx = {"left": ("start", x), "right": ("end", x + w)}.get(e["textAlign"], ("middle", x + w / 2))
        for i, line in enumerate(lines):
            ly = y + size * (1.25 * i + 1.0)
            svg.append(f'<text x="{tx}" y="{ly}" font-family="{family}" font-size="{size}" '
                       f'fill="{e["strokeColor"]}" text-anchor="{anchor}" xml:space="preserve">{escape(line)}</text>')
    svg.append("</svg>")
    subprocess.run(["rsvg-convert", "-o", out_png], input="\n".join(svg).encode(), check=True)


def main(argv):
    if len(argv) == 3 and argv[1] == "--check":
        problems = check(argv[2])
        for p in problems:
            print(f"{argv[2]}: {p}", file=sys.stderr)
        return 1 if problems else 0
    if len(argv) == 4 and argv[1] == "--png":
        preview(argv[2], argv[3])
        print(f"wrote {argv[3]}")
        return 0
    if len(argv) == 3:
        with open(argv[1]) as f:
            scene = draw(json.load(f))
        with open(argv[2], "w") as f:
            json.dump(scene, f, indent=2)
        print(f"wrote {argv[2]} ({len(scene['elements'])} elements)")
        return 0
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
