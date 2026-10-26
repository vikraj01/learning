# Two Dockerfiles in one folder: `docker build -f`

After this page you'll be able to keep two Dockerfiles for the same app (one for real use, one for working on it), pick which one to build with `-f`, and know the difference between `-f` and the `.` at the end.

## Two recipe cards, one kitchen

A restaurant kitchen can have two cards for the same dish: the proper one served to guests, and a quick one the cook uses while trying things out. Same kitchen, same ingredients, different card.

Your `greet` folder can have two Dockerfiles in the same way:

- **`Dockerfile`**: the real one. Builds `greet:3.0`, the version you'd give to others. (Some people call this "production".)
- **`Dockerfile.dev`**: for while you're working on the code ("development"). Restarts the app every time you save a file.

## The idea

When you run `docker build`, Docker looks for a file called exactly **`Dockerfile`**. That's why you never had to name it. To use a different file, tell Docker with **`-f`** ("file"):

```bash
docker build -f Dockerfile.dev -t greet:dev .
```

## Try it: write `Dockerfile.dev`

In your `greet` folder, next to `Dockerfile`, make `Dockerfile.dev`:

```dockerfile
FROM node:24-slim
WORKDIR /app
COPY app.js say.js ./
ENV COLOR=lightyellow
EXPOSE 3000
ENTRYPOINT ["node"]
CMD ["--watch", "app.js"]
```

Only two lines differ from `Dockerfile`:

| Line | `Dockerfile` | `Dockerfile.dev` | Why |
| --- | --- | --- | --- |
| `ENV COLOR=` | `lightblue` | `lightyellow` | so you can see at a glance which one you're looking at |
| `CMD` | `["app.js"]` | `["--watch", "app.js"]` | `node --watch` restarts the app when a file changes |

With the `ENTRYPOINT` from section 12, the dev container runs `node` + `--watch app.js`.

Your folder now:

```
greet/
├── app.js
├── say.js
├── .env
├── Dockerfile
└── Dockerfile.dev
```

Build it, with its own tag:

```bash
docker build -f Dockerfile.dev -t greet:dev .
```

## `-f` and the `.` are different things

```
docker build  -f Dockerfile.dev  -t greet:dev  .
                └── which recipe    └── its name  └── which folder
```

- **`-f Dockerfile.dev`**: which recipe to follow.
- **`.`**: the **build context**, the folder Docker is allowed to take files from. `COPY app.js say.js ./` copies from this folder.

They don't have to be the same place. From the folder *above* `greet`, this builds the same image:

```bash
docker build -f greet/Dockerfile.dev -t greet:dev greet
```

The recipe is `greet/Dockerfile.dev`, and the files come from the `greet` folder.

[Diagram: one folder, two Dockerfiles, two images](./two-dockerfiles.excalidraw)

## Try it: run both, side by side

The real one on 3000, the dev one on 3001:

```bash
docker run --rm -d -p 3000:3000 --name greet greet:3.0
docker run --rm -d -p 3001:3000 -v "$(pwd):/app" --name greet-dev greet:dev
```

The dev one has a **bind mount** (section 2): your whole `greet` folder appears as `/app` inside the container. So the container runs *your* `app.js`, the one you're editing, not the copy made during the build.

- <http://localhost:3000>: light blue, **Hello, friend! 👋**
- <http://localhost:3001>: light yellow, **Hello, Tanvi! 👋**

Why `Tanvi` on the dev one? The bind mount brought your `.env` file in too, and `app.js` loads it (section 9, page 4). `NAME` came from the file. `COLOR` stayed `lightyellow`, because the `ENV` line wins over the file. Same rule as before.

## Try it: change the code, watch it restart

Follow the dev container's logs (`-f` here means "follow", a different `-f`):

```bash
docker logs -f greet-dev
```

```
Saying hello to Tanvi on port 3000
```

Now open `app.js` in your editor, change `Hello` to `Hi` in the heading, and save. The logs show:

```
Restarting 'app.js'
Saying hello to Tanvi on port 3000
```

Refresh <http://localhost:3001>: **Hi, Tanvi! 👋**. No build, no restart by you.

Refresh <http://localhost:3000>: still **Hello**. The real image doesn't change until you build it again, with a new tag.

Press `Ctrl+C` to stop following the logs, change `Hi` back to `Hello`, and stop both:

```bash
docker stop greet greet-dev
```

## Names you'll see

`Dockerfile.dev` is one common name. You'll also see `dev.Dockerfile`, or a `docker/` folder with several files in it. They all work the same way: whatever the name, you point at it with `-f`.

## Check yourself

1. You run `docker build -t greet:test .` in the `greet` folder. Which Dockerfile does Docker use?
2. In `docker build -f Dockerfile.dev -t greet:dev .`, what does the `.` mean?
3. Why does editing `app.js` change the page on port 3001 but not on 3000?

## Next

[Compose: all of it in one file](../14-compose-greet/01-compose-greet.md). The commands are getting long.

Finished files for this section: [`13-build-f/greet/`](greet/).
