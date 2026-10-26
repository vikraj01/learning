# Settings in a file: how an app reads `.env`

After this page you'll know what a `.env` file is, why it does **nothing** on its own, and the two ways an app can get its settings out of it.

## A note on the fridge

Mum leaves a note on the fridge: "dinner at 8, buy milk". The note doesn't do anything by itself. Somebody has to **read** it. If nobody looks at the fridge, nothing happens.

A `.env` file is that note. It's an ordinary text file. Your app only gets the settings if **someone reads the file** and turns each line into an environment variable.

## Make the file

In your `greet` folder, make a file called `.env` (the name starts with a dot):

```
NAME=Tanvi
COLOR=pink
```

Rules:

- one setting per line: `NAME=value`
- no spaces around `=`
- no `export`, no quotes needed

Your folder:

```
greet/
├── app.js
├── say.js
└── .env
```

## Try it: the file does nothing on its own

```bash
node app.js
```

```
Saying hello to friend on port 3000
```

Open <http://localhost:3000>: white page, **Hello, friend!** The file is sitting right there, but `app.js` only looks at `process.env`, and nobody put the file's lines there. Stop it with `Ctrl+C`.

There are two ways to fix that. Either **Node reads the file** before your app starts, or **your app reads the file** itself.

## Way 1: Node reads the file (`--env-file`)

```bash
node --env-file=.env app.js
```

```
Saying hello to Tanvi on port 3000
```

Pink page, **Hello, Tanvi!**

What happened, step by step:

1. Node opens `.env`.
2. It turns each line into an environment variable: `NAME=Tanvi`, `COLOR=pink`.
3. It starts `app.js`. The app finds them in `process.env`, as if you'd typed `NAME=Tanvi COLOR=pink node app.js`.

`app.js` didn't change at all. It doesn't even know a file was involved. Stop it with `Ctrl+C`.

## Way 2: the app reads the file itself

Now let the app do the reading, so a plain `node app.js` is enough. Add these lines at the very **top** of `app.js`:

```js
const fs = require("fs");

if (fs.existsSync(".env")) {
  process.loadEnvFile();
}
```

- **`fs`** is Node's built-in module for files ("file system").
- **`fs.existsSync(".env")`** asks "is there a `.env` file in this folder?"
- **`process.loadEnvFile()`** reads `.env` and puts every line into `process.env`.

So: *if there's a `.env` file here, load it.* If there isn't, carry on with the defaults. (Without the `if`, the app would crash when the file is missing.)

The top of `app.js` now looks like this:

```js
const fs = require("fs");
const http = require("http");

if (fs.existsSync(".env")) {
  process.loadEnvFile();
}

const port = process.env.PORT || 3000;
const name = process.env.NAME || "friend";
const color = process.env.COLOR || "white";
```

The rest stays the same. Run it, with no flags:

```bash
node app.js
```

```
Saying hello to Tanvi on port 3000
```

Pink page, **Hello, Tanvi!** This time the app read the note itself.

> **Good to know:** most real Node projects do this with a small package called **dotenv**: `require("dotenv").config()` at the top of the file. It does the same job as `process.loadEnvFile()`. You'll see it everywhere.

## When the file and a real setting disagree

What if `.env` says `COLOR=pink`, but you also set `COLOR` when starting the app?

```bash
COLOR=green node app.js
```

Open <http://localhost:3000>: **green** page, still **Hello, Tanvi!**

A setting that's **already** in the environment always wins. The file only fills in what's missing: `NAME` came from the file, `COLOR` didn't. This is true for both ways (`--env-file` and `process.loadEnvFile()`).

Remember this one. It matters a lot on page 4, inside Docker.

From weakest to strongest:

| Where the setting comes from | Example | Wins over |
| --- | --- | --- |
| the default in the code | `"white"` in `app.js` | nothing |
| the `.env` file | `COLOR=pink` | the default |
| a real environment variable | `COLOR=green node app.js` | the file and the default |

[Diagram: who reads the .env file](./who-reads-env.excalidraw)

## Keep `.env` out of git

Real `.env` files hold passwords. So projects list it in a file called **`.gitignore`**, which tells git "never save this file". Ours only has a name and a colour, so it's fine here.

## Check yourself

1. You have a `.env` file and run plain `node app.js` with the **original** `app.js` (without `loadEnvFile`). Which name does the page show? Why?
2. In Way 1, who reads the file: Node or `app.js`? And in Way 2?
3. `.env` says `NAME=Tanvi`. You run `NAME=Ravi node app.js`. Who does the page say hello to?

## Next

[Environment variables in Docker](03-env-in-docker.md): the same settings, given to a container.
