export interface Slide {
  /** Número que aparece en el encabezado "## SLIDE N:" (NO es el índice 0-based) */
  number: number;
  /** Título después de "SLIDE N:" */
  title: string;
  /** Contenido visual renderizado como HTML (tablas, listas, diagramas) */
  contentHtml: string;
  /** Script teleprompter renderizado como HTML (párrafos) */
  scriptHtml: string;
  /** Texto plano del script, para longitud y búsqueda */
  scriptText: string;
  /** Bloque temático al que pertenece (si aplica) */
  blockTitle: string | null;
  /** Icono Lucide del bloque, ej. "briefcase" (si aplica) */
  blockIcon: string | null;
  /** Minutos estimados para todo el bloque (si aplica) */
  blockMinutes: number | null;
  /** Minutos estimados para este slide (blockMinutes / slides del bloque) */
  estimatedMinutes: number | null;
}

export interface Deck {
  /** Slug único para URLs, ej. "modulo-04-clase-01" */
  slug: string;
  /** Ruta relativa al archivo fuente, para mostrar al usuario */
  sourcePath: string;
  /** Título principal del deck (primer H1) */
  title: string;
  /** Subtítulo (segundo H2 si existe) */
  subtitle: string | null;
  /** Duración total (leída del frontmatter metadata o calculada) */
  totalMinutes: number | null;
  /** Todos los slides parseados */
  slides: Slide[];
}
