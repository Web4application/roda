import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/automl": "http://127.0.0.1:8000",  // Proxy backend API calls to FastAPI
    },
  },
});
