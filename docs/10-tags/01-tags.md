# Tags: giving images versions

After this page you'll be able to keep two versions of the same app side by side, and you'll know what `:latest` really means (it's not what it sounds like).

## essay-v1, essay-v2

When you write an essay and want to change it without losing the old one, you save a copy: `essay-v1.docx`, `essay-v2.docx`. Same essay, two versions, both still there.

Docker does this with **tags**.

## The idea

A full image name has two parts, joined by a colon:

```
greet:2.0
  │    │
  │    └── tag: which version
  └─────── name: which app
```

- The **name** says which app it is: `greet`.
- The **tag** says which version: `1.0`, `2.0`, `dev`, anything you like.

You've used tags all along: in `node:24-slim`, the name is `node` and the tag is `24-slim` (Node 24, small version).

If you don't write a tag, Docker adds **`latest`** for you. So in section 9, `docker build -t greet .` really made `greet:latest`.

> **`latest` is just a word.** It doesn't mean "newest". It's only the tag Docker uses when you don't give one. It never moves by itself.

## Try it: list what you have

```bash
docker images greet
```

```
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
greet:latest   ab9c46957e5d        330MB         81.1MB
```

One image, tagged `latest`. Your ID will be different. (On older Docker the columns look a little different: `REPOSITORY  TAG  IMAGE ID ...`. Same information.)

## Give it a version: `docker tag`

This image is our first version. Give it a proper tag:

```bash
docker tag greet greet:1.0
docker images greet
```

```
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
greet:1.0      ab9c46957e5d        330MB         81.1MB
greet:latest   ab9c46957e5d        330MB         81.1MB
```

Two rows, but look at the ID: **the same**. `docker tag` doesn't copy anything. It sticks a second label on the same image, like two name stickers on one box.

## Make version 2

Change the app a little. In `app.js` (your `greet` folder from section 9), add a wave to the heading:

```js
  <h1>Hello, ${name}! 👋</h1>
```

Build it with a new tag:

```bash
docker build -t greet:2.0 .
docker images greet
```

```
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
greet:1.0      ab9c46957e5d        330MB         81.1MB
greet:2.0      7d41c0f2b9a3        330MB         81.1MB
greet:latest   ab9c46957e5d        330MB         81.1MB
```

`greet:2.0` has a **new** ID: it's a different image. And `latest` is still on the old one, the same ID as `1.0`. It didn't follow the new build.

## Run both versions at once

Each one gets its own port on your laptop and its own container name:

```bash
docker run --rm -d -p 3001:3000 --name greet-1 greet:1.0
docker run --rm -d -p 3002:3000 --name greet-2 greet:2.0
```

- <http://localhost:3001>: **Hello, friend!** (version 1)
- <http://localhost:3002>: **Hello, friend! 👋** (version 2)

Both light blue, both still there. This is why tags matter: if version 2 breaks something, version 1 is right there to go back to.

```bash
docker stop greet-1 greet-2
```

## Move `latest`

If you want `latest` to mean version 2, move it yourself:

```bash
docker tag greet:2.0 greet:latest
docker images greet
```

```
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
greet:1.0      ab9c46957e5d        330MB         81.1MB
greet:2.0      7d41c0f2b9a3        330MB         81.1MB
greet:latest   7d41c0f2b9a3        330MB         81.1MB
```

Now `latest` and `2.0` share an ID.

## Habits worth having

- **Always give a tag** when you build: `docker build -t greet:2.0 .`. Then you know exactly what you're running.
- **Don't trust `latest`** in other people's images either. `node:latest` today and `node:latest` next month can be different Node versions. `node:24-slim` stays Node 24.
- You can give **two tags in one build**: `docker build -t greet:2.0 -t greet:latest .`
- To share an image on Docker Hub, the name starts with your Docker Hub username: `tanvi/greet:2.0`. Same idea, longer name.

From now on we always use a tag: `greet:2.0` (sections 10–11), `greet:3.0` (section 12), `greet:dev` (section 13).

## Check yourself

1. You type `docker run greet`. Which tag does Docker use?
2. After `docker tag greet:2.0 greet:stable`, how many images are there, and how many tags point at `2.0`'s ID?
3. You build `greet:3.0`. Does `greet:latest` change?

## Next

[CMD: what a container runs](../11-cmd/01-cmd.md): the last line of the Dockerfile, and how to replace it.

Finished files for this section: [`10-tags/greet/`](greet/).
