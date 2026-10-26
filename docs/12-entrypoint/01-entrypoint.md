# ENTRYPOINT: the part you can't replace by accident

After this page you'll know the difference between `ENTRYPOINT` and `CMD`, how they join together into one command, and how to get past `ENTRYPOINT` when you need to.

## The coffee machine

A coffee machine always makes coffee. You don't choose *that*. You only choose the size: small, medium, large. If you press nothing, you get medium.

- The machine itself = **`ENTRYPOINT`**: fixed, always runs.
- The size = **`CMD`**: a default you can change.

## The idea

On the last page, every run of `say.js` needed `node` in front: `docker run greet:2.0 node say.js`. Every program in this image is a Node program, so `node` should just be there, always.

Change the end of your Dockerfile. Replace the `CMD` line with these two:

```dockerfile
ENTRYPOINT ["node"]
CMD ["app.js"]
```

The whole Dockerfile now:

```dockerfile
FROM node:24-slim
WORKDIR /app
COPY app.js say.js ./
ENV COLOR=lightblue
EXPOSE 3000
ENTRYPOINT ["node"]
CMD ["app.js"]
```

- **`ENTRYPOINT ["node"]`**: the program that always runs.
- **`CMD ["app.js"]`**: the default words added after it.

Docker joins them: **`ENTRYPOINT` + `CMD`** = `node` + `app.js` = `node app.js`. Same as before when you type nothing extra.

This is a new version of the image, so give it a new tag:

```bash
docker build -t greet:3.0 .
```

## Try it: what you type replaces only `CMD`

```bash
docker run --rm -p 3000:3000 --name greet greet:3.0
```

```
Saying hello to friend on port 3000
```

`node` + `app.js`. Stop it with `Ctrl+C`. Now type just the file name, no `node`:

```bash
docker run --rm greet:3.0 say.js
```

```
Hello, friend!
```

`node` + `say.js`. And:

```bash
docker run --rm greet:3.0 --version
```

```
v24.22.1
```

`node` + `--version`.

| You type | `ENTRYPOINT` | `CMD` part | The container runs |
| --- | --- | --- | --- |
| `docker run greet:3.0` | `node` | `app.js` (default) | `node app.js` |
| `docker run greet:3.0 say.js` | `node` | `say.js` | `node say.js` |
| `docker run greet:3.0 --version` | `node` | `--version` | `node --version` |
| `docker run greet:3.0 bash` | `node` | `bash` | `node bash` ✗ |

[Diagram: how ENTRYPOINT and CMD make one command](./entrypoint-and-cmd.excalidraw)

## The last row: `bash` doesn't work any more

On the CMD page, `docker run greet:2.0 bash` gave you a shell. Try it on `3.0`:

```bash
docker run --rm greet:3.0 bash
```

```
Error: Cannot find module '/app/bash'
```

(Node prints a few more lines around it; this is the one that matters.)

`bash` only replaced the `CMD` part. `node` stayed, so Docker ran `node bash`, and Node looked for a JavaScript file called `bash`. That's what "can't replace by accident" means.

## Getting past it: `--entrypoint`

When you really do want a different program, say so with `--entrypoint`. It goes **before** the image name:

```bash
docker run --rm -it --entrypoint bash greet:3.0
```

```
root@9a2b4c6d8e0f:/app#
```

A shell. Type `exit` to leave.

## Which one should I use?

- **Only `CMD`**: most apps. Easy to run anything else in its place.
- **`ENTRYPOINT` + `CMD`**: when the image is one tool that should always run, and only its options change. Like our `greet`: always `node`, sometimes `app.js`, sometimes `say.js`.

> **Good to know:** the `node` image already had an `ENTRYPOINT`: a small script called `docker-entrypoint.sh` that just runs your `CMD`. Our `ENTRYPOINT ["node"]` replaced it. Many images (postgres, nginx) use a script like that to set things up before starting the real program. You'll see the name in `docker ps`.

## Check yourself

1. `ENTRYPOINT ["node"]` and `CMD ["app.js"]`. What runs with `docker run greet:3.0 say.js`?
2. Why does `docker run greet:3.0 ls` fail, but `docker run greet:2.0 ls` works?
3. Where does `--entrypoint` go in the command: before or after the image name?

## Next

[Two Dockerfiles in one folder: `docker build -f`](../13-build-f/01-build-f.md).

Finished files for this section: [`12-entrypoint/greet/`](greet/).
