Every container gets its own **address** (an IP address), like a house number on a street. Its network has a **gateway**: the way out of the street, which is your laptop.

A container called `target` is running a website on Docker's **default network**.

## Your job

Write each answer into its file on the left, and save.

1. `ip.txt`: the IP address of `target`.
2. `gateway.txt`: the gateway of the default network (it's called `bridge`).
3. `page.txt`: the **title** of `target`'s web page. Fetch it **by number**, from another container:

   ```
   docker run --rm busybox wget -qO- http://<target's ip>
   ```

## Commands that help

```
docker inspect target
docker network inspect bridge
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' target
```

> On the default network, numbers work but names don't. That's why `http://<ip>` works here and `http://target` wouldn't.
