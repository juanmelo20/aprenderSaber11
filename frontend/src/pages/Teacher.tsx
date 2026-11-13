import { useEffect, useState } from "react";
import { api, AREA_ORDER, AREAS } from "../lib";
import { useSession } from "../session";
import { Bar, Notice, Shell } from "../ui";

export function AreaOverview({ areas }: { areas: string[] }) {
  const [area, setArea] = useState(areas[0]);
  const [group, setGroup] = useState("");
  const [data, setData] = useState<any>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    setData(null);
    api(`/api/teacher/overview?area=${area}${group ? `&group=${encodeURIComponent(group)}` : ""}`).then(setData).catch((e) => setError(e.message));
  }, [area, group]);

  return (
    <>
      <div className="tabs" role="tablist">
        {areas.map((a) => <button key={a} role="tab" aria-selected={a === area} className={a === area ? "tab on" : "tab"} onClick={() => setArea(a)}>{AREAS[a].name}</button>)}
      </div>
      {error && <Notice kind="error">{error}</Notice>}
      {!data && !error && <p>Cargando…</p>}
      {data && (
        <>
          <div className="row between">
            <p className="hint">{data.diagnosed} de {data.students.length} estudiantes ya hicieron el diagnóstico de {data.areaName}.</p>
            <label className="inline">Grupo
              <select value={group} onChange={(e) => setGroup(e.target.value)}>
                <option value="">Todos</option>
                {data.groups.map((g: string) => <option key={g}>{g}</option>)}
              </select>
            </label>
          </div>

          <div className="two-col">
            <section>
              <h2>Dominio del grupo por competencia</h2>
              {data.competencias.map((c: any) => <Bar key={c.key} label={c.label} value={c.avg} />)}
              <h3>Estudiantes por nivel</h3>
              <p className="levels">
                {data.levelOrder.map((l: string) => <span key={l}><b>{data.levels[l] || 0}</b> en nivel {l}</span>)}
              </p>
            </section>
            <section>
              <h2>Qué trabajar en clase esta semana</h2>
              {data.classPlan.length === 0 && <p className="hint">Aparece cuando al menos un estudiante termine el diagnóstico.</p>}
              {data.classPlan.map((p: any) => (
                <div key={p.competencia} className="class-plan">
                  <b>{p.competencia}</b> <small>dominio promedio {Math.round(p.avg * 100)} %</small>
                  <ul>{p.tips.map((t: string) => <li key={t}>{t}</li>)}</ul>
                </div>
              ))}
            </section>
          </div>

          <section>
            <h2>Estudiantes, del que más apoyo necesita al que menos</h2>
            <div className="table-wrap">
              <table className="table">
                <thead>
                  <tr><th>Estudiante</th><th>Grupo</th><th>Nivel</th><th>Puntaje</th>
                    {data.competencias.map((c: any) => <th key={c.key}>{c.label}</th>)}<th>Semana</th><th>Sesiones</th></tr>
                </thead>
                <tbody>
                  {data.students.map((s: any) => (
                    <tr key={s.uid}>
                      <td>{s.name}</td><td>{s.group}</td><td>{s.level ?? "sin diagnóstico"}</td><td>{s.score ?? ""}</td>
                      {data.competencias.map((c: any) => {
                        const v = s.mastery[c.key];
                        return <td key={c.key} className={v == null ? "" : v < 0.4 ? "cell low" : v < 0.7 ? "cell mid" : "cell high"}>{v == null ? "" : `${Math.round(v * 100)} %`}</td>;
                      })}
                      <td>{s.week || ""}</td><td>{s.attempts || ""}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>

          {data.hardItems.length > 0 && (
            <section>
              <h2>Preguntas en las que más falla el grupo</h2>
              <ul className="plain">
                {data.hardItems.map((h: any) => <li key={h.id}><b>{h.pct} % de acierto</b> ({h.n} respuestas), {h.competencia}: {h.stem}</li>)}
              </ul>
            </section>
          )}
        </>
      )}
    </>
  );
}

function ItemReview({ areas }: { areas: string[] }) {
  const [area, setArea] = useState(areas[0]);
  const [items, setItems] = useState<any[] | null>(null);
  const [error, setError] = useState("");
  const [shown, setShown] = useState(8);
  const load = () => api(`/api/items?area=${area}&status=borrador`).then(setItems).catch((e) => setError(e.message));
  useEffect(() => {
    setItems(null);
    load();
  }, [area]); // eslint-disable-line react-hooks/exhaustive-deps

  async function decide(id: string, status: string, explanation?: string) {
    try {
      await api(`/api/items/${id}`, { method: "PATCH", body: { status, ...(explanation ? { explanation } : {}) } });
      load();
    } catch (e: any) {
      setError(e.message);
    }
  }

  return (
    <>
      <div className="tabs">
        {areas.map((a) => <button key={a} className={a === area ? "tab on" : "tab"} onClick={() => setArea(a)}>{AREAS[a].name}</button>)}
      </div>
      <p className="hint">Estas preguntas están en borrador. Revise enunciado, clave y explicación; al aprobar quedan publicadas con su nombre como revisor.</p>
      {error && <Notice kind="error">{error}</Notice>}
      {items && items.length === 0 && <p>No hay preguntas pendientes en esta área.</p>}
      {items && items.length > 0 && <p className="hint">{items.length} pendientes en esta área.</p>}
      {items?.slice(0, shown).map((it) => <ReviewCard key={it.id} item={it} onDecide={decide} />)}
      {items && items.length > shown && <button className="secondary" onClick={() => setShown(shown + 8)}>Mostrar más</button>}
    </>
  );
}

function ReviewCard({ item, onDecide }: { item: any; onDecide: (id: string, status: string, explanation?: string) => void }) {
  const [explanation, setExplanation] = useState(item.explanation);
  return (
    <div className="sheet review-card">
      <small>{item.id}, {item.competencia}, uso: {item.pool}</small>
      {item.pool === "plantilla" && <Notice>Esta pregunta es un ejemplo de una familia: al aprobarla, el sistema podrá generar variantes con otros datos y la misma estructura. Revise que el planteamiento y el procedimiento sean correctos.</Notice>}
      {item.origin === "ia" && <Notice>Borrador redactado por un modelo de lenguaje. Verifique cada dato y que solo una opción sea correcta antes de aprobar.</Notice>}
      {item.context && <p className="context">{item.context}</p>}
      <p className="stem">{item.stem}</p>
      <ul className="plain">
        {Object.keys(item.options).sort().map((k) => <li key={k} className={k === item.correct ? "key" : ""}><b>{k}.</b> {item.options[k]}{k === item.correct && " (clave)"}</li>)}
      </ul>
      <label>Explicación que verá el estudiante<textarea value={explanation} onChange={(e) => setExplanation(e.target.value)} rows={3} /></label>
      <div className="row">
        <button onClick={() => onDecide(item.id, "publicado", explanation)}>Aprobar y publicar</button>
        <button className="secondary" onClick={() => onDecide(item.id, "descartado")}>Descartar</button>
      </div>
    </div>
  );
}

export default function Teacher() {
  const { profile } = useSession();
  const areas: string[] = AREA_ORDER.filter((a) => (profile.areas || []).includes(a));
  const [view, setView] = useState<"grupo" | "preguntas">("grupo");
  return (
    <Shell wide>
      <h1>{profile.institutionName}</h1>
      <div className="tabs main-tabs">
        <button className={view === "grupo" ? "tab on" : "tab"} onClick={() => setView("grupo")}>Mi grupo</button>
        <button className={view === "preguntas" ? "tab on" : "tab"} onClick={() => setView("preguntas")}>Revisar preguntas</button>
      </div>
      {areas.length === 0 ? <Notice>La institución aún no le ha asignado un área.</Notice> : view === "grupo" ? <AreaOverview areas={areas} /> : <ItemReview areas={areas} />}
    </Shell>
  );
}
