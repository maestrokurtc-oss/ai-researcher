CREATE TABLE `feedback_events` (
	`sequence` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	`event_id` text NOT NULL,
	`manifest_id` text NOT NULL,
	`report_id` text NOT NULL,
	`content_key` text NOT NULL,
	`content_id` text NOT NULL,
	`surface` text NOT NULL,
	`reaction` text NOT NULL,
	`voter_hash` text NOT NULL,
	`title` text NOT NULL,
	`url` text NOT NULL,
	`ai_score` real NOT NULL,
	`source_type` text,
	`profile` text,
	`tags_json` text DEFAULT '[]' NOT NULL,
	`received_at` text DEFAULT CURRENT_TIMESTAMP NOT NULL,
	CONSTRAINT "feedback_surface_check" CHECK("feedback_events"."surface" IN ('selected', 'more')),
	CONSTRAINT "feedback_reaction_check" CHECK("feedback_events"."reaction" IN ('like', 'dislike', 'clear')),
	CONSTRAINT "feedback_score_check" CHECK("feedback_events"."ai_score" >= 0 AND "feedback_events"."ai_score" <= 10)
);
--> statement-breakpoint
CREATE UNIQUE INDEX `feedback_events_event_id_unique` ON `feedback_events` (`event_id`);--> statement-breakpoint
CREATE INDEX `feedback_latest_idx` ON `feedback_events` (`content_key`,`voter_hash`,`sequence`);--> statement-breakpoint
CREATE INDEX `feedback_report_idx` ON `feedback_events` (`report_id`,`sequence`);--> statement-breakpoint
CREATE INDEX `feedback_received_idx` ON `feedback_events` (`received_at`);