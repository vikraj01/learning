The notes app is running on **http://localhost:3502**, started from the `compose.yaml` on the left. Look at it: the password `secret` is typed **twice**, once for `db` (`POSTGRES_PASSWORD`) and once for `api` (`DB_PASSWORD`).

Two problems: it's easy to change one and forget the other, and anyone who reads the file (or the Git history) sees the password.

## `${...}` and `.env`

Compose reads a file called **`.env`** from this folder **by itself**, and fills in every `${NAME}` in `compose.yaml` with its value.

```
# .env
DB_PASSWORD=mango-lassi-7
```

```yaml
# compose.yaml
      DB_PASSWORD: ${DB_PASSWORD}
```

One line in `.env`, used in both places. They can't disagree any more.

## Your job

1. Make `.env` with a **new** password in `DB_PASSWORD`.
2. Put `${DB_PASSWORD}` in both places in `compose.yaml`, so `secret` appears nowhere.
3. Apply it with `docker compose up -d`.
4. Make the page work again. (It will break. Read the hint when it does: it's the most common Compose surprise there is.)

## Commands that help

```
docker compose config | grep -i password
docker compose up -d
docker compose logs api
docker compose down -v
```

> `.env` is for **Compose**. The app inside never sees the file; it only gets what `compose.yaml` hands it under `environment:`.
