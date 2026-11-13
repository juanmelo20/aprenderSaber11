import { onAuthStateChanged, signOut, User } from "firebase/auth";
import { createContext, ReactNode, useCallback, useContext, useEffect, useState } from "react";
import { api, auth, cacheGet, cacheSet } from "./lib";

type Ctx = { user: User | null; profile: any; loading: boolean; error: string; refresh: () => Promise<void>; logout: () => void };
const SessionCtx = createContext<Ctx>(null as any);
export const useSession = () => useContext(SessionCtx);

export function SessionProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [profile, setProfile] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const load = useCallback(async (u: User | null) => {
    if (!u) {
      setProfile(null);
      setLoading(false);
      return;
    }
    const key = `perfil:${u.uid}`;
    try {
      const me = await api("/api/me");
      cacheSet(key, me);
      setProfile(me);
      setError("");
    } catch (e: any) {
      const cached = cacheGet<any>(key); // sin conexión: se usa el último perfil conocido
      if (cached) setProfile(cached);
      else setError(e.status ? e.message : "No hay conexión con el servidor. Revisa tu señal e intenta de nuevo.");
    }
    setLoading(false);
  }, []);

  useEffect(
    () =>
      onAuthStateChanged(auth, (u) => {
        setUser(u);
        setLoading(true);
        load(u);
      }),
    [load],
  );

  return (
    <SessionCtx.Provider value={{ user, profile, loading, error, refresh: () => load(auth.currentUser), logout: () => signOut(auth) }}>
      {children}
    </SessionCtx.Provider>
  );
}

export function useOnline() {
  const [online, setOnline] = useState(navigator.onLine);
  useEffect(() => {
    const on = () => setOnline(true);
    const off = () => setOnline(false);
    window.addEventListener("online", on);
    window.addEventListener("offline", off);
    return () => {
      window.removeEventListener("online", on);
      window.removeEventListener("offline", off);
    };
  }, []);
  return online;
}
