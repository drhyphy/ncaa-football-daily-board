import { env } from "cloudflare:workers";

export const dynamic = "force-dynamic";

const headers = {
  "content-type": "application/json; charset=utf-8",
  "cache-control": "no-store, max-age=0",
};

async function ensureSchema() {
  await env.DB.batch([
    env.DB.prepare(`CREATE TABLE IF NOT EXISTS board_runs (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      generated_at TEXT NOT NULL UNIQUE,
      slate_date TEXT NOT NULL,
      run_label TEXT NOT NULL,
      model_version TEXT NOT NULL,
      qualifying_count INTEGER NOT NULL DEFAULT 0,
      payload_json TEXT NOT NULL,
      created_at TEXT NOT NULL
    )`),
    env.DB.prepare("CREATE INDEX IF NOT EXISTS board_runs_generated_idx ON board_runs(generated_at DESC)"),
  ]);
}

export async function GET() {
  await ensureSchema();
  const result = await env.DB.prepare(
    "SELECT payload_json FROM board_runs ORDER BY generated_at DESC LIMIT 14",
  ).all<{ payload_json: string }>();
  const boards = result.results.flatMap((row) => {
    try { return [JSON.parse(row.payload_json)]; } catch { return []; }
  });
  return new Response(JSON.stringify({ boards }), { headers });
}

export async function POST(request: Request) {
  await ensureSchema();
  if (!env.INGEST_TOKEN || request.headers.get("x-ingest-token") !== env.INGEST_TOKEN) {
    return new Response(JSON.stringify({ error: "unauthorized" }), { status: 401, headers });
  }
  const length = Number(request.headers.get("content-length") ?? 0);
  if (length > 250_000) {
    return new Response(JSON.stringify({ error: "payload too large" }), { status: 413, headers });
  }
  let payload: Record<string, unknown>;
  try { payload = await request.json() as Record<string, unknown>; }
  catch { return new Response(JSON.stringify({ error: "invalid JSON" }), { status: 400, headers }); }

  if (
    typeof payload.generated_at !== "string" ||
    typeof payload.slate_date !== "string" ||
    typeof payload.run_label !== "string" ||
    !Array.isArray(payload.qualified_bets) ||
    !Array.isArray(payload.watchlist)
  ) {
    return new Response(JSON.stringify({ error: "invalid board payload" }), { status: 422, headers });
  }

  await env.DB.prepare(`INSERT INTO board_runs
    (generated_at, slate_date, run_label, model_version, qualifying_count, payload_json, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(generated_at) DO UPDATE SET payload_json = excluded.payload_json`)
    .bind(
      payload.generated_at,
      payload.slate_date,
      payload.run_label,
      String(payload.model_version ?? "ncaaf-market-residual-v2-alpha75"),
      Number(payload.qualifying_count ?? 0),
      JSON.stringify(payload),
      new Date().toISOString(),
    ).run();

  return new Response(JSON.stringify({ ok: true }), { status: 201, headers });
}
