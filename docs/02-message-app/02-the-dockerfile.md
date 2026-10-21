# Put the app in a container

After this page your message box runs inside a container, built from a Dockerfile you wrote.

## The recipe

A **Dockerfile** is a recipe for an image. Ours is **5 lines**, and each line is one step.

In your `message-box` folder, make a file called `Dockerfile` (capital D, no ending like `.txt`):

```dockerfile
FROM node:24-slim
WORKDIR /app
RUN npm install express
COPY app.js .
CMD ["node", "app.js"]
```

## The 5 lines, one sentence each

| # | Line | In plain words |
| --- | --- | --- |
| 1 | `FROM node:24-slim` | Start from a ready-made image that already has Node installed. |
| 2 | `WORKDIR /app` | Make a folder called `/app` inside the image and work in it. |
| 3 | `RUN npm install express` | Download Express into the image, like you did on your laptop. |
| 4 | `COPY app.js .` | Copy your `app.js` from your laptop into `/app`. |
| 5 | `CMD ["node", "app.js"]` | When a container starts, run `node app.js`. |

That's all for today. We'll look at each of these more closely another day.

## Try it: build the image

From inside the `message-box` folder:

```bash
docker build -t message-box .
```

- **`-t message-box`**: give the image a name.
- **`.`**: "the recipe and files are in this folder".

The last lines should say something like:

```
naming to docker.io/library/message-box:latest done
```

## Try it: run a container

```bash
docker run -d --name msg -p 3000:3000 message-box
```

- **`-d`**: run in the background, so you get your terminal back.
- **`--name msg`**: call the container `msg`, so it's easy to talk about.
- **`-p 3000:3000`**: connect door 3000 on your laptop to door 3000 in the container (remember port mapping).

See what the app printed when it started:

```bash
docker logs msg
```

```
Message box is running on http://localhost:3000/web
```

Open `http://localhost:3000/web` and send a message. It works the same as before, but now Node is running inside the container, not on your laptop.

Leave the container running. You'll use it on the next page.

## Check yourself

1. How many lines does the Dockerfile have? Which one runs when the container **starts**?
2. Why do we need `-p 3000:3000`?
3. You sent a message. Look in your laptop's `data/messages.txt`. Is the new message there? Why not?

## Next

So where did that message go? [Containers forget](03-containers-forget.md).
