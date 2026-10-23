const express = require("express");
const { Pool } = require("pg");

const app = express();
app.use(express.json());

// Where the database is, and how to log in. compose.yaml sets these.
const db = new Pool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

// List every todo
app.get("/api/todos", async (req, res) => {
  const result = await db.query("SELECT id, text, done FROM todos ORDER BY id");
  res.json(result.rows);
});

// Add a todo
app.post("/api/todos", async (req, res) => {
  const result = await db.query(
    "INSERT INTO todos (text) VALUES ($1) RETURNING id, text, done",
    [req.body.text]
  );
  res.status(201).json(result.rows[0]);
});

// Tick or untick a todo
app.patch("/api/todos/:id", async (req, res) => {
  const result = await db.query(
    "UPDATE todos SET done = NOT done WHERE id = $1 RETURNING id, text, done",
    [req.params.id]
  );
  res.json(result.rows[0]);
});

// Delete a todo
app.delete("/api/todos/:id", async (req, res) => {
  await db.query("DELETE FROM todos WHERE id = $1", [req.params.id]);
  res.status(204).end();
});

app.listen(3000, () => {
  console.log(`Backend is running on port 3000, database at ${process.env.DB_HOST}`);
});
