import "@fontsource/atkinson-hyperlegible/400.css";
import "@fontsource/atkinson-hyperlegible/700.css";
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { APP_NAME } from "./lib";
import "./styles.css";

document.title = APP_NAME;
ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
