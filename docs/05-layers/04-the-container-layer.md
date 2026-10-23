# The container's own layer

After this page you'll know where a container's changes go, how to list them with `docker diff`, and why removing a container throws them away.

## Tracing paper on a printed map

You have a printed map you're not allowed to draw on. So you lay a sheet of tracing paper over it, and draw on that: a new route, a cross over a road that's closed.

Looking down, you see the map with your changes. Lift the tracing paper off, and the map is exactly as it was. Someone else can lay their own tracing paper on the same map.

## The idea

Back in section 1 you saw that a file a container writes isn't in the image. Now you can see *where* it goes.

When a container starts, Docker lays one extra, empty sheet on top of the image's layers: the container's **writable layer**. The image's layers stay read-only. Every change the container makes goes into its own writable layer:

- **Add** a file: it's written to the writable layer.
- **Change** a file that came from the image: Docker first **copies it up** into the writable layer, then changes the copy. This is called **copy-on-write**. The image's original stays untouched.
- **Delete** a file that came from the image: it can't really be removed from a read-only layer, so the writable layer gets a note saying "hide this file". It's gone from the container's view, but still in the image.

Every container has its own writable layer, so containers from the same image never see each other's changes.

[Diagram: each container's writable layer on a shared image](./container-layer.excalidraw)

## Try it: make some changes

Start a container from `layers-cow`, but go inside it with `bash` instead of running the cow. `--entrypoint bash` swaps the image's ENTRYPOINT for `bash`, just this once:

```bash
docker run -it --name layers-a --entrypoint bash layers-cow
```

Inside, add a file, change one, and delete one:

```bash
echo "remember to feed the cow" > note.txt
echo "// a change" >> app.js
rm package.json
ls
```

```
app.js	node_modules  note.txt	package-lock.json
```

Leave with `exit`. The container stops, but it isn't removed yet, so its writable layer is still there.

## Try it: docker diff

**`docker diff`** lists what's in a container's writable layer, compared with its image:

```bash
docker diff layers-a
```

```
C /app
C /app/app.js
A /app/note.txt
D /app/package.json
C /root
A /root/.bash_history
```

- **A** = added: `note.txt`.
- **C** = changed: `app.js` (copied up, then changed), and the folders that hold changed files.
- **D** = deleted: `package.json`, hidden from this container.
- `/root/.bash_history` is `bash` keeping a list of the commands you typed. Even that is a change.

How big is the writable layer?

```bash
docker ps -as --filter name=layers-a
```

```
CONTAINER ID   IMAGE        COMMAND   CREATED         STATUS                      PORTS     NAMES      SIZE
ed0b8b7a12db   layers-cow   "bash"    7 seconds ago   Exited (0) 5 seconds ago              layers-a   24.6kB (virtual 259MB)
```

- `-a`: show stopped containers too. `-s`: show sizes.
- **24.6kB** is the writable layer: only your changes.
- **virtual 259MB** is the image underneath, which it shares with every other container from `layers-cow`.

## Try it: the image didn't change

Start a **second** container from the same image and look in `/app`:

```bash
docker run --rm --entrypoint ls layers-cow /app
```

```
app.js
node_modules
package-lock.json
package.json
```

`package.json` is back, and there's no `note.txt`. The new container got its own fresh, empty writable layer on top of the same untouched image. (Its `app.js` doesn't have your `// a change` line either.)

## Remove it, and the changes go

```bash
docker rm layers-a
```

The writable layer is deleted with the container: the note, the changed `app.js`, all of it. This is the "containers forget" lesson from section 2, now with the reason: the changes only ever lived on that container's sheet of tracing paper.

That's why anything worth keeping goes in a **volume** or a **bind mount**: they live outside the layers altogether.

## Check yourself

1. Where do a container's changes go? Where do they *not* go?
2. What does copy-on-write mean, in your own words?
3. In `docker diff`, what do A, C and D mean?
4. A container deletes a 100MB file that came from its image. Does the image get smaller? Why not?

## Next

Then: build a program with one big image, and ship it in a tiny one: [multi-stage builds](05-multi-stage-builds.md).
