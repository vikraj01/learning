The notes app is running on **http://localhost:3503**. The `compose.yaml` has no `networks:` anywhere, so Compose put all three services on one network it made by itself, called `labprivate_default`.

That means **web can reach the database directly**. web is the part the world can reach; if someone breaks into it, the database is right there.

Remember the restaurant: dining room (`web`), kitchen (`api`), pantry (`db`). Only the kitchen should go into the pantry.

## Your job

Split it into two networks:

| Service | `front` | `back` |
| --- | --- | --- |
| `web` | ✓ | |
| `api` | ✓ | ✓ |
| `db` | | ✓ |

Then check the app still works, and save a note.

## How networks look in compose.yaml

At the bottom, the networks the project needs:

```yaml
networks:
  front:
  back:
```

Under each service, the ones it joins:

```yaml
  api:
    ...
    networks:
      - front
      - back
```

## Commands that help

```
docker compose up -d
docker compose exec api ping -c 1 db     # should work
docker compose exec web ping -c 1 db     # should say: bad address 'db'
docker network ls
```

> A container can only find names on networks it has joined. If `web` and `db` share none, to `web` the name `db` doesn't exist.
