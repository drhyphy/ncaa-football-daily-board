CREATE TABLE `board_runs` (
	`id` integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	`generated_at` text NOT NULL,
	`slate_date` text NOT NULL,
	`run_label` text NOT NULL,
	`model_version` text NOT NULL,
	`qualifying_count` integer DEFAULT 0 NOT NULL,
	`payload_json` text NOT NULL,
	`created_at` text NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `board_runs_generated_at_unique` ON `board_runs` (`generated_at`);