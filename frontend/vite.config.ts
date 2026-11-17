import react from "@vitejs/plugin-react";
import { defineConfig, loadEnv } from "vite";
import { VitePWA } from "vite-plugin-pwa";

export default defineConfig(({ command, mode }) => {
  const env = loadEnv(mode, process.cwd(), "VITE_");
  const APP_NAME = env.VITE_APP_NAME || "Rumbo 11";
  // Una compilación para publicar sin la configuración de Firebase produce una web que intenta conectarse a los
  // emuladores del computador de quien la compiló: nadie podría entrar. Mejor fallar aquí con un mensaje claro.
  if (command === "build" && mode === "production" && (!env.VITE_FIREBASE_API_KEY || !env.VITE_API_URL)) {
    throw new Error(
      "Falta frontend/.env.production (o le faltan VITE_FIREBASE_API_KEY y VITE_API_URL). " +
        "Compila desde la última versión del repositorio en GitHub. Para pruebas locales usa: npx vite build --mode e2e",
    );
  }
  return {
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
};
});
