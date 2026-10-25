import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api";
import type { LabSummary } from "../types";
import { CheckCircle, ChevronRight, Logo } from "../components/Icons";

const RING = 97.4; // circumference of the progress ring (r = 15.5)

export default function Home() {
  const [labs, setLabs] = useState<LabSummary[] | null>(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    document.title = "Docker Labs";
    api.labs().then(setLabs).catch(() => setError(true));
  }, []);

  const solved = labs?.filter((l) => l.solved).length ?? 0;
  const total = labs?.length ?? 0;

  return (
    <main className="home">
      <div className="brand">
        <div className="logo"><Logo /></div>
        <div>
          <div className="brand-name">Docker Labs</div>
          <div className="brand-sub">Learn by doing, one lab at a time</div>
        </div>
      </div>

      <section className="hero">
        <div>
          <h1>Real tasks. A real terminal. <em>Press Check.</em></h1>
          <p>Each lab gives you a small job to do with Docker. You type the commands, change the files, and the lab tells you what worked and what didn't.</p>
        </div>
        <div className="ring" aria-label={`${solved} of ${total} labs solved`}>
          <svg viewBox="0 0 36 36" aria-hidden="true">
            <circle className="track" cx="18" cy="18" r="15.5" fill="none" strokeWidth="3.5" />
            <circle className="fill" cx="18" cy="18" r="15.5" fill="none" strokeWidth="3.5" strokeLinecap="round"
              strokeDasharray={RING} strokeDashoffset={total ? RING - (RING * solved) / total : RING} />
          </svg>
          <div><b>{solved} / {total}</b><small>labs solved</small></div>
        </div>
      </section>

      <section className="how">
        <div><span className="n">1</span><div><b>Read the task</b><span>What to make, in plain words. Hints if you get stuck.</span></div></div>
        <div><span className="n">2</span><div><b>Do it</b><span>Type commands in the terminal, write files in the editor.</span></div></div>
        <div><span className="n">3</span><div><b>Press Check</b><span>Every step turns green or red, and tells you why.</span></div></div>
      </section>

      <div className="list-head">
        <h2>Labs</h2>
        <span>Do them in order</span>
      </div>
      <div className="labs">
        {error && <div className="empty-row">Could not load the labs. Is the lab server running? Start it with <code>make labs</code>.</div>}
        {!labs && !error && <div className="empty-row">Loading labs…</div>}
        {labs?.map((lab) => (
          <Link key={lab.id} className={`lab-row${lab.solved ? " solved" : ""}`} to={`/lab/${lab.id}`}>
            <span className="lab-num">{String(lab.number).padStart(2, "0")}</span>
            <div>
              <div className="lab-title">{lab.title}</div>
              <div className="lab-sum">{lab.summary}</div>
              <div className="lab-meta">
                <span className={`chip ${lab.level.toLowerCase()}`}>{lab.level}</span>
                <span className="chip">~{lab.minutes} min</span>
                <span className="chip">{lab.tasks.length} tasks</span>
                {lab.topics.map((t) => <span key={t} className="chip">{t}</span>)}
              </div>
            </div>
            <div className="lab-side">
              {lab.solved ? (
                <span className="status solved"><CheckCircle /> Solved</span>
              ) : lab.started ? (
                <span className="status started">In progress</span>
              ) : (
                <span className="status">Not started</span>
              )}
              <span className={`btn${lab.solved ? "" : " primary"}`}>
                {lab.solved ? "Open again" : lab.started ? "Continue" : "Start"} <ChevronRight />
              </span>
            </div>
          </Link>
        ))}
      </div>
    </main>
  );
}
