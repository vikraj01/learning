A friend wrote a `compose.yaml` for the notes app (web → api → db) and says it "doesn't work". There are **three mistakes** in it, all in `compose.yaml`. The code in `web/` and `api/` is fine; don't change it.

Find them one at a time. Each fix gets you to the next error.

## How to hunt

1. **Can Compose read it?** `docker compose config`. If not, it names a line. YAML errors are reported **near** the problem, so look at the whole block around that line.
2. **Does it start?** `docker compose up -d --build`, then `docker compose ps -a`.
3. **Does the page open?** If nothing answers on **http://localhost:3504**, the door is wrong: `docker compose logs web` says which port the app really listens on inside.
4. **Is there a red error on the page?** Read it: it says which part can't reach which.

## Commands that help

```
docker compose config
docker compose up -d --build
docker compose ps -a
docker compose logs web
docker compose logs api
```

> After each fix, save and run `docker compose up -d` again. Compose only recreates the services whose settings changed.
