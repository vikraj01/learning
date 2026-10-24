# Networks demo: the notes app

After this page you'll know what a network is, what Docker's default network does, and what changes when containers share a network of their own, or sit on different ones.

## The app

A small notes app in three parts. Each part runs in its own container:

- **web**: the page you open in the browser, on port 3000. You write a note there.
- **api**: gets the note from web and saves it in the database.
- **db**: the database (Postgres). It keeps the notes.

```
 browser  →  web  →  api  →  db
```

Each part calls the next one **by name**. Look in the code:

- `web/server.js`: `const API_URL = "http://api:4000";` means web looks for a computer called **api**.
- `api/server.js`: `const DB_HOST = "db";` means api looks for a computer called **db**.

The files are in `notes-app/`, next to this page.

## What a network is

A **network** is a group of computers connected so they can talk to each other.

Think of a house. People in the same house can call each other by name. People in different houses can't hear each other.

Each container is a small computer of its own. Two containers can only talk if they're in the **same network**, and that's where they find each other by name.

## Build the three images (once)

```bash
cd docs/08-networks-demo/notes-app
docker build -t notes-db ./db
docker build -t notes-api ./api
docker build -t notes-web ./web
```

## Demo 1: the default network

If you don't say which network to use, Docker puts the container on its **default network**. Every container lands there unless you say otherwise.

Start all three without saying anything about networks:

```bash
docker run -d --name db notes-db
docker run -d --name api notes-api
docker run -d --name web -p 3000:3000 notes-web
```

Open <http://localhost:3000>. You'll see:

```
web can't reach the api: ENOTFOUND
```

**ENOTFOUND** means "not found": web looked for a computer called **api** and couldn't find one.

All three are on the same default network, but the default network has **no list of names**. Nobody there can find anyone else by name.

## Every container has an address (IP)

Names don't work on the default network, but **numbers do**. Every container gets its own address, its IP, like a house number. Containers on the **same network** can always reach each other by that number.

Get a container's IP:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db
```

```
172.17.0.3
```

Or list every container on a network, each with its IP:

```bash
docker network inspect bridge -f '{{range .Containers}}{{.Name}} {{.IPv4Address}}{{"\n"}}{{end}}'
```

```
db 172.17.0.3/16
api 172.17.0.4/16
web 172.17.0.5/16
```

`bridge` is the default network's name. For a network you made, use its own name, for example `notes-net`. Your numbers may be different from these.

### Try it: numbers instead of names

The three containers from demo 1 are still running.

1. Get **db**'s IP (the command above).
2. In `api/server.js`, put that number where the name was:

    ```js
    const DB_HOST = "172.17.0.3";
    ```

3. Rebuild api and start it again:

    ```bash
    docker rm -f api
    docker build -t notes-api ./api
    docker run -d --name api notes-api
    ```

4. Get **api**'s IP now. It's a new container, so it may have a new number:

    ```bash
    docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' api
    ```

5. In `web/server.js`, put that number where the name was:

    ```js
    const API_URL = "http://172.17.0.4:4000";
    ```

6. Rebuild web and start it again:

    ```bash
    docker rm -f web
    docker build -t notes-web ./web
    docker run -d --name web -p 3000:3000 notes-web
    ```

Open <http://localhost:3000>. It works ✓, even on the default network.

So why not always use numbers? Because **the number can change**. Every time a container is removed and started again, it may get a different one, and then the code points at the wrong house. A name stays the same. That's why demo 2 uses names.

Before going on, put the names back in both files (`"db"` and `"http://api:4000"`) and rebuild:

```bash
docker rm -f web api db
docker build -t notes-api ./api
docker build -t notes-web ./web
```

## Demo 2: your own network

Make a network of your own and call it `notes-net`:

```bash
docker network create notes-net
```

Start all three on it. `--network notes-net` tells Docker which network to put the container on:

```bash
docker run -d --name db  --network notes-net notes-db
docker run -d --name api --network notes-net notes-api
docker run -d --name web --network notes-net -p 3000:3000 notes-web
```

Wait a few seconds for the database to start, then open <http://localhost:3000>. Write a note and click **Save**. It shows up in the list ✓

This time it works. On a network **you** make, Docker keeps a list of names, so web finds **api** and api finds **db**.

## Demo 3: different networks

Make a second network, then move **db** onto it:

```bash
docker network create other-net
docker rm -f db
docker run -d --name db --network other-net notes-db
```

Reload <http://localhost:3000>:

```
api can't reach the database at "db": ENOTFOUND
```

Read the message carefully:

- **web still reaches api** ✓, because they're both on `notes-net`.
- **api can't find db** ✗, because db is now in a different house, `other-net`.

Put db back on `notes-net`:

```bash
docker rm -f db
docker run -d --name db --network notes-net notes-db
```

Reload: the app works again ✓. Your old note is gone, though. This is a brand-new db container, and containers forget (section 2, page 3).

## Clean up

```bash
docker rm -f web api db
docker network rm notes-net other-net
```

## What you saw

| Where the containers are | Can they find each other by name? |
| --- | --- |
| All on the default network | ✗ no list of names |
| All on your own network | ✓ |
| On different networks | ✗ different houses |

## Questions

1. What network does a container join when you don't say?
2. Why did web find api in demo 2 but not in demo 1?
3. In demo 3, which part still worked, and why?
