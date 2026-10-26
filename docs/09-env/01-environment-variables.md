# Environment variables: settings from outside

After this page you'll be able to give a program settings (a name, a colour, a port) without changing a single line of its code.

## Same recipe, different order

When you order chai, you don't hand the shop a new recipe. You say "less sugar" or "extra ginger". The recipe stays the same; your **order** changes what comes out.

Programs work the same way. The code is the recipe. The settings you give it when you start it are the order.

## The idea

An **environment variable** is a setting with a **name** and a **value**, like `NAME=Tanvi`. It sits around a program when the program starts, and the program can read it.

- Names are usually in CAPITALS: `NAME`, `PORT`, `COLOR`.
- Values are always text. Even `PORT=4000` is the text `"4000"`.
- Every program you start from the terminal gets a copy of the terminal's environment variables.

Your terminal already has lots of them. Try:

```bash
echo $HOME
```

```
/home/tanvi
```

`HOME` is an environment variable holding your home folder. The `$` means "the value of". Yours will show your own folder. To see all of them, type `env`. It's a long list; don't worry about most of it.

## Try it: the greet app

We'll use one small app for this whole section. It's called **greet**, and all it does is say hello.

Make a folder and go into it:

```bash
mkdir greet
cd greet
```

### A hello in the terminal: `say.js`

Make a file called `say.js`:

```js
const name = process.env.NAME || "friend";

console.log(`Hello, ${name}!`);
```

Two new things:

- **`process.env`** is how Node reads environment variables. `process.env.NAME` is the value of `NAME`.
- **`|| "friend"`** means "or, if there's no `NAME`, use `"friend"`". That's a **default**: the value used when nobody gives one.

Run it without any setting:

```bash
node say.js
```

```
Hello, friend!
```

Now put a setting in front of the command:

```bash
NAME=Tanvi node say.js
```

```
Hello, Tanvi!
```

Same code, different output. Run plain `node say.js` again: it's back to `friend`. A setting written in front of a command is only for **that one command**.

To keep a setting for every command in this terminal window, use `export`:

```bash
export NAME=Tanvi
node say.js
```

```
Hello, Tanvi!
```

It stays until you close the window, or remove it with `unset NAME`. Do that now, so the next part starts clean:

```bash
unset NAME
```

### A hello in the browser: `app.js`

Make a second file, `app.js`. It's a small web server that reads **three** settings:

```js
const http = require("http");

const port = process.env.PORT || 3000;
const name = process.env.NAME || "friend";
const color = process.env.COLOR || "white";

const server = http.createServer((req, res) => {
  res.setHeader("Content-Type", "text/html");
  res.end(`<body style="background:${color}; font-family:sans-serif">
  <h1>Hello, ${name}!</h1>
  <p>port: ${port} · color: ${color}</p>
</body>`);
});

server.listen(port, () => {
  console.log(`Saying hello to ${name} on port ${port}`);
});
```

There's no Express this time. Node has a built-in `http` module, so there's nothing to install: no `npm install`, no `node_modules`.

| Setting | What it changes | Default |
| --- | --- | --- |
| `PORT` | the port the server listens on | `3000` |
| `NAME` | who it says hello to | `friend` |
| `COLOR` | the page's background colour | `white` |

Start it with no settings:

```bash
node app.js
```

```
Saying hello to friend on port 3000
```

Open <http://localhost:3000>. A white page says **Hello, friend!**

Stop it with `Ctrl+C`, then start it again with all three settings:

```bash
NAME=Tanvi COLOR=pink PORT=4000 node app.js
```

```
Saying hello to Tanvi on port 4000
```

Open <http://localhost:4000> (the port changed too). A pink page says **Hello, Tanvi!** Stop it with `Ctrl+C`.

Your folder now has two files:

```
greet/
├── app.js
└── say.js
```

## Why this matters

- **Same code, different places.** On your laptop the app uses port 3000; on a real server it might use 80. You change the setting, not the code.
- **Secrets stay out of the code.** Passwords go in environment variables, not in `app.js`.
- **Images can't be edited easily.** Once the app is inside a Docker image, changing its code means building again. Environment variables let you change its behaviour when you *start* it. That's page 3.

## Check yourself

1. What does `NAME=Tanvi node say.js` print? And `node say.js` right after it?
2. In `app.js`, what colour is the page if you don't set `COLOR`? Which part of the code decides that?
3. You start `PORT=5000 node app.js`. Which address do you open in the browser?

## Next

[Settings in a file: how an app reads `.env`](02-the-env-file.md): typing settings every time gets long. Put them in a file instead.
