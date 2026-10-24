# Progress log

Newest first. Each entry: date, what was done, where things stand, what's next. Keep entries to a few lines.

<!-- entries below -->

## 2026-10-24: networking redo, planned (no pages yet)

- Vikash asked how a container reaches a database on the host, and laid out the order to teach networking to Tanvi again (see `decisions.md`). Explained in chat, with a step-by-step outline built on the message box.
- Tested on this laptop: Docker here is **rootless** (rootlesskit, `--disable-host-loopback`), so `host-gateway` (172.17.0.1) does **not** reach the real host; the laptop's LAN IP (192.168.1.18) does, if the server listens on `0.0.0.0`. Normal (rootful) Docker and Docker Desktop behave as the textbook says. Check which one Tanvi runs before writing pages.
- Explainer for Vikash himself (not Tanvi): https://claude.ai/artifact/7zxDgDJPBaziv8dkTPukuE. v1 (one long page) was rejected as too thin and too advanced; v2 has 12 tabs, starting on the Linux laptop (interfaces, ports lab, DNS path nsswitch → /etc/hosts → 127.0.0.53 systemd-resolved → 8.8.8.8 with TTL, loopback), then the container, bridge, own network + Docker DNS 127.0.0.11, host DB, host, none, cheat sheet, Tanvi plan. All outputs from this laptop.
- v3 rewrote the bridge tab (switch, veth, IPAM, ARP, masquerade, DNS, IP churn, nsenter into rootlesskit). Vikash: still "so unhelpful, I gave up". Long, dense pages aren't working for him; next time ask what exactly is unclear and teach in small chat steps.
- What Vikash actually wanted: a **teaching script** built on the message box, simple, no `ip addr`, no env vars. Made https://claude.ai/artifact/4cGJqJC3XP3sTPC3iSAxEZ: one new route `/friend` (bob fetches `http://alice:8080/messages`), then default network ✗ → own network `family` ✓ → carol on `other` ✗ → alice on the laptop with `--add-host=alice:host-gateway` ✓ → host → none. Each tab = Say / She types / She sees + a house picture. Not yet run end to end; `/friend` not yet added to `app.js`.
- Lesson for explainers: start from the basics on the machine itself, go deep and detailed, split into tabs; never open with the advanced answer.
- Next: Vikash decides on the `box` + `store` example and whether this replaces section 4 or becomes a new section.

## 2026-10-24: practice list made truly beginner-level

- Vikash: the 50 "were not easy". LeetCode Easy (Two Sum, Roman to Integer, Single Number…) is too hard for a first-time programmer.
- Done: new 50 in `leetcode-list.md` / `.pdf`: 35 GeeksforGeeks problems (its "Basic" level, plus 6 from its Python practice set) and 15 LeetCode problems with ≥85% acceptance. Names and links generated from the sites' own APIs. Stages: 8 / 9 / 7 / 17 / 3 / 6 (after lessons 5–10). Rule for future lists: pick by measured easiness (GfG Basic, LeetCode acceptance ≥85%), not by the "Easy" label.
- Next: Vikash's review.

## 2026-10-24: Python for LeetCode → two PDFs

- Done: `python-dsa/` with lessons 1–10 (+ examples) and two PDFs built by `make pdf` (`python-dsa/pdf/build.py`, Markdown → HTML → headless Chrome): `python-for-leetcode.pdf` (84 pages) and `leetcode-list.pdf` (50 easy problems, 6 stages matching lessons 5–10, from `leetcode-list.md`). All 46 LeetCode problems checked against LeetCode's API (title, Easy, free); 4 GfG problems checked against GfG's API. Signatures switched to LeetCode's current `list[int]` style everywhere.
- Mistakes this session: added graphs/trees/Medium problems and a 150-problem list after Vikash asked whether the *Python* was covered. Reverted to 50 easy.
- Left out (untracked, not committed): agent-written lessons 12–17 (grids, built-ins, recursion, classes, collections, heapq). Lesson 11 (two pointers/stacks) stays in the repo but not in the PDF. `practice/`/`solutions/` (old 50, runnable with tests) kept; they overlap the list but don't match it exactly.
- Next: Vikash's call on lessons 12–17 and on the `practice/` folder.
- CLAUDE.md layout line for `python-dsa/` updated to match (lessons 1–10, two PDFs).

## 2026-10-24: Tanvi's first branch merged

- Done: merged Tanvi's branch `01tanvi-work` (her commit "bind-mount": message-box on port 8080, a `/messages` route, her test `data/messages.txt`, `package.json` + lock) into main, together with Vikash's own edit (`table/` folder + `/messages`). Conflict in `message-box/app.js` resolved by keeping both: `table/` + port 8080, one `/messages` route. App tested in Docker. Branch left on GitHub; backup tag `backup/main-before-tanvi-merge` (local only).
- State: `message-box/app.js` no longer matches pages 1–6 of section 2 (they use port 3000 and `/app/data`).
- Next: Vikash decides whether the reference app goes back to the page version (Tanvi's experiments could live on her branch), or the pages change.

## 2026-10-24: sections 05, 06, 07

- Doing: `05-layers` (example app `cow-says/`), `06-how-networking-works` (fundamentals), `07-compose` (todo app: nginx frontend + Node API + Postgres), written in parallel; then review, nav, index, commit.
- Untouched: Vikash's own uncommitted edit to `docs/02-message-app/message-box/app.js` (`data/` → `table/`, `/messages` route). Not committed by Claude.
- 05 (5 pages: layers, build cache + order, sharing/size + .dockerignore, container layer + docker diff, multi-stage with a tiny Go cow; 4 diagrams; apps `cow-says/`, `tiny-cow/`) and 06 (6 pages, 6 diagrams, `demo.sh`; one analogy: laptop = building, IP = address, ports = flats, 127.0.0.1 = intercom, 0.0.0.0 = front door, DNS = contacts app, router = watchman) written, reviewed, in nav + index, committed. 07 done too (see below).
- 06 caveats: phone steps and Mac-only commands not verified here. 05: outputs from rootless Docker with containerd store (DISK USAGE / CONTENT SIZE columns).
- 07: 5 pages (three parts with a restaurant comparison → by hand with network/volume/3 runs → compose.yaml line by line → logs, psql, fix a real bug (empty todos) and rebuild, down vs down -v → how parts find each other: service names as DNS, env vars, only 8080 published, 502 when backend stops). `todo-app/` = nginx (static page + `/api/` proxy with `resolver 127.0.0.11` so a rebuilt backend's new IP is found) + Express/pg + postgres:17-alpine (healthcheck, `service_healthy`, volume, init.sql with 2 sample todos). 3 diagrams, `demo.sh`. Verified here; interactive psql prompt and clicking the UI not driven by hand.
- Also: `draw.py --png` now sizes previews correctly with bent arrows.
- Next: Vikash's feedback on 05–07. Open question still: redraw sections 1–3 diagrams in the detailed style?

## 2026-10-22: networking section + explaining diagrams

- Done: `docs/04-networking/`, 4 pages: 01 default network (busybox, IPs, ping by number ✓ / name ✗), 02 your own network (create, DNS 127.0.0.11, nslookup, alias, outsider, connect, inspect, command table), 03 visit counter (`visit-counter/` Node + Redis, ENOTFOUND on default network, `counter-net`, db private, step-by-step flow, redis-cli from a third container, replace web and the count stays), 04 which address (rule + table, `-e DB_URL`, mistakes: localhost → ECONNREFUSED, laptop port 6380 → ECONNREFUSED, wrong network → Name does not resolve; error table). 4 diagrams in the new style. `demo.sh` (Enter-per-step, or `--no-wait`) ran clean end to end. Every page command verified here.
- Diagrams: `draw.py` rewritten + `--png` preview; style guide, skill and CLAUDE.md updated to "explain properly". Specs in `.claude/skills/excalidraw/specs/04-networking/`.
- Next: Vikash's feedback on the new diagram style; whether to redraw sections 1–3 diagrams the same way.
- Also: `docs/README.md` section 4 and a `demo.sh` pointer at the end of page 04 (same commit).

## 2026-10-22: producer and consumer project

- Done: `docs/03-two-apps/` (Vikash asked: a producer app like message-box, a consumer that reads and shows, shared once with a volume and once with a bind mount). `producer/` = message-box with a new heading (port 3000, `/web`, writes `data/messages.txt`); `consumer/` = Express `GET /read` on port 4000 that lists the lines. Same 5-line Dockerfile. Pages: 01 the two apps (+ shows they can't see each other without sharing), 02 volume `shared`, 03 bind mount `./shared` (+ she adds a line by hand in VS Code). Diagrams `share-volume`, `share-bind-mount`. Every command verified here, including a second consumer on 4001.
- Note: on this machine (rootless Docker) the bind-mounted file is owned by Vikash. On rootful Linux Docker it would be root-owned and her hand edit would fail.
- Next: Vikash's feedback.

## 2026-10-22: go inside a container

- Done: `docs/02-message-app/09-go-inside-a-container.md` (Vikash asked: how to get into a container, what `-it` means). Covers `docker exec -it msg bash`, reading the prompt, look around, `exit` leaves the container running, `-i` vs `-t` table (no flags / only -t / only -i / both), `sh` when there's no bash, changes inside don't last. Diagram `go-inside.excalidraw`. Added to nav + `docs/README.md`. Every command verified here, including each flag combination.
- Next: Vikash's feedback.

## 2026-10-21: MkDocs site

- Done: `mkdocs.yml` (Material, light/dark, copy buttons, nav for both sections), `pyproject.toml` + `uv.lock`, `Makefile`, root `README.md` how-to. `make build` and `make serve` verified.
- Known gaps: `.excalidraw` links open as raw files in the site (not drawn), and links to folders (`message-box/`, `files/`) don't list their contents.
- Next: Vikash's call on rendering diagrams in the site.

## 2026-10-21: message-box project

- Done: `docs/02-message-app/` with 5 pages (the app → Dockerfile → containers forget → bind mount → volume), `message-box/` (app.js + Dockerfile) and 2 diagrams (`app-flow`, `where-messages-live`). Linked from `docs/README.md`. Every command verified here (local run, build, stop/start vs rm, bind mount, volume).
- Added `06-all-commands-explained.md` (both files + every command and flag, in page order, plus look-around and cleanup) and `commands-journey.excalidraw` (files → build → image → run → container → stop / rm).
- Added a Python version (Vikash asked for one as well): `07-same-app-in-python.md` + `message-box-python/` (Flask app.py, 5-line Dockerfile). Same port 3000 and `/app/data`, so pages 3–6 commands work unchanged with image `message-box-python`. Verified locally and in Docker (logs, rm forgets, bind mount, volume).
- Added `08-dockerfile-keywords.md`: all 18 Dockerfile instructions (table with how often used, the 5 she knows, the common ones explained, rare ones listed, mixed-up pairs, exec vs shell form, comments/syntax/.dockerignore) + `message-box/Dockerfile.full` using most of them. Built and run here: user `node`, NODE_ENV, healthy, ARG override, CMD replaced.
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
