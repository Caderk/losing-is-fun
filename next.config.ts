import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */

  // Configure Turbopack to ignore models directory
  turbopack: {},

  webpack: (config) => {
    // Exclude models directory from being processed by webpack
    config.watchOptions = {
      ...config.watchOptions,
      ignored: ["**/node_modules", "**/models/**", "**/.git", "**/.next"],
    };

    // Ignore large GGUF model files
    config.module.rules.push({
      test: /\.gguf$/,
      type: "asset/resource",
      generator: {
        emit: false,
      },
    });

    return config;
  },
};

export default nextConfig;
