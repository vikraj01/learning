# Which address do I use?

After this page you'll know which address to use from anywhere: from your laptop, or from one container to another. You'll also have tried the three mistakes everyone makes, so you'll recognise them.

You need `web` and `db` running on `counter-net` from the last page.

## It depends on where you're standing

"Room 2" means one thing in your building and another thing in the building next door. Addresses are the same: what you type depends on **where you are** when you type it.

[Diagram: which address, from where](./which-address.excalidraw)

| You are... | You want... | Use | Why |
| --- | --- | --- | --- |
| on your laptop (browser, terminal) | `web` | `localhost:8080` | `-p 8080:3000` made a door on your laptop |
| on your laptop | `db` | nothing works | `db` has no `-p`, no door |
| inside `web` | `db` | `db:6379` | same network: name + its own port |
| inside a container on another network | `db` | nothing works | not in `counter-net`'s phone book |

The rule:

- **From your laptop**: `localhost` + the **left** side of `-p`.
- **From one container to another**: the container's **name** + the port it listens on **inside** (the **right** side of `-p`). Both must be on the same network.

## A new flag: `-e`

The app reads its database address from `DB_URL`. You can give it a different one when starting a container, with **`-e`** (short for **environment variable**: a setting you pass to a program from outside):

```bash
-e DB_URL=redis://somewhere:1234
```

We'll use that to try each mistake in a second app, `web2`, on door 8081. Your real `web` keeps working on 8080.

## Mistake 1: `localhost`

On your laptop, `localhost` means your laptop. So it's tempting to tell the app "the database is at `localhost:6379`":

```bash
docker run -d --name web2 --network counter-net -p 8081:3000 -e DB_URL=redis://localhost:6379 visit-counter
```

Open http://localhost:8081:

> Could not reach the database at redis://localhost:6379
>
> Reason: ECONNREFUSED

**ECONNREFUSED** means "connection refused": it knocked, and nobody was listening there.

Why? **Inside a container, `localhost` means that container itself.** `web2` knocked on its own port 6379. There's no Redis inside `web2`, so nobody answered. Every container has its own `localhost`.

```bash
docker rm -f web2
```

## Mistake 2: the laptop's door number

Start a second Redis, `db2`, and this time **do** give it a door to your laptop, on 6380:

```bash
docker run -d --name db2 --network counter-net -p 6380:6379 redis:8-alpine
```

Now tell an app to use `db2:6380`, the door number:

```bash
docker run -d --name web2 --network counter-net -p 8081:3000 -e DB_URL=redis://db2:6380 visit-counter
```

http://localhost:8081:

> Could not reach the database at redis://db2:6380
>
> Reason: ECONNREFUSED

Refused again. **6380 is a door on your laptop.** Inside the network, Redis still listens on **6379**. Fix it:

```bash
docker rm -f web2
docker run -d --name web2 --network counter-net -p 8081:3000 -e DB_URL=redis://db2:6379 visit-counter
```

http://localhost:8081:

> Visits so far: **1**

It works. And it's `db2`'s count, separate from `db`'s, because it's a separate database.

## Mistake 3: the wrong network

A container that isn't on `counter-net` can't find `db` at all:

```bash
docker run --rm redis:8-alpine redis-cli -h db PING
```

```
Could not connect to Redis at db:6379: Name does not resolve
```

"Name does not resolve" is Redis's way of saying ENOTFOUND: `db` isn't in this container's phone book. Add `--network counter-net` and it works:

```bash
docker run --rm --network counter-net redis:8-alpine redis-cli -h db PING
```

```
PONG
```

(`PING` → `PONG` is Redis saying "yes, I'm here".)

## Reading the errors

| Error | Means | Usually because |
| --- | --- | --- |
| `ENOTFOUND` / `Name does not resolve` / `bad address` | The name isn't in the phone book | Not on the same network, a typo in the name, or the default network |
| `ECONNREFUSED` | Found the place, but nobody's listening on that port | Used `localhost` inside a container, or the laptop's port instead of the inside one |

## Check yourself

1. Inside a container, what does `localhost` mean?
2. `db` is started with `-p 6380:6379`. Which address do you use from your laptop? Which from `web`?
3. An app says `ENOTFOUND`. What are the first two things you'd check?

## Clean up

```bash
docker rm -f web web2 db db2
docker network rm counter-net
```

## Next

That's Docker networking: networks, names, ports, and where you're standing.

Want to watch all four pages run in one go? From the `04-networking` folder:

```bash
./demo.sh
```

It shows each command, waits for you to press Enter, then runs it. It cleans up after itself.

Tell Vikash what felt easy and what felt confusing.
