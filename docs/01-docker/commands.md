# Docker commands: cheat sheet

Every command from the Docker pages, in one place. Run them top to bottom, or jump to a section.

Ready-made files are in [`files/`](files/):

- [`files/my-site/`](files/my-site/): `index.html` + a two-line nginx `Dockerfile` (page 7)
- [`files/my-site-python/`](files/my-site-python/): `index.html` + the six-line Python `Dockerfile` (page 8)

## 1. Is Docker installed?

```bash
docker --version
```

## 2. Run containers (page 2)

```bash
docker run hello-world                    # download + run, prints a message, stops
docker run -d --name my-web nginx         # run nginx in the background, named my-web
docker ps                                 # what's running
docker ps -a                              # everything, including stopped
docker stop my-web                        # stop it
docker rm my-web                          # remove it
docker rm -f my-web                       # stop + remove in one go
```

## 3. Images (page 3)

```bash
docker pull nginx                         # download (same as nginx:latest)
docker pull nginx:alpine                  # a smaller flavour
docker images                             # list images on your laptop
docker rmi nginx:alpine                   # delete an image
docker run --rm alpine ls /               # look inside an image (--rm = clean up after)
```

## 4. Port mapping (page 4)

```bash
docker run -d --name my-web -p 8080:80 nginx    # laptop 8080 -> container 80
# open http://localhost:8080
docker rm -f my-web
```

## 5. Bind mounts (page 5)

Run from inside `files/my-site/` (or your own `my-site` folder):

```bash
docker run -d --name my-web -p 8080:80 -v "$(pwd)":/usr/share/nginx/html nginx
# open http://localhost:8080, edit index.html, refresh
docker rm -f my-web
```

Windows PowerShell: use `${PWD}` instead of `$(pwd)`.

## 6. Volumes (page 6)

```bash
docker volume create my-notes
docker run --rm -v my-notes:/notes alpine sh -c "echo 'written by container 1' > /notes/today.txt"
docker run --rm -v my-notes:/notes alpine cat /notes/today.txt    # data survived

docker volume create site
docker run -d --name web -p 8080:80 -v site:/usr/share/nginx/html nginx
docker run --rm -v site:/data alpine sh -c "echo '<h1>Written by another container</h1>' > /data/index.html"
# refresh http://localhost:8080

docker volume ls
docker rm -f web
docker volume rm my-notes site
```

## 7. Build your own image (page 7)

From inside `files/my-site/`:

```bash
docker build -t my-site .                 # don't forget the dot
docker images my-site
docker run -d --name my-web -p 8080:80 my-site
# open http://localhost:8080
docker rm -f my-web
```

## 8. The bigger Dockerfile (page 8)

From inside `files/my-site-python/`:

```bash
docker build -t my-site:v2 .
docker run -d --name my-web2 -p 8000:8000 my-site:v2
# open http://localhost:8000 and http://localhost:8000/built-at.txt
docker rm -f my-web2
```

## Clean up everything from these pages

```bash
docker rm -f my-web my-web2 web box1
docker volume rm my-notes site
docker rmi my-site my-site:v2 nginx nginx:alpine alpine hello-world python:3.12-slim
```

Errors like "No such container" here are fine: it means that one was already gone.
