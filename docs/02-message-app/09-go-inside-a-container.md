# Go inside a container

After this page you'll be able to step inside a running container, look around, and you'll know what `-it` means.

## Asking through the door vs walking in

On page 3 you ran `docker exec msg cat data/messages.txt`. That's like asking someone through a closed door: "read me that note". You get one answer, and the door stays shut.

Today you open the door and walk in. You can look at anything, for as long as you like, and leave when you're done.

## Before you start

You need the message box running. If it isn't:

```bash
docker run -d --name msg -p 3000:3000 message-box
```

Open http://localhost:3000/web and send one message, `hello`, so there's something to find.

## Try it: walk in

```bash
docker exec -it msg bash
```

Your prompt changes to something like this:

```
root@9a3bbe6597ff:/app#
```

You're inside the container now. The prompt tells you where you are:

- `root`: the user you are inside the container.
- `9a3bbe6597ff`: the container's ID. Yours will be different.
- `/app`: the folder you're in. That's the `WORKDIR /app` line from the Dockerfile.
- `#`: the container is waiting for you to type.

**`bash`** is a **shell**: the program that reads what you type and runs it. Your laptop's terminal runs a shell too. So you've started a second shell, inside the box.

Look around. Type these one at a time:

```bash
pwd
ls
cat data/messages.txt
whoami
```

```
/app
app.js  data  node_modules  package-lock.json  package.json
hello
root
```

That's the inside of the box: `app.js`, the `node_modules` folder that `npm install` made, and your message.

## Walk out

```bash
exit
```

(Pressing `Ctrl+D` does the same.) Your normal prompt comes back.

Leaving doesn't stop the container. Check:

```bash
docker ps
```

`msg` is still in the list, still `Up`. You only closed the shell you opened. The app kept running the whole time.

## What `-it` means

`-it` is two flags squeezed together: `-i` and `-t`. Writing `-i -t` is the same thing.

- **`-i`** means **interactive**. It keeps a line open from your keyboard into the container, so what you type reaches `bash`.
- **`-t`** means **TTY** (say "tee-tee-why"). It's an old word for a terminal, from "teletypewriter". It gives `bash` a proper screen, so it shows you a prompt and lays out its output neatly.

You need both. Here's what happens if one is missing:

| You type | What happens |
| --- | --- |
| `docker exec msg bash` | `bash` starts, hears nothing, and stops straight away. You're back at your own prompt, nothing printed. |
| `docker exec -t msg bash` | You see the prompt, but your typing doesn't reach it. You're stuck. Press `Ctrl+C` to get out. |
| `docker exec -i msg bash` | Your typing works, but there's no prompt. It works, but it feels like typing blind. |
| `docker exec -it msg bash` | Typing goes in, a proper prompt comes back. This is the one. |

[Diagram: what -i and -t do](./go-inside.excalidraw)

A simple rule:

- **One question, one answer** → no flags: `docker exec msg cat data/messages.txt`
- **Go in and stay a while** → `-it`: `docker exec -it msg bash`

## When there's no bash

Some images are kept very small and don't include `bash`. If you try it, you'll see:

```
OCI runtime exec failed: exec failed: unable to start container process: exec: "bash": executable file not found in $PATH
```

That only means "there's no program called bash in here". Use **`sh`** instead, a smaller shell that's in almost every image:

```bash
docker exec -it msg sh
```

## Changes inside don't last

You can create and change files while you're inside. But remember page 3: they live in this container only. When the container is removed, they go with it.

So going inside is for **looking and checking**. A real fix goes in `app.js` or the Dockerfile, and then you build again.

## Check yourself

1. What's the difference between `docker exec msg ls` and `docker exec -it msg bash`?
2. What does `-i` do? What does `-t` do? What happens if you only use `-t`?
3. You type `exit` inside the container. Is the `msg` container still running?

## Next

Clean up:

```bash
docker rm -f msg
```

That's how you look inside any container, not only this one. Next, Vikash will pick what comes after.
