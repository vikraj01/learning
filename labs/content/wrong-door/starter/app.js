const http = require("http");

const PORT = 5000;

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/html" });
  res.end("<h1>Quiet app</h1><p>You found the right door.</p>");
});

server.listen(PORT, () => {
  console.log(`Quiet app is listening on port ${PORT}`);
});
