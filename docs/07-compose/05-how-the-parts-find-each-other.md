# How the parts find each other

After this page you'll know how the frontend finds the backend and the backend finds the database, why only the frontend has a door, and what happens when one part stops.

Everything here is section 4 (networking), happening inside a Compose app. You need the todo app running.

## Compose made a network for you

On page 2 you typed `docker network create todo-net`. With Compose you didn't, but there is one:

```bash
docker network inspect todo_default --format '{{range .Containers}}{{.Name}} {{.IPv4Address}}{{"\n"}}{{end}}'
```

```
todo-backend-1 172.23.0.3/16
todo-db-1 172.23.0.2/16
todo-frontend-1 172.23.0.4/16
```

(The `--format` part picks just the names and addresses out of the long output. Copy it as it is.) Three containers, each with its own number, on the network `todo_default`. Your numbers may be different.

## Service names are phone-book names

On this network, each container can be found by its **service name**, the name in `compose.yaml`. Ask the backend where `db` is:

```bash
docker compose exec backend getent hosts db
```

```
172.23.0.2      db
```

`getent hosts` asks the phone book, like `nslookup` did in section 4. And the frontend, where's `backend`?

```bash
docker compose exec frontend getent hosts backend
```

```
172.23.0.3        backend  backend
```

That's how the code finds things:

- **The backend → the database.** `compose.yaml` sets `DB_HOST: db`, and `backend/app.js` uses `process.env.DB_HOST`. Check what the backend sees:

  ```bash
  docker compose exec backend printenv DB_HOST DB_USER DB_NAME
  ```

  ```
  db
  todo
  todo
  ```

- **The frontend → the backend.** `frontend/nginx.conf` passes `/api/` on to `http://backend:3000`:

  ```nginx
  location /api/ {
    resolver 127.0.0.11 valid=5s;      # Docker's phone book: look "backend" up again every 5s
    set $backend http://backend:3000;
    proxy_pass $backend;
  }
  ```

  `127.0.0.11` is Docker's DNS, the same phone book from section 4. nginx asks it where `backend` is, and asks again every 5 seconds, so it still finds the backend after you rebuild it and it gets a new number.

You can even play the frontend's part yourself, and ask the backend directly from inside the frontend container:

```bash
docker compose exec frontend wget -qO- http://backend:3000/api/todos
```

```
[{"id":1,"text":"Learn Docker Compose","done":false},{"id":2,"text":"Make chai","done":false}]
```

(`wget -qO-` fetches an address and prints what comes back, like a tiny browser.) A name, plus the port the backend listens on **inside**: 3000. Section 4's rule again.

[Diagram: three parts, one request](./todo-architecture.excalidraw)

## Only one door

From your laptop, the frontend is at `localhost:8080`. Now try the backend and the database from your browser:

- http://localhost:3000/api/todos
- http://localhost:5432

Both: **"This site can't be reached"**. (If 3000 does answer, something else of yours is using that door, like the message box from section 2. Stop it and try again.) There's no `ports:` for `backend` or `db` in `compose.yaml`, so they have no door to your laptop. That's on purpose:

- Nobody outside can talk to the database directly. Only the backend can, and the backend only does the four things in its API.
- There's one way in, through nginx. One door is easier to watch and protect than three.

| From | To | Address | Works? |
| --- | --- | --- | --- |
| your browser | frontend | `localhost:8080` | ✓ the only door |
| your browser | backend | `localhost:3000` | ✗ no door |
| frontend (nginx) | backend | `backend:3000` | ✓ same network |
| backend | db | `db:5432` | ✓ same network |
| your browser | db | `localhost:5432` | ✗ no door |

## When one part stops

Each part is its own container, so each can stop on its own. Stop just the kitchen:

```bash
docker compose stop backend
```

Open http://localhost:8080. The page still loads (nginx is fine), but it stays on **Loading...** with no list: it asked for the todos and got nothing back. Open http://localhost:8080/api/todos to see why:

```
502 Bad Gateway
```

**502 Bad Gateway** is nginx saying "I passed your request on, but there was nobody there to answer".

Start it again:

```bash
docker compose start backend
```

Give it a few seconds (nginx checks the phone book every 5), refresh, and the list is back. Nothing was lost: the todos are in the database, and the database never stopped.

## Check yourself

1. How does the backend know the database is called `db`? Where is that written?
2. Why can't your browser open `localhost:3000`, even though the backend is running?
3. The page says **Loading...** forever. Which part would you check first, and with which command?

## Clean up

```bash
docker compose down
```

(Add `-v` if you want a fresh database next time.)

## Next

That's a real app: frontend, backend and database, started with one command, talking over a network, with its data in a volume. To watch it all run in one go, from the `07-compose` folder:

```bash
./demo.sh
```

It shows each command, waits for you to press Enter, then runs it.

Tell Vikash what felt easy and what felt confusing.
