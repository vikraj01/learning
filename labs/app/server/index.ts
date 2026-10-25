// Docker Labs server. Listens on 127.0.0.1 only: it hands a shell to the browser.

import fs from "node:fs";
import path from "node:path";
import http from "node:http";
import express, { type Request, type Response } from "express";
import { WORKSPACES, check, listLabs, prepare, publicLab, readLab, readProgress, readTracks, type Lab } from "./labs.ts";
import { safePath, tree } from "./files.ts";
import { attachTerminal } from "./terminal.ts";

const PORT = Number(process.env.PORT ?? 7000);
const DIST = path.resolve(import.meta.dirname, "..", "dist");

const app = express();
app.use(express.json({ limit: "2mb" }));

function labOr404(req: Request, res: Response): Lab | null {
  const lab = readLab(req.params.id);
  if (!lab) res.status(404).json({ error: "No such lab" });
  return lab;
}

// ---------- labs ----------

app.get("/api/tracks", (_req, res) => res.json(readTracks()));

app.get("/api/labs", (_req, res) => {
  const progress = readProgress();
  res.json(
    listLabs().map((lab) => ({
      ...publicLab(lab),
      solved: Boolean(progress.solved[lab.id]),
      started: Boolean(progress.started[lab.id]),
    }))
  );
});

app.get("/api/labs/:id", (req, res) => {
  const lab = labOr404(req, res);
  if (!lab) return;
  const progress = readProgress();
  const all = listLabs();
  const next = all[all.findIndex((l) => l.id === lab.id) + 1];
  res.json({
    ...publicLab(lab),
    task: fs.readFileSync(path.join(lab.dir, "task.md"), "utf8"),
    solved: Boolean(progress.solved[lab.id]),
    started: Boolean(progress.started[lab.id]),
    ready: fs.existsSync(lab.workspace),
    next: next ? { id: next.id, title: next.title } : null,
    trackTitle: readTracks().find((t) => t.id === lab.track)?.title ?? "",
  });
});

const busy = new Set<string>();

async function setUp(req: Request, res: Response, fresh: boolean) {
  const lab = labOr404(req, res);
  if (!lab) return;
  if (!fresh && fs.existsSync(lab.workspace)) return res.json({ ok: true, output: "" });
  if (busy.has(lab.id)) return res.status(409).json({ error: "This lab is already being set up" });
  busy.add(lab.id);
  try {
    const r = await prepare(lab, fresh);
    res.json({ ok: r.code === 0, output: r.output });
  } finally {
    busy.delete(lab.id);
  }
}

app.post("/api/labs/:id/start", (req, res) => setUp(req, res, false));
app.post("/api/labs/:id/reset", (req, res) => setUp(req, res, true));

app.post("/api/labs/:id/check", async (req, res) => {
  const lab = labOr404(req, res);
  if (!lab) return;
  res.json(await check(lab));
});

// ---------- files ----------

app.get("/api/labs/:id/tree", (req, res) => {
  const lab = labOr404(req, res);
  if (lab) res.json(tree(lab.workspace));
});

app.get("/api/labs/:id/file", (req, res) => {
  const lab = labOr404(req, res);
  if (!lab) return;
  const full = safePath(lab, req.query.path);
  if (!full || !fs.existsSync(full) || fs.statSync(full).isDirectory())
    return res.status(404).json({ error: "No such file" });
  const stat = fs.statSync(full);
  if (stat.size > 1_000_000) return res.status(413).json({ error: "This file is too big to open here" });
  res.json({ content: fs.readFileSync(full, "utf8"), mtime: stat.mtimeMs });
});

app.put("/api/labs/:id/file", (req, res) => {
  const lab = labOr404(req, res);
  if (!lab) return;
  const full = safePath(lab, req.body.path);
  if (!full) return res.status(400).json({ error: "That name points outside the lab folder" });
  fs.mkdirSync(path.dirname(full), { recursive: true });
  fs.writeFileSync(full, String(req.body.content ?? ""));
  res.json({ mtime: fs.statSync(full).mtimeMs });
});

app.post("/api/labs/:id/folder", (req, res) => {
  const lab = labOr404(req, res);
  if (!lab) return;
  const full = safePath(lab, req.body.path);
  if (!full) return res.status(400).json({ error: "That name points outside the lab folder" });
  fs.mkdirSync(full, { recursive: true });
  res.json({ ok: true });
});

app.delete("/api/labs/:id/file", (req, res) => {
  const lab = labOr404(req, res);
  if (!lab) return;
  const full = safePath(lab, req.query.path);
  if (!full) return res.status(400).json({ error: "Can't delete that" });
  fs.rmSync(full, { recursive: true, force: true });
  res.json({ ok: true });
});

// ---------- the built site ----------

if (fs.existsSync(DIST)) {
  app.use(express.static(DIST));
  app.get("*", (_req, res) => res.sendFile(path.join(DIST, "index.html")));
}

const server = http.createServer(app);
attachTerminal(server);
fs.mkdirSync(WORKSPACES, { recursive: true });
server.listen(PORT, "127.0.0.1", () => {
  console.log(`\n  Docker Labs is running:  http://localhost:${PORT}\n  Stop it with Ctrl+C.\n`);
});
