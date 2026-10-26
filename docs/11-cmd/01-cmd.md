# CMD: what a container runs

After this page you'll know what the `CMD` line in a Dockerfile does, how to run something else in its place, and why some containers stop straight away while others keep running.

## The TV's last channel

When you switch the TV on, it starts on a channel by itself, usually the last one. That's the **default**. You can still pick any other channel with the remote.

`CMD` is a container's default channel: the command it runs when you start it and don't ask for anything else.

## The idea

Look at the last line of the `greet` Dockerfile:

```dockerfile
CMD ["node", "app.js"]
```

**`CMD`** means: "when a container starts from this image, run `node app.js`". It doesn't run during `docker build`. It's only stored in the image, waiting.

You can ask the image what its `CMD` is:

```bash
docker image inspect greet:2.0 --format '{{.Config.Cmd}}'
```

```
[node app.js]
```

Write `CMD` as a list in square brackets, every word in its own quotes: `["node", "app.js"]`, not `node app.js`. That's the form we always use.

## Try it: the default

```bash
docker run --rm -p 3000:3000 --name greet greet:2.0
```

```
Saying hello to friend on port 3000
```

That's `CMD` running: `node app.js`. Stop it with `Ctrl+C`.

## Try it: replace `CMD`

Anything you type **after the image name** replaces `CMD`. Remember `say.js`, the terminal hello from section 9? It's in the image too:

```bash
docker run --rm greet:2.0 node say.js
```

```
Hello, friend!
```

The container ran `node say.js` instead of `node app.js`. Settings still work the same way:

```bash
docker run --rm -e NAME=Tanvi greet:2.0 node say.js
```

```
Hello, Tanvi!
```

Some more, all from the same image:

```bash
docker run --rm greet:2.0 node --version
```

```
v24.22.1
```

```bash
docker run --rm greet:2.0 ls
```

```
app.js
say.js
```

| You type | The container runs |
| --- | --- |
| `docker run greet:2.0` | `node app.js` (the `CMD`) |
| `docker run greet:2.0 node say.js` | `node say.js` |
| `docker run greet:2.0 node --version` | `node --version` |
| `docker run greet:2.0 ls` | `ls` |

The whole `CMD` is thrown away, not added to. In the last row there's no `node` at all.

## A container lives as long as its command

Notice the difference:

- `node app.js` is a server. It waits for the browser forever, so the container keeps running until you stop it.
- `node say.js` prints one line and ends. The moment it ends, the container stops. That's why you got your prompt back straight away.

**A container is only alive while its command is running.** When the command finishes, the container stops. A container that "exits immediately" usually means its command finished (or crashed) right away.

## Go inside: replace `CMD` with a shell

Replacing `CMD` with `bash` gives you a shell inside a fresh container:

```bash
docker run --rm -it greet:2.0 bash
```

```
root@5c1e8f3a2b7d:/app#
```

`-it` keeps it interactive, so you can type. Try `ls`, `env`, `node say.js`. Type `exit` to leave; the container stops because its command (`bash`) ended.

## Good to know

- Only the **last** `CMD` in a Dockerfile counts.
- `docker exec` (section 2) runs a command in a container that's **already running**. Replacing `CMD` starts a **new** container with a different command.

## Check yourself

1. You run `docker run greet:2.0 node say.js`. Does `app.js` run too?
2. Why does a container running `node say.js` stop by itself, but one running `node app.js` doesn't?
3. What does `docker run --rm greet:2.0 echo hi` print?

## Next

[ENTRYPOINT: the part you can't replace by accident](../12-entrypoint/01-entrypoint.md). Typing `node` every time is getting old.

This section uses the files from [`10-tags/greet/`](../10-tags/greet/); nothing new to add.
