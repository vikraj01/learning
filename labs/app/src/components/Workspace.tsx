import { useCallback, useEffect, useRef, useState } from "react";
import Editor, { type OnMount } from "@monaco-editor/react";
import { api } from "../api";
import { languageFor } from "../monaco";
import type { TreeNode } from "../types";
import FileTree from "./FileTree";
import { Check, Cross } from "./Icons";

interface Tab {
  path: string;
  value: string;
  saved: string;
  mtime: number;
}

function flatten(nodes: TreeNode[], out = new Map<string, TreeNode>()) {
  for (const n of nodes) {
    out.set(n.path, n);
    if (n.children) flatten(n.children, out);
  }
  return out;
}

// The file list, the open tabs and the editor. Files changed from the terminal show up on their own.
export default function Workspace({ labId }: { labId: string }) {
  const [nodes, setNodes] = useState<TreeNode[]>([]);
  const [tabs, setTabs] = useState<Tab[]>([]);
  const [active, setActive] = useState<string | null>(null);
  const [saveState, setSaveState] = useState<"" | "saving" | "saved" | "error">("");
  const tabsRef = useRef(tabs);
  tabsRef.current = tabs;
  const activeRef = useRef(active);
  activeRef.current = active;

  const loadTree = useCallback(async () => {
    const tree = await api.tree(labId).catch(() => null);
    if (!tree) return;
    setNodes(tree);
    // Reload open files that changed on disk (e.g. from the terminal), unless she has unsaved edits.
    const files = flatten(tree);
    for (const tab of tabsRef.current) {
      const node = files.get(tab.path);
      if (node?.mtime && node.mtime > tab.mtime + 1 && tab.value === tab.saved) {
        const fresh = await api.read(labId, tab.path).catch(() => null);
        if (fresh)
          setTabs((ts) => ts.map((t) => (t.path === tab.path ? { ...t, value: fresh.content, saved: fresh.content, mtime: fresh.mtime } : t)));
      }
    }
  }, [labId]);

  useEffect(() => {
    loadTree();
    const timer = setInterval(() => document.visibilityState === "visible" && loadTree(), 2500);
    return () => clearInterval(timer);
  }, [loadTree]);

  async function open(path: string) {
    if (!tabsRef.current.some((t) => t.path === path)) {
      const file = await api.read(labId, path).catch(() => null);
      if (!file) return;
      setTabs((ts) => (ts.some((t) => t.path === path) ? ts : [...ts, { path, value: file.content, saved: file.content, mtime: file.mtime }]));
    }
    setActive(path);
  }

  function close(path: string) {
    setTabs((ts) => {
      const i = ts.findIndex((t) => t.path === path);
      const rest = ts.filter((t) => t.path !== path);
      if (activeRef.current === path) setActive(rest[Math.max(0, i - 1)]?.path ?? null);
      return rest;
    });
  }

  const save = useCallback(async () => {
    const tab = tabsRef.current.find((t) => t.path === activeRef.current);
    if (!tab) return;
    setSaveState("saving");
    try {
      const { mtime } = await api.write(labId, tab.path, tab.value);
      setTabs((ts) => ts.map((t) => (t.path === tab.path ? { ...t, saved: tab.value, mtime } : t)));
      setSaveState("saved");
      setTimeout(() => setSaveState((s) => (s === "saved" ? "" : s)), 1600);
      loadTree();
    } catch {
      setSaveState("error");
    }
  }, [labId, loadTree]);

  const saveRef = useRef(save);
  saveRef.current = save;

  const onMount: OnMount = (editor, monaco) => {
    editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyS, () => saveRef.current());
  };

  async function create(path: string, kind: "file" | "folder") {
    if (kind === "folder") await api.mkdir(labId, path);
    else {
      await api.write(labId, path, "");
      await loadTree();
      await open(path);
    }
    await loadTree();
  }

  async function remove(path: string) {
    await api.remove(labId, path).catch(() => null);
    setTabs((ts) => ts.filter((t) => t.path !== path && !t.path.startsWith(path + "/")));
    if (activeRef.current === path || activeRef.current?.startsWith(path + "/")) setActive(null);
    loadTree();
  }

  const current = tabs.find((t) => t.path === active);

  return (
    <div className="editor-area">
      <FileTree nodes={nodes} active={active} onOpen={open} onCreate={create} onDelete={remove} onRefresh={loadTree} />
      <div className="editor-col">
        <div className="tabs" role="tablist">
          {tabs.map((t) => (
            <div
              key={t.path}
              className={`tab${t.path === active ? " active" : ""}`}
              role="tab"
              aria-selected={t.path === active}
              title={t.path}
              onClick={() => setActive(t.path)}
              onAuxClick={(e) => e.button === 1 && close(t.path)}
            >
              {t.path.split("/").pop()}
              {t.value !== t.saved ? <span className="dirty" title="Not saved" /> : null}
              <span
                className="x"
                role="button"
                aria-label={`Close ${t.path}`}
                onClick={(e) => {
                  e.stopPropagation();
                  close(t.path);
                }}
              >
                <Cross size={12} />
              </span>
            </div>
          ))}
          <span className={`save-state${saveState === "saved" ? " ok" : ""}`}>
            {saveState === "saving" && "Saving…"}
            {saveState === "saved" && <><Check size={13} /> Saved</>}
            {saveState === "error" && "Could not save"}
            {saveState === "" && current && current.value !== current.saved && "Ctrl+S to save"}
          </span>
        </div>
        <div className="editor-host">
          {current ? (
            <Editor
              path={current.path}
              value={current.value}
              language={languageFor(current.path)}
              theme="labs"
              onMount={onMount}
              onChange={(v) => setTabs((ts) => ts.map((t) => (t.path === current.path ? { ...t, value: v ?? "" } : t)))}
              options={{
                fontFamily: '"JetBrains Mono", ui-monospace, Menlo, monospace',
                fontSize: 13.5,
                lineHeight: 21,
                minimap: { enabled: false },
                scrollBeyondLastLine: false,
                renderLineHighlight: "line",
                smoothScrolling: true,
                padding: { top: 12 },
                tabSize: 2,
                automaticLayout: true,
                stickyScroll: { enabled: false },
              }}
            />
          ) : (
            <div className="editor-empty">
              <div>
                <b>No file open</b>
                Pick a file on the left, or make a new one.
                <br />
                Save with <kbd>Ctrl</kbd> + <kbd>S</kbd>.
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
