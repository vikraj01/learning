# Two apps: a producer and a consumer

After this page you'll have two apps in two containers: one that writes messages, and one that shows them. You'll also see why they can't talk to each other yet.

## A notice board

Think of the notice board in a hostel. One person pins up a note. Other people walk past and read it. The writer and the readers never meet; the **board** is what joins them.

If the writer pins notes on a board in their own room, nobody else ever sees them.

## Two new words

- **Producer**: an app that **makes** data. Here, it saves messages to a file.
- **Consumer**: an app that **uses** data someone else made. Here, it reads the file and shows the messages.

Real systems are full of these pairs: one app takes orders, another packs them; one app saves photos, another makes small previews of them.

## The producer

The producer is your message box from section 2, with a new heading. Make a folder called `two-apps`, and inside it a folder called `producer`:

```bash
mkdir -p two-apps/producer
cd two-apps
```

(`-p` makes both folders in one go.)

Copy `app.js` and `Dockerfile` from your `message-box` folder into `producer/`. Then change one line in `producer/app.js`, the heading:

```html
<h1>Producer: write a message</h1>
```

Nothing else changes. It still shows a form at `/web`, and still saves each message to `data/messages.txt`, on door 3000.

## The consumer

Make a second folder:

```bash
mkdir consumer
```

Make `consumer/app.js` and type this in:

```js
const express = require("express");
const fs = require("fs");

const app = express();

app.get("/read", (req, res) => {
  let text = "";
  if (fs.existsSync("data/messages.txt")) {
    text = fs.readFileSync("data/messages.txt", "utf8");
  }
  const lines = text.split("\n").filter((line) => line !== "");

  if (lines.length === 0) {
    res.send("<h1>Consumer: messages</h1><p>No messages yet.</p>");
    return;
  }

  const items = lines.map((line) => `<li>${line}</li>`).join("");
  res.send(`<h1>Consumer: messages</h1><ul>${items}</ul>`);
});

app.listen(4000, () => {
  console.log("Consumer is running on http://localhost:4000/read");
});
```

Read it in three pieces:

1. **Read the file**: if `data/messages.txt` exists, read all of it into `text`. If it doesn't exist yet, `text` stays empty.
2. **Split it into lines**: one message per line, and skip any empty lines.
3. **Answer the browser**: no messages? Say "No messages yet." Otherwise put each message in an `<li>` (a **list item**) inside a `<ul>` (an HTML **list** with bullet points).

It waits on door **4000**, so it doesn't clash with the producer on 3000.

The consumer only has a GET route. It never writes anything; it only reads.

Its Dockerfile is the same five lines as the producer's. Copy `producer/Dockerfile` into `consumer/`.

You should now have:

```
two-apps/
  producer/
    app.js
    Dockerfile
  consumer/
    app.js
    Dockerfile
```

## Try it: build both images

```bash
cd producer
docker build -t producer .
cd ../consumer
docker build -t consumer .
cd ..
```

Near the end of each build you'll see a line like:

```
naming to docker.io/library/consumer:latest done
```

## Try it: run both, side by side

```bash
docker run -d --name producer -p 3000:3000 producer
docker run -d --name consumer -p 4000:4000 consumer
```

The container and the image have the same name here. The last word is the **image**; `--name` is the **container**.

Open http://localhost:3000/web and send `hello`. Then open http://localhost:4000/read:

> **Consumer: messages**
>
> No messages yet.

The producer saved it. Check with `docker exec`:

```bash
docker exec producer cat data/messages.txt
docker exec consumer cat data/messages.txt
```

```
hello
cat: data/messages.txt: No such file or directory
```

Each container has its own private files. The producer pinned its note on a board in its own room, and the consumer can't see in.

To join them, both containers need the **same** `/app/data` folder: one shared board. Docker gives you two ways to do that, and they're the next two pages.

## Check yourself

1. In your own words, what's a producer and what's a consumer?
2. Why does the consumer say "No messages yet", even though the producer saved `hello`?
3. Why does the consumer use door 4000 and not 3000?

## Next

Clean up:

```bash
docker rm -f producer consumer
```

Then: give both apps one shared board, with a [volume](02-share-with-a-volume.md).
