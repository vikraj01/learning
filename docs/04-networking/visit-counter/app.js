const express = require("express");
const { createClient } = require("redis");

const app = express();

// Where the database is. "db" is the name of the Redis container.
const DB_URL = process.env.DB_URL || "redis://db:6379";

app.get("/", async (req, res) => {
  const db = createClient({ url: DB_URL, socket: { reconnectStrategy: false } });
  db.on("error", () => {});

  try {
    await db.connect();
    const visits = await db.incr("visits");
    await db.close();
    res.send(`<h1>Visit counter</h1><p>Visits so far: <b>${visits}</b></p>`);
  } catch (error) {
    res.send(`<h1>Visit counter</h1><p>Could not reach the database at ${DB_URL}</p><p>Reason: ${error.code || error.message}</p>`);
  }
});

app.listen(3000, () => {
  console.log(`Visit counter is running on port 3000, using the database at ${DB_URL}`);
});
