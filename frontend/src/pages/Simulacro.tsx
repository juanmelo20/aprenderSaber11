import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, AREA_ORDER, AREAS, cacheGet, cacheSet } from "../lib";
import { useSession } from "../session";
import { Notice, Question, Shell } from "../ui";

export default function Simulacro() {
  const { simId } = useParams();
  const uid = useSession().user!.uid;
  const key = `simulacro:${uid}:${simId}`;
  const [sim, setSim] = useState<any>(null);
  const [answers, setAnswers] = useState<Record<string, string>>(() => cacheGet(key) || {});
  const [idx, setIdx] = useState(0);
  const [left, setLeft] = useState<number | null>(null);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    api(`/api/simulacros/${simId}`).then(setSim).catch((e) => setError(e.status ? e.message : "El simulacro necesita conexión para empezar."));
  }, [simId]);

  useEffect(() => {
    if (!sim || sim.submitted) return;
    const end = new Date(sim.startedAt).getTime() + sim.minutes * 60000;
    const tick = () => setLeft(Math.max(0, Math.round((end - Date.now()) / 1000)));
    tick();
    const t = setInterval(tick, 1000);
    return () => clearInterval(t);
  }, [sim]);

  async function submit() {
    setBusy(true);
    setError("");
    try {
      setSim(await api(`/api/simulacros/${simId}/submit`, { body: { answers } }));
      localStorage.removeItem(key);
      window.scrollTo(0, 0);
    } catch (e: any) {
      setError(e.status ? e.message : "No hay conexión. Tus respuestas siguen guardadas: entrega cuando vuelva la señal.");
    }
    setBusy(false);
  }

  useEffect(() => {
    if (left === 0 && sim && !sim.submitted && !busy) submit();
  }, [left]); // eslint-disable-line react-hooks/exhaustive-deps

  if (!sim) return <Shell>{error ? <Notice kind="error">{error}</Notice> : <p>Cargando…</p>}<Link className="button secondary" to="/">Volver</Link></Shell>;

  if (sim.submitted)
    return (
      <Shell>
        <h1>{sim.title}</h1>
        <p className="result"><mark>{sim.total.correct} de {sim.total.total}</mark> correctas</p>
        <table className="table">
          <thead><tr><th>Área</th><th>Correctas</th><th>Porcentaje</th></tr></thead>
          <tbody>
            {AREA_ORDER.filter((a) => sim.byArea[a]).map((a) => (
              <tr key={a}><td>{AREAS[a].name}</td><td>{sim.byArea[a].correct} de {sim.byArea[a].total}</td><td>{sim.byArea[a].pct} %</td></tr>
            ))}
          </tbody>
        </table>
        <p className="hint">Con pocas preguntas por área, este resultado es una señal, no un puntaje del examen.</p>
        <h2>Revisión</h2>
        <div className="review">
          {sim.items.map((it: any, i: number) => (
            <details key={it.id}>
              <summary className={it.selected === it.correct ? "ok" : "bad"}>
                {i + 1}. {AREAS[it.area].short}: {it.selected === it.correct ? "correcta" : it.selected ? `marcaste ${it.selected}, era ${it.correct}` : `sin responder, era ${it.correct}`}
              </summary>
              {it.context && <p className="context">{it.context}</p>}
              <p>{it.stem}</p>
              <p><b>{it.correct}.</b> {it.options[it.correct]}</p>
              <p>{it.explanation}</p>
            </details>
          ))}
        </div>
        <Link className="button" to="/">Volver a mi inicio</Link>
      </Shell>
    );

  const item = sim.items[idx];
  const answered = Object.keys(answers).length;
  const mm = left == null ? "" : `${Math.floor(left / 60)}:${String(left % 60).padStart(2, "0")}`;
  return (
    <Shell>
      <div className="sim-head">
        <h1>{sim.title}</h1>
        <span className="timer" aria-label="Tiempo restante">{mm}</span>
      </div>
      {error && <Notice kind="error">{error}</Notice>}
      <p className="progress">Pregunta {idx + 1} de {sim.items.length}, {AREAS[item.area].name}. Llevas {answered} respondidas.</p>
      <Question item={item} selected={answers[item.id] || null} onSelect={(k) => {
        const next = { ...answers, [item.id]: k };
        setAnswers(next);
        cacheSet(key, next);
      }} />
      <div className="row">
        <button className="secondary" disabled={idx === 0} onClick={() => setIdx(idx - 1)}>Anterior</button>
        {idx + 1 < sim.items.length
          ? <button onClick={() => { setIdx(idx + 1); window.scrollTo(0, 0); }}>Siguiente</button>
          : <button disabled={busy} onClick={submit}>Entregar simulacro</button>}
      </div>
      <nav className="grid-nav" aria-label="Ir a una pregunta">
        {sim.items.map((it: any, i: number) => (
          <button key={it.id} className={(answers[it.id] ? "filled" : "") + (i === idx ? " here" : "")} onClick={() => setIdx(i)} aria-label={`Pregunta ${i + 1}${answers[it.id] ? ", respondida" : ""}`}>{i + 1}</button>
        ))}
      </nav>
    </Shell>
  );
}
