import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { DatabaseSync } from "node:sqlite";
import test from "node:test";

import { createFeedbackRoutes } from "../app/api/v1/feedback/core.ts";

const origin = "https://maestrokurtc-oss.github.io";
const eventId = "018f1d58-7f2a-7c66-8ca7-72c328f92c77";
const visitorId = "018f1d58-7f2a-7c66-8ca7-72c328f92c78";
const contentKey = "a".repeat(64);
const manifestId = "b".repeat(64);
const secret = "test-only-secret-that-is-longer-than-32-characters";

function request(body, options = {}) {
  const headers = {
    "Content-Type": "application/json",
    Origin: options.origin ?? origin,
    ...(options.headers ?? {}),
  };
  return new Request("http://localhost/api/v1/feedback", {
    method: "POST",
    headers,
    body: options.rawBody ?? JSON.stringify(body),
  });
}

function payload(overrides = {}) {
  return {
    event_id: eventId,
    report_id: "2026-09-12-evening",
    content_key: contentKey,
    manifest_id: manifestId,
    visitor_id: visitorId,
    reaction: "like",
    ...overrides,
  };
}

function manifest(overrides = {}) {
  return {
    schema_version: 1,
    report_id: "2026-09-12-evening",
    manifest_id: manifestId,
    items: [{
      id: "near-miss-1",
      content_key: contentKey,
      surface: "more",
      title: "Trusted title",
      url: "https://example.com/trusted",
      score: 7.2,
      source_type: "news",
      profile: "tech-news",
      tags: ["AI"],
    }],
    ...overrides,
  };
}

function databaseStub(options = {}) {
  const calls = [];
  let eventSelects = 0;
  let rateSelects = 0;
  const database = {
    prepare(query) {
      let values = [];
      return {
        bind(...nextValues) {
          values = nextValues;
          return this;
        },
        async first() {
          calls.push({ operation: "first", query, values });
          if (query.includes("SELECT manifest_id")) {
            const result = eventSelects === 0
              ? (options.existing ?? null)
              : (options.concurrent ?? options.existing ?? null);
            eventSelects += 1;
            return result;
          }
          if (query.includes("INSERT INTO feedback_rate_limits")) {
            const count = options.rateCounts?.[rateSelects] ?? options.rateCount ?? 1;
            rateSelects += 1;
            if (count === "blocked") return null;
            return { count };
          }
          if (query.includes("INSERT INTO feedback_events")) {
            return options.inserted === false ? null : { event_id: values[0] };
          }
          return null;
        },
        async run() {
          calls.push({ operation: "run", query, values });
          return { success: true };
        },
      };
    },
  };
  return { database, calls };
}

async function hmacVisitor(value) {
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
    new TextEncoder().encode(`visitor:${value}`),
  );
  return Buffer.from(signature).toString("hex");
}

function runtime(database) {
  return {
    DB: database,
    ALLOWED_ORIGIN: origin,
    VOTER_HMAC_SECRET: secret,
  };
}

test("status page explains storage and privacy accurately", async () => {
  const source = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  assert.match(source, /피드백 저장소가 작동 중입니다/);
  assert.match(source, /원본 브라우저 ID/);
  assert.doesNotMatch(source, /codex-preview|react-loading-skeleton/);
});

test("OPTIONS returns the exact report origin", async () => {
  const routes = createFeedbackRoutes(() => ({ ALLOWED_ORIGIN: origin }));
  const response = await routes.OPTIONS(new Request("http://localhost/api/v1/feedback", {
    method: "OPTIONS",
    headers: { Origin: origin },
  }));

  assert.equal(response.status, 204);
  assert.equal(response.headers.get("Access-Control-Allow-Origin"), origin);
  assert.equal(response.headers.get("Access-Control-Allow-Methods"), "POST, OPTIONS");
});

test("feedback endpoint rejects requests outside the report origin", async () => {
  const routes = createFeedbackRoutes(() => ({ ALLOWED_ORIGIN: origin }));
  const response = await routes.POST(request({}, { origin: "https://example.com" }));

  assert.equal(response.status, 403);
  assert.deepEqual(await response.json(), { error: "forbidden" });
});

test("malformed JSON returns a client error", async () => {
  const routes = createFeedbackRoutes(() => ({ ALLOWED_ORIGIN: origin }));
  const response = await routes.POST(request({}, { rawBody: "{" }));

  assert.equal(response.status, 400);
  assert.deepEqual(await response.json(), { error: "invalid request" });
});

test("feedback endpoint validates payload before database access", async () => {
  const routes = createFeedbackRoutes(() => ({ ALLOWED_ORIGIN: origin }));
  const response = await routes.POST(request({}));

  assert.equal(response.status, 400);
  assert.deepEqual(await response.json(), { error: "invalid request" });
});

test("feedback endpoint stores trusted metadata without raw identifiers", async () => {
  const { database, calls } = databaseStub();
  const fetchManifest = async () => Response.json(manifest());
  const routes = createFeedbackRoutes(() => runtime(database), fetchManifest);

  const response = await routes.POST(request({
    ...payload(),
    title: "Client-supplied title must be ignored",
  }, { headers: { "CF-Connecting-IP": "203.0.113.10" } }));

  assert.equal(response.status, 201);
  assert.deepEqual(await response.json(), { accepted: true, reaction: "like" });
  const write = calls.find((call) => call.query.includes("INSERT INTO feedback_events"));
  assert.ok(write);
  assert.equal(write.values[8], "Trusted title");
  assert.equal(write.values[9], "https://example.com/trusted");
  assert.notEqual(write.values[7], visitorId);
  assert.equal(calls.some((call) => call.values.includes(visitorId)), false);
  assert.equal(calls.some((call) => call.values.includes("203.0.113.10")), false);
});

test("idempotent retry skips manifest fetch after infrastructure limiting", async () => {
  const existing = {
    manifest_id: manifestId,
    report_id: "2026-09-12-evening",
    content_key: contentKey,
    voter_hash: await hmacVisitor(visitorId),
    reaction: "like",
  };
  const { database, calls } = databaseStub({ existing });
  let fetchCount = 0;
  const routes = createFeedbackRoutes(() => runtime(database), async () => {
    fetchCount += 1;
    return Response.json(manifest());
  });

  const response = await routes.POST(request(payload()));

  assert.equal(response.status, 200);
  assert.equal(fetchCount, 0);
  assert.equal(calls.some((call) => call.query.includes("feedback_rate_limits")), true);
});

test("global cap rejects before manifest fetch", async () => {
  const { database } = databaseStub({ rateCounts: ["blocked"] });
  let fetchCount = 0;
  const routes = createFeedbackRoutes(() => runtime(database), async () => {
    fetchCount += 1;
    return Response.json(manifest());
  });

  const response = await routes.POST(request(payload()));

  assert.equal(response.status, 429);
  assert.equal(fetchCount, 0);
});

test("migrations and capped rate UPSERT execute in SQLite", async () => {
  const database = new DatabaseSync(":memory:");
  try {
    for (const filename of ["0000_adorable_kylun.sql", "0001_stale_cardiac.sql"]) {
      const migration = await readFile(
        new URL(`../drizzle/${filename}`, import.meta.url),
        "utf8",
      );
      migration.split("--> statement-breakpoint").forEach((statement) => {
        if (statement.trim()) database.exec(statement);
      });
    }

    const rate = database.prepare(`
      INSERT INTO feedback_rate_limits (key_hash, bucket, count, expires_at)
      VALUES (?, ?, 1, datetime('now', '+2 hours'))
      ON CONFLICT(key_hash, bucket)
      DO UPDATE SET count = feedback_rate_limits.count + 1
      WHERE feedback_rate_limits.count < ?
      RETURNING count
    `);
    assert.equal(rate.get("global", 1, 2).count, 1);
    assert.equal(rate.get("global", 1, 2).count, 2);
    assert.equal(rate.get("global", 1, 2), undefined);

    assert.throws(() => database.exec(`
      INSERT INTO feedback_events (
        event_id, manifest_id, report_id, content_key, content_id, surface,
        reaction, voter_hash, title, url, ai_score, tags_json
      ) VALUES (
        'event', '${manifestId}', '2026-09-12-evening', '${contentKey}',
        'content', 'invalid', 'like', '${"c".repeat(64)}', 'title',
        'https://example.com', 5, '[]'
      )
    `), /CHECK constraint failed/);
  } finally {
    database.close();
  }
});

test("malformed manifest is rejected without a feedback insert", async () => {
  const { database, calls } = databaseStub();
  const routes = createFeedbackRoutes(
    () => runtime(database),
    async () => Response.json(manifest({
      items: [{
        id: "bad",
        content_key: contentKey,
        surface: "more",
        title: "Unsafe",
        url: "javascript:alert(1)",
        score: 5,
        tags: [],
      }],
    })),
  );
  const originalError = console.error;
  console.error = () => {};
  try {
    const response = await routes.POST(request(payload()));
    assert.equal(response.status, 503);
  } finally {
    console.error = originalError;
  }
  assert.equal(calls.some((call) => call.query.includes("INSERT INTO feedback_events")), false);
});

test("concurrent duplicate insert resolves as an idempotent success", async () => {
  const matching = {
    manifest_id: manifestId,
    report_id: "2026-09-12-evening",
    content_key: contentKey,
    voter_hash: await hmacVisitor(visitorId),
    reaction: "like",
  };
  const { database } = databaseStub({ inserted: false, concurrent: matching });
  const routes = createFeedbackRoutes(
    () => runtime(database),
    async () => Response.json(manifest()),
  );

  const response = await routes.POST(request(payload()));

  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { accepted: true, reaction: "like" });
});
