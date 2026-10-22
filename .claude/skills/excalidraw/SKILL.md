---
name: excalidraw
description: Draw a detailed, explaining Excalidraw diagram (.excalidraw) for Tanvi's study pages from a JSON spec, using this repo's draw.py script, and check it with a PNG preview. Use whenever a diagram, drawing, sketch or picture is wanted. Never hand-write Excalidraw JSON.
---

# Explaining Excalidraw diagrams

Read `context/excalidraw-style.md` first; it holds Vikash's preferences and wins over anything here. Vikash disliked the old minimal diagrams ("very light"): a diagram should teach on its own.

## Steps

1. **Decide the point** in one sentence. That becomes the title.
2. **Write the spec** in the scratchpad. The full format is in the docstring at the top of `draw.py`. The parts that make a diagram explain:
   - `title` + `subtitle`: the point, and one line of context.
   - Nodes with `label` (the name) and `detail` (IP, port, image, what it does; `\n` between lines). Place them with `pos: [x, y]` in pixels for anything beyond a simple row.
   - `areas` for where things live (container / network / "Your laptop"), with a `detail` line. Areas nest automatically.
   - `edges` with `label`, `step` (numbered badge), `color` (`green` works ✓, `red` + `dashed` fails ✗), `via` bend points to route around boxes, `both` for a question-and-answer arrow.
   - `notes`: `style: "callout"` (yellow, the "aha" in 2–3 sentences, set `w`) and `style: "code"` (the commands).
   Worked examples: `.claude/skills/excalidraw/specs/04-networking/`.
3. **Draw and check:**
   ```bash
   python3 -I .claude/skills/excalidraw/draw.py <spec.json> <out.excalidraw>
   python3 -I .claude/skills/excalidraw/draw.py --png <out.excalidraw> <preview.png>
   ```
   **Look at the preview** (Read the PNG). Fix overlaps, labels squeezed between close boxes, arrows crossing labels or leaving their area, notes sitting on area borders. Redraw until it's clean. The preview uses a stand-in font, so leave a little spare room in boxes.
4. **Save next to the page** that uses it, named after what it shows (`own-network.excalidraw`). Save the spec in `.claude/skills/excalidraw/specs/<section>/`.
5. **Tell Vikash the path.** Vikash opens it in VS Code (Excalidraw extension) to adjust it.

The PostToolUse hook runs `draw.py --check` on every `.excalidraw` written: valid JSON, bindings, at most 60 shapes.

## Editing an existing diagram

- If Vikash has tweaked a file by hand, **don't regenerate it**; that would throw away those changes. Make small edits to the JSON instead (change a `text`/`originalText`, a `backgroundColor`), then run `--check`.
- If it was never hand-edited and needs real changes, edit the spec and redraw.

## Don't

- No crossing arrows, no overlapping text, no decorative icons, no colours without a meaning.
- Don't cram two ideas into one diagram; make two.
