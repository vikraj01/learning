# Context index

Notes for Claude. Read this first, then whichever file the task needs. Keep each file short and current: replace stale lines rather than piling on.

| File | What's in it |
| --- | --- |
| `about.md` | Why this repo exists, who Tanvi is, what she already knows. |
| `teaching-style.md` | How to write and explain for Tanvi. |
| `excalidraw-style.md` | What a good (detailed, explaining) diagram looks like here. |
| `decisions.md` | Choices Vikash has made (order of topics, tools, tone). |
| `progress.md` | Log of what's been done, newest first. |

## Current state

- Setup done (CLAUDE.md, context/, .claude/).
- Topic order from `plan/plan.md`: Python → apps/servers/React/web → Docker → Kubernetes. Starting with **Docker**.
- Docker pages 01–08 + 6 diagrams written in `docs/01-docker/`; waiting on Vikash's review.
- Message-box project (JS app + Docker + storage), 9 pages in `docs/02-message-app/` (latest: 09 go inside a container).
- Producer/consumer project, 3 pages in `docs/03-two-apps/`: two apps sharing data via a volume, then a bind mount.
- Networking, 4 pages in `docs/04-networking/` (visit counter: Node + Redis) + `demo.sh`. First section with the new detailed diagram style.
- Layers, 5 pages in `docs/05-layers/`. Networking fundamentals, 6 pages in `docs/06-how-networking-works/` + `demo.sh`. Compose project (todo app: nginx + Node API + Postgres), 5 pages in `docs/07-compose/` + `demo.sh`.
- Python notebooks in `python-dsa/notebooks/` (theory + run + tasks + quiz): all 22 done (hard lessons split in two), plus strong practice sets `P1`–`P6` (checkpoints after 05, 09, 12, 16, 22, and mini projects). Waiting on Vikash's review. `make` in `python-dsa/notebooks/` (or `make notebooks` at the root) starts Jupyter.
- Python for LeetCode, in `python-dsa/` (root, outside the site): lessons 1–10 + examples, two PDFs (`python-for-leetcode.pdf`, `leetcode-list.pdf` = exactly 50 easy problems). `make pdf` rebuilds them.
- Sections 9–14 (one topic each, same `greet` app): `09-env/` (4 pages: env in Node, the `.env` file, env in Docker, `.env` + Docker), `10-tags/`, `11-cmd/`, `12-entrypoint/`, `13-build-f/`, `14-compose/`. Section 14 is now 4 pages + `commands.md` (greet, `${...}` from `.env`, notes app with two networks, WordPress). Waiting on Vikash's review. Next lesson he named: busybox and raw stuff (not started).
- Docker Labs (`labs/`): 28 labs in 8 tracks, up to Compose (16–28 added 2026-10-28, not yet played through).
