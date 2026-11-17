import { initializeApp } from "firebase/app";
import { connectAuthEmulator, getAuth } from "firebase/auth";
import { connectFirestoreEmulator, initializeFirestore, persistentLocalCache, persistentMultipleTabManager } from "firebase/firestore";

const env = import.meta.env;
export const APP_NAME: string = env.VITE_APP_NAME || "Rumbo 11";
const onThisComputer = ["localhost", "127.0.0.1"].includes(location.hostname);
// Los emuladores solo tienen sentido cuando la web corre en el mismo computador que los emuladores.
export const usingEmulators = onThisComputer && (env.VITE_USE_EMULATORS === "true" || !env.VITE_FIREBASE_API_KEY);
const useEmulators = usingEmulators;

const app = initializeApp({
  apiKey: env.VITE_FIREBASE_API_KEY || "demo",
  authDomain: env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: env.VITE_FIREBASE_PROJECT_ID || "demo-rumbo11",
  appId: env.VITE_FIREBASE_APP_ID,
});

export const auth = getAuth(app);
// Caché persistente: el plan y los cuestionarios quedan guardados en el dispositivo y los
// intentos se envían solos cuando vuelve la conexión.
export const db = initializeFirestore(app, {
  localCache: persistentLocalCache({ tabManager: persistentMultipleTabManager() }),
});

if (useEmulators) {
  connectAuthEmulator(auth, "http://127.0.0.1:9099", { disableWarnings: true });
  connectFirestoreEmulator(db, "127.0.0.1", 8080);
}

const BASE: string = env.VITE_API_URL || "http://127.0.0.1:8000";

export async function api(path: string, opts: { method?: string; body?: unknown } = {}): Promise<any> {
  const token = auth.currentUser ? await auth.currentUser.getIdToken() : null;
  const res = await fetch(BASE + path, {
    method: opts.method || (opts.body ? "POST" : "GET"),
    headers: { "Content-Type": "application/json", ...(token ? { Authorization: `Bearer ${token}` } : {}) },
    body: opts.body ? JSON.stringify(opts.body) : undefined,
  });
  if (!res.ok) {
    let detail: any;
    try {
      detail = (await res.json()).detail;
    } catch {
      /* respuesta sin cuerpo */
    }
    const message = typeof detail === "string" ? detail : detail?.message || `No se pudo completar la acción (${res.status}).`;
    throw Object.assign(new Error(message), { status: res.status, code: detail?.code });
  }
  return res.json();
}

export const AREA_ORDER = ["LEC", "MAT", "SOC", "NAT", "ING"] as const;
export const AREAS: Record<string, { name: string; short: string }> = {
  LEC: { name: "Lectura Crítica", short: "Lectura" },
  MAT: { name: "Matemáticas", short: "Matemáticas" },
  SOC: { name: "Sociales y Ciudadanas", short: "Sociales" },
  NAT: { name: "Ciencias Naturales", short: "Naturales" },
  ING: { name: "Inglés", short: "Inglés" },
};

export function cacheGet<T>(key: string): T | null {
  try {
    return JSON.parse(localStorage.getItem(key) || "null");
  } catch {
    return null;
  }
}
export function cacheSet(key: string, value: unknown) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch {
    /* almacenamiento lleno o bloqueado */
  }
}

export function authMessage(code: string): string {
  const map: Record<string, string> = {
    "auth/invalid-credential": "Correo o contraseña incorrectos.",
    "auth/wrong-password": "Correo o contraseña incorrectos.",
    "auth/user-not-found": "No hay una cuenta con ese correo.",
    "auth/email-already-in-use": "Ya existe una cuenta con ese correo. Entra o usa 'Activar mi cuenta'.",
    "auth/weak-password": "La contraseña debe tener al menos 6 caracteres.",
    "auth/invalid-email": "Escribe un correo válido.",
    "auth/network-request-failed": "No hay conexión. Intenta de nuevo cuando tengas señal.",
    "auth/too-many-requests": "Demasiados intentos seguidos. Espera unos minutos e intenta de nuevo.",
  };
  if (code === "auth/network-request-failed" && navigator.onLine) {
    return usingEmulators
      ? "No responden los emuladores de Firebase. Enciéndelos con 'npm run emuladores' o publica la web con 'npm run desplegar:web'."
      : "No se pudo conectar con el servicio de cuentas. Recarga la página con Ctrl + Shift + R. Si sigue igual, desactiva el bloqueador de anuncios para este sitio.";
  }
  return map[code] || "No se pudo completar. Intenta de nuevo.";
}
