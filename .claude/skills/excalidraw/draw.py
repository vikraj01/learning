#!/usr/bin/env python3
"""Draw a calm Excalidraw diagram from a tiny JSON spec.

    python3 draw.py spec.json out.excalidraw     # draw
    python3 draw.py --check file.excalidraw      # validate an existing file

Spec (everything except nodes is optional):

    {
      "direction": "right",              # or "down"; only affects default layout
      "nodes": [
        {"id": "me",  "label": "You"},
        {"id": "app", "label": "Your app", "color": "blue", "at": [1, 0]},
        {"id": "box", "label": "Container", "color": "green", "shape": "ellipse"}
      ],
      "edges": [
        {"from": "me", "to": "app", "label": "opens"},
        {"from": "app", "to": "box", "dashed": true}
      ],
      "notes": [{"text": "same app, any laptop", "at": [1, 1]}],
      "areas": [
        {"label": "Container", "nodes": ["box"], "color": "green"},
        {"label": "Your laptop", "nodes": ["me", "app", "box"]}
      ]
    }

`at` is [column, row] on a loose grid. Nodes without `at` are placed in a line
(left to right, or top to bottom with direction "down"). Colours: white
(default), blue, green, yellow, red, violet, gray. Shapes: box (default),
ellipse, diamond. `"size": "small"` makes a smaller box (good for ports).

An area is a big, softly filled box drawn behind the nodes it lists, with its
label in the top-left corner: a laptop, a container, a server. Areas can nest:
an area that lists all the nodes of another area wraps around it.
"""
import json
import random
import sys
import time

BOX_W, BOX_H = 180, 80
COL_GAP, ROW_GAP = 170, 90
FONT, FONT_SIZE, LABEL_SIZE = 1, 20, 16  # 1 = Virgil (hand-drawn)
INK = "#1e1e1e"
SOFT = "#868e96"
SMALL_W, SMALL_H = 120, 60
AREA_PAD, AREA_TOP = 30, 50  # room around the nodes, and above them for the label
COLORS = {
    "white": "#ffffff",
    "blue": "#a5d8ff",
    "green": "#b2f2bb",
    "yellow": "#ffec99",
    "red": "#ffc9c9",
    "violet": "#d0bfff",
    "gray": "#e9ecef",
}
# Areas are big, so they get the palest tint of each colour.
AREA_COLORS = {
    "white": "transparent",
    "blue": "#e7f5ff",
    "green": "#ebfbee",
    "yellow": "#fff9db",
    "red": "#fff5f5",
    "violet": "#f3f0ff",
    "gray": "#f8f9fa",
}
SHAPES = {"box": "rectangle", "rectangle": "rectangle", "ellipse": "ellipse", "diamond": "diamond"}
MAX_SHAPES, MAX_WORDS = 10, 4

_rng = random.Random(7)


def _id():
    return "".join(_rng.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(12))


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


def _text_size(text, size):
    lines = text.split("\n")
    return max(len(l) for l in lines) * size * 0.55, len(lines) * size * 1.25


def _wrap(text, size, max_w):
    """Break text onto lines that fit max_w, at spaces only."""
    lines = []
    for word in text.split():
        if lines and _text_size(f"{lines[-1]} {word}", size)[0] <= max_w:
            lines[-1] += f" {word}"
        else:
            lines.append(word)
    return "\n".join(lines)


def _text(text, cx, cy, size, container=None, color=INK):
    w, h = _text_size(text, size)
    return _base(
        "text", cx - w / 2, cy - h / 2, w, h, strokeColor=color,
        text=text, originalText=text, fontSize=size, fontFamily=FONT,
        textAlign="center", verticalAlign="middle", containerId=container,
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


def draw(spec):
    nodes = spec.get("nodes") or []
    if not nodes:
        sys.exit("spec needs at least one node")
    down = spec.get("direction") == "down"
    elements, by_id = [], {}

    for i, n in enumerate(nodes):
        col, row = n.get("at") or ((0, i) if down else (i, 0))
        small = n.get("size") == "small"
        w, h, size = (SMALL_W, SMALL_H, LABEL_SIZE) if small else (BOX_W, BOX_H, FONT_SIZE)
        # Small boxes sit centred in their grid cell, so rows and columns still line up.
        x = col * (BOX_W + COL_GAP) + (BOX_W - w) / 2
        y = row * (BOX_H + ROW_GAP) + (BOX_H - h) / 2
        color = n.get("color", "white")
        if color not in COLORS:
            sys.exit(f"node {n['id']}: unknown color {color!r}; use one of {', '.join(COLORS)}")
        shape = SHAPES.get(n.get("shape", "box"))
        if not shape:
            sys.exit(f"node {n['id']}: unknown shape {n['shape']!r}; use box, ellipse or diamond")
        box = _base(shape, x, y, w, h, backgroundColor=COLORS[color],
                    roundness={"type": 3} if shape == "rectangle" else {"type": 2})
        text = _wrap(n["label"], size, w - 30)
        if _text_size(text, size)[0] > w - 20:
            sys.exit(f"node {n['id']}: a word in {n['label']!r} is too long for a box; shorten it")
        label = _text(text, x + w / 2, y + h / 2, size, container=box["id"])
        box["boundElements"].append({"type": "text", "id": label["id"]})
        elements += [box, label]
        by_id[n["id"]] = box

    for e in spec.get("edges") or []:
        a, b = by_id.get(e["from"]), by_id.get(e["to"])
        if not a or not b:
            sys.exit(f"edge {e['from']} -> {e['to']}: unknown node id")
        bx, by = b["x"] + b["width"] / 2, b["y"] + b["height"] / 2
        ax, ay = a["x"] + a["width"] / 2, a["y"] + a["height"] / 2
        sx, sy = _edge_point(a, bx, by)
        ex, ey = _edge_point(b, ax, ay)
        arrow = _base(
            "arrow", sx, sy, abs(ex - sx), abs(ey - sy),
            strokeStyle="dashed" if e.get("dashed") else "solid",
            roundness={"type": 2}, points=[[0, 0], [ex - sx, ey - sy]],
            lastCommittedPoint=None, startArrowhead=None, endArrowhead="arrow",
            startBinding={"elementId": a["id"], "focus": 0, "gap": 8},
            endBinding={"elementId": b["id"], "focus": 0, "gap": 8},
        )
        a["boundElements"].append({"type": "arrow", "id": arrow["id"]})
        b["boundElements"].append({"type": "arrow", "id": arrow["id"]})
        elements.append(arrow)
        if e.get("label"):
            label = _text(e["label"], (sx + ex) / 2, (sy + ey) / 2, LABEL_SIZE, container=arrow["id"])
            arrow["boundElements"].append({"type": "text", "id": label["id"]})
            elements.append(label)

    for note in spec.get("notes") or []:
        col, row = note.get("at", [0, 1])
        cx = col * (BOX_W + COL_GAP) + BOX_W / 2
        cy = row * (BOX_H + ROW_GAP) + BOX_H / 2
        elements.append(_text(note["text"], cx, cy, LABEL_SIZE, color=SOFT))

    return {
        "type": "excalidraw", "version": 2, "source": "https://excalidraw.com",
        "elements": _areas(spec.get("areas") or [], by_id) + elements,
        "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None},
        "files": {},
    }


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
        color = a.get("color", "white")
        if color not in AREA_COLORS:
            sys.exit(f"area {a['label']!r}: unknown color {color!r}; use one of {', '.join(AREA_COLORS)}")
        rects = [(n["x"], n["y"], n["x"] + n["width"], n["y"] + n["height"]) for n in (by_id[m] for m in members)]
        rects += [r for inner, r, *_ in sized if inner < members]
        x0 = min(r[0] for r in rects) - AREA_PAD
        y0 = min(r[1] for r in rects) - AREA_TOP
        x1 = max(r[2] for r in rects) + AREA_PAD
        y1 = max(r[3] for r in rects) + AREA_PAD
        sized.append((members, (x0, y0, x1, y1), a, color))

    elements = []
    for members, (x0, y0, x1, y1), a, color in reversed(sized):
        group = _id()
        box = _base("rectangle", x0, y0, x1 - x0, y1 - y0, backgroundColor=AREA_COLORS[color],
                    roundness={"type": 3}, groupIds=[group])
        w, h = _text_size(a["label"], FONT_SIZE)
        label = _text(a["label"], x0 + 16 + w / 2, y0 + 12 + h / 2, FONT_SIZE, color=SOFT)
        label["groupIds"] = [group]
        label["textAlign"] = "left"
        elements += [box, label]
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
        problems.append(f"{len(shapes)} shapes: too busy for a calm diagram (max {MAX_SHAPES}); split it")
    for e in live:
        if e.get("type") == "text" and e.get("containerId") in {s["id"] for s in shapes}:
            if len(e.get("text", "").split()) > MAX_WORDS:
                problems.append(f"box label {e['text']!r} is long; keep it to {MAX_WORDS} words")
    return problems


def main(argv):
    if len(argv) == 3 and argv[1] == "--check":
        problems = check(argv[2])
        for p in problems:
            print(f"{argv[2]}: {p}", file=sys.stderr)
        return 1 if problems else 0
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
