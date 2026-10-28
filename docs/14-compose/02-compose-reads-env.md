# Compose reads `.env` too: `${...}` in compose.yaml

After this page you'll be able to put changing values (a port, a password) into `.env` and use them inside `compose.yaml` with `${...}`, and see the finished file Compose really uses.

## One envelope, two jobs

Think of the `.env` file as an envelope of notes. On page 1, Compose handed the whole envelope **to the app** (`env_file: .env`): the app opened it and read `NAME` and `COLOR`.

There's a second job the same envelope can do. Compose itself **reads it first**, for its own use, to fill in blanks in `compose.yaml`. That's what this page is about.

| | Who reads it | What for | You write |
| --- | --- | --- | --- |
| **Job 1**: `env_file: .env` | the app, inside the container | the app's settings | `env_file: .env` under a service |
| **Job 2**: `${...}` | Compose, before it starts anything | blanks in `compose.yaml` | `${NAME}` anywhere in `compose.yaml` |

Job 2 happens by itself: Compose always looks for a file called `.env` in the folder you run it from. You don't have to ask.

[Diagram: one `.env` file, two jobs](./env-two-jobs.excalidraw)

## A blank to fill in: `${...}`

**`${WEB_PORT}`** in `compose.yaml` means "put the value of `WEB_PORT` here". The word for this is **interpolation**: filling a value into the middle of some text.

Open `greet/compose.yaml` and change the `web` port line:

```yaml
  web:
    ...
    ports:
      - "${WEB_PORT:-3000}:3000"
```

Read `${WEB_PORT:-3000}` in three parts:

- **`WEB_PORT`**: the name to look up.
- **`:-`**: "and if it isn't set...".
- **`3000`**: "...use this instead". This is the **default**.

So: use `WEB_PORT` if someone set it, otherwise 3000.

## Try it: see what Compose sees

`docker compose config` prints `compose.yaml` **after** Compose has filled in every blank and read every file. It starts nothing; it only shows.

```bash
docker compose config
```

Find the `web` part:

```
  web:
    build:
      context: /home/tanvi/learning/docs/14-compose/greet
      dockerfile: Dockerfile
    environment:
      COLOR: pink
      NAME: Tanvi
    image: greet:3.0
    networks:
      default: null
    ports:
      - mode: ingress
        target: 3000
        published: "3000"
        protocol: tcp
```

Three things to notice:

- **`published: "3000"`**: nobody set `WEB_PORT`, so the default 3000 was used.
- **`environment:` with `COLOR` and `NAME`**: that's job 1. `env_file: .env` was opened and turned into real settings for the app.
- `context:` is now the full path of your folder. Yours will start with your own home folder.

`docker compose config` is the first thing to run when Compose does something you didn't expect.

## Try it: set it in `.env`

Add one line to `greet/.env`:

```
NAME=Tanvi
COLOR=pink
WEB_PORT=4000
```

```bash
docker compose config | grep published
```

```
        published: "3001"
        published: "4000"
```

The first line is `dev` (Compose lists services in A to Z order); it stays on 3001, since its line has no `${...}`. The second is `web`, now on 4000.

```bash
docker compose up -d
```

Open <http://localhost:4000>. Pink, **Hello, Tanvi! 👋**.

One `.env`, both jobs at once: Compose used `WEB_PORT` for the door (job 2), and `env_file` still handed `NAME` and `COLOR` to the app (job 1). The app also gets `WEB_PORT`, since `env_file` hands over every line; it doesn't use it, so nothing happens.

## Try it: the terminal wins

A value typed in front of the command beats the file, just like in section 9:

```bash
WEB_PORT=5000 docker compose config | grep published
```

```
        published: "3001"
        published: "5000"
```

Who wins for `${...}`, strongest first:

1. A variable set in your terminal (`WEB_PORT=5000 docker compose ...`)
2. The line in `.env`
3. The default after `:-` in `compose.yaml`

## Try it: forget the default

Take `:-3000` out, so the line is `"${WEB_PORT}:3000"`, and remove `WEB_PORT` from `.env`. Then:

```bash
docker compose config
```

```
WARN[0000] The "WEB_PORT" variable is not set. Defaulting to a blank string.
```

(Your warning may look a little different, but it says the same thing.)

Compose doesn't stop; it puts **nothing** there, and then `":3000"` is a broken port. When you see this warning, a name in `${...}` has no value. Put the `:-3000` back and remove the `WEB_PORT` line from `.env`.

## Why bother?

Because now `compose.yaml` stays the same for everyone, and only `.env` changes:

- Port 3000 is busy on your friend's laptop? She sets `WEB_PORT=3005` in her `.env`. The `compose.yaml` stays the same.
- A password? It goes in `.env` as `DB_PASSWORD=...`, and `compose.yaml` only says `${DB_PASSWORD}`. You'll do exactly this on the next page.

## Clean up

```bash
docker compose down
```

## Check yourself

1. `.env` has `WEB_PORT=4000` and you run `WEB_PORT=4500 docker compose up -d`. Which port is `web` on?
2. What does `${WEB_PORT:-3000}` mean, in plain words?
3. `compose.yaml` has no `env_file:` at all, but uses `${COLOR}`. Does the app inside the container get `COLOR`? (Hint: which job is that?)

## Next

[Frontend, backend, database: the notes app in Compose](03-notes-app.md). Section 8's three-part app, written as one file, with a password in `.env`.
