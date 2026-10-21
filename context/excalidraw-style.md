# Calm Excalidraw diagrams

The goal: a diagram Tanvi understands in five seconds, and Vikash can tweak in the editor.

- **3–7 boxes.** Hard cap 10. If it needs more, split it into two diagrams.
- **1–3 words per box.** Detail goes in the page text, not the drawing.
- **Flow left → right** (or top → bottom). One direction per diagram.
- **Soft colours, used for meaning.** Same kind of thing = same colour. Most boxes plain white; colour only what matters.
- **Arrow labels are verbs**, one or two words ("sends", "runs on").
- **One small note at most**, for the "aha" bit.
- Hand-drawn look (roughness 1), normal stroke width, rounded boxes, lots of space.

Draw with `/excalidraw` (spec → `.claude/skills/excalidraw/draw.py`). Never hand-write the JSON.

## Vikash's tweaks

- 2026-10-20: **Show the container as a box.** When a diagram is about what's inside vs outside a container (ports, volumes, networks), draw the container as its own green area inside a grey "Your laptop" area, so it reads as a separate little machine. Ports are small yellow "door" boxes, one on each side of the edge. Plain arrows between floating boxes were "weak" for this.
