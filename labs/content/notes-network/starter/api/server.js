const express = require("express");
const { Pool } = require("pg");

const app = express();
app.use(express.json());

// Where is the database? The container named "db"
const DB_HOST = "db";
const db = new Pool({ host: DB_HOST, user: "postgres", password: "secret", database: "postgres" });

const dbError = (res, err) =>
  res.status(500).json({ error: `api can't reach the database at "${DB_HOST}": ${err.code || err.message}` });

app.get("/notes", async (req, res) => {
  try {
    await db.query("CREATE TABLE IF NOT EXISTS notes (id SERIAL PRIMARY KEY, text TEXT NOT NULL)");
    const result = await db.query("SELECT text FROM notes ORDER BY id");
    res.json(result.rows.map((row) => row.text));
  } catch (err) { dbError(res, err); }
});

app.post("/notes", async (req, res) => {
  try {
    await db.query("CREATE TABLE IF NOT EXISTS notes (id SERIAL PRIMARY KEY, text TEXT NOT NULL)");
    await db.query("INSERT INTO notes (text) VALUES ($1)", [req.body.text]);
    res.json({ ok: true });
  } catch (err) { dbError(res, err); }
});

app.listen(4000, "0.0.0.0", () => console.log(`api on port 4000, database host: ${DB_HOST}`));
