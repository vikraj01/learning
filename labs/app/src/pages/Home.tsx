import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api";
import type { LabSummary, Track } from "../types";
import { Check, GridIcon, ListIcon, Logo, RowsIcon, Search } from "../components/Icons";

type Status = "all" | "todo" | "started" | "solved";
type Level = "all" | "Easy" | "Medium";
type View = "gallery" | "list" | "compact";

const VIEW_KEY = "docker-labs:view";
const TOPICS_SHOWN = 10;

// A small colour per track, only for the dots in the sidebar.
const PAINT: Record<string, string> = {
  basics: "#2f5f8a",
  images: "#8c3d2c",
  inside: "#9c7420",
  storage: "#2c6a5c",
  networking: "#4f5f2c",
  settings: "#6a4c7a",
  "image-options": "#7a5a3c",
  compose: "#2c5a7a",
};
const paintOf = (track: string) => PAINT[track] ?? "#4a4f57";

function readView(): View {
  try {
    const v = localStorage.getItem(VIEW_KEY);
    if (v === "gallery" || v === "list" || v === "compact") return v;
  } catch {
    /* storage blocked */
  }
  return "gallery";
}

const statusOf = (lab: LabSummary): Exclude<Status, "all"> => (lab.solved ? "solved" : lab.started ? "started" : "todo");
const STATUS_TEXT = { solved: "Done", started: "In progress", todo: "Not started" } as const;

export default function Home() {
  const [labs, setLabs] = useState<LabSummary[] | null>(null);
  const [tracks, setTracks] = useState<Track[]>([]);
  const [error, setError] = useState(false);

  const [track, setTrack] = useState<string>("all");
  const [status, setStatus] = useState<Status>("all");
  const [level, setLevel] = useState<Level>("all");
  const [tags, setTags] = useState<Set<string>>(new Set());
  const [query, setQuery] = useState("");
  const [allTopics, setAllTopics] = useState(false);
  const [view, setView] = useState<View>(readView);

  useEffect(() => {
    document.title = "Docker Labs";
    Promise.all([api.labs(), api.tracks().catch(() => [] as Track[])])
      .then(([l, t]) => {
        setLabs(l);
        setTracks(t);
      })
      .catch(() => setError(true));
  }, []);

  function chooseView(v: View) {
    setView(v);
    try {
      localStorage.setItem(VIEW_KEY, v);
    } catch {
      /* storage blocked */
    }
  }

  const toggleTag = (t: string) =>
    setTags((prev) => {
      const next = new Set(prev);
      if (next.has(t)) next.delete(t);
      else next.add(t);
      return next;
    });

  const clearFilters = () => {
    setTrack("all");
    setStatus("all");
    setLevel("all");
    setTags(new Set());
    setQuery("");
  };

  const all = labs ?? [];
  const solved = all.filter((l) => l.solved).length;
  const minutesLeft = all.filter((l) => !l.solved).reduce((n, l) => n + l.minutes, 0);
  const upNext = all.find((l) => l.started && !l.solved) ?? all.find((l) => !l.solved) ?? null;
  const trackTitle = (id: string) => tracks.find((t) => t.id === id)?.title ?? "Other";

  const topics = useMemo(() => {
    const count = new Map<string, number>();
    for (const l of all) for (const t of l.topics) count.set(t, (count.get(t) ?? 0) + 1);
    return [...count.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
  }, [all]);

  const shown = useMemo(() => {
    const words = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
    return all.filter((lab) => {
      if (track !== "all" && lab.track !== track) return false;
      if (status !== "all" && statusOf(lab) !== status) return false;
      if (level !== "all" && lab.level !== level) return false;
      if (tags.size && !lab.topics.some((t) => tags.has(t))) return false;
      if (words.length) {
        const text = [lab.title, lab.summary, ...lab.topics].join(" ").toLowerCase();
        if (!words.every((w) => text.includes(w))) return false;
      }
      return true;
    });
  }, [all, track, status, level, tags, query]);

  const filtering = track !== "all" || status !== "all" || level !== "all" || tags.size > 0 || query.trim() !== "";
  const currentTrack = tracks.find((t) => t.id === track);

  const groups = useMemo(() => {
    const ids = [...tracks.map((t) => t.id), ...new Set(shown.map((l) => l.track).filter((id) => !tracks.some((t) => t.id === id)))];
    return ids.map((id) => ({ id, labs: shown.filter((l) => l.track === id) })).filter((g) => g.labs.length);
  }, [shown, tracks]);

  const countBy = (pred: (l: LabSummary) => boolean) => all.filter(pred).length;
  const hours = Math.round(minutesLeft / 6) / 10;

  return (
    <div className="shell">
      {/* ---------------- sidebar ---------------- */}
      <aside className="side">
        <div className="brand">
          <div className="logo"><Logo /></div>
          <span className="brand-name">Docker Labs</span>
        </div>

        <div className="progress">
          <div className="progress-text">
            <b>{solved} of {all.length}</b> labs done
          </div>
          <div className="progress-bar"><i style={{ width: `${all.length ? (solved / all.length) * 100 : 0}%` }} /></div>
          <div className="progress-sub">{minutesLeft ? `About ${hours} hours left` : "Every lab is done"}</div>
        </div>

        <nav className="side-section" aria-label="Tracks">
          <h3>Tracks</h3>
          <button type="button" className={`side-item${track === "all" ? " on" : ""}`} onClick={() => setTrack("all")}>
            <span className="si-name">All labs</span>
            <span className="si-count">{all.length}</span>
          </button>
          {tracks.map((t) => {
            const inT = all.filter((l) => l.track === t.id);
            const done = inT.filter((l) => l.solved).length;
            const complete = inT.length > 0 && done === inT.length;
            return (
              <button key={t.id} type="button" className={`side-item${track === t.id ? " on" : ""}`} onClick={() => setTrack(t.id)}>
                <span className="dot" style={{ background: paintOf(t.id) }} />
                <span className="si-name">{t.title}</span>
                <span className={`si-count${complete ? " done" : ""}`}>{complete ? <Check size={13} /> : `${done}/${inT.length}`}</span>
              </button>
            );
          })}
        </nav>

        <div className="side-section">
          <h3>Status</h3>
          {([
            ["all", "Any", all.length],
            ["todo", "Not started", countBy((l) => statusOf(l) === "todo")],
            ["started", "In progress", countBy((l) => statusOf(l) === "started")],
            ["solved", "Done", solved],
          ] as [Status, string, number][]).map(([id, label, n]) => (
            <button key={id} type="button" className={`side-item${status === id ? " on" : ""}`} onClick={() => setStatus(id)}>
              <span className="si-name">{label}</span>
              <span className="si-count">{n}</span>
            </button>
          ))}
        </div>

        <div className="side-section">
          <h3>Level</h3>
          {(["all", "Easy", "Medium"] as Level[]).map((l) => (
            <button key={l} type="button" className={`side-item${level === l ? " on" : ""}`} onClick={() => setLevel(l)}>
              <span className="si-name">{l === "all" ? "Any" : l}</span>
              <span className="si-count">{l === "all" ? all.length : countBy((x) => x.level === l)}</span>
            </button>
          ))}
        </div>

        <div className="side-section">
          <h3>
            Topics
            {tags.size > 0 && <button type="button" className="text-btn" onClick={() => setTags(new Set())}>Clear</button>}
          </h3>
          <div className="topics">
            {(allTopics ? topics : topics.slice(0, TOPICS_SHOWN)).map(([t, n]) => (
              <button key={t} type="button" className={`topic${tags.has(t) ? " on" : ""}`} onClick={() => toggleTag(t)} aria-pressed={tags.has(t)}>
                {t} <span>{n}</span>
              </button>
            ))}
          </div>
          {topics.length > TOPICS_SHOWN && (
            <button type="button" className="text-btn more" onClick={() => setAllTopics((v) => !v)}>
              {allTopics ? "Show fewer topics" : `Show all ${topics.length} topics`}
            </button>
          )}
        </div>
      </aside>

      {/* ---------------- main ---------------- */}
      <main className="main">
        <header className="main-head">
          <div>
            <h1>{currentTrack ? currentTrack.title : "All labs"}</h1>
            <p>
              {currentTrack
                ? currentTrack.description
                : "Small jobs with real Docker. Type the commands, change the files, then press Check."}
            </p>
          </div>
          {upNext && !filtering && (
            <Link className="resume" to={`/lab/${upNext.id}`}>
              <span className="resume-text">
                <span>{upNext.started ? `Pick up where you stopped: lab ${upNext.number}` : `Next: lab ${upNext.number}`}</span>
                <b>{upNext.title}</b>
              </span>
              <span className="resume-go">{upNext.started ? "Continue" : "Start"}</span>
            </Link>
          )}
        </header>

        <div className="main-tools">
          <label className="search">
            <Search size={15} />
            <input id="lab-search" type="search" placeholder="Search by name or topic" value={query} onChange={(e) => setQuery(e.target.value)} />
          </label>
          <span className="result">
            {filtering ? (
              <>
                {shown.length} of {all.length} labs
                <button className="text-btn" type="button" onClick={clearFilters}>Clear filters</button>
              </>
            ) : (
              <>{all.length} labs</>
            )}
          </span>
          <div className="views" role="tablist" aria-label="View">
            {([
              ["gallery", "Gallery", <GridIcon key="g" />],
              ["list", "List", <ListIcon key="l" />],
              ["compact", "Compact", <RowsIcon key="c" />],
            ] as [View, string, React.ReactNode][]).map(([id, label, icon]) => (
              <button key={id} type="button" role="tab" aria-selected={view === id} className={view === id ? "on" : ""} onClick={() => chooseView(id)}>
                {icon}<span>{label}</span>
              </button>
            ))}
          </div>
        </div>

        {error && <p className="empty">The lab server isn't answering. Start it with <code>make start</code> in the <code>labs</code> folder, then reload.</p>}
        {!labs && !error && <p className="empty">Loading labs…</p>}
        {labs && shown.length === 0 && (
          <p className="empty">
            No labs match these filters. <button className="text-btn" type="button" onClick={clearFilters}>Clear filters</button>
          </p>
        )}

        {view === "gallery" &&
          groups.map((g) => (
            <section key={g.id} className="group">
              {track === "all" && <GroupHead title={trackTitle(g.id)} labs={g.labs} />}
              <div className="gallery">
                {g.labs.map((lab) => (
                  <Link key={lab.id} to={`/lab/${lab.id}`} className={`card ${statusOf(lab)}`}>
                    <span className="card-top">
                      <span className="card-num">Lab {lab.number}</span>
                      <span className={`card-status ${statusOf(lab)}`}>
                        {lab.solved && <Check size={13} />}
                        {lab.solved || lab.started ? STATUS_TEXT[statusOf(lab)] : ""}
                      </span>
                    </span>
                    <span className="card-title">{lab.title}</span>
                    <span className="card-sum">{lab.summary}</span>
                    <span className="card-meta">
                      <span className={`lvl ${lab.level.toLowerCase()}`}>{lab.level}</span>
                      <span>{lab.minutes} min</span>
                      <span>{lab.tasks.length} tasks</span>
                    </span>
                  </Link>
                ))}
              </div>
            </section>
          ))}

        {view === "list" &&
          groups.map((g) => (
            <section key={g.id} className="group">
              {track === "all" && <GroupHead title={trackTitle(g.id)} labs={g.labs} />}
              <div className="list">
                {g.labs.map((lab) => (
                  <Link key={lab.id} to={`/lab/${lab.id}`} className={`row ${statusOf(lab)}`}>
                    <span className="row-num">{lab.number}</span>
                    <span className="row-main">
                      <span className="row-title">{lab.title}</span>
                      <span className="row-sum">{lab.summary}</span>
                    </span>
                    <span className="row-topics">
                      {lab.topics.slice(0, 3).map((t) => <span key={t} className={tags.has(t) ? "on" : ""}>{t}</span>)}
                    </span>
                    <span className={`lvl ${lab.level.toLowerCase()}`}>{lab.level}</span>
                    <span className="row-min">{lab.minutes} min</span>
                    <span className={`row-status ${statusOf(lab)}`}>{STATUS_TEXT[statusOf(lab)]}</span>
                  </Link>
                ))}
              </div>
            </section>
          ))}

        {view === "compact" && shown.length > 0 && (
          <div className="table-wrap">
            <table className="compact">
              <thead>
                <tr>
                  <th className="num">No.</th>
                  <th>Lab</th>
                  <th>Track</th>
                  <th>Level</th>
                  <th className="num">Time</th>
                  <th className="num">Tasks</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {shown.map((lab) => (
                  <tr key={lab.id} className={statusOf(lab)}>
                    <td className="num">{lab.number}</td>
                    <td className="t-title"><Link to={`/lab/${lab.id}`}>{lab.title}</Link></td>
                    <td>{trackTitle(lab.track)}</td>
                    <td><span className={`lvl ${lab.level.toLowerCase()}`}>{lab.level}</span></td>
                    <td className="num">{lab.minutes} min</td>
                    <td className="num">{lab.tasks.length}</td>
                    <td className={`t-status ${statusOf(lab)}`}>{STATUS_TEXT[statusOf(lab)]}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </main>
    </div>
  );
}

function GroupHead({ title, labs }: { title: string; labs: LabSummary[] }) {
  const done = labs.filter((l) => l.solved).length;
  return (
    <div className="group-head">
      <h2>{title}</h2>
      <span>{done} of {labs.length} done</span>
    </div>
  );
}
