On the left you have the **message box**: `app.js` (the app) and `package.json` (the list of packages it needs, here only `express`). There's no Dockerfile yet. You'll write it.

## A Dockerfile is a recipe

Each line is one step, run from top to bottom:

| Line | Means |
| --- | --- |
| `FROM node:24-slim` | Start from an image that already has Node.js |
| `WORKDIR /app` | Work in the folder `/app` inside the image |
| `COPY package.json .` | Copy a file from this folder into the image |
| `RUN npm install` | Run a command while building (here: install the packages) |
| `CMD ["node", "app.js"]` | The command to start when a container runs |

## Your job

1. Write a `Dockerfile` for the message box, using lines like the ones above. You need: a starting image, a work folder, the packages, the app, and the start command.
2. Build it as `my-box`.
3. Run it as a container called `my-box`, opening on **http://localhost:8096/web** (the app listens on port **8080** inside).

```
docker build -t my-box .
docker run -d --name my-box -p 8096:8080 my-box
```

> Changed the Dockerfile? Build again, then `docker rm -f my-box` and run it again.
