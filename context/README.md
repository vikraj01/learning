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
- Python for LeetCode, in `python-dsa/` (root, outside the site): 11 learn pages + examples, 50 easy problems in 7 stages with solutions. Index `python-dsa/README.md`, problem list `python-dsa/practice/README.md`.
