import { integer, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const boardRuns = sqliteTable("board_runs", {
  id: integer("id").primaryKey({ autoIncrement: true }),
  generatedAt: text("generated_at").notNull().unique(),
  slateDate: text("slate_date").notNull(),
  runLabel: text("run_label").notNull(),
  modelVersion: text("model_version").notNull(),
  qualifyingCount: integer("qualifying_count").notNull().default(0),
  payloadJson: text("payload_json").notNull(),
  createdAt: text("created_at").notNull(),
});
