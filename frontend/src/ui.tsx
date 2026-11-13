import { ReactNode } from "react";
import { Link } from "react-router-dom";
import { APP_NAME } from "./lib";
import { useOnline, useSession } from "./session";

const ROLE_LABEL: Record<string, string> = {
  admin: "Administrador", institucion: "Institución", docente: "Docente", estudiante: "Estudiante", particular: "Estudiante",
};

export function Shell({ children, wide = false }: { children: ReactNode; wide?: boolean }) {
  const { profile, logout } = useSession();
  const online = useOnline();
  return (
    <div className="shell">
      <header className="top">
        <Link to="/" className="brand">{APP_NAME}</Link>
        <div className="top-right">
          {!online && <span className="offline" role="status">Sin conexión: tu avance se guarda aquí</span>}
          {profile && (
            <>
              <span className="who">{profile.displayName} <small>{ROLE_LABEL[profile.role]}</small></span>
              <button className="link" onClick={logout}>Salir</button>
            </>
          )}
        </div>
      </header>
      <main className={wide ? "page wide" : "page"}>{children}</main>
    </div>
  );
}

type Item = { id: string; context?: string | null; stem: string; options: Record<string, string> };

/** Pregunta con opciones en forma de hoja de respuestas (óvalos A-D). */
export function Question({ item, selected, onSelect, locked = false, correct }: {
  item: Item; selected: string | null; onSelect: (k: string) => void; locked?: boolean; correct?: string;
}) {
  return (
    <div className="sheet">
      {item.context && <p className="context">{item.context}</p>}
      <p className="stem">{item.stem}</p>
      <div className="options" role="radiogroup" aria-label="Opciones de respuesta">
        {Object.keys(item.options).sort().map((k) => {
          const state = correct ? (k === correct ? " right" : k === selected ? " wrong" : "") : "";
          return (
            <button key={k} type="button" role="radio" aria-checked={selected === k} disabled={locked}
              className={"option" + (selected === k ? " chosen" : "") + state} onClick={() => onSelect(k)}>
              <span className="bubble">{k}</span>
              <span>{item.options[k]}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
}

export function Bar({ value, label }: { value: number | null | undefined; label: string }) {
  const pct = value == null ? 0 : Math.round(value * 100);
  return (
    <div className="bar-row">
      <span className="bar-label">{label}</span>
      <span className="bar" aria-hidden="true"><span style={{ width: `${pct}%` }} className={pct < 40 ? "low" : pct < 70 ? "mid" : "high"} /></span>
      <span className="bar-num">{value == null ? "sin datos" : `${pct} %`}</span>
    </div>
  );
}

export function Notice({ kind = "info", children }: { kind?: "info" | "error" | "ok"; children: ReactNode }) {
  return <p className={`notice ${kind}`} role={kind === "error" ? "alert" : "status"}>{children}</p>;
}

export function CopyLink({ url, label }: { url?: string | null; label: string }) {
  if (!url) return null;
  return (
    <button className="link" type="button" onClick={() => navigator.clipboard?.writeText(url)} title={url}>
      Copiar {label}
    </button>
  );
}
