import { doc, getDoc, setDoc } from "firebase/firestore";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, cacheGet, cacheSet, db } from "../lib";
import { useOnline, useSession } from "../session";
import { Notice, Question, Shell } from "../ui";

type Ans = { itemId: string; selected: string; hintsUsed: number };

export default function Practice() {
  const { planId, sessionId } = useParams();
  const uid = useSession().user!.uid;
  const online = useOnline();
  const saveKey = `sesion:${uid}:${planId}:${sessionId}`;
  const [session, setSession] = useState<any>(undefined);
  const [answers, setAnswers] = useState<Ans[]>(() => cacheGet<any>(saveKey)?.answers || []);
  const [startedAt] = useState<string>(() => cacheGet<any>(saveKey)?.startedAt || new Date().toISOString());
  const [selected, setSelected] = useState<string | null>(null);
  const [revealed, setRevealed] = useState(false);
  const [hints, setHints] = useState(0);
  const [question, setQuestion] = useState("");
  const [tutor, setTutor] = useState<{ text: string; source: string } | null>(null);
  const [tutorBusy, setTutorBusy] = useState(false);
  const [finished, setFinished] = useState(false);

  useEffect(() => {
    // getDoc usa la copia guardada en el dispositivo cuando no hay conexión.
    getDoc(doc(db, "users", uid, "plans", planId!))
      .then((snap) => setSession(snap.exists() ? (snap.data().sessions || []).find((s: any) => s.id === sessionId) || null : null))
      .catch(() => setSession(null));
  }, [uid, planId, sessionId]);

  if (session === undefined) return <Shell><p>Cargando…</p></Shell>;
  if (session === null)
    return <Shell><Notice kind="error">No encontramos esta sesión en tu dispositivo. Vuelve al inicio con conexión para descargar tu plan.</Notice><Link className="button" to="/">Volver</Link></Shell>;

  const items: any[] = session.items;
  const withTutor: boolean = !!session.tutor;
  const idx = Math.min(answers.length, items.length - 1);
  const item = items[idx];
  const allAnswered = answers.length >= items.length;

  function record() {
    const next = [...answers, { itemId: item.id, selected: selected!, hintsUsed: hints }];
    setAnswers(next);
    cacheSet(saveKey, { answers: next, startedAt });
    setSelected(null);
    setRevealed(false);
    setHints(0);
    setTutor(null);
    setQuestion("");
    window.scrollTo(0, 0);
    if (next.length >= items.length) finish(next);
  }

  function finish(all: Ans[]) {
    // No se espera la confirmación del servidor: sin conexión, Firestore guarda el intento y lo envía después.
    setDoc(doc(db, "users", uid, "attempts", `${planId}_${sessionId}`), {
      planId, sessionId, type: session.type, answers: all, startedAt, finishedAt: new Date().toISOString(), processed: false,
    }).catch(() => undefined);
    localStorage.removeItem(saveKey);
    setFinished(true);
  }

  async function askTutor() {
    setTutorBusy(true);
    try {
      const r = await api("/api/tutor/ask", { body: { planId, sessionId, itemId: item.id, answered: revealed, selected, question } });
      setTutor({ text: r.reply, source: r.limit ? "limite" : r.source });
      if (!revealed) setHints((h) => h + 1);
    } catch (e: any) {
      setTutor({ text: e.status ? e.message : "El tutor necesita conexión. Usa las pistas guardadas mientras tanto.", source: "error" });
    }
    setTutorBusy(false);
  }

  if (finished || (allAnswered && !selected)) {
    const correct = answers.filter((a) => items.find((i) => i.id === a.itemId)?.correct === a.selected).length;
    const pct = Math.round((100 * correct) / items.length);
    return (
      <Shell>
        <h1>{session.title}</h1>
        <p className="result"><mark>{correct} de {items.length}</mark> correctas</p>
        {session.type === "salida" && (
          <Notice kind={pct >= 60 ? "ok" : "info"}>
            {pct >= 60 ? "Superaste el cuestionario de salida. Tu ruta de la próxima semana sube de nivel." : "Aún no llegas al 60 %. La próxima semana refuerzas estos mismos temas con preguntas distintas."}
          </Notice>
        )}
        {!online && <Notice>Quedó guardada en este dispositivo y se envía sola cuando haya conexión.</Notice>}
        {session.type === "salida" && (
          <div className="review">
            {items.map((it, i) => {
              const a = answers.find((x) => x.itemId === it.id);
              return (
                <details key={it.id}>
                  <summary className={a?.selected === it.correct ? "ok" : "bad"}>Pregunta {i + 1}: {a?.selected === it.correct ? "correcta" : `marcaste ${a?.selected}, era ${it.correct}`}</summary>
                  <p>{it.stem}</p>
                  <p>{it.explanation}</p>
                </details>
              );
            })}
          </div>
        )}
        <Link className="button" to="/">Volver a mi ruta</Link>
      </Shell>
    );
  }

  const isCorrect = selected === item.correct;
  return (
    <Shell>
      <h1>{session.title}</h1>
      <p className="progress">Pregunta {idx + 1} de {items.length}{!withTutor && ". Sin pistas ni tutor: es para medir cómo vas."}</p>
      <Question item={item} selected={selected} onSelect={setSelected} locked={revealed} correct={revealed ? item.correct : undefined} />

      {withTutor && !revealed && (
        <div className="help">
          {item.hints.slice(0, hints).map((h: string, i: number) => <p key={i} className="hint-card">Pista {i + 1}: {h}</p>)}
          <button type="button" className="secondary" disabled={hints >= item.hints.length} onClick={() => setHints(hints + 1)}>
            {hints >= item.hints.length ? "No hay más pistas guardadas" : hints === 0 ? "Dame una pista" : "Otra pista"}
          </button>
        </div>
      )}

      {withTutor && revealed && (
        <div className={`feedback ${isCorrect ? "ok" : "bad"}`}>
          <b>{isCorrect ? "Correcto." : `No era la ${selected}. La correcta es la ${item.correct}.`}</b>
          <p>{item.explanation}</p>
        </div>
      )}

      {withTutor && (
        <div className="tutor">
          <label>{revealed ? "¿Algo no quedó claro? Pregúntale al tutor" : "Pregúntale al tutor (te orienta, no te da la respuesta)"}
            <input value={question} onChange={(e) => setQuestion(e.target.value)} maxLength={300} placeholder={revealed ? "Por ejemplo: ¿por qué no era la A?" : "Por ejemplo: no entiendo qué me piden"} />
          </label>
          <button type="button" className="secondary" disabled={!online || tutorBusy || question.trim().length < 3} onClick={askTutor}>
            {online ? (tutorBusy ? "Pensando…" : "Preguntar") : "El tutor necesita conexión"}
          </button>
          {tutor && <p className="tutor-reply">{tutor.text}{tutor.source === "limite" && " (Llegaste al límite de preguntas al tutor por hoy.)"}</p>}
        </div>
      )}

      {withTutor && !revealed && <button disabled={!selected} onClick={() => setRevealed(true)}>Responder</button>}
      {withTutor && revealed && <button onClick={record}>{idx + 1 === items.length ? "Terminar sesión" : "Siguiente pregunta"}</button>}
      {!withTutor && <button disabled={!selected} onClick={record}>{idx + 1 === items.length ? "Entregar cuestionario" : "Siguiente pregunta"}</button>}
    </Shell>
  );
}
