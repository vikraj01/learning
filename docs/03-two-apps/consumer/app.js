const express = require("express");
const fs = require("fs");

const app = express();

app.get("/read", (req, res) => {
  let text = "";
  if (fs.existsSync("data/messages.txt")) {
    text = fs.readFileSync("data/messages.txt", "utf8");
  }
  const lines = text.split("\n").filter((line) => line !== "");

  if (lines.length === 0) {
    res.send("<h1>Consumer: messages</h1><p>No messages yet.</p>");
    return;
  }

  const items = lines.map((line) => `<li>${line}</li>`).join("");
  res.send(`<h1>Consumer: messages</h1><ul>${items}</ul>`);
});

app.listen(4000, () => {
  console.log("Consumer is running on http://localhost:4000/read");
});
