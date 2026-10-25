const express = require("express");

const app = express();
app.use(express.urlencoded({ extended: false }));

// Where is the api? The container named "api", on port 4000
const API_URL = "http://api:4000";

const page = (body) => `
<!doctype html>
<html>
  <body style="font-family: system-ui, sans-serif; max-width: 36rem; margin: 2rem auto; padding: 0 1rem;">
    <h1>My notes</h1>
    <form action="/add" method="post">
      <input name="text" placeholder="Write a note" autofocus required>
      <button>Save</button>
    </form>
    ${body}
    <p style="color: gray;">web is calling the api at ${API_URL}</p>
  </body>
</html>`;

const problem = (err) =>
  `<p style="color: crimson;"><b>web can't reach the api:</b> ${err.cause?.code || err.message}</p>`;

app.get("/", async (req, res) => {
  try {
    const r = await fetch(API_URL + "/notes");
    const data = await r.json();
    if (data.error) return res.send(page(`<p style="color: crimson;"><b>${data.error}</b></p>`));
    res.send(page(`<ul>${data.map((n) => `<li>${n.replace(/</g, "&lt;")}</li>`).join("")}</ul>`));
  } catch (err) {
    res.send(page(problem(err)));
  }
});

app.post("/add", async (req, res) => {
  try {
    await fetch(API_URL + "/notes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: req.body.text }),
    });
    res.redirect("/");
  } catch (err) {
    res.send(page(problem(err)));
  }
});

app.listen(3000, "0.0.0.0", () => console.log(`web on port 3000, api at ${API_URL}`));
