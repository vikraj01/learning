# Compose: all of it in one file

After this page you'll be able to write everything from sections 9 to 13 (settings, `.env`, tags, `CMD`, `ENTRYPOINT`, `-f`) into one `compose.yaml`, and start it all with one command.

## This section

You met Compose in section 7 with the todo app. This section goes further, one example per page:

1. **This page**: greet. Everything from sections 9–13, in one file.
2. [Compose reads `.env` too](02-compose-reads-env.md): `${...}` in `compose.yaml`.
3. [The notes app](03-notes-app.md): frontend, backend and database, with two networks and a password in `.env`.
4. [WordPress](04-wordpress.md): a ready-made app, no code at all.
5. [Compose commands](commands.md): everything on one page.

## The long commands, written down once

Look at what you typed in section 13 just to start two containers:

```bash
docker build -t greet:3.0 .
docker build -f Dockerfile.dev -t greet:dev .
docker run --rm -d -p 3000:3000 --env-file .env --name greet greet:3.0
docker run --rm -d -p 3001:3000 -v "$(pwd):/app" -e NAME=Tanvi --name greet-dev greet:dev
```

You already know Compose from section 7: it's a file that remembers all of this for you. This page shows where each thing from the last five sections goes in that file.

## Before you start

You need the `greet` folder from section 13: `app.js`, `say.js`, `Dockerfile` (with `ENTRYPOINT ["node"]` and `CMD ["app.js"]`), `Dockerfile.dev`, and `.env`:

```
NAME=Tanvi
COLOR=pink
```

Stop the section 13 containers if they're still running, so ports 3000 and 3001 are free:

```bash
docker rm -f greet greet-dev
```

## The file

In your `greet` folder, make `compose.yaml`:

```yaml
name: greet

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    image: greet:3.0
    env_file: .env
    ports:
      - "3000:3000"

  dev:
    build:
      context: .
      dockerfile: Dockerfile.dev
    image: greet:dev
    environment:
      NAME: Tanvi
    ports:
      - "3001:3000"
    volumes:
      - ./:/app

  say:
    image: greet:3.0
    environment:
      NAME: Ravi
    command: ["say.js"]
```

Three services, all from the same `greet` folder:

- **`web`**: the real one (`Dockerfile`), on port 3000.
- **`dev`**: the one you work on (`Dockerfile.dev`), on port 3001, with your folder mounted in.
- **`say`**: the same image as `web`, but runs `say.js` instead, prints one line and stops.

## Every line, and where you learned it

| In `compose.yaml` | Same as on the command line | Section |
| --- | --- | --- |
| `environment:` `NAME: Tanvi` | `-e NAME=Tanvi` | 9 |
| `env_file: .env` | `--env-file .env` | 9 |
| `image: greet:3.0` (with `build:`) | `docker build -t greet:3.0` | 10 |
| `command: ["say.js"]` | words after the image name: `docker run greet:3.0 say.js` | 11 |
| `entrypoint: ["bash"]` (not in our file) | `--entrypoint bash` | 12 |
| `context: .` | the `.` at the end of `docker build` | 13 |
| `dockerfile: Dockerfile.dev` | `-f Dockerfile.dev` | 13 |
| `ports:` `"3001:3000"` | `-p 3001:3000` | 1 |
| `volumes:` `./:/app` | `-v "$(pwd):/app"` | 1 |

A few things to notice:

- **`image:` next to `build:`** means "build it, and give it this name and tag". Without `image:`, Compose would name it `greet-web` itself.
- **`say` has `image:` but no `build:`**. It doesn't build anything; it uses the `greet:3.0` that `web` builds.
- **`command:` replaces `CMD` only.** The `ENTRYPOINT` (`node`) stays, so `say` runs `node say.js`. Exactly like section 12.
- **`env_file:` works like Way 1 from section 9 page 4**: Compose reads `.env` and makes real environment variables, so `COLOR=pink` beats the image's `lightblue`.

## Try it: start everything

```bash
docker compose up -d
```

```
 ✔ greet:3.0                Built
 ✔ greet:dev                Built
 ✔ Network greet_default    Created
 ✔ Container greet-web-1    Started
 ✔ Container greet-dev-1    Started
 ✔ Container greet-say-1    Started
```

(The first time it also prints the build steps. Your lines may look slightly different.)

- <http://localhost:3000>: **pink**, **Hello, Tanvi! 👋** (`web`: `.env` through `env_file`)
- <http://localhost:3001>: **light yellow**, **Hello, Tanvi! 👋** (`dev`: `Dockerfile.dev`'s `ENV` colour)

And `say`? It already ran and stopped. Read what it printed:

```bash
docker compose logs say
```

```
say-1  | Hello, Ravi!
```

`NAME: Ravi` from `environment:`, `say.js` from `command:`.

## Try it: run `say` again, with something else

`docker compose run` starts a fresh container for one service. Words after the service name replace its `command:`, just like words after the image name in `docker run`:

```bash
docker compose run --rm say
```

```
Hello, Ravi!
```

```bash
docker compose run --rm -e NAME=Tanvi say
```

```
Hello, Tanvi!
```

```bash
docker compose run --rm say --version
```

```
v24.22.1
```

`node` (the `ENTRYPOINT`) + `--version`.

## Try it: the tags Compose made

```bash
docker images greet
```

```
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
greet:1.0      ab9c46957e5d        330MB         81.1MB
greet:2.0      7d41c0f2b9a3        330MB         81.1MB
greet:3.0      585063c94312        330MB         81.1MB
greet:dev      8bf970d1a0ce        330MB         81.1MB
greet:latest   7d41c0f2b9a3        330MB         81.1MB
```

`greet:3.0` and `greet:dev` were built by Compose, with the names from `image:`. The older ones are from section 10. Your IDs will be different.

## After you change the code

`docker compose up -d` only builds an image if it doesn't exist yet. After you change `app.js`, build again:

```bash
docker compose up -d --build
```

(The `dev` service doesn't need this: its bind mount and `--watch` pick up changes by themselves, as in section 13.)

## Clean up

```bash
docker compose down
```

This stops and removes all three containers and the network. The images stay.

## `up` or `run`?

| | `docker compose up -d` | `docker compose run --rm say` |
| --- | --- | --- |
| Starts | every service in the file | one service, in a new container |
| For | apps that keep running (`web`, `dev`) | one-off jobs that do something and stop (`say`) |
| `command:` | as written in `compose.yaml` | can be replaced by words after the service name |

## Check yourself

1. Which line in `compose.yaml` does the same job as `-f Dockerfile.dev`?
2. `say` has `command: ["say.js"]`. Why does it run `node say.js` and not just `say.js`?
3. You change `NAME=Tanvi` to `NAME=Asha` in `.env` and run `docker compose up -d`. Which page changes: 3000, 3001, or both? (Hint: `web` reads `.env` through `env_file`. Does `dev` read it at all? Think about the bind mount.)

## Next

[Compose reads `.env` too](02-compose-reads-env.md): use `${...}` in `compose.yaml` to fill in a port from `.env`.

Finished files: [`14-compose/greet/`](greet/). (Its `web` port line already has the change from page 2.)
