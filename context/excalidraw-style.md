# Excalidraw diagrams: explaining, not decorative

The goal: a diagram that **teaches on its own**. Tanvi should be able to look at it without the page and still understand what happens, where, and why.

Changed 2026-10-22. Vikash on the old "calm" diagrams (3–7 boxes, 1–3 words): "very light ... don't like those excalidraws ... i hate that ... do this properly". So the old minimal style is out.

## What every diagram has

- **A title that states the point**, as a sentence ("The default network: numbers work, names don't"), plus a one-line subtitle.
- **Real details on the boxes**: a name in big text, and detail lines under it (IP address, port it listens on, image, "no -p: private", what `localhost` means there).
- **Where things live**: containers inside network areas inside a grey "Your laptop" area (from Vikash's 2026-10-20 tweak). Areas carry a detail line too ("made with: docker network create lab").
- **Numbered steps** (badges 1, 2, 3...) when something happens in order, like a request going browser → door → app → database → back.
- **What works and what fails**: green arrows with ✓, red dashed arrows with ✗ and the reason ("✗ not on 'lab'", "✗ that's web itself").
- **An explanation note** (yellow callout) with the "aha" in two or three sentences.
- **The commands** that produce what's drawn (grey code box), when there are commands.

## Colours (meaning, not decoration)

- Containers: green. Docker DNS / helpers: violet. Ports ("doors"): small yellow boxes. Networks: blue areas. Laptop: grey area. Folder: yellow, volume: blue (as in the storage diagrams).
- Arrows: green = works, red dashed = fails, violet = DNS lookups, black = ordinary flow.

## Still true

- One diagram explains one thing. Rich is fine; muddled isn't: no crossing arrows, nothing overlapping, labels readable.
- Hand-drawn look (Virgil font, roughness 1) so Vikash can edit it in VS Code.

## How

Draw with `/excalidraw`: a JSON spec → `.claude/skills/excalidraw/draw.py`. Never hand-write the JSON. **Always render the preview** (`draw.py --png`) and look at it before saving into `docs/`; fix overlaps first. Keep the spec in `.claude/skills/excalidraw/specs/<section>/` so it can be redrawn.

## Vikash's tweaks

- 2026-10-22: **Diagrams must explain properly** (see top). Minimal "calm" diagrams are disliked.
- 2026-10-20: **Show the container as a box.** When a diagram is about what's inside vs outside a container (ports, volumes, networks), draw the container as its own green area inside a grey "Your laptop" area, so it reads as a separate little machine. Ports are small yellow "door" boxes, one on each side of the edge. Plain arrows between floating boxes were "weak" for this.
