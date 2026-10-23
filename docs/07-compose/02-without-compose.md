# Running it by hand

After this page you'll have the todo app running with plain `docker` commands, and you'll see why people don't like doing it this way.

You know every command on this page already. There are just a lot of them.

## Before you start

Go into the project folder:

```bash
cd docs/07-compose/todo-app
```

## Step 1: a network and a volume

The three containers need to find each other by name, so they need their own network (section 4). The database needs a volume to keep its data (section 2).

```bash
docker network create todo-net
docker volume create todo-data
```

## Step 2: build two images

The frontend and backend are ours, so we build them. The database is the official `postgres` image; nothing to build.

```bash
docker build -t todo-frontend ./frontend
docker build -t todo-backend ./backend
```

`./frontend` means "the Dockerfile and files are in the `frontend` folder", instead of `.` for "this folder".

## Step 3: start the database

Take a breath, it's a long one:

```bash
docker run -d --name db --network todo-net \
  -e POSTGRES_USER=todo -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=todo \
  -v todo-data:/var/lib/postgresql/data \
  -v "$(pwd)/db/init.sql:/docker-entrypoint-initdb.d/init.sql" \
  postgres:17-alpine
```

(The `\` at the end of a line means "the command carries on on the next line".)

- `--name db`: the name the backend will look for. It must be exactly `db`.
- The three `-e` settings tell Postgres to make a user `todo` with password `secret`, and a database called `todo`.
- `-v todo-data:/var/lib/postgresql/data`: the volume, where Postgres keeps its files.
- The second `-v` is a bind mount of one file: Postgres runs whatever it finds in `/docker-entrypoint-initdb.d/` the first time it starts, so `init.sql` makes our table.

## Step 4: start the backend

```bash
docker run -d --name backend --network todo-net \
  -e DB_HOST=db -e DB_USER=todo -e DB_PASSWORD=secret -e DB_NAME=todo \
  todo-backend
```

The same user, password and database name again, so the backend can log in. `DB_HOST=db` is where to find the database: by name. No `-p`: the backend stays private.

## Step 5: start the frontend

```bash
docker run -d --name frontend --network todo-net -p 8080:80 todo-frontend
```

The only container with a door: `-p 8080:80`.

## Try it

Open http://localhost:8080. Add a todo, tick one, delete one.

Now open the API on its own: http://localhost:8080/api/todos. You'll see the raw JSON the frontend works with, something like:

```json
[{"id":1,"text":"Learn Docker Compose","done":false},{"id":2,"text":"Make chai","done":false},{"id":3,"text":"Water the plants","done":false}]
```

If you were very quick after step 3, you may have seen an error page instead, starting with one of these:

```
Error: connect ECONNREFUSED 172.23.0.2:5432
error: the database system is starting up
```

Postgres takes a few seconds to get ready. At first nobody's listening on 5432 yet (ECONNREFUSED, from section 4), then Postgres is there but still getting ready. Nothing made the backend wait. Refresh and it's fine. Keep that in mind: page 3 fixes it properly.

## Count the work

To **start** the app you typed: 1 network, 1 volume, 2 builds, 3 long `docker run` commands. Seven commands, and you had to remember:

- the **order**: network and volume first, the database before the backend;
- the **names**: `db` and `backend` must be exactly right, because the code and `nginx.conf` look for them;
- the **same settings in two places**: user, password and database name, for both Postgres and the backend;
- which container gets `-p`, and which doesn't.

Now **stop** it all:

```bash
docker rm -f frontend backend db
docker network rm todo-net
docker volume rm todo-data
```

And tomorrow, to start it again, the same seven commands.

Imagine an app with ten parts. Or a teammate who has to type all this to try your app. There has to be a better way.

## Check yourself

1. Why must the database container be called exactly `db`?
2. Which container has `-p`, and why only that one?
3. Name two things that are easy to get wrong when you start the app by hand.

## Next

Write all of this down **once**, in one file, and start everything with one command: [compose.yaml](03-compose-yaml.md).
