---
name: generate-deck
description: Genera un archivo slides-scripts.md completo desde un tema, para el presenter del diplomado. Sigue el formato y las reglas de densidad del spec de autoría. Invócalo cuando el usuario diga "genera una clase sobre X", "crea slides de Y", "nuevo deck para Z", o pida explícitamente el skill `generate-deck`.
---

# Generador de decks de presentación

Este skill produce un archivo `slides-scripts.md` válido para el presenter, listo para renderizarse como presentación interactiva + teleprompter.

## Cuándo usar este skill

- "Genera una clase sobre IVA para personas morales"
- "Crea slides para explicar depreciación de activos fijos en 45 minutos"
- "Necesito un deck para el módulo 5 sobre personas morales"
- Cualquier solicitud de slides siguiendo el formato del diplomado fiscal

## Inputs que debes extraer del usuario

Si no los proporciona, pregunta antes de generar:

1. **Tema principal** — qué se va a enseñar (obligatorio)
2. **Duración objetivo** — ej. 3.5 hrs efectivas, 210 min (obligatorio)
3. **Audiencia** — ej. contadores, profesionistas, estudiantes (opcional, asumir "contadores públicos mexicanos" por default)
4. **Ubicación del archivo** — `modulo-N-<slug>/clase-N-<slug>/slides-scripts.md` (preguntar si el usuario no lo sabe)
5. **Énfasis / enfoque pedagógico** — opcional (ej. "práctico, con cifras 2026", "defensa fiscal", "cálculos paso a paso")

## Output esperado

Un solo archivo `slides-scripts.md` escrito en la ruta que indique el usuario, siguiendo exactamente el formato documentado en [presenter/AUTHORING.md](../../../presenter/AUTHORING.md).

## Estructura del deck a producir

```markdown
# Clase N — Módulo M: Título del curso
## Subtítulo explicativo

**Duración**: X horas Y minutos efectivos (9:00 am - 1:00 pm con receso)
**Actualización normativa**: Enero 2026 (CFF/LISR/RMF vigentes)

---

## SLIDE 1: Título-gancho

### Contenido Visual

**Subtítulo** breve + metadata (módulo, clase, instructor).

Instructor — **LCP Israel Castro**

### Script

"Buenos días. Bienvenidos a la Clase X..." (apertura de 2-3 párrafos)

---

## SLIDE 2: Hoja de Ruta

### Contenido Visual

| Bloque | Tema | Min |
|---|---|---|
| 1 | ... | NN |

### Script
...

---

# BLOQUE 1 — NOMBRE DEL BLOQUE (NN min) {icon: lucide-name}

---

## SLIDE 3: ...
```

El deck termina con:

```markdown
## SLIDE N: Gracias · Próxima Clase

### Contenido Visual

Tarea para estas 2 semanas · contacto del instructor

### Script
"Cerramos. En las próximas dos semanas..."

---

## Notas Técnicas para el Instructor

### Cronograma Detallado
[tabla hora por hora]

### Dinámica de Participación
[notas]
```

## Reglas de densidad (OBLIGATORIAS)

El instructor narra todo desde el script. El slide NO repite el script, refuerza ideas ancla.

### Por slide (contenido visual)

1. **Máximo 5 bullets** — si hay más, divide el slide
2. **Cada bullet ≤ 14 palabras** — frase-gancho, no oración completa
3. **1 a 3 palabras en negrita** — son los acentos azules del slide
4. **Una tabla por slide** — si la tabla es la idea, no hay bullets
5. **Cifras y plazos en negrita** (ej. **$3.5 MDP**, **Art. 96 LISR**, **20 días hábiles**)
6. **Referencias normativas abreviadas** (ej. "Art. 96" no "artículo noventa y seis")
7. El slide **nunca** explica — eso lo hace el script

### Por bloque

- Cada bloque cubre 15-45 minutos
- 3 a 7 slides por bloque
- Asigna un icono Lucide al header: `{icon: briefcase}`, `{icon: scale}`, etc.

### Por script (teleprompter)

- **Primera persona**, conversacional
- 2-4 párrafos por slide (alrededor de 150-300 palabras)
- Incluye **referencias normativas precisas** ("Art. 91 LISR", "Capítulo II del Título IV")
- Cierra cada script con una transición al siguiente slide cuando sea natural
- Anécdotas breves cuando apliquen ("me encontré con un cliente que...")
- Números concretos siempre, no aproximaciones vagas

## Iconos Lucide sugeridos por tipo de tema

| Tema | Icono |
|---|---|
| Reglas generales / principios | `scale` |
| Sueldos / empleo | `briefcase` |
| Empresas / actividad empresarial | `building-2` |
| RESICO / simplicidad | `sparkles` |
| Inmuebles / arrendamiento | `key-round` |
| Régimen extinto / histórico | `archive` |
| Digital / plataformas | `smartphone` |
| Cierre / resumen | `flag` |
| Deducciones | `receipt` |
| Retenciones | `scissors` |
| Declaraciones | `file-text` |
| Auditorías / revisión | `search` |
| Pagos / tesorería | `wallet` |
| Cumplimiento | `check-circle` |
| Defensa / litigio | `gavel` |
| IVA | `percent` |
| Personas morales | `building` |

Usa nombres exactos de [lucide.dev/icons](https://lucide.dev/icons) en kebab-case.

## Estilo de tono — referencia viva

Antes de generar, lee el script de 3-4 slides del deck existente como referencia de tono:

[modulo-04-isr-personas-fisicas/clase-01-regimenes-fiscales-pf/slides-scripts.md](../../../modulo-04-isr-personas-fisicas/clase-01-regimenes-fiscales-pf/slides-scripts.md)

Puntos característicos del tono:

- Conversacional, tuteo plural ("ustedes") — NO usted ni vosotros
- Afirma con autoridad: "Esta tarifa la van a usar cientos de veces al año"
- Reconoce la práctica real: "Me encuentro todavía papeles de trabajo donde..."
- Conecta artículos con ejemplos concretos: no cita ley sin aterrizar
- Frases cortas mezcladas con largas. Rítmico.
- Usa "ojo", "cuidado", "moraleja" como señales de atención
- Cuando presenta cifras, siempre contextualiza: "...son casi $40,000 de ahorro"

## Proceso recomendado para generar

1. **Parsear input del usuario**: tema, duración, ubicación
2. **Esbozar estructura**: 6-8 bloques, repartir los minutos
3. **Enumerar slides por bloque**: 3-7 cada uno, identificar qué idea-ancla lleva cada slide
4. **Redactar portada + hoja de ruta** (slides 1 y 2)
5. **Redactar bloques secuencialmente** — para cada slide: título, contenido visual (denso al mínimo), script conversacional
6. **Redactar cierre** (slide final + tarea + contacto del instructor)
7. **Agregar notas técnicas al final** (cronograma + dinámica)
8. **Validar mentalmente**: ¿cada slide cumple las 7 reglas de densidad?

## Ejemplo mínimo autocontenido (3 slides)

```markdown
# Clase 1 — Módulo 9: Depreciación Fiscal de Activos Fijos
## Reglas de depreciación para personas morales 2026

**Duración**: 1 hora

---

## SLIDE 1: Depreciación Fiscal

### Contenido Visual

**Tasas máximas** del Título II de la LISR.

Módulo 9 · Clase 1 · Enero 2026

Instructor — **LCP Israel Castro**

### Script

"Bienvenidos. La depreciación fiscal parece un tema seco, pero les voy a demostrar en una hora que es la palanca silenciosa de la planeación fiscal de toda persona moral. Dominar las tasas del Título II no es cuestión de memoria: es cuestión de timing, y es dinero. Arrancamos."

---

# BLOQUE 1 — FUNDAMENTOS DE LA DEPRECIACIÓN (30 min) {icon: calculator}

---

## SLIDE 2: Concepto y Fundamento Legal

### Contenido Visual

**Arts. 31-34 LISR** · gasto anual que representa el **desgaste** del activo.

- Se aplica a partir del mes en que se empieza a usar
- Pro-rata por meses completos
- Es deducción, no pago real

### Script

"La depreciación es el ÚNICO mecanismo fiscal que no sigue el flujo de efectivo. Ustedes pagaron por el activo hace tres años; hoy siguen deduciendo su desgaste. Art. 31 LISR define el mecanismo, del 32 al 34 están las particularidades..."

---

## SLIDE 3: Tabla de Tasas Máximas

### Contenido Visual

| Activo | Tasa anual |
|---|---|
| Construcciones | 5% |
| Mobiliario | 10% |
| **Computadoras** | **30%** |
| Automóviles (tope $175K) | 25% |

Son **máximas**: el contribuyente puede depreciar más lento, nunca más rápido.

### Script

"Esta tabla es la Biblia. Art. 34. Memórenla. Pero ojo: son tasas MÁXIMAS..."

---

## Notas Técnicas para el Instructor

### Cronograma
9:00-9:10 Slide 1 (apertura)
9:10-9:40 Bloque 1 (conceptos)
...
```

## Validación antes de entregar

Antes de devolver el archivo, verifica mentalmente:

- [ ] Portada con título-gancho, subtítulo, módulo, clase, fecha, instructor
- [ ] Hoja de ruta con tabla de bloques y minutos
- [ ] Al menos 5 bloques con `{icon: ...}` válido
- [ ] Cada slide tiene `### Contenido Visual` o solo título (para slides de portada/transición)
- [ ] Cada slide tiene `### Script` en primera persona
- [ ] Ningún slide excede 5 bullets o una tabla grande + 2 bullets
- [ ] Las negritas del contenido visual son 1-3 por slide
- [ ] El script es conversacional, no manual
- [ ] Slide final de cierre con tarea + contacto del instructor
- [ ] Sección `## Notas Técnicas para el Instructor` al final
- [ ] El nombre del instructor es **LCP Israel Castro** salvo que el usuario indique otro

## Después de generar

Avisa al usuario:

1. La ruta donde se guardó el archivo
2. Que reinicie el dev server (`npm run dev` en `presenter/`) o refresque el navegador — el hot-reload del presenter lo detectará
3. Que el nuevo deck aparecerá automáticamente en `/` (el hub) y será accesible en `/presenter/<slug>`
4. Sugerencias de iconos alternativos si aplica
5. Si faltan imágenes, indicar que se pueden agregar en `images/` dentro de la carpeta de la clase

## Referencias

- [presenter/AUTHORING.md](../../../presenter/AUTHORING.md) — spec formal del formato
- [modulo-04-isr-personas-fisicas/clase-01-regimenes-fiscales-pf/slides-scripts.md](../../../modulo-04-isr-personas-fisicas/clase-01-regimenes-fiscales-pf/slides-scripts.md) — deck de producción como referencia de tono y densidad
