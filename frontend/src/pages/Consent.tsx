import { FormEvent, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { api, APP_NAME } from "../lib";
import { Notice } from "../ui";

/** Texto de la autorización. Debe revisarlo un abogado antes de usarlo con familias reales. */
export function Policy({ name }: { name?: string }) {
  return (
    <div className="policy">
      <p><b>Qué datos se guardan.</b> Nombre, correo, grado y grupo; las respuestas a las preguntas y el avance en el plan de estudio{name ? ` de ${name}` : ""}.</p>
      <p><b>Para qué.</b> Para darle un plan de estudio personalizado, para que el docente de cada área vea en qué reforzar y, de forma anónima (sin nombre ni correo), para un trabajo de investigación universitario sobre la plataforma.</p>
      <p><b>Dónde quedan.</b> En servicios en la nube contratados para operar la plataforma (base de datos y servidor), que los tratan solo por encargo. Al tutor de inteligencia artificial no se le envía el nombre ni el correo del estudiante.</p>
      <p><b>Qué no se hace.</b> No se venden los datos ni se entregan a nadie para publicidad u otros fines.</p>
      <p><b>Sus derechos.</b> Puede conocer, corregir o pedir que se eliminen los datos en cualquier momento (Ley 1581 de 2012), escribiendo al colegio o al responsable de la plataforma. La autorización es voluntaria.</p>
    </div>
  );
}

export default function Consent() {
  const { token } = useParams();
  const [info, setInfo] = useState<any>(null);
  const [error, setError] = useState("");
  const [name, setName] = useState("");
  const [rel, setRel] = useState("");
  const [accept, setAccept] = useState(false);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    api(`/api/public/consent/${token}`).then(setInfo).catch((e) => setError(e.message));
  }, [token]);

  async function submit(e: FormEvent) {
    e.preventDefault();
    setBusy(true);
    setError("");
    try {
      const r = await api(`/api/public/consent/${token}`, { body: { guardianName: name, relationship: rel, accept } });
      setInfo({ ...info, status: r.status });
    } catch (err: any) {
      setError(err.message);
    }
    setBusy(false);
  }

  return (
    <div className="shell">
      <header className="top"><span className="brand">{APP_NAME}</span></header>
      <main className="page">
        {!info && !error && <p>Cargando…</p>}
        {error && <Notice kind="error">{error}</Notice>}
        {info?.status === "aceptado" && (
          <>
            <h1>Autorización registrada</h1>
            <p>Gracias. La cuenta de {info.studentFirstName} ya está activa y puede empezar su diagnóstico.</p>
          </>
        )}
        {info?.status === "pendiente" && (
          <form onSubmit={submit} className="stack">
            <h1>Autorización para {info.studentFirstName}</h1>
            <p>
              {info.institutionName ? `${info.institutionName} registró a ${info.studentFirstName}` : `${info.studentFirstName} se registró`} en {APP_NAME},
              una plataforma para preparar la prueba de Estado de grado 11. Como es menor de edad, necesitamos la autorización de su madre, padre o acudiente.
            </p>
            <Policy name={info.studentFirstName} />
            <label>Nombre completo de quien autoriza<input value={name} onChange={(e) => setName(e.target.value)} required minLength={5} /></label>
            <label>Parentesco
              <select value={rel} onChange={(e) => setRel(e.target.value)} required>
                <option value="">Selecciona…</option>
                <option>Madre</option><option>Padre</option><option>Abuela o abuelo</option><option>Otro acudiente legal</option>
              </select>
            </label>
            <label className="check"><input type="checkbox" checked={accept} onChange={(e) => setAccept(e.target.checked)} required />
              Soy representante legal de {info.studentFirstName}, le expliqué de qué se trata y escuché su opinión, y autorizo el tratamiento de sus datos como se describe arriba.</label>
            <button disabled={busy || !accept}>Autorizar</button>
          </form>
        )}
      </main>
    </div>
  );
}
