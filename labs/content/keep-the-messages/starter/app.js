const express = require("express");
const fs = require("fs");

const app = express();
app.use(express.urlencoded());

// The messages are kept in /app/data/messages.txt
const FILE = "data/messages.txt";

const page = (messages) => `
<!doctype html>
<html>
  <body style="font-family: sans-serif; max-width: 32rem; margin: 2rem auto;">
    <h1>Message box</h1>
    <form action="/send" method="post">
      <input name="message" placeholder="Write something" required>
      <button type="submit">Send</button>
    </form>
    <ul>${messages.map((m) => `<li>${m.replace(/</g, "&lt;")}</li>`).join("")}</ul>
  </body>
</html>`;

function read() {
  if (!fs.existsSync(FILE)) return [];
  return fs.readFileSync(FILE, "utf8").split("\n").filter((line) => line !== "");
}

app.get("/web", (req, res) => res.send(page(read())));

app.post("/send", (req, res) => {
  fs.mkdirSync("data", { recursive: true });
  fs.appendFileSync(FILE, req.body.message + "\n");
  res.redirect("/web");
});

app.listen(8080, () => console.log("Message box is running on port 8080"));
