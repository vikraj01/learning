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
