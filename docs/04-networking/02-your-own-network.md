# Your own network: call containers by name

After this page you'll be able to make your own network, put containers on it, and reach them by name. You'll also see that containers on different networks can't see each other.

## The idea

When **you** create a network, Docker gives it a reception desk: a small **DNS**.

**DNS** (Domain Name System) is a phone book for computers: you give it a name, it gives you back the number. The internet uses DNS to turn `google.com` into a number. Docker runs a tiny one inside every network you make, and it knows the name of every container on that network.

[Diagram: your own network, with its phone book](./own-network.excalidraw)

## Try it: make a network

```bash
docker network create lab
```

```
57687662f452e5913fd858208b34ed65bb142b683e310ee2858d2c34d47be990
```

That long number is the network's ID. Check it's there:

```bash
docker network ls
```

You'll see `lab` in the list, next to `bridge`, `host` and `none`.

## Try it: two containers on it

The new flag is **`--network lab`**: "join the `lab` network, not the default one".

```bash
docker run -d --name box1 --network lab busybox:1.37 sleep 3600
docker run -d --name box2 --network lab busybox:1.37 sleep 3600
```

Now knock on `box1` by **name**:

```bash
docker exec box2 ping -c 2 box1
```

```
PING box1 (172.23.0.2): 56 data bytes
64 bytes from 172.23.0.2: seq=0 ttl=64 time=0.146 ms
64 bytes from 172.23.0.2: seq=1 ttl=64 time=0.106 ms

--- box1 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
```

It works. Look at the first line: `ping` turned `box1` into `172.23.0.2` before knocking. That's the phone book at work.

## Try it: ask the phone book yourself

`nslookup` asks DNS "what's the number for this name?":

```bash
docker exec box2 nslookup box1
```

```
Server:		127.0.0.11
Address:	127.0.0.11:53

Name:	box1
Address: 172.23.0.2
```

- `Server: 127.0.0.11` is Docker's phone book. Every container on your network asks it.
- `Address: 172.23.0.2` is the answer: `box1`'s number.

(You may see "Non-authoritative answer:" too. It means "I'm passing on an answer", and you can ignore it.)

## A second name: alias

A container can have extra names on a network, called **aliases**. Start a third box with the alias `helper`:

```bash
docker run -d --name box3 --network lab --network-alias helper busybox:1.37 sleep 3600
docker exec box1 ping -c 1 helper
```

```
PING helper (172.23.0.4): 56 data bytes
64 bytes from 172.23.0.4: seq=0 ttl=64 time=0.109 ms
```

Aliases are useful when an app expects a fixed name, like `database`, and you want to choose which container answers to it.

## Try it: an outsider

Start a container **without** `--network`, so it joins the default network:

```bash
docker run -d --name outsider busybox:1.37 sleep 3600
docker exec outsider ping -c 1 box1
```

```
ping: bad address 'box1'
```

`outsider` is in a different building. It isn't in `lab`'s phone book and can't reach anything inside `lab`. That's on purpose: networks keep groups of containers apart.

You can move it in, though, while it's running:

```bash
docker network connect lab outsider
docker exec outsider ping -c 1 box1
```

```
PING box1 (172.23.0.2): 56 data bytes
64 bytes from 172.23.0.2: seq=0 ttl=64 time=0.074 ms
```

Now it can. (`docker network disconnect lab outsider` would take it out again.)

## Try it: who's on the network?

```bash
docker network inspect lab
```

It prints a lot. Look for the `"Containers"` part:

```
"Containers": {
    "28b2f05f7aea...": {
        "Name": "box1",
        "IPv4Address": "172.23.0.2/16",
        ...
    },
    "6bfaf6d68e3b...": {
        "Name": "box2",
        "IPv4Address": "172.23.0.3/16",
        ...
```

Every container on `lab`, with its number. (Ignore the `/16` for now.)

## The commands so far

| Command | What it does |
| --- | --- |
| `docker network ls` | List the networks |
| `docker network create lab` | Make a network called `lab` |
| `docker run --network lab ...` | Start a container on `lab` |
| `--network-alias helper` | Give it an extra name on that network |
| `docker network connect lab outsider` | Add a running container to `lab` |
| `docker network disconnect lab outsider` | Take it out again |
| `docker network inspect lab` | See who's on `lab` |
| `docker network rm lab` | Delete the network (empty it first) |

## Check yourself

1. What does DNS do? Where is Docker's DNS?
2. Why could `box2` reach `box1` by name here, but not on the previous page?
3. `outsider` couldn't reach `box1`. What are two ways to fix that?

## Next

Clean up. A network can only be removed once nobody's on it, so remove the containers first:

```bash
docker rm -f box1 box2 box3 outsider
docker network rm lab
```

Then: a real app and a real database talking over a network: [the visit counter](03-the-visit-counter.md).
