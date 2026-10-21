# Keep the messages in your folder: bind mount

After this page the app in the container will save messages straight into a folder on your laptop, and they'll survive the container being removed.

## The idea

A **bind mount** connects a folder on your laptop to a folder inside the container. It's the same folder seen from two sides: whatever the app writes into it lands on your laptop.

Our app writes into `/app/data` inside the container (the `WORKDIR` is `/app`, and the app uses `data/`). So we connect your laptop's `data` folder there.

[Diagram: where the messages can live](./where-messages-live.excalidraw)

## Try it

From inside your `message-box` folder (you already have a `data` folder there from page 1; if not, make one with `mkdir data`):

```bash
docker run -d --name msg -p 3000:3000 -v "$(pwd)/data:/app/data" message-box
```

The new part is **`-v "$(pwd)/data:/app/data"`**:

- Left of the `:` is the folder on **your laptop**. `$(pwd)` means "the folder I'm in now", so this is your `message-box/data`.
- Right of the `:` is the folder **inside the container**.

Open `http://localhost:3000/web` and send `hello from the container`. Now look on your laptop, not in the container:

```bash
cat data/messages.txt
```

```
hello
my second message
hello from the container
```

The first lines are the ones you sent on page 1, before Docker. The container can see them too, because it's the same folder.

## Remove the container

```bash
docker rm -f msg
cat data/messages.txt
```

```
hello
my second message
hello from the container
```

The container is gone, and the messages are still there, because they never lived in the container.

## Check yourself

1. In `-v "$(pwd)/data:/app/data"`, which side is your laptop and which side is the container?
2. Why did the container show your old messages from page 1?
3. Open `data/messages.txt` in VS Code and add a line by hand. Then run the container again and check with `docker exec msg cat data/messages.txt`. Can the container see your line?

## Next

Clean up:

```bash
docker rm -f msg
```

Then: let Docker look after the storage for you, with a [volume](05-volume.md).
