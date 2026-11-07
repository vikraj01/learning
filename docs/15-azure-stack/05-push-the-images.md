# 5. Push the images

The VM needs the web and api images. It can't see your laptop, so they go through **Docker Hub**: a website that stores images. You **push** from the laptop, the VM **pulls**.

Same idea as `postgres:17-alpine`: you never built that one, Docker pulled it from Docker Hub. Now your own images go there too.

## The code change: the port comes from the environment

In section 14 the app read `API_URL` and the database settings from environment variables, but the ports were fixed in the code (`app.listen(3000, ...)`). Now the port is a setting too, in `notes-app/web/server.js`:

```js
// Which port to listen on. Comes from the environment too, 3000 if not set.
const PORT = process.env.PORT || 3000;
app.listen(PORT, "0.0.0.0", () => console.log(`web on port ${PORT}, api at ${API_URL}`));
```

`notes-app/api/server.js` does the same, with 4000. Nothing in the code is tied to one machine any more: everything that can differ comes from outside.

| Variable | Read by | Value on the VM |
| --- | --- | --- |
| `PORT` | web | `3000` |
| `API_URL` | web | `http://api:4000` |
| `PORT` | api | `4000` |
| `DB_HOST` | api | `db` |
| `DB_USER`, `DB_PASSWORD`, `DB_NAME` | api | from `.env` |

## 1. Log in to Docker Hub

Make a free account at hub.docker.com if you don't have one. On your laptop:

```bash
docker login
```

It asks for your Docker Hub name and password (or opens the browser). You type them yourself.

```text
Login Succeeded
```

## 2. Build with your name in the tag

A Docker Hub image name is `<your-name>/<image>:<tag>`. The first part says whose it is.

```bash
cd docs/15-azure-stack/notes-app
export DOCKERHUB_USER=tanvikanwar23     # your Docker Hub name

docker build -t $DOCKERHUB_USER/notes-web:1.0 ./web
docker build -t $DOCKERHUB_USER/notes-api:1.0 ./api
docker images | grep notes-
```

```text
tanvikanwar23/notes-api   1.0   ...   2 seconds ago    140MB
tanvikanwar23/notes-web   1.0   ...   10 seconds ago   135MB
```

!!! note "Mac with an M chip?"
    The VM is an Intel/AMD computer. Build for it with `docker build --platform linux/amd64 ...`, or the VM can't run the image.

## 3. Push

```bash
docker push $DOCKERHUB_USER/notes-web:1.0
docker push $DOCKERHUB_USER/notes-api:1.0
```

```text
The push refers to repository [docker.io/tanvikanwar23/notes-web]
...
1.0: digest: sha256:... size: 1784
```

Open `https://hub.docker.com/u/<your-name>`: both images are there. They're **public**, so the VM can pull them without logging in. Don't put passwords in images (that's why they come from `.env`).

## Changed the code later?

Build with a new tag and push again:

```bash
docker build -t $DOCKERHUB_USER/notes-web:1.1 ./web
docker push $DOCKERHUB_USER/notes-web:1.1
```

Then change `1.0` to `1.1` in `compose.yaml` on the VM and run `docker compose up -d`. The old `1.0` stays on Docker Hub, so you can go back.

## Check yourself

1. Why can't the VM just build from your laptop's folder?
2. What does the `tanvikanwar23/` part of the name mean?
3. Which value does web use for `PORT` if nobody sets it?

Next: [Run the notes app on the VM](06-run-the-notes-app.md).
