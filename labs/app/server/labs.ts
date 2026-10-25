// Labs live in labs/content/<id>/: lab.json, task.md, starter/, setup.sh, check.sh, cleanup.sh.
// Each lab gets its own working folder in labs/workspace/<id>/.

import fs from "node:fs";
import path from "node:path";
import { spawn } from "node:child_process";

export const ROOT = path.resolve(import.meta.dirname, "..", "..");
const CONTENT = path.join(ROOT, "content");
export const WORKSPACES = path.join(ROOT, "workspace");
const PROGRESS_FILE = path.join(ROOT, ".progress.json");

export interface Task {
  id: string;
  title: string;
  hint: string;
}

export interface Track {
  id: string;
  title: string;
  description: string;
}

export interface Lab {
  id: string;
  number: number;
  track: string;
  title: string;
  summary: string;
  level: string;
  minutes: number;
  topics: string[];
  tasks: Task[];
  dir: string;
  workspace: string;
}

export interface CheckResult {
  pass: boolean;
  message: string;
}

interface Progress {
  solved: Record<string, string>;
  started: Record<string, string>;
}

export function readLab(id: string): Lab | null {
  if (!/^[a-z0-9-]+$/.test(id)) return null;
  const dir = path.join(CONTENT, id);
  const file = path.join(dir, "lab.json");
  if (!fs.existsSync(file)) return null;
  const meta = JSON.parse(fs.readFileSync(file, "utf8"));
  return { ...meta, id, dir, workspace: path.join(WORKSPACES, id) };
}

export function readTracks(): Track[] {
  const file = path.join(CONTENT, "tracks.json");
  return fs.existsSync(file) ? JSON.parse(fs.readFileSync(file, "utf8")) : [];
}

export function listLabs(): Lab[] {
  return fs
    .readdirSync(CONTENT, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => readLab(d.name))
    .filter((l): l is Lab => l !== null)
    .sort((a, b) => a.number - b.number);
}

export function publicLab(lab: Lab) {
  const { dir: _dir, workspace: _workspace, ...rest } = lab;
  return rest;
}

export function readProgress(): Progress {
  try {
    return JSON.parse(fs.readFileSync(PROGRESS_FILE, "utf8"));
  } catch {
    return { solved: {}, started: {} };
  }
}

function saveProgress(p: Progress) {
  fs.writeFileSync(PROGRESS_FILE, JSON.stringify(p, null, 2));
}

function runScript(lab: Lab, name: string, timeoutMs: number): Promise<{ code: number; output: string }> {
  return new Promise((resolve) => {
    const script = path.join(lab.dir, name);
    if (!fs.existsSync(script)) return resolve({ code: 0, output: "" });
    fs.mkdirSync(lab.workspace, { recursive: true });
    const child = spawn("bash", [script], {
      cwd: lab.workspace,
      env: { ...process.env, LAB_ID: lab.id, LAB_DIR: lab.dir, LAB_WORKSPACE: lab.workspace },
    });
    let output = "";
    child.stdout.on("data", (d) => (output += d));
    child.stderr.on("data", (d) => (output += d));
    const timer = setTimeout(() => child.kill("SIGKILL"), timeoutMs);
    child.on("close", (code) => {
      clearTimeout(timer);
      resolve({ code: code ?? 1, output });
    });
  });
}

// Copy the starter files, then run setup.sh. With fresh=true, clean everything up first.
export async function prepare(lab: Lab, fresh: boolean) {
  if (fresh) {
    await runScript(lab, "cleanup.sh", 60_000);
    fs.rmSync(lab.workspace, { recursive: true, force: true });
    const progress = readProgress();
    delete progress.solved[lab.id];
    saveProgress(progress);
  }
  const starter = path.join(lab.dir, "starter");
  fs.mkdirSync(lab.workspace, { recursive: true });
  if (fs.existsSync(starter)) fs.cpSync(starter, lab.workspace, { recursive: true });

  const result = await runScript(lab, "setup.sh", 600_000);
  const progress = readProgress();
  progress.started[lab.id] = new Date().toISOString();
  saveProgress(progress);
  return result;
}

// check.sh prints one line per task: "PASS <task-id> <message>" or "FAIL <task-id> <message>".
export async function check(lab: Lab) {
  const { output } = await runScript(lab, "check.sh", 120_000);
  const results: Record<string, CheckResult> = {};
  for (const line of output.split("\n")) {
    const m = line.match(/^(PASS|FAIL)\s+(\S+)\s*(.*)$/);
    if (m) results[m[2]] = { pass: m[1] === "PASS", message: m[3] };
  }
  const solved = lab.tasks.every((t) => results[t.id]?.pass);
  if (solved) {
    const progress = readProgress();
    progress.solved[lab.id] ??= new Date().toISOString();
    saveProgress(progress);
  }
  return { solved, results };
}
