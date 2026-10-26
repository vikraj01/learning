# The `.env` file and Docker

After this page you'll be able to make the app inside a container use your `.env` file, in two different ways, and know why one of them gives a surprise.

## The note is at home, the app is away

On page 2 the note (`.env`) and the reader (`app.js`) were in the same folder. Now the app lives inside a container, and the note is still in your `greet` folder on your laptop. The container can't see your folder.

Same two choices as on page 2, just with Docker in the middle:

| | Page 2 (no Docker) | This page (Docker) |
| --- | --- | --- |
| **Way 1: someone reads it for the app** | `node --env-file=.env app.js` | `docker run --env-file .env ...` |
| **Way 2: the app reads it itself** | `process.loadEnvFile()` | put the file inside the container, then `process.loadEnvFile()` |

[Diagram: two ways the .env file reaches the app](./env-file-docker.excalidraw)

Your `.env` file, from page 2:

```
NAME=Tanvi
COLOR=pink
```

## Way 1: Docker reads the file (`--env-file`)

```bash
docker run --rm -d -p 3000:3000 --env-file .env --name greet greet
docker logs greet
```

```
Saying hello to Tanvi on port 3000
```

Open <http://localhost:3000>: **pink** page, **Hello, Tanvi!**

What happened, step by step:

1. Docker opens `.env` **on your laptop**.
2. It turns each line into an environment variable for the container, exactly like `-e NAME=Tanvi -e COLOR=pink`.
3. The container starts. `app.js` finds them in `process.env`.

The file itself never goes into the container. Check:

```bash
docker exec greet ls -a
```

```
.
..
app.js
say.js
```

No `.env` in there. The app got the settings, not the file. And because Docker made them real environment variables, `COLOR=pink` beat the image's `ENV COLOR=lightblue`, the same as `-e` did on page 3.

```bash
docker stop greet
```

## Way 2: the app reads the file itself

`app.js` already knows how to read a `.env` file (the `loadEnvFile()` lines from page 2). It just needs the file to be **inside the container**, in `/app`, next to `app.js`. A bind mount does that: it shows one file from your laptop inside the container.

```bash
docker run --rm -d -p 3000:3000 -v "$(pwd)/.env:/app/.env" --name greet greet
docker exec greet ls -a
```

```
.
..
.env
app.js
say.js
```

Now `.env` is there. `app.js` sees it and loads it:

```bash
docker logs greet
```

```
Saying hello to Tanvi on port 3000
```

Open <http://localhost:3000>: **Hello, Tanvi!** ...on a **light blue** page. Not pink.

### Why not pink?

Remember the rule from page 2: **a setting that's already in the environment always wins; the file only fills in what's missing.**

Inside this container, `COLOR=lightblue` is already a real environment variable: the Dockerfile's `ENV` line put it there. So when `app.js` loads the file:

- `NAME`: not set yet → taken from the file → `Tanvi`
- `COLOR`: already `lightblue` → the file's `pink` is ignored

Way 1 didn't have this problem, because there Docker made `COLOR=pink` a real environment variable, and that beats `ENV`.

```bash
docker stop greet
```

## Don't copy `.env` into the image

A third idea comes up sooner or later: `COPY .env .` in the Dockerfile. Don't. The file would be baked into the image, and anyone who gets the image can read every password in it. It would also be the same for everyone, which is the opposite of what settings are for.

That's why our Dockerfile copies only `app.js` and `say.js`.

## Which one to use?

| | Way 1: `--env-file` | Way 2: bind mount + app reads it |
| --- | --- | --- |
| Who reads `.env` | Docker | `app.js` |
| Is the file inside the container? | no | yes, at `/app/.env` |
| Beats `ENV` in the Dockerfile? | yes | no (file only fills gaps) |
| App needs code to read files? | no | yes (`loadEnvFile` or dotenv) |

**Way 1 is the usual Docker way.** The app stays simple (it just reads `process.env`), and the settings behave like `-e`. You'll meet it again in Compose as `env_file:`.

Way 2 is worth knowing because many apps (anything using dotenv) read `.env` themselves. When such an app runs in Docker and "ignores" your file, now you know where to look.

## Check yourself

1. In Way 1, is there a `.env` file inside the container? In Way 2?
2. With the bind mount, why does the page say **Tanvi** but stay **light blue**?
3. You want the bind-mount way to give a pink page. What could you change? (There's more than one answer.)

## Next

That's environment variables done. Next section: [Tags: giving images versions](../10-tags/01-tags.md).

Finished files for this section: [`09-env/greet/`](greet/).
