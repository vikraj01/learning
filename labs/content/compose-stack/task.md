The **notes app** in three parts:

| Part | Service name | Where it comes from | Listens on |
| --- | --- | --- | --- |
| Frontend | `web` | the `web` folder (has a Dockerfile) | 3000 |
| Backend | `api` | the `api` folder (has a Dockerfile) | 4000 |
| Database | `db` | the ready-made image `postgres:17-alpine` | 5432 |

There's no `compose.yaml` yet. You'll write it.

## The settings each part reads

Open `web/server.js` and `api/server.js`: they read their settings from environment variables.

- **web** reads `API_URL`: where the api is. Use `http://api:4000`.
- **api** reads `DB_HOST` (where the database is: `db`), `DB_USER`, `DB_PASSWORD`, `DB_NAME`.
- **db** (the postgres image) reads `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, and makes that user and database on its first start.

The api logs in with what Postgres made, so the two sides must match: `DB_USER` = `POSTGRES_USER`, and so on. Pick any values, say `notes` / `secret` / `notes`.

## Your job

1. Write `compose.yaml` with the three services.
2. Only `web` gets a door: **http://localhost:3501** (port **3000** inside). `api` and `db` stay private.
3. Give `db` a named volume on `/var/lib/postgresql/data`, so the notes survive `docker compose down`.
4. Start it, open the page, save a note.

## Commands that help

```
docker compose config
docker compose up -d --build
docker compose ps -a
docker compose logs api
docker compose down          # add -v to throw the database away too
```

> Services find each other **by service name** on the network Compose makes. No `docker network create` needed.
