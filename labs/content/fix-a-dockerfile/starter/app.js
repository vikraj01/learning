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
  fs.appendFileSync("messages.txt", req.body.message + "\n");
  res.send('Saved! <a href="/web">Write another</a>');
});

app.get("/messages", (req, res) => {
  if (!fs.existsSync("messages.txt")) {
    res.json([]);
    return;
  }
  const text = fs.readFileSync("messages.txt", "utf8");
  res.json(text.split("\n").filter((line) => line !== ""));
});

app.listen(8080, () => {
  console.log("Message box is running on http://localhost:8080/web");
});
