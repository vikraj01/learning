# Every command, explained

This page goes back over the whole message box project, every command in the order you used it, with every part explained. Use it to look things up or to revise later.

[Diagram: which command moves things where](./commands-journey.excalidraw)

The big picture in one line: you write **files**, `docker build` turns them into an **image**, `docker run` makes a **container** from it, and `docker stop` / `docker rm` pause it or throw it away.

## The two files

| File | What it is |
| --- | --- |
| `app.js` | The app. `GET /web` sends back the form. `POST /send` adds the message to `data/messages.txt`. Listens on door 3000. |
| `Dockerfile` | The recipe for the image, 5 lines. |

The Dockerfile again, one line at a time:

| Line | In plain words |
| --- | --- |
| `FROM node:24-slim` | Start from an image that already has Node. |
| `WORKDIR /app` | Work in a folder called `/app` inside the image. |
| `RUN npm install express` | Download Express into the image. |
| `COPY app.js .` | Copy `app.js` from your laptop into `/app`. |
| `CMD ["node", "app.js"]` | When a container starts, run the app. |

Finished copies of both files are in [`message-box/`](message-box/).

## 1. Run the app on your laptop (page 1)

```bash
node --version
```
Shows which Node you have. If it prints a version, Node is installed.

```bash
mkdir message-box
cd message-box
```
`mkdir` (make directory) makes a new folder. `cd` (change directory) goes into it.

```bash
npm install express
```
- `npm`: Node's tool for downloading packages.
- `install express`: download Express into this folder. It goes into `node_modules/`, and gets written down in `package.json`.

```bash
node app.js
```
Start the app. It keeps running until you press `Ctrl + C`. Open `http://localhost:3000/web`.

```bash
cat data/messages.txt
```
`cat` prints a file. Here: every message you've sent.

## 2. Build and run in Docker (page 2)

```bash
docker build -t message-box .
```
- `docker build`: follow the Dockerfile and make an image.
- `-t message-box`: give the image a name (a **tag**). Without it you'd get a long random ID.
- `.`: the Dockerfile and `app.js` are in **this** folder. Don't forget the dot.

```bash
docker run -d --name msg -p 3000:3000 message-box
```
- `docker run`: make a new container from an image and start it.
- `-d`: **detached**, run in the background and give you the terminal back.
- `--name msg`: call the container `msg`. Other commands use this name.
- `-p 3000:3000`: **port mapping**. Left is the door on your laptop, right is the door in the container.
- `message-box`: which image to use. This always comes last.

```bash
docker logs msg
```
Show what the app printed inside the container. Useful when something doesn't work.

## 3. Look inside, stop and remove (page 3)

```bash
docker exec msg cat data/messages.txt
```
- `docker exec`: run one command inside a container that's already running.
- `msg`: which container.
- `cat data/messages.txt`: the command to run in there.

```bash
docker stop msg
docker start msg
```
Pause the container, and start it again. Its files are kept, so the messages are still there.

```bash
docker rm -f msg
```
- `docker rm`: remove (delete) a container, and its files with it.
- `-f`: **force**, stop it first if it's running. Without `-f` you'd have to `docker stop` first.

## 4. Bind mount (page 4)

```bash
docker run -d --name msg -p 3000:3000 -v "$(pwd)/data:/app/data" message-box
```
Same as before, plus:
- `-v`: connect storage to the container.
- `"$(pwd)/data"`: left side, a folder on your laptop. `pwd` (print working directory) is the folder you're in, so this is `message-box/data`.
- `:/app/data`: right side, the folder inside the container where the app writes.
- The quotes keep it working even if a folder name has a space in it.

On Windows PowerShell, write `${PWD}` instead of `$(pwd)`.

## 5. Volume (page 5)

```bash
docker volume create messages
```
Make a volume called `messages`. Docker decides where it lives.

```bash
docker run -d --name msg -p 3000:3000 -v messages:/app/data message-box
```
The same `-v`, but with a **name** on the left instead of a folder path. A name means volume; a path means bind mount.

```bash
docker volume rm messages
```
Delete the volume **and everything in it**. It can't be attached to a container when you do this, so `docker rm -f msg` first.

## Handy commands to look around

```bash
docker ps              # containers that are running
docker ps -a           # all containers, stopped ones too
docker images          # images on your laptop
docker volume ls       # volumes
```

## Clean up everything from this project

```bash
docker rm -f msg
docker volume rm messages
docker rmi message-box
```

`docker rmi` (remove image) deletes the image. You can always build it again from the Dockerfile.

## Check yourself

1. In `docker run -d --name msg -p 3000:3000 message-box`, what does each part do?
2. What's the difference between `docker stop` and `docker rm`?
3. Which command shows you what's inside a running container's file?
