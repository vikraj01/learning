// A real bash in the browser: each WebSocket gets its own shell, started in the lab's folder.
// pty-bridge.py gives bash a real terminal, so colours, Ctrl+C and full-screen tools work.

import fs from "node:fs";
import path from "node:path";
import type http from "node:http";
import { spawn } from "node:child_process";
import type { Writable } from "node:stream";
import { WebSocketServer } from "ws";
import { readLab } from "./labs.ts";

type Message = { type: "input"; data: string } | { type: "resize"; cols: number; rows: number };

export function attachTerminal(server: http.Server) {
  const wss = new WebSocketServer({ server, path: "/term" });

  wss.on("connection", (socket, req) => {
    const url = new URL(req.url ?? "", "http://localhost");
    const lab = readLab(url.searchParams.get("lab") ?? "");
    if (!lab) return socket.close();
    fs.mkdirSync(lab.workspace, { recursive: true });

    const cols = String(Number(url.searchParams.get("cols")) || 100);
    const rows = String(Number(url.searchParams.get("rows")) || 24);
    const shell = spawn(
      "python3",
      [path.join(import.meta.dirname, "pty-bridge.py"), cols, rows, path.join(import.meta.dirname, "bashrc")],
      {
        cwd: lab.workspace,
        env: { ...process.env, TERM: "xterm-256color", COLORTERM: "truecolor", LAB_WORKSPACE: lab.workspace },
        stdio: ["pipe", "pipe", "pipe", "pipe"],
      }
    );
    const control = shell.stdio[3] as Writable;

    const send = (d: Buffer) => socket.readyState === socket.OPEN && socket.send(d);
    shell.stdout!.on("data", send);
    shell.stderr!.on("data", send);
    shell.on("close", () => socket.readyState === socket.OPEN && socket.close());

    socket.on("message", (raw) => {
      let msg: Message;
      try {
        msg = JSON.parse(String(raw));
      } catch {
        return;
      }
      if (msg.type === "input") shell.stdin!.write(msg.data);
      if (msg.type === "resize") control.write(`${msg.cols | 0} ${msg.rows | 0}\n`);
    });
    socket.on("close", () => shell.kill("SIGHUP"));
  });
}
