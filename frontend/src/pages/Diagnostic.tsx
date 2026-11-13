import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, AREAS } from "../lib";
import { Notice, Question, Shell } from "../ui";

export default function Diagnostic() {
  const area = (useParams().area || "").toUpperCase();
  const [state, setState] = useState<any>(null);
  const [selected, setSelected] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    api(`/api/diagnostic/${area}/start`, { method: "POST" }).then(setState).catch((e) => setError(e.message));
  }, [area]);

  async function answer() {
    if (!selected) return;
    setBusy(true);
    setError("");
    try {
      setState(await api(`/api/diagnostic/${area}/answer`, { body: { itemId: state.item.id, selected } }));
      setSelected(null);
      window.scrollTo(0, 0);
    } catch (e: any) {
      setError(e.status ? e.message : "Se fue la conexión. Tu avance quedó guardado: intenta de nuevo cuando vuelva.");
    }
    setBusy(false);
  }

  return (
    <Shell>
      <h1>Diagnóstico de {AREAS[area]?.name}</h1>
      {error && <Notice kind="error">{error}</Notice>}
      {!state && !error && <p>Cargando…</p>}
      {state && !state.done && (
        <>
          <p className="progress">Pregunta {state.n} de máximo {state.max}. Las preguntas se ajustan a tus respuestas; si no sabes una, marca la que creas y sigue.</p>
          <Question item={state.item} selected={selected} onSelect={setSelected} locked={busy} />
          <button disabled={!selected || busy} onClick={answer}>Responder y seguir</button>
        </>
      )}
      {state?.done && (
        <div className="stack">
          <p className="result"><mark>Nivel {state.result.level}</mark> en {AREAS[area]?.name}</p>
          <p>Puntaje estimado: entre {state.result.low} y {state.result.high} sobre 100 (lo más probable, {state.result.score}), con {state.result.n} preguntas. Es un punto de partida, no una nota: con tan pocas preguntas el rango es amplio y se va afinando cada semana con el cuestionario de salida.</p>
          <Link className="button" to="/">Volver a mi inicio</Link>
        </div>
      )}
    </Shell>
  );
}
