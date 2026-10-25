// Monaco (the editor inside VS Code), bundled locally so the labs work offline.

import * as monaco from "monaco-editor";
import { loader } from "@monaco-editor/react";
import EditorWorker from "monaco-editor/esm/vs/editor/editor.worker?worker";
import JsonWorker from "monaco-editor/esm/vs/language/json/json.worker?worker";
import CssWorker from "monaco-editor/esm/vs/language/css/css.worker?worker";
import HtmlWorker from "monaco-editor/esm/vs/language/html/html.worker?worker";
import TsWorker from "monaco-editor/esm/vs/language/typescript/ts.worker?worker";

self.MonacoEnvironment = {
  getWorker(_id: string, label: string) {
    if (label === "json") return new JsonWorker();
    if (label === "css" || label === "scss" || label === "less") return new CssWorker();
    if (label === "html" || label === "handlebars" || label === "razor") return new HtmlWorker();
    if (label === "typescript" || label === "javascript") return new TsWorker();
    return new EditorWorker();
  },
};

// Plain Node files use require() and process; don't underline them as errors.
monaco.languages.typescript.javascriptDefaults.setDiagnosticsOptions({
  noSemanticValidation: true,
  noSyntaxValidation: false,
});

monaco.editor.defineTheme("labs", {
  base: "vs-dark",
  inherit: true,
  rules: [],
  colors: {
    "editor.background": "#17191c",
    "editorGutter.background": "#17191c",
    "editor.lineHighlightBackground": "#1e2124",
    "editor.lineHighlightBorder": "#00000000",
    "editorLineNumber.foreground": "#4c5157",
    "editorLineNumber.activeForeground": "#a29e94",
    "editor.selectionBackground": "#3a4049",
    "editorIndentGuide.background1": "#2a2e33",
    "editorCursor.foreground": "#f2c75c",
    "scrollbarSlider.background": "#3a3f4666",
  },
});

loader.config({ monaco });

export function languageFor(path: string): string {
  const name = path.split("/").pop() ?? "";
  if (/^Dockerfile/i.test(name) || name.endsWith(".dockerfile")) return "dockerfile";
  const ext = name.includes(".") ? name.split(".").pop()!.toLowerCase() : "";
  const map: Record<string, string> = {
    js: "javascript", mjs: "javascript", cjs: "javascript", ts: "typescript", json: "json",
    html: "html", css: "css", md: "markdown", py: "python", sh: "shell", bash: "shell",
    yml: "yaml", yaml: "yaml", sql: "sql", txt: "plaintext", conf: "ini", env: "ini",
  };
  return map[ext] ?? "plaintext";
}
