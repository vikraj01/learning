# Bind mounts: sharing your folder with a container

After this page you'll be able to serve your own web page from nginx, and change it without restarting anything.

Docker has **two** ways to give a container files from outside itself:

1. **Bind mount**: share a folder from your laptop. *This page.*
2. **Volume**: a storage box that Docker looks after for you. *Next page.*

## Your own page

Make a folder called `my-site` and, inside it, a file called `index.html` with this in it:

```html
<h1>Hello, I'm Tanvi!</h1>
<p>This page is running inside a container.</p>
```

nginx shows whatever is in one folder *inside the container*: `/usr/share/nginx/html`. Right now that folder has the "Welcome to nginx!" page in it.

How do we get your file in there?

## Share a folder

A **bind mount** shares a folder from your laptop with the container. "Mount" means "attach a folder so it shows up somewhere". Both your laptop and the container see the same files. Change a file on your laptop, and the container sees the change straight away.

[Diagram: my-site folder shared with nginx](./bind-mount.excalidraw)

Go into your `my-site` folder in the terminal, then run:

```bash
docker run -d --name my-web -p 8080:80 -v "$(pwd)":/usr/share/nginx/html nginx
```

**`-v laptop-folder:container-folder`** means "share this folder of mine as that folder in the container". Laptop first, container second, same as `-p`.

**`$(pwd)`** means "the folder I'm in right now". (On Windows PowerShell, write `${PWD}` instead.)

Open `http://localhost:8080`. You should see:

> **Hello, I'm Tanvi!**
>
> This page is running inside a container.

## Change it live

Edit `index.html` on your laptop: change the text, save it, and refresh the browser. The change shows up immediately. No restart, because it's the same file.

## Try it

1. Add a second file, `about.html`, with a line about yourself. Open `http://localhost:8080/about.html`.
2. Remove the container (`docker rm -f my-web`). Is your `index.html` still on your laptop?
3. Run the same command again. Is your page back?

## Check yourself

1. In `-v "$(pwd)":/usr/share/nginx/html`, which side is your laptop?
2. Why did your edit show up without restarting the container?
3. When the container is removed, what happens to the files in your folder?

## Next

What happens to a container's files when it's removed, and what's the second kind of storage? [Volumes: keeping data safe](06-volumes.md).
