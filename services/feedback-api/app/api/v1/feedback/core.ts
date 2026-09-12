type Reaction = "like" | "dislike" | "clear";

type FeedbackRequest = {
  event_id?: unknown;
  report_id?: unknown;
  content_key?: unknown;
  reaction?: unknown;
  visitor_id?: unknown;
  manifest_id?: unknown;
};

type ManifestItem = {
  id: string;
  content_key: string;
  surface: "selected" | "more";
  title: string;
  url: string;
  score: number;
  source_type?: string | null;
  profile?: string | null;
  tags: string[];
};

type ReportManifest = {
  schema_version: number;
  report_id: string;
  manifest_id: string;
  items: ManifestItem[];
};

type ExistingEvent = {
  manifest_id: string;
  report_id: string;
  content_key: string;
  voter_hash: string;
  reaction: string;
};

type DatabaseStatement = {
  bind: (...values: unknown[]) => DatabaseStatement;
  first: <T>() => Promise<T | null>;
  run: () => Promise<unknown>;
};

export type RuntimeEnv = {
  DB: { prepare: (query: string) => DatabaseStatement };
  VOTER_HMAC_SECRET?: string;
  ALLOWED_ORIGIN?: string;
  REPORT_DATA_ORIGIN?: string;
};

const REPORT_ID = /^\d{4}-\d{2}-\d{2}-(morning|evening)$/;
const HEX_64 = /^[a-f0-9]{64}$/;
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
const REACTIONS = new Set<Reaction>(["like", "dislike", "clear"]);
const SURFACES = new Set(["selected", "more"]);
const MAX_BODY_BYTES = 2048;
const MAX_MANIFEST_BYTES = 2_000_000;
const MAX_MANIFEST_ITEMS = 2_000;
const HOURLY_GLOBAL_LIMIT = 5_000;
const HOURLY_NETWORK_LIMIT = 300;
const HOURLY_VISITOR_LIMIT = 120;

function corsHeaders(origin: string): HeadersInit {
  return {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    "Cache-Control": "no-store",
    Vary: "Origin",
  };
}

function json(origin: string, data: unknown, status = 200): Response {
  return Response.json(data, { status, headers: corsHeaders(origin) });
}

function parsePayload(payload: FeedbackRequest) {
  const eventId = typeof payload.event_id === "string" ? payload.event_id : "";
  const reportId = typeof payload.report_id === "string" ? payload.report_id : "";
  const contentKey = typeof payload.content_key === "string" ? payload.content_key : "";
  const visitorId = typeof payload.visitor_id === "string" ? payload.visitor_id : "";
  const manifestId = typeof payload.manifest_id === "string" ? payload.manifest_id : "";
  const reaction = typeof payload.reaction === "string" ? payload.reaction : "";

  if (
    !UUID.test(eventId) ||
    !UUID.test(visitorId) ||
    !REPORT_ID.test(reportId) ||
    !HEX_64.test(contentKey) ||
    !HEX_64.test(manifestId) ||
    !REACTIONS.has(reaction as Reaction)
  ) {
    return null;
  }
  return {
    eventId,
    reportId,
    contentKey,
    visitorId,
    manifestId,
    reaction: reaction as Reaction,
  };
}

function validOptionalText(value: unknown, maxLength: number): boolean {
  return value == null || (typeof value === "string" && value.length <= maxLength);
}

function validateManifest(raw: unknown, reportId: string): ReportManifest | null {
  if (!raw || typeof raw !== "object" || Array.isArray(raw)) return null;
  const candidate = raw as Partial<ReportManifest>;
  if (
    candidate.schema_version !== 1 ||
    candidate.report_id !== reportId ||
    typeof candidate.manifest_id !== "string" ||
    !HEX_64.test(candidate.manifest_id) ||
    !Array.isArray(candidate.items) ||
    candidate.items.length > MAX_MANIFEST_ITEMS
  ) {
    return null;
  }

  const seen = new Set<string>();
  const items: ManifestItem[] = [];
  for (const rawItem of candidate.items) {
    if (!rawItem || typeof rawItem !== "object" || Array.isArray(rawItem)) return null;
    const item = rawItem as Partial<ManifestItem>;
    if (
      typeof item.id !== "string" ||
      item.id.length < 1 ||
      item.id.length > 500 ||
      typeof item.content_key !== "string" ||
      !HEX_64.test(item.content_key) ||
      seen.has(item.content_key) ||
      typeof item.surface !== "string" ||
      !SURFACES.has(item.surface) ||
      typeof item.title !== "string" ||
      item.title.trim().length < 1 ||
      item.title.length > 500 ||
      typeof item.url !== "string" ||
      item.url.length > 2_000 ||
      typeof item.score !== "number" ||
      !Number.isFinite(item.score) ||
      item.score < 0 ||
      item.score > 10 ||
      !validOptionalText(item.source_type, 80) ||
      !validOptionalText(item.profile, 80) ||
      (item.tags !== undefined &&
        (!Array.isArray(item.tags) ||
          item.tags.length > 30 ||
          item.tags.some(
            (tag) => typeof tag !== "string" || tag.length < 1 || tag.length > 80,
          )))
    ) {
      return null;
    }
    try {
      const parsedUrl = new URL(item.url);
      if (parsedUrl.protocol !== "http:" && parsedUrl.protocol !== "https:") return null;
    } catch {
      return null;
    }
    seen.add(item.content_key);
    items.push({
      id: item.id,
      content_key: item.content_key,
      surface: item.surface as "selected" | "more",
      title: item.title,
      url: item.url,
      score: item.score,
      source_type: item.source_type ?? null,
      profile: item.profile ?? null,
      tags: item.tags ?? [],
    });
  }

  return {
    schema_version: 1,
    report_id: reportId,
    manifest_id: candidate.manifest_id,
    items,
  };
}

export function createFeedbackRoutes(
  runtime: () => RuntimeEnv,
  fetchManifest: typeof fetch = fetch,
) {
  function allowedOrigin(request: Request): string | null {
    const origin = request.headers.get("Origin");
    const allowed = runtime().ALLOWED_ORIGIN ?? "https://maestrokurtc-oss.github.io";
    return origin === allowed ? origin : null;
  }

  async function hmacValue(namespace: string, value: string): Promise<string> {
    const secret = runtime().VOTER_HMAC_SECRET;
    if (!secret || secret.length < 32) throw new Error("feedback service is not configured");
    const key = await crypto.subtle.importKey(
      "raw",
      new TextEncoder().encode(secret),
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["sign"],
    );
    const signature = await crypto.subtle.sign(
      "HMAC",
      key,
      new TextEncoder().encode(`${namespace}:${value}`),
    );
    return Array.from(new Uint8Array(signature), (byte) =>
      byte.toString(16).padStart(2, "0"),
    ).join("");
  }

  async function loadManifest(reportId: string): Promise<ReportManifest> {
    const base = (
      runtime().REPORT_DATA_ORIGIN ??
      "https://maestrokurtc-oss.github.io/ai-researcher/data/reports"
    ).replace(/\/$/, "");
    const response = await fetchManifest(`${base}/${reportId}.json`, {
      headers: { Accept: "application/json" },
    });
    if (!response.ok) throw new Error("report manifest is unavailable");
    const declaredLength = Number(response.headers.get("Content-Length") ?? 0);
    if (declaredLength > MAX_MANIFEST_BYTES) throw new Error("report manifest is too large");
    const text = await response.text();
    if (new TextEncoder().encode(text).byteLength > MAX_MANIFEST_BYTES) {
      throw new Error("report manifest is too large");
    }
    let payload: unknown;
    try {
      payload = JSON.parse(text);
    } catch {
      throw new Error("report manifest is invalid");
    }
    const manifest = validateManifest(payload, reportId);
    if (!manifest) throw new Error("report manifest is invalid");
    return manifest;
  }

  async function findExisting(eventId: string): Promise<ExistingEvent | null> {
    return runtime()
      .DB.prepare(
        `SELECT manifest_id, report_id, content_key, voter_hash, reaction
         FROM feedback_events WHERE event_id = ?`,
      )
      .bind(eventId)
      .first<ExistingEvent>();
  }

  function sameEvent(
    existing: ExistingEvent,
    parsed: NonNullable<ReturnType<typeof parsePayload>>,
    voterHash: string,
  ): boolean {
    return (
      existing.manifest_id === parsed.manifestId &&
      existing.report_id === parsed.reportId &&
      existing.content_key === parsed.contentKey &&
      existing.voter_hash === voterHash &&
      existing.reaction === parsed.reaction
    );
  }

  async function takeRateLimit(keyHash: string, limit: number): Promise<boolean> {
    const bucket = Math.floor(Date.now() / 3_600_000);
    const row = await runtime()
      .DB.prepare(
        `INSERT INTO feedback_rate_limits (key_hash, bucket, count, expires_at)
         VALUES (?, ?, 1, datetime('now', '+2 hours'))
         ON CONFLICT(key_hash, bucket)
         DO UPDATE SET count = feedback_rate_limits.count + 1
         WHERE feedback_rate_limits.count < ?
         RETURNING count`,
      )
      .bind(keyHash, bucket, limit)
      .first<{ count: number }>();
    if (!row) return false;
    if (!Number.isFinite(Number(row.count))) throw new Error("rate limiter is unavailable");
    return Number(row.count) <= limit;
  }

  async function withinInfrastructureLimits(request: Request): Promise<boolean> {
    await runtime()
      .DB.prepare("DELETE FROM feedback_rate_limits WHERE expires_at < datetime('now')")
      .run();

    const clientIp = request.headers.get("CF-Connecting-IP")?.trim();
    if (clientIp && clientIp.length <= 128) {
      const networkHash = await hmacValue("network", clientIp);
      if (!(await takeRateLimit(networkHash, HOURLY_NETWORK_LIMIT))) return false;
    }
    return takeRateLimit("global", HOURLY_GLOBAL_LIMIT);
  }

  async function OPTIONS(request: Request): Promise<Response> {
    const origin = allowedOrigin(request);
    if (!origin) return Response.json({ error: "forbidden" }, { status: 403 });
    return new Response(null, { status: 204, headers: corsHeaders(origin) });
  }

  async function POST(request: Request): Promise<Response> {
    const origin = allowedOrigin(request);
    if (!origin) return Response.json({ error: "forbidden" }, { status: 403 });
    if (!request.headers.get("Content-Type")?.toLowerCase().startsWith("application/json")) {
      return json(origin, { error: "invalid request" }, 415);
    }
    const declaredLength = Number(request.headers.get("Content-Length") ?? 0);
    if (declaredLength > MAX_BODY_BYTES) {
      return json(origin, { error: "request too large" }, 413);
    }

    let raw = "";
    try {
      raw = await request.text();
    } catch {
      return json(origin, { error: "invalid request" }, 400);
    }
    if (new TextEncoder().encode(raw).byteLength > MAX_BODY_BYTES) {
      return json(origin, { error: "request too large" }, 413);
    }
    let payload: FeedbackRequest;
    try {
      payload = JSON.parse(raw) as FeedbackRequest;
    } catch {
      return json(origin, { error: "invalid request" }, 400);
    }
    const parsed = parsePayload(payload);
    if (!parsed) return json(origin, { error: "invalid request" }, 400);

    try {
      const voterHash = await hmacValue("visitor", parsed.visitorId);
      // Protect even idempotency lookups. Capped buckets stop updating once
      // full, so rejected floods do not keep growing rate-limit write volume.
      if (!(await withinInfrastructureLimits(request))) {
        return json(origin, { error: "too many requests" }, 429);
      }
      const existing = await findExisting(parsed.eventId);
      if (existing) {
        return sameEvent(existing, parsed, voterHash)
          ? json(origin, { accepted: true, reaction: parsed.reaction })
          : json(origin, { error: "event conflict" }, 409);
      }

      if (!(await takeRateLimit(voterHash, HOURLY_VISITOR_LIMIT))) {
        return json(origin, { error: "too many requests" }, 429);
      }

      const manifest = await loadManifest(parsed.reportId);
      if (manifest.manifest_id !== parsed.manifestId) {
        return json(origin, { error: "stale report" }, 409);
      }
      const item = manifest.items.find(
        (candidate) => candidate.content_key === parsed.contentKey,
      );
      if (!item) return json(origin, { error: "unknown content" }, 404);

      const inserted = await runtime()
        .DB.prepare(
          `INSERT INTO feedback_events (
            event_id, manifest_id, report_id, content_key, content_id, surface,
            reaction, voter_hash, title, url, ai_score, source_type, profile, tags_json
          ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
          ON CONFLICT(event_id) DO NOTHING
          RETURNING event_id`,
        )
        .bind(
          parsed.eventId,
          manifest.manifest_id,
          parsed.reportId,
          item.content_key,
          item.id,
          item.surface,
          parsed.reaction,
          voterHash,
          item.title,
          item.url,
          item.score,
          item.source_type ?? null,
          item.profile ?? null,
          JSON.stringify(item.tags),
        )
        .first<{ event_id: string }>();

      if (inserted) {
        return json(origin, { accepted: true, reaction: parsed.reaction }, 201);
      }
      const concurrent = await findExisting(parsed.eventId);
      if (concurrent && sameEvent(concurrent, parsed, voterHash)) {
        return json(origin, { accepted: true, reaction: parsed.reaction });
      }
      return json(origin, { error: "event conflict" }, 409);
    } catch (error) {
      console.error("feedback write failed", error);
      return json(origin, { error: "feedback unavailable" }, 503);
    }
  }

  return { OPTIONS, POST };
}
