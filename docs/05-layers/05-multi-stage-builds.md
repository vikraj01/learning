# Multi-stage builds: build big, ship small

After this page you'll be able to read a Dockerfile with two `FROM` lines, and know why it can make an image hundreds of times smaller.

## The workshop and the gift box

A carpenter builds a wooden toy in a workshop full of saws, drills and sawdust. When it's finished, they put **only the toy** in a gift box. Nobody ships the workshop.

Many programs are the same. To **build** them you need big tools. To **run** them you need only the finished result.

## A program that needs building

Some languages **compile** a program: turn the code you write into one finished file the computer can run directly. Go is one of them.

You don't need to know Go. Here's a tiny Go program that prints a cow. Make a folder `tiny-cow` and save this as `main.go`:

```go
package main

import "fmt"

func main() {
	fmt.Println(` ___________________
< I am a tiny cow! >
 -------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||`)
}
```

To compile it you need the Go tools. There's an official image with them: `golang`.

## Try it: one stage

Save this as `Dockerfile.one-stage`:

```dockerfile
FROM golang:1.25
WORKDIR /src
COPY main.go .
RUN CGO_ENABLED=0 go build -o cow main.go
ENTRYPOINT ["/src/cow"]
```

- `go build -o cow main.go`: compile `main.go` into one finished file called `cow`.
- `CGO_ENABLED=0`: "make that file fully self-contained, needing nothing else". It matters in the next step.

```bash
docker build -f Dockerfile.one-stage -t layers-tiny-cow:one-stage .
docker run --rm layers-tiny-cow:one-stage
```

```
 ___________________
< I am a tiny cow! >
 -------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

It works. But this image is the whole workshop: Linux, the Go compiler and all its tools, plus our 2MB program.

## Try it: two stages

Save this as `Dockerfile`:

```dockerfile
# Stage 1: a big image with the Go tools, only to build the program
FROM golang:1.25 AS build
WORKDIR /src
COPY main.go .
RUN CGO_ENABLED=0 go build -o cow main.go

# Stage 2: start from nothing, and copy in only the finished program
FROM scratch
COPY --from=build /src/cow /cow
ENTRYPOINT ["/cow"]
```

The new parts:

- **Two `FROM` lines** mean two **stages**. Each `FROM` starts a fresh stack of layers.
- **`AS build`** gives the first stage a name, so we can talk about it later.
- **`FROM scratch`** starts from a completely empty image: no Linux files, no shell, nothing. Our `cow` file needs nothing else (that's what `CGO_ENABLED=0` was for).
- **`COPY --from=build /src/cow /cow`** copies one file **out of the first stage** into this one. This is the gift box.

Only the **last** stage becomes the image. The first stage, with all its tools, is used during the build and then left behind.

```bash
docker build -t layers-tiny-cow:multi-stage .
docker run --rm layers-tiny-cow:multi-stage
```

Same cow. Now compare:

```bash
docker images layers-tiny-cow
```

```
IMAGE                         ID             DISK USAGE   CONTENT SIZE
layers-tiny-cow:multi-stage   7f173e581a0d       3.62MB         1.36MB
layers-tiny-cow:one-stage     a070f143be2b       1.29GB          314MB
```

**1.29GB** down to **3.62MB**, for the same cow. About 350 times smaller.

And the layers:

```bash
docker history layers-tiny-cow:multi-stage
```

```
IMAGE          CREATED        CREATED BY                      SIZE
7f173e581a0d   1 second ago   ENTRYPOINT ["/cow"]             0B
<missing>      1 second ago   COPY /src/cow /cow # buildkit   2.26MB
```

One layer: the program. None of the workshop.

## Why small is good

- **Faster** to download and start, on every laptop and server that runs it.
- **Less disk** used.
- **Safer**: the fewer programs inside an image, the fewer things can have security problems. A `scratch` image doesn't even have a shell to break into.

Node and Python apps can use stages too (install packages in one stage, copy only what's needed into a slim one), but the saving is biggest for compiled programs like this one.

## Check yourself

1. What does each `FROM` line start?
2. Which stage becomes the final image? What happens to the other one?
3. What does `COPY --from=build` do?
4. Why can the final stage be `FROM scratch` here, but not for our Node cow?

## Next

Clean up the images from this section:

```bash
docker rmi layers-tiny-cow:one-stage layers-tiny-cow:multi-stage layers-cow layers-cow-slow
```

`golang:1.25` and `node:24` are big too. If you don't need them, `docker rmi golang:1.25 node:24` frees a lot of space.

That's layers: what they are, the build cache, sharing, the container's own layer, and stages. Tell Vikash what felt easy and what felt confusing.
