const list = document.querySelector("#list");
const count = document.querySelector("#count");
const form = document.querySelector("#new");
const input = document.querySelector("#text");

// Ask the backend for the todos, and draw them.
async function load() {
  const response = await fetch("/api/todos");
  const todos = await response.json();

  const left = todos.filter((todo) => !todo.done).length;
  count.textContent = `${left} of ${todos.length} left to do`;

  list.innerHTML = "";
  for (const todo of todos) {
    const item = document.createElement("li");
    item.className = todo.done ? "done" : "";
    item.innerHTML = `<button class="tick">✓</button><span></span><button class="remove">×</button>`;
    item.querySelector("span").textContent = todo.text;

    item.querySelector(".tick").onclick = async () => {
      await fetch(`/api/todos/${todo.id}`, { method: "PATCH" });
      load();
    };
    item.querySelector(".remove").onclick = async () => {
      await fetch(`/api/todos/${todo.id}`, { method: "DELETE" });
      load();
    };
    list.append(item);
  }
}

// Send a new todo to the backend.
form.onsubmit = async (event) => {
  event.preventDefault();
  await fetch("/api/todos", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: input.value }),
  });
  input.value = "";
  load();
};

load();
