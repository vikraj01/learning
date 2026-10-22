const express = require("express");
const fs = require("fs");

const app = express();
app.use(express.urlencoded());

const form = `
<!doctype html>
<html>
  <body>
    <h1>Producer: write a message</h1>
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
  console.log("Producer is running on http://localhost:3000/web");
});
