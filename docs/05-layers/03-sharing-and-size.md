# Sharing layers, and keeping images small

After this page you'll know why ten images built on the same base don't take ten times the space, how to compare base image sizes, and how `.dockerignore` keeps junk out of your images.

## A shared bookshelf

Three friends each want to read the same encyclopedia. They don't buy three copies; they keep one copy on a shared shelf, and each has their own notebook for their own notes.

Docker does this with layers. Layers never change (page 1), so it's safe for many images to point at the **same** layer. Docker keeps it on disk once.

## Try it: how big is an image?

```bash
docker images layers-cow
```

```
IMAGE               ID             DISK USAGE   CONTENT SIZE   EXTRA
layers-cow:latest   12c0215f2385        341MB         82.8MB
```

- **DISK USAGE**: how much space it takes once unpacked on your laptop.
- **CONTENT SIZE**: how much you'd download: the layers are squeezed (compressed) for the trip.

(Depending on your Docker version, you may see one column called just `SIZE` instead. It means the same as disk usage.)

341MB, for a cow that prints some text. Where does it all go? Into the base image, `node:24-slim`. Your own layers are only about 9MB.

## Try it: compare base images

The same Node.js comes in different "flavours". Download two more:

```bash
docker pull node:24
docker pull node:24-alpine
docker images node
```

```
IMAGE            ID             DISK USAGE   CONTENT SIZE
node:24          6449e19d8184       1.65GB          426MB
node:24-alpine   06d7adf3e0ef        244MB         62.8MB
node:24-slim     8cabefbd4448        333MB         83.7MB
```

(`node:24` is big, so this download takes a while. Your numbers may differ a little.)

- **`node:24`**: Debian Linux plus lots of tools for building things: compilers, git, and more. Big.
- **`node:24-slim`**: Debian with only what Node needs. Much smaller. This is what we've been using.
- **`node:24-alpine`**: built on **Alpine Linux**, a very small Linux. Smallest, but some packages behave a little differently on it.

Every image you build carries its base along. Pick the smallest base that works.

## Try it: images share layers

You now have a few images built `FROM node:24-slim`: `layers-cow` and `layers-cow-slow` from the last page. Ask Docker how they use the disk:

```bash
docker system df -v
```

It prints a lot. Near the top, under "Images space usage", find your images (a few columns are left out here):

```
REPOSITORY        TAG       SIZE      SHARED SIZE   UNIQUE SIZE   CONTAINERS
layers-cow-slow   latest    341MB     330.4MB       11MB          0
layers-cow        latest    341MB     330.4MB       11MB          0
node              24-slim   333MB     330.4MB       2.61MB        0
```

- **SIZE**: the whole stack of sheets, 341MB.
- **SHARED SIZE**: the part it shares with other images: 330MB of `node:24-slim` layers.
- **UNIQUE SIZE**: the part that's only its own: 11MB.

So two "341MB" images really cost about 330 + 11 + 11 = 352MB together, not 682MB. The `node:24-slim` layers sit on the shelf once.

[Diagram: three images, one shared base](./shared-layers.excalidraw)

This is also why pulling a second image from the same family is fast: Docker skips the layers it already has.

## Try it: keep junk out with .dockerignore

`Dockerfile.slow` uses `COPY . .`: "copy **everything** in this folder". Everything really means everything. Let's see what that costs.

In your `cow-says` folder, install the packages on your laptop too (this makes a `node_modules` folder), and make a pretend 50MB holiday video:

```bash
npm install
head -c 50000000 /dev/urandom > holiday-video.mp4
```

(`/dev/urandom` gives random bytes; `head -c 50000000` takes 50 million of them. It's a fake video, only to have a big file.)

Build with `Dockerfile.slow`, and look at the top layer:

```bash
docker build -f Dockerfile.slow -t layers-cow-junk .
docker history layers-cow-junk
```

```
IMAGE          CREATED         CREATED BY                                      SIZE
5514f87d6211   2 seconds ago   ENTRYPOINT ["node" "app.js"]                    0B
<missing>      2 seconds ago   RUN /bin/sh -c npm install # buildkit           2.76MB
<missing>      4 seconds ago   COPY . . # buildkit                             52.8MB
...
```

The `COPY . .` layer is **52.8MB**: your video and your laptop's `node_modules` went into the image. Nobody needs a holiday video inside a cow app.

A **`.dockerignore`** file lists what `docker build` should leave out, one pattern per line. Make one in `cow-says`:

```
node_modules
*.mp4
```

(`*.mp4` means "any file ending in .mp4".) Build again:

```bash
docker build -f Dockerfile.slow -t layers-cow-clean .
docker history layers-cow-clean
```

```
IMAGE          CREATED          CREATED BY                                      SIZE
eeea08fd0d28   11 seconds ago   ENTRYPOINT ["node" "app.js"]                    0B
<missing>      11 seconds ago   RUN /bin/sh -c npm install # buildkit           6.55MB
<missing>      12 seconds ago   COPY . . # buildkit                             49.2kB
...
```

49.2kB instead of 52.8MB. Compare the whole images:

```bash
docker images layers-cow-junk
docker images layers-cow-clean
```

```
layers-cow-junk:latest    5514f87d6211   437MB   132MB
layers-cow-clean:latest   eeea08fd0d28   338MB   82.2MB
```

(Headers left out.) Always keep a `.dockerignore` next to a Dockerfile that uses `COPY . .`.

Your good `Dockerfile` copies `package.json` and `app.js` by name, so it never picks up the video. That's one more reason to copy files by name when you can.

## Check yourself

1. Two images both say 341MB. Why can they take less than 682MB together?
2. What's the difference between `node:24`, `node:24-slim` and `node:24-alpine`?
3. What does `.dockerignore` do? When do you need it most?

## Next

Clean up the fake video and the extra images:

```bash
rm holiday-video.mp4
docker rmi layers-cow-junk layers-cow-clean
```

Then: images are read-only, so where does a running container put its changes? [The container's own layer](04-the-container-layer.md).
