import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Let the real report origin exercise CORS against the local API during QA.
  allowedDevOrigins: ["maestrokurtc-oss.github.io"],
};

export default nextConfig;
