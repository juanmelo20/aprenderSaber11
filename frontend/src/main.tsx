import "@fontsource/atkinson-hyperlegible/400.css";
import "@fontsource/atkinson-hyperlegible/700.css";
import React from "react";
import ReactDOM from "react-dom/client";
import { registerSW } from "virtual:pwa-register";
import App from "./App";
import { APP_NAME } from "./lib";
import "./styles.css";

document.title = APP_NAME;
// Cuando se publica una versión nueva, la página se recarga sola en cuanto el navegador la descarga.
// Así nadie se queda usando una copia vieja guardada para trabajar sin conexión.
registerSW({ immediate: true });
ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
