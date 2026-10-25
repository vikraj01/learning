The notes app is running, and it works: open **http://localhost:3301**. All three parts are on one network called `notes-all`.

```
browser  →  web  →  api  →  db
```

But there's a problem. **web** only ever needs to talk to **api**, yet it can reach **db** directly. If someone broke into web, the database would be one step away.

## Your job

Split the app into two networks:

| Network | Who's on it |
| --- | --- |
| `front-net` | `web`, `api` |
| `back-net` | `api`, `db` |

`api` sits on **both**, like a door between two rooms. `web` and `db` must share **no** network. The app must still work.

## Commands that help

```
docker network create <name>
docker network connect <network> <container>
docker network disconnect <network> <container>
docker network inspect <network>
```

> You don't need to restart anything: `connect` and `disconnect` plug cables in and out of running containers.
