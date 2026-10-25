The lab started the **Quiet app** for you:

```
docker run -d --name quiet -p 8098:8080 quiet-app
```

`docker ps` says it's **Up**. But **http://localhost:8098** doesn't open.

## Your job

Find out why, and make the page open on **http://localhost:8098**, **without changing the code**.

## How to investigate

```
docker ps                 is it running? which door is open?
docker logs quiet         what did the app print when it started?
```

> A door on your laptop (`8098`) only helps if it leads to the door the app is **really** listening on inside the container.
