# Share the messages with a volume

After this page the producer and the consumer will use one volume, so whatever the producer saves, the consumer shows.

## The idea

You already know a **volume**: a storage box Docker makes and looks after, outside every container.

So far you've attached a volume to one container. But you can attach the **same** volume to as many containers as you like. Each of them sees the same files. That's the shared notice board.

[Diagram: two containers, one volume](./share-volume.excalidraw)

## Try it

Run these from your `two-apps` folder. Make a volume called `shared`:

```bash
docker volume create shared
```

```
shared
```

Run both apps, both with `shared` attached at `/app/data`:

```bash
docker run -d --name producer -p 3000:3000 -v shared:/app/data producer
docker run -d --name consumer -p 4000:4000 -v shared:/app/data consumer
```

Look closely: the `-v` part is **the same** in both lines. That's what joins them.

Open http://localhost:4000/read first:

> No messages yet.

The volume is new and empty. Now open http://localhost:3000/web and send `hello from the producer`. Refresh the consumer page:

> **Consumer: messages**
>
> - hello from the producer

Send `a second one` and refresh again:

> - hello from the producer
> - a second one

Two containers, two apps, one set of files.

## Remove both, keep the messages

```bash
docker rm -f producer consumer
docker run -d --name consumer -p 4000:4000 -v shared:/app/data consumer
```

Refresh http://localhost:4000/read:

> - hello from the producer
> - a second one

Both containers were removed, and a brand new consumer still finds the messages. They live in the volume, not in any container.

## Check yourself

1. What in the two `docker run` lines makes the two apps share messages?
2. You remove both containers. Where are the messages now?
3. Could you add a **second** consumer, on door 4001, that shows the same messages? What would you type?

## Next

Clean up:

```bash
docker rm -f consumer
docker volume rm shared
```

Then: share a folder on your laptop instead, with a [bind mount](03-share-with-a-bind-mount.md).
