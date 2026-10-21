# Volumes: keeping data safe

After this page you'll know why containers lose their data, and how a **volume** keeps it safe and lets containers share it.

## Containers forget

A container's own files live in its scratch space (remember page 3?). That space belongs to the container, and it goes away with it.

Try it:

```bash
docker run --name box1 alpine sh -c "echo 'my notes' > /notes.txt && cat /notes.txt"
```

```
my notes
```

The file is there. Now remove the container, and look for the file from a new one:

```bash
docker rm box1
docker run --rm alpine cat /notes.txt
```

```
cat: can't open '/notes.txt': No such file or directory
```

Gone.

- **Stopping** a container (`docker stop`) keeps its files, like closing a laptop lid.
- **Removing** it (`docker rm`) throws its files away, like throwing the laptop out.

Containers get removed all the time: to update to a new image, to fix a problem, to start fresh. Now imagine the container was a database holding everyone's accounts. We need somewhere safer.

## Volumes: a storage box Docker looks after

A **volume** is a storage box that Docker creates and keeps for you, **outside** any container. You attach it to a container, and the container uses it like a normal folder. When the container is removed, the volume stays.

Make one:

```bash
docker volume create my-notes
```

Attach it with `-v`, the same flag as a bind mount, but with a **name** on the left instead of a folder:

```bash
docker run --rm -v my-notes:/notes alpine sh -c "echo 'written by container 1' > /notes/today.txt"
```

That container is already gone (`--rm`). Start a brand new one with the same volume:

```bash
docker run --rm -v my-notes:/notes alpine cat /notes/today.txt
```

```
written by container 1
```

The container is gone, and the data survived.

## Sharing: two containers, one volume

A volume can be attached to more than one container at the same time. One can write, another can read.

[Diagram: two containers sharing one volume](./shared-volume.excalidraw)

Make a volume for a website, and start nginx serving from it:

```bash
docker volume create site
docker run -d --name web -p 8080:80 -v site:/usr/share/nginx/html nginx
```

Open `http://localhost:8080`. You'll see "Welcome to nginx!" (when an empty volume is attached, Docker fills it with what the image had in that folder).

Now a **different** container writes a new page into the same volume:

```bash
docker run --rm -v site:/data alpine sh -c "echo '<h1>Written by another container</h1>' > /data/index.html"
```

Refresh the browser:

> **Written by another container**

Notice the folder names: alpine called it `/data`, nginx called it `/usr/share/nginx/html`. Same volume, different doors into it.

## Bind mount or volume?

| | Bind mount (page 5) | Volume |
| --- | --- | --- |
| Where the files live | A folder **you** pick on your laptop | A place **Docker** manages |
| How you write it | `-v "$(pwd)":/path` (a folder path on the left) | `-v my-volume:/path` (a plain name on the left) |
| Good for | Editing your own files while you work | Data that must survive: databases, uploads |

Docker tells them apart by the left side: a path means bind mount, a plain name means volume.

## Commands for volumes

| Command | What it does |
| --- | --- |
| `docker volume create site` | Make a volume. |
| `docker volume ls` | List volumes. |
| `docker volume rm site` | Delete a volume **and its data**. It can't be in use by a container. |

## Try it

1. Remove the `web` container (`docker rm -f web`), then start it again with the same `docker run` command. Is "Written by another container" still there? Why?
2. Run `docker volume ls`. Do you see `my-notes` and `site`?
3. Clean up:
   ```bash
   docker rm -f web
   docker volume rm my-notes site
   ```

## Check yourself

1. What happens to a container's own files when you `docker stop` it? And when you `docker rm` it?
2. In `-v site:/usr/share/nginx/html`, is that a bind mount or a volume? How can you tell?
3. You're running a database in a container. Bind mount, volume, or nothing? Why?

## Next

Typing those long `-v` flags every time is tiring. What if your page could live *inside* an image? [Dockerfile and build](07-dockerfile-and-build.md).
