On the left is **greet**, the tiny app from sections 9–14. Open `app.js`: it reads three **environment variables** (settings handed to a program from outside):

```js
const port = process.env.PORT || 3000;
const name = process.env.NAME || "friend";
const color = process.env.COLOR || "white";
```

The lab already built it into an image called `greet-lab`. The `Dockerfile` sets one setting of its own: `ENV COLOR=lightblue`.

## Your job

1. Run a container called `hello` from `greet-lab`, on **http://localhost:3400** (the app listens on **3000** inside).
2. Make the page say **Hello, &lt;your name&gt;!** instead of "friend".
3. Make the page **pink**.

Don't change `app.js` or the `Dockerfile`: settings come from outside.

## Commands that help

```
docker run -d --name hello -p 3400:3000 -e NAME=... greet-lab
docker exec hello env          # the settings the container really has
docker rm -f hello
```

> Who wins? A `-e` on `docker run` beats the `ENV` in the Dockerfile, and the `ENV` beats the default in the code.
