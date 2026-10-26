# Environment variables in Docker

After this page you'll be able to give a container its settings, put defaults inside the image, and know which one wins when they disagree.

## One image, everyone's own settings

Think of a hotel. Every room is built the same (the **image**). But each guest's key card is set up at the front desk for *their* room and *their* dates (the **settings**). Nobody rebuilds the room for a new guest.

A Docker image is the same for everyone who runs it. Environment variables are how each container gets its own settings.

## Try it: put greet in an image

In your `greet` folder, make a file called `Dockerfile`:

```dockerfile
FROM node:24-slim
WORKDIR /app
COPY app.js say.js ./
ENV COLOR=lightblue
EXPOSE 3000
CMD ["node", "app.js"]
```

You've seen every line before except one:

- **`ENV COLOR=lightblue`** sets an environment variable **inside the image**. Every container made from this image starts with `COLOR=lightblue`, unless you say otherwise.

`COPY` copies only `app.js` and `say.js`. Your `.env` file stays **out** of the image, on purpose. (Page 4 is all about how the container can still use it.)

Build it:

```bash
docker build -t greet .
```

Run it:

```bash
docker run --rm -p 3000:3000 --name greet greet
```

```
Saying hello to friend on port 3000
```

Open <http://localhost:3000>. A **light blue** page says **Hello, friend!**

- `friend`: there's no `.env` file inside the container, so `app.js` skipped `loadEnvFile()` and used its default.
- `lightblue`: nobody typed a colour. It came from the `ENV` line.

Stop it with `Ctrl+C`.

## Give a setting: `-e`

`-e` means "environment". Write it as `-e NAME=value`, **before** the image name. One `-e` per setting:

```bash
docker run --rm -p 3000:3000 -e NAME=Tanvi -e COLOR=pink --name greet greet
```

```
Saying hello to Tanvi on port 3000
```

Pink page, **Hello, Tanvi!** Notice `COLOR=pink` beat the image's `lightblue`. Stop it with `Ctrl+C`.

## Who wins?

| How you start it | `COLOR` the app sees | Why |
| --- | --- | --- |
| `node app.js` (no Docker, no `.env`) | `white` | the default written in `app.js` |
| `docker run ... greet` | `lightblue` | `ENV` in the Dockerfile beats the code's default |
| `docker run ... -e COLOR=pink greet` | `pink` | `-e` beats `ENV` |

From weakest to strongest: **default in the code → `ENV` in the Dockerfile → `-e` on `docker run`**.

Use `ENV` for **sensible defaults** that come with the image. Don't put passwords there: anyone who has the image can read them.

## Look inside: what the container sees

Start it in the background this time (`-d`), then ask the container for its environment:

```bash
docker run --rm -d -p 3000:3000 -e NAME=Tanvi -e COLOR=pink --name greet greet
docker exec greet env
```

```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=40b2cf5eca68
NAME=Tanvi
COLOR=pink
NODE_VERSION=24.22.1
YARN_VERSION=1.22.22
HOME=/root
```

`docker exec greet env` runs the `env` command inside the running container. You can see your two settings, a few that came with the `node` image (`NODE_VERSION`, `PATH`), and one Docker adds (`HOSTNAME`, the container's id). Your `HOSTNAME` will be different.

```bash
docker stop greet
```

## The one that trips everyone up: `PORT`

`PORT` changes the port the app listens on **inside the container**. Port mapping (`-p`) has to follow it. Try the wrong way:

```bash
docker run --rm -d -p 3000:3000 -e PORT=4000 --name greet greet
docker logs greet
```

```
Saying hello to friend on port 4000
```

Open <http://localhost:3000>: the browser shows an error page (something like "didn't send any data"). Door 3000 on your laptop leads to port 3000 inside, but the app is listening on 4000. Nobody's home.

```bash
docker stop greet
docker run --rm -d -p 4000:4000 -e PORT=4000 --name greet greet
```

Now <http://localhost:4000> works. The right side of `-p` must match `PORT`.

```bash
docker stop greet
```

> **Good to know:** `export NAME=Tanvi` on your laptop does **not** reach the container. A container only gets what the image's `ENV` gives it and what you pass when you start it.

## Check yourself

1. The Dockerfile says `ENV COLOR=lightblue` and you run with `-e COLOR=green`. What colour is the page?
2. Your `.env` file is in the `greet` folder, but the page inside Docker still says **Hello, friend!** Why?
3. You run `-p 8080:3000 -e PORT=5000`. Will <http://localhost:8080> work? What would you change?

## Next

[The .env file and Docker](04-env-file-and-docker.md): two ways to make the app in the container use your `.env` file.
