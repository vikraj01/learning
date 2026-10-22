# Decisions

Choices Vikash has made. Newest first. One line each, with the date.

- 2026-10-22: **Diagrams must explain, not just decorate.** Vikash hated the minimal "calm" diagrams ("very light"). New standard in `excalidraw-style.md`; `draw.py` rewritten (titles, detail lines, pixel layout, numbered steps, ✓/✗ arrows, callouts, code boxes, `--png` preview). Older diagrams in sections 1–3 are still the old style.
- 2026-10-22: Section 4 `docs/04-networking/`: a **new example**, not producer/consumer again (Vikash: "dont' repeate the same example"). busybox boxes for pages 1–2 (default network vs own network, DNS, alias, connect), then a visit counter: Node `web` + Redis `db` on `counter-net`, `db` private (no `-p`). Page 4 = which address from where + the three mistakes (localhost, laptop port, wrong network). `demo.sh` runs the whole thing step by step for Vikash to show.
- 2026-10-22: Section 3 `docs/03-two-apps/`: producer (message-box copy, port 3000) + consumer (`/read`, port 4000), JavaScript. Sharing order as Vikash said it: volume first, then bind mount. Container names match image names (`producer`, `consumer`).
- 2026-10-21: `docs/` is also a MkDocs Material site, set up with uv (`pyproject.toml`, `uv.lock`) and a `Makefile` (`make serve` / `build` / `clean`). Explicit `nav` in `mkdocs.yml`; MkDocs pinned `<2`. `site/` is gitignored.
- 2026-10-21: Message-box project (`docs/02-message-app/`): a JavaScript app (Node + Express, not Python; Vikash asked for JS). `GET /web` returns an HTML form, `POST /send` appends to `data/messages.txt`. Then a 5-line Dockerfile, explained one sentence per line with the line count (no deep detail yet), then ephemeral containers → bind mount → volume, all with this app. Port 3000. JavaScript is the main version; a Python (Flask) twin sits alongside as page 7, same port and data path.
- 2026-10-21: Always commit and push after each piece of work (rule in `CLAUDE.md`). Tanvi (GitHub `Tanvikanwar23`) invited as a collaborator on `vikraj01/learning`.
- 2026-10-20: Storage is two pages: bind mounts (her own folder, live edits), then volumes (containers aren't persistent, named volumes persist and can be shared). Call them "bind mount" and "volume", never "volume mount".
- 2026-10-20: Images get their own page (Vikash: "important concept"), right after run: what's inside (Linux files, program, start command), layers, read-only, name:tag, pull/images/rmi.
- 2026-10-20: Docker order: what it is (image vs container) → run (hello-world, nginx) → what is an image → port mapping → volumes → Dockerfile + build → Dockerfile instructions. Build comes after Dockerfile, not before. One running example throughout: her own `index.html` served by nginx. No Python needed for Docker.
- 2026-10-20: Go slow. Set up the repo first; no docs until Vikash adds notes to `plan/`.
- 2026-10-20: Study material goes in `docs/`; Vikash's own thinking stays in `plan/`.
- 2026-10-20: Diagrams in Excalidraw, editable by Vikash afterwards. ("Simple and calm" replaced on 2026-10-22, see above.)
- 2026-10-20: Claude runs in bypass-permissions mode in this repo.
- 2026-10-20 (from `plan/plan.md`): topics are Python, apps/servers/React/web, Docker, Kubernetes. Start with Docker: build & run, Dockerfile, port mapping, volumes.
