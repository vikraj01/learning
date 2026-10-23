# Layers: what an image is made of

After this page you'll be able to see the layers inside any image, and say which line of a Dockerfile made each one.

## Transparent sheets

Picture an old classroom projector with transparent plastic sheets:

- The first sheet has a drawing of a house.
- You lay a second sheet on top that adds a tree.
- A third sheet adds a cat on the roof.

Look down through all three and you see **one** picture: house, tree, cat. Each sheet only holds what it added.

A Docker image is built the same way. Each sheet is a **layer**: a set of files that one step of the Dockerfile added or changed. Stack them up, and you get the complete set of folders a container starts with.

## A new little app: the talking cow

For this section we use a small Node app that prints a cow saying something. It uses one package from npm, called `cowsay`.

Make a folder and go into it:

```bash
mkdir cow-says
cd cow-says
```

Make `package.json`. It's the list of packages the app needs:

```json
{
  "name": "cow-says",
  "dependencies": {
    "cowsay": "1.6.0"
  }
}
```

Make `app.js`:

```js
const cowsay = require("cowsay");

const words = process.argv[2] || "Hello from inside a container!";
console.log(cowsay.say({ text: words }));
```

`process.argv[2]` is "the first word you type after the command". If you don't type any, the cow says hello.

Make the `Dockerfile`:

```dockerfile
FROM node:24-slim
WORKDIR /app
COPY package.json .
RUN npm install
COPY app.js .
ENTRYPOINT ["node", "app.js"]
```

You know most of these lines. Two things are new:

- `COPY package.json .` comes **before** `RUN npm install`, and `COPY app.js .` comes **after**. There's a good reason, and it's the next page.
- **`ENTRYPOINT`** is like `CMD`, but anything you type after the image name in `docker run` is handed to it as extra words. That's how we'll make the cow say different things.

## Try it: build and run

```bash
docker build -t layers-cow .
docker run --rm layers-cow
```

```
 ________________________________
< Hello from inside a container! >
 --------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Give it your own words:

```bash
docker run --rm layers-cow "Layers are like pancakes"
```

```
 __________________________
< Layers are like pancakes >
 --------------------------
        \   ^__^
         \  (oo)\_______
...
```

## Try it: see the layers

**`docker history`** lists every step that went into an image, newest at the top:

```bash
docker history layers-cow
```

```
IMAGE          CREATED         CREATED BY                                      SIZE
12c0215f2385   5 seconds ago   ENTRYPOINT ["node" "app.js"]                    0B
<missing>      5 seconds ago   COPY app.js . # buildkit                        12.3kB
<missing>      5 seconds ago   RUN /bin/sh -c npm install # buildkit           9.27MB
<missing>      8 seconds ago   COPY package.json . # buildkit                  12.3kB
<missing>      2 days ago      WORKDIR /app                                    8.19kB
<missing>      2 days ago      CMD ["node"]                                    0B
<missing>      2 days ago      ENTRYPOINT ["docker-entrypoint.sh"]             0B
<missing>      2 days ago      COPY docker-entrypoint.sh /usr/local/bin/ # …   20.5kB
<missing>      2 days ago      RUN /bin/sh -c set -ex   && savedAptMark="$(…   7.33MB
<missing>      2 days ago      ENV YARN_VERSION=1.22.22                        0B
<missing>      2 days ago      RUN /bin/sh -c ARCH= OPENSSL_ARCH= && dpkgAr…   157MB
<missing>      2 days ago      ENV NODE_VERSION=24.22.1                        0B
<missing>      2 days ago      RUN /bin/sh -c groupadd --gid 1000 node   &&…   69.6kB
<missing>      2 days ago      # debian.sh --arch 'amd64' out/ 'bookworm' '…   85.3MB
```

(Your IDs, times and some sizes will be different. There's also a COMMENT column on the right; you can ignore it.)

How to read it:

- **The top five lines are yours**: your Dockerfile, upside down. `COPY app.js` added 12.3kB, `RUN npm install` added 9.27MB of `node_modules`.
- **Everything below came with `FROM node:24-slim`.** Someone else built those steps: Debian Linux files at the very bottom (85.3MB), then Node.js itself (157MB), and so on. You downloaded them; you didn't build them.
- **Lines with `0B` are settings, not layers.** `ENTRYPOINT`, `CMD` and `ENV` don't add or change any files; they only change how a container starts. Only steps that change files make a real layer.
- `<missing>` only means "this step doesn't have its own image name". Nothing is broken.

So how many real layers are there? Ask Docker:

```bash
docker image inspect layers-cow --format '{{len .RootFS.Layers}}'
```

```
9
```

Nine sheets: five from `node:24-slim`, and four of yours (`WORKDIR`, `COPY package.json`, `RUN npm install`, `COPY app.js`).

[Diagram: the layers of layers-cow](./layer-stack.excalidraw)

## Layers never change

Once a layer is built, it's **read-only**: nothing ever changes it. When you change `app.js` and build again, Docker doesn't edit the old layer. It makes a **new** layer and puts it on top in a new image.

That one fact explains the next three pages: why rebuilds can be fast, why images can share space, and where a running container puts its changes.

## Check yourself

1. In your own words, what is a layer?
2. Which line of your Dockerfile made the biggest layer? How big was it?
3. `ENTRYPOINT` shows `0B` in `docker history`. Why?

## Next

Keep the `cow-says` folder and the `layers-cow` image; the next pages use them.

Then: why a second build is much faster than the first, and why the order of the lines matters: [the build cache](02-build-cache.md).
