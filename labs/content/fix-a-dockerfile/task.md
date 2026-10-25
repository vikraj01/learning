Someone wrote a Dockerfile for the **message box** in a hurry. It has **three small mistakes**.

Open `Dockerfile` on the left. `app.js` is the app itself, and it's fine: don't change it.

## Your job

1. Fix the Dockerfile until the image builds.
2. Run it as a container called `box`, and make sure it **stays** running.
3. Open the message box at **http://localhost:8081/web**.

## Commands you'll need

```
docker build -t message-box-fixed .
docker run -d --name box -p 8081:8080 message-box-fixed
docker ps
docker logs box
docker rm -f box
```

> Save the file with **Ctrl + S** before you build again. Docker builds what's saved on disk, not what's on your screen.
