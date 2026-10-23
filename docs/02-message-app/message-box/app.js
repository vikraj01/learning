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

app.listen(8080, () => {
  console.log("Message box is running on http://localhost:8080/web");
});

app.get("/messages", (req, res) => {
  if (!fs.existsSync("data/messages.txt")) {
    res.json([]);
    return;
  }
  const text = fs.readFileSync("data/messages.txt", "utf8");
  const messages = text.split("\n").filter((line) => line !== "");
  res.json(messages);
});