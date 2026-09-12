import { env } from "cloudflare:workers";

import { createFeedbackRoutes, type RuntimeEnv } from "./core";

const routes = createFeedbackRoutes(() => env as unknown as RuntimeEnv);

export const OPTIONS = routes.OPTIONS;
export const POST = routes.POST;
