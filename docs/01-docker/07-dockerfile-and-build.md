# Your own image: Dockerfile and build

After this page you'll be able to make your own image with your page inside it, and run it anywhere.

## Why make your own image?

With a bind mount, your page lives on *your* laptop. If you send someone the nginx image, they get "Welcome to nginx!", not your page.

If your page is **baked into an image**, anyone who runs that image sees your page. No folder sharing needed.

## The Dockerfile: a recipe

A **Dockerfile** is a small text file with steps for making an image. Docker reads it top to bottom.

In your `my-site` folder, next to `index.html`, make a file called exactly `Dockerfile` (capital D, no extension):

```dockerfile
FROM nginx
COPY index.html /usr/share/nginx/html/index.html
```

That's the whole recipe:

1. **`FROM nginx`**: start from the nginx image.
2. **`COPY ...`**: copy my `index.html` into the folder nginx serves.

## Build: cook the recipe into an image

```bash
docker build -t my-site .
```

- **`docker build`** reads the Dockerfile and makes an image.
- **`-t my-site`** names (tags) the image `my-site`.
- **`.`** means "use this folder". Docker looks here for the Dockerfile and the files to copy. Don't forget the dot.

You'll see the steps go by, ending with something like:

```
#6 [2/2] COPY index.html /usr/share/nginx/html/index.html
#6 DONE 0.0s
...
#7 naming to docker.io/library/my-site:latest done
```

Check it's there:

```bash
docker images my-site
```

You'll see `my-site:latest` in the list.

## Run: start a container from your image

```bash
docker run -d --name my-web -p 8080:80 my-site
```

Same as before, but the image is now `my-site`, and there's no `-v`. Open `http://localhost:8080`: there's your page, coming from inside the image.

[Diagram: Dockerfile → build → image → run → container](./build-and-run.excalidraw)

## Build vs run

- **Build** happens once: Dockerfile + files → image.
- **Run** happens as often as you like: image → container.

## Try it

1. Change `index.html` and refresh the browser. Does it change? (It shouldn't. Why not?)
2. Make it change: `docker rm -f my-web`, then `docker build -t my-site .` again, then run again.
3. Clean up: `docker rm -f my-web`.

## Check yourself

1. What does the `.` at the end of `docker build` mean?
2. Why didn't editing `index.html` change the running page this time, when it did with a bind mount?
3. Which comes first, build or run?

## Next

[What each line of a Dockerfile means](08-dockerfile-instructions.md).
