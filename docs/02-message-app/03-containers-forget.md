# Containers forget

After this page you'll know where the container keeps your messages, and why they can disappear.

## Where did the message go?

When the app runs in a container, it writes `data/messages.txt` **inside the container**, not on your laptop. The container has its own little set of files, separate from yours.

You can look inside with **`docker exec`**, which runs one command inside a running container:

```bash
docker exec msg cat data/messages.txt
```

```
hello
```

There it is, inside the box.

## Stop is fine

Stop the container and start it again:

```bash
docker stop msg
docker start msg
docker exec msg cat data/messages.txt
```

```
hello
```

Still there. Stopping is like closing a laptop lid: everything is waiting when you open it.

## Remove is not

Now remove the container, and run a fresh one from the same image:

```bash
docker rm -f msg
docker run -d --name msg -p 3000:3000 message-box
docker exec msg cat data/messages.txt
```

```
cat: data/messages.txt: No such file or directory
```

Your messages are gone.

The new container started from the image, and the image only has what the Dockerfile put in it: Node, Express and `app.js`. Your messages were never in the image. They lived in the old container, and went away with it.

This is what people mean when they say containers are **ephemeral** (say "eh-FEM-er-ul"): short-lived. You should expect a container to be thrown away and replaced. People remove containers all the time: to update the app, to fix a problem, to start fresh.

So anything you want to keep has to live **outside** the container. Docker gives you two ways, and they're the next two pages.

[Diagram: where the messages can live](./where-messages-live.excalidraw)

## Check yourself

1. What does `docker exec msg cat data/messages.txt` do?
2. After `docker stop` and `docker start`, are the messages still there? After `docker rm`?
3. Why doesn't a new container have the old messages, even though it's the same image?

## Next

Clean up before the next page:

```bash
docker rm -f msg
```

Then: keep the messages in a folder on your laptop, with a [bind mount](04-bind-mount.md).
