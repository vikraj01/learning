# Share the messages with a bind mount

After this page the producer and the consumer will share a folder on your laptop, and you'll be able to add messages too, by hand.

## The idea

A **bind mount** connects a folder on your laptop to a folder inside a container. Like a volume, you can connect the **same** folder to more than one container.

The difference: this time the shared board is a folder **you** can see and open. So there are three people at the board: the producer, the consumer, and you.

[Diagram: two containers, one folder](./share-bind-mount.excalidraw)

## Try it

From your `two-apps` folder, make the folder you'll share:

```bash
mkdir shared
```

Run both apps, both connected to it:

```bash
docker run -d --name producer -p 3000:3000 -v "$(pwd)/shared:/app/data" producer
docker run -d --name consumer -p 4000:4000 -v "$(pwd)/shared:/app/data" consumer
```

Same as the volume page, but the left side of `-v` is a **folder path**, not a name. And again, it's the same in both lines.

Open http://localhost:3000/web and send `hello through my folder`. Refresh http://localhost:4000/read:

> - hello through my folder

Now look on your laptop, not in a container:

```bash
cat shared/messages.txt
```

```
hello through my folder
```

The file the producer wrote is right there, in your folder.

## Try it: be a producer yourself

Open `shared/messages.txt` in VS Code. Add a line at the end:

```
I wrote this one by hand
```

Save the file, and refresh http://localhost:4000/read:

> - hello through my folder
> - I wrote this one by hand

The consumer doesn't know or care who wrote the line. It reads the file, and the file is yours.

## Volume or bind mount?

Both join the two apps. Pick by what you need:

| | Volume | Bind mount |
| --- | --- | --- |
| Left side of `-v` | A name: `shared` | A folder path: `"$(pwd)/shared"` |
| Can you see and edit the files? | Not easily | Yes, it's your folder |
| Good for | Apps sharing data that must stay safe | Watching and poking at the data while you learn or build |

## Check yourself

1. In the two `docker run` lines, how does Docker know this is a bind mount and not a volume?
2. You added a line by hand and the consumer showed it. Why did that work?
3. If you remove both containers, is `shared/messages.txt` still on your laptop?

## Next

Clean up:

```bash
docker rm -f producer consumer
```

Your `shared` folder stays. Delete it when you're done (`rm -r shared`).

That's two apps sharing data, two ways. Tell Vikash what felt easy and what felt confusing.
