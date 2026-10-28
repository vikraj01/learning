`main.go` is a tiny program in **Go** (another programming language; you don't need to read it). It prints a cow.

To turn Go code into a program you need the Go tools, so the `Dockerfile` starts from `golang:1.25`, an image with all of them. It works, but look at the size the lab built it at:

```
docker images big-cow
```

Over **1 GB**, to ship a program of about **2 MB**. The image still carries the whole workshop: Linux, the Go compiler, its tools.

## Build big, ship small

A **multi-stage build** has more than one `FROM`. Each `FROM` starts a new **stage**, a fresh image. Only the **last** stage becomes your image; the others are thrown away after the build.

```dockerfile
# Stage 1: the workshop. Build the program here.
FROM golang:1.25 AS build
...

# Stage 2: the box we ship. Start from nothing, take only the program.
FROM scratch
COPY --from=build /src/cow /cow
ENTRYPOINT ["/cow"]
```

- **`AS build`** gives the first stage a name.
- **`FROM scratch`** starts from a completely empty image: no Linux files at all. Fine for a Go program, which needs nothing else.
- **`COPY --from=build`** copies a file from the `build` stage instead of from your folder.

## Your job

1. Turn the `Dockerfile` into a two-stage build.
2. Build it as `small-cow`, and check the cow still talks.
3. Get it under **20 MB**.

## Commands that help

```
docker build -t small-cow .
docker run --rm small-cow
docker images big-cow small-cow
```
