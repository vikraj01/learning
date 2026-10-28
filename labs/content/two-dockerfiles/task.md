One app often needs **two** images:

- the **real** one, to ship: the code baked in, nothing extra.
- a **dev** one, to work on the code: it restarts by itself when you save a file.

Two recipes, so two Dockerfiles in one folder. Docker only looks for the name `Dockerfile` by itself; for any other name you point at it with **`-f`** (for "file"):

```
docker build -t greet-f:1.0 .                         # uses Dockerfile
docker build -f Dockerfile.dev -t greet-f:dev .       # uses Dockerfile.dev
```

The `.` at the end is still the folder the files come from. `-f` only picks the recipe.

## Your job

1. Build the real image from `Dockerfile` as `greet-f:1.0`. Don't change `Dockerfile`.
2. Make `Dockerfile.dev`: the same, but `ENV COLOR=lightyellow` and `CMD ["--watch", "app.js"]`. Build it as `greet-f:dev`.
3. Run `greet-dev` from `greet-f:dev` on **http://localhost:3406**, with this folder bind-mounted on `/app`.
4. Change `Hello` to `Hi` in `app.js` and see the page change, with no rebuild.

## Why it works

- **`node --watch app.js`** restarts the app whenever `app.js` changes.
- **`-v "$(pwd)":/app`** puts this folder over the image's `/app`, so the container sees your file the moment you save it.

## Commands that help

```
docker build -f Dockerfile.dev -t greet-f:dev .
docker run -d --name greet-dev -p 3406:3000 -v "$(pwd)":/app greet-f:dev
docker logs -f greet-dev
docker images greet-f
```
