import { createUserWithEmailAndPassword, sendPasswordResetEmail, signInWithEmailAndPassword, updateProfile } from "firebase/auth";
import { FormEvent, useState } from "react";
import { APP_NAME, auth, authMessage } from "../lib";
import { Notice } from "../ui";

type Mode = "entrar" | "activar" | "crear";

export default function Login() {
  const [mode, setMode] = useState<Mode>("entrar");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [msg, setMsg] = useState<{ kind: "error" | "ok"; text: string } | null>(null);
  const [busy, setBusy] = useState(false);

  async function submit(e: FormEvent) {
    e.preventDefault();
    setBusy(true);
    setMsg(null);
    try {
      if (mode === "entrar") await signInWithEmailAndPassword(auth, email.trim(), password);
      else if (mode === "crear") {
        const cred = await createUserWithEmailAndPassword(auth, email.trim(), password);
        if (name.trim()) await updateProfile(cred.user, { displayName: name.trim() });
      } else {
        await sendPasswordResetEmail(auth, email.trim());
        setMsg({ kind: "ok", text: "Te enviamos un correo con el enlace para crear tu contraseña. Revisa también la carpeta de correo no deseado." });
      }
    } catch (err: any) {
      setMsg({ kind: "error", text: authMessage(err.code) });
    }
    setBusy(false);
  }

  return (
    <div className="login">
      <section className="login-pitch">
        <h1>{APP_NAME}</h1>
        <p className="lead">Un diagnóstico corto, un plan para cada semana y un tutor que te da pistas, no respuestas.</p>
        <ol className="route preview" aria-label="Cómo funciona">
          <li className="stop done"><b>Diagnóstico</b><span>Entre 6 y 10 preguntas por área.</span></li>
          <li className="stop current"><b>Plan de la semana</b><span>Prácticas cortas en lo que más te cuesta.</span></li>
          <li className="stop"><b>Cuestionario de salida</b><span>Sin ayudas, para medir de nuevo tu nivel.</span></li>
        </ol>
      </section>
      <form className="login-form" onSubmit={submit}>
        <h2>{mode === "entrar" ? "Entrar" : mode === "crear" ? "Crear cuenta individual" : "Activar mi cuenta"}</h2>
        {mode === "activar" && <p className="hint">Si tu colegio te registró, escribe el correo con el que te inscribieron y te enviamos el enlace para crear tu contraseña.</p>}
        {mode === "crear" && (
          <label>Nombre completo<input value={name} onChange={(e) => setName(e.target.value)} required autoComplete="name" /></label>
        )}
        <label>Correo<input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required autoComplete="email" /></label>
        {mode !== "activar" && (
          <label>Contraseña<input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required minLength={6}
            autoComplete={mode === "crear" ? "new-password" : "current-password"} /></label>
        )}
        {msg && <Notice kind={msg.kind}>{msg.text}</Notice>}
        <button disabled={busy}>{mode === "entrar" ? "Entrar" : mode === "crear" ? "Crear cuenta" : "Enviar enlace"}</button>
        <div className="login-alt">
          {mode !== "entrar" && <button type="button" className="link" onClick={() => setMode("entrar")}>Ya tengo contraseña</button>}
          {mode !== "activar" && <button type="button" className="link" onClick={() => setMode("activar")}>Activar mi cuenta u olvidé la contraseña</button>}
          {mode !== "crear" && <button type="button" className="link" onClick={() => setMode("crear")}>No estoy en un colegio: crear cuenta individual</button>}
        </div>
      </form>
    </div>
  );
}
