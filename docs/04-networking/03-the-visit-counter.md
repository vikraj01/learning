# The visit counter: an app and a database

After this page you'll have a web app in one container talking to a database in another, over a network you made, with the database kept private.

## The idea

A web page that counts how many times it's been opened. Two containers:

- **`web`**: a small Node app. Every time you open the page, it asks the database to add one, and shows you the new number.
- **`db`**: a **database**, a program whose whole job is to keep data safe and hand it out when asked. We use **Redis** (say "RED-iss"), a small, fast database. We only store one number in it, called `visits`.

This is how most real apps look: the app in one container, the database in another, talking over a network.

## A few words first

- **Redis listens on port 6379.** That's its door number *inside* its container, the same way our Node apps listened on 3000.
- **`INCR visits`**: the Redis command for "add one to `visits`, and tell me the new number".
- **`redis://db:6379`**: the address the app uses to find the database. `redis://` says what kind of thing is there, `db` is the container's **name**, and `6379` is its port.

## Try it: make the app

Make a folder and go into it:

```bash
mkdir visit-counter
cd visit-counter
```

Make `app.js`:

```js
const express = require("express");
const { createClient } = require("redis");

const app = express();

// Where the database is. "db" is the name of the Redis container.
const DB_URL = process.env.DB_URL || "redis://db:6379";

app.get("/", async (req, res) => {
  const db = createClient({ url: DB_URL, socket: { reconnectStrategy: false } });
  db.on("error", () => {});

  try {
    await db.connect();
    const visits = await db.incr("visits");
    await db.close();
    res.send(`<h1>Visit counter</h1><p>Visits so far: <b>${visits}</b></p>`);
  } catch (error) {
    res.send(`<h1>Visit counter</h1><p>Could not reach the database at ${DB_URL}</p><p>Reason: ${error.code || error.message}</p>`);
  }
});

app.listen(3000, () => {
  console.log(`Visit counter is running on port 3000, using the database at ${DB_URL}`);
});
```

Read it in three pieces:

1. **`DB_URL`**: where the database is. Normally `redis://db:6379`. (`process.env.DB_URL ||` means "unless someone gives a different address when starting the container". We'll use that on the next page.)
2. **The `/` route**: connect to the database, `incr("visits")` to add one, close the connection, and show the number. `await` means "wait for the database to answer before going on".
3. **If anything goes wrong** (`catch`): show where it tried to go and why it failed, instead of crashing. This will help us a lot.

Make the `Dockerfile`. Same as before, but `npm install` gets the Redis helper package too:

```dockerfile
FROM node:24-slim
WORKDIR /app
RUN npm install express redis
COPY app.js .
CMD ["node", "app.js"]
```

Build it:

```bash
docker build -t visit-counter .
```

## Try it: first, without a network

Run both on the default network, the way you'd have done before this section:

```bash
docker run -d --name db redis:8-alpine
docker run -d --name web -p 8080:3000 visit-counter
```

`redis:8-alpine` is the official Redis image, ready to use; we don't build it. Open http://localhost:8080:

> **Visit counter**
>
> Could not reach the database at redis://db:6379
>
> Reason: ENOTFOUND

**ENOTFOUND** means "name not found". It's the same problem as `ping box1` on page 1: no phone book on the default network, so `db` means nothing. Clean up:

```bash
docker rm -f web db
```

## Try it: on their own network

```bash
docker network create counter-net
docker run -d --name db --network counter-net redis:8-alpine
docker run -d --name web --network counter-net -p 8080:3000 visit-counter
```

Look closely at what's different:

- Both have **`--network counter-net`**, so they're in the same building, with a phone book.
- The database container is called **`db`**, which is exactly the name in `redis://db:6379`.
- Only `web` has **`-p`**. `db` has no door to your laptop at all. It doesn't need one: only `web` talks to it, from inside the network.

Open http://localhost:8080:

> **Visit counter**
>
> Visits so far: **1**

Refresh a few times: 2, 3, 4...

## What happens on each visit

[Diagram: one page visit, step by step](./visit-counter-flow.excalidraw)

1. Your browser opens `localhost:8080`.
2. The `-p 8080:3000` door passes it to `web`, on port 3000.
3. `web` needs `db`. It asks Docker's phone book "where is db?" and gets back its number.
4. `web` sends `INCR visits` to that number, on port 6379.
5. `db` adds one and answers with the new number.
6. `web` puts the number in a page and sends it back to your browser.

All that, in a blink, every time you refresh.

## Try it: look inside the database

`db` has no door to your laptop. To talk to it, start a **third** container on the same network, with Redis's own command-line tool, `redis-cli`:

```bash
docker run --rm -it --network counter-net redis:8-alpine redis-cli -h db
```

- `--rm`: remove this container when you leave it.
- `-it`: you'll be typing into it (you met `-it` in section 2).
- `redis-cli -h db`: start the Redis tool and connect to the **host** (machine) called `db`. A name again, and the phone book finds it.

You'll get a Redis prompt. Type these:

```
db:6379> GET visits
"4"
db:6379> SET visits 100
OK
db:6379> exit
```

`GET` reads the number; `SET` changes it. Now refresh http://localhost:8080:

> Visits so far: **101**

You changed the database from a third container, and `web` saw it.

## Try it: replace the app, keep the count

```bash
docker rm -f web
docker run -d --name web --network counter-net -p 8080:3000 visit-counter
```

Refresh: **102**. The app container is brand new, but the count lives in `db`, not in `web`.

## Check yourself

1. Why does `db` not need `-p`?
2. What do `db` and `6379` mean in `redis://db:6379`?
3. Without `--network counter-net`, what error did the page show? Why?
4. If you remove `db` and start a new one, what happens to the count? (Hint: section 2.) How could you keep it?

## Next

Leave `web` and `db` running. Next: the mistakes everyone makes with addresses, and the rule that fixes them: [which address do I use?](04-which-address.md)
