# What happens when you open a website

After this page you'll be able to explain, step by step, what happens between pressing Enter and seeing a page, and watch it happen with `curl`.

## A letter and a reply

Opening a website is like writing to a shop for their catalogue:

1. You look up the shop's address in a directory.
2. You walk to the building and find the right flat.
3. You hand over a letter: "Please send me your catalogue."
4. They hand back a reply: "Here you go", and the catalogue.

The internet does exactly this, in about a tenth of a second.

## The idea

When you type `http://example.com` and press Enter:

1. **DNS**: your laptop asks "where is example.com?" and gets `104.20.23.154` (page 4).
2. **Connect**: it knocks on that address, on port **80**, the website flat (page 2). For `https://`, it's port **443**.
3. **Request**: it sends a short message, the **request**: `GET /`, meaning "give me the main page".
4. **Response**: the server sends back the **response**: a **status code** (like `200 OK`) and then the page itself.
5. Your browser draws the page.

The language the request and response are written in is **HTTP** (HyperText Transfer Protocol). **HTTPS** is the same, sealed in an envelope nobody else can open on the way.

[Diagram: what happens when you open a website](./open-a-website.excalidraw)

## Try it: watch it happen

`curl -v` (verbose) shows every step. `-s -o /dev/null` hides the page itself, so you only see the conversation:

```bash
curl -sv -o /dev/null http://example.com
```

```
* Host example.com:80 was resolved.
* IPv4: 172.66.147.243, 104.20.23.154
*   Trying 172.66.147.243:80...
* Connected to example.com (172.66.147.243) port 80
> GET / HTTP/1.1
> Host: example.com
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: text/html; charset=utf-8
< Server: cloudflare
...
```

Read it by the first character:

- **`*`** lines are curl telling you what it's doing: **resolved** the name (step 1), **Trying**, then **Connected** on port 80 (step 2).
- **`>`** lines are **your request** going out (step 3). `GET /` asks for the main page; `Host: example.com` says which website you mean.
- **`<`** lines are **the response** coming back (step 4). `200 OK` means "here it is". The lines after it, called **headers**, describe the page: what kind of file it is, which server sent it.

Now the secure version on port 443. `-I` asks only for the headers:

```bash
curl -sI https://example.com
```

```
HTTP/2 200
content-type: text/html; charset=utf-8
server: cloudflare
...
```

Same `200`. (HTTP/2 is a newer, faster way of writing the same letters.)

## Try it: be the website yourself

Start your own server in `flat-1` again, and you can watch **both** sides of the conversation:

```bash
python3 -m http.server 9001
```

In another terminal, ask for a page that exists, and one that doesn't:

```bash
curl -s -o /dev/null -w "%{http_code}\n" localhost:9001/
curl -s -o /dev/null -w "%{http_code}\n" localhost:9001/nope
```

```
200
404
```

(`-w "%{http_code}\n"` prints only the status code.) Now look at the server's terminal. It saw both requests:

```
127.0.0.1 - - [24/Oct/2026 00:08:31] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [24/Oct/2026 00:08:31] code 404, message File not found
127.0.0.1 - - [24/Oct/2026 00:08:31] "GET /nope HTTP/1.1" 404 -
```

Who knocked (`127.0.0.1`), what they asked for (`GET /nope`), and what the server answered (`404`). Every website in the world keeps a log like this.

## Status codes you'll meet

The first digit tells you the kind of answer:

| Code | Means | Like |
| --- | --- | --- |
| **200** OK | Here it is | The catalogue arrives |
| **301** Moved | It's at a new address now | "We've moved, go to the new shop" |
| **404** Not Found | No such page | "We don't sell that" |
| **500** Server Error | The server broke while answering | The shop's printer caught fire |

2xx = good, 3xx = go elsewhere, 4xx = you asked for something wrong, 5xx = the server has a problem.

## Postcards, not parcels

A page can be big: pictures, videos. It doesn't travel in one piece. It's cut into many small **packets**, like a long letter sent on a stack of numbered postcards. They can even take different roads across the internet. Your laptop collects them and puts them back in order before the browser shows anything.

## Try it: in your browser

Browsers can show this too. In Chrome or Firefox, open any website, right-click, choose **Inspect**, go to the **Network** tab, and reload the page. Every line is one request, with its status code. A normal website makes dozens of them: one for the page, more for each picture, style and script.

## Check yourself

1. Put these in order: request, DNS, response, connect.
2. In `curl -v` output, what do the `>` lines show? And the `<` lines?
3. What's the difference between a 404 and a 500?

## Next

Stop the server with `Ctrl+C`.

One question is left: your laptop's address is `192.168.1.23`, but so is someone else's laptop, in another house. How does the reply find its way back to **you**? [Your home network](06-your-home-network.md).
