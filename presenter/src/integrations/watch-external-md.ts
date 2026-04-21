import path from "node:path";
import chokidar from "chokidar";
import type { AstroIntegration } from "astro";
import { copyImages } from "../lib/copyImages";

/**
 * Integración Astro que vigila los archivos `slides-scripts.md` que viven FUERA
 * del directorio del presenter (en carpetas hermanas modulo-N/clase-N). Cuando
 * alguno cambia, dispara un `full-reload` del navegador en el dev server.
 *
 * Sin esta integración, Astro/Vite solo vigila archivos dentro de `src/` y los
 * cambios en el contenido fuente (los MDs de cada clase) no se reflejan hasta
 * reiniciar manualmente `npm run dev`.
 *
 * Solo activa en dev — en build no corre.
 */
export function watchExternalMarkdown(): AstroIntegration {
  return {
    name: "watch-external-markdown",
    hooks: {
      "astro:build:start": ({ logger }) => {
        // Copiar imágenes de cada carpeta de clase a presenter/public/images/<slug>/
        const presenterRoot = process.cwd();
        const repoRoot = path.resolve(presenterRoot, "..");
        const result = copyImages({
          repoRoot,
          presenterRoot,
          log: (m) => logger.info(m),
        });
        if (result.copied > 0) {
          logger.info(
            `🖼  Copiadas ${result.copied} imágenes de ${result.decks} deck${result.decks === 1 ? "" : "s"}`
          );
        }
      },
      "astro:server:setup": ({ server, logger }) => {
        // server.config.root es el project root (presenter/)
        // subimos un nivel para llegar a la raíz del repo
        const presenterRoot = server.config.root as string;
        const repoRoot = path.resolve(presenterRoot, "..");

        // Copia inicial de imágenes al arrancar el dev server
        copyImages({ repoRoot, presenterRoot, log: (m) => logger.info(m) });

        // chokidar v4+ ya no acepta globs; vigilamos el repo root y filtramos
        // con `ignored` para aceptar solo slides-scripts.md e imágenes.
        const watcher = chokidar.watch(repoRoot, {
          ignoreInitial: true,
          awaitWriteFinish: {
            stabilityThreshold: 100,
            pollInterval: 50,
          },
          ignored: (filePath, stats) => {
            // Ignorar siempre node_modules, dist, .git, .astro
            const rel = path.relative(repoRoot, filePath);
            if (!rel || rel.startsWith("..")) return false;
            if (/(^|[\\/])(node_modules|dist|\.git|\.astro|presenter)([\\/]|$)/.test(rel)) {
              return true;
            }
            // Si es un archivo: solo aceptar slides-scripts.md o rutas dentro de images/
            if (stats?.isFile()) {
              if (rel.endsWith("slides-scripts.md")) return false;
              if (/[\\/]images[\\/]/.test(rel)) return false;
              return true;
            }
            return false;
          },
        });

        // Debounce: si se disparan varios eventos (p.ej. guardar + mover tmp)
        // restarteamos una sola vez en una ventana de 200ms.
        let pending: NodeJS.Timeout | null = null;
        const reload = (file: string) => {
          const relative = path.relative(repoRoot, file);
          if (pending) clearTimeout(pending);
          pending = setTimeout(() => {
            logger.info(`📝 ${relative} cambió — reiniciando dev server`);
            // `server.restart()` re-ejecuta getStaticPaths desde cero.
            // Es la única forma confiable en Astro de invalidar rutas generadas
            // por data externa al árbol de src/.
            server.restart();
          }, 200);
        };

        watcher.on("change", reload);
        watcher.on("add", reload);
        watcher.on("unlink", reload);

        logger.info("👀 Vigilando cambios en slides-scripts.md e imágenes externas");
      },
    },
  };
}
