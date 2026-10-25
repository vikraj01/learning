A container called `vault` is running. Somewhere under the folder **`/var/lib/vault`** inside it, there's a file with a **secret code**: one word.

## Your job

1. Go **inside** the running container and find the code.
2. Write the code into the file `answer.txt` (on the left) and save it.

## Going inside

```
docker exec -it vault sh
```

- `docker exec` runs a command **inside** a container that's already running.
- `-it` makes it interactive: you can type, like a normal terminal.
- `sh` is the command to run: a shell.

The prompt changes. Now every command runs **inside** the container. Type `exit` to come back to your laptop.

## Commands for looking around

```
pwd          where am I?
ls           what's in this folder?
ls -a        ...including hidden files (names starting with a dot)
cd <folder>  go into a folder
cat <file>   show what's in a file
```
