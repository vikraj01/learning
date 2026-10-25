After a while, Docker fills up with old stuff: containers that finished long ago, volumes nobody uses. Let's tidy up, carefully.

## What's there now

- `keep-me`: a running website. **Keep it.**
- `sleepy`: a website that was stopped. **Start it again.**
- `old-1` and `old-2`: jobs that finished. **Remove them.**
- Volumes `junk-1` and `junk-2`: **remove them.** Volume `keep-data`: **keep it.**

## Commands that help

```
docker ps          running containers
docker ps -a       all containers, stopped ones too
docker start <name>
docker rm <name>
docker volume ls
docker volume rm <name>
```

> `docker ps` only shows running containers. Stopped ones are still there, taking space, until you remove them.
