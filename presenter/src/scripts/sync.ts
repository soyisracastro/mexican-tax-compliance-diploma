/**
 * Sincronización dual-screen vía BroadcastChannel.
 *
 * Cada deck tiene su propio canal (`deck-sync:<slug>`) para que varias clases
 * abiertas en pestañas distintas no se crucen mensajes.
 *
 * Fallback: `localStorage` + evento `storage` para navegadores sin BroadcastChannel.
 */

export type SyncMessage =
  | { type: "goto"; slideIndex: number; source?: string }
  | { type: "announce-ready"; source: string }
  | { type: "request-state"; source: string };

export interface SyncAPI {
  post: (msg: SyncMessage) => void;
  onMessage: (handler: (msg: SyncMessage) => void) => () => void;
  close: () => void;
}

export function createSync(deckSlug: string): SyncAPI {
  const channelName = `deck-sync:${deckSlug}`;
  const storageKey = `${channelName}:last`;

  const useBC = typeof BroadcastChannel !== "undefined";
  const bc = useBC ? new BroadcastChannel(channelName) : null;

  const listeners = new Set<(m: SyncMessage) => void>();

  const emit = (msg: SyncMessage) => {
    for (const l of listeners) l(msg);
  };

  if (bc) {
    bc.onmessage = (e) => emit(e.data as SyncMessage);
  }

  // Fallback: escuchar cambios de localStorage desde otras pestañas
  const onStorage = (e: StorageEvent) => {
    if (e.key !== storageKey || !e.newValue) return;
    try {
      const parsed = JSON.parse(e.newValue);
      emit(parsed as SyncMessage);
    } catch {
      /* ignore */
    }
  };
  if (typeof window !== "undefined") {
    window.addEventListener("storage", onStorage);
  }

  return {
    post(msg) {
      if (bc) bc.postMessage(msg);
      // Siempre escribir a localStorage como persistencia de estado
      try {
        localStorage.setItem(storageKey, JSON.stringify(msg));
      } catch {
        /* ignore quota */
      }
    },
    onMessage(handler) {
      listeners.add(handler);
      return () => listeners.delete(handler);
    },
    close() {
      listeners.clear();
      if (bc) bc.close();
      if (typeof window !== "undefined") {
        window.removeEventListener("storage", onStorage);
      }
    },
  };
}

/**
 * Lee el último mensaje persistido (para recuperar estado al abrir una nueva vista).
 */
export function readPersistedSlide(deckSlug: string): number | null {
  if (typeof localStorage === "undefined") return null;
  try {
    const raw = localStorage.getItem(`deck-sync:${deckSlug}:last`);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    if (parsed?.type === "goto" && typeof parsed.slideIndex === "number") {
      return parsed.slideIndex;
    }
  } catch {
    /* ignore */
  }
  return null;
}
