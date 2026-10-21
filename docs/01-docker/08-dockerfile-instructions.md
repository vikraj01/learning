# What each line of a Dockerfile means

After this page you'll be able to read a simple Dockerfile and know what every line does.

## A slightly bigger recipe

Your first Dockerfile had two lines. Here's one with six. It serves your same `index.html`, but this time with a small web server that comes with Python, instead of nginx.

```dockerfile
FROM python:3.12-slim
WORKDIR /site
COPY index.html .
RUN date > built-at.txt
EXPOSE 8000
CMD ["python", "-m", "http.server", "8000"]
```

You don't need to know Python for this. Python is the starting point here, like nginx was before.

## Line by line

Each line starts with an **instruction** (the word in capitals).

| Instruction | What it means | Here |
| --- | --- | --- |
| `FROM` | Which image to start from. Every Dockerfile begins with this. | Start from an image that has Python 3.12 installed. |
| `WORKDIR` | "Go into this folder" inside the image (and make it if it's missing). Later lines happen here. | Work in `/site`. |
| `COPY` | Copy files from your folder into the image. | Copy `index.html` into `.`, which means "the current folder", so `/site`. |
| `RUN` | Run a command **while building** the image. The result is saved in the image. | Write today's date and time into a file called `built-at.txt`. |
| `EXPOSE` | A note saying which door the app listens on. It does **not** open the door by itself; you still need `-p`. | The server listens on door 8000. |
| `CMD` | The command to start **when a container runs**. | Start Python's built-in web server on door 8000. |

## RUN vs CMD

This is the one people mix up:

- **`RUN`** happens once, at **build** time. Its result gets baked into the image.
- **`CMD`** happens every time a container **starts**.

The `built-at.txt` file shows this: it holds the time you *built* the image, not the time you ran it.

## Try it

Put this Dockerfile in your `my-site` folder (replacing the old one), then build and run it:

```bash
docker build -t my-site:v2 .
docker run -d --name my-web2 -p 8000:8000 my-site:v2
```

- **`my-site:v2`**: the part after `:` is a **tag**, like a version label. Before, Docker used `latest` for you.

Open:

- `http://localhost:8000`: your page.
- `http://localhost:8000/built-at.txt`: the build time, something like `Tue Oct 20 11:35:23 UTC 2026`.

Then:

1. Stop and remove the container, and run it again. Does `built-at.txt` change? Why not?
2. Build again (without changing anything), then run again. Does it change now? Look at the build output: you'll see **CACHED** next to the steps. Docker remembers steps it has already done and skips them if nothing before them changed.
3. Now edit `index.html`, then build and run again. Does `built-at.txt` change this time?
4. Clean up: `docker rm -f my-web2`.

## Check yourself

1. Which instruction must every Dockerfile start with?
2. Does `EXPOSE 8000` let your browser in on its own?
3. In your own words: when does `RUN` happen, and when does `CMD` happen?

## Next

That's the Docker basics done. Ask Vikash what's next.
