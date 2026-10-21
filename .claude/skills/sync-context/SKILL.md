---
name: sync-context
description: Read Vikash's notes in plan/ and recent changes, then bring context/ up to date (about Tanvi, teaching style, decisions, progress). Use when plan/ changed, when Vikash shares feelings or ideas about teaching Tanvi, at the start of a session flagged by the SessionStart hook, or when asked to "update context".
---

# Sync context

`context/` is Claude's memory for this repo. It should always reflect what Vikash has said, so any future session can pick up without re-asking.

## Steps

1. Read `context/README.md` and the `## <date>` entry at the top of `context/progress.md` to know what's already recorded.
2. Find what's new:
   ```bash
   find plan docs -type f -newer context/progress.md 2>/dev/null
   git status --short
   git diff -- plan/
   ```
   Read every changed file in `plan/` in full. Also use anything Vikash said in this conversation.
3. Sort each new fact into one place:
   - about Tanvi (what she knows, likes, struggles with, her setup) → `about.md`
   - how to write or explain for her → `teaching-style.md`
   - diagram preferences → `excalidraw-style.md`
   - a choice (topic order, tool, scope, tone) → `decisions.md`, dated, newest first
4. Edit in place. Replace stale lines; don't append contradictions. Keep files short.
5. Refresh "Current state" in `context/README.md`.
6. Add an entry to the top of `context/progress.md` (below the `<!-- entries below -->` marker): date, done, state, next. Two to four lines.

## Rules

- `plan/` is Vikash's. Read it; don't edit it unless asked.
- Record what Vikash actually said. If something is unclear (for example what Tanvi already knows), write it as an open question in the relevant file and ask Vikash at the end, in one short line.
- Tell Vikash in two or three lines what you updated.
