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

Finished files, if you get stuck: [`02-message-app/message-box/`](02-message-app/message-box/).
