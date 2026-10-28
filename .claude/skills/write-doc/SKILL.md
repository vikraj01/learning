---
name: write-doc
description: Write one study page for Tanvi in docs/, on a topic Vikash names, following the teaching style in context/. Use only when Vikash asks for a doc, page, lesson or notes for Tanvi. Never create pages ahead of time.
---

# Write a study page for Tanvi

## Before writing

1. Read `context/README.md`, `context/about.md`, `context/teaching-style.md` and `context/decisions.md`.
2. Read the relevant notes in `plan/`, and list existing pages in `docs/` so you build on what she's already seen and don't repeat it.
3. If the scope is unclear (how deep, what she knows already), ask Vikash one short question before writing.

## The page

- Path: `docs/<NN>-<topic>/<NN>-<slug>.md`, numbered in the order she'll read them (for example `docs/01-docker/01-what-is-a-container.md`). Create the folder only when the first page in it is written.
- Shape (adapt, don't pad):
  1. `# Title` and one line on what she'll be able to do after.
  2. A real-life comparison she already knows.
  3. The idea, in plain words. New terms in **bold** and explained right there.
  4. **Try it**: one small thing to type or do, with the exact output she should see.
  5. A diagram if it helps: draw it with `/excalidraw` into the same folder and link it (`[diagram](./<name>.excalidraw)`).
  6. **Check yourself**: 2–3 tiny questions.
  7. **Next**: one line on what comes after.
- Verify every command and its output by running it here before putting it in the page.
- Target ~10 minutes of reading and doing.

## After

- **Wire it**: add the page to `nav` in `mkdocs.yml` and link it from `docs/README.md`, every time. No page in `docs/` is ever left unwired.
- Tell Vikash the path and a two-line summary. Vikash will review and adjust.
- Log it in `context/progress.md`. If the feedback changes the style, update `context/teaching-style.md`.
