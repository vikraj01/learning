# Who can come in? 127.0.0.1 vs 0.0.0.0

After this page you'll be able to make a program reachable only from your laptop, or from other devices too, and open a page on your phone that's served by your laptop.

## The intercom and the front door

A building has two ways to reach a flat:

- The **intercom** inside the building. Only people already inside can use it.
- The **front door** onto the street. Anyone who knows the address can walk up and knock.

When a program starts listening, it chooses which of these it answers:

- **`127.0.0.1`**: the intercom. Only programs on this same laptop can reach it.
- **`0.0.0.0`**: the front door. "Answer on every address this laptop has", so other devices on the network can reach it too.

Choosing the address to listen on is called **binding**.

[Diagram: who can come in?](./who-can-come-in.excalidraw)

## Try it: two servers, two choices

You need your laptop's IP address from page 1 (`hostname -I` on Linux, `ipconfig getifaddr en0` on a Mac). We'll write it as `192.168.1.23`; use yours.

In the `flat-1` folder from the last page, start **server A**, intercom only:

```bash
python3 -m http.server 9003 --bind 127.0.0.1
```

```
Serving HTTP on 127.0.0.1 port 9003 (http://127.0.0.1:9003/) ...
```

In a second terminal, same folder, start **server B**, front door:

```bash
python3 -m http.server 9004 --bind 0.0.0.0
```

```
Serving HTTP on 0.0.0.0 port 9004 (http://0.0.0.0:9004/) ...
```

## Try it: knock from inside

In a third terminal, knock on both with `localhost`:

```bash
curl localhost:9003
curl localhost:9004
```

```
<h1>Hello from flat 1</h1>
<h1>Hello from flat 1</h1>
```

Both answer. You're inside the building, so the intercom and the front door both work.

Now knock using your laptop's **street address** instead of `localhost`, as if you were outside:

```bash
curl 192.168.1.23:9003
curl 192.168.1.23:9004
```

```
curl: (7) Failed to connect to 192.168.1.23 port 9003 after 0 ms: Couldn't connect to server
<h1>Hello from flat 1</h1>
```

Server A only answers its intercom, so the street address gets nothing. Server B answers the front door.

## Try it: knock from your phone

This is the fun part. Your phone must be on the **same Wi-Fi** as your laptop.

On your phone's browser, open:

```
http://192.168.1.23:9004
```

You should see **Hello from flat 1**: a page served by your laptop, on your phone. Look at server B's terminal. There's a new line, and the address at the start is your **phone's** IP:

```
192.168.1.40 - - [24/Oct/2026 00:12:03] "GET / HTTP/1.1" 200 -
```

Now try server A:

```
http://192.168.1.23:9003
```

The phone can't connect. It's outside, and server A only answers the intercom.

If even 9004 doesn't open on your phone:

- **On a Mac**, a box may pop up asking "Do you want the application python3 to accept incoming network connections?" Click **Allow**.
- **Office, college, café and hotel Wi-Fi** often stop devices from talking to each other. Try at home, or on your phone's hotspot with the laptop connected to it.

## Why this matters for Docker

Remember `-p 8080:80` from the Docker section? It opens the **front door**: Docker listens on `0.0.0.0:8080`. You can keep it to the intercom by putting `127.0.0.1` in front:

```bash
docker run -d --name front -p 9010:80 nginx
docker run -d --name intercom -p 127.0.0.1:9011:80 nginx
docker port front
docker port intercom
```

```
80/tcp -> 0.0.0.0:9010
80/tcp -> [::]:9010
80/tcp -> 127.0.0.1:9011
```

Your phone can open `http://192.168.1.23:9010`, but not `:9011`. Clean up with `docker rm -f front intercom`.

Real programs use this all the time. A database that only your own apps should use listens on `127.0.0.1`; a website for everyone listens on `0.0.0.0`.

## Check yourself

1. What's the difference between listening on `127.0.0.1` and on `0.0.0.0`?
2. Your phone can't open a page your laptop is serving. Name two things you'd check.
3. What does `-p 127.0.0.1:9011:80` do differently from `-p 9011:80`?

## Next

Stop both servers with `Ctrl+C`.

So far you've typed numbers like `192.168.1.23`. But you never type numbers to visit Google. How do names become numbers? [DNS](04-dns.md).
