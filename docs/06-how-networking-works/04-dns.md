# DNS: the contacts app of the internet

After this page you'll know how a name like `google.com` turns into an IP address, look it up yourself, and see your laptop's own private list of names.

## The contacts app

You don't remember your friends' phone numbers. You tap "Mum" in your contacts, and the phone dials the number for you.

Computers can only connect to **numbers** (IP addresses). But people like **names**. So there's a giant contacts app for the internet, called **DNS**.

## The idea

- **DNS** (Domain Name System) turns a name into an IP address. Asking it is called a **lookup**, and turning a name into a number is called **resolving** the name.
- A **domain name** is a name like `google.com` or `example.com`.
- A **DNS server** is a computer that answers lookups. Your Wi-Fi tells your laptop which one to ask.
- Before asking any DNS server, your laptop checks its own small list first: the **hosts file**. Think of it as your private contacts.

So when you type `example.com` in the browser:

1. Your laptop checks the hosts file. Not there.
2. It asks the DNS server: "what's example.com?"
3. The DNS server answers: `104.20.23.154`.
4. Your laptop connects to `104.20.23.154`.

[Diagram: DNS, step by step](./dns.excalidraw)

## Try it: look up a name

`nslookup` (name server lookup) asks DNS for you:

```bash
nslookup example.com
```

```
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	example.com
Address: 104.20.23.154
Name:	example.com
Address: 172.66.147.243
```

- **Server** is the DNS server your laptop asked. Yours may say something like `192.168.1.1` (your router) instead.
- **Address** is the answer. Big websites often have **several** addresses, like a company with several phone lines. Any of them works.
- You may see more lines with long addresses full of colons, like `2606:4700:10::ac42:93f3`. Those are **IPv6** addresses, the newer, longer kind. Same idea.

## Try it: ping a name

`ping` does a lookup before it knocks. Watch the first line:

```bash
ping -c 2 google.com
```

```
PING google.com (142.250.193.174) 56(84) bytes of data.
64 bytes from 142.250.193.174: icmp_seq=1 ttl=117 time=17.4 ms
64 bytes from 142.250.193.174: icmp_seq=2 ttl=117 time=9.04 ms
```

`google.com` became `142.250.193.174` before a single knock. (Your number may differ: Google has many buildings, and DNS gives you a nearby one.)

## Try it: a name that doesn't exist

```bash
nslookup made-up-tanvi.com
```

```
** server can't find made-up-tanvi.com: NXDOMAIN
```

**NXDOMAIN** means "non-existent domain": no such contact. When a browser says "This site can't be reached ... DNS_PROBE_FINISHED_NXDOMAIN", this is what happened.

## Try it: your private contacts

Look at the hosts file. It's in the same place on Linux and Mac:

```bash
cat /etc/hosts
```

```
127.0.0.1 localhost
::1     ip6-localhost ip6-loopback
...
```

There it is: `localhost` → `127.0.0.1`. That's why `localhost` always means your own laptop: it's in your private contacts, so your laptop never even asks the DNS server.

You could add your own lines here, like `127.0.0.1 tanvi.test`, and that name would work on your laptop only. Changing the file needs admin rights (`sudo`), so just look for now.

## Try it: any name you like, for free

There's one shortcut that needs no setup: every name that **ends in `.localhost`** means your own laptop. Start a server in `flat-1` from page 2:

```bash
python3 -m http.server 9001
```

Then, in another terminal:

```bash
curl http://tanvi.localhost:9001
curl http://anything-you-like.localhost:9001
```

```
<h1>Hello from flat 1</h1>
<h1>Hello from flat 1</h1>
```

Try http://tanvi.localhost:9001 in Chrome or Firefox too. Stop the server with `Ctrl+C` when you're done.

## Check yourself

1. Why do we need DNS at all? Use the contacts app picture.
2. Where does your laptop look **before** asking a DNS server?
3. What does NXDOMAIN mean?

## Next

You now know addresses, ports and names. Put them together, and you can follow everything that happens when you open a website: [opening a website, step by step](05-opening-a-website.md).
