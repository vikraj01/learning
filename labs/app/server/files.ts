// Read and write files inside a lab's working folder, and never outside it.

import fs from "node:fs";
import path from "node:path";
import type { Lab } from "./labs.ts";

export interface TreeNode {
  name: string;
  path: string;
  type: "file" | "dir";
  mtime?: number;
  children?: TreeNode[];
}

const HIDDEN = new Set(["node_modules", ".git"]);

export function safePath(lab: Lab, rel: unknown): string | null {
  if (typeof rel !== "string" || rel === "") return null;
  const full = path.resolve(lab.workspace, rel);
  return full.startsWith(lab.workspace + path.sep) ? full : null;
}

export function tree(dir: string, base = ""): TreeNode[] {
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir, { withFileTypes: true })
    .filter((d) => !HIDDEN.has(d.name))
    .sort((a, b) =>
      a.isDirectory() === b.isDirectory() ? a.name.localeCompare(b.name) : a.isDirectory() ? -1 : 1
    )
    .map((d): TreeNode => {
      const rel = base ? `${base}/${d.name}` : d.name;
      const full = path.join(dir, d.name);
      if (d.isDirectory()) return { name: d.name, path: rel, type: "dir", children: tree(full, rel) };
      return { name: d.name, path: rel, type: "file", mtime: fs.statSync(full).mtimeMs };
    });
}
