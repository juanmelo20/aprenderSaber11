import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Admin from "./pages/Admin";
import Consent from "./pages/Consent";
import Diagnostic from "./pages/Diagnostic";
import Gate from "./pages/Gate";
import Institution from "./pages/Institution";
import Login from "./pages/Login";
import Practice from "./pages/Practice";
import Simulacro from "./pages/Simulacro";
import StudentHome from "./pages/StudentHome";
import Teacher from "./pages/Teacher";
import { SessionProvider, useSession } from "./session";
import { Notice, Shell } from "./ui";

function Home() {
  const { profile } = useSession();
  if (profile.role === "admin") return <Admin />;
  if (profile.role === "institucion") return <Institution />;
  if (profile.role === "docente") return <Teacher />;
  return profile.access?.ok ? <StudentHome /> : <Gate />;
}

function Private() {
  const { user, profile, loading, error, refresh } = useSession();
  if (loading) return <Shell><p>Cargando…</p></Shell>;
  if (!user) return <Login />;
  if (!profile)
    return (
      <Shell>
        <Notice kind="error">{error || "No se pudo cargar tu perfil."}</Notice>
        <button onClick={refresh}>Intentar de nuevo</button>
      </Shell>
    );
  const learner = profile.role === "estudiante" || profile.role === "particular";
  const ready = learner && profile.access?.ok;
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      {ready && <Route path="/diagnostico/:area" element={<Diagnostic />} />}
      {ready && <Route path="/sesion/:planId/:sessionId" element={<Practice />} />}
      {ready && <Route path="/simulacro/:simId" element={<Simulacro />} />}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <SessionProvider>
        <Routes>
          <Route path="/autorizacion/:token" element={<Consent />} />
          <Route path="/*" element={<Private />} />
        </Routes>
      </SessionProvider>
    </BrowserRouter>
  );
}
