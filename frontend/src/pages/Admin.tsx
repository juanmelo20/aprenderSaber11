import { FormEvent, useEffect, useState } from "react";
import { api, AREA_ORDER, AREAS } from "../lib";
import { CopyLink, Notice, Shell } from "../ui";

const inAYear = () => new Date(Date.now() + 330 * 864e5).toISOString().slice(0, 10);

function toCsv(rows: any[]) {
  const cols = Array.from(new Set(rows.flatMap((r) => Object.keys(r))));
  const esc = (v: any) => (v == null ? "" : /[",\n;]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : String(v));
  return [cols.join(";"), ...rows.map((r) => cols.map((c) => esc(r[c])).join(";"))].join("\n");
}

export default function Admin() {
  const [insts, setInsts] = useState<any[]>([]);
  const [people, setPeople] = useState<any[]>([]);
  const [stats, setStats] = useState<any>(null);
  const [msg, setMsg] = useState<{ kind: "ok" | "error"; text: string; link?: string } | null>(null);
  const [form, setForm] = useState({ name: "", municipality: "", seats: 30, expires: inAYear(), adminEmail: "", adminName: "" });
  const [draftArea, setDraftArea] = useState("LEC");
  const [drafting, setDrafting] = useState(false);
  const [lic, setLic] = useState({ email: "", plan: "mensual", expires: new Date(Date.now() + 30 * 864e5).toISOString().slice(0, 10) });

  const load = () => {
    api("/api/admin/institutions").then(setInsts).catch((e) => setMsg({ kind: "error", text: e.message }));
    api("/api/admin/particulares").then(setPeople).catch(() => undefined);
    api("/api/admin/items/stats").then(setStats).catch(() => undefined);
  };
  useEffect(load, []);

  async function run(fn: () => Promise<any>, ok: (r: any) => { text: string; link?: string }) {
    try {
      const r = await fn();
      setMsg({ kind: "ok", ...ok(r) });
      load();
    } catch (e: any) {
      setMsg({ kind: "error", text: e.message });
    }
  }

  const createInst = (e: FormEvent) => {
    e.preventDefault();
    run(() => api("/api/admin/institutions", { body: { ...form, seats: Number(form.seats) } }),
      (r) => ({ text: `Institución creada. Comparte el enlace de activación con ${form.adminName}.`, link: r.activationLink }));
  };
  const grant = (e: FormEvent) => {
    e.preventDefault();
    run(() => api("/api/admin/licenses", { body: lic }), () => ({ text: `Plan activado para ${lic.email}.` }));
  };

  async function exportCsv() {
    const { rows } = await api("/api/admin/research/export");
    const url = URL.createObjectURL(new Blob(["﻿" + toCsv(rows)], { type: "text/csv;charset=utf-8" }));
    Object.assign(document.createElement("a"), { href: url, download: "datos-investigacion-anonimos.csv" }).click();
    URL.revokeObjectURL(url);
  }

  return (
    <Shell wide>
      <h1>Administración</h1>
      {msg && <Notice kind={msg.kind}>{msg.text} <CopyLink url={msg.link} label="enlace" /></Notice>}

      <section>
        <h2>Instituciones</h2>
        {insts.length === 0 ? <p className="hint">Aún no hay instituciones. Crea la primera con el formulario.</p> : (
          <div className="table-wrap">
            <table className="table">
              <thead><tr><th>Institución</th><th>Municipio</th><th>Cupos usados</th><th>Vigente hasta</th></tr></thead>
              <tbody>{insts.map((i) => <tr key={i.id}><td>{i.name}</td><td>{i.municipality}</td><td>{i.seatsUsed} de {i.licenseSeats}</td><td>{new Date(i.licenseExpires).toLocaleDateString("es-CO")}</td></tr>)}</tbody>
            </table>
          </div>
        )}
        <form onSubmit={createInst} className="stack form-box">
          <h3>Crear institución y licencia</h3>
          <div className="row">
            <label>Nombre de la institución<input value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} required minLength={3} /></label>
            <label>Municipio<input value={form.municipality} onChange={(e) => setForm({ ...form, municipality: e.target.value })} required /></label>
          </div>
          <div className="row">
            <label>Cupos de estudiantes
              <select value={form.seats} onChange={(e) => setForm({ ...form, seats: Number(e.target.value) })}>{[10, 30, 50, 100].map((n) => <option key={n}>{n}</option>)}</select>
            </label>
            <label>Vigente hasta<input type="date" value={form.expires} onChange={(e) => setForm({ ...form, expires: e.target.value })} required /></label>
          </div>
          <div className="row">
            <label>Nombre de quien administra en el colegio<input value={form.adminName} onChange={(e) => setForm({ ...form, adminName: e.target.value })} required /></label>
            <label>Su correo<input type="email" value={form.adminEmail} onChange={(e) => setForm({ ...form, adminEmail: e.target.value })} required /></label>
          </div>
          <button>Crear institución</button>
        </form>
      </section>

      <section>
        <h2>Usuarios individuales</h2>
        {people.length > 0 && (
          <div className="table-wrap">
            <table className="table">
              <thead><tr><th>Nombre</th><th>Correo</th><th>Autorización</th><th>Plan</th></tr></thead>
              <tbody>{people.map((p) => (
                <tr key={p.uid}><td>{p.name}</td><td>{p.email}</td><td>{p.consent ? "Sí" : "Pendiente"}</td>
                  <td>{p.license ? `${p.license.plan}, hasta ${new Date(p.license.expires).toLocaleDateString("es-CO")}` : "Sin plan"}</td></tr>
              ))}</tbody>
            </table>
          </div>
        )}
        <form onSubmit={grant} className="stack form-box">
          <h3>Activar plan individual (tras recibir el pago)</h3>
          <div className="row">
            <label>Correo del usuario<input type="email" value={lic.email} onChange={(e) => setLic({ ...lic, email: e.target.value })} required /></label>
            <label>Plan<select value={lic.plan} onChange={(e) => setLic({ ...lic, plan: e.target.value })}><option value="mensual">Mensual ($19.900)</option><option value="pase">Pase hasta el examen ($89.000)</option></select></label>
            <label>Vigente hasta<input type="date" value={lic.expires} onChange={(e) => setLic({ ...lic, expires: e.target.value })} required /></label>
          </div>
          <button>Activar plan</button>
        </form>
      </section>

      <section>
        <h2>Banco de preguntas</h2>
        {stats && (
          <div className="table-wrap">
            <table className="table">
              <thead><tr><th>Área</th><th>Diagnóstico</th><th>Práctica</th><th>Simulacro</th><th>Familias que generan variantes</th><th>Aprobadas por docentes</th></tr></thead>
              <tbody>
                {AREA_ORDER.map((a) => {
                  const s = stats.byArea[a] || {};
                  const sum = (pool: string) => Object.entries<number>(s).filter(([k]) => k.startsWith(pool + "/") && !k.endsWith("/descartado")).reduce((t, [, v]) => t + v, 0);
                  const published = Object.entries<number>(s).filter(([k]) => k.endsWith("/publicado")).reduce((t, [, v]) => t + v, 0);
                  return <tr key={a}><td>{AREAS[a].name}</td><td>{sum("diagnostico")}</td><td>{sum("practica")}</td><td>{sum("simulacro")}</td><td>{stats.familiesByArea?.[a] || 0}</td><td>{published}</td></tr>;
                })}
              </tbody>
            </table>
          </div>
        )}
        <p className="hint">Una familia es una plantilla que produce preguntas nuevas cada vez (otros números, otras frases), así que esa práctica no se repite. Las preguntas de lectura no se pueden generar así: su banco crece escribiendo más. Todo entra en borrador y debe aprobarlo un docente del área antes del uso real.</p>
        <button className="secondary" onClick={() => run(() => api("/api/admin/items/seed", { method: "POST" }), (r) => ({ text: `Banco cargado: ${r.written} preguntas escritas, ${r.skipped} ya revisadas sin tocar.` }))}>Cargar o actualizar banco semilla</button>
        <div className="form-box stack">
          <h3>Redactar borradores con IA</h3>
          <p className="hint">El modelo escribe un texto o caso nuevo con cuatro preguntas para la competencia que menos preguntas tiene en el área. Quedan en borrador: ningún estudiante las ve hasta que un docente las revisa y aprueba.</p>
          <div className="row">
            <label>Área<select value={draftArea} onChange={(e) => setDraftArea(e.target.value)}>{AREA_ORDER.map((a) => <option key={a} value={a}>{AREAS[a].name}</option>)}</select></label>
            <button className="secondary" disabled={drafting} onClick={async () => {
              setDrafting(true);
              await run(() => api(`/api/admin/items/draft/${draftArea}`, { method: "POST" }), (r) => ({ text: `${r.created} borradores creados para "${r.competencia}". Ya están en la bandeja de revisión del docente del área.` }));
              setDrafting(false);
            }}>{drafting ? "Redactando…" : "Redactar 4 borradores"}</button>
          </div>
        </div>
      </section>

      <section>
        <h2>Datos para la investigación</h2>
        <p className="hint">Exporta el avance de todos los estudiantes sin nombres ni correos: cada fila lleva un identificador anónimo.</p>
        <button className="secondary" onClick={exportCsv}>Descargar datos anónimos (CSV)</button>
      </section>
    </Shell>
  );
}
