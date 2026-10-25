import { useState } from "react";
import { Link } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { CheckResult, LabDetail } from "../types";
import InlineCode from "./InlineCode";
import { Bulb, Check, ChevronRight, Cross, Reset } from "./Icons";

interface Props {
  lab: LabDetail;
  results: Record<string, CheckResult>;
  solved: boolean;
  checking: boolean;
  onCheck: () => void;
  onReset: () => void;
}

export default function TaskPanel({ lab, results, solved, checking, onCheck, onReset }: Props) {
  const [openHints, setOpenHints] = useState<Set<string>>(new Set());
  const [confirmReset, setConfirmReset] = useState(false);
  const passed = lab.tasks.filter((t) => results[t.id]?.pass).length;

  const toggleHint = (id: string) =>
    setOpenHints((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });

  return (
    <aside className="left">
      <div className="left-scroll">
        <div className="eyebrow">
          <span className={`chip ${lab.level.toLowerCase()}`}>{lab.level}</span>
          <span className="chip">~{lab.minutes} min</span>
          {lab.topics.map((t) => <span key={t} className="chip">{t}</span>)}
          {solved && <span className="chip solved"><Check size={12} /> Solved</span>}
        </div>
        <h1>{lab.title}</h1>
        <div className="md">
          <ReactMarkdown remarkPlugins={[remarkGfm]}>{lab.task}</ReactMarkdown>
        </div>

        <div className="tasks-title">
          <h2>Your tasks</h2>
          <span>{passed} / {lab.tasks.length}</span>
        </div>
        <ol className="tasks">
          {lab.tasks.map((task, i) => {
            const r = results[task.id];
            const state = r ? (r.pass ? "pass" : "fail") : "";
            return (
              <li key={task.id} className={`task ${state}`}>
                <div className="task-row">
                  <span className="mark">{r ? (r.pass ? <Check size={12} /> : <Cross size={11} />) : i + 1}</span>
                  <div>
                    <div className="task-name"><InlineCode text={task.title} /></div>
                    {r?.message && <div className="task-msg"><InlineCode text={r.message} /></div>}
                    {!r?.pass && (
                      <button className="hint-btn" type="button" onClick={() => toggleHint(task.id)} aria-expanded={openHints.has(task.id)}>
                        <Bulb size={14} /> {openHints.has(task.id) ? "Hide hint" : "Show hint"}
                      </button>
                    )}
                    {!r?.pass && openHints.has(task.id) && <div className="hint"><InlineCode text={task.hint} /></div>}
                  </div>
                </div>
              </li>
            );
          })}
        </ol>
      </div>

      <div className="left-foot">
        {solved && (
          <div className="banner win" role="status">
            <span className="badge"><Check size={18} /></span>
            <div>
              <b>Lab solved!</b>
              <span>{lab.next ? "Every task passed. Ready for the next one?" : "Every task passed. That was the last lab, for now."}</span>
            </div>
          </div>
        )}
        {confirmReset && (
          <div className="confirm">
            <div><b>Start this lab over?</b><br />Your file changes and this lab's containers are removed, and everything goes back to the start.</div>
            <div className="row">
              <button className="btn danger" type="button" onClick={() => { setConfirmReset(false); onReset(); }}>Yes, start over</button>
              <button className="btn" type="button" onClick={() => setConfirmReset(false)}>Cancel</button>
            </div>
          </div>
        )}
        <div className="row">
          {solved && lab.next ? (
            <Link className="btn success grow" to={`/lab/${lab.next.id}`}>Next lab: {lab.next.title} <ChevronRight /></Link>
          ) : (
            <button className="btn primary grow" type="button" onClick={onCheck} disabled={checking}>
              {checking ? <span className="spinner" /> : <Check />}
              {checking ? "Checking…" : "Check my work"}
            </button>
          )}
          {solved && lab.next && (
            <button className="btn" type="button" onClick={onCheck} disabled={checking} title="Check again">
              {checking ? <span className="spinner" /> : <Check />}
            </button>
          )}
          <button className="btn" type="button" onClick={() => setConfirmReset(true)} title="Start this lab over">
            <Reset /> Reset
          </button>
        </div>
        <div className="kbd-note">Tip: <kbd>Ctrl</kbd> + <kbd>Enter</kbd> checks your work from anywhere.</div>
      </div>
    </aside>
  );
}
