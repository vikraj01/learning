The greet app is built as `greet-lab`. Next to it is a `.env` file, the app's settings written down:

```
NAME=Tanvi
COLOR=pink
```

On its own, a `.env` file does nothing. Somebody has to read it. Here, Docker will: `--env-file .env` reads the file and makes every line a real environment variable inside the container, like one `-e` per line.

## Your job

1. Run a container called `from-file` from `greet-lab` on **http://localhost:3401** (the app listens on **3000** inside), with its settings from `.env`.
2. Open the page: Tanvi, pink.
3. Change `COLOR` in `.env` to `lightgreen`. Make the page light green.

## Commands that help

```
docker run -d --name from-file -p 3401:3000 --env-file .env greet-lab
docker exec from-file env
docker restart from-file
docker rm -f from-file
```

> The file is read **once**, when the container is made. The `.env` file itself never goes into the container.
