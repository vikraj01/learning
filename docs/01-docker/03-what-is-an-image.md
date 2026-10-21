# What is an image?

After this page you'll know what's inside an image, how images are named, and how to download, list and delete them.

## More than a recipe

On page 1 we said an image is like a recipe. Let's be more exact. An image is a **frozen package** that holds:

1. **A tiny set of Linux files**: the basic folders and tools a program expects to find.
2. **The program itself**: nginx, Python, whatever the image is for.
3. **Settings, and the command to start it**: what should happen when a container starts.

Everything the program needs, nothing from your laptop.

## Look inside one

`alpine` is a very small Linux image. Ask it to list its top folder:

```bash
docker run --rm alpine ls /
```

```
bin
dev
etc
home
lib
...
usr
var
```

Those folders aren't on your laptop. They're inside the image. Every container made from it gets its own copy to look at.

**`--rm`** means "remove the container when it finishes", so you don't have to clean up after.

## Layers

An image is built in **layers**, stacked like sheets of paper: Linux files at the bottom, the program on top, the start command on top of that. When you pull an image, each `Pull complete` line you see is one layer arriving.

[Diagram: what's inside the nginx image](./inside-an-image.excalidraw)

Layers are why images download fast the second time: Docker already has the bottom sheets and only fetches what's new.

## Images never change

An image is **read-only**. A running container gets its own scratch space on top of the image, and anything it changes goes there, not into the image.

See it for yourself. This container writes a file and reads it back:

```bash
docker run --name box1 alpine sh -c "echo hi > /note.txt && cat /note.txt"
```

```
hi
```

Now start a **new** container from the same image and look for that file:

```bash
docker run --rm alpine cat /note.txt
```

```
cat: can't open '/note.txt': No such file or directory
```

The file was in the first container's scratch space. The image stayed exactly as it was. That's why one image can make many containers that all start the same, fresh.

Clean up: `docker rm box1`.

## Names and tags

An image name has two parts: **name:tag**.

- The **name** says what it is: `nginx`, `python`, `alpine`.
- The **tag** says which version or flavour: `nginx:alpine`, `python:3.12-slim`.
- No tag? Docker uses **`latest`**. So `nginx` means `nginx:latest`.

Images come from **Docker Hub** ([hub.docker.com](https://hub.docker.com)), a big online library. Search for `nginx` there and look at the **Tags** tab.

## Commands for images

| Command | What it does |
| --- | --- |
| `docker pull nginx:alpine` | Download an image without running it. |
| `docker images` | List the images on your laptop. |
| `docker rmi nginx:alpine` | Delete an image (it can't be in use by a container). |

## Try it

1. Pull two flavours of nginx:
   ```bash
   docker pull nginx
   docker pull nginx:alpine
   ```
2. Run `docker images` and compare their sizes. You'll see something like this (your columns may look a little different):
   ```
   IMAGE           ID             DISK USAGE   CONTENT SIZE
   nginx:alpine    892bb2152464        103MB         29.7MB
   nginx:latest    bc4cad49969a        243MB         66.8MB
   ```
   Same web server, very different sizes. The `alpine` flavour is built on the tiny alpine Linux.
3. Delete the one you don't need: `docker rmi nginx:alpine`.

## Check yourself

1. Name the three things inside an image.
2. If a container changes a file, does the image change?
3. What does `nginx` mean when you don't write a tag?

## Next

Images and containers are clear. Now let's see nginx's page in the browser: [Port mapping](04-port-mapping.md).
