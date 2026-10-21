# Every Dockerfile keyword

This page lists every keyword a Dockerfile can use, what each one does, and which ones you'll actually need. Use it as a reference; you don't need to remember it all.

## What's a keyword?

Each line of a Dockerfile starts with a **keyword** (Docker calls them **instructions**), like `FROM` or `COPY`. After it come the details for that step.

- They're written in CAPITALS. Docker would accept lowercase, but everyone uses capitals so they stand out.
- Docker reads them **top to bottom**, one step at a time.
- There are **18** in total. You already know 5.

## All 18 at a glance

| Keyword | What it does | How often you'll use it |
| --- | --- | --- |
| `FROM` | Pick the image to start from. | Every time |
| `WORKDIR` | Pick the folder to work in inside the image. | Almost always |
| `COPY` | Copy files from your laptop into the image. | Almost always |
| `RUN` | Run a command while **building**. | Almost always |
| `CMD` | The command to run when a container **starts**. | Almost always |
| `EXPOSE` | Note which door (port) the app listens on. | Often |
| `ENV` | Set a setting (environment variable) for the app. | Often |
| `ARG` | A setting used only while building. | Sometimes |
| `ENTRYPOINT` | The fixed part of the start command. | Sometimes |
| `USER` | Which user the app runs as. | Sometimes |
| `VOLUME` | Mark a folder as "data goes here". | Sometimes |
| `LABEL` | Stick a note on the image (who made it, what it is). | Sometimes |
| `ADD` | Like `COPY`, plus a few extra tricks. | Rarely |
| `HEALTHCHECK` | A command Docker runs to check the app is OK. | Rarely |
| `SHELL` | Change which shell `RUN` uses. | Rarely |
| `STOPSIGNAL` | Change how Docker asks the app to stop. | Rarely |
| `ONBUILD` | A step saved for images built **from** this one. | Rarely |
| `MAINTAINER` | Old way to say who made the image. Don't use it; use `LABEL`. | Never |

## The 5 you already know

From the message box Dockerfile:

```dockerfile
FROM node:24-slim
WORKDIR /app
RUN npm install express
COPY app.js .
CMD ["node", "app.js"]
```

- **`FROM node:24-slim`**: start from an image that has Node. Every Dockerfile begins with `FROM`.
- **`WORKDIR /app`**: make `/app` and work in it. Every line after this happens in `/app`.
- **`RUN npm install express`**: run a command now, while building. The result is saved in the image.
- **`COPY app.js .`**: copy `app.js` from your folder into the image. `.` means "the current folder" (`/app`).
- **`CMD ["node", "app.js"]`**: what to run when a container starts.

## The ones you'll meet soon

### EXPOSE

```dockerfile
EXPOSE 3000
```

A note that says "this app listens on door 3000". It does **not** open the door. You still need `-p 3000:3000` when you run it. Think of it as a sign on the door, not a key.

### ENV

```dockerfile
ENV NODE_ENV=production
```

Sets an **environment variable**: a named setting the app can read while it runs. `NODE_ENV=production` tells Express "this is the real thing, not a test", so it runs a bit faster.

You can change it when you run a container, without rebuilding:

```bash
docker run -e NODE_ENV=development message-box
```

### ARG

```dockerfile
ARG EXPRESS_VERSION=5
RUN npm install express@${EXPRESS_VERSION}
```

A setting that only exists **while building**. Here it picks which version of Express to install (5 unless told otherwise). Change it at build time:

```bash
docker build --build-arg EXPRESS_VERSION=4 -t message-box .
```

`${EXPRESS_VERSION}` means "put the value of `EXPRESS_VERSION` here".

### ENTRYPOINT

```dockerfile
ENTRYPOINT ["node"]
CMD ["app.js"]
```

`ENTRYPOINT` is the part of the start command that stays fixed. `CMD` is the part that can be swapped. Together they make `node app.js`.

Anything you type after the image name in `docker run` replaces `CMD`, but keeps `ENTRYPOINT`:

```bash
docker run --rm message-box-full -e "console.log('CMD replaced')"
```

```
CMD replaced
```

That ran `node -e "console.log('CMD replaced')"` instead of `node app.js`.

### USER

```dockerfile
USER node
```

Run the app as a normal user called `node` instead of **root** (the all-powerful admin user). It's safer: if someone breaks into the app, they can't do as much. The `node` image comes with a `node` user ready.

Lines after `USER` run as that user, so it usually goes near the end.

### VOLUME

```dockerfile
VOLUME /app/data
```

Says "this folder holds data". If you run the container without a `-v`, Docker makes a nameless volume for that folder by itself. It's a hint; you'll usually still give your own `-v messages:/app/data` so the volume has a name you can find.

### LABEL

```dockerfile
LABEL description="Message box app"
```

A sticky note on the image. It doesn't change how anything runs. You can read it with `docker inspect message-box`.

## The rare ones

You can skip these for now. They're here so the list is complete.

- **`ADD`**: like `COPY`, but it can also download a file from a web address, and it unpacks `.tar` archives by itself. Those surprises are why people prefer `COPY` unless they need the trick.
- **`HEALTHCHECK`**: a command Docker runs every 30 seconds to check the app still answers. `docker ps` then shows `(healthy)` or `(unhealthy)` next to the container.
  ```dockerfile
  HEALTHCHECK CMD node -e "fetch('http://localhost:3000/web').then(r => process.exit(r.ok ? 0 : 1))"
  ```
- **`SHELL`**: `RUN` uses `/bin/sh` to run commands. `SHELL ["/bin/bash", "-c"]` switches it to bash.
- **`STOPSIGNAL`**: when you `docker stop`, Docker sends the app a polite "please stop" message called a **signal**. This changes which one.
- **`ONBUILD`**: a step that doesn't run now, but runs later when someone else writes `FROM your-image`.
- **`MAINTAINER`**: old and replaced by `LABEL`. You might see it in old Dockerfiles.

## Pairs that get mixed up

| These two | The difference |
| --- | --- |
| `RUN` vs `CMD` | `RUN` happens once, at **build** time. `CMD` happens every time a container **starts**. |
| `CMD` vs `ENTRYPOINT` | `CMD` is easy to replace from `docker run`. `ENTRYPOINT` stays. |
| `COPY` vs `ADD` | Use `COPY`. `ADD` only when you need its download or unpack trick. |
| `ARG` vs `ENV` | `ARG` exists only while building. `ENV` is still there when the app runs. |
| `EXPOSE` vs `-p` | `EXPOSE` is a note. `-p` actually connects the door. |
| `VOLUME` vs `-v` | `VOLUME` is a hint in the image. `-v` is you choosing the storage when you run. |

## Two ways to write a command

`RUN`, `CMD` and `ENTRYPOINT` can be written two ways:

```dockerfile
CMD ["node", "app.js"]     # exec form: a list, in square brackets and double quotes
CMD node app.js            # shell form: plain words
```

Use the **list form** for `CMD` and `ENTRYPOINT`; the app then gets the "please stop" signal properly. Plain words are fine for `RUN`.

## Not keywords, but you'll see them

- **`#` comments**: any line starting with `#` is a note for people. Docker skips it.
- **`# syntax=docker/dockerfile:1`**: a special first line telling Docker which Dockerfile version to read with. Optional.
- **`.dockerignore`**: a separate file (next to the Dockerfile) listing files `COPY` should never take, like `node_modules` or `.env`.

## Try it: one Dockerfile with most of them

[`message-box/Dockerfile.full`](message-box/Dockerfile.full) is the message box recipe using most of the keywords:

```dockerfile
# syntax=docker/dockerfile:1

# Start from an image that has Node
FROM node:24-slim

LABEL description="Message box app"

ARG EXPRESS_VERSION=5
ENV NODE_ENV=production

WORKDIR /app
RUN npm install express@${EXPRESS_VERSION}
COPY app.js .

RUN mkdir data && chown node data
VOLUME /app/data

EXPOSE 3000
USER node

HEALTHCHECK CMD node -e "fetch('http://localhost:3000/web').then(r => process.exit(r.ok ? 0 : 1))"

ENTRYPOINT ["node"]
CMD ["app.js"]
```

`RUN mkdir data && chown node data` makes the `data` folder and gives it to the `node` user (`chown` = change owner). Without it, the app running as `node` wouldn't be allowed to write messages.

It's not called `Dockerfile`, so tell `docker build` its name with `-f` (file):

```bash
docker build -f Dockerfile.full -t message-box-full .
docker run -d --name msg-full -p 3000:3000 message-box-full
```

Send a message at `http://localhost:3000/web`, then check:

```bash
docker exec msg-full whoami
```

```
node
```

Wait about 30 seconds, then:

```bash
docker ps
```

The `STATUS` column should say something like `Up 33 seconds (healthy)`.

Clean up:

```bash
docker rm -f -v msg-full
docker rmi message-box-full
```

`-v` on `docker rm` also deletes the nameless volume that `VOLUME` made.

## Check yourself

1. Which keyword must every Dockerfile start with?
2. Does `EXPOSE 3000` mean you can skip `-p 3000:3000`?
3. You want a setting the app can read while it runs. `ARG` or `ENV`?
