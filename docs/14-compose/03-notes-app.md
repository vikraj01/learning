# Frontend, backend, database: the notes app in Compose

After this page you'll be able to write a `compose.yaml` for a three-part app on your own, keep its password in `.env`, and use two networks so the frontend can't reach the database at all.

## The notes app again

In section 8 you ran the notes app by hand: three images, three `docker run`s, a `docker network create`, and the right order in your head. Its three parts are the same three you met with the todo app in section 7:

| Part | Service | Does | Listens on |
| --- | --- | --- | --- |
| **Frontend** | `web` | the page you see in the browser | 3000 |
| **Backend** | `api` | takes a note from `web`, saves it in the database | 4000 |
| **Database** | `db` | Postgres, keeps the notes | 5432 |

```
 browser  →  web  →  api  →  db
```

Remember the restaurant from section 7: the dining room (frontend), the kitchen (backend), the pantry (database). **Only the kitchen goes into the pantry.** On this page you'll make Docker enforce that rule.

## What's new compared to section 8

The finished files are in `14-compose/notes-app/`. The `web` and `api` folders are section 8's, with one change each: they read their settings from **environment variables** (section 9) instead of having them written into the code.

In `api/server.js`:

```js
const DB_HOST = process.env.DB_HOST || "db";
const db = new Pool({
  host: DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});
```

In `web/server.js`:

```js
const API_URL = process.env.API_URL || "http://api:4000";
```

So the password isn't in the code any more. It will come from `.env`, through `compose.yaml`.

And `db` has no folder at all: it's the ready-made `postgres:17-alpine` image, with its settings given in `compose.yaml`.

## The password goes in `.env`

In the `notes-app` folder, make a file called `.env`:

```
DB_USER=notes
DB_PASSWORD=secret
DB_NAME=notes
```

Compose reads it by itself (page 2, job 2).

## The file

`notes-app/compose.yaml`:

```yaml
name: notes

services:
  web:
    build: ./web
    environment:
      API_URL: http://api:4000
    ports:
      - "3000:3000"
    networks:
      - front
    depends_on:
      - api
    restart: unless-stopped

  api:
    build: ./api
    environment:
      DB_HOST: db
      DB_USER: ${DB_USER}
      DB_PASSWORD: ${DB_PASSWORD}
      DB_NAME: ${DB_NAME}
    networks:
      - front
      - back
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped

  db:
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - data:/var/lib/postgresql/data
    networks:
      - back
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "${DB_USER}"]
      interval: 2s
      retries: 10
    restart: unless-stopped

networks:
  front:
  back:

volumes:
  data:
```

Most of it you know from section 7: `build`, `ports`, `environment`, `depends_on` with a `healthcheck`, a named volume. Three things are new.

### New 1: two networks of your own

In section 7 you didn't write any network: Compose made one called `todo_default` and put everyone on it. Here we write our own, two of them:

```yaml
networks:
  front:
  back:
```

At the bottom, like `volumes:`: "this project needs two networks". Compose makes them as `notes_front` and `notes_back` (project name + `_` + network name, like volumes).

Then each service says which networks it joins:

| Service | `front` | `back` | Can find by name |
| --- | --- | --- | --- |
| `web` | ✓ | | `api` |
| `api` | ✓ | ✓ | `web` and `db` |
| `db` | | ✓ | `api` |

`api` is on **both**, like a kitchen with one door to the dining room and one to the pantry. `web` and `db` share no network, so `web` can't even find `db`'s name. It's section 8's demo 3 (different networks), but this time on purpose.

Why would you want that? If someone breaks into `web` (the part the whole internet can reach), the database isn't even in sight. Only `api` can talk to it.

[Diagram: two networks, only api is on both](./notes-networks.excalidraw)

### New 2: values from `.env`: `${DB_PASSWORD}`

`DB_USER`, `DB_PASSWORD` and `DB_NAME` each appear **twice** in the file: once for `db` (`POSTGRES_PASSWORD`, so Postgres sets that password) and once for `api` (`DB_PASSWORD`, so the app logs in with it). Both come from the same line in `.env`, so they can never be different.

Change the password in one place, `.env`, and both sides change together.

(The `-U ${DB_USER}` in the healthcheck is filled in the same way.)

!!! warning "One catch"
    Postgres reads `POSTGRES_USER`, `POSTGRES_PASSWORD` and `POSTGRES_DB` only **the very first time**, when its volume is empty and it sets the database up. Change the password in `.env` later, and Postgres still has the old one (it's saved in the volume), while `api` now tries the new one: `api` can't log in. To start over with the new password, throw the old database away with `docker compose down -v`.

### New 3: `restart: unless-stopped`

What should Docker do if the program inside a container crashes and the container stops? Without a `restart:` line: nothing. It stays stopped until you start it.

| `restart:` | Means |
| --- | --- |
| `"no"` (the default) | never start it again by itself |
| `on-failure` | start it again only if it stopped because of an error |
| `always` | always start it again |
| `unless-stopped` | always start it again, **unless you stopped it yourself** |

With `unless-stopped`, if `api` crashes, Docker starts it again. If your laptop restarts, the notes app comes back when Docker starts. But if you ran `docker compose stop`, it stays stopped: you asked for that.

## Try it: start everything

From the `notes-app` folder:

```bash
docker compose up -d --build
```

After the builds you'll see something like this:

```
 ✔ Network notes_front      Created
 ✔ Network notes_back       Created
 ✔ Volume notes_data        Created
 ✔ Container notes-db-1     Healthy
 ✔ Container notes-api-1    Started
 ✔ Container notes-web-1    Started
```

Two networks, one volume. `db` first, and `api` only once `db` was healthy.

Open <http://localhost:3000>, write a note, click **Save**. It shows up in the list ✓

## Try it: who can see whom

`ping` sends a tiny "are you there?" message to a computer by name. It comes with the Alpine images we use.

From `api` (on both networks), find `db`:

```bash
docker compose exec api ping -c 1 db
```

```
PING db (172.19.0.2): 56 data bytes
64 bytes from 172.19.0.2: seq=0 ttl=64 time=0.120 ms

--- db ping statistics ---
1 packets transmitted, 1 packets received, 0% packet loss
```

✓ `api` found `db` and got an answer. (`-c 1` means "only once". Your numbers will be different.)

Now from `web` (only on `front`):

```bash
docker compose exec web ping -c 1 db
```

```
ping: bad address 'db'
```

✗ `web` doesn't even know the name `db`. Exactly what we wanted.

And `web` can still reach `api`:

```bash
docker compose exec web ping -c 1 api
```

```
PING api (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=0.095 ms
...
```

✓ Same network (`front`).

See the networks Compose made:

```bash
docker network ls --filter name=notes
```

```
NETWORK ID     NAME          DRIVER    SCOPE
3c1f0e6a2b7d   notes_back    bridge    local
9a4d52e1c8f0   notes_front   bridge    local
```

## Try it: the password, in one place

Look at what Compose filled in:

```bash
docker compose config | grep -i password
```

```
      DB_PASSWORD: secret
      POSTGRES_PASSWORD: secret
```

Both from the one `DB_PASSWORD=secret` line in `.env`.

## Section 8 vs this page

| | Section 8 (by hand) | Here (Compose) |
| --- | --- | --- |
| Networks | `docker network create notes-net` | `networks:` at the bottom of the file |
| Put a container on a network | `--network notes-net` | `networks: - front` under the service |
| Password | written in the `db` Dockerfile and in `server.js` | one line in `.env` |
| Order | you start `db`, wait, then `api`, then `web` | `depends_on` + healthcheck |
| Notes after removing `db` | gone (no volume) | kept in the `notes_data` volume |
| Start everything | 3 builds + 3 runs | `docker compose up -d --build` |

## Clean up

```bash
docker compose down
```

The notes stay in the `notes_data` volume. To throw them away too, `docker compose down -v` (section 7, page 4).

## Check yourself

1. You add `networks: - back` to `web` as well. What changes? Is that a good idea?
2. You change `DB_PASSWORD` in `.env` to `hello` and run `docker compose up -d`. Which two settings change? Why does the app stop working anyway?
3. Your laptop restarts. Which services come back by themselves, and why?

## Next

[A ready-made app: WordPress, with no code at all](04-wordpress.md).
