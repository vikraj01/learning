Typing this every time gets old:

```
docker build -t greet .
docker run -d -p 3500:3000 -e NAME=Tanvi -e COLOR=pink greet
docker run --rm greet node say.js
```

**Docker Compose** lets you write it down once, in a file called **`compose.yaml`**, and start everything with `docker compose up -d`.

## The shape of the file

```yaml
name: hello

services:
  web:
    build: .
    ports:
      - "3500:3000"
    environment:
      NAME: Tanvi
      COLOR: pink
```

- **`services:`**: the parts of your app. Each one becomes a container.
- **`build: .`**: build the image from this folder (the `.` from `docker build .`).
- **`ports:`**: `-p`. **`environment:`**: `-e`.
- **Indentation** (the spaces at the start of a line) shows what belongs to what. Two spaces per level, never tabs.

## Your job

1. Make `compose.yaml` with a service `web` built from this folder, on **http://localhost:3500** (port **3000** inside), greeting **you** on a **pink** page.
2. Add a second service, `say`, from the same folder, that runs `node say.js` instead of the web app.
3. Start it all: `docker compose up -d`.

## Commands that help

```
docker compose config      # what Compose read (or where it got stuck)
docker compose up -d
docker compose ps -a
docker compose logs say
docker compose down
```

> `command:` in Compose is the words after the image name in `docker run`: it replaces the `CMD`.
