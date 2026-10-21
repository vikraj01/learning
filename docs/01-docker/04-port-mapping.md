# Port mapping: letting the browser in

After this page you'll be able to open a container's web page in your browser.

## The locked box

Start nginx again:

```bash
docker run -d --name my-web nginx
```

Now open your browser and go to `http://localhost:8080`. It doesn't work: "This site can't be reached".

nginx *is* running. The problem is that a container is a sealed box. It has its own doors, and none of them are connected to your laptop.

## Ports are doors

A **port** is a numbered door on a computer. Programs listen behind a door, waiting for visitors.

- nginx, inside the container, listens on door **80** (that's the `80/tcp` you saw in `docker ps`).
- Your browser can only knock on doors of *your laptop*.

So we connect a door on your laptop to the door on the container. That's **port mapping**.

[Diagram: browser → laptop door 8080 → container door 80](./port-mapping.excalidraw)

## Open the door

Remove the old container first:

```bash
docker rm -f my-web
```

(`-f` means "force": stop it and remove it in one go.)

Now run it again, with a door connected:

```bash
docker run -d --name my-web -p 8080:80 nginx
```

**`-p 8080:80`** means: "door 8080 on my laptop leads to door 80 in the container". Laptop first, container second.

Open `http://localhost:8080` in your browser. You should see:

> **Welcome to nginx!**

Run `docker ps` again. The PORTS column now shows the connection:

```
0.0.0.0:8080->80/tcp
```

**`localhost`** means "this computer, the one I'm sitting at".

## Try it

1. Stop and remove `my-web`. Start it again with `-p 9000:80`. Which address do you open now?
2. Start **two** nginx containers at once, `web1` on `-p 8081:80` and `web2` on `-p 8082:80`. Do both pages open?
3. Clean up: `docker rm -f web1 web2 my-web`.

## Check yourself

1. In `-p 8080:80`, which number belongs to your laptop and which to the container?
2. Why couldn't the browser see nginx before we added `-p`?
3. Could two containers both use door 8080 on your laptop at the same time? (Try it and see.)

## Next

The page says "Welcome to nginx!". Let's make it show *your* page: [Bind mounts](05-bind-mounts.md).
