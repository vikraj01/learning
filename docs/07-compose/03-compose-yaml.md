# One file: compose.yaml

After this page you'll be able to read a `compose.yaml` line by line, and start the whole todo app with one command.

## A recipe card for the whole meal

A Dockerfile is a recipe for **one** dish (one image). **Docker Compose** is the menu for the whole meal: which dishes, in which order, served where. You write it down once in a file called **`compose.yaml`**, and Compose does all of page 2's work for you.

**YAML** (say "YAM-ul") is the file format: plain text where **indentation** (spaces at the start of a line) shows what belongs to what. Use spaces, never tabs.

Check Compose is installed (it comes with Docker Desktop):

```bash
docker compose version
```

```
Docker Compose version v2.40.3
```

Your number may be different. Anything starting with 2 is fine.

## The file

This is `todo-app/compose.yaml`, all of it:

```yaml
name: todo

services:
  frontend:
    build: ./frontend
    ports:
      - "8080:80"
    depends_on:
      - backend

  backend:
    build: ./backend
    environment:
      DB_HOST: db
      DB_USER: todo
      DB_PASSWORD: secret
      DB_NAME: todo
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: todo
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: todo
    volumes:
      - data:/var/lib/postgresql/data
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "todo"]
      interval: 2s
      retries: 10

volumes:
  data:
```

Put it next to page 2's commands, and you'll see they say the same things.

## Line by line

**`name: todo`**: the **project** name. Compose puts it in front of everything it makes: containers `todo-frontend-1`, `todo-backend-1`, `todo-db-1`, network `todo_default`, volume `todo_data`.

**`services:`**: the parts of the app. Each **service** becomes a container. We have three: `frontend`, `backend`, `db`. The service name is also the container's name **on the network**, so the backend can find `db`, and nginx can find `backend`.

**The `frontend` service:**

| Line | Means | On page 2 it was |
| --- | --- | --- |
| `build: ./frontend` | build an image from the `frontend` folder | `docker build -t todo-frontend ./frontend` |
| `ports: - "8080:80"` | door 8080 on your laptop → port 80 inside | `-p 8080:80` |
| `depends_on: - backend` | start `backend` before this one | you, remembering the order |

The `-` at the start of a line means "an item in a list". `ports` is a list because a service can have several doors.

**The `backend` service:**

| Line | Means | On page 2 it was |
| --- | --- | --- |
| `build: ./backend` | build from the `backend` folder | `docker build -t todo-backend ./backend` |
| `environment:` + 4 lines | settings for the app, read with `process.env.DB_HOST` etc. | `-e DB_HOST=db -e ...` |
| `depends_on: db: condition: service_healthy` | don't start until `db` is **healthy** (see below) | nothing: that's why you could see "the database system is starting up" |

No `ports:` at all. The backend stays private.

**The `db` service:**

| Line | Means | On page 2 it was |
| --- | --- | --- |
| `image: postgres:17-alpine` | use this image, don't build anything | the last word of `docker run` |
| `environment:` + 3 lines | make user `todo`, password `secret`, database `todo` | `-e POSTGRES_USER=todo ...` |
| `- data:/var/lib/postgresql/data` | the `data` volume, where Postgres keeps its files | `-v todo-data:/var/lib/postgresql/data` |
| `- ./db/init.sql:/docker-...` | bind mount `init.sql`, so the table is made on first start | `-v "$(pwd)/db/init.sql:..."` |
| `healthcheck:` | how to tell if the database is ready | nothing |

A **healthcheck** is a small test Docker runs inside the container, again and again, to ask "are you ready yet?". Here it runs `pg_isready -U todo` (a tool that comes with Postgres) every 2 seconds, up to 10 times. When it says yes, the container is **healthy**, and only then does Compose start the backend.

**`volumes: data:`**: at the bottom, on its own: "this project needs a volume called `data`". Compose makes it if it isn't there (as `todo_data`). Same as `docker volume create`.

Notice what's **missing**: no `docker network create`. Compose makes a network for every project by itself (`todo_default`) and puts all the services on it.

[Diagram: what docker compose up makes](./compose-makes.excalidraw)

## Try it: start everything

From the `todo-app` folder (clean up page 2 first if you haven't):

```bash
docker compose up -d --build
```

- **`up`**: make and start everything in `compose.yaml`.
- **`-d`**: in the background, like `docker run -d`.
- **`--build`**: build the images first (`frontend` and `backend`). Without it, Compose only builds them the very first time.

You'll see the builds go by, then these lines (between some `Creating` and `Starting` lines):

```
 Network todo_default  Created
 Volume todo_data  Created
 Container todo-db-1  Created
 Container todo-backend-1  Created
 Container todo-frontend-1  Created
 Container todo-db-1  Started
 Container todo-db-1  Waiting
 Container todo-db-1  Healthy
 Container todo-backend-1  Started
 Container todo-frontend-1  Started
```

Read it as a story: network, volume, three containers made. `db` started. Compose **waited** until `db` was **healthy**, and only then started the backend, then the frontend. That's `depends_on` and the healthcheck at work.

## Try it: see what's running

```bash
docker compose ps
```

```
NAME              IMAGE                COMMAND                  SERVICE    CREATED         STATUS                   PORTS
todo-backend-1    todo-backend         "docker-entrypoint.s…"   backend    3 seconds ago   Up 2 seconds
todo-db-1         postgres:17-alpine   "docker-entrypoint.s…"   db         3 seconds ago   Up 3 seconds (healthy)   5432/tcp
todo-frontend-1   todo-frontend        "/docker-entrypoint.…"   frontend   3 seconds ago   Up 2 seconds             0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
```

Like `docker ps`, but only this project's containers. Look at the `PORTS` column: only the frontend has `0.0.0.0:8080->80`, a door to your laptop. `db` shows `5432/tcp`: it listens on 5432, but only inside the network.

Open http://localhost:8080. Your todo app, from one command.

## Page 2 vs page 3

| | By hand (page 2) | Compose (page 3) |
| --- | --- | --- |
| Start | 7 commands | `docker compose up -d --build` |
| Order | you remember it | `depends_on` + healthcheck |
| Settings | typed every time | written once in `compose.yaml` |
| Share with a teammate | send them a list of commands | send them the folder |
| Stop and clean up | 3 commands | `docker compose down` (next page) |

## Check yourself

1. What does each of `up`, `-d` and `--build` do?
2. Why does the backend wait for the database, and how does Compose know the database is ready?
3. Where in `compose.yaml` is the network? (Trick question: why isn't it there?)

## Next

Leave it running. Next: the everyday commands for living with a Compose app: [logs, looking inside, changing code, stopping](04-living-with-compose.md).
