The Dockerfile ends with `CMD ["node", "app.js"]`. Anything after the image name in `docker run` replaces the **whole** line, `node` included.

An **`ENTRYPOINT`** is the part of the start command that **stays**. Split the line in two:

```dockerfile
ENTRYPOINT ["node"]
CMD ["app.js"]
```

Now a container runs `ENTRYPOINT` + `CMD`: `node app.js`. Words after the image name replace only the `CMD` part, and `node` stays in front of them.

| You type | It runs |
| --- | --- |
| `docker run greet-ep` | `node app.js` |
| `docker run greet-ep say.js` | `node say.js` |
| `docker run greet-ep --version` | `node --version` |

## Your job

1. Change the Dockerfile to use `ENTRYPOINT ["node"]` and `CMD ["app.js"]`. Build it as `greet-ep`.
2. Run `ep-web` from it with no command, on **http://localhost:3405** (port **3000** inside).
3. Run `ep-say` from it, so it runs `say.js` with `NAME=Asha`.
4. Find out which Node version is inside, and write it in `version.txt`.

## Commands that help

```
docker build -t greet-ep .
docker image inspect -f '{{.Config.Entrypoint}} {{.Config.Cmd}}' greet-ep
docker run --rm greet-ep --version
docker logs ep-say
```

> Want to replace the `ENTRYPOINT` too? That's a separate flag: `docker run --rm -it --entrypoint bash greet-ep`.
