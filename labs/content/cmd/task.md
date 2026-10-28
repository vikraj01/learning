The greet folder has **two** programs:

- `app.js`: the web page (listens on 3000, keeps running).
- `say.js`: prints `Hello, <NAME>!` once and stops.

The `Dockerfile` ends with `CMD ["node", "app.js"]`. **`CMD`** is the image's **default command**: what a container runs when you don't say otherwise. The lab built this folder as `greet-cmd`.

## Your job

1. From `greet-cmd`, run a container called `say-ravi` that runs **`say.js`** with `NAME=Ravi`, without changing the Dockerfile.
2. Change the Dockerfile so `say.js` is the default, and build it as `sayer`.
3. From `sayer`, run a container `sayer-web` that serves the **web page** on **http://localhost:3404**.

## How it works

```
docker run  [options]  <image>  [command]
```

If you write a command after the image name, it **replaces** the image's `CMD`. If you don't, the `CMD` runs.

## Commands that help

```
docker run --name say-ravi -e NAME=Ravi greet-cmd node say.js
docker logs say-ravi
docker build -t sayer .
docker run --rm sayer
docker image inspect -f '{{.Config.Cmd}}' sayer
```

> A container lives as long as its command runs. `say.js` finishes in a blink, so its container stops right away. That's not a crash: it's done.
