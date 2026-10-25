**nginx** (say "engine-x") is a web server: a program that sends web pages to the browser. You don't have to install it. Docker can run it in a container.

## Your job

Start nginx in a container called `hello-web`, and make it open in your browser at **http://localhost:8080**.

## Remember

- `docker run` starts a container from an image.
- `-d` keeps it running in the background, so you get your terminal back.
- `--name` gives it a name you choose.
- `-p laptop:container` opens a door from your laptop into the container.

> When you think it works, open http://localhost:8080 in your browser, then press **Check my work**.
