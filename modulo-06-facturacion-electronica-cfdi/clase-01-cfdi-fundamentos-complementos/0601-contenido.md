# Módulo 6 — Clase 1: Facturación Electrónica y CFDI 4.0

**Diplomado en Herramientas Prácticas ante la Autoridad Fiscal**
**Duración efectiva:** 3 horas 30 minutos (4 horas con 30 min de descanso)
**Modalidad:** 100% online
**Público objetivo:** Contadores en ejercicio que requieren actualización profesional
**Docente:** C.P. Israel Castro Urieta (Isca)

---

## 🎯 Objetivos de aprendizaje

Al finalizar la sesión, el participante será capaz de:

1. Identificar los fundamentos legales y técnicos del CFDI 4.0 vigentes para 2026, distinguiendo lo que cambió respecto a versiones anteriores y lo que se ha consolidado.
2. Explicar los campos obligatorios del receptor (nombre/razón social, código postal y régimen fiscal) y su impacto en el timbrado y la deducibilidad.
3. Reconocer los principales complementos del CFDI 4.0 vigentes (Recepción de Pagos 2.0, Carta Porte 3.1, INE, Comercio Exterior, Nómina) y los supuestos en los que cada uno es obligatorio.
4. Diagnosticar los errores frecuentes en la emisión y cancelación del CFDI, así como diseñar controles internos preventivos para evitarlos.
5. Vincular los requisitos del CFDI con los requisitos de deducibilidad del artículo 27 LISR y de acreditamiento del artículo 5 LIVA.

---

## 🗺️ Mapa de la sesión y tiempos sugeridos

| Bloque | Tema | Tiempo | Acumulado |
|---|---|---|---|
| 0 | Apertura, encuadre y diagnóstico inicial | 15 min | 0:15 |
| 1 | Fundamentos del CFDI 4.0 y requisitos fiscales | 45 min | 1:00 |
| 2 | Nuevos campos obligatorios del receptor | 30 min | 1:30 |
| ☕ | **DESCANSO** | **30 min** | — |
| 3 | Complementos: Pagos, Carta Porte, INE y otros | 60 min | 2:30 |
| 4 | Errores frecuentes y cómo evitarlos | 30 min | 3:00 |
| 5 | Impacto fiscal del CFDI en deducciones | 25 min | 3:25 |
| 6 | Cierre, preguntas de reflexión y enlace con Clase 2 | 5 min | 3:30 |

> **Nota didáctica para el docente:** Estos tiempos son de referencia. Si el grupo se torna complejo en algún tema (especialmente complementos o cancelación), reasignar minutos del bloque 5 que se puede convertir en lectura comentada. La Clase 2 está diseñada para retomar casos prácticos, por lo que es válido cerrar la teoría aquí y reservar los ejercicios para la siguiente sesión.

---

## Bloque 0 — Apertura y diagnóstico inicial *(15 min)*

### 0.1 Encuadre

Presentación del módulo dentro del diplomado y de la lógica de las dos clases:

- **Clase 1 (hoy):** marco normativo, requisitos, complementos, errores e impacto en deducciones.
- **Clase 2:** taller práctico de emisión, validación de XML, casos de cancelación y corrección.

### 0.2 Diagnóstico rápido (10 min)

Tres preguntas abiertas al grupo —idealmente con herramienta tipo encuesta, chat o levantando la mano virtual— para calibrar el nivel:

1. ¿Cuántos de ustedes han recibido al menos una carta invitación del SAT por discrepancias entre CFDI emitidos y declaraciones presentadas en los últimos 12 meses?
2. ¿Quién ha tenido que cancelar un CFDI fuera del ejercicio en que se emitió y enfrentar el problema?
3. ¿Quiénes manejan clientes que requieren Carta Porte o complemento INE?

> **Para el docente:** las respuestas a estas tres preguntas permiten ajustar la profundidad de los bloques 4 y 5. Si la mayoría dice sí a la pregunta 1, conviene reforzar el bloque 4 sobre errores frecuentes.

---

## Bloque 1 — Fundamentos del CFDI 4.0 y sus requisitos fiscales *(45 min)*

### 1.1 Marco legal vigente *(10 min)*

El CFDI no nace de un acuerdo administrativo: tiene base legal expresa. Para 2026 el andamiaje normativo aplicable es:

| Norma | Contenido relevante |
|---|---|
| **CFF, art. 29** | Obligación de expedir comprobantes fiscales mediante documentos digitales a través del portal del SAT cuando las leyes establezcan obligación de comprobar actos, actividades, ingresos o retenciones. |
| **CFF, art. 29-A** | Catálogo de requisitos que debe contener todo CFDI (clave RFC, régimen fiscal, lugar y fecha de expedición, datos del receptor, descripción de bienes/servicios, valor unitario, etc.) |
| **CFF, art. 29 Bis** | Reglas para los Proveedores Autorizados de Certificación (PAC) y validación. |
| **Reglamento del CFF, art. 39** | Especificaciones técnicas adicionales que debe cumplir el CFDI. |
| **RMF 2026** (DOF 28/12/2025) | Capítulo 2.7 “De los CFDI o Factura Electrónica”, reglas 2.7.1.1 a 2.7.7.x |
| **Anexo 20 RMF 2026** | Estándar técnico (XSD) para la generación, sellado y validación del CFDI 4.0. Su Guía de llenado fue actualizada al 29 de diciembre de 2025. |

> **Punto a destacar al grupo:** El SAT publicó la RMF 2026 y sus principales anexos el 28 y 29 de diciembre de 2025; los anexos 3, 7, 10, 11, 12, 13, 14 y 16 se publicaron el 9 de enero de 2026. El Anexo 20 mantuvo la estructura del CFDI 4.0 sin cambios estructurales: lo que cambió fueron referencias a URLs y una precisión de llenado para productos con nicotina. La estabilidad estructural del CFDI 4.0 desde abril de 2023 es, en sí misma, una señal de madurez del sistema.

### 1.2 Naturaleza jurídica del CFDI *(10 min)*

El CFDI no es solo una representación digital de la factura tradicional. Es:

- **Un documento digital con efectos fiscales propios** (CFF art. 29 párrafo segundo).
- **Una declaración del contribuyente** sobre la operación realizada, con el sello digital como manifestación de voluntad.
- **Insumo de fiscalización electrónica:** el SAT pre-llena declaraciones de ISR e IVA con base en los CFDI emitidos y recibidos.
- **Requisito constitutivo —no meramente probatorio— de la deducibilidad y del acreditamiento.**

**Estructura técnica esencial:**

```
CFDI 4.0 (XML)
│
├── Comprobante (nodo raíz: versión, serie, folio, fecha, sello, certificado)
│   ├── CfdiRelacionados (cuando aplique: sustitución, devolución, etc.)
│   ├── Emisor (RFC, Nombre/Razón social, RégimenFiscal)
│   ├── Receptor (RFC, Nombre, DomicilioFiscalReceptor [CP], RegimenFiscalReceptor, UsoCFDI)
│   ├── Conceptos (ClaveProdServ, ClaveUnidad, Descripción, ValorUnitario, Importe…)
│   │   ├── Impuestos (Traslados, Retenciones)
│   │   └── ACuentaTerceros / InformacionAduanera / CuentaPredial / etc.
│   ├── Impuestos (totales)
│   └── Complemento (Pagos, CartaPorte, INE, ComercioExterior, Nómina, etc.)
│
└── TimbreFiscalDigital (insertado por el PAC: UUID, sello SAT, fecha de timbrado)
```

### 1.3 Tipos de CFDI vigentes *(10 min)*

Repaso a velocidad media —el grupo ya los conoce, pero conviene reordenar el mapa mental:

| Tipo | Clave | Uso típico |
|---|---|---|
| Ingreso | **I** | Venta de bienes, prestación de servicios, arrendamiento, honorarios. |
| Egreso | **E** | Devoluciones, descuentos, bonificaciones, notas de crédito. |
| Traslado | **T** | Movimiento de mercancía propia (típicamente con Carta Porte). |
| Nómina | **N** | Pago de salarios y asimilables (Complemento Nómina 1.2). |
| Pago | **P** | Recepción de pagos en parcialidades o diferidos (REP con Complemento de Pagos 2.0). |
| Retenciones e información de pagos | — | Documento técnico distinto al Anexo 20 “principal” (regla 2.7.5.4 RMF 2026). |

### 1.4 Métodos y formas de pago: la fuente de la mitad de los problemas *(15 min)*

Esta distinción merece tiempo porque es la causa de muchas cartas invitación:

**Método de pago** — *cómo se acuerda liquidar la operación*:
- **PUE** (Pago en Una sola Exhibición): el pago se realiza al momento de emitir el CFDI o antes.
- **PPD** (Pago en Parcialidades o Diferido): el pago llega después de emitir el CFDI, ya sea total o parcial.

**Forma de pago** — *qué medio físico/electrónico se utiliza* (catálogo c_FormaPago):
- 01 Efectivo, 02 Cheque nominativo, 03 Transferencia electrónica, 04 Tarjeta de crédito… hasta clave 99 “Por definir” (que SOLO se usa con PPD).

**Reglas críticas que el contador debe internalizar:**

1. **PUE → exige forma de pago real** (01, 03, 04, etc.). No se puede usar “99 Por definir” en un PUE.
2. **PPD → siempre forma de pago “99 Por definir”** y, al recibir el cobro, se debe emitir CFDI tipo P con Complemento de Pagos.
3. **Si emitiste un PUE pero el cliente paga semanas después**, técnicamente debiste emitirlo como PPD. Corregirlo implica cancelación con motivo 01 y sustitución.
4. **El IVA se causa con el cobro efectivo**, no con la fecha del CFDI. Por eso el Complemento de Pagos es insumo directo para el llenado del IVA mensual y por eso el SAT cruza tan agresivamente esta información.

### 🤔 Preguntas de reflexión para el grupo

- ¿En tu despacho, qué porcentaje de los CFDI que emiten tus clientes son realmente PUE versus PPD? ¿Cómo lo documentan?
- ¿Has tenido el caso del cliente que “factura todo PUE” porque “es más fácil” pero cobra a 30/60/90 días? ¿Cuál es el riesgo fiscal real que corre?
- Si el SAT te enviara mañana una carta invitación por discrepancia de IVA, ¿en cuánto tiempo podrías reconciliar los CFDI emitidos contra los pagos efectivamente cobrados?

---

## Bloque 2 — Nuevos campos obligatorios del receptor *(30 min)*

### 2.1 De dónde venimos: el cambio del CFDI 3.3 al 4.0 *(5 min)*

El CFDI 4.0 entró en vigor el 1 de enero de 2022 con un periodo de convivencia con la 3.3, y se volvió de uso obligatorio el 1 de abril de 2023. Para 2026 ya no hay debate: la 4.0 es la única versión válida. La diferencia más visible y dolorosa para el contribuyente fue la inclusión de **datos del receptor que antes no eran obligatorios y cuya validación por parte del SAT es estricta**.

### 2.2 Los tres campos críticos del receptor *(15 min)*

Para que un CFDI 4.0 timbre correctamente, los siguientes campos del nodo Receptor deben coincidir EXACTAMENTE con lo registrado en el SAT:

#### A) Nombre o Razón Social

- **Persona física:** debe registrarse SIN régimen societario y SIN abreviaturas, exactamente como aparece en la Constancia de Situación Fiscal.
- **Persona moral:** razón social completa, normalmente en mayúsculas, sin punto final, exactamente como en la Constancia.
- **Caso típico de error:** “MARÍA GUADALUPE LÓPEZ HERNÁNDEZ” vs “MA. GUADALUPE LOPEZ HERNANDEZ”. El acento, la abreviatura, el guion, todo importa.

#### B) Código Postal (DomicilioFiscalReceptor)

- Es el **CP del domicilio fiscal**, no el de la sucursal o el del proyecto.
- Debe coincidir con el CP que el receptor tiene registrado en su RFC.
- Si el receptor cambió de domicilio y no actualizó el aviso, el CFDI no timbrará.

#### C) Régimen Fiscal del Receptor

- Es la clave del **régimen del receptor según el catálogo c_RegimenFiscal** (601 General, 605 Sueldos y Salarios, 612 Personas Físicas con Actividades Empresariales y Profesionales, 626 RESICO, etc.).
- Debe corresponder a un régimen vigente del receptor en el momento de la emisión.
- **Si el cliente tributa en varios regímenes, debe indicar cuál aplica para esa operación.**

### 2.3 Uso del CFDI: ya no existe “P01 Por definir” como salida fácil *(5 min)*

El catálogo c_UsoCFDI obliga al receptor a indicar el destino del comprobante:

- **G01** Adquisición de mercancías
- **G03** Gastos en general
- **D01** Honorarios médicos
- **D02** Gastos médicos por incapacidad o discapacidad
- **D10** Pagos por servicios educativos
- **CP01** Pagos (exclusivo para CFDI tipo P con complemento de Pagos)
- **CN01** Nómina
- **S01** Sin efectos fiscales (operaciones con público en general, donativos no deducibles, etc.)

> **El uso del CFDI debe ser congruente con el régimen fiscal del receptor.** Una persona física en régimen de sueldos y salarios (605) no puede recibir un CFDI con uso G03 “Gastos en general” porque ese régimen no permite esa deducción. El sistema lo rechaza al timbrado.

### 2.4 La trampa de la Constancia de Situación Fiscal *(5 min)*

Este es un punto que conviene aclarar al grupo porque genera fricción:

- El SAT **prohíbe expresamente** condicionar la emisión del CFDI a la entrega física de la Constancia de Situación Fiscal (criterio 50/CFF del Anexo 3 RMF de prácticas indebidas).
- Pero el emisor **necesita los datos correctos** (nombre, CP, régimen) para timbrar.
- La práctica recomendada: solicitar los datos por escrito (correo, formulario web), no exigir el documento, y configurar “clientes frecuentes” con protocolos de actualización al menos anual.

### 🤔 Preguntas de reflexión

- En tu cartera de clientes ¿quién es responsable de validar el CP, nombre y régimen fiscal de los receptores? ¿El emisor, el cliente, ambos?
- ¿Tienes protocolo para actualizar los datos cuando un cliente cambia de régimen (por ejemplo, se da de alta en RESICO o sale de él)?

---

## ☕ DESCANSO *(30 min)*

---

## Bloque 3 — Complementos: Pagos, Carta Porte, INE y otros *(60 min)*

### 3.1 ¿Qué es un complemento y por qué importa? *(5 min)*

Un complemento es un **nodo XML adicional anidado dentro del nodo Complemento del CFDI**, que el SAT publica para cubrir información específica de ciertos sectores o tipos de operación.

Tres reglas generales que rigen a TODOS los complementos:

1. **Obligatoriedad por sector u operación:** cada complemento aplica a contribuyentes específicos o a operaciones específicas; no son opcionales una vez que se actualiza el supuesto de obligatoriedad.
2. **Validación adicional por el PAC:** los complementos tienen sus propias reglas de validación que el PAC debe verificar antes de timbrar.
3. **Plazo de adopción de nuevos complementos:** la RMF 2026 establece que los nuevos complementos publicados por el SAT son obligatorios 30 días naturales después de su publicación en el portal.

### 3.2 Complemento de Recepción de Pagos 2.0 (REP) *(20 min)*

Es el complemento que más impacta el día a día del contador. También se le conoce como “Recibo Electrónico de Pago”.

#### Fundamento legal
- CFF art. 29-A, fracción VII, inciso b)
- RMF 2026 reglas 2.7.1.29 (requisitos en la expedición de CFDI), 2.7.1.32 (expedición de CFDI por pagos realizados) y 2.7.1.35 (criterios de aplicación de pagos a CFDI).

#### Versión vigente
- **Versión 2.0, Revisión B** (vigente desde el 15 de enero de 2024 a la fecha).
- Compatible exclusivamente con CFDI 4.0.

#### Cuándo se emite
- Cuando el CFDI original se emitió como **PPD** (Pago en Parcialidades o Diferido).
- Cada vez que se reciba un pago, sea total o parcial.
- **Plazo de emisión:** a más tardar el quinto día natural del mes inmediato siguiente al que se recibió el pago.

> **Nota importante:** algunas fuentes y guías antiguas siguen mencionando el plazo de 10 días del mes siguiente, que era el vigente antes de 2022. El plazo aplicable hoy es de 5 días naturales (regla 2.7.1.32 RMF 2026).

#### Estructura esencial del REP

El REP tiene una estructura particular: el CFDI es un “cascarón” y el pago va en el complemento.

**En el nodo Comprobante (cascarón):**
- TipoDeComprobante: **P**
- SubTotal: 0
- Total: 0
- Moneda: XXX
- NO se registra MetodoPago ni FormaPago

**En el nodo Complemento (Pagos 2.0):**
- Pago: fecha, forma, moneda, monto, tipo de cambio (si aplica)
- DoctoRelacionado: UUID de la factura original, número de parcialidad, importe del saldo anterior, importe pagado, importe del saldo insoluto
- ImpuestosDR: desglose de impuestos del documento relacionado
- ImpuestosP: totales de impuestos del pago

#### Validaciones críticas que el PAC verifica

Versión 2.0 incluye 23 reglas adicionales de validación. Las más comunes que generan rechazo:

- Que el UUID relacionado exista, esté vigente y sea PPD.
- Que el importe pagado no exceda el saldo insoluto del documento relacionado.
- Que la equivalencia entre monedas (cuando hay tipo de cambio) sea matemáticamente consistente.
- Que los impuestos desglosados en el complemento sean proporcionales a la parte del pago aplicada.

#### Ejemplo numérico para presentar al grupo

| Evento | Fecha | CFDI | Total | Saldo |
|---|---|---|---|---|
| Emisión factura PPD | 15-feb-2026 | I (Ingreso) | $50,000 + IVA | $58,000 |
| Pago 1 (parcialidad) | 10-mar-2026 | P (REP #1) | $0 | Pagado: $30,000 / Insoluto: $28,000 |
| Pago 2 (liquidación) | 28-abr-2026 | P (REP #2) | $0 | Pagado: $28,000 / Insoluto: $0 |

> **Plazos críticos en el ejemplo:**
> - REP #1 debe timbrarse a más tardar el 5-abr-2026.
> - REP #2 debe timbrarse a más tardar el 5-may-2026.

### 3.3 Complemento Carta Porte 3.1 *(20 min)*

Probablemente el complemento que más controversias y multas ha generado.

#### Fundamento legal
- CFF arts. 29 y 29-A
- RMF 2026 reglas 2.7.7.1.1 a 2.7.7.12 (capítulo de Carta Porte)
- Anexo 20 (estructura técnica del complemento)
- CFF art. 103 (presunción de contrabando si se transporta sin Carta Porte)
- CFF art. 84 fracción IV (multas por no expedir o expedir con errores)

#### Versión vigente
- **Versión 3.1**, obligatoria desde el 17 de julio de 2024.
- El SAT actualizó los catálogos del complemento al 13 de enero de 2026 (sin cambiar la estructura, sí los valores válidos: pedimentos del ejercicio 2026, lista IATA 67ª edición de materiales peligrosos, ajuste a tasa IEPS, corrección de descripciones).

#### Quién está obligado

| Sujeto | Tipo de CFDI | Cuándo |
|---|---|---|
| Propietario que mueve mercancía propia | Traslado (T) | Siempre que el traslado implique tramos de jurisdicción federal. |
| Transportista (servicio a terceros) | Ingreso (I) | Siempre que preste el servicio de transporte de carga. |
| Intermediario o agente de transporte | Traslado (T) | Cuando contrata el traslado para un tercero. |

#### Excepción de traslado local
La regla **2.7.7.2.1** de la RMF 2026 establece que NO se requiere Carta Porte para:
- Traslados dentro del mismo municipio o zona metropolitana.
- Que NO impliquen transitar por tramos de jurisdicción federal.
- Para vehículos que no excedan las características del C2 (camión rígido de 2 ejes).

> **Atención:** la mera circulación dentro del mismo municipio no exime si en algún punto del trayecto se utiliza una carretera federal. Esta es la fuente de muchísimas multas en retenes.

#### Información mínima del complemento 3.1

1. **Identificador del complemento (IdCCP):** clave alfanumérica única generada por el sistema.
2. **Ubicaciones:** origen y destino con CP, ID de ubicación, fecha y hora estimadas.
3. **Mercancías:** clave del catálogo c_ClaveProdServCP, descripción detallada (ya no se acepta “mercancía general”), peso en kilogramos, valor de mercancías.
4. **Materiales peligrosos** (cuando aplique): clave del catálogo c_MaterialPeligroso (alineada con NOM-002-SCT y lista IATA vigente).
5. **Autotransporte (cuando aplique):**
   - Permiso SICT: tipo y número.
   - Configuración vehicular (catálogo c_ConfigAutotransporte).
   - Placa, año modelo, peso bruto vehicular conforme a NOM-012-SCT.
   - Datos del seguro.
6. **Figura de transporte:** datos del operador (RFC, CURP, número de licencia), propietario o arrendador del vehículo.
7. **Comercio exterior:** desde la versión 3.1 se incorpora el campo Régimen Aduanero (hasta 10 regímenes). La fracción arancelaria es opcional pero debe corresponder a la mercancía. La Documentación Aduanera (antes Pedimento) debe corresponder al ejercicio vigente.

#### Sanciones

| Concepto | Sanción |
|---|---|
| No expedir CFDI con Carta Porte (CFF art. 83 fracc. VII y 84 fracc. IV) | $19,700 a $112,650 (Anexo 5 RMF 2026, montos actualizados anualmente) |
| Reincidencia | Clausura preventiva de 3 a 15 días |
| Transportar sin CFDI con Carta Porte | Presunción de contrabando (CFF art. 103) — pena de prisión 3 a 6 años (CFF art. 104 fracc. IV) |

#### Cancelación de Carta Porte
- Se requiere **aceptación expresa del receptor** para cancelar.
- Si el complemento ampara hidrocarburos con el Complemento Concepto para Hidrocarburos y Petrolíferos, también requiere aceptación.
- Para gasolina y diésel (regla 2.7.7.1.6 RMF 2026): cancelación sin aceptación únicamente antes de iniciar el traslado; una vez iniciado, ya no se puede cancelar.

### 3.4 Complemento INE *(8 min)*

#### Fundamento
- Artículo 46 del Reglamento de Fiscalización del INE.
- RMF (regla 2.7.1.8 y referencias correlativas).
- Vigente desde el 1 de mayo de 2016 (versión 1.1 desde 1-sep-2016).

#### Quién lo emite
Todos los proveedores de bienes o servicios que vendan a:
- Partidos políticos.
- Coaliciones.
- Asociaciones civiles que respaldan a aspirantes y candidatos independientes.

#### Cuándo es obligatorio
- **Procesos de Precampaña y Campaña:** SIEMPRE, sin importar el monto, para propaganda, espectáculos, eventos electorales, publicidad utilitaria.
- **Proceso Ordinario:** opcional o cuando el receptor lo solicite.

#### Datos que debe contener
- Tipo de Proceso (Ordinario/Precampaña/Campaña)
- Tipo de Comité (Ejecutivo Nacional o Estatal)
- ID o Clave de Contabilidad del INE
- Clave de Entidad Federativa
- Ámbito (Federal o Local)

> **Relevancia para 2026:** aunque las elecciones federales fuertes ya pasaron, hay procesos locales activos en varios estados y siempre conviene tenerlo presente para clientes con esa cartera.

### 3.5 Otros complementos a tener en el radar *(7 min)*

Mención breve para contexto del grupo:

| Complemento | Cuándo aplica |
|---|---|
| **Nómina 1.2** | Pagos de salarios y asimilables (CFDI tipo N). Lo verán a fondo en otro módulo. |
| **Comercio Exterior 2.0** | Exportaciones definitivas de mercancías clave A1, complemento al CFDI de Ingreso. |
| **Leyendas Fiscales** | Para incluir leyendas obligatorias por disposición fiscal (estímulos, frontera norte/sur, etc.). |
| **IEDU** | Pagos por servicios educativos (uso D10) para personas físicas que deduzcan colegiaturas. |
| **Donatarias** | Donativos a donatarias autorizadas (uso D04). |
| **Identificación de Recurso y Minuta de Gastos por Cuenta de Terceros** | Pendiente de publicación, será obligatorio 30 días naturales después de su publicación oficial (RMF 2026). |
| **Concepto Hidrocarburos y Petrolíferos** | Pendiente de publicación, mismo plazo de 30 días. Aplica a sectores específicos. |

### 🤔 Preguntas de reflexión

- ¿En tu cartera de clientes hay alguno que requiera Carta Porte y que actualmente esté operando sin ella o con ella mal llenada? ¿Cuál es la exposición real?
- Para el REP, ¿cómo controlas internamente que no se pase el quinto día del mes siguiente? ¿Es un proceso manual o automatizado?

---

## Bloque 4 — Errores frecuentes y cómo evitarlos *(30 min)*

### 4.1 Top 10 de errores recurrentes en CFDI 4.0 *(15 min)*

A partir de la experiencia acumulada desde 2022 y de los criterios de fiscalización electrónica del SAT para 2026, los errores más frecuentes son:

| # | Error | Consecuencia | Cómo evitarlo |
|---|---|---|---|
| 1 | Discrepancia entre nombre/CP/régimen del receptor y el SAT | El CFDI no timbra | Validar datos con la herramienta del SAT antes de emitir; mantener clientes frecuentes actualizados |
| 2 | Uso de “PUE” cuando realmente fue PPD | Cancelación obligada con motivo 01 + sustitución | Acordar contractualmente la condición de pago antes de emitir |
| 3 | No emitir REP en los 5 días del mes siguiente | Carta invitación por discrepancia IVA | Calendario y alertas automatizadas; revisión semanal |
| 4 | Forma de pago “99 Por definir” en CFDI tipo PUE | Inconsistencia que el SAT detecta en cruces | “99” es exclusivo para PPD; cualquier otro caso debe usar la clave real |
| 5 | Uso de CFDI incompatible con el régimen del receptor | Rechazo en timbrado o detección posterior | Configurar reglas de validación interna por régimen |
| 6 | Cancelación fuera del plazo del ejercicio | Imposibilidad de cancelar; CFDI permanece como ingreso/gasto | Revisión mensual de CFDI por cancelar antes del cierre |
| 7 | Carta Porte con descripción genérica (“mercancía general”) | Multa y posible retención en retén | Especificar la mercancía con la clave correcta del catálogo |
| 8 | Carta Porte con CP/coordenadas aproximadas | Multa por información falsa o incompleta | Capturar coordenadas exactas y validar el CP |
| 9 | Complemento de Pagos sin desglose correcto de impuestos en ImpuestosDR | Rechazo del PAC o discrepancia en IVA | Revisión técnica del XML antes del timbrado |
| 10 | No relacionar UUID al sustituir un CFDI con motivo 01 | Cancelación rechazada o queda como “errores con relación” sin sustento | Aplicar el procedimiento correcto: emitir nuevo CFDI con relación tipo 04 → solicitar cancelación con motivo 01 |

### 4.2 El proceso correcto de cancelación con motivos *(10 min)*

Este es uno de los temas que más se enredan en la práctica. Repaso del esquema vigente:

#### Los 4 motivos de cancelación

| Clave | Motivo | Cuándo aplica | ¿Requiere CFDI nuevo? |
|---|---|---|---|
| **01** | Comprobante emitido con errores **con** relación | Errores en datos que requieren reexpedir (RFC, importes, descripción, etc.) | Sí — debe relacionarse al CFDI sustituto |
| **02** | Comprobante emitido con errores **sin** relación | Errores que no ameritan sustituto (factura duplicada al cliente correcto, p. ej.) | No |
| **03** | No se llevó a cabo la operación | El CFDI se emitió pero la operación nunca ocurrió | No |
| **04** | Operación nominativa relacionada en una factura global | Cliente que estaba en factura global pide CFDI nominativo | Sí — se cancela la global y se emite el nominativo |

#### Procedimiento correcto para motivo 01 (el más usado)

1. **Primero** se emite el nuevo CFDI con los datos corregidos, usando tipo de relación **04 (Sustitución de los CFDI previos)** y registrando el UUID del CFDI a cancelar.
2. **Después** se solicita la cancelación del CFDI original, indicando motivo **01** y registrando el UUID del CFDI sustituto.
3. Si el sistema falla y no permite la cancelación con motivo 01, se puede usar motivo 02 como alternativa (criterio del SAT en preguntas frecuentes).

#### Plazo límite de cancelación

- Regla general: hasta el último día del mes en que se debe presentar la **declaración anual del ISR del ejercicio en que se emitió** el CFDI (CFF art. 29-A, párrafo cuarto).
- Personas morales: a más tardar el 31 de marzo del año siguiente.
- Personas físicas: a más tardar el 30 de abril del año siguiente.
- **RESICO Personas Físicas:** la factura global solo se puede cancelar en el mismo mes que se generó.

#### Cancelación sin aceptación del receptor

La regla **2.7.1.34** de la RMF 2026 mantiene los supuestos que permiten cancelar sin aceptación:
- CFDI emitidos en los 72 horas posteriores a su emisión.
- CFDI con monto total hasta $1,000.00 MXN (IVA incluido).
- CFDI por concepto de nómina (con limitaciones).
- CFDI emitidos a contribuyentes del RIF.
- CFDI tipo Egreso, Traslado y Pago (con matices).
- CFDI con público en general y emitidos a residentes en el extranjero.

> **Nota importante:** el plazo para que el receptor acepte o rechace una solicitud de cancelación es de **3 días hábiles**; si no responde, el SAT da por aceptada (aceptación tácita).

### 4.3 Sanciones específicas por errores en CFDI *(5 min)*

Marco sancionatorio vigente conforme al CFF y al Anexo 5 RMF 2026:

| Conducta | Fundamento | Sanción |
|---|---|---|
| No expedir, no entregar o no poner a disposición el CFDI | CFF art. 83 fracc. VII y 84 fracc. IV | $19,700 a $112,650 |
| Reincidencia en no expedir CFDI | CFF art. 84 fracc. IV | Clausura preventiva 3 a 15 días |
| No cancelar o cancelar fuera de plazo | CFF art. 81 fracc. XLVI y 82 fracc. XLII | 5% a 10% del monto del CFDI |
| Expedir CFDI sin cumplir requisitos del 29-A CFF | CFF art. 83 fracc. VII | $19,700 a $112,650 |
| Asentar datos falsos en el CFDI | CFF art. 83 fracc. VII | Sanción aplicable + posible delito (CFF art. 110) |

### 🤔 Preguntas de reflexión

- ¿Cuál es el error de esta lista que con más frecuencia ves en tu despacho? ¿Por qué crees que se repite?
- ¿Tu sistema o tu PAC te avisa cuando un CFDI se está acercando al límite del plazo de cancelación, o lo descubres en el cierre del año?

---

## Bloque 5 — Impacto fiscal del CFDI en deducciones *(25 min)*

### 5.1 El CFDI como requisito constitutivo, no probatorio *(8 min)*

Esta es probablemente la idea más importante de toda la sesión. Un gasto NO ES DEDUCIBLE simplemente porque se haya pagado y exista un comprobante. La deducibilidad nace cuando concurren TODOS los requisitos del artículo 27 de la LISR. El CFDI es uno de esos requisitos, no es la deducibilidad en sí.

#### Requisitos del artículo 27 LISR (los más relevantes para CFDI)

1. **Fracción I** — Ser **estrictamente indispensable** para los fines de la actividad del contribuyente.
2. **Fracción III** — Estar **amparados con un CFDI** que cumpla los requisitos del CFF.
3. **Fracción III** — Cuando el monto exceda de **$2,000.00**, el pago debe realizarse mediante:
   - Transferencia electrónica de fondos.
   - Cheque nominativo del contribuyente (con la leyenda “para abono en cuenta del beneficiario”).
   - Tarjeta de crédito, débito, servicios o monedero electrónico autorizado por el SAT.
   - **Excepción combustibles:** sin importar el monto (incluso menor a $2,000), el pago debe ser por medios electrónicos.
4. **Fracción IV** — Estar debidamente **registrados en contabilidad** y restados una sola vez.
5. **Fracción V** — Cumplir con las obligaciones de **retención y entero** de impuestos a cargo de terceros (ISR e IVA cuando corresponda).
6. **Fracción VIII** — Pagos a personas físicas, contribuyentes del régimen agropecuario o RIF: deducibles hasta que sean **efectivamente erogados**.
7. **Fracción XVIII** — La fecha del CFDI debe corresponder al **ejercicio por el que se efectúa la deducción** y obtenerse a más tardar el día en que el contribuyente deba presentar la declaración del ejercicio.

> **Caso típico que conviene comentar al grupo:** gasto pagado en diciembre de 2025, CFDI expedido en enero de 2026. ¿En qué ejercicio se deduce? La regla general (fracc. XVIII) es que se deduce en el ejercicio que corresponda a la fecha del CFDI, salvo los supuestos del 27 fracc. XVIII para enajenación de bienes o prestación de servicios cuando el pago ocurra primero o se cumplan otros requisitos específicos.

### 5.2 Acreditamiento de IVA: el CFDI como condición *(7 min)*

El artículo **5 de la LIVA** exige para el acreditamiento del IVA:

| Fracción | Requisito |
|---|---|
| **I** | Que el IVA corresponda a bienes, servicios o uso o goce temporal estrictamente indispensables. |
| **II** | Que el IVA haya sido **trasladado expresamente y por separado** en un CFDI. |
| **III** | Que el IVA haya sido **efectivamente pagado** en el mes de que se trate. |
| **IV** | Tratándose de IVA retenido, que se haya enterado en términos de la LIVA. |
| **V** | Cuando corresponda, prorratear el IVA acreditable conforme a actos gravados/exentos. |

> **Conexión clave con el bloque 1:** el acreditamiento del IVA depende del pago efectivo. Por eso el REP es tan importante: sin REP no hay constancia de pago efectivo y, técnicamente, no procede el acreditamiento del IVA del mes correspondiente al cobro.

### 5.3 Razón de negocio y materialidad: lo que viene después del CFDI *(5 min)*

Aunque el enfoque del diplomado es la ley positiva, conviene mencionar al grupo la línea jurisprudencial y de criterios normativos que el SAT viene aplicando con fuerza:

- **CFF art. 5-A:** facultades de la autoridad para recaracterizar operaciones que carecen de **razón de negocio**.
- **Criterios no vinculativos del Anexo 3 RMF 2026:** prácticas fiscales indebidas, incluyendo el uso indebido de CFDI para inflar deducciones (esquemas EFOS/EDOS).
- **Listas 69 y 69-B del SAT** (publicadas en el portal): contribuyentes que emiten o reciben comprobantes sin sustento (EFOS) y los que les compran (EDOS).

> **Recomendación al grupo:** validar a los proveedores en la lista 69-B antes de aplicar deducciones es hoy una práctica básica de control. Los CFDI de un EFOS pueden ser declarados sin efectos fiscales con efecto retroactivo.

### 5.4 La trampa de “tengo CFDI, tengo deducción” *(5 min)*

Esquema mental para el contador en ejercicio:

```
            ¿Es estrictamente indispensable?  ──── NO ──→ NO DEDUCIBLE
                       │ SÍ
                       ▼
            ¿Hay CFDI 4.0 con datos correctos?  ── NO ──→ NO DEDUCIBLE
                       │ SÍ
                       ▼
            ¿El pago supera $2,000?            ── NO ──→ Pago en cualquier forma OK
                       │ SÍ
                       ▼
            ¿Se pagó por medio bancario?        ── NO ──→ NO DEDUCIBLE
                       │ SÍ
                       ▼
            ¿Se efectuaron las retenciones?     ── NO ──→ NO DEDUCIBLE
                       │ SÍ
                       ▼
            ¿El proveedor está vigente y NO está en lista 69-B?  ── NO ──→ Riesgo alto
                       │ SÍ
                       ▼
            ¿La fecha del CFDI corresponde al ejercicio?   ── NO ──→ NO DEDUCIBLE
                       │ SÍ
                       ▼
                  GASTO DEDUCIBLE
```

> **El CFDI es necesario pero no suficiente para la deducibilidad.** Esta frase debe quedar grabada en el grupo.

### 🤔 Preguntas de reflexión

- En tu práctica, cuando un cliente te presenta una factura, ¿qué validaciones haces antes de aplicarla como deducible? ¿Cuántas de los 7 pasos del esquema realizas en automático?
- Si el SAT te requiriera demostrar la razón de negocio de los gastos más relevantes de un cliente, ¿con qué soportes adicionales al CFDI cuentas?

---

## Bloque 6 — Cierre y enlace con la Clase 2 *(5 min)*

### 6.1 Síntesis de la sesión

Tres ideas para llevarse:

1. El CFDI 4.0 está consolidado y es estable; lo que cambia son los catálogos y las reglas de validación. La disciplina operativa es lo que separa al despacho que tiene cartas invitación cada mes del que no las tiene.
2. Los complementos no son “opcionales” por defecto; cada uno tiene un supuesto de obligatoriedad y la mayoría tienen sanciones específicas asociadas.
3. El CFDI es **condición necesaria pero insuficiente** para la deducibilidad. La fiscalización electrónica del SAT cruza información en automático: la única defensa es la coherencia interna de los datos y la materialidad de las operaciones.

### 6.2 Lectura sugerida (no obligatoria) para llegar preparados a la Clase 2

- **CFF arts. 29 y 29-A** (lectura completa y comentada).
- **Anexo 20 RMF 2026** — Apéndice 7 “Preguntas y respuestas sobre el Anexo 20 versión 4.0”.
- **Guía de llenado del Complemento para Recepción de Pagos** (versión 2.0 Revisión B).
- **Documento del SAT:** “Preguntas frecuentes y escenarios de cancelación conforme a la Reforma Fiscal 2022”.

### 6.3 Qué viene en la Clase 2

- Casos prácticos de emisión correcta de CFDI (con sus complementos).
- Uso de herramientas del SAT: Mis Cuentas, Factura Fácil, Visores.
- Validación del CFDI y cancelaciones paso a paso.
- Revisión del XML y su estructura nodo por nodo.
- Detección de errores fiscales y su corrección práctica.

### 6.4 Pregunta abierta para el cierre

> **¿Cuál es el cambio de proceso interno que vas a implementar esta semana en tu despacho a partir de lo que vimos hoy?**

Invitar a 2 o 3 participantes a compartir su respuesta. Cierra la sesión.

---

## 📚 Referencias normativas citadas en la sesión

### Leyes y Reglamentos
- Código Fiscal de la Federación (CFF), arts. 5-A, 29, 29-A, 29 Bis, 81, 82, 83, 84, 103, 104, 110.
- Ley del Impuesto sobre la Renta (LISR), arts. 27, 28, 99.
- Ley del Impuesto al Valor Agregado (LIVA), art. 5.
- Reglamento del Código Fiscal de la Federación, art. 39.

### Resolución Miscelánea Fiscal 2026 (DOF 28/12/2025)
- Capítulo 2.7 (CFDI), reglas 2.7.1.1, 2.7.1.2, 2.7.1.4, 2.7.1.8, 2.7.1.29, 2.7.1.32, 2.7.1.34, 2.7.1.35.
- Capítulo de Carta Porte, reglas 2.7.7.1.1 a 2.7.7.12 y 2.7.7.1.6.
- Regla 2.7.5.4 (CFDI de retenciones e información de pagos).
- Regla 12.1.4 (residentes en el extranjero por servicios digitales).

### Anexos RMF 2026
- Anexo 3 — Compilación de criterios sobre prácticas fiscales indebidas (publicado 9-ene-2026).
- Anexo 5 — Cantidades actualizadas de multas (publicado 28-dic-2025).
- Anexo 7 — Compilación de criterios normativos fiscales (publicado 9-ene-2026).
- Anexo 20 — Estándar técnico del CFDI 4.0 (Guía de llenado actualizada al 29-dic-2025).

### Documentos técnicos y guías del SAT
- Guía de llenado del CFDI 4.0 (Anexo 20).
- Guía de llenado del Complemento para Recepción de Pagos versión 2.0 Revisión B (vigente desde 15-ene-2024).
- Estándar técnico del Complemento Carta Porte versión 3.1 (vigente desde 17-jul-2024; catálogos actualizados al 13-ene-2026).
- Estándar técnico del Complemento INE versión 1.1 (vigente desde 1-sep-2016).
- Preguntas frecuentes y escenarios de cancelación conforme a la Reforma Fiscal 2022 (publicado 20-dic-2021).

### Otras fuentes
- Reglamento de Fiscalización del INE, art. 46.
- NOM-002-SCT (transporte de materiales y residuos peligrosos).
- NOM-012-SCT (peso bruto vehicular).

---

*Última actualización: mayo de 2026. Documento elaborado con base en la normativa fiscal vigente para el ejercicio 2026. Cualquier modificación posterior a la fecha de elaboración deberá ser verificada en las publicaciones oficiales del SAT.*
