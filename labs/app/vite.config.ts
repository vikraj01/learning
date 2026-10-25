import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// In development the site runs on :5173 and passes /api and /term to the lab server on :7000.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": "http://127.0.0.1:7000",
      "/term": { target: "ws://127.0.0.1:7000", ws: true },
    },
  },
  build: {
    outDir: "dist",
    chunkSizeWarningLimit: 6000,
  },
});
