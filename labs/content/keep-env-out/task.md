This greet folder has a `.env` with the app's settings, **and a password**:

```
NAME=Tanvi
COLOR=pink
DB_PASSWORD=...
```

Look at the `Dockerfile`: `COPY . .` copies **everything** in the folder into the image. Everything includes `.env`. The lab built it for you as an image called `leaky`.

An image gets shared: pushed to Docker Hub, sent to a teammate, put on a server. Whoever has it can read every file in it.

## Your job

1. **Be the thief.** Read the password out of the `leaky` image and write it in `found.txt`.
2. **Close the hole.** Make a `.dockerignore` file that leaves `.env` out.
3. Build `greet-clean` from the same folder. It must have no `.env` inside.
4. Run it as `clean` on **http://localhost:3402**, with the settings handed in from outside.

## `.dockerignore`

A file called `.dockerignore`, next to the Dockerfile. One name per line. Docker leaves those files out of the build completely, as if they weren't in the folder. `COPY . .` can't copy what Docker never sent it.

```
.env
```

## Commands that help

```
docker run --rm leaky cat /app/.env
docker build -t greet-clean .
docker run --rm greet-clean ls -a /app
docker run -d --name clean -p 3402:3000 --env-file .env greet-clean
```

> The rule: settings and secrets go **into the container** when it starts (`--env-file`, `-e`), never **into the image** when it's built.
