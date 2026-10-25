The **notes app** has three parts, each in its own container:

- **web**: the page you open in the browser
- **api**: takes your note from web and saves it in the database
- **db**: the database, where the notes are kept

```
browser  →  web  →  api  →  db
```

Each part calls the next one **by name**. Open `web/server.js` and `api/server.js` on the left and find the names `api` and `db`.

## What's wrong

The lab already started all three for you, without saying which network to use:

```
docker run -d --name db  notes-db
docker run -d --name api notes-api
docker run -d --name web -p 3300:3000 notes-web
```

Open **http://localhost:3300**. It says **web can't reach the api: ENOTFOUND**. On Docker's default network there's no list of names, so web can't find a computer called `api`.

## Your job

Make the notes app work, **without changing the code**: put all three containers on a network that **you** make. Then save a note.

## Commands that help

```
docker network create <name>
docker network connect <network> <container>
docker network ls
docker inspect <container>
docker ps
```

> On a network you make, Docker keeps a list of names, so `web` finds `api` and `api` finds `db`.
