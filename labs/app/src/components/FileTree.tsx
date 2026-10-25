import { useState } from "react";
import type { TreeNode } from "../types";
import { ChevronDown, ChevronRight, FileIcon, FolderIcon, NewFile, NewFolder, Refresh, Trash } from "./Icons";

interface Props {
  nodes: TreeNode[];
  active: string | null;
  onOpen: (path: string) => void;
  onCreate: (path: string, kind: "file" | "folder") => Promise<void>;
  onDelete: (path: string) => Promise<void>;
  onRefresh: () => void;
}

export default function FileTree({ nodes, active, onOpen, onCreate, onDelete, onRefresh }: Props) {
  const [closed, setClosed] = useState<Set<string>>(new Set());
  const [creating, setCreating] = useState<"file" | "folder" | null>(null);
  const [name, setName] = useState("");
  const [error, setError] = useState("");
  const [confirmDelete, setConfirmDelete] = useState<string | null>(null);

  const toggle = (path: string) =>
    setClosed((prev) => {
      const next = new Set(prev);
      if (next.has(path)) next.delete(path);
      else next.add(path);
      return next;
    });

  async function submit() {
    const clean = name.trim().replace(/^\/+/, "");
    if (!clean) return setCreating(null);
    try {
      await onCreate(clean, creating!);
      setCreating(null);
      setName("");
      setError("");
    } catch (e) {
      setError((e as Error).message);
    }
  }

  function render(list: TreeNode[], depth: number): React.ReactNode {
    return list.map((node) => {
      const pad = { paddingLeft: 10 + depth * 14 };
      const isClosed = closed.has(node.path);
      const confirming = confirmDelete === node.path;
      return (
        <div key={node.path}>
          <div
            className={`tree-item ${node.type}${active === node.path ? " active" : ""}${confirming ? " confirm-del" : ""}`}
            style={pad}
            role="button"
            tabIndex={0}
            onClick={() => (node.type === "dir" ? toggle(node.path) : onOpen(node.path))}
            onKeyDown={(e) => e.key === "Enter" && (node.type === "dir" ? toggle(node.path) : onOpen(node.path))}
            onMouseLeave={() => confirming && setConfirmDelete(null)}
          >
            <span className="ico">
              {node.type === "dir" ? (isClosed ? <ChevronRight size={14} /> : <ChevronDown size={14} />) : <span style={{ width: 14 }} />}
            </span>
            <span className="ico">{node.type === "dir" ? <FolderIcon size={15} /> : <FileIcon size={15} />}</span>
            <span className="name">{confirming ? `Delete ${node.name}?` : node.name}</span>
            <button
              className="icon-btn del"
              type="button"
              title={confirming ? "Click again to delete" : "Delete"}
              onClick={(e) => {
                e.stopPropagation();
                if (confirming) {
                  setConfirmDelete(null);
                  onDelete(node.path);
                } else setConfirmDelete(node.path);
              }}
            >
              <Trash />
            </button>
          </div>
          {node.type === "dir" && !isClosed && node.children && render(node.children, depth + 1)}
        </div>
      );
    });
  }

  return (
    <div className="files">
      <div className="pane-head">
        <span className="label">Files</span>
        <button className="icon-btn" type="button" title="New file" onClick={() => { setCreating("file"); setError(""); }}><NewFile /></button>
        <button className="icon-btn" type="button" title="New folder" onClick={() => { setCreating("folder"); setError(""); }}><NewFolder /></button>
        <button className="icon-btn" type="button" title="Refresh" onClick={onRefresh}><Refresh /></button>
      </div>
      <div className="tree">
        {creating && (
          <div className="tree-new">
            <input
              autoFocus
              id="new-name"
              value={name}
              placeholder={creating === "file" ? "name, e.g. Dockerfile" : "folder name"}
              onChange={(e) => setName(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") submit();
                if (e.key === "Escape") { setCreating(null); setName(""); }
              }}
              onBlur={() => !name.trim() && setCreating(null)}
            />
            <small>{error || "Enter to create · Esc to cancel"}</small>
          </div>
        )}
        {nodes.length === 0 && !creating ? (
          <div className="tree-note">This lab starts with no files. Make one with the + button, or work in the terminal.</div>
        ) : (
          render(nodes, 0)
        )}
      </div>
    </div>
  );
}
