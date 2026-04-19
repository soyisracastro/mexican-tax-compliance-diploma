# Presentador — Diplomado Fiscal

Presentador de slides con teleprompter dual-screen para las clases del **Diplomado en Herramientas Prácticas ante la Autoridad Fiscal**.

Lee directamente los archivos `slides-scripts.md` del repo — la misma fuente usada por Gamma — y genera tres vistas sincronizadas en tiempo real.

## Cómo correrlo

```bash
cd presenter
npm install
npm run dev
```

Abre [http://localhost:4321/](http://localhost:4321/) (o el puerto que indique Astro si el 4321 está ocupado).

## Vistas

| Vista | URL | Uso |
|---|---|---|
| **Hub** | `/` | Lista de clases disponibles |
| **Presenter** | `/presenter/<deck>` | Slides grandes, minimalistas — pantalla de proyección |
| **Notes** | `/notes/<deck>` | Script teleprompter en tema oscuro + temporizador + preview del siguiente slide |
| **Overview** | `/overview/<deck>` | Grid de todas las slides agrupadas por bloque |

`<deck>` es el slug derivado de la ruta del archivo, por ejemplo `modulo-04-clase-01`.

## Flujo típico (dual-screen)

1. Conecta tu laptop a un proyector o pantalla externa (modo extendido).
2. Abre `/presenter/<deck>` → mueve esa ventana a la pantalla de proyección y pon fullscreen (`Cmd+Ctrl+F` en macOS).
3. Abre `/notes/<deck>` en otra pestaña o ventana → mantenla en la pantalla de tu laptop.
4. Navega con flechas en cualquiera de las dos ventanas; la otra se mueve instantáneamente.

La sincronización usa **BroadcastChannel API** (mismo origen, sin backend) con fallback a `localStorage` para navegadores viejos.

## Atajos de teclado

| Tecla | Acción |
|---|---|
| `←` / `→` | Slide anterior / siguiente |
| `Space` | Avanzar |
| `PageUp` / `PageDown` | Igual que flechas |
| `Home` / `End` | Primer / último slide |
| `N` | Abrir vista **Notas** en nueva pestaña |
| `P` | Abrir vista **Presenter** en nueva pestaña |
| `O` | Abrir vista **Overview** en nueva pestaña |
| `Esc` | Cerrar overview (volver al presenter) |

## Formato de contenido

El parser espera archivos `slides-scripts.md` en cualquier carpeta del repo con esta estructura:

```markdown
# Clase 01 — Título del deck
## Subtítulo

---

# BLOQUE 1 — Tema del bloque (35 min)

---

## SLIDE 1: Portada

### Contenido Visual
- Bullet 1
- Bullet 2

| Columna A | Columna B |
|---|---|
| valor | valor |

### Script
"Texto teleprompter en primera persona..."

---

## SLIDE 2: Siguiente slide
...
```

- **Slides** se detectan por `## SLIDE N: Título`
- **Bloques** (opcionales) se detectan por `# BLOQUE N — ... (M min)` y agrupan slides consecutivos
- Todo lo que aparece después de `## Notas Técnicas para el Instructor` se excluye (metadatos del docente)
- Los minutos del bloque se dividen entre sus slides para el temporizador

## Estructura del código

```
presenter/
├── astro.config.mjs            # vite + tailwind v4
├── package.json
├── src/
│   ├── lib/
│   │   ├── parseSlides.ts      # parser markdown → Deck
│   │   ├── types.ts            # Slide, Deck
│   │   └── utils.ts            # cn() utility (clsx + tailwind-merge)
│   ├── scripts/
│   │   ├── sync.ts             # BroadcastChannel wrapper con fallback localStorage
│   │   └── presenter-controller.ts  # estado + keybindings + broadcast
│   ├── layouts/Base.astro       # HTML shell + fuentes Inter/Fraunces/JetBrains Mono
│   ├── pages/
│   │   ├── index.astro          # hub
│   │   ├── presenter/[deck].astro
│   │   ├── notes/[deck].astro
│   │   └── overview/[deck].astro
│   └── styles/global.css        # design tokens de TodoConta landing + estilos slide/notes
```

## Design system

Los tokens de color, tipografía y espaciado provienen de `todoconta-apps/apps/landing/src/styles/global.css` — misma identidad visual que la landing pública del diplomado. Si se actualiza la landing, conviene copiar los cambios aquí.

- Fondo: `#FAFAF7` (beige cálido)
- Primario: `#0B5FFF` (Azul Legal)
- Tipografía: Inter (UI), Fraunces (editorial si se usa), JetBrains Mono (mono)

## Agregar una nueva clase

1. Crea el archivo `modulo-N-.../clase-M-.../slides-scripts.md` en el repo con el formato descrito arriba.
2. Reinicia `npm run dev` (Astro detecta archivos nuevos en `getStaticPaths` al build).
3. El nuevo deck aparece automáticamente en el hub como `modulo-N-clase-M`.

## Build de producción

```bash
npm run build
```

Genera `dist/` con HTML + JS estáticos. Se puede servir desde cualquier static host (Vercel, Netlify, `npx serve dist`).

## Troubleshooting

- **Puerto ocupado**: Astro automáticamente prueba 4322, 4323, etc. Revisa la salida del `dev`.
- **Cambios en markdown no se reflejan**: reinicia el dev server. Astro parsea las rutas estáticas al arrancar; ediciones al `.md` no hacen hot-reload.
- **Dual-screen no sincroniza**: verifica que ambas ventanas estén en el mismo origen (`localhost:4321`). BroadcastChannel no cruza orígenes.
