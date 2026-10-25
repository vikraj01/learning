import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api";
import type { LabSummary, Track } from "../types";
import { Check, ChevronRight, GridIcon, ListIcon, Logo, RowsIcon, Search } from "../components/Icons";

type Status = "all" | "todo" | "started" | "solved";
type Level = "all" | "Easy" | "Medium";
type View = "gallery" | "list" | "compact";

const VIEW_KEY = "docker-labs:view";
const TOPICS_SHOWN = 10;
const pad = (n: number) => String(n).padStart(2, "0");

// Each track gets its own colour, used for the stripe on cards and the dots in the sidebar.
const TRACK_HUES: Record<string, string> = {
  basics: "#3fa7f5",
  images: "#a487f5",
  inside: "#e0a63b",
  storage: "#36c2b4",
  networking: "#5fcf7f",
};
const hueOf = (track: string) => TRACK_HUES[track] ?? "#8796a8";

function readView(): View {
  try {
    const v = localStorage.getItem(VIEW_KEY);
    if (v === "gallery" || v === "list" || v === "compact") return v;
  } catch {
    /* storage blocked */
  }
  return "gallery";
}

function statusOf(lab: LabSummary): Exclude<Status, "all"> {
  return lab.solved ? "solved" : lab.started ? "started" : "todo";
}

function StatusMark({ lab }: { lab: LabSummary }) {
  const s = statusOf(lab);
  if (s === "solved") return <span className="mark-dot solved" title="Solved"><Check size={12} /></span>;
  if (s === "started") return <span className="mark-dot started" title="In progress" />;
  return <span className="mark-dot" title="Not started" />;
}

const STATUS_TEXT = { solved: "Solved", started: "In progress", todo: "Not started" } as const;

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

  // Gallery and list are grouped by track; compact is one table.
  const groups = useMemo(() => {
    const order = [...tracks.map((t) => t.id), ...new Set(shown.map((l) => l.track).filter((id) => !tracks.some((t) => t.id === id)))];
    return order.map((id) => ({ id, labs: shown.filter((l) => l.track === id) })).filter((g) => g.labs.length);
  }, [shown, tracks]);

  const countBy = (pred: (l: LabSummary) => boolean) => all.filter(pred).length;

  return (
    <div className="shell">
      {/* ---------------- sidebar ---------------- */}
      <aside className="side">
        <div className="brand">
          <div className="logo"><Logo /></div>
          <div>
            <div className="brand-name">Docker Labs</div>
            <div className="brand-sub">Learn by doing</div>
          </div>
        </div>

        <div className="side-progress">
          <div className="sp-top">
            <span><b>{solved}</b> / {all.length} solved</span>
            <span>{minutesLeft ? `~${Math.round(minutesLeft / 6) / 10} h left` : "all done"}</span>
          </div>
          <div className="sp-bar">
            {tracks.map((t) => {
              const inT = all.filter((l) => l.track === t.id);
              const done = inT.filter((l) => l.solved).length;
              return (
                <span key={t.id} style={{ flex: inT.length || 1 }} title={`${t.title}: ${done}/${inT.length}`}>
                  <i style={{ width: `${inT.length ? (done / inT.length) * 100 : 0}%`, background: hueOf(t.id) }} />
                </span>
              );
            })}
          </div>
        </div>

        <nav className="side-section">
          <div className="side-label">Tracks</div>
          <button type="button" className={`side-item${track === "all" ? " on" : ""}`} onClick={() => setTrack("all")}>
            <span className="swatch all" />
            <span className="si-name">All labs</span>
            <span className="si-count">{all.length}</span>
          </button>
          {tracks.map((t) => {
            const inT = all.filter((l) => l.track === t.id);
            const done = inT.filter((l) => l.solved).length;
            return (
              <button key={t.id} type="button" className={`side-item${track === t.id ? " on" : ""}`} onClick={() => setTrack(t.id)}>
                <span className="swatch" style={{ background: hueOf(t.id) }} />
                <span className="si-name">{t.title}</span>
                <span className={`si-count${done === inT.length && inT.length ? " done" : ""}`}>
                  {done === inT.length && inT.length ? <Check size={12} /> : `${done}/${inT.length}`}
                </span>
              </button>
            );
          })}
        </nav>

        <div className="side-section">
          <div className="side-label">Status</div>
          {([
            ["all", "Any status", all.length],
            ["todo", "Not started", countBy((l) => statusOf(l) === "todo")],
            ["started", "In progress", countBy((l) => statusOf(l) === "started")],
            ["solved", "Solved", solved],
          ] as [Status, string, number][]).map(([id, label, n]) => (
            <button key={id} type="button" className={`side-item${status === id ? " on" : ""}`} onClick={() => setStatus(id)}>
              <span className={`state-dot ${id}`} />
              <span className="si-name">{label}</span>
              <span className="si-count">{n}</span>
            </button>
          ))}
        </div>

        <div className="side-section">
          <div className="side-label">Level</div>
          <div className="seg small">
            {(["all", "Easy", "Medium"] as Level[]).map((l) => (
              <button key={l} type="button" className={level === l ? "on" : ""} onClick={() => setLevel(l)}>
                {l === "all" ? "Any" : l}
              </button>
            ))}
          </div>
        </div>

        <div className="side-section">
          <div className="side-label">
            Topics
            {tags.size > 0 && <button type="button" className="side-clear" onClick={() => setTags(new Set())}>clear</button>}
          </div>
          <div className="topic-cloud">
            {(allTopics ? topics : topics.slice(0, TOPICS_SHOWN)).map(([t, n]) => (
              <button key={t} type="button" className={`topic${tags.has(t) ? " on" : ""}`} onClick={() => toggleTag(t)} aria-pressed={tags.has(t)}>
                {t}<span>{n}</span>
              </button>
            ))}
          </div>
          {topics.length > TOPICS_SHOWN && (
            <button type="button" className="side-more" onClick={() => setAllTopics((v) => !v)}>
              {allTopics ? "Show fewer" : `Show all ${topics.length}`}
            </button>
          )}
        </div>
      </aside>

      {/* ---------------- main ---------------- */}
      <main className="main">
        {upNext && !filtering && (
          <Link className="resume" to={`/lab/${upNext.id}`}>
            <span className="resume-stripe" style={{ background: hueOf(upNext.track) }} />
            <span className="resume-label">{upNext.started ? "Continue" : solved ? "Up next" : "Start here"}</span>
            <span className="resume-num">{pad(upNext.number)}</span>
            <span className="resume-title">{upNext.title}</span>
            <span className="resume-meta">{trackTitle(upNext.track)} · ~{upNext.minutes} min</span>
            <span className="resume-go">{upNext.started ? "Continue" : "Start"} <ChevronRight /></span>
          </Link>
        )}

        <div className="main-head">
          <div>
            <h1>{currentTrack ? currentTrack.title : "All labs"}</h1>
            <p>
              {currentTrack
                ? currentTrack.description
                : "Each lab is a small job: you type the commands, change the files, and press Check."}
            </p>
          </div>
        </div>

        <div className="main-tools">
          <label className="search">
            <Search size={15} />
            <input id="lab-search" type="search" placeholder="Search by name or topic" value={query} onChange={(e) => setQuery(e.target.value)} />
          </label>
          <span className="result">
            {filtering ? (
              <>
                <b>{shown.length}</b> of {all.length}
                <button className="link-btn" type="button" onClick={clearFilters}>Clear filters</button>
              </>
            ) : (
              <><b>{all.length}</b> labs</>
            )}
          </span>
          <div className="seg views" role="tablist" aria-label="View">
            {([
              ["gallery", "Gallery", <GridIcon key="g" />],
              ["list", "List", <ListIcon key="l" />],
              ["compact", "Compact", <RowsIcon key="c" />],
            ] as [View, string, React.ReactNode][]).map(([id, label, icon]) => (
              <button key={id} type="button" role="tab" aria-selected={view === id} className={view === id ? "on" : ""} onClick={() => chooseView(id)} title={label}>
                {icon}<span>{label}</span>
              </button>
            ))}
          </div>
        </div>

        {error && <div className="empty">Could not load the labs. Is the lab server running? Run <code>make start</code> in <code>labs/</code>.</div>}
        {!labs && !error && <div className="empty">Loading labs…</div>}
        {labs && shown.length === 0 && (
          <div className="empty">
            No labs match. <button className="link-btn" type="button" onClick={clearFilters}>Clear filters</button>
          </div>
        )}

        {/* gallery */}
        {view === "gallery" &&
          groups.map((g) => (
            <section key={g.id} className="group">
              {track === "all" && <GroupHead id={g.id} title={trackTitle(g.id)} labs={g.labs} />}
              <div className="gallery">
                {g.labs.map((lab) => (
                  <Link key={lab.id} to={`/lab/${lab.id}`} className={`card ${statusOf(lab)}`} style={{ "--hue": hueOf(lab.track) } as React.CSSProperties}>
                    <div className="card-top">
                      <span className="card-num">{pad(lab.number)}</span>
                      <span className="card-track">{trackTitle(lab.track)}</span>
                      <StatusMark lab={lab} />
                    </div>
                    <div className="card-title">{lab.title}</div>
                    <div className="card-sum">{lab.summary}</div>
                    <div className="card-foot">
                      <span className={`lvl ${lab.level.toLowerCase()}`}>{lab.level}</span>
                      <span className="meta">{lab.minutes} min</span>
                      <span className="meta">{lab.tasks.length} tasks</span>
                      <span className="card-status">{STATUS_TEXT[statusOf(lab)]}</span>
                    </div>
                  </Link>
                ))}
              </div>
            </section>
          ))}

        {/* list */}
        {view === "list" &&
          groups.map((g) => (
            <section key={g.id} className="group">
              {track === "all" && <GroupHead id={g.id} title={trackTitle(g.id)} labs={g.labs} />}
              <div className="list">
                {g.labs.map((lab) => (
                  <Link key={lab.id} to={`/lab/${lab.id}`} className={`row ${statusOf(lab)}`}>
                    <StatusMark lab={lab} />
                    <span className="row-num">{pad(lab.number)}</span>
                    <span className="row-main">
                      <span className="row-title">{lab.title}</span>
                      <span className="row-sum">{lab.summary}</span>
                    </span>
                    <span className="row-topics">
                      {lab.topics.slice(0, 3).map((t) => (
                        <span key={t} className={`topic mini${tags.has(t) ? " on" : ""}`}>{t}</span>
                      ))}
                    </span>
                    <span className={`lvl ${lab.level.toLowerCase()}`}>{lab.level}</span>
                    <span className="meta w">{lab.minutes} min</span>
                    <ChevronRight />
                  </Link>
                ))}
              </div>
            </section>
          ))}

        {/* compact */}
        {view === "compact" && shown.length > 0 && (
          <div className="table-wrap">
            <table className="compact">
              <thead>
                <tr>
                  <th aria-label="Status" />
                  <th>#</th>
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
                    <td><StatusMark lab={lab} /></td>
                    <td className="mono">{pad(lab.number)}</td>
                    <td className="t-title"><Link to={`/lab/${lab.id}`}>{lab.title}</Link></td>
                    <td><span className="t-track"><span className="swatch" style={{ background: hueOf(lab.track) }} />{trackTitle(lab.track)}</span></td>
                    <td><span className={`lvl ${lab.level.toLowerCase()}`}>{lab.level}</span></td>
                    <td className="num">{lab.minutes} min</td>
                    <td className="num">{lab.tasks.length}</td>
                    <td className="t-status">{STATUS_TEXT[statusOf(lab)]}</td>
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

function GroupHead({ id, title, labs }: { id: string; title: string; labs: LabSummary[] }) {
  const done = labs.filter((l) => l.solved).length;
  return (
    <div className="group-head">
      <span className="swatch" style={{ background: hueOf(id) }} />
      <h2>{title}</h2>
      <span className="group-count">{done}/{labs.length}</span>
    </div>
  );
}
