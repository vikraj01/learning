# How containers find each other

After this page you'll know what an IP address is, how to find a container's address, and why container names don't work on Docker's default network.

## A building full of rooms

Think of an office building:

- Every room has a **number**, like room 2 or room 3.
- Every room has a **name on the door**, like "Accounts".
- To find "Accounts", you ask reception. Reception has a list: "Accounts is room 2."

If the building has **no reception**, you can still walk to room 2. But if you only know the name "Accounts", you're stuck.

Docker containers live in a building like this.

## A few words first

- **Network**: a group of containers that can reach each other. Like the building.
- **IP address**: a container's number on the network, like `172.17.0.2`. Like a room number. Every container gets its own.
- **ping**: a tiny tool that knocks on another address and says whether anyone answered. Good for testing "can I reach it?".
- **busybox**: a very small image with lots of little tools inside, including `ping`. Handy for experiments.

## Try it: see the networks

Docker comes with some networks already made:

```bash
docker network ls
```

```
NETWORK ID     NAME      DRIVER    SCOPE
5a4d30187a8b   bridge    bridge    local
485b92386c70   host      host      local
b5f80e4cbb50   none      null      local
```

(Your IDs will be different.) **`bridge`** is the **default network**: every container you've run so far joined it without you asking. You can ignore `host` and `none` for now.

## Try it: two containers, two addresses

Start two busybox containers, `box1` and `box2`:

```bash
docker run -d --name box1 busybox:1.37 sleep 3600
docker run -d --name box2 busybox:1.37 sleep 3600
```

`sleep 3600` means "wait for an hour". It keeps the container running, so we have time to play with it.

Ask each one for its IP address:

```bash
docker exec box1 hostname -i
docker exec box2 hostname -i
```

```
172.17.0.2
172.17.0.3
```

Two rooms, two numbers. Yours may be different; use your own numbers below.

## Try it: knock by number, then by name

From `box2`, ping `box1` by its **number**:

```bash
docker exec box2 ping -c 2 172.17.0.2
```

```
PING 172.17.0.2 (172.17.0.2): 56 data bytes
64 bytes from 172.17.0.2: seq=0 ttl=64 time=0.096 ms
64 bytes from 172.17.0.2: seq=1 ttl=64 time=0.114 ms

--- 172.17.0.2 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
```

`-c 2` means "knock twice". **2 received**: `box1` answered. The containers *are* connected.

Now try its **name**:

```bash
docker exec box2 ping -c 1 box1
```

```
ping: bad address 'box1'
```

`box2` has no idea who `box1` is. On the default network there's no reception desk: numbers work, names don't.

[Diagram: the default network](./default-network.excalidraw)

## Why not just use numbers?

Because numbers change. When a container is removed and started again, it can get a different number. Apps that save `172.17.0.2` somewhere would break.

Names don't change: you pick them with `--name`. So we want names to work. That's the next page.

## Check yourself

1. What's an IP address, in your own words?
2. On the default network, can `box2` reach `box1`? By number, by name, or both?
3. Why is it a bad idea for an app to use another container's IP address?

## Next

Clean up:

```bash
docker rm -f box1 box2
```

Then: make a network with a reception desk, so names work: [your own network](02-your-own-network.md).
