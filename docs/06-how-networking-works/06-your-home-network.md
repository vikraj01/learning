# Your home network: private and public addresses

After this page you'll know what your router does, the difference between a private and a public IP address, and how a reply from a website finds its way back to your laptop.

## A gated society

Think of a gated housing society:

- Inside, every building has a **society number**: Building 23, Building 40. These only mean something **inside** the gate. Another society across town also has a Building 23.
- From outside, the world only knows **one** address: the society's gate on the main road.
- At the gate sits the **watchman**. When a letter goes out from Building 23, he notes it in his register and writes the gate's address as the return address. When the reply comes back to the gate, he checks his register and walks it to Building 23.

That's your home network:

| Society | Home network |
| --- | --- |
| Building's society number | **Private IP address** (`192.168.1.23`) |
| The gate's address on the main road | **Public IP address** (`27.7.203.40`) |
| The watchman | The **router** (your Wi-Fi box) |
| The watchman's register | **NAT** (Network Address Translation) |

[Diagram: one public address for the whole house](./home-network.excalidraw)

## The idea

- A **private IP address** works only inside your own network. Your laptop, phone and TV each get one from the router.
- A **public IP address** is the one the internet sees. Your whole home shares one, the router's.
- The **router** connects the two. It has an address on each side: a private one facing your home (often `192.168.1.1`) and the public one facing the internet.
- **NAT** is the watchman's trick: swap the private return address for the public one on the way out, and swap it back on the way in.

Private addresses always start in one of three ways, so you can spot them:

| Starts with | Example |
| --- | --- |
| `192.168.` | `192.168.1.23` (most homes) |
| `10.` | `10.0.0.5` (offices, phone hotspots) |
| `172.16.` to `172.31.` | `172.17.0.2` (Docker's containers in section 4!) |

Everything else, like `8.8.8.8` or `104.20.23.154`, is public.

## Try it: your private address

You found it on page 1:

```bash
hostname -I                 # Linux
ipconfig getifaddr en0      # Mac
```

```
192.168.1.23
```

## Try it: your router's address

On **Linux**:

```bash
ip route | grep default
```

```
default via 192.168.1.1 dev wlp0s20f3 proto dhcp src 192.168.1.23 metric 600
```

On a **Mac**:

```bash
route -n get default | grep gateway
```

```
    gateway: 192.168.1.1
```

The router is called the **default gateway**: the gate every letter goes through when it isn't for a neighbour. Yours may be `192.168.0.1`, `10.0.0.1`, or similar.

## Try it: your public address

Your laptop doesn't know its public address: only the router does. So ask a website what address your letters arrive from:

```bash
curl ifconfig.me
```

```
27.7.203.40
```

Yours will be different. That's your whole home's address on the internet. Every device on your Wi-Fi shares it.

Check it on your phone: open http://ifconfig.me in its browser.

- **On Wi-Fi**, it shows the **same** public address as your laptop: same gate.
- **On mobile data**, it shows a **different** one: your phone left the society and is using the mobile company's gate.

## Why this matters

- **Strangers can't knock on your laptop directly.** Its private address means nothing outside, and the watchman only lets in replies to letters you sent. That's why, on page 3, your phone could reach your laptop at home, but a friend's phone across town couldn't.
- **To put a website on the internet**, it needs a public address, or the router has to be told to pass certain knocks inside (called **port forwarding**). That's what servers in a data centre or the cloud are for.
- **Docker uses the same trick.** Containers get private addresses (`172.17.0.x`), and `-p 8080:80` is port forwarding: "knocks on the laptop's port 8080 go to this container's port 80".

## Check yourself

1. Is `192.168.1.40` private or public? And `8.8.8.8`?
2. What does the router do with a reply from a website? Use the watchman picture.
3. Your laptop and your phone are on the same Wi-Fi. Do they have the same public address? The same private address?

## Next

That's how networking works: addresses, ports, who can come in, names, a request and its response, and the gate out to the internet.

Want to see it all run at once? From this folder:

```bash
./demo.sh
```

Then tell Vikash what felt easy and what felt confusing.
