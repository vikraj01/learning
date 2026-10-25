The message box saves messages in a file inside the container: `/app/data/messages.txt`. Remove the container and that file goes with it. **Containers forget.**

A **volume** is storage that Docker keeps **outside** any container. Mount it on a folder, and whatever the app writes there lands in the volume. It stays after the container is gone.

## Your job

1. Run the message box (the image `msg-keeper` is already built) as a container called `keeper`, opening on **http://localhost:8099/web**, with a volume called `messages` on the folder `/app/data`.
2. Write a message, then press **Check my work**.
3. Remove `keeper`, start a new one the same way, and see that your message is still there. Press **Check** again.

## The new part

```
-v messages:/app/data
   ────┬─── ────┬───
   volume   folder inside the container
```

## Commands that help

```
docker volume ls
docker volume inspect messages
docker rm -f keeper
```
