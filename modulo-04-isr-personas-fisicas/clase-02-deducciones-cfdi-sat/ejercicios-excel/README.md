# Ejercicios en Excel — Clase 02, Módulo 4

Dos ejercicios prácticos para realizar en vivo durante la clase, diseñados para reforzar el cálculo de deducciones personales, el tope global y la mecánica completa de la declaración anual.

## Archivos

| Archivo | Tema | Tiempo |
|---|---|---|
| [01-deducciones-personales-tope.xlsx](01-deducciones-personales-tope.xlsx) | Clasificar gastos, aplicar límites por fracción (especialmente el SMG del Art. 151 Frac. V) y calcular el tope global | 20 min |
| [02-declaracion-anual-pf.xlsx](02-declaracion-anual-pf.xlsx) | Declaración anual completa para un asalariado y una contadora independiente con tarifa Art. 152 2026 | 25 min |

Total aproximado: **45 minutos** (repartibles en los bloques de deducciones y casos prácticos).

## Estructura de cada archivo

Cada xlsx lleva 4 hojas:

1. **Instrucciones** — objetivo, pasos, fórmulas sugeridas, pregunta de discusión
2. **Datos** — tarifa anual 2026 (Anexo 8 RMF 2026, factor 1.13213) + constantes UMA y SMG
3. **Ejercicio** — celdas amarillas (input dado) y blancas (a calcular por el alumno)
4. **Solución** — misma tabla con valores ya calculados; sirve como referencia

## Uso sugerido en clase

### Opción A — Un ejercicio por bloque

| Cuándo | Ejercicio | Bloque al que apoya |
|---|---|---|
| Después del Slide 10 (límite global y fracc. V) | 01 — deducciones + tope | Bloque 1 · Deducciones personales |
| Después del Slide 27 (Caso 2 — contador) | 02 — declaración anual | Bloque 5 · Casos prácticos |

### Opción B — Taller integrador (cierre de clase)

Reservar los últimos 45 minutos como taller en vivo. Hacer los ejercicios en orden después de revisar los casos prácticos de los slides. Los participantes verifican sus resultados con la hoja Solución de forma autónoma.

## Formato de las celdas

| Color | Significado |
|---|---|
| 🟡 Amarillo suave | **Input dado** — el alumno puede cambiarlo para probar sensibilidades |
| ⬜ Blanco con borde | **A calcular** — el alumno escribe la fórmula |
| 🔵 Azul suave | Input en la hoja Solución (referencia) |
| 🟢 Verde suave | **Resultado destacado** — base gravable final o ISR determinado |
| 🔴 Rojo suave | ISR a cargo (positivo) — alerta visual |

## Puntos pedagógicos críticos en estos ejercicios

### Ejercicio 1 — PPR/PPAP: SMG, no UMA (Art. 151 Frac. V)

El ejercicio obliga a los alumnos a usar la fórmula `=MIN(PPR_bruto, ingresos*10%, 574948)`.

El $574,948 viene de **5 salarios mínimos generales anuales** ($315.04 × 365 × 5), NO de 5 UMAs ($213,973.20).
La hoja de Instrucciones y Solución resaltan este error frecuente en materiales de capacitación.

### Ejercicio 1 — Colegiaturas fuera del tope global

Las colegiaturas (Decreto DOF 26-dic-2013) se suman **después** de aplicar el tope global de Arts. 151+185.
La columna N de la hoja Ejercicio refleja esto como un paso separado.

### Ejercicio 2 — Diferencia entre asalariado y profesionista

Juan (asalariado) solo puede reducir su base con deducciones personales.
María (profesionista) puede deducir gastos del negocio **primero**, y luego aplica deducciones personales sobre esa base reducida.
Esta diferencia estructural es la razón central por la que el Capítulo II tiene más herramientas de planeación.

## Tarifa utilizada

Ambos ejercicios usan la tarifa anual **Anexo 8 RMF 2026** (DOF 28-dic-2025), factor de actualización **1.13213**.

> ⚠ Esta tarifa es diferente a la que usa el generate.py de la Clase 01, que tiene un factor incorrecto en los tramos superiores. Para actualizaciones futuras, editar `generate.py` de esta carpeta, no el de clase-01.

## Regenerar los archivos

Si actualizas cifras por cambio normativo, edita `generate.py` y ejecuta:

```bash
cd ejercicios-excel
python3 generate.py
```

Requisitos: `openpyxl >= 3.1` (`pip install openpyxl`).

## Resumen de contenido

### Ejercicio 1 — Deducciones personales y tope global

- 4 perfiles: asalariada $350K, contador independiente $937K, arrendadora $180K, RESICO $480K
- Columnas: ingresos · colegiaturas (D10) · médicos (D01) · seguros (D07) · hipoteca (D05) · PPR bruto (D06)
- Alumno calcula: PPR con límite SMG · subtotal · tope 15% · tope 5 UMAs · tope aplicable · deducción final
- Pregunta de discusión: ¿a partir de qué ingreso el tope pasa de ser el 15% a ser fijo en $213,973?

### Ejercicio 2 — Declaración anual PF

- **Juan (asalariado $650K)**: retenciones $122K, gastos médicos $30K, seguros $15K, PPR $25K
  - ISR determinado vs retenciones → resultado: saldo a favor o a cargo
- **María (contadora $1.1M)**: gastos negocio $250K, pagos provisionales $140K, gastos médicos $45K, seguros $20K, PPR $85K
  - Deduce negocio primero → reduce base → aplica tarifa → compara con pagos provisionales
- Pregunta de discusión: ¿qué herramienta del SAT les permite a Juan y María pre-verificar sus CFDIs antes de declarar?

## Notas pedagógicas

- **Celdas amarillas modificables**: invite a los alumnos a cambiar el ingreso de Juan a $300,000 y ver cómo el tope cambia de 5 UMAs a 15% — es un experimento de 30 segundos muy ilustrativo.
- **Google Sheets**: los archivos son compatibles. Google Sheets traduce `BUSCARV` a `VLOOKUP` automáticamente al importar.
- **Distribución**: compartir con la hoja Solución visible permite que los alumnos se auto-verifiquen en tiempo real.

---

**Documento elaborado para fines educativos**
**Diplomado en Herramientas Prácticas ante la Autoridad Fiscal**
**Módulo 4 · Clase 2 — Enero 2026**
