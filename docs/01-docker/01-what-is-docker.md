# What is Docker?

After this page you'll know what problem Docker solves, and the difference between an **image** and a **container**.

## The problem

Imagine you bake a cake at home and it comes out perfect. You give the recipe to a friend. Their cake fails. Their oven is different, their flour is different, they're missing one ingredient.

Apps have the same problem. An app works on one laptop and breaks on another, because the other laptop has a different version of something, or is missing something. Programmers say: *"but it works on my machine!"*

## What Docker does

Docker puts the app **and everything it needs** into one sealed box. The box runs the same way on any laptop or server that has Docker.

Two words you'll see all the time:

- **Image**: the recipe, frozen. Everything the app needs, packed together, ready to use. It never changes once it's made.
- **Container**: one running copy made from an image. The dish cooked from the recipe.

From one image you can start many containers, like cooking the same recipe many times. (Page 3 looks inside an image properly.)

[Diagram: one image, many containers](./image-and-containers.excalidraw)

## Where images come from

There's a big online library of ready-made images called **Docker Hub**. Someone has already made images for web servers, databases, programming languages and more. You can download and run them with one command. Later, you'll make your own.

## Try it

Check Docker is installed. Open a terminal and type:

```bash
docker --version
```

You should see something like:

```
Docker version 29.6.1, build 8900f1d
```

(Your number may be different. That's fine.)

If you see "command not found", Docker isn't installed yet. Ask Vikash.

## Check yourself

1. In your own words: what's the difference between an image and a container?
2. Can one image make three containers?
3. Why would "it works on my machine" stop being a problem with Docker?

## Next

[Run your first container](02-run-a-container.md).
