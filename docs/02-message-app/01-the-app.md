# A small web app: the message box

After this page you'll have your own little web app running: a page with a form, and a place where everything you send gets saved.

## The idea

Think of a suggestion box in a shop:

1. You pick up a blank slip at the counter.
2. You write on it and drop it in the box.
3. The shopkeeper keeps every slip in a file.

Our app does the same thing, with two addresses:

- **`/web`** gives you the blank slip: a page with a text box and a **Send** button.
- **`/send`** takes what you wrote and adds it to a file called `messages.txt`.

[Diagram: how the app works](./app-flow.excalidraw)

## A few words first

- **Server**: a program that waits for the browser to ask for something, and answers. Our app is a server.
- **Node.js**: lets you run JavaScript on your laptop, outside the browser. You start it with the `node` command.
- **Express**: a small helper package for Node that makes writing a server short. **npm** is the tool that downloads packages like it.
- **Route**: one address the server answers, like `/web` or `/send`.

Check Node is installed:

```bash
node --version
```

```
v24.15.0
```

Any number from `v20` up is fine. If you get "command not found", ask Vikash.

## Try it: make the app

Make a folder for the app and download Express into it:

```bash
mkdir message-box
cd message-box
npm install express
```

```
added 65 packages in 2s
```

You'll now see a `node_modules` folder (Express and the packages it needs) and a `package.json` file (a list saying "this app uses Express").

Now make a file called `app.js` in the same folder and type this in:

```js
const express = require("express");
const fs = require("fs");

const app = express();
app.use(express.urlencoded());

const form = `
<!doctype html>
<html>
  <body>
    <h1>Message box</h1>
    <form action="/send" method="post">
      <input name="message" placeholder="Write something">
      <button type="submit">Send</button>
    </form>
  </body>
</html>
`;

app.get("/web", (req, res) => {
  res.send(form);
});

app.post("/send", (req, res) => {
  fs.mkdirSync("data", { recursive: true });
  fs.appendFileSync("data/messages.txt", req.body.message + "\n");
  res.send('Saved! <a href="/web">Write another</a>');
});

app.listen(3000, () => {
  console.log("Message box is running on http://localhost:3000/web");
});
```

## What the parts do

You don't need to understand every symbol yet. Read it in four pieces:

1. **The top**: load Express, and `fs` (short for "file system", Node's tool for reading and writing files). `express.urlencoded()` lets the app read what the form sends.
2. **`form`**: plain HTML. A heading, a text box called `message`, and a button. When you press the button, the browser sends the text to `/send`.
3. **The two routes**:
   - `app.get("/web", ...)`: when the browser **asks for** `/web`, send back the form. **GET** means "give me something".
   - `app.post("/send", ...)`: when the browser **sends** something to `/send`, make a `data` folder if it isn't there yet, add the message to the end of `data/messages.txt`, and say "Saved!". **POST** means "here, take this".
4. **`app.listen(3000, ...)`**: start the server, waiting on door **3000**, and print a line so you know it's running.

## Try it: run it

```bash
node app.js
```

```
Message box is running on http://localhost:3000/web
```

The terminal stays busy: the server is waiting. Open `http://localhost:3000/web` in your browser. Type `hello` and press **Send**. You'll see:

> Saved! Write another

Send one or two more. Then open a **second** terminal, go to the same folder, and look at the file:

```bash
cat data/messages.txt
```

```
hello
my second message
```

Your messages, saved in a file on your laptop.

To stop the server, go back to the first terminal and press `Ctrl + C`.

## Check yourself

1. Which address shows the form, and which one saves the message?
2. What's the difference between GET and POST, in your own words?
3. Where on your laptop do the messages end up?

## Next

Right now the app only runs where Node is installed. Let's put it in a container: [the Dockerfile](02-the-dockerfile.md).
