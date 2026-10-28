An image name has two parts: **name:tag**. The **tag** is usually a version: `node:24-slim`, `postgres:17-alpine`. Leave it out and Docker uses the tag `latest`.

Giving your own images versions means you can always go back: if 2.0 is broken, 1.0 is still there.

## Your job

1. Build the greet app, as it is now, as `greet-tags:1.0`.
2. In `app.js`, change `Hello` to `Welcome` in the `<h1>` line. Build it as `greet-tags:2.0`.
3. Make `greet-tags:latest` point at 2.0.
4. Run the **old** version, 1.0, as a container called `v1` on **http://localhost:3403** (the app listens on **3000** inside).

## Commands that help

```
docker build -t greet-tags:1.0 .
docker tag <existing-image> <new-name:tag>
docker images greet-tags
docker run -d --name v1 -p 3403:3000 greet-tags:1.0
```

> `latest` isn't magic. It doesn't mean "newest"; it's just the tag Docker uses when you don't type one. It points wherever you last put it.
