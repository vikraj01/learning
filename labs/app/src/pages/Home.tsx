import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api";
import type { LabSummary, Track } from "../types";
import { Check, ChevronRight, Logo, Search } from "../components/Icons";

type Filter = "all" | "todo" | "started" | "solved";
type Level = "all" | "Easy" | "Medium";

const FILTERS: { id: Filter; label: string }[] = [
  { id: "all", label: "All" },
  { id: "todo", label: "To do" },
  { id: "started", label: "In progress" },
  { id: "solved", label: "Solved" },
];

const pad = (n: number) => String(n).padStart(2, "0");

interface Filters {
  status: Filter;
  level: Level;
  tags: Set<string>;
  query: string;
}

function matches(lab: LabSummary, { status: filter, level, tags, query }: Filters) {
  if (level !== "all" && lab.level !== level) return false;
  if (tags.size > 0 && !lab.topics.some((t) => tags.has(t))) return false;
  if (filter === "todo" && (lab.solved || lab.started)) return false;
  if (filter === "started" && (lab.solved || !lab.started)) return false;
  if (filter === "solved" && !lab.solved) return false;
  if (!query) return true;
  const text = [lab.title, lab.summary, ...lab.topics].join(" ").toLowerCase();
  return query.toLowerCase().split(/\s+/).every((word) => text.includes(word));
}

function StatusBadge({ lab }: { lab: LabSummary }) {
  if (lab.solved) return <span className="badge-status solved" title="Solved"><Check size={14} /></span>;
  if (lab.started) return <span className="badge-status started" title="In progress">{pad(lab.number)}</span>;
  return <span className="badge-status" title="Not started">{pad(lab.number)}</span>;
}

function LabRow({ lab, tags, onTag }: { lab: LabSummary; tags: Set<string>; onTag: (t: string) => void }) {
  return (
    <Link className={`lab-row${lab.solved ? " solved" : ""}`} to={`/lab/${lab.id}`}>
      <StatusBadge lab={lab} />
      <div className="lab-main">
        <div className="lab-title">{lab.title}</div>
        <div className="lab-sum">{lab.summary}</div>
        <div className="lab-meta">
          <span className={`chip ${lab.level.toLowerCase()}`}>{lab.level}</span>
          <span className="chip">~{lab.minutes} min</span>
          <span className="chip">{lab.tasks.length} tasks</span>
          {lab.topics.map((t) => (
            <button
              key={t}
              type="button"
              className={`chip topic tag-btn${tags.has(t) ? " on" : ""}`}
              title={tags.has(t) ? `Stop filtering by ${t}` : `Show labs about ${t}`}
              onClick={(e) => {
                e.preventDefault();
                e.stopPropagation();
                onTag(t);
              }}
            >
              {t}
            </button>
          ))}
        </div>
      </div>
      <div className="lab-side">
        {lab.solved ? (
          <span className="status solved">Solved</span>
        ) : lab.started ? (
          <span className="status started">In progress</span>
        ) : null}
        <span className={`btn small-row${!lab.solved && lab.started ? " primary" : ""}`}>
          {lab.solved ? "Open" : lab.started ? "Continue" : "Start"} <ChevronRight />
        </span>
      </div>
    </Link>
  );
}

export default function Home() {
  const [labs, setLabs] = useState<LabSummary[] | null>(null);
  const [tracks, setTracks] = useState<Track[]>([]);
  const [error, setError] = useState(false);
  const [filter, setFilter] = useState<Filter>("all");
  const [query, setQuery] = useState("");
  const [level, setLevel] = useState<Level>("all");
  const [tags, setTags] = useState<Set<string>>(new Set());

  const toggleTag = (t: string) =>
    setTags((prev) => {
      const next = new Set(prev);
      if (next.has(t)) next.delete(t);
      else next.add(t);
      return next;
    });
  const clearFilters = () => {
    setFilter("all");
    setLevel("all");
    setTags(new Set());
    setQuery("");
  };
  const filtering = filter !== "all" || level !== "all" || tags.size > 0 || query.trim() !== "";

  useEffect(() => {
    document.title = "Docker Labs";
    Promise.all([api.labs(), api.tracks().catch(() => [])])
      .then(([l, t]) => {
        setLabs(l);
        setTracks(t);
      })
      .catch(() => setError(true));
  }, []);

  const solved = labs?.filter((l) => l.solved).length ?? 0;
  const total = labs?.length ?? 0;
  const minutesLeft = labs?.filter((l) => !l.solved).reduce((sum, l) => sum + l.minutes, 0) ?? 0;
  const upNext = labs?.find((l) => l.started && !l.solved) ?? labs?.find((l) => !l.solved) ?? null;

  const allTags = useMemo(() => {
    const count = new Map<string, number>();
    for (const l of labs ?? []) for (const t of l.topics) count.set(t, (count.get(t) ?? 0) + 1);
    return [...count.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
  }, [labs]);

  const groups = useMemo(() => {
    if (!labs) return [];
    const known = new Set(tracks.map((t) => t.id));
    const all = [...tracks, ...(labs.some((l) => !known.has(l.track)) ? [{ id: "", title: "More labs", description: "" }] : [])];
    return all.map((track) => {
      const inTrack = labs.filter((l) => (track.id ? l.track === track.id : !known.has(l.track)));
      return {
        track,
        labs: inTrack,
        shown: inTrack.filter((l) => matches(l, { status: filter, level, tags, query: query.trim() })),
        solved: inTrack.filter((l) => l.solved).length,
      };
    });
  }, [labs, tracks, filter, level, tags, query]);

  const shownCount = groups.reduce((n, g) => n + g.shown.length, 0);
  const nothingShown = labs && shownCount === 0;

  return (
    <main className="home">
      <header className="home-top">
        <div className="brand">
          <div className="logo"><Logo /></div>
          <div>
            <div className="brand-name">Docker Labs</div>
            <div className="brand-sub">Learn by doing, one lab at a time</div>
          </div>
        </div>
        {labs && (
          <div className="top-stats">
            <span><b>{solved}</b> of {total} solved</span>
            <span className="dot-sep" />
            <span>{minutesLeft > 0 ? <>about <b>{Math.round(minutesLeft / 6) / 10}</b> hours to go</> : "all done"}</span>
          </div>
        )}
      </header>

      <section className="hero">
        <div className="hero-text">
          <h1>Real tasks. A real terminal. <em>Press Check.</em></h1>
          <p>Each lab gives you a small job to do with Docker. You type the commands, change the files, and the lab tells you what worked and what didn't.</p>
          <div className="steps-inline">
            <span><i>1</i> Read the task</span>
            <ChevronRight size={14} />
            <span><i>2</i> Type commands, edit files</span>
            <ChevronRight size={14} />
            <span><i>3</i> Press Check</span>
          </div>
        </div>

        {upNext ? (
          <Link className="next-card" to={`/lab/${upNext.id}`}>
            <span className="next-eyebrow">{upNext.started ? "Continue where you left off" : solved ? "Up next" : "Start here"}</span>
            <span className="next-num">Lab {pad(upNext.number)}</span>
            <span className="next-title">{upNext.title}</span>
            <span className="next-sum">{upNext.summary}</span>
            <span className="next-foot">
              <span className="chip">~{upNext.minutes} min</span>
              <span className="chip">{upNext.tasks.length} tasks</span>
              <span className="btn primary">{upNext.started ? "Continue" : "Start"} <ChevronRight /></span>
            </span>
          </Link>
        ) : labs ? (
          <div className="next-card done">
            <span className="next-eyebrow">All done</span>
            <span className="next-title">Every lab solved.</span>
            <span className="next-sum">Open any lab again to practise, or press Reset inside it to start it fresh.</span>
          </div>
        ) : (
          <div className="next-card skeleton" />
        )}
      </section>

      {labs && (
        <section className="track-progress" aria-label="Progress by track">
          {groups.map(({ track, labs: inTrack, solved: done }) => (
            <a key={track.id} href={`#track-${track.id}`} className="tp">
              <span className="tp-name">{track.title}</span>
              <span className="tp-bar"><i style={{ width: `${inTrack.length ? (done / inTrack.length) * 100 : 0}%` }} /></span>
              <span className="tp-count">{done}/{inTrack.length}</span>
            </a>
          ))}
        </section>
      )}

      <div className="toolbar">
        <div className="seg" role="tablist" aria-label="Show">
          {FILTERS.map((f) => (
            <button key={f.id} type="button" role="tab" aria-selected={filter === f.id}
              className={filter === f.id ? "on" : ""} onClick={() => setFilter(f.id)}>
              {f.label}
            </button>
          ))}
        </div>
        <label className="search">
          <Search size={15} />
          <input id="lab-search" type="search" placeholder="Search labs: volumes, ports, logs…" value={query} onChange={(e) => setQuery(e.target.value)} />
        </label>
      </div>

      <div className="filters">
        <div className="filter-group">
          <span className="filter-label">Level</span>
          {(["all", "Easy", "Medium"] as Level[]).map((l) => (
            <button key={l} type="button" className={`chip pick${level === l ? " on" : ""}${l !== "all" ? ` ${l.toLowerCase()}-pick` : ""}`} onClick={() => setLevel(l)}>
              {l === "all" ? "Any" : l}
            </button>
          ))}
        </div>
        <div className="filter-group tags">
          <span className="filter-label">Topics</span>
          {allTags.map(([t, n]) => (
            <button key={t} type="button" className={`chip pick tag-btn${tags.has(t) ? " on" : ""}`} onClick={() => toggleTag(t)} aria-pressed={tags.has(t)}>
              {t}<span className="count">{n}</span>
            </button>
          ))}
        </div>
        {labs && (
          <div className="filter-result">
            {filtering ? (
              <>
                Showing <b>{shownCount}</b> of {total} labs
                <button className="link-btn" type="button" onClick={clearFilters}>Clear filters</button>
              </>
            ) : (
              <>All <b>{total}</b> labs, in order. Click a topic to filter.</>
            )}
          </div>
        )}
      </div>

      {error && <div className="labs empty-row">Could not load the labs. Is the lab server running? Start it with <code>make start</code> in <code>labs/</code>.</div>}
      {!labs && !error && <div className="labs empty-row">Loading labs…</div>}
      {nothingShown && (
        <div className="labs empty-row">
          No labs match these filters. <button className="link-btn" type="button" onClick={clearFilters}>Clear filters</button>
        </div>
      )}

      {groups.map(({ track, labs: inTrack, shown, solved: done }, i) =>
        shown.length === 0 ? null : (
          <section key={track.id} className="track" id={`track-${track.id}`}>
            <div className="track-head">
              <span className="track-num">{pad(i + 1)}</span>
              <div>
                <h2>{track.title}</h2>
                {track.description && <p>{track.description}</p>}
              </div>
              <span className={`track-count${done === inTrack.length ? " complete" : ""}`}>
                {done === inTrack.length ? <><Check size={13} /> Complete</> : `${done} / ${inTrack.length} solved`}
              </span>
            </div>
            <div className="labs">
              {shown.map((lab) => <LabRow key={lab.id} lab={lab} tags={tags} onTag={toggleTag} />)}
            </div>
          </section>
        )
      )}
    </main>
  );
}
