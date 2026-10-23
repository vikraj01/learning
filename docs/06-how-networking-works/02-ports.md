# One address, many doors: ports

After this page you'll know what a port is, run two little web servers side by side, and see what happens when two programs want the same port.

## Flats in a building

A letter addressed only to "Building 23" is a problem: who inside should get it? So addresses have a **flat number** too: "Building 23, **flat 9001**".

Your laptop is a building with **65,535** flats. Each program that wants visitors moves into a flat and waits there. The flat number is called a **port**.

You've used ports all along without the name: `localhost:3000` means "my own building, flat 3000".

## The idea

- A **port** is a number from 1 to 65,535 that says which program on a computer should get the message.
- A program **listens** on a port: it moves into that flat and waits for knocks.
- **Only one program per port.** Two programs can't live in the same flat.
- An address with a port is written with a colon: `192.168.1.23:9001`, `localhost:9001`.

Some flats have well-known tenants, so everyone knows where to knock:

| Port | Who usually lives there |
| --- | --- |
| 80 | Websites (http) |
| 443 | Secure websites (https) |
| 22 | SSH (logging in to another computer) |
| 3000 | Our Node apps (we picked it) |
| 6379 | Redis |
| 5432 | PostgreSQL (a database) |

[Diagram: one address, many doors](./ports.excalidraw)

## Try it: two flats, two servers

Python comes with a tiny web server. Make two folders, each with a small page:

```bash
mkdir flat-1 flat-2
echo "<h1>Hello from flat 1</h1>" > flat-1/index.html
echo "<h1>Hello from flat 2</h1>" > flat-2/index.html
```

Start a server in `flat-1`, listening on port **9001**:

```bash
cd flat-1
python3 -m http.server 9001
```

```
Serving HTTP on 0.0.0.0 port 9001 (http://0.0.0.0:9001/) ...
```

(On a Mac it may say `::` instead of `0.0.0.0`. Same meaning; page 3 explains it.)

The terminal stays busy: the server is waiting in its flat. Open a **second terminal**, go to the same place, and start another server in `flat-2` on port **9002**:

```bash
cd flat-2
python3 -m http.server 9002
```

Now open a **third terminal** and knock on both doors:

```bash
curl localhost:9001
curl localhost:9002
```

```
<h1>Hello from flat 1</h1>
<h1>Hello from flat 2</h1>
```

Same building (`localhost`), two different flats, two different answers. Open both in your browser too: http://localhost:9001 and http://localhost:9002.

Look back at the first terminal. The server wrote a line for each visit:

```
127.0.0.1 - - [24/Oct/2026 00:07:48] "GET / HTTP/1.1" 200 -
```

`127.0.0.1` is who knocked: you, from your own building.

## Try it: two programs, one flat

In the third terminal, go into `flat-2` and try to start a **second** server on port 9001, which is already taken:

```bash
cd flat-2
python3 -m http.server 9001
```

```
OSError: [Errno 98] Address already in use
```

(On a Mac it's `[Errno 48]`.) Flat 9001 is taken, so Python can't move in. You'll see this error a lot in real life: it always means "something is already listening on that port".

## Try it: who lives in flat 9001?

`lsof` (list open files) can tell you which program is listening on a port:

```bash
lsof -nP -iTCP:9001 -sTCP:LISTEN
```

```
COMMAND    PID         USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python3 207351 tanvi        3u  IPv4 868898      0t0  TCP *:9001 (LISTEN)
```

`python3` is the tenant. When you get "Address already in use", this is how you find out who's in the way.

## Try it: an empty flat

Knock on a flat where nobody lives:

```bash
curl localhost:9005
```

```
curl: (7) Failed to connect to localhost port 9005 after 0 ms: Couldn't connect to server
```

The building is there, but nobody is listening in flat 9005. This is the **connection refused** you met in section 4 (`ECONNREFUSED`).

## Check yourself

1. What's a port? Use the building picture.
2. What does "Address already in use" mean? How would you find out who's using the port?
3. `curl localhost:9005` failed. Is that because the building doesn't exist, or because nobody's in that flat?

## Next

Stop both servers with `Ctrl+C` in their terminals. Keep the folders.

Then: can your **phone** knock on your laptop's flats? It depends on which door the program opened: [who can come in?](03-who-can-come-in.md)
