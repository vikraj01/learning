# Progress log

Newest first. Each entry: date, what was done, where things stand, what's next. Keep entries to a few lines.

<!-- entries below -->

## 2026-10-21: message-box project

- Done: `docs/02-message-app/` with 5 pages (the app → Dockerfile → containers forget → bind mount → volume), `message-box/` (app.js + Dockerfile) and 2 diagrams (`app-flow`, `where-messages-live`). Linked from `docs/README.md`. Every command verified here (local run, build, stop/start vs rm, bind mount, volume).
- Next: Vikash's feedback; Tanvi works through it today.

## 2026-10-21: first real commit, pushed; Tanvi invited

- Done: everything committed and pushed to `vikraj01/learning` (public). New rule: always commit + push. Collaborator invite sent to `Tanvikanwar23` (an earlier invite to the wrong account `TanviKanwar` was cancelled).
- Next: Tanvi accepts the invite; Vikash's feedback on the Docker pages.

## 2026-10-20: Vikash hand-edited image-and-containers.excalidraw

- Same boxes and labels, layout tweaked in VS Code. Do not regenerate it from the spec; edit the JSON in place if it needs changes.

## 2026-10-20: commands cheat sheet

- Done: `docs/01-docker/commands.md` (every command by page, plus a cleanup block) and `docs/01-docker/files/` (`my-site/` nginx Dockerfile, `my-site-python/` six-line Dockerfile, each with `index.html`). Linked from `docs/README.md`.
- Next: Vikash's feedback.

## 2026-10-20: bind mounts vs volumes

- Done: page 05 is now `05-bind-mounts.md` (fixed: it used to call bind mounts "volume mounts"); new `06-volumes.md` (containers forget on `rm` but not on `stop`, named volumes survive, two containers sharing one volume, bind vs volume table) + `shared-volume.excalidraw`. Diagram `volume-mount` renamed `bind-mount`. Dockerfile pages now 07–08. All demos verified.
- State: Docker set is 8 pages + 6 diagrams.
- Next: Vikash's feedback.

## 2026-10-20: images page

- Done: new `docs/01-docker/03-what-is-an-image.md` + `inside-an-image.excalidraw` (layers stacked inside a blue image area). Old pages 03–06 renumbered to 04–07; all links and `docs/README.md` updated. Commands verified (alpine `ls /`, note.txt read-only demo, nginx vs nginx:alpine sizes).
- State: Docker set is 7 pages + 5 diagrams, waiting on Vikash's review.
- Next: Vikash's feedback.

## 2026-10-20: container-as-a-box diagrams

- Done: `draw.py` gained areas (nested, labelled boxes) and small nodes. Redrew `port-mapping` and `volume-mount` with the container as a box inside the laptop. Previewed both as PNGs to check the layout.
- State: the image-and-containers and build-and-run diagrams are unchanged (no inside/outside idea in them).
- Next: Vikash reviews them in VS Code.

## 2026-10-20: Docker pages written

- Done: `docs/README.md` + `docs/01-docker/` pages 01–06 and 4 diagrams (image-and-containers, port-mapping, volume-mount, build-and-run). Every command was run here (Docker 29.6.1) and its output checked. `draw.py` now wraps long box labels and leaves wider gaps for arrow labels.
- State: waiting for Vikash to review the pages and diagrams. Unknown: Tanvi's OS and whether Docker is installed on her machine (page 04 has a PowerShell note for `$(pwd)`).
- Next: Vikash's feedback → adjust pages, and `teaching-style.md` / `excalidraw-style.md` if the style changes.
- Also: CLAUDE.md now describes the `docs/` layout (topic folders, numbered pages, diagrams beside pages).

## 2026-10-20: repo setup

- Done: CLAUDE.md, `context/` (about, teaching-style, excalidraw-style, decisions, progress), `.claude/` (bypass mode, hooks, skills `/sync-context` `/write-doc` `/excalidraw`, plugins). Hooks and `draw.py` (draw + `--check`) tested.
- State: no `docs/` yet. `plan/plan.md` has the topic list.
- Next: Vikash adds notes/feelings to `plan/`; then `/sync-context`.
