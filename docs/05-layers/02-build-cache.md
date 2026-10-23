# The build cache: why order matters

After this page you'll be able to tell which steps Docker reuses on a rebuild, and order a Dockerfile so rebuilds stay fast.

## Baking a layered cake

You're baking a three-layer cake: sponge at the bottom, cream in the middle, strawberries on top.

- Want different strawberries? Take the old ones off and put new ones on. The sponge and cream are fine as they are.
- Want a different sponge? Everything on top of it has to come off and be made again.

Docker builds images exactly like that.

## The idea

When you build, Docker remembers each layer it made. That memory is the **build cache**.

On the next build, Docker goes through the Dockerfile from the top. For each step it asks: "Is this step the same as last time, with the same files, and was everything before it the same too?"

- **Yes**: reuse the old layer. The build output says **`CACHED`**, and it takes no time.
- **No**: run the step again. And from that point on, **every step after it runs again too**, because they sit on top of something new.

## Try it: build again, change nothing

From your `cow-says` folder:

```bash
docker build -t layers-cow .
```

```
[+] Building 0.1s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                    0.0s
 ...
 => [1/5] FROM docker.io/library/node:24-slim@sha256:8cabefbd4448...    0.0s
 => CACHED [2/5] WORKDIR /app                                           0.0s
 => CACHED [3/5] COPY package.json .                                    0.0s
 => CACHED [4/5] RUN npm install                                        0.0s
 => CACHED [5/5] COPY app.js .                                          0.0s
 ...
```

Every step says `CACHED`. The whole build took **0.1 seconds**. Nothing ran.

## Try it: change app.js

Open `app.js` and change the default words:

```js
const words = process.argv[2] || "Moo! I was rebuilt.";
```

Build again:

```bash
docker build -t layers-cow .
```

```
[+] Building 0.2s (10/10) FINISHED
 => [1/5] FROM docker.io/library/node:24-slim@sha256:8cabefbd4448...    0.0s
 => CACHED [2/5] WORKDIR /app                                           0.0s
 => CACHED [3/5] COPY package.json .                                    0.0s
 => CACHED [4/5] RUN npm install                                        0.0s
 => [5/5] COPY app.js .                                                 0.0s
```

Only step 5 ran, because only `app.js` changed. `npm install` was reused: Docker could see `package.json` was the same as last time.

## Try it: change package.json

Now add a second package to `package.json`:

```json
{
  "name": "cow-says",
  "dependencies": {
    "cowsay": "1.6.0",
    "chalk": "4.1.2"
  }
}
```

```bash
docker build -t layers-cow .
```

```
[+] Building 3.9s (10/10) FINISHED
 => [1/5] FROM docker.io/library/node:24-slim@sha256:8cabefbd4448...    0.0s
 => CACHED [2/5] WORKDIR /app                                           0.0s
 => [3/5] COPY package.json .                                           0.0s
 => [4/5] RUN npm install                                               3.0s
 => [5/5] COPY app.js .                                                 0.0s
```

`package.json` changed, so step 3 ran. And everything after it ran too: `npm install` (3 seconds) and `COPY app.js`, even though `app.js` didn't change this time. That's the "everything after it" rule.

That's correct behaviour: new packages really do need a new `npm install`.

Put `package.json` back the way it was (only `cowsay`) before going on.

## Try it: the wrong order

Here's a shorter Dockerfile that looks fine. Save it as `Dockerfile.slow`:

```dockerfile
FROM node:24-slim
WORKDIR /app
COPY . .
RUN npm install
ENTRYPOINT ["node", "app.js"]
```

`COPY . .` copies the whole folder at once, `app.js` included, **before** `npm install`.

`-f` tells `docker build` which Dockerfile to use. Build it once so the cache is warm:

```bash
docker build -f Dockerfile.slow -t layers-cow-slow .
```

Now change **one word** in `app.js`, and build again:

```bash
docker build -f Dockerfile.slow -t layers-cow-slow .
```

```
[+] Building 2.7s (9/9) FINISHED
 => [1/4] FROM docker.io/library/node:24-slim@sha256:8cabefbd4448...    0.0s
 => CACHED [2/4] WORKDIR /app                                           0.0s
 => [3/4] COPY . .                                                      0.0s
 => [4/4] RUN npm install                                               2.0s
```

`npm install` ran again, for a one-word change. `app.js` is part of `COPY . .`, so that step changed, and everything after it had to run again.

Here it's 2 seconds. In a real app with hundreds of packages, it's minutes, every time you change a line of code.

[Diagram: what gets rebuilt, good order vs bad order](./build-cache.excalidraw)

## The rule

**Put what changes least at the top, and what changes most at the bottom.**

For a Node app (and Python, and most others) that means:

1. The base image (`FROM`)
2. The package list (`COPY package.json .`)
3. Installing packages (`RUN npm install`)
4. Your code (`COPY app.js .`), last, because you change it all the time

## Check yourself

1. What does `CACHED` mean in the build output?
2. You change `package.json`. Which steps run again in the good Dockerfile? Why does `COPY app.js` run too?
3. Why is `COPY . .` before `RUN npm install` slow while you're working on your code?

## Next

Then: images can be big. Why they don't fill your disk as fast as you'd think, and how to keep them small: [sharing and size](03-sharing-and-size.md).
