CREATE TABLE `feedback_rate_limits` (
	`key_hash` text NOT NULL,
	`bucket` integer NOT NULL,
	`count` integer DEFAULT 1 NOT NULL,
	`expires_at` text NOT NULL,
	PRIMARY KEY(`key_hash`, `bucket`),
	CONSTRAINT "feedback_rate_count_check" CHECK("feedback_rate_limits"."count" >= 1)
);
--> statement-breakpoint
CREATE INDEX `feedback_rate_expiry_idx` ON `feedback_rate_limits` (`expires_at`);--> statement-breakpoint
DROP INDEX `feedback_latest_idx`;--> statement-breakpoint
CREATE INDEX `feedback_latest_idx` ON `feedback_events` (`report_id`,`manifest_id`,`content_key`,`voter_hash`,`sequence`);