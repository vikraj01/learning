import { useCallback, useEffect, useRef, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api";
import type { CheckResult, LabDetail } from "../types";
import TaskPanel from "../components/TaskPanel";
import Workspace from "../components/Workspace";
import TerminalPane from "../components/TerminalPane";
import Splitter from "../components/Splitter";
import { ChevronLeft } from "../components/Icons";

type Phase = "loading" | "preparing" | "ready" | "failed";

const LEFT_MIN = 300;
const LEFT_MAX = 640;

export default function LabPage() {
  const { id = "" } = useParams();
  const [lab, setLab] = useState<LabDetail | null>(null);
  const [notFound, setNotFound] = useState(false);
  const [phase, setPhase] = useState<Phase>("loading");
  const [prepTitle, setPrepTitle] = useState("Getting your lab ready…");
  const [prepLog, setPrepLog] = useState("");
  const [results, setResults] = useState<Record<string, CheckResult>>({});
  const [solved, setSolved] = useState(false);
  const [checking, setChecking] = useState(false);
  const [session, setSession] = useState(0); // bumps after a reset: fresh terminal and editor
  const [left, setLeft] = useState(400);
  const [top, setTop] = useState(56); // % of the right side used by the editor
  const rightRef = useRef<HTMLElement>(null);

  // Load the lab, and set it up the first time it's opened.
  useEffect(() => {
    let cancelled = false;
    setPhase("loading");
    setResults({});
    api
      .lab(id)
      .then(async (data) => {
        if (cancelled) return;
        setLab(data);
        setSolved(data.solved);
        document.title = `${data.title} · Docker Labs`;
        if (data.ready) return setPhase("ready");
        setPrepTitle("Getting your lab ready…");
        setPhase("preparing");
        const r = await api.start(id);
        if (cancelled) return;
        setPrepLog(r.output);
        setPhase(r.ok ? "ready" : "failed");
      })
      .catch(() => !cancelled && setNotFound(true));
    return () => {
      cancelled = true;
    };
  }, [id]);

  const runCheck = useCallback(async () => {
    if (checking || phase !== "ready") return;
    setChecking(true);
    try {
      const r = await api.check(id);
      setResults(r.results);
      setSolved(r.solved);
    } finally {
      setChecking(false);
    }
  }, [checking, phase, id]);

  async function reset() {
    setPrepTitle("Starting the lab over…");
    setPrepLog("");
    setPhase("preparing");
    const r = await api.reset(id).catch((e: Error) => ({ ok: false, output: e.message }));
    setResults({});
    setSolved(false);
    setPrepLog(r.output);
    setSession((s) => s + 1);
    setPhase(r.ok ? "ready" : "failed");
  }

  // Ctrl+Enter checks from anywhere, even from the terminal or the editor.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
        e.preventDefault();
        runCheck();
      }
    };
    window.addEventListener("keydown", onKey, true);
    return () => window.removeEventListener("keydown", onKey, true);
  }, [runCheck]);

  if (notFound)
    return (
      <div className="page-error">
        <b>There's no lab called “{id}”.</b>
        <Link to="/">Back to all labs</Link>
      </div>
    );

  return (
    <div className="wb">
      <header className="topbar">
        <Link className="back" to="/"><ChevronLeft /> All labs</Link>
        <span className="sep" />
        <div className="crumb">
          {lab && <><small>LAB {String(lab.number).padStart(2, "0")}</small>{lab.title}</>}
        </div>
        <span className="spacer" />
        {lab && (
          <div className="progress-dots" aria-label="Task results">
            <span className="label">{lab.tasks.filter((t) => results[t.id]?.pass).length}/{lab.tasks.length}</span>
            {lab.tasks.map((t) => (
              <i key={t.id} className={results[t.id] ? (results[t.id].pass ? "pass" : "fail") : ""} title={t.title} />
            ))}
          </div>
        )}
      </header>

      <div className="body" style={{ "--left": `${left}px` } as React.CSSProperties}>
        {lab ? (
          <TaskPanel lab={lab} results={results} solved={solved} checking={checking} onCheck={runCheck} onReset={reset} />
        ) : (
          <aside className="left" />
        )}

        <Splitter direction="vertical" label="Resize the task panel" onMove={(x) => setLeft(Math.min(LEFT_MAX, Math.max(LEFT_MIN, x)))} />

        <section className="right" ref={rightRef} style={{ "--top": `${top}%` } as React.CSSProperties}>
          {phase === "ready" && lab ? (
            <>
              <Workspace key={`ws-${session}`} labId={lab.id} />
              <Splitter
                direction="horizontal"
                label="Resize the terminal"
                onMove={(y) => {
                  const box = rightRef.current?.getBoundingClientRect();
                  if (box) setTop(Math.min(80, Math.max(18, ((y - box.top) / box.height) * 100)));
                }}
              />
              <TerminalPane key={`t-${session}`} labId={lab.id} folder={`labs/workspace/${lab.id}`} />
            </>
          ) : null}
        </section>
      </div>

      {(phase === "loading" || phase === "preparing" || phase === "failed") && (
        <div className="overlay" role="status" aria-live="polite">
          <div className="overlay-card">
            {phase === "failed" ? (
              <>
                <b>The lab could not be set up</b>
                <p>Is Docker running? Try <code>docker ps</code> in a terminal, then press Try again.</p>
                {prepLog && <pre>{prepLog.trim().split("\n").slice(-30).join("\n")}</pre>}
                <div className="row">
                  <button className="btn primary" type="button" onClick={reset}>Try again</button>
                  <Link className="btn" to="/">All labs</Link>
                </div>
              </>
            ) : (
              <>
                <div className="spinner" />
                <b>{phase === "loading" ? "Opening the lab…" : prepTitle}</b>
                {phase === "preparing" && <p>The first time can take a minute: Docker may need to download or build things.</p>}
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
