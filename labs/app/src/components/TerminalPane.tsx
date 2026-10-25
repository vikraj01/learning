import { useEffect, useRef, useState } from "react";
import { Terminal } from "@xterm/xterm";
import { FitAddon } from "@xterm/addon-fit";

type Status = "connecting" | "on" | "off";

// A real bash on the laptop, started in the lab's folder. "New terminal" starts a fresh one.
export default function TerminalPane({ labId, folder }: { labId: string; folder: string }) {
  const host = useRef<HTMLDivElement>(null);
  const termRef = useRef<Terminal | null>(null);
  const [session, setSession] = useState(0);
  const [status, setStatus] = useState<Status>("connecting");

  useEffect(() => {
    const el = host.current;
    if (!el) return;

    const term = new Terminal({
      fontFamily: '"JetBrains Mono", ui-monospace, Menlo, monospace',
      fontSize: 13.5,
      lineHeight: 1.25,
      cursorBlink: true,
      cursorStyle: "bar",
      scrollback: 5000,
      allowProposedApi: true,
      theme: {
        background: "#121416",
        foreground: "#e4e0d7",
        cursor: "#f2c75c",
        selectionBackground: "#3a4049",
        black: "#2a2e33", brightBlack: "#737069",
        red: "#f2645a", brightRed: "#ff8a80",
        green: "#3fb97a", brightGreen: "#6fdc9f",
        yellow: "#e0a63b", brightYellow: "#f5c46a",
        blue: "#3fa7f5", brightBlue: "#7cc2ff",
        magenta: "#b392f0", brightMagenta: "#d2b8ff",
        cyan: "#4fc7d9", brightCyan: "#82e3f0",
        white: "#d6d2c9", brightWhite: "#f7f4ee",
      },
    });
    const fit = new FitAddon();
    term.loadAddon(fit);
    term.open(el);
    fit.fit();
    termRef.current = term;

    const proto = location.protocol === "https:" ? "wss" : "ws";
    const ws = new WebSocket(
      `${proto}://${location.host}/term?lab=${encodeURIComponent(labId)}&cols=${term.cols}&rows=${term.rows}`
    );
    ws.binaryType = "arraybuffer";
    setStatus("connecting");

    ws.onopen = () => {
      setStatus("on");
      term.focus();
    };
    ws.onmessage = (e) => term.write(typeof e.data === "string" ? e.data : new Uint8Array(e.data));
    ws.onclose = () => {
      setStatus("off");
      term.write("\r\n\x1b[38;5;245m[terminal closed — press “New terminal” to start again]\x1b[0m\r\n");
    };

    const input = term.onData((data) => ws.readyState === WebSocket.OPEN && ws.send(JSON.stringify({ type: "input", data })));
    const resize = term.onResize(({ cols, rows }) =>
      ws.readyState === WebSocket.OPEN && ws.send(JSON.stringify({ type: "resize", cols, rows }))
    );

    const observer = new ResizeObserver(() => {
      try {
        fit.fit();
      } catch {
        /* hidden while resizing */
      }
    });
    observer.observe(el);

    return () => {
      observer.disconnect();
      input.dispose();
      resize.dispose();
      ws.onclose = null;
      ws.close();
      term.dispose();
      termRef.current = null;
    };
  }, [labId, session]);

  return (
    <div className="term">
      <div className="pane-head">
        <span className={`conn ${status === "on" ? "on" : status === "off" ? "off" : ""}`} />
        <span className="label" style={{ flex: "none" }}>Terminal</span>
        <span className="path" title={folder}>{folder}</span>
        <button className="btn ghost small" type="button" onClick={() => termRef.current?.clear()}>Clear</button>
        <button className="btn ghost small" type="button" onClick={() => setSession((s) => s + 1)}>New terminal</button>
      </div>
      <div className="term-host" ref={host} />
    </div>
  );
}
