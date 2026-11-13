import { collection, limit, onSnapshot, query, where } from "firebase/firestore";
import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { api, AREA_ORDER, AREAS, cacheGet, cacheSet, db } from "../lib";
import { useOnline, useSession } from "../session";
import { Bar, Notice, Shell } from "../ui";

const TYPE_LABEL: Record<string, string> = { practica: "Práctica", repaso: "Repaso", salida: "Cuestionario de salida" };

export default function StudentHome() {
  const { user, profile } = useSession();
  const uid = user!.uid;
  const online = useOnline();
  const [overview, setOverview] = useState<any>(() => cacheGet(`resumen:${uid}`));
  const [catalog, setCatalog] = useState<any>(() => cacheGet("catalogo"));
  const [plan, setPlan] = useState<any>(undefined);
  const [attempts, setAttempts] = useState<Record<string, { processed: boolean; local: boolean }>>({});
  const [sims, setSims] = useState<any[]>(() => cacheGet(`simulacros:${uid}`) || []);
  const [error, setError] = useState("");

  useEffect(() => {
    const plans = query(collection(db, "users", uid, "plans"), where("status", "==", "activo"), limit(1));
    const stopPlans = onSnapshot(plans, (snap) => setPlan(snap.empty ? null : { id: snap.docs[0].id, ...snap.docs[0].data() }));
    const stopAttempts = onSnapshot(collection(db, "users", uid, "attempts"), { includeMetadataChanges: true }, (snap) => {
      const map: Record<string, { processed: boolean; local: boolean }> = {};
      snap.forEach((d) => (map[d.id] = { processed: !!d.data().processed, local: d.metadata.hasPendingWrites }));
      setAttempts(map);
    });
    return () => {
      stopPlans();
      stopAttempts();
    };
  }, [uid]);

  // Intentos que ya llegaron al servidor pero aún no se han calificado.
  const toSync = useMemo(() => Object.values(attempts).filter((a: any) => !a.processed && !a.local).length, [attempts]);
  const waiting = useMemo(() => Object.values(attempts).filter((a: any) => a.local).length, [attempts]);

  useEffect(() => {
    if (!online) return;
    let alive = true;
    (async () => {
      try {
        if (toSync > 0) await api("/api/sync", { method: "POST" });
        const ov = await api("/api/overview");
        if (!alive) return;
        cacheSet(`resumen:${uid}`, ov);
        setOverview(ov);
        if (!catalog) {
          const c = await api("/api/catalog");
          cacheSet("catalogo", c);
          setCatalog(c);
        }
        if (ov.diagnosed.length === AREA_ORDER.length && plan === null) await api("/api/plan/ensure", { method: "POST" });
        const s = await api("/api/simulacros");
        cacheSet(`simulacros:${uid}`, s);
        if (alive) setSims(s);
        setError("");
      } catch (e: any) {
        if (alive && e.status) setError(e.message);
      }
    })();
    return () => {
      alive = false;
    };
  }, [online, toSync, plan === null, uid]); // eslint-disable-line react-hooks/exhaustive-deps

  const diagnosed: string[] = overview?.diagnosed || [];
  const pendingAreas = AREA_ORDER.filter((a) => !diagnosed.includes(a));

  function sessionState(s: any, all: any[]) {
    const done = s.status === "hecha" || !!attempts[`${plan.id}_${s.id}`];
    if (done) return "done";
    if (s.type !== "salida") return "open";
    return all.filter((x) => x.type !== "salida").every((x) => x.status === "hecha" || attempts[`${plan.id}_${x.id}`]) ? "open" : "locked";
  }
  const states: string[] = plan ? plan.sessions.map((s: any) => sessionState(s, plan.sessions)) : [];
  const firstOpen = states.indexOf("open");

  return (
    <Shell>
      <h1>Hola, {String(profile.displayName || "").split(" ")[0]}</h1>
      {error && <Notice kind="error">{error}</Notice>}
      {waiting > 0 && <Notice>Tienes {waiting === 1 ? "una sesión guardada" : `${waiting} sesiones guardadas`} en este dispositivo. Se envían solas cuando vuelva la conexión.</Notice>}

      <section>
        <h2>Tu nivel por área</h2>
        {pendingAreas.length > 0 && (
          <p className="hint">{diagnosed.length === 0
            ? "Empieza por el diagnóstico de cada área: son entre 6 y 10 preguntas y no tiene nota. Sirve para armar tu plan."
            : `Te ${pendingAreas.length === 1 ? "falta 1 diagnóstico" : `faltan ${pendingAreas.length} diagnósticos`} para completar tu punto de partida.`}</p>
        )}
        <ul className="areas">
          {AREA_ORDER.map((a) => {
            const r = overview?.areas?.[a];
            return (
              <li key={a}>
                <span className="area-name">{AREAS[a].name}</span>
                {r ? (
                  <span className="level"><mark>Nivel {r.level}</mark> <small>puntaje estimado {r.low != null ? `entre ${r.low} y ${r.high}` : r.score}</small></span>
                ) : online ? (
                  <Link className="button small" to={`/diagnostico/${a}`}>Hacer diagnóstico</Link>
                ) : (
                  <small>Necesitas conexión para el diagnóstico</small>
                )}
              </li>
            );
          })}
        </ul>
      </section>

      <section>
        <h2>{plan ? `Tu ruta de la semana ${plan.week}` : "Tu ruta de la semana"}</h2>
        {plan === undefined && <p>Cargando tu plan…</p>}
        {plan === null && diagnosed.length === 0 && <p className="hint">Tu ruta aparece aquí cuando termines los diagnósticos.</p>}
        {plan === null && diagnosed.length > 0 && diagnosed.length < AREA_ORDER.length && (
          <div className="stack">
            <p className="hint">Puedes terminar los diagnósticos que faltan o empezar ya con las áreas que llevas.</p>
            <button className="secondary" disabled={!online} onClick={() => api("/api/plan/ensure", { method: "POST" }).catch((e) => setError(e.message))}>
              Armar mi plan con lo que llevo
            </button>
          </div>
        )}
        {plan === null && diagnosed.length === AREA_ORDER.length && <p className="hint">Estamos armando tu plan…</p>}
        {plan && (
          <>
            {plan.refuerzo && <Notice>Esta semana refuerzas los mismos temas: en el cuestionario de salida anterior todavía no alcanzaste el 60 %.</Notice>}
            <p className="hint">Esta semana trabajas en: {plan.focusLabels.join("; ")}.</p>
            <ol className="route">
              {plan.sessions.map((s: any, i: number) => {
                const st = states[i];
                const local = attempts[`${plan.id}_${s.id}`] && s.status !== "hecha";
                return (
                  <li key={s.id} className={`stop ${st === "done" ? "done" : i === firstOpen ? "current" : st}`}>
                    <b>{s.title}</b>
                    <span>
                      {TYPE_LABEL[s.type]}, {s.items.length} preguntas
                      {s.status === "hecha" && `. Resultado: ${s.correct} de ${s.total}`}
                      {local && ". Hecha; pendiente de calificar"}
                      {st === "locked" && ". Se abre cuando termines las prácticas"}
                    </span>
                    {st === "open" && <Link className={i === firstOpen ? "button small" : "button small secondary"} to={`/sesion/${plan.id}/${s.id}`}>{i === firstOpen ? "Empezar" : "Abrir"}</Link>}
                  </li>
                );
              })}
            </ol>
          </>
        )}
      </section>

      {sims.length > 0 && (
        <section>
          <h2>Simulacro general</h2>
          <p className="hint">Igual para todos los estudiantes, con tiempo y sin ayudas. Sus preguntas no se repiten en tus prácticas.</p>
          <ul className="areas">
            {sims.map((s) => (
              <li key={s.id}>
                <span className="area-name">{s.title} <small>{s.questions} preguntas, {s.minutes} minutos</small></span>
                {online ? <Link className="button small secondary" to={`/simulacro/${s.id}`}>{s.submitted ? "Ver resultado" : s.startedAt ? "Continuar" : "Presentar"}</Link> : <small>Necesitas conexión</small>}
              </li>
            ))}
          </ul>
        </section>
      )}

      {overview && Object.keys(overview.mastery || {}).length > 0 && catalog && (
        <details className="mastery">
          <summary>Ver mi dominio por competencia</summary>
          {AREA_ORDER.filter((a) => diagnosed.includes(a)).map((a) => (
            <div key={a} className="mastery-area">
              <h3>{AREAS[a].name}</h3>
              {Object.entries<any>(catalog.areas[a].competencias).map(([c, info]) => (
                <Bar key={c} label={info.label} value={overview.mastery[`${a}.${c}`]} />
              ))}
            </div>
          ))}
        </details>
      )}
    </Shell>
  );
}
