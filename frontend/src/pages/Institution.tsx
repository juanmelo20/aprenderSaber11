import { FormEvent, useEffect, useState } from "react";
import { api, AREA_ORDER, AREAS } from "../lib";
import { CopyLink, Notice, Shell } from "../ui";
import { AreaOverview } from "./Teacher";

function parseStudents(text: string) {
  return text.split("\n").map((l) => l.trim()).filter(Boolean).map((line) => {
    const [name = "", email = "", grade = "11", group = "A", adult = "", guardianEmail = ""] = line.split(/[;,\t]/).map((c) => c.trim());
    return { name, email, grade: grade || "11", group: group || "A", adult: /^(s|si|sí|x|1)$/i.test(adult), guardianEmail: guardianEmail || null };
  });
}

export default function Institution() {
  const [inst, setInst] = useState<any>(null);
  const [view, setView] = useState<"personas" | "resultados">("personas");
  const [error, setError] = useState("");
  const [text, setText] = useState("");
  const [results, setResults] = useState<any[] | null>(null);
  const [teacher, setTeacher] = useState({ name: "", email: "", areas: [] as string[] });
  const [teacherLink, setTeacherLink] = useState("");
  const [links, setLinks] = useState<Record<string, any>>({});
  const [busy, setBusy] = useState(false);

  const load = () => api("/api/institution").then(setInst).catch((e) => setError(e.message));
  useEffect(() => {
    load();
  }, []);

  async function addStudents(e: FormEvent) {
    e.preventDefault();
    setBusy(true);
    setError("");
    try {
      const r = await api("/api/institution/students", { body: { students: parseStudents(text) } });
      setResults(r.results);
      if (r.results.every((x: any) => x.ok)) setText("");
      load();
    } catch (err: any) {
      setError(err.message);
    }
    setBusy(false);
  }

  async function addTeacher(e: FormEvent) {
    e.preventDefault();
    setError("");
    try {
      const r = await api("/api/institution/teachers", { body: teacher });
      setTeacherLink(r.activationLink || "");
      setTeacher({ name: "", email: "", areas: [] });
      load();
    } catch (err: any) {
      setError(err.message);
    }
  }

  if (!inst) return <Shell wide>{error ? <Notice kind="error">{error}</Notice> : <p>Cargando…</p>}</Shell>;
  const free = inst.licenseSeats - inst.seatsUsed;
  const teacherName = (uid: string) => inst.teachers.find((t: any) => t.uid === uid)?.name;

  return (
    <Shell wide>
      <h1>{inst.name}</h1>
      <p className="hint">Licencia para {inst.licenseSeats} estudiantes, vigente hasta el {new Date(inst.licenseExpires).toLocaleDateString("es-CO")}. <mark>{free} cupos libres</mark></p>
      <div className="tabs main-tabs">
        <button className={view === "personas" ? "tab on" : "tab"} onClick={() => setView("personas")}>Docentes y estudiantes</button>
        <button className={view === "resultados" ? "tab on" : "tab"} onClick={() => setView("resultados")}>Resultados por área</button>
      </div>
      {error && <Notice kind="error">{error}</Notice>}

      {view === "resultados" && <AreaOverview areas={[...AREA_ORDER]} />}

      {view === "personas" && (
        <>
          <section>
            <h2>Docente responsable de cada área</h2>
            <ul className="areas">
              {AREA_ORDER.map((a) => <li key={a}><span className="area-name">{AREAS[a].name}</span><span>{teacherName(inst.teacherByArea?.[a]) || <small>sin asignar</small>}</span></li>)}
            </ul>
            <form onSubmit={addTeacher} className="stack form-box">
              <h3>Asignar o actualizar un docente</h3>
              <div className="row">
                <label>Nombre<input value={teacher.name} onChange={(e) => setTeacher({ ...teacher, name: e.target.value })} required /></label>
                <label>Correo<input type="email" value={teacher.email} onChange={(e) => setTeacher({ ...teacher, email: e.target.value })} required /></label>
              </div>
              <fieldset><legend>Áreas a su cargo</legend>
                {AREA_ORDER.map((a) => (
                  <label key={a} className="check"><input type="checkbox" checked={teacher.areas.includes(a)}
                    onChange={(e) => setTeacher({ ...teacher, areas: e.target.checked ? [...teacher.areas, a] : teacher.areas.filter((x) => x !== a) })} />{AREAS[a].name}</label>
                ))}
              </fieldset>
              <button disabled={teacher.areas.length === 0}>Guardar docente</button>
              {teacherLink && <Notice kind="ok">Docente guardado. Puede activar su cuenta desde "Activar mi cuenta" en la pantalla de entrada, o con este enlace: <CopyLink url={teacherLink} label="enlace de activación" /></Notice>}
            </form>
          </section>

          <section>
            <h2>Registrar estudiantes</h2>
            <form onSubmit={addStudents} className="stack form-box">
              <label>Un estudiante por línea: nombre, correo, grado, grupo, mayor de edad (sí o no), correo del acudiente (opcional)
                <textarea rows={5} value={text} onChange={(e) => setText(e.target.value)} placeholder={"Ana Pérez, ana@correo.com, 11, A, no, mama@correo.com\nLuis Rojas, luis@correo.com, 11, A, sí"} required />
              </label>
              <button disabled={busy || free <= 0}>{free <= 0 ? "No quedan cupos" : "Registrar"}</button>
            </form>
            {results && (
              <div className="table-wrap">
                <table className="table">
                  <thead><tr><th>Estudiante</th><th>Resultado</th><th>Enlaces para compartir</th></tr></thead>
                  <tbody>
                    {results.map((r, i) => (
                      <tr key={i}>
                        <td>{r.name || r.email}</td>
                        <td className={r.ok ? "cell high" : "cell low"}>{r.ok ? "Registrado" : r.error}</td>
                        <td>{r.ok && <><CopyLink url={r.activationLink} label="activación" /> {r.consentLink ? <CopyLink url={r.consentLink} label="autorización del acudiente" /> : "Mayor de edad: autoriza al entrar"}</>}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </section>

          <section>
            <h2>Estudiantes registrados</h2>
            {inst.students.length === 0 ? <p className="hint">Aún no hay estudiantes. Regístrelos con el formulario de arriba.</p> : (
              <div className="table-wrap">
                <table className="table">
                  <thead><tr><th>Nombre</th><th>Correo</th><th>Grupo</th><th>Autorización de datos</th><th></th></tr></thead>
                  <tbody>
                    {inst.students.map((s: any) => (
                      <tr key={s.uid}>
                        <td>{s.name}</td><td>{s.email}</td><td>{s.grade}{s.group}</td>
                        <td className={s.consent ? "cell high" : "cell mid"}>{s.consent ? "Autorizado" : "Pendiente"}</td>
                        <td>
                          {links[s.uid] ? <><CopyLink url={links[s.uid].activationLink} label="activación" /> {!s.consent && <CopyLink url={links[s.uid].consentLink} label="autorización" />}</>
                            : <button className="link" onClick={async () => setLinks({ ...links, [s.uid]: await api(`/api/institution/students/${s.uid}/consent-link`, { method: "POST" }) })}>Generar enlaces</button>}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </section>
        </>
      )}
    </Shell>
  );
}
