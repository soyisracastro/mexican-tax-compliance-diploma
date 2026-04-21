import fs from "node:fs";
import path from "node:path";
import { deriveSlugFromPath, findSlideDecks } from "./parseSlides";

/**
 * Recorre todas las carpetas `modulo-N/clase-N/images/` del repo y copia su
 * contenido a `presenter/public/images/<deck-slug>/` para que Astro las
 * sirva como assets estáticos.
 *
 * Se invoca al arrancar el dev server y antes de cada build.
 */
export function copyImages(opts: {
  repoRoot: string;
  presenterRoot: string;
  log?: (msg: string) => void;
}): { copied: number; decks: number } {
  const { repoRoot, presenterRoot, log = () => {} } = opts;
  const decks = findSlideDecks(repoRoot);
  const destBase = path.join(presenterRoot, "public", "images");
  let totalCopied = 0;
  let decksWithImages = 0;

  for (const deckPath of decks) {
    const deckDir = path.dirname(deckPath);
    const imagesDir = path.join(deckDir, "images");
    if (!fs.existsSync(imagesDir)) continue;

    const slug = deriveSlugFromPath(deckPath);
    const dest = path.join(destBase, slug);
    fs.mkdirSync(dest, { recursive: true });

    let count = 0;
    for (const entry of walkFiles(imagesDir)) {
      const rel = path.relative(imagesDir, entry);
      const target = path.join(dest, rel);
      fs.mkdirSync(path.dirname(target), { recursive: true });
      fs.copyFileSync(entry, target);
      count += 1;
    }
    if (count > 0) {
      log(`🖼  ${slug}: ${count} imagen${count === 1 ? "" : "es"}`);
      decksWithImages += 1;
      totalCopied += count;
    }
  }

  return { copied: totalCopied, decks: decksWithImages };
}

function* walkFiles(dir: string): Generator<string> {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name.startsWith(".")) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) yield* walkFiles(full);
    else if (entry.isFile()) yield full;
  }
}
