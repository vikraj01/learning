# Run your first container

After this page you'll be able to run a container, see what's running, and stop it.

## Hello, world

The first container everyone runs is called `hello-world`. Type:

```bash
docker run hello-world
```

The first time, Docker doesn't have the image yet, so it downloads it from Docker Hub. Then it starts a container from it. You'll see:

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
...
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

What happened:

1. **`docker run`** means "make a container from this image and start it".
2. Docker looked for the `hello-world` image on your laptop, didn't find it, and **pulled** (downloaded) it.
3. The container printed its message and then **stopped**, because its job was done.

## A container that keeps running

Some programs finish (like `hello-world`). Others keep running and wait for someone to talk to them. A **server** is one of those: a program that waits for requests and answers them.

**nginx** (say "engine-x") is a web server: it hands out web pages. Run it:

```bash
docker run -d --name my-web nginx
```

- **`-d`** means "detached": run in the background, give me my terminal back.
- **`--name my-web`** gives the container a name, so you can talk about it later.

Docker prints a long id, like `ff91a7ca1079...`. That's the container's id.

## See what's running

```bash
docker ps
```

```
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
ff91a7ca1079   nginx     "/docker-entrypoint.…"   2 seconds ago   Up 2 seconds   80/tcp    my-web
```

There's your container: made from the `nginx` image, **Up** (running), named `my-web`.

Notice `80/tcp` under PORTS. Remember that; it's the next page.

## Stop it and clean up

```bash
docker stop my-web
docker rm my-web
```

- **`docker stop`** stops the container (like closing an app).
- **`docker rm`** removes it (like deleting it). The *image* stays, so running nginx again next time is fast.

## Try it

1. Run `hello-world` again. Is it faster this time? Why?
2. Start nginx with the name `my-web`, check it with `docker ps`, then stop and remove it.
3. Run `docker ps -a`. The `-a` shows **all** containers, even stopped ones. Do you see your old `hello-world` containers?

## Check yourself

1. What's the difference between `hello-world` and `nginx` in how long they run?
2. What does `-d` do?
3. After `docker rm`, is the image gone too?

## Next

You've now got two images on your laptop: `hello-world` and `nginx`. What exactly is an image? [What is an image?](03-what-is-an-image.md)
