import type { CheckResponse, LabDetail, LabSummary, Track, TreeNode } from "./types";

async function call<T>(url: string, init?: RequestInit): Promise<T> {
  const res = await fetch(url, {
    ...init,
    headers: init?.body ? { "Content-Type": "application/json" } : undefined,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error ?? `Request failed (${res.status})`);
  return data as T;
}

const lab = (id: string) => `/api/labs/${encodeURIComponent(id)}`;
const q = (path: string) => `?path=${encodeURIComponent(path)}`;

export const api = {
  labs: () => call<LabSummary[]>("/api/labs"),
  tracks: () => call<Track[]>("/api/tracks"),
  lab: (id: string) => call<LabDetail>(lab(id)),
  start: (id: string) => call<{ ok: boolean; output: string }>(`${lab(id)}/start`, { method: "POST" }),
  reset: (id: string) => call<{ ok: boolean; output: string }>(`${lab(id)}/reset`, { method: "POST" }),
  check: (id: string) => call<CheckResponse>(`${lab(id)}/check`, { method: "POST" }),

  tree: (id: string) => call<TreeNode[]>(`${lab(id)}/tree`),
  read: (id: string, path: string) => call<{ content: string; mtime: number }>(`${lab(id)}/file${q(path)}`),
  write: (id: string, path: string, content: string) =>
    call<{ mtime: number }>(`${lab(id)}/file`, { method: "PUT", body: JSON.stringify({ path, content }) }),
  mkdir: (id: string, path: string) =>
    call<{ ok: boolean }>(`${lab(id)}/folder`, { method: "POST", body: JSON.stringify({ path }) }),
  remove: (id: string, path: string) => call<{ ok: boolean }>(`${lab(id)}/file${q(path)}`, { method: "DELETE" }),
};
