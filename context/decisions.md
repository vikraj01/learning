# Decisions

Choices Vikash has made. Newest first. One line each, with the date.

- 2026-10-21: Always commit and push after each piece of work (rule in `CLAUDE.md`). Tanvi (GitHub `Tanvikanwar23`) invited as a collaborator on `vikraj01/learning`.
- 2026-10-20: Storage is two pages: bind mounts (her own folder, live edits), then volumes (containers aren't persistent, named volumes persist and can be shared). Call them "bind mount" and "volume", never "volume mount".
- 2026-10-20: Images get their own page (Vikash: "important concept"), right after run: what's inside (Linux files, program, start command), layers, read-only, name:tag, pull/images/rmi.
- 2026-10-20: Docker order: what it is (image vs container) → run (hello-world, nginx) → what is an image → port mapping → volumes → Dockerfile + build → Dockerfile instructions. Build comes after Dockerfile, not before. One running example throughout: her own `index.html` served by nginx. No Python needed for Docker.
- 2026-10-20: Go slow. Set up the repo first; no docs until Vikash adds notes to `plan/`.
- 2026-10-20: Study material goes in `docs/`; Vikash's own thinking stays in `plan/`.
- 2026-10-20: Diagrams in Excalidraw, kept simple and calm, editable by Vikash afterwards.
- 2026-10-20: Claude runs in bypass-permissions mode in this repo.
- 2026-10-20 (from `plan/plan.md`): topics are Python, apps/servers/React/web, Docker, Kubernetes. Start with Docker: build & run, Dockerfile, port mapping, volumes.
