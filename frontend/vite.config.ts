import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";
import { VitePWA } from "vite-plugin-pwa";

const APP_NAME = process.env.VITE_APP_NAME || "Rumbo 11";

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: "autoUpdate",
      includeAssets: ["icon.svg"],
      manifest: {
        name: APP_NAME,
        short_name: APP_NAME,
        description: "Preparación adaptativa para la prueba de Estado de grado 11.",
        lang: "es-CO",
        theme_color: "#16245A",
        background_color: "#F2F6FC",
        display: "standalone",
        start_url: "/",
        icons: [{ src: "icon.svg", sizes: "any", type: "image/svg+xml", purpose: "any maskable" }],
      },
      workbox: { globPatterns: ["**/*.{js,css,html,svg,woff2}"], navigateFallback: "/index.html" },
    }),
  ],
  server: { port: 5173 },
});
