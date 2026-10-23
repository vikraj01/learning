# Frontend, backend, database

After this page you'll know what a frontend, a backend and a database are, and you'll know your way around a small todo app built from all three.

## A restaurant

Think of a restaurant:

- The **dining room** is what you see: the menu, the tables, the waiter. You never walk into the kitchen.
- The **kitchen** does the real work. It takes your order, cooks, and sends the plate out.
- The **pantry** is where the food is kept. Only the kitchen goes in there.

Most apps you use are built the same way, in three parts.

## The three parts

- **Frontend**: the dining room. The page you see in the browser: the HTML, the colours (CSS), and the bit of JavaScript that reacts when you click. Ours is served by **nginx** (say "engine-x"), the web server you met in section 1.
- **Backend**: the kitchen. A program that does the work: it takes requests like "add this todo", checks them, and talks to the database. Ours is a small Node + Express app, like the message box.
- **Database**: the pantry. It keeps the data safe, in **tables**, like a spreadsheet with rows and columns. Ours is **Postgres** (PostgreSQL, say "post-gress"), one of the most used databases in the world.

Each part runs in its own container. That makes three containers that work together, and on the next pages you'll start all three with **one** command.

## The app: a todo list

It looks like this: a card with a text box, an **Add** button, and your list. Click the circle to tick a todo off, click **×** to delete it.

```
 ┌──────────────────────────────────┐
 │  Todo                            │
 │  1 of 2 left to do               │
 │  [ What needs doing?    ] [Add]  │
 │  ✓  Learn Docker Compose      ×  │
 │  ○  Water the plants          ×  │
 └──────────────────────────────────┘
```

## Where it lives

The finished project is in this section's folder, `docs/07-compose/todo-app/`. Open that folder in VS Code and look around:

```
todo-app/
  compose.yaml          ← the plan for all three parts (page 3)
  frontend/
    index.html          ← the page
    style.css           ← the colours and layout
    app.js              ← clicks → requests to the backend
    nginx.conf          ← nginx's settings
    Dockerfile
  backend/
    app.js              ← the API: list, add, tick, delete
    Dockerfile
  db/
    init.sql            ← makes the table, the first time
```

## A few words first

- **API** (Application Programming Interface): the list of things a backend lets you ask for, each at its own address. Ours:

  | Ask | At | Does |
  | --- | --- | --- |
  | GET | `/api/todos` | list every todo |
  | POST | `/api/todos` | add one |
  | PATCH | `/api/todos/3` | tick or untick todo 3 |
  | DELETE | `/api/todos/3` | delete todo 3 |

  You know GET and POST from the message box. **PATCH** means "change a bit of this", and **DELETE** means what it says.

- **JSON** (say "jay-son"): the way the backend and frontend send data to each other. It's plain text that looks like this:

  ```json
  {"id": 3, "text": "Water the plants", "done": false}
  ```

- **SQL** (say "sequel" or "S-Q-L"): the language for talking to a database. The backend sends SQL like `SELECT id, text, done FROM todos`: "give me these columns from the todos table".

## The three files that matter most

**`frontend/app.js`**: when you click **Add**, it sends your text to the backend:

```js
await fetch("/api/todos", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ text: input.value }),
});
```

**`backend/app.js`**: the backend receives it and puts it in the database with SQL:

```js
app.post("/api/todos", async (req, res) => {
  const result = await db.query(
    "INSERT INTO todos (text) VALUES ($1) RETURNING id, text, done",
    [req.body.text]
  );
  res.status(201).json(result.rows[0]);
});
```

`$1` is a blank that gets filled with your text, safely. `RETURNING` asks the database to hand back the new row, with its new `id`. `201` means "created".

**`db/init.sql`**: makes the `todos` table, and puts two todos in to start with:

```sql
CREATE TABLE todos (
  id   SERIAL PRIMARY KEY,
  text TEXT NOT NULL,
  done BOOLEAN NOT NULL DEFAULT false
);

INSERT INTO todos (text) VALUES ('Learn Docker Compose'), ('Make chai');
```

Three columns: `id` (a number the database counts up by itself), `text`, and `done` (true or false, `false` to begin with).

## One request, all the way through

You type "Water the plants" and press **Add**. Here's the journey:

[Diagram: three parts, one request](./todo-architecture.excalidraw)

1. The browser sends `POST /api/todos` to `localhost:8080`.
2. The `-p 8080:80` door passes it to the frontend container (nginx), on port 80.
3. nginx sees the address starts with `/api/`, so it passes it on to the backend, at `backend:3000`. (A name! You know this from section 4.)
4. The backend runs `INSERT INTO todos ...` on the database, at `db:5432`. Postgres saves the row in its volume.
5. The answer goes back the same way, and the page redraws your list.

Notice that only the frontend has a door to your laptop. The kitchen and the pantry are private.

## Check yourself

1. In the restaurant, which part is the frontend, which the backend, which the database?
2. Which part talks to the database? Can the browser talk to it directly?
3. What does `POST /api/todos` do? And `DELETE /api/todos/3`?

## Next

Start all three containers by hand, with the commands you already know, and see how much work it is: [running it by hand](02-without-compose.md).
