# Tanvi's study notes

Read the pages in order. Take your time: one page at a time is perfect.

Each page has a **Try it** part. Type the commands yourself rather than copy-pasting; it sticks better.

The `.excalidraw` files are the drawings. Open them in VS Code to see them.

## 1. Docker

1. [What is Docker?](01-docker/01-what-is-docker.md)
2. [Run your first container](01-docker/02-run-a-container.md)
3. [What is an image?](01-docker/03-what-is-an-image.md)
4. [Port mapping: letting the browser in](01-docker/04-port-mapping.md)
5. [Bind mounts: sharing your folder with a container](01-docker/05-bind-mounts.md)
6. [Volumes: keeping data safe](01-docker/06-volumes.md)
7. [Your own image: Dockerfile and build](01-docker/07-dockerfile-and-build.md)
8. [What each line of a Dockerfile means](01-docker/08-dockerfile-instructions.md)

Quick reference: [all Docker commands](01-docker/commands.md), with ready-made files in [`01-docker/files/`](01-docker/files/).

## 2. Project: the message box

Build a small web app in JavaScript, put it in Docker, and learn where its data lives.

1. [A small web app: the message box](02-message-app/01-the-app.md)
2. [Put the app in a container](02-message-app/02-the-dockerfile.md)
3. [Containers forget](02-message-app/03-containers-forget.md)
4. [Keep the messages in your folder: bind mount](02-message-app/04-bind-mount.md)
5. [Let Docker keep the messages: volume](02-message-app/05-volume.md)
6. [Every command, explained](02-message-app/06-all-commands-explained.md)
7. [The same app, in Python](02-message-app/07-same-app-in-python.md)
8. [Every Dockerfile keyword](02-message-app/08-dockerfile-keywords.md)
9. [Go inside a container](02-message-app/09-go-inside-a-container.md)

Finished files, if you get stuck: [`02-message-app/message-box/`](02-message-app/message-box/) (JavaScript) and [`02-message-app/message-box-python/`](02-message-app/message-box-python/) (Python).

## 3. Project: producer and consumer

Two apps: one writes messages, the other shows them. Then make them share the messages, once with a volume and once with a bind mount.

1. [Two apps: a producer and a consumer](03-two-apps/01-producer-and-consumer.md)
2. [Share the messages with a volume](03-two-apps/02-share-with-a-volume.md)
3. [Share the messages with a bind mount](03-two-apps/03-share-with-a-bind-mount.md)

Finished files, if you get stuck: [`03-two-apps/producer/`](03-two-apps/producer/) and [`03-two-apps/consumer/`](03-two-apps/consumer/).

## 4. Networking

How containers find and talk to each other: IP addresses, your own networks, names, and which address to use from where. The example is a visit counter: a web app and a Redis database.

1. [How containers find each other](04-networking/01-the-default-network.md)
2. [Your own network: call containers by name](04-networking/02-your-own-network.md)
3. [The visit counter: an app and a database](04-networking/03-the-visit-counter.md)
4. [Which address do I use?](04-networking/04-which-address.md)

Finished app: [`04-networking/visit-counter/`](04-networking/visit-counter/). To watch everything run step by step: `cd docs/04-networking && ./demo.sh` (press Enter for each step).

## 5. Layers

What an image is really made of, why some builds are fast and others slow, and how to keep images small. The example is `cow-says`, a cow that says what you tell it.

1. [Layers: what an image is made of](05-layers/01-what-is-a-layer.md)
2. [The build cache: why order matters](05-layers/02-build-cache.md)
3. [Sharing layers, and keeping images small](05-layers/03-sharing-and-size.md)
4. [The container's own layer](05-layers/04-the-container-layer.md)
5. [Multi-stage builds: build big, ship small](05-layers/05-multi-stage-builds.md)

Finished files: [`05-layers/cow-says/`](05-layers/cow-says/) and [`05-layers/tiny-cow/`](05-layers/tiny-cow/).

## 6. How networking works

Not just Docker: how any two computers find and talk to each other. Addresses, ports, who's allowed in, names, what happens when you open a website, and your home network. It explains the *why* behind section 4.

1. [Every computer has an address](06-how-networking-works/01-addresses.md)
2. [One address, many doors: ports](06-how-networking-works/02-ports.md)
3. [Who can come in? 127.0.0.1 vs 0.0.0.0](06-how-networking-works/03-who-can-come-in.md)
4. [DNS: the contacts app of the internet](06-how-networking-works/04-dns.md)
5. [What happens when you open a website](06-how-networking-works/05-opening-a-website.md)
6. [Your home network: private and public addresses](06-how-networking-works/06-your-home-network.md)

To watch it all run step by step: `cd docs/06-how-networking-works && ./demo.sh`.

