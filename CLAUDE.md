# learning

Vikash is teaching **Tanvi**, Vikash's sister, tech from the basics, slowly. This repo is where they plan it and where her study material will live.

Read `context/README.md` first. It indexes everything Claude needs to know and is kept up to date as we go.

## Who's who

- **Vikash**: the teacher, and the person talking to Claude. Writes informally and fast; answer the intent.
- **Tanvi**: the learner. She reads what ends up in `docs/`. Everything written for her follows `context/teaching-style.md`.

## Layout

- `plan/`: Vikash's own notes, feelings and ideas about what to teach and how. **Vikash's space.** Read it closely; don't rewrite it unless asked.
- `context/`: notes for Claude. Who Tanvi is, how to teach her, decisions made, and a progress log. Claude owns these and keeps them current.
- `docs/`: study material for Tanvi, one folder per topic (`01-docker/`), pages numbered in reading order, diagrams next to the pages. `docs/README.md` is her index. New pages only when Vikash asks.
- `.claude/`: skills, hooks and settings for this repo.

## How to work here

- **Go slow. One step at a time.** Do only what was asked. Don't create lessons, docs or extra files ahead of time, and don't jump to later topics (Kubernetes etc.) before Vikash gets there.
- **Keep context fresh.** When Vikash shares something about Tanvi, the plan, or how to teach her, record it in the right `context/` file in the same turn. Log real work in `context/progress.md`. `/sync-context` does a full pass.
- **Diagrams are Excalidraw, and calm.** Use `/excalidraw`: write a tiny spec and let the script draw it. Never hand-write `.excalidraw` JSON. Few boxes, soft colours, short words. Vikash edits them afterwards in VS Code (Excalidraw extension is installed).
- **Always commit and push.** After every piece of work (a page, a diagram, a context update), commit it with a short clear message and `git push` to `origin main`. Don't leave changes uncommitted at the end of a turn.
- Hands-on work uses local tools only: `python3`/`uv`, `docker`, and a local `kind` cluster when we get to Kubernetes.

## Skills

- `/sync-context`: read `plan/` and recent changes, update `context/`.
- `/write-doc`: write one study page for Tanvi (only when asked).
- `/excalidraw`: draw a simple, calm diagram from a small spec.

## Hooks

- **SessionStart** prints the latest progress and any `plan/` notes changed since context was last updated.
- **Stop** asks Claude (once) to update `context/` if `plan/`, `docs/` or `.claude/` changed since the progress log.
- **PostToolUse** checks every `.excalidraw` file written or edited (valid JSON, bindings, not too busy).
