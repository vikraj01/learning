# Every computer has an address

After this page you'll know what an IP address is, how to find your laptop's, and what `localhost` really means.

## Buildings and addresses

Imagine a city full of buildings. To send a letter, you need the building's **address**. Without one, the postman has nowhere to go.

Computers are the same. Your laptop, your phone, Google's computers: each is a building, and each has an address so others can find it.

We'll keep using this picture for the whole section:

| In the city | On a network |
| --- | --- |
| A building | A computer (laptop, phone, server) |
| The building's address | Its **IP address** |
| Flats inside the building | **Ports** (next page) |

## The idea

An **IP address** (Internet Protocol address) is four numbers with dots between them, each from 0 to 255:

```
192.168.1.23
8.8.8.8
104.20.23.154
```

Every device on a network has one. When your laptop talks to another computer, it's sending small messages to that computer's IP address.

There's one special address every computer has: **`127.0.0.1`**. It always means "**this computer, myself**". Its name is **`localhost`**. When you opened `http://localhost:3000` in earlier sections, you were sending a letter to your own building.

[Diagram: every computer has an address](./addresses.excalidraw)

## Try it: find your own address

On **Linux**:

```bash
hostname -I
```

On a **Mac**:

```bash
ipconfig getifaddr en0
```

You'll see something like:

```
192.168.1.23
```

Yours will be different. On Linux you may see a few addresses; the first one is usually your Wi-Fi. Write yours down: you'll use it on page 3.

## Try it: knock on doors

**`ping`** sends a tiny "are you there?" to an address and waits for the answer. Start with yourself:

```bash
ping -c 2 127.0.0.1
```

```
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.039 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.044 ms

--- 127.0.0.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss
```

(`-c 2` means "knock twice". On a Mac the lines look slightly different, but say the same thing.)

Look at the **time**: about 0.04 milliseconds. That's a note to yourself: it never leaves the building.

Now try the name instead of the number:

```bash
ping -c 2 localhost
```

```
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.075 ms
```

Same address: `localhost` is just the name for `127.0.0.1`.

Now knock on a building far away. `8.8.8.8` is one of Google's computers:

```bash
ping -c 2 8.8.8.8
```

```
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=41.6 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=117 time=38.2 ms
```

About **40 milliseconds**, a thousand times slower than knocking on your own door. That's a letter across the city: it leaves your laptop, goes through your Wi-Fi, out to the internet, to Google's building, and back. (Your times will differ. Still very fast!)

## Try it: your phone's address

On your phone, open the Wi-Fi settings, tap your Wi-Fi network, and look for **IP address**. It'll look a lot like your laptop's, for example `192.168.1.40`: same first three numbers, different last one. They're neighbours on the same Wi-Fi. (Page 6 explains why.)

## Check yourself

1. What's an IP address, in your own words?
2. What does `127.0.0.1` mean? What's its name?
3. Why did `ping 127.0.0.1` answer so much faster than `ping 8.8.8.8`?

## Next

One address per building. But a building has many flats, and a computer runs many programs. How does a letter reach the right one? [Ports](02-ports.md).
