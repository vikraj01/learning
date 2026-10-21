# Let Docker keep the messages: volume

After this page you'll keep the messages in a **volume**, and know when to pick a volume instead of a bind mount.

## The idea

A **volume** is a storage box that Docker makes and looks after for you. It lives outside every container, so removing a container doesn't touch it. You don't pick a folder on your laptop; you give the volume a name, and Docker handles where it lives.

[Diagram: where the messages can live](./where-messages-live.excalidraw)

## Try it

Make a volume called `messages`:

```bash
docker volume create messages
```

```
messages
```

Run the app with the volume attached to `/app/data`:

```bash
docker run -d --name msg -p 3000:3000 -v messages:/app/data message-box
```

It's the same `-v` flag as before, but with a **name** on the left instead of a folder path.

Open `http://localhost:3000/web` and send `saved in a volume`.

## Remove it, start a new one

```bash
docker rm -f msg
docker run -d --name msg -p 3000:3000 -v messages:/app/data message-box
docker exec msg cat data/messages.txt
```

```
saved in a volume
```

A brand new container, and the message is still there, because it lives in the volume.

Notice your old messages from page 1 are **not** here. The volume started empty; it isn't your laptop's `data` folder.

## Bind mount or volume?

| | Bind mount | Volume |
| --- | --- | --- |
| Left side of `-v` | A folder path: `"$(pwd)/data"` | A name: `messages` |
| Where the files live | A folder **you** choose | A place **Docker** looks after |
| Can you open the file in VS Code? | Yes, it's your folder | Not easily; use `docker exec` |
| Good for | Seeing and editing files while you work | Data that must stay safe: databases, uploads |

Docker tells them apart by the left side: a path means bind mount, a plain name means volume.

## Check yourself

1. In `-v messages:/app/data`, is that a bind mount or a volume? How can you tell?
2. Why aren't your page 1 messages in the volume?
3. If this app were a real website with lots of users, which one would you use to keep the messages? Why?

## Clean up

```bash
docker rm -f msg
docker volume rm messages
```

`docker volume rm` deletes the volume **and everything in it**, so only do it when you're done.

## Next

That's the whole message box: an app, a Dockerfile, and two ways to keep its data. To revise, every command is explained on one page: [every command, explained](06-all-commands-explained.md). Then tell Vikash what felt easy and what felt confusing.
