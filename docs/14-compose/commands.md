# Compose commands

Every `docker compose` command from sections 7 and 14, on one page. Run them from the folder that has `compose.yaml`: Compose looks for the file in the folder you're in.

Wherever a command takes a service name (`web`, `db`...), it's the name under `services:` in `compose.yaml`, not the container name.

## Start and stop

| Command | What it does | Seen in |
| --- | --- | --- |
| `docker compose up -d` | make and start everything in the background (builds images only if they don't exist yet) | 7.3, 14.1 |
| `docker compose up -d --build` | build the images again first, then start. Use it after you change code | 7.3, 14.1 |
| `docker compose up -d web` | start only `web` (and whatever it `depends_on`) | |
| `docker compose stop` | stop the containers, keep them | 7.5 |
| `docker compose start` | start the stopped containers again | 7.5 |
| `docker compose restart api` | stop and start `api` | |
| `docker compose down` | remove the containers and the network. **Volumes are kept** | 7.4, 14.1 |
| `docker compose down -v` | the same, **and delete the volumes** (the data is gone) | 7.4, 14.4 |

## Look at it

| Command | What it does | Seen in |
| --- | --- | --- |
| `docker compose ps` | this project's containers, their state and doors | 7.3 |
| `docker compose logs` | what every container printed | 7.4 |
| `docker compose logs -f api` | keep watching `api`'s output (`Ctrl + C` to stop watching) | 7.4 |
| `docker compose config` | the finished file: every `${...}` filled in, every `env_file` read | 14.2 |
| `docker compose config --services` | just the service names | |
| `docker compose images` | the images this project uses | |

## Go inside, run things

| Command | What it does | Seen in |
| --- | --- | --- |
| `docker compose exec db psql -U todo` | run a command inside the **running** `db` container | 7.4 |
| `docker compose exec api ping -c 1 db` | from inside `api`, check it can find `db` | 14.3 |
| `docker compose exec api sh` | a shell inside `api` (`exit` to leave) | |
| `docker compose run --rm say` | a **new, one-off** container for `say`, removed when it ends | 14.1 |
| `docker compose run --rm say --version` | the same, with the words after the name replacing `command:` | 14.1 |

`exec` = into a container that's already running. `run` = a fresh container just for this.

## Images

| Command | What it does |
| --- | --- |
| `docker compose build` | build the images, start nothing |
| `docker compose pull` | download the newest version of every `image:` |

## Options before the command

These go between `docker compose` and the command:

| Option | What it does | Example |
| --- | --- | --- |
| `-f <file>` | use this file instead of `compose.yaml` | `docker compose -f other.yaml up -d` |
| `-p <name>` | use this project name instead of `name:` | `docker compose -p test up -d` |

## The keys in `compose.yaml`

| Key | Means | Command-line twin | Seen in |
| --- | --- | --- | --- |
| `name:` | project name, in front of every container, network and volume | `-p` | 7.3 |
| `image:` | the image to use (or, with `build:`, the name to give it) | the image in `docker run` / `-t` | 7.3, 14.1 |
| `build:` | build from this folder | `docker build <folder>` | 7.3 |
| `build:` `context:` + `dockerfile:` | the folder, and which Dockerfile | `docker build -f` | 14.1 |
| `command:` | replace the image's `CMD` | words after the image name | 14.1 |
| `entrypoint:` | replace the image's `ENTRYPOINT` | `--entrypoint` | 14.1 |
| `ports:` | doors from your laptop in | `-p` | 7.3 |
| `environment:` | settings for the app | `-e` | 7.3 |
| `env_file:` | settings for the app, from a file | `--env-file` | 14.1 |
| `volumes:` (under a service) | volumes and bind mounts | `-v` | 7.3 |
| `volumes:` (at the bottom) | the named volumes this project needs | `docker volume create` | 7.3 |
| `networks:` (under a service) | which networks it joins | `--network` | 14.3 |
| `networks:` (at the bottom) | the networks this project needs | `docker network create` | 14.3 |
| `depends_on:` | start these first | (you, remembering) | 7.3 |
| `healthcheck:` | how to tell it's ready | `--health-cmd` | 7.3 |
| `restart:` | start it again if it stops | `--restart` | 14.3 |
| `${NAME:-default}` | fill in a value from `.env` or the terminal | | 14.2 |
