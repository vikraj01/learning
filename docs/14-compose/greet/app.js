const fs = require("fs");
const http = require("http");

if (fs.existsSync(".env")) {
  process.loadEnvFile();
}

const port = process.env.PORT || 3000;
const name = process.env.NAME || "friend";
const color = process.env.COLOR || "white";

const server = http.createServer((req, res) => {
  res.setHeader("Content-Type", "text/html");
  res.end(`<body style="background:${color}; font-family:sans-serif">
  <h1>Hello, ${name}! 👋</h1>
  <p>port: ${port} · color: ${color}</p>
</body>`);
});

server.listen(port, () => {
  console.log(`Saying hello to ${name} on port ${port}`);
});
