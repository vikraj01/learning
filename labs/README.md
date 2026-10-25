# Docker Labs

Hands-on Docker practice for Tanvi, in the browser: a task on the left, a file editor and a **real terminal** on the right, and a **Check my work** button that marks every step ✓ or ✗ with a hint. Like KodeKloud or Killercoda, but on her own laptop with her own projects.

## Start it

From this folder:

```bash
make            # list the commands
make start      # install, build and open the labs
```

Or from the repo root: `make labs`.

Then open **http://localhost:7000**. The first run installs packages and builds the site, which takes a minute.

Needs: Node 20+, Python 3, Docker, `curl`. The server only listens on `127.0.0.1`, because it gives the browser a shell on this laptop.

## How it works

```
labs/
  app/                      the site (React + TypeScript, Vite) and the server (Express + TypeScript)
    src/                    pages and components: task panel, file tree, Monaco editor, xterm terminal
    server/                 API, file access, and the terminal (bash in a pty via pty-bridge.py)
  content/                  one folder per lab
    _lib/check.sh           helpers for checkers: pass, fail, running, exists, page, networks_of …
    01-run-a-website/
      lab.json              title, level, minutes, topics, and the tasks (id, title, hint)
      task.md               what she reads (Markdown)
      starter/              files she starts with (copied into her workspace)
      setup.sh              prepares the lab (pull images, start broken containers …)
      check.sh              prints PASS/FAIL <task-id> <message> for each task
      cleanup.sh            removes the lab's containers and images (used by Reset)
  workspace/<lab-id>/       her working copy of each lab (not committed)
  .progress.json            which labs she has solved (not committed)
```

- **Open a lab**: the first time, `starter/` is copied into `workspace/<lab-id>/` and `setup.sh` runs. The terminal and the editor both work in that folder.
- **Check my work**: runs `check.sh`. Every task listed in `lab.json` needs a `PASS` line for the lab to count as solved.
- **Reset**: runs `cleanup.sh`, wipes the workspace, and sets the lab up again.
- **Ctrl + Enter** checks from anywhere. **Ctrl + S** saves the open file.

## Add a lab

Make a new folder in `content/` with the files above. Number it in `lab.json`. Checkers should only look at the **result** (what's running, which network, does the page answer), so any correct way of solving it passes. Write messages that say what's wrong and point at the fix. Use `backticks` for names and commands; they show as code.

## Develop

```bash
make dev             # site on :5173 with live reload, server on :7000
make typecheck
make reset-progress  # forget solved labs, delete every workspace
```

## The labs

Grouped into tracks (`content/tracks.json`); each lab's `lab.json` names its `track` and its `number` (the order).

| # | Track | Lab | Teaches | Port |
|---|-------|-----|---------|------|
| 1 | Basics | Run a website in a container | `docker run`, `--name`, `-d`, `-p` | 8080 |
| 2 | Basics | Two websites at once | same inside port, different laptop doors | 8091, 8092 |
| 3 | Basics | That door is taken | "port is already allocated", leftover containers, `docker rm` | 8093, 8094 |
| 4 | Basics | A website only you can open | `-p 127.0.0.1:…` | 8095 |
| 5 | Basics | Tidy up Docker | `ps -a`, `start`, `rm`, `volume rm`, removing by name | – |
| 6 | Images | Write your first Dockerfile | `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD` | 8096 |
| 7 | Images | Fix a broken Dockerfile | build errors, `docker logs` | 8081 |
| 8 | Images | Make rebuilds fast | build cache, layer order (the checker really rebuilds) | – |
| 9 | Inside | Find the secret inside a container | `docker exec -it`, `ls -a`, `cat` | – |
| 10 | Inside | Running, but the page won't open | `docker logs`, the app's real port | 8098 |
| 11 | Storage | Messages that survive | volumes, `-v name:/path`, replacing a container | 8099 |
| 12 | Storage | Edit a website live | bind mounts, `-v "$(pwd)/site":…` | 8100 |
| 13 | Networking | Every container has an address | IPs, gateway, reaching a container by number | – |
| 14 | Networking | Make the notes app talk | default vs own network, names, `network connect` | 3300 |
| 15 | Networking | Keep the database private | two networks, `connect`/`disconnect` | 3301 |

Labs 14 and 15 both use the notes app with containers named `web`, `api` and `db`, so opening one breaks the other's setup. Press **Reset** when you go back to one.
