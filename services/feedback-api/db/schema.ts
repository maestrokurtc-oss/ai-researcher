import { sql } from "drizzle-orm";
import {
  check,
  index,
  integer,
  primaryKey,
  real,
  sqliteTable,
  text,
} from "drizzle-orm/sqlite-core";

export const feedbackEvents = sqliteTable(
  "feedback_events",
  {
    sequence: integer("sequence").primaryKey({ autoIncrement: true }),
    eventId: text("event_id").notNull().unique(),
    manifestId: text("manifest_id").notNull(),
    reportId: text("report_id").notNull(),
    contentKey: text("content_key").notNull(),
    contentId: text("content_id").notNull(),
    surface: text("surface", { enum: ["selected", "more"] }).notNull(),
    reaction: text("reaction", {
      enum: ["like", "dislike", "clear"],
    }).notNull(),
    voterHash: text("voter_hash").notNull(),
    title: text("title").notNull(),
    url: text("url").notNull(),
    aiScore: real("ai_score").notNull(),
    sourceType: text("source_type"),
    profile: text("profile"),
    tagsJson: text("tags_json").notNull().default("[]"),
    receivedAt: text("received_at").notNull().default(sql`CURRENT_TIMESTAMP`),
  },
  (table) => [
    check(
      "feedback_surface_check",
      sql`${table.surface} IN ('selected', 'more')`,
    ),
    check(
      "feedback_reaction_check",
      sql`${table.reaction} IN ('like', 'dislike', 'clear')`,
    ),
    check(
      "feedback_score_check",
      sql`${table.aiScore} >= 0 AND ${table.aiScore} <= 10`,
    ),
    index("feedback_latest_idx").on(
      table.reportId,
      table.manifestId,
      table.contentKey,
      table.voterHash,
      table.sequence,
    ),
    index("feedback_report_idx").on(table.reportId, table.sequence),
    index("feedback_received_idx").on(table.receivedAt),
  ],
);

export const feedbackRateLimits = sqliteTable(
  "feedback_rate_limits",
  {
    keyHash: text("key_hash").notNull(),
    bucket: integer("bucket").notNull(),
    count: integer("count").notNull().default(1),
    expiresAt: text("expires_at").notNull(),
  },
  (table) => [
    primaryKey({ columns: [table.keyHash, table.bucket] }),
    check("feedback_rate_count_check", sql`${table.count} >= 1`),
    index("feedback_rate_expiry_idx").on(table.expiresAt),
  ],
);
