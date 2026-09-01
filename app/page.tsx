"use client";

import { useEffect, useMemo, useState } from "react";
import { Activity, CalendarDays, ChevronRight, Clock3, ShieldCheck } from "lucide-react";

type Bet = {
  rank: number;
  event_id: string;
  game: string;
  selection: string;
  opponent: string;
  side: "home" | "away";
  kickoff: string;
  sportsbook: string;
  american_odds: number;
  model_probability: number;
  market_probability: number;
  probability_edge: number;
  expected_value: number;
  stake_fraction: number;
  timing_bucket: string;
  book_count: number;
  qualifies: boolean;
  flags: string[];
  gate_reasons: string[];
};

type TimingBucket = {
  label: string;
  window: string;
  signals: number;
  graded: number;
  price_clv: number | null;
  roi: number | null;
};

type Board = {
  generated_at: string;
  slate_date: string;
  run_label: string;
  model_version: string;
  week: number;
  scanned_games: number;
  schedule_matches: number;
  qualifying_count: number;
  alpha_label: string;
  qualified_bets: Bet[];
  watchlist: Bet[];
  timing_status: string;
  timing_buckets: TimingBucket[];
};

const sample: Board = {
  generated_at: "2026-08-31T14:42:41Z",
  slate_date: "2026-09-03",
  run_label: "Daily 10:42 AM ET",
  model_version: "ncaaf-market-residual-v2-alpha75",
  week: 1,
  scanned_games: 77,
  schedule_matches: 77,
  qualifying_count: 4,
  alpha_label: "75% residual · 21% effective FPI",
  qualified_bets: [
    ["Tulane Green Wave", "Duke Blue Devils", 300, 0.275, 0.25, 0.099, 0.025, "draftkings", "2026-09-05T16:00:00Z", "D4"],
    ["Toledo Rockets", "Michigan State Spartans", 340, 0.245, 0.222, 0.079, 0.023, "betrivers", "2026-09-05T23:30:00Z", "D5"],
    ["Colorado Buffaloes", "Georgia Tech Yellow Jackets", 220, 0.336, 0.316, 0.074, 0.02, "draftkings", "2026-09-06T00:00:00Z", "D5"],
    ["Hawaii Rainbow Warriors", "UNLV Rebels", 135, 0.443, 0.423, 0.042, 0.02, "lowvig", "2026-09-06T03:59:00Z", "D5"],
  ].map((row, index) => ({
    rank: index + 1,
    event_id: `sample-${index}`,
    game: `${row[0]} at ${row[1]}`,
    selection: String(row[0]),
    opponent: String(row[1]),
    side: index === 3 ? "home" : "away",
    american_odds: Number(row[2]),
    model_probability: Number(row[3]),
    market_probability: Number(row[4]),
    expected_value: Number(row[5]),
    probability_edge: Number(row[6]),
    sportsbook: String(row[7]),
    kickoff: String(row[8]),
    timing_bucket: String(row[9]),
    stake_fraction: index === 0 ? 0.0033 : index === 1 ? 0.0023 : index === 2 ? 0.0034 : 0.0031,
    book_count: 5,
    qualifies: true,
    flags: [],
    gate_reasons: [],
  })),
  watchlist: [],
  timing_status: "Collecting forward samples — no entry window selected yet.",
  timing_buckets: ["D7", "D6", "D5", "D4", "D3", "D2", "D1", "D0"].map((label, index) => ({
    label,
    window: `${7 - index} days`,
    signals: index < 4 ? index + 2 : 0,
    graded: 0,
    price_clv: null,
    roi: null,
  })),
};

function formatOdds(value: number) {
  return value > 0 ? `+${value}` : String(value);
}

function formatPercent(value: number, digits = 1) {
  return `${value >= 0 ? "+" : ""}${(value * 100).toFixed(digits)}%`;
}

function formatBook(value: string) {
  const books: Record<string, string> = {
    betmgm: "BetMGM", betrivers: "BetRivers", draftkings: "DraftKings",
    fanduel: "FanDuel", caesars: "Caesars", betonlineag: "BetOnline",
    lowvig: "LowVig", bovada: "Bovada",
  };
  return books[value.toLowerCase()] ?? value;
}

function formatDate(value: string) {
  return new Intl.DateTimeFormat("en-US", {
    weekday: "short", month: "short", day: "numeric", hour: "numeric", minute: "2-digit",
    timeZone: "America/New_York",
  }).format(new Date(value));
}

function formatUpdated(value: string) {
  return new Intl.DateTimeFormat("en-US", {
    month: "short", day: "numeric", hour: "numeric", minute: "2-digit",
    timeZone: "America/New_York", timeZoneName: "short",
  }).format(new Date(value));
}

function BetCard({ bet }: { bet: Bet }) {
  return (
    <article className="bet-card">
      <div className="bet-card-topline">
        <span className="rank">{String(bet.rank).padStart(2, "0")}</span>
        <span className="qualified"><ShieldCheck size={13} /> Qualified</span>
      </div>
      <div className="matchup">{bet.game}</div>
      <h3>{bet.selection}</h3>
      <div className="price-lockup"><strong>{formatOdds(bet.american_odds)}</strong><span>{formatBook(bet.sportsbook)}</span></div>
      <dl className="bet-metrics">
        <div><dt>Model</dt><dd>{(bet.model_probability * 100).toFixed(1)}%</dd></div>
        <div><dt>Market</dt><dd>{(bet.market_probability * 100).toFixed(1)}%</dd></div>
        <div><dt>Model EV</dt><dd className="positive">{formatPercent(bet.expected_value)}</dd></div>
      </dl>
      <div className="bet-card-footer"><span><Clock3 size={13} /> {formatDate(bet.kickoff)}</span><span>{bet.timing_bucket}</span></div>
    </article>
  );
}

export default function Home() {
  const [boards, setBoards] = useState<Board[]>([sample]);
  const [active, setActive] = useState(0);
  const [live, setLive] = useState(false);

  useEffect(() => {
    const sources = [
      "https://raw.githubusercontent.com/drhyphy/ncaa-football-daily-board/main/site-data/boards.json",
      "/api/board",
    ];
    (async () => {
      for (const source of sources) {
        try {
          const response = await fetch(source, { cache: "no-store" });
          if (!response.ok) continue;
          const payload = await response.json() as { boards?: Board[] };
          if (payload.boards?.length) {
            setBoards(payload.boards);
            setLive(true);
            return;
          }
        } catch { /* fall through to the next independent source */ }
      }
    })();
  }, []);

  const board = boards[active] ?? boards[0];
  const visibleBets = board.qualified_bets.slice(0, 8);
  const slateLabel = useMemo(() => `Week ${board.week} · ${board.qualifying_count} qualified`, [board]);

  return (
    <main id="top">
      <header className="masthead">
        <a className="brand" href="#top" aria-label="NCAA Football Daily Board home">
          <span className="brand-mark">CF</span>
          <span><strong>College Football</strong><small>Daily moneyline board</small></span>
        </a>
        <nav aria-label="Board navigation"><a href="#board">Board</a><a href="#market-scan">Market scan</a><a href="#timing">Timing</a></nav>
        <div className="model-chip"><span className="pulse" /> {live ? "Cloud board live" : "Preview data"}</div>
      </header>

      <section className="control-strip">
        <div className="week-lockup"><span className="eyebrow">NCAA · FBS + FCS</span><h1>{slateLabel}</h1></div>
        <div className="strip-stat"><span>Model</span><strong>75% regression</strong><small>Market + FPI residual</small></div>
        <div className="strip-stat"><span>Coverage</span><strong>{board.scanned_games} games</strong><small>{board.schedule_matches} schedule matched</small></div>
        <div className="strip-stat update-stat"><span>Latest cloud run</span><strong>{formatUpdated(board.generated_at)}</strong><small>Runs daily, independent of local Mac</small></div>
      </section>

      {boards.length > 1 && (
        <nav className="run-tabs" aria-label="Recent daily boards">
          {boards.map((item, index) => (
            <button className={index === active ? "active" : ""} key={item.generated_at} onClick={() => setActive(index)}>
              <strong>{item.run_label}</strong><span>{item.qualifying_count} qualified</span>
            </button>
          ))}
        </nav>
      )}

      <section className="board-section" id="board">
        <div className="section-heading">
          <div><span className="eyebrow light">Today&apos;s qualified moneylines</span><h2>{visibleBets.length ? "The board" : "No bets cleared every gate"}</h2></div>
          <div className="section-note"><Activity size={17} /><span>Minimum +1.5% probability edge<br />and +4.0% modeled EV</span></div>
        </div>
        {visibleBets.length ? (
          <div className="bet-grid">{visibleBets.map((bet) => <BetCard bet={bet} key={`${bet.event_id}-${bet.side}`} />)}</div>
        ) : (
          <div className="empty-board"><span>00</span><div><h3>Discipline is part of the model.</h3><p>Every listed game was scanned, but none offers enough price-adjusted edge at this snapshot.</p></div></div>
        )}
      </section>

      <section className="market-section" id="market-scan">
        <div className="section-heading paper-heading">
          <div><span className="eyebrow">Full-slate audit</span><h2>Closest calls</h2></div>
          <p>The strongest model disagreements that did not clear every execution gate.</p>
        </div>
        {board.watchlist.length ? (
          <div className="market-table-wrap">
            <table className="market-table">
              <thead><tr><th>Matchup / selection</th><th>Price</th><th>Model</th><th>Market</th><th>Edge</th><th>EV</th><th>Why it missed</th></tr></thead>
              <tbody>{board.watchlist.slice(0, 12).map((bet) => (
                <tr key={`${bet.event_id}-${bet.side}`}>
                  <td><strong>{bet.selection}</strong><span>{bet.game}</span></td>
                  <td><strong>{formatOdds(bet.american_odds)}</strong><span>{formatBook(bet.sportsbook)}</span></td>
                  <td>{(bet.model_probability * 100).toFixed(1)}%</td><td>{(bet.market_probability * 100).toFixed(1)}%</td>
                  <td className="positive">{formatPercent(bet.probability_edge)}</td>
                  <td className={bet.expected_value >= 0 ? "positive" : ""}>{formatPercent(bet.expected_value)}</td>
                  <td>
                    <div className="reason-list">
                      {(bet.gate_reasons?.length ? bet.gate_reasons : bet.flags.map((flag) => flag.replaceAll("_", " "))).map((reason) => (
                        <span className="gate-label" key={reason}>{reason}</span>
                      ))}
                    </div>
                  </td>
                </tr>
              ))}</tbody>
            </table>
          </div>
        ) : <p className="pending-copy">The full market scan will populate with the first live cloud run.</p>}
      </section>

      <section className="timing-section" id="timing">
        <div className="timing-intro">
          <span className="eyebrow light">Daily timing ledger</span><h2>When is the price best?</h2><p>{board.timing_status}</p>
          <div className="timing-rule"><CalendarDays size={18} /><span>A timing window needs at least 50 graded qualified signals before it can lead.</span></div>
        </div>
        <div className="timing-grid">
          {board.timing_buckets.map((bucket) => (
            <div className="timing-cell" key={bucket.label}>
              <div><strong>{bucket.label}</strong><span>{bucket.window}</span></div>
              <dl><div><dt>Signals</dt><dd>{bucket.signals}</dd></div><div><dt>Graded</dt><dd>{bucket.graded}</dd></div><div><dt>Price CLV</dt><dd>{bucket.price_clv == null ? "—" : formatPercent(bucket.price_clv)}</dd></div></dl>
            </div>
          ))}
        </div>
      </section>

      <section className="method-strip">
        <div><span className="eyebrow">Model contract</span><h2>Market first. FPI second. Price decides.</h2></div>
        <p>The leading build begins with the de-vigged multi-book moneyline, then retains 75% of the historically fitted FPI residual. It scans FBS–FBS, FBS–FCS, and FCS–FCS games, and only issues a paper recommendation when schedule, liquidity, dispersion, probability-edge, and EV gates all pass.</p>
        <a href="#top">Back to board <ChevronRight size={15} /></a>
      </section>

      <footer><span>Forward paper research · No automatic wagering</span><span>Prices can move after capture · Best available at listed book</span></footer>
    </main>
  );
}
