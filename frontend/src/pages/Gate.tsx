import { useState } from "react";
import { api } from "../lib";
import { useSession } from "../session";
import { CopyLink, Notice, Shell } from "../ui";
import { Policy } from "./Consent";

/** Pantalla para quien todavía no puede estudiar: falta autorización o licencia. */
export default function Gate() {
  const { profile, refresh } = useSession();
  const reason = profile.access?.reason;
  const [adult, setAdult] = useState(false);
  const [accept, setAccept] = useState(false);
  const [link, setLink] = useState("");
  const [error, setError] = useState("");
  const canSelfConsent = profile.role === "particular" || profile.adult;

  async function selfConsent() {
    try {
      await api("/api/me/consent", { body: { declaresAdult: adult, accept } });
      await refresh();
    } catch (e: any) {
      setError(e.message);
    }
  }

  return (
    <Shell>
      {reason === "consentimiento" && (
        <div className="stack">
          <h1>Falta la autorización de datos</h1>
          {!canSelfConsent && (
            <>
              <p>Tu colegio te registró como menor de edad. Tu mamá, papá o acudiente debe abrir el enlace de autorización que le entregó el colegio. Cuando lo haga, vuelve a entrar.</p>
              <button onClick={refresh}>Ya autorizaron: revisar de nuevo</button>
            </>
          )}
          {canSelfConsent && (
            <>
              <Policy />
              <label className="check"><input type="checkbox" checked={adult} onChange={(e) => setAdult(e.target.checked)} /> Soy mayor de edad (18 años o más).</label>
              <label className="check"><input type="checkbox" checked={accept} onChange={(e) => setAccept(e.target.checked)} /> Autorizo el tratamiento de mis datos como se describe arriba.</label>
              <button disabled={!adult || !accept} onClick={selfConsent}>Autorizar y continuar</button>
              {profile.role === "particular" && (
                <div className="aside">
                  <p>Si eres menor de edad, debe autorizar tu acudiente. Genera el enlace y envíaselo:</p>
                  <button className="secondary" onClick={async () => setLink((await api("/api/me/consent-link", { method: "POST" })).link)}>Generar enlace para mi acudiente</button>
                  {link && <p className="mono-wrap">{link} <CopyLink url={link} label="enlace" /></p>}
                </div>
              )}
            </>
          )}
        </div>
      )}
      {reason === "licencia" && (
        <div className="stack">
          <h1>Tu cuenta está lista; falta activar tu plan</h1>
          <p>Elige un plan y escribe al administrador para activarlo. Apenas quede activo podrás hacer tu diagnóstico.</p>
          <ul className="plans">
            <li><b>Mensual</b><span>$19.900 al mes</span></li>
            <li><b>Pase hasta el examen</b><span>$89.000, un solo pago</span></li>
          </ul>
          <button onClick={refresh}>Ya lo activaron: revisar de nuevo</button>
        </div>
      )}
      {reason === "licencia_institucion" && (
        <div className="stack">
          <h1>La licencia de tu colegio no está activa</h1>
          <p>Avísale a tu docente o a la coordinación. Tu avance está guardado y lo recuperas cuando el colegio renueve.</p>
          <button onClick={refresh}>Revisar de nuevo</button>
        </div>
      )}
      {error && <Notice kind="error">{error}</Notice>}
    </Shell>
  );
}
