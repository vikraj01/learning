---
name: excalidraw
description: Draw a simple, calm Excalidraw diagram (.excalidraw) for Tanvi's study pages, from a tiny spec, using this repo's draw.py script. Use whenever a diagram, drawing, sketch or picture is wanted. Never hand-write Excalidraw JSON.
---

# Calm Excalidraw diagrams

Read `context/excalidraw-style.md` first; it holds Vikash's preferences and wins over anything here.

## Steps

1. **Decide the one thing** the diagram shows, in one sentence. If it's two things, make two diagrams.
2. **Write a tiny spec** in the scratchpad (not the repo): 3–7 nodes, 1–3 words each, arrows labelled with a verb.
   ```json
   {
     "nodes": [
       {"id": "code", "label": "Your code"},
       {"id": "image", "label": "Image", "color": "blue"},
       {"id": "box", "label": "Container", "color": "green"}
     ],
     "edges": [
       {"from": "code", "to": "image", "label": "build"},
       {"from": "image", "to": "box", "label": "run"}
     ],
     "notes": [{"text": "one recipe, many boxes", "at": [1, 1]}]
   }
   ```
   - Layout: nodes go left → right by default. `"direction": "down"` stacks them. Use `"at": [col, row]` only when a node must sit somewhere specific (a second row, a fork).
   - Colours: `white` (default), `blue`, `green`, `yellow`, `red`, `violet`, `gray`. Colour only what matters; same kind of thing, same colour.
   - Shapes: `box` (default), `ellipse`, `diamond`. Boxes are almost always right.
   - Edges: `label` (optional), `"dashed": true` for "sometimes" or "optional".
   - `"size": "small"` on a node makes a smaller box. Use it for ports ("doors").
   - **Areas show where things live**: a big, pale box drawn behind the nodes it lists, with its label top-left. Nest them: an area listing all of another area's nodes wraps around it.
     ```json
     "areas": [
       {"label": "Container", "nodes": ["port80", "nginx"], "color": "green"},
       {"label": "Your laptop", "nodes": ["browser", "port8080", "port80", "nginx"], "color": "gray"}
     ]
     ```
   - Notes take fractional rows (`"at": [1, 0.85]`) to sit close under an area.
3. **Draw it:**
   ```bash
   python3 -I .claude/skills/excalidraw/draw.py <spec.json> <out.excalidraw>
   ```
   The PostToolUse hook and `draw.py --check <file>` validate files: JSON, bindings, at most 10 shapes, box labels at most 4 words.
4. **Save next to the page that uses it**, named after what it shows (`build-and-run.excalidraw`).
5. **Tell Vikash the path.** Vikash opens it in VS Code (Excalidraw extension) to nudge positions, colours or wording.

## Editing an existing diagram

- If Vikash has tweaked a file by hand, **don't regenerate it**; that would throw away those changes. Make small edits to the JSON instead (change a `text`/`originalText`, a `backgroundColor`), then run `--check`.
- If it was never hand-edited and needs real changes, edit the spec and redraw.

## Don't

- No more than 10 shapes, no paragraphs in boxes, no decorative icons, no crossing arrows, no rainbow colours.
