# Ejercicios en Excel — Clase 01, Módulo 4

Tres ejercicios prácticos para realizar en vivo durante la clase, diseñados para reforzar el manejo de tarifas 2026 y las decisiones de régimen fiscal.

## Archivos

| Archivo | Tema | Tiempo |
|---|---|---|
| [01-retencion-isr-mensual.xlsx](01-retencion-isr-mensual.xlsx) | Construcción de la fórmula de retención mensual (Art. 96) con BUSCARV | 15 min |
| [02-resico-vs-612.xlsx](02-resico-vs-612.xlsx) | 5 clientes, comparativo RESICO vs Actividad Empresarial anual | 20 min |
| [03-arrendador-tres-opciones.xlsx](03-arrendador-tres-opciones.xlsx) | 3 arrendadores, comparativo Comprobadas · Ciega · RESICO | 20 min |

Total aproximado: **55 minutos** (repartible entre bloques de la clase).

## Estructura de cada archivo

Cada xlsx lleva 4 hojas:

1. **Instrucciones** — objetivo, pasos, fórmulas sugeridas, pregunta de discusión
2. **Datos** — tarifas oficiales 2026 como tabla para BUSCARV
3. **Ejercicio** — celdas amarillas (input) y blancas (a llenar por el alumno)
4. **Solución** — misma tabla con las fórmulas ya escritas; sirve como referencia si el alumno se atora

## Uso sugerido en clase

### Opción A — Ejercicio 1 solamente (formato exprés)
Después del Bloque 2 (Sueldos y Salarios), al terminar el Slide 13 (ejemplo $25,000):

> "Abran el archivo 01 en sus laptops. Lo resolvemos en 15 minutos aplicando BUSCARV. Quien no llegue a fórmula con BUSCARV puede hacerlo a mano con la tabla; pero hoy queremos que lo dejen parametrizado."

Buen enganche después de ver el ejemplo estático del slide — aquí ellos parametrizan.

### Opción B — Los 3 ejercicios integrados al flujo de la clase

| Cuándo | Ejercicio | Bloque al que apoya |
|---|---|---|
| Después del Slide 13 (ejemplo sueldo $25K) | 01 — retención mensual | Bloque 2 · Sueldos |
| Después del Slide 25 (comparativo RESICO vs 612) | 02 — RESICO vs 612 | Bloque 4 · RESICO |
| Después del Slide 29 (ejemplo local comercial) | 03 — arrendador 3 opciones | Bloque 5 · Arrendamiento |

Con este flujo se invierten ~55 minutos en ejercicio en vivo; ajustar el tiempo de los slides teóricos si es necesario.

### Opción C — Cierre post-receso (taller integrador)
Reservar los últimos 45–60 minutos de la clase como **"taller en vivo"** y hacer los 3 ejercicios seguidos. En este caso, reducir algunos slides teóricos.

## Formato de las celdas

| Color | Significado |
|---|---|
| 🟡 Amarillo suave | **Input** — el alumno cambia el valor |
| ⬜ Blanco con borde | **A calcular** — el alumno escribe la fórmula |
| 🔵 Azul suave | Celda de input en la hoja Solución (referencia) |
| Texto en azul primario | **Resultado final** destacado |

## Regenerar los archivos

Si actualizas las tarifas (por cambio normativo) o modificas casos, edita `generate.py` y ejecuta:

```bash
cd ejercicios-excel
python3 generate.py
```

Requisitos: `openpyxl >= 3.1` (`pip install openpyxl`).

## Resumen de contenido

### Ejercicio 1 — Retención ISR mensual
- 5 casos: sueldos desde $8,000 hasta $200,000
- Alumno construye la fórmula completa: `(sueldo − LI) × tasa + cuota fija`
- Enseña **BUSCARV con aproximación** (último argumento VERDADERO)
- Pregunta de cierre: ¿por qué la carga efectiva varía del 0% al 27% según el sueldo?

### Ejercicio 2 — RESICO vs 612
- 5 clientes con perfiles muy distintos:
  - Arquitecto freelance (gastos 15%) — RESICO domina
  - Dueño de taller (gastos 60%) — depende
  - Consultora (gastos 12%) — RESICO domina
  - Comerciante mayorista ($4.2M) — solo puede 612
  - Profesionista joven — RESICO domina
- Pregunta de cierre: ¿a partir de qué % de gastos empieza a ganar 612?

### Ejercicio 3 — Arrendador 3 opciones
- 3 arrendadores:
  - Doña Carmen — 2 casas, sin hipoteca → gana ciega o RESICO
  - Don Miguel — 1 local pequeño → RESICO domina
  - Sra. Ana — 4 deptos con hipoteca → comprobadas puede ganar por intereses
- Pregunta de cierre: ¿cuándo tiene sentido escoger comprobadas sobre las opciones simples?

## Notas pedagógicas

- **Validar fórmulas abiertas**: pasar de mesa en mesa confirmando que usaron BUSCARV y no valores hardcodeados.
- **Propagar pregunta estratégica**: los ejercicios 2 y 3 deben terminar con discusión en plenaria sobre *cuándo* y *por qué* cambia la recomendación.
- **Distribuir archivos**: compartir por Google Classroom **con la hoja Solución visible** (los alumnos aprenden más si pueden auto-verificarse en tiempo real).
- **Google Sheets**: los archivos son compatibles pero Google Sheets traduce `BUSCARV` a `VLOOKUP` al importar. Las fórmulas siguen funcionando.

---

**Documento elaborado para fines educativos**
**Diplomado en Herramientas Prácticas ante la Autoridad Fiscal**
**Módulo 4 · Clase 1 — Enero 2026**
