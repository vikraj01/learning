const cowsay = require("cowsay");

const words = process.argv[2] || "Hello from inside a container!";
console.log(cowsay.say({ text: words }));
