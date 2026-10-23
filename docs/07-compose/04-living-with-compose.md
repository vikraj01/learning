# Living with a Compose app

After this page you'll be able to watch the logs, look inside the database, fix a bug and ship the fix, and stop the app without losing your data.

You need the todo app running from the last page (`docker compose up -d --build`, in the `todo-app` folder). Every `docker compose` command on this page is run from that folder: Compose finds `compose.yaml` in the folder you're in.

## Watch the logs

```bash
docker compose logs -f
```

- **`logs`**: what all three containers have printed, mixed together. Each line starts with the service it came from.
- **`-f`** (follow): keep watching, and show new lines as they come.

Now add a todo in the browser, and tick one. New lines appear as you click:

```
frontend-1  | 172.23.0.1 - - [23/Oct/2026:18:45:29 +0000] "POST /api/todos HTTP/1.1" 201 47 ...
frontend-1  | 172.23.0.1 - - [23/Oct/2026:18:45:29 +0000] "PATCH /api/todos/1 HTTP/1.1" 200 50 ...
```

That's nginx writing down every request: who asked (`172.23.0.1`, your browser coming in through the door), when, what (`POST /api/todos`), and the answer (`201` created, `200` OK).

Press `Ctrl + C` to stop watching. Only the watching stops; the app keeps running.

One service only:

```bash
docker compose logs backend
```

```
backend-1  | Backend is running on port 3000, database at db
```

## Look inside the database

`docker compose exec` is `docker exec` for a service: you use the **service** name (`db`), not the container name.

```bash
docker compose exec db psql -U todo -c "SELECT * FROM todos ORDER BY id;"
```

- **`psql`**: Postgres's own command-line tool, already inside the `db` container.
- **`-U todo`**: log in as the user `todo`.
- **`-c "..."`**: run this one SQL command. `SELECT *` means "every column"; `ORDER BY id` means "in order of id".

```
 id |         text         | done
----+----------------------+------
  1 | Learn Docker Compose | t
  2 | Make chai            | f
  3 | Water the plants     | f
(3 rows)
```

The real table, straight from the pantry. `t` and `f` are true and false: ticked or not.

(To stay and type SQL, leave off the `-c "..."` part: `docker compose exec db psql -U todo`. You get a `todo=#` prompt. Type `\q` to leave. `docker compose exec` gives you `-it` by itself.)

## Find a bug

In the browser, click **Add** with the text box **empty**. A blank todo appears in the list. Look in the table:

```bash
docker compose exec db psql -U todo -c "SELECT * FROM todos ORDER BY id;"
```

```
 id |         text         | done
----+----------------------+------
  1 | Learn Docker Compose | t
  2 | Make chai            | f
  3 | Water the plants     | f
  4 |                      | f
(4 rows)
```

Row 4 has no text. The backend saves whatever it's given, even nothing. Delete the blank one in the browser with its **×**.

## Fix it, and ship the fix

The backend is the right place to check, because it's the one that writes to the database. Open `backend/app.js` and add four lines at the top of the "Add a todo" route:

```js
// Add a todo
app.post("/api/todos", async (req, res) => {
  if (!req.body.text || req.body.text.trim() === "") {
    res.status(400).json({ error: "A todo needs some text" });
    return;
  }
  const result = await db.query(
```

In plain words: "if there's no text, or only spaces (`trim()` cuts spaces off the ends), answer **400** (bad request) with a short reason, and stop."

The container still runs the **old** code: the image was built before you changed the file. Build and restart with the same command as before:

```bash
docker compose up -d --build
```

```
 Container todo-db-1  Running
 Container todo-backend-1  Recreate
 Container todo-backend-1  Recreated
 Container todo-frontend-1  Recreate
 Container todo-frontend-1  Recreated
 Container todo-db-1  Waiting
 Container todo-db-1  Healthy
 Container todo-backend-1  Started
 Container todo-frontend-1  Started
```

Compose only redoes what changed. The backend image changed, so the backend container was replaced (**Recreate**). The frontend depends on the backend, so it was restarted too. `db` didn't change at all: **Running**, untouched, data and all.

Click **Add** with an empty box again. Nothing is added. The fix is live.

## Stop: `down`

```bash
docker compose down
```

```
 Container todo-frontend-1  Removed
 Container todo-backend-1  Removed
 Container todo-db-1  Removed
 Network todo_default  Removed
```

(Plus `Stopping`, `Stopped` and `Removing` lines.) All three containers and the network are gone. `docker compose ps` shows nothing.

But the **volume** is still there:

```bash
docker volume ls
```

```
DRIVER    VOLUME NAME
local     todo_data
```

Start again, and open http://localhost:8080:

```bash
docker compose up -d
```

Your todos are all still there, ticks included. New containers, same volume.

## Wipe: `down -v`

```bash
docker compose down -v
```

```
 Volume todo_data  Removed
 Network todo_default  Removed
```

**`-v`** also deletes the project's volumes. Start again:

```bash
docker compose up -d
```

Open http://localhost:8080: only **Learn Docker Compose** and **Make chai**, unticked. The volume was new and empty, so Postgres ran `init.sql` again, just like the very first time.

[Diagram: down vs down -v](./down-vs-down-v.excalidraw)

## The everyday commands

| Command | What it does |
| --- | --- |
| `docker compose up -d --build` | build what changed, start everything |
| `docker compose ps` | what's running in this project |
| `docker compose logs -f` | watch everything the containers print |
| `docker compose logs backend` | one service's logs |
| `docker compose exec db psql -U todo` | open a tool inside a running service |
| `docker compose down` | remove containers + network, **keep** the data |
| `docker compose down -v` | remove the data too |

## Check yourself

1. You changed `backend/app.js`, but the app still behaves the old way. What did you forget?
2. Why did `db` say **Running** when you rebuilt?
3. You want to stop for the night and carry on tomorrow. `down` or `down -v`?

## Next

Leave it running. Last page: how the three parts actually find each other, and why only one of them has a door: [how the parts find each other](05-how-the-parts-find-each-other.md).
