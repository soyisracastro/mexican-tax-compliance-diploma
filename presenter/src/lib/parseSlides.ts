import fs from "node:fs";
import path from "node:path";
import { marked } from "marked";
import type { Deck, Slide } from "./types";

/**
 * Localiza todos los `slides-scripts.md` en el repo del diplomado.
 * El presenter vive en `presenter/`, las clases viven en carpetas hermanas
 * con estructura `modulo-N.../clase-N.../slides-scripts.md`.
 */
export function findSlideDecks(repoRoot: string): string[] {
  const results: string[] = [];
  const walk = (dir: string) => {
    if (!fs.existsSync(dir)) return;
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const e of entries) {
      if (e.name.startsWith(".") || e.name === "node_modules" || e.name === "dist" || e.name === "presenter") continue;
      const full = path.join(dir, e.name);
      if (e.isDirectory()) walk(full);
      else if (e.isFile() && e.name === "slides-scripts.md") results.push(full);
    }
  };
  walk(repoRoot);
  return results;
}

/**
 * Deriva un slug estable desde el path de un archivo slides-scripts.md.
 *   /repo/modulo-04-isr-personas-fisicas/clase-01-regimenes-fiscales-pf/slides-scripts.md
 *   → modulo-04-clase-01
 */
export function deriveSlugFromPath(filePath: string): string {
  const parts = filePath.split(path.sep);
  const moduleSeg = parts.find((p) => /^modulo-\d+/.test(p)) ?? "modulo-x";
  const classSeg = parts.find((p) => /^clase-\d+/.test(p)) ?? "clase-x";
  const moduleNum = moduleSeg.match(/^modulo-(\d+)/)?.[1] ?? "0";
  const classNum = classSeg.match(/^clase-(\d+)/)?.[1] ?? "0";
  return `modulo-${moduleNum.padStart(2, "0")}-clase-${classNum.padStart(2, "0")}`;
}

/**
 * Parser principal. Convierte el markdown en un Deck con slides tipados.
 *
 * Formato esperado (confirmado en M1C1, M1C2, M4C1):
 *   # <título deck>
 *   ## <subtítulo>
 *   ...preámbulo...
 *   ---
 *   # BLOQUE N — <tema> (<minutos> min)   ← opcional, agrupa slides
 *   ## SLIDE N: <título>
 *   ### Contenido Visual
 *   <markdown>
 *   ### Script
 *   <markdown>
 *   ---
 *   ...
 *   ## Notas Técnicas para el Instructor   ← corte; todo lo siguiente se ignora
 */
export function parseDeck(filePath: string, repoRoot: string): Deck {
  const raw = fs.readFileSync(filePath, "utf-8");
  const relative = path.relative(repoRoot, filePath);
  const slug = deriveSlugFromPath(filePath);

  // Cortar en el marcador de notas del instructor (si existe)
  const instructorNotesMarker = /^## Notas Técnicas para el Instructor\b/im;
  const instructorMatch = raw.match(instructorNotesMarker);
  const body = instructorMatch ? raw.slice(0, instructorMatch.index) : raw;

  // Título y subtítulo del deck
  const titleMatch = body.match(/^#\s+(.+)$/m);
  const subtitleMatch = body.match(/^##\s+(?!SLIDE\b)(.+)$/m);
  const title = titleMatch?.[1]?.trim() ?? "Sin título";
  const subtitle = subtitleMatch?.[1]?.trim() ?? null;

  // Dividir en secciones por encabezados de slide (## SLIDE N: ...)
  const slideHeadingRe = /^## SLIDE (\d+):\s*(.*)$/gm;
  const blockHeadingRe = /^#\s+(BLOQUE\s+\d+[^\n]*|CIERRE[^\n]*)$/gm;

  // Recolectar posiciones de bloques para anclar slides al bloque más cercano previo
  type BlockAnchor = {
    start: number;
    title: string;
    minutes: number | null;
    icon: string | null;
  };
  const blocks: BlockAnchor[] = [];
  for (const m of body.matchAll(blockHeadingRe)) {
    const rawTitle = m[1].trim();
    const minMatch = rawTitle.match(/\((\d+)\s*min\)/i);
    // Parsear directiva {icon: nombre} opcional
    const iconMatch = rawTitle.match(/\{\s*icon:\s*([a-z0-9-]+)\s*\}/i);
    let title = rawTitle;
    if (iconMatch) title = title.replace(iconMatch[0], "").trim();
    title = title.replace(/\s*\(\d+\s*min\)\s*$/i, "").trim();
    blocks.push({
      start: m.index ?? 0,
      title,
      minutes: minMatch ? parseInt(minMatch[1], 10) : null,
      icon: iconMatch ? iconMatch[1].toLowerCase() : null,
    });
  }

  // Recolectar slides con sus posiciones
  type SlideRaw = { number: number; title: string; start: number; end: number };
  const slidesRaw: SlideRaw[] = [];
  const matches = [...body.matchAll(slideHeadingRe)];
  for (let i = 0; i < matches.length; i++) {
    const m = matches[i];
    const start = m.index ?? 0;
    const end = i + 1 < matches.length ? (matches[i + 1].index ?? body.length) : body.length;
    slidesRaw.push({
      number: parseInt(m[1], 10),
      title: m[2].trim(),
      start,
      end,
    });
  }

  // Asignar cada slide a su bloque anterior más cercano
  const findBlock = (pos: number): BlockAnchor | null => {
    let current: BlockAnchor | null = null;
    for (const b of blocks) {
      if (b.start < pos) current = b;
      else break;
    }
    return current;
  };

  // Contar slides por bloque para repartir los minutos
  const slidesPerBlock = new Map<number, number>();
  for (const s of slidesRaw) {
    const b = findBlock(s.start);
    const key = b?.start ?? -1;
    slidesPerBlock.set(key, (slidesPerBlock.get(key) ?? 0) + 1);
  }

  const slides: Slide[] = slidesRaw.map((s) => {
    const section = body.slice(s.start, s.end);
    const { contentHtml, scriptHtml, scriptText } = extractSlideSections(section, slug);
    const block = findBlock(s.start);
    const slidesInBlock = block ? slidesPerBlock.get(block.start) ?? 1 : 1;
    const estimatedMinutes =
      block?.minutes != null ? Math.round((block.minutes / slidesInBlock) * 10) / 10 : null;
    return {
      number: s.number,
      title: s.title,
      contentHtml,
      scriptHtml,
      scriptText,
      blockTitle: block?.title ?? null,
      blockIcon: block?.icon ?? null,
      blockMinutes: block?.minutes ?? null,
      estimatedMinutes,
    };
  });

  const totalMinutes = blocks
    .filter((b) => b.minutes != null)
    .reduce((sum, b) => sum + (b.minutes ?? 0), 0) || null;

  return {
    slug,
    sourcePath: relative,
    title,
    subtitle,
    totalMinutes,
    slides,
  };
}

/**
 * Dada la porción de markdown de un slide (desde "## SLIDE N:" hasta el siguiente slide),
 * extrae Contenido Visual y Script.
 *
 * Las secciones son opcionales y están delimitadas por "### Contenido Visual" y "### Script".
 */
function extractSlideSections(section: string, slug: string): {
  contentHtml: string;
  scriptHtml: string;
  scriptText: string;
} {
  // Remover el encabezado "## SLIDE N: ..." inicial
  const withoutHeader = section.replace(/^## SLIDE \d+:[^\n]*\n/, "");

  // Buscar las subsecciones
  const visualMatch = withoutHeader.match(
    /### Contenido Visual\s*\n([\s\S]*?)(?=\n### Script\b|\n---\s*$|$)/
  );
  const scriptMatch = withoutHeader.match(
    /### Script\s*\n([\s\S]*?)(?=\n---\s*$|$)/
  );

  const contentRaw = visualMatch?.[1]?.trim() ?? "";
  const scriptRaw = scriptMatch?.[1]?.trim() ?? "";

  // Limpiar el trailing "---" si quedó
  const clean = (s: string) => s.replace(/\n---\s*$/g, "").trim();

  const renderer = buildImageRewritingRenderer(slug);

  const contentHtml = contentRaw
    ? (marked.parse(clean(contentRaw), { async: false, renderer }) as string)
    : "";
  const scriptHtml = scriptRaw
    ? (marked.parse(clean(scriptRaw), { async: false, renderer }) as string)
    : "";
  const scriptText = clean(scriptRaw);

  return { contentHtml, scriptHtml, scriptText };
}

/**
 * Renderer de marked que reescribe rutas relativas `./images/X` (o `images/X`)
 * a `/images/<slug>/X` para que Astro sirva las imágenes copiadas por
 * copyImages() desde `presenter/public/images/<slug>/`.
 */
function buildImageRewritingRenderer(slug: string) {
  const renderer = new marked.Renderer();
  const originalImage = renderer.image.bind(renderer);
  renderer.image = function ({ href, title, text }) {
    let rewritten = href ?? "";
    if (rewritten.startsWith("./images/") || rewritten.startsWith("images/")) {
      rewritten = rewritten.replace(/^\.?\/?images\//, `/images/${slug}/`);
    }
    return originalImage({ href: rewritten, title, text });
  };
  return renderer;
}

/**
 * Helper para rutas Astro: carga todos los decks del repo.
 */
export function loadAllDecks(): Deck[] {
  const repoRoot = path.resolve(process.cwd(), "..");
  const files = findSlideDecks(repoRoot);
  return files.map((f) => parseDeck(f, repoRoot));
}
