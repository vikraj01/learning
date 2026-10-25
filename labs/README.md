# Docker Labs

Hands-on Docker practice for Tanvi, in the browser: a task on the left, a file editor and a **real terminal** on the right, and a **Check my work** button that marks every step ✓ or ✗ with a hint. Like KodeKloud or Killercoda, but on her own laptop with her own projects.

## Start it

From the repo root:

```bash
make labs
```

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
cd labs/app
npm install
npm run dev        # site on :5173 with live reload, server on :7000
npm run typecheck
```

## The labs

| # | Lab | Teaches |
|---|-----|---------|
| 1 | Run a website in a container | `docker run`, `--name`, `-d`, `-p` |
| 2 | Fix a broken Dockerfile | reading build errors, `FROM`, `COPY`, `CMD`, `docker logs` |
| 3 | Make the notes app talk | default network vs your own network, names, `docker network connect` |
