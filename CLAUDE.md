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
- `python-dsa/`: Python from zero via 50 easy problems: `notebooks/` (one Jupyter notebook per lesson: theory, runnable cells, tasks, quiz via `checks.py`; `make` inside it, or `make notebooks` from the root, opens them), `learn/` lessons 1–17 + `examples/`, `leetcode-list.md`, and two PDFs built with `make pdf`. Not part of the MkDocs site.
- `labs/`: Docker Labs, a local KodeKloud-style site (React + TypeScript, Express) with a task, file editor, real terminal and Check button. `make labs` → http://localhost:7000. One folder per lab in `labs/content/` (`lab.json`, `task.md`, `starter/`, `setup.sh`, `check.sh`, `cleanup.sh`). See `labs/README.md`.
- `.claude/`: skills, hooks and settings for this repo.
- `mkdocs.yml`, `pyproject.toml`, `Makefile`: the docs site. `make serve` opens `docs/` at http://localhost:8000 (MkDocs Material, installed with uv).

## How to work here

- **Every `.md` in `docs/` is wired, always** (Vikash's rule). In the same turn a page is created, renamed or moved: add it to `nav` in `mkdocs.yml` (in reading order, under its section) and link it from `docs/README.md`. Fix any links to the old path. The Stop hook `check-nav.sh` blocks until this is done.
- **Go slow. One step at a time.** Do only what was asked. Don't create lessons, docs or extra files ahead of time, and don't jump to later topics (Kubernetes etc.) before Vikash gets there.
- **Keep context fresh.** When Vikash shares something about Tanvi, the plan, or how to teach her, record it in the right `context/` file in the same turn. Log real work in `context/progress.md`. `/sync-context` does a full pass.
- **Diagrams are Excalidraw, and they explain properly.** Use `/excalidraw`: write a spec and let the script draw it, then look at the PNG preview before saving. Never hand-write `.excalidraw` JSON. A title stating the point, real details (IPs, ports, names), numbered steps, ✓/✗ paths, a short explanation note, the commands. Vikash dislikes thin, minimal diagrams. Vikash edits them afterwards in VS Code (Excalidraw extension is installed).
- **Always commit and push.** After every piece of work (a page, a diagram, a context update), commit it with a short clear message and `git push` to `origin main`. Don't leave changes uncommitted at the end of a turn.
- Hands-on work uses local tools only: `python3`/`uv`, `docker`, and a local `kind` cluster when we get to Kubernetes.

## Skills

- `/sync-context`: read `plan/` and recent changes, update `context/`.
- `/write-doc`: write one study page for Tanvi (only when asked).
- `/excalidraw`: draw a detailed, explaining diagram from a spec, and preview it.

## Hooks

- **SessionStart** prints the latest progress and any `plan/` notes changed since context was last updated.
- **Stop** blocks (once) if any `docs/**/*.md` is missing from `mkdocs.yml` nav or `docs/README.md` (`check-nav.sh`), and asks Claude (once) to update `context/` if `plan/`, `docs/` or `.claude/` changed since the progress log.
- **PostToolUse** checks every `.excalidraw` file written or edited (valid JSON, bindings, at most 60 shapes).
