# Formato de autoría de slides

Especificación del archivo `slides-scripts.md` que el presenter procesa. Cualquier markdown que cumpla este formato se convierte en una presentación completa con notas teleprompter.

## Ubicación del archivo

```
<repo-root>/
└── <modulo-N>-.../
    └── <clase-N>-.../
        ├── slides-scripts.md    ← este archivo
        └── images/              ← opcional, imágenes referenciadas
            └── *.jpg|png|svg|webp
```

El slug del deck se deriva automáticamente del path: `modulo-04-.../clase-01-...` → `/presenter/modulo-04-clase-01`.

## Estructura del archivo

```markdown
# Título del deck
## Subtítulo opcional
### Metadata libre

**Duración**: ...
**Actualización normativa**: ...

---

# BLOQUE 1 — TÍTULO DEL BLOQUE (NN min) {icon: lucide-name}

---

## SLIDE 1: Título del slide

### Contenido Visual

Aquí va lo que se proyecta. Markdown completo: bullets, tablas, imágenes.

### Script

"Aquí va lo que el instructor lee en el teleprompter. En primera persona."

---

## SLIDE 2: Siguiente slide
...

---

## Notas Técnicas para el Instructor

Todo lo que aparezca después de este encabezado se excluye del deck.
```

## Elementos obligatorios

### 1. Encabezado de slide

```markdown
## SLIDE <número>: <título>
```

- **Número**: entero positivo. Se muestra en el HUD como `N / total`.
- **Título**: texto libre. Aparece en tamaño grande en el centro del slide.
- No dupliques números; el parser los toma literal.

### 2. Sección `### Contenido Visual` (opcional)

Lo que se proyecta en pantalla. Soporta markdown completo:

- Párrafos
- Listas con viñetas (`-`) o numeradas (`1.`)
- **Negritas** — se pintan en **azul primario** automáticamente (es el acento del slide)
- *Itálicas* — tratamiento sutil
- Tablas
- Blockquotes (`>`)
- Código inline (`` `código` ``) y bloques (```` ``` ````)
- Imágenes (ver sección más abajo)

Si se omite, el slide muestra solo el título centrado.

### 3. Sección `### Script` (opcional)

Texto teleprompter que ve el instructor en la pantalla secundaria. Recomendado:

- Primera persona
- Conversacional, no robótico
- Con puntos de énfasis en **negritas** (se pintan en blanco en el tema oscuro del teleprompter)
- Con ideas clave en *itálicas* (ámbar)

## Bloques temáticos (opcional)

Agrupan slides consecutivos. El HUD superior muestra el nombre del bloque + icono.

```markdown
# BLOQUE N — NOMBRE (NN min) {icon: lucide-name}
```

- El nombre y el prefijo `BLOQUE N` son parte del display.
- `(NN min)` es opcional. Si está presente, el tiempo se reparte entre los slides del bloque para el timer de las notas.
- `{icon: name}` es opcional. Usa cualquier nombre válido de [lucide.dev/icons](https://lucide.dev/icons) en **kebab-case** (ej. `briefcase`, `building-2`, `key-round`, `sparkles`).

También se acepta `# CIERRE DE LA CLASE {icon: flag}` como bloque especial.

## Densidad de slides — reglas de oro

El instructor narra todo desde el script. El slide NO repite el script, solo refuerza las ideas ancla.

### Recomendaciones

1. **Máximo 5 bullets por slide** — si necesitas más, divide en dos slides
2. **Cada bullet ≤ 14 palabras** — frases-gancho, no oraciones completas
3. **1-3 palabras en negrita por slide** — son los acentos visuales; más de 3 satura
4. **Una tabla por slide máximo** — si es inevitable mostrar tabla + bullets, que los bullets sean ≤ 3
5. **Los números importan** — cifras, porcentajes y plazos casi siempre van en negrita
6. **Referencias normativas** abreviadas (ej. "Art. 96 LISR" no "Artículo 96 de la Ley del ISR")

### Tablas

Las tablas sí "llenan" el slide correctamente. El presenter permite scroll vertical si la tabla excede la pantalla. Úsalas cuando la comparación sea el punto — no como dump de datos.

### Ejemplo correcto de densidad

```markdown
## SLIDE 4: Sujetos y Flujo de Efectivo

### Contenido Visual

Residente fiscal mexicano = tributa por **renta mundial** (Art. 9 CFF · Art. 90 LISR).

PF acumula cuando **efectivamente percibe** — no cuando devenga (Art. 102).

- En efectivo, bienes, servicios
- Crédito y cheque: **al cobro**
- Cheque no cobrado en 4 meses → se acumula igual

### Script

"Dos ideas aquí. La primera: la regla de los tres mundos. Persona física residente en México: tributa por todo..."
```

### Ejemplo **incorrecto** (demasiado denso)

```markdown
## SLIDE 4: Sujetos del Impuesto y Principio de Flujo de Efectivo

### Contenido Visual

**Sujetos obligados (Art. 90 LISR):**

1. **Residentes en México**: Por todos sus ingresos, sin importar la ubicación...
2. **Residentes en el extranjero con establecimiento permanente**: Por ingresos...
3. **Residentes en el extranjero sin EP**: Por ingresos procedentes de fuente...

> **Residencia fiscal** (Art. 9 CFF): Se consideran residentes a quienes tengan...

**Principio de acumulación (Art. 102 LISR)**: Las personas físicas acumulan...

[tabla con 5 columnas]
```

— demasiado texto, el slide compite con el script.

## Imágenes

### Convención

Coloca los archivos en una subcarpeta `images/` al lado del `slides-scripts.md`:

```
clase-01-xxx/
├── slides-scripts.md
└── images/
    ├── portada.jpg
    └── bloque-2-nomina.svg
```

Referencia con markdown estándar:

```markdown
![Alt text descriptivo](./images/portada.jpg)
```

También acepta `images/portada.jpg` (sin `./`).

### Cómo se renderizan

- **Imagen sola en el slide** → variante hero (hasta 70vh, casi fullbleed)
- **Imagen + texto** → tamaño inline moderado (máx 55vh), centrada, con sombra sutil y borde redondeado

### Recomendaciones

- Formato: **webp** o **svg** preferidos; jpg/png válidos
- Tamaño: max 1920×1080 antes de compresión — el presenter es para proyección, no necesitas 4K
- Alt text: descriptivo para accesibilidad y contexto

### Pipeline de build

El build copia automáticamente `images/` → `public/images/<deck-slug>/`. El parser reescribe las rutas relativas a rutas absolutas. Nada manual.

## Corte del archivo — `## Notas Técnicas para el Instructor`

Todo lo que aparezca después de este encabezado se ignora en la presentación. Úsalo para:

- Cronograma detallado
- Recursos visuales a preparar
- Dinámica por slide
- Materiales a llevar

## Valores por default y atajos del presenter

El que presenta tiene estos controles:

| Tecla | Acción |
|---|---|
| `←` / `→` · `Space` | Navegar slides |
| `Home` / `End` | Primer / último |
| `N` / `P` / `O` | Abrir vista de notas / presenter / overview |
| `2` `5` `Enter` | Ir al slide 25 |
| `⌘K` / `Ctrl+K` | Buscar slide por título |
| `F` | Spotlight (oscurece resto) |
| `+` / `-` / `0` (en notas) | Escalar fuente del script |
| `Esc` | Cerrar overlay / buscador |

## Crear un deck nuevo desde cero

1. Crea la carpeta con el patrón `modulo-N-<slug>/clase-N-<slug>/`
2. Copia como plantilla un `slides-scripts.md` existente (ej. `modulo-04-.../clase-01-.../slides-scripts.md`)
3. Reemplaza contenido siguiendo esta spec
4. Si necesitas imágenes, crea `images/` y referencia con markdown estándar
5. Reinicia el dev server (`npm run dev`) o simplemente edita — el hot-reload detecta archivos nuevos
6. El nuevo deck aparece en el hub `/` automáticamente

## Generación automatizada con LLM

Existe un skill para Claude (u otro LLM) que, dado un tema y una audiencia, produce un `slides-scripts.md` válido siguiendo este spec. Ver [.claude/skills/generate-deck/SKILL.md](.claude/skills/generate-deck/SKILL.md).

## Referencia completa

Los decks de ejemplo en producción son la mejor referencia de tono y densidad:

- [modulo-04-.../clase-01-.../slides-scripts.md](../modulo-04-isr-personas-fisicas/clase-01-regimenes-fiscales-pf/slides-scripts.md) — 37 slides, 7 bloques con iconos, nivel profesional
- [modulo-01-.../clase-01-.../slides-scripts.md](../modulo-01-fundamentos-sistema-fiscal/clase-01-principios-constitucionales/slides-scripts.md) — 24 slides, formato inicial sin bloques

Para tono teleprompter conversacional, el script de M4C1 es la referencia.
