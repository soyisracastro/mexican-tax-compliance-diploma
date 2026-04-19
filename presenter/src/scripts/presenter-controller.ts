/**
 * Controlador de estado cliente-side para una vista del deck.
 *
 * Maneja:
 *   - Índice actual (0-based)
 *   - Navegación prev/next/goto/first/last
 *   - Keybindings globales
 *   - Broadcast vía sync API
 *
 * Se inyecta como módulo cliente en cada vista (presenter, notes, overview).
 */

import { createSync, type SyncAPI } from "./sync";

export interface ControllerOptions {
  deckSlug: string;
  totalSlides: number;
  /** Llamado cada vez que cambia el índice (incluye la carga inicial). */
  onChange: (index: number) => void;
  /** Fuente identificadora para debug, ej. "presenter", "notes", "overview". */
  viewName: string;
  /** Si está en `notes`, las flechas ↑↓ desplazan el script, no cambian de slide. */
  role?: "presenter" | "notes" | "overview";
}

export interface Controller {
  current: () => number;
  goto: (i: number) => void;
  next: () => void;
  prev: () => void;
  first: () => void;
  last: () => void;
  destroy: () => void;
  sync: SyncAPI;
}

export function createController(opts: ControllerOptions): Controller {
  const { deckSlug, totalSlides, onChange, viewName, role = "presenter" } = opts;

  // Estado inicial: lee de URL ?slide=N, luego de localStorage, luego 0
  let index = initialIndex(totalSlides);

  const sync = createSync(deckSlug);

  // Escuchar cambios remotos (emitidos por otras vistas)
  const unsubscribe = sync.onMessage((msg) => {
    if (msg.type === "goto" && msg.source !== viewName) {
      if (msg.slideIndex !== index) {
        index = clamp(msg.slideIndex, 0, totalSlides - 1);
        updateUrl(index);
        onChange(index);
      }
    }
  });

  // Anunciar estado actual a cualquier vista que se conecte después
  setTimeout(() => sync.post({ type: "goto", slideIndex: index, source: viewName }), 0);

  const broadcast = () => {
    sync.post({ type: "goto", slideIndex: index, source: viewName });
  };

  const set = (i: number) => {
    const next = clamp(i, 0, totalSlides - 1);
    if (next === index) return;
    index = next;
    updateUrl(index);
    onChange(index);
    broadcast();
  };

  const goto = (i: number) => set(i);
  const next = () => set(index + 1);
  const prev = () => set(index - 1);
  const first = () => set(0);
  const last = () => set(totalSlides - 1);

  // Keybindings
  const onKey = (e: KeyboardEvent) => {
    // Ignorar si el usuario está escribiendo en un input/textarea
    const target = e.target as HTMLElement | null;
    if (target && (target.tagName === "INPUT" || target.tagName === "TEXTAREA" || target.isContentEditable)) {
      return;
    }

    switch (e.key) {
      case "ArrowRight":
      case "PageDown":
      case " ":
        e.preventDefault();
        next();
        break;
      case "ArrowLeft":
      case "PageUp":
        e.preventDefault();
        prev();
        break;
      case "Home":
        e.preventDefault();
        first();
        break;
      case "End":
        e.preventDefault();
        last();
        break;
      case "n":
      case "N":
        // Abre la vista de notas en nueva pestaña
        openView("notes", deckSlug, index);
        break;
      case "p":
      case "P":
        // Abre la vista de presenter en nueva pestaña
        openView("presenter", deckSlug, index);
        break;
      case "o":
      case "O":
        openView("overview", deckSlug, index);
        break;
      case "Escape":
        if (role === "overview") {
          openView("presenter", deckSlug, index, true);
        }
        break;
    }
  };

  window.addEventListener("keydown", onKey);

  // Render inicial
  onChange(index);

  return {
    current: () => index,
    goto,
    next,
    prev,
    first,
    last,
    sync,
    destroy: () => {
      window.removeEventListener("keydown", onKey);
      unsubscribe();
      sync.close();
    },
  };
}

function clamp(n: number, min: number, max: number): number {
  return Math.max(min, Math.min(max, n));
}

function initialIndex(total: number): number {
  // 1. URL param ?slide=N (1-based para humanos, 0-based interno)
  const params = new URLSearchParams(window.location.search);
  const fromUrl = params.get("slide");
  if (fromUrl) {
    const n = parseInt(fromUrl, 10) - 1;
    if (!isNaN(n) && n >= 0 && n < total) return n;
  }
  return 0;
}

function updateUrl(index: number) {
  const url = new URL(window.location.href);
  url.searchParams.set("slide", String(index + 1));
  window.history.replaceState(null, "", url.toString());
}

function openView(view: "presenter" | "notes" | "overview", slug: string, slideIndex: number, sameTab = false) {
  const url = `/${view}/${slug}?slide=${slideIndex + 1}`;
  if (sameTab) window.location.href = url;
  else window.open(url, `_${view}_${slug}`);
}
