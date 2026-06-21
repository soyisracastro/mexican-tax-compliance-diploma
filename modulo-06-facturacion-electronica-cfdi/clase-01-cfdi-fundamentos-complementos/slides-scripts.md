# Clase 01 — Módulo 6: Facturación Electrónica y CFDI 4.0
## Fundamentos, Complementos e Impacto Fiscal en Deducciones
### Slides con Scripts para Teleprompter

**Duración**: 3 horas 30 minutos efectivos (9:00 am – 1:00 pm, hora centro, con receso 10:30–11:00)
**Contenido activo**: 210 minutos
**Actualización normativa**: Enero 2026 (CFF reforma 14-nov-2025; RMF 2026 DOF 28-dic-2025; Anexo 20 actualizado 29-dic-2025; catálogos Carta Porte 3.1 al 13-ene-2026)

---

## SLIDE 1: Facturación Electrónica y CFDI 4.0

### Contenido Visual

El comprobante que el SAT usa para **fiscalizarte en automático**.

Módulo 6 · Clase 1 de 2 · Enero 2026

Instructor — **LCP Israel Castro**

### Script

"Buenos días. Bienvenidos al Módulo 6 del diplomado. Hoy entramos al documento que más tocamos en el día a día y, paradójicamente, el que peor entendemos: el CFDI.

Les voy a hacer una afirmación incómoda para arrancar. El CFDI dejó de ser una factura hace años. Hoy es la materia prima con la que el SAT pre-llena sus declaraciones, cruza su información y decide a quién le manda carta invitación. Cada vez que ustedes o sus clientes timbran un comprobante, le están entregando al SAT una declaración firmada de lo que pasó. Eso cambia todo.

Durante los próximas horas —con un receso de 30 minutos a media mañana— vamos a recorrer el andamiaje legal del CFDI 4.0, los campos que más rechazos generan, los complementos obligatorios, los errores que provocan cartas invitación, y la conexión directa entre el CFDI y la deducibilidad. Esta clase es de marco y criterio; la Clase 2 es el taller práctico de emisión y validación de XML.

Empecemos."

---

## SLIDE 2: Hoja de Ruta

### Contenido Visual

**6 bloques**.

| Bloque | Tema | Min |
|---|---|---|
| 0 | Apertura y diagnóstico | 15 |
| 1 | Fundamentos del CFDI 4.0 | 45 |
| 2 | Campos obligatorios del receptor | 30 |
| — | **Receso** | 30 |
| 3 | Complementos: Pagos, Carta Porte, INE | 60 |
| 4 | Errores frecuentes y cancelación | 30 |
| 5 | Impacto fiscal en deducciones | 25 |
| 6 | Cierre | 5 |

### Script

"Vean la tabla. Antes del receso cubrimos tres bloques: fundamentos legales del CFDI, los campos del receptor que hacen que un comprobante timbre o se rechace, y por qué eso le importa al SAT.

Después del receso viene el bloque más pesado y más útil: complementos. Le vamos a dedicar una hora completa porque ahí está el Recibo Electrónico de Pago y la Carta Porte, que son las dos fuentes principales de multas y cartas invitación. Cerramos con los errores frecuentes, el procedimiento correcto de cancelación, y la idea más importante de toda la sesión: que tener CFDI no significa tener deducción.

Una nota pedagógica: esta clase es densa en referencias normativas. No quiero que memoricen artículos; quiero que sepan dónde buscar y por qué cada regla existe. Si algo no queda claro, levanten la mano en el momento."

---

# BLOQUE 0 — APERTURA Y DIAGNÓSTICO (15 min) {icon: compass}

---

## SLIDE 3: Diagnóstico Inicial

### Contenido Visual

Tres preguntas antes de empezar:

- ¿Han recibido **carta invitación** por discrepancia CFDI vs declaraciones?
- ¿Han tenido que cancelar un CFDI **fuera del ejercicio**?
- ¿Manejan clientes con **Carta Porte** o complemento INE?

> El módulo son **dos clases**: hoy marco y criterio, la próxima taller práctico.

### Script

"Antes de entrar en materia, quiero tomarle el pulso al grupo con tres preguntas. Levanten la mano —física o virtual— con honestidad, esto es para calibrar la clase, no para exhibir a nadie.

Primera: ¿cuántos han recibido, en los últimos doce meses, al menos una carta invitación del SAT por discrepancias entre los CFDI emitidos y lo declarado? … Tomen nota de cuántas manos suben, porque ese número me dice cuánto tiempo le dedicamos al bloque de errores.

Segunda: ¿quién ha tenido que cancelar un CFDI fuera del ejercicio en que se emitió y se topó con que el sistema ya no lo permitía? Ese es de los dolores más caros.

Tercera: ¿quiénes tienen clientes que mueven mercancía y necesitan Carta Porte, o que le venden a partidos políticos y necesitan complemento INE?

Estas respuestas me permiten ajustar la profundidad sobre la marcha. Encuadremos: este módulo son dos sesiones. Hoy construimos el marco normativo y el criterio. La próxima nos sentamos a emitir, validar XML y cancelar paso a paso. Arrancamos con los fundamentos."

---

# BLOQUE 1 — FUNDAMENTOS DEL CFDI 4.0 (45 min) {icon: scroll-text}

---

## SLIDE 4: Marco Legal Vigente 2026

### Contenido Visual

El CFDI tiene **base legal expresa**, no es acuerdo administrativo.

| Norma | Qué aporta |
|---|---|
| **CFF 29** | Obligación de expedir comprobantes digitales |
| **CFF 29-A** | Catálogo de requisitos del CFDI |
| **CFF 29 Bis** | Reglas de los PAC y validación |
| **RMF 2026** | Cap. 2.7, reglas 2.7.1.1 a 2.7.7.x |
| **Anexo 20** | Estándar técnico XSD del CFDI 4.0 |

> Nota 2026: el **29-A sigue vigente** (la reforma de nov-2025 lo modificó, no lo derogó) y se adicionó el **29-A Bis**. El catálogo de requisitos del CFDI vive en el 29-A.

### Script

"Empecemos por lo que casi nadie repasa: de dónde sale la obligación de facturar electrónicamente. No es un capricho del SAT ni una circular interna. Es ley.

El artículo 29 del Código Fiscal establece la obligación de expedir comprobantes mediante documentos digitales cuando las leyes obliguen a comprobar actos, actividades, ingresos o retenciones. El 29-A es el corazón: ahí está el catálogo de todo lo que debe contener un CFDI —RFC, régimen fiscal, lugar y fecha, datos del receptor, descripción, valor unitario. Cada requisito que veremos hoy nace de ese artículo. El 29 Bis regula a los PAC, los Proveedores Autorizados de Certificación, que son quienes validan y timbran.

Y abajo del Código vive la operación: la Resolución Miscelánea Fiscal 2026 —publicada en el Diario Oficial el 28 de diciembre— en su capítulo 2.7, y el Anexo 20, que es el estándar técnico, el XSD que define la estructura del XML. Un dato tranquilizador: el Anexo 20 mantuvo la estructura del 4.0 sin cambios estructurales. Lo que cambió fueron URLs y una precisión de llenado para productos con nicotina. Esa estabilidad desde abril de 2023 es, en sí misma, señal de que el sistema maduró."

---

## SLIDE 5: Naturaleza Jurídica del CFDI

### Contenido Visual

El CFDI no es una factura digitalizada. Es:

- Un **documento digital con efectos fiscales propios** (CFF 29)
- Una **declaración del contribuyente** sobre la operación
- **Insumo de fiscalización**: el SAT pre-llena ISR e IVA
- **Requisito constitutivo** de deducción y acreditamiento

> No meramente probatorio: **constitutivo**.

### Script

"Esta distinción parece filosófica pero tiene consecuencias prácticas enormes. Muchos contadores siguen tratando el CFDI como la versión PDF de la factura de papel. No lo es.

Primero, es un documento digital con efectos fiscales propios. El sello digital es la manifestación de voluntad del contribuyente: cuando ustedes sellan, están firmando una declaración de que esa operación ocurrió como la describen.

Segundo, y aquí está el cambio de paradigma: el SAT usa los CFDI emitidos y recibidos para pre-llenar las declaraciones de ISR e IVA. Ya no le declaran al SAT lo que pasó; el SAT les propone lo que él ya sabe que pasó, y ustedes ajustan. El que entiende esto deja de pelearse con la autoridad.

Tercero —y esto lo vamos a martillar en el último bloque— el CFDI es requisito constitutivo de la deducibilidad, no meramente probatorio. ¿Qué quiere decir? Que sin CFDI no hay deducción, punto. No es que el CFDI 'pruebe' una deducción que ya existía; es que la deducción nace, en parte, porque existe el CFDI. Guarden esa palabra: constitutivo. Vuelve al final."

---

## SLIDE 6: Estructura Técnica del XML

### Contenido Visual

```
CFDI 4.0 (XML)
├── Comprobante  (versión, serie, folio, fecha, sello, cert.)
│   ├── CfdiRelacionados   (sustitución, devolución…)
│   ├── Emisor   (RFC, Nombre, RégimenFiscal)
│   ├── Receptor (RFC, Nombre, CP, RégimenFiscal, UsoCFDI)
│   ├── Conceptos (ClaveProdServ, ClaveUnidad, ValorUnitario…)
│   ├── Impuestos (totales)
│   └── Complemento (Pagos, CartaPorte, INE, Nómina…)
└── TimbreFiscalDigital  (lo inserta el PAC: UUID, sello SAT)
```

### Script

"No los voy a convertir en programadores, pero sí necesitan tener este mapa mental, porque cuando el PAC les rechaza un timbrado, el error siempre apunta a uno de estos nodos.

Arriba está el nodo Comprobante, que es la raíz: versión, serie, folio, fecha, sello y certificado. Adentro cuelgan los actores: el Emisor con su RFC, nombre y régimen; el Receptor con sus datos —que es donde está el campo de batalla de esta clase—; los Conceptos, que es el detalle de qué se vendió; los Impuestos totales; y el nodo Complemento, donde se anidan los complementos que veremos después del receso.

Y abajo, separado, el Timbre Fiscal Digital. Ojo con esto: el Timbre NO lo pone el contribuyente. Lo inserta el PAC al validar. Ahí nace el UUID, el folio fiscal único, y el sello del SAT. Por eso un CFDI sin timbrar no existe para efectos fiscales: es un borrador. En la Clase 2 vamos a abrir un XML real y recorrer nodo por nodo. Por hoy, quédense con el mapa."

---

## SLIDE 7: Tipos de CFDI Vigentes

### Contenido Visual

| Tipo | Clave | Uso típico |
|---|---|---|
| Ingreso | **I** | Venta, servicios, arrendamiento, honorarios |
| Egreso | **E** | Devoluciones, descuentos, notas de crédito |
| Traslado | **T** | Movimiento de mercancía propia (Carta Porte) |
| Nómina | **N** | Salarios y asimilables (Compl. Nómina 1.2) |
| Pago | **P** | Recepción de pagos (REP, Complemento Pagos 2.0) |

### Script

"Repaso a velocidad media porque ya los conocen, pero conviene reordenar el mapa mental.

Tipo I, Ingreso: es el 90% de lo que emiten. Venta, servicio, arrendamiento, honorarios. Tipo E, Egreso: la nota de crédito, la devolución, el descuento, la bonificación. Aquí un error común: cuando hay que corregir a la baja, no se cancela el ingreso, se emite un Egreso que lo relaciona. Eso lo retomamos en cancelaciones.

Tipo T, Traslado: ampara movimiento de mercancía propia, sin que haya venta, y típicamente carga la Carta Porte. Tipo N, Nómina: salarios y asimilables, con el complemento de Nómina 1.2 —ese lo verán a fondo en otro módulo—. Y tipo P, Pago: el Recibo Electrónico de Pago, que carga el Complemento de Pagos 2.0.

Hay un sexto, el de Retenciones e información de pagos, que es un documento técnico distinto al del Anexo 20 principal, regulado en la regla 2.7.5.4. Lo menciono para que sepan que existe, pero no es nuestro foco hoy. El protagonista del día a día es la pareja I y P, y por qué se relacionan es el siguiente slide."

---

## SLIDE 8: Método vs. Forma de Pago

### Contenido Visual

Dos campos distintos que se confunden todo el tiempo:

**Método de pago** — *cómo se acuerda liquidar*:
- **PUE** — Pago en Una sola Exhibición
- **PPD** — Pago en Parcialidades o Diferido

**Forma de pago** — *qué medio se usa* (catálogo c_FormaPago):
- 01 Efectivo · 03 Transferencia · 04 Tarjeta… **99 Por definir**

### Script

"Esta distinción merece tiempo porque es la causa de la mitad de las cartas invitación que recibe el grupo. Y casi nadie la explica bien.

Método de pago responde a CÓMO se acuerda liquidar la operación. Solo hay dos opciones: PUE, Pago en Una sola Exhibición, que significa que el pago ocurre al emitir el comprobante o antes; y PPD, Pago en Parcialidades o Diferido, que significa que el pago llega después de emitir el CFDI.

Forma de pago es otra cosa completamente distinta: responde a QUÉ medio físico o electrónico se usó. Es el catálogo c_FormaPago: 01 efectivo, 02 cheque, 03 transferencia, 04 tarjeta de crédito, y así hasta la clave 99, 'Por definir'.

¿Por qué se confunden? Porque están uno al lado del otro en la pantalla del sistema de facturación, y mucha gente captura en automático. El error clásico es poner método PUE con forma de pago '99 Por definir'. Eso es una contradicción lógica que el SAT detecta de inmediato: si fue en una sola exhibición, ya sabes con qué se pagó; el '99' no tiene sentido ahí. En el siguiente slide les doy las cuatro reglas que tienen que internalizar para no volver a equivocarse."

---

## SLIDE 9: Reglas Críticas PUE / PPD

### Contenido Visual

- **PUE** exige forma de pago real (01, 03, 04…). **Nunca 99**.
- **PPD** siempre lleva **99 Por definir** + REP al cobrar.
- ¿Emitiste PUE pero cobraron semanas después? Debió ser **PPD**.
- El **IVA se causa al cobro efectivo**, no con la fecha del CFDI.

> Corregir un PUE mal puesto = cancelación motivo **01** + sustitución.

### Script

"Cuatro reglas. Si se las llevan tatuadas, evitan el 80% de los problemas de IVA.

Una: si es PUE, va forma de pago real. La que sea, pero real. Jamás el 99 en un PUE.

Dos: si es PPD, la forma de pago siempre es 99 'Por definir', y cuando llegue el cobro están obligados a emitir el CFDI tipo P con Complemento de Pagos. Eso no es opcional.

Tres, y esta es la trampa más cara: si emitieron un PUE pero el cliente paga semanas o meses después, técnicamente debieron emitirlo como PPD desde el inicio. Cuando lo cobran tarde, ya están en falta. Corregirlo implica cancelar con motivo 01 y sustituir. Por eso conviene acordar la condición de pago ANTES de timbrar.

Cuatro, la regla que lo explica todo: el IVA se causa con el cobro efectivo, no con la fecha del CFDI. Esto es flujo de efectivo, igual que vimos en personas físicas. Por eso el Complemento de Pagos es insumo directo del IVA mensual, y por eso el SAT cruza esta información de forma tan agresiva: si ustedes facturaron en enero pero cobraron en marzo, el IVA va en marzo, y el SAT lo sabe por el REP. Sin REP, ese cruce truena."

---

## SLIDE 9B: PUE vs PPD lado a lado

### Contenido Visual

**PUE — pago en una sola exhibición** | **PPD — pago en parcialidades o diferido**

| Característica | PUE | PPD |
|---|---|---|
| Ejemplo en clase | F-2026001 | F-2026000 |
| Forma de pago | 03 · se conoce al facturar | 99 · por definir |
| Cuándo se cobra | al emitir la factura | después, una o varias veces |
| CFDI que genera | uno solo (tipo I) | factura (I) + un REP (P) por pago |
| Efecto en IVA | se causa al facturar | se causa con cada REP (flujo) |
| ¿Genera REP? | No | Sí, obligatorio |

> Regla rápida: si cobras al emitir, es PUE. Si cobras después, es PPD y emites un REP por cada pago.

### Script

Esta es la diferencia que más confunde y la que más rebota facturas. Véanlo lado a lado.

A la izquierda, PUE: el pago en una sola exhibición. Cobras al momento de facturar, ya sabes con qué forma de pago, y todo queda en un solo CFDI tipo Ingreso. El IVA se causa ahí mismo, con esa factura, y no hay nada más que emitir.

A la derecha, PPD: pago en parcialidades o diferido. Aquí la factura nace "incompleta" a propósito: la forma de pago va como 99, "por definir", porque al emitirla todavía no sabes ni cómo ni cuándo te van a pagar. Y por cada pago que recibas después, tienes que emitir un REP, un CFDI tipo Pago.

El punto fino, y que conecta con el papel de trabajo, es el IVA. En PUE el IVA se causa con la factura. En PPD el IVA se causa con cada REP, conforme cobras. Por eso una sola factura puede repartir su IVA en varios meses: nuestro ejemplo F-2026000 lo causa en marzo y en abril, no en febrero cuando se emitió.

La regla para no equivocarse es simple: si cobras al emitir, PUE. Si cobras después, PPD más un REP por cada pago.

---

## SLIDE 10: Reflexión — PUE vs PPD

### Contenido Visual

Para discutir con el grupo:

- ¿Qué % de los CFDI de sus clientes son realmente **PUE vs PPD**?
- ¿Tienen al cliente que "factura todo PUE porque es más fácil" pero cobra a **30/60/90 días**?
- Si llegara carta invitación de IVA, ¿en cuánto **reconcilian** CFDI emitidos vs cobros?

### Script

"Hagamos una pausa de criterio antes de seguir. No necesito respuestas en voz alta de todos, pero quiero que cada quien piense en su cartera real.

Primera: de los CFDI que emiten sus clientes, ¿qué porcentaje son honestamente PUE y qué porcentaje son PPD? La mayoría me va a decir 'casi todo PUE'. Y casi siempre es mentira operativa: facturan PUE porque es más fácil, pero cobran a crédito.

Ahí está la segunda pregunta, que es la trampa: el cliente que 'factura todo PUE porque es más fácil' pero cobra a 30, 60 o 90 días, está acumulando IVA que reportó como cobrado y no cobró, o al revés, dependiendo de cómo lo registren. El riesgo fiscal real es una discrepancia de IVA que tarde o temprano el SAT detecta.

Y la tercera, la de oro: si mañana les llega una carta invitación por discrepancia de IVA de un cliente, ¿en cuánto tiempo podrían reconciliar los CFDI emitidos contra los pagos efectivamente cobrados? Si la respuesta es 'no sé' o 'semanas', ahí tienen su primer proyecto de mejora de proceso. Lo retomamos en el cierre. Pasamos a los campos del receptor."

---

# BLOQUE 2 — CAMPOS OBLIGATORIOS DEL RECEPTOR (30 min) {icon: user-check}

---

## SLIDE 11: Del 3.3 al 4.0

### Contenido Visual

El CFDI 4.0 es obligatorio desde el **1-abr-2023**. Para 2026 es la **única versión válida**.

El cambio más doloroso: **datos del receptor** que antes no eran obligatorios y hoy el SAT **valida de forma estricta**.

- Nombre / Razón social
- Código Postal del domicilio fiscal
- Régimen fiscal del receptor

### Script

"Hagamos memoria corta. El CFDI 4.0 entró en vigor el 1 de enero de 2022, convivió un tiempo con la versión 3.3, y se volvió obligatorio el 1 de abril de 2023. Para 2026 no hay debate: la 4.0 es la única versión válida. Quien todavía hable de la 3.3 está hablando de historia.

¿Cuál fue el cambio que más dolió y que más rechazos sigue generando hoy? La inclusión de datos del receptor que en la 3.3 eran opcionales o ni existían, y que ahora el SAT valida de forma estricta contra su propia base de datos.

Son tres campos, los que ven en pantalla: nombre o razón social, código postal del domicilio fiscal, y régimen fiscal del receptor. Parece trivial. No lo es. Estos tres campos son responsables de la mayoría de los timbrados que truenan a la primera. Y lo peor: muchas veces el error no es del emisor, es que el receptor tiene mal sus propios datos en el SAT. Vamos uno por uno."

---

## SLIDE 12: Los Tres Campos Críticos

### Contenido Visual

Deben coincidir **EXACTAMENTE** con lo registrado en el SAT:

- **Nombre**: sin régimen societario, sin abreviaturas, tal cual la Constancia
- **CP**: el del **domicilio fiscal**, no el de la sucursal
- **Régimen**: clave vigente de c_RegimenFiscal (601, 605, 612, 626…)

> "MARÍA GUADALUPE" ≠ "MA. GUADALUPE". El acento y el guion **importan**.

### Script

"La palabra clave de este slide es EXACTAMENTE. No 'parecido', no 'casi'. Idéntico a lo registrado en el SAT.

El nombre: persona física sin régimen societario y sin abreviaturas, exactamente como aparece en la Constancia de Situación Fiscal. Persona moral, razón social completa, normalmente en mayúsculas y sin punto final. El caso típico que tumba timbrados: 'MARÍA GUADALUPE LÓPEZ HERNÁNDEZ' contra 'MA. GUADALUPE LOPEZ HERNANDEZ'. El acento importa, la abreviatura importa, el guion importa. El sistema no perdona.

El código postal: es el del domicilio fiscal del receptor, no el de la sucursal donde se hizo la venta ni el del proyecto. Y debe coincidir con el CP que el receptor tiene registrado en su RFC. Si el cliente cambió de domicilio y no presentó el aviso, el CFDI no va a timbrar, y no es culpa de ustedes.

El régimen fiscal: la clave del catálogo c_RegimenFiscal. 601 General de personas morales, 605 Sueldos y Salarios, 612 Actividad Empresarial y Profesional, 626 RESICO. Debe ser un régimen vigente del receptor al momento de emitir. Y atención: si el cliente tributa en varios regímenes, debe indicar cuál aplica para esa operación específica. Eso conecta con el uso del CFDI, que es el siguiente slide."

---

## SLIDE 13: Uso del CFDI

### Contenido Visual

El uso debe ser **congruente con el régimen** del receptor.

| Clave | Uso |
|---|---|
| **G03** | Gastos en general |
| **G01** | Adquisición de mercancías |
| **D01–D10** | Deducciones personales (médicos, educación…) |
| **CP01** | Pagos (exclusivo tipo P) |
| **S01** | Sin efectos fiscales |

> Un asalariado (605) **no puede** recibir un CFDI con uso G03. El sistema lo rechaza.

### Script

"Ya quedó atrás la época del 'P01 Por definir' como salida fácil. Hoy el catálogo c_UsoCFDI obliga al receptor a declarar el destino del comprobante, y aquí está la regla que casi nadie aplica bien: el uso del CFDI debe ser congruente con el régimen fiscal del receptor.

Los más comunes: G03 gastos en general, G01 adquisición de mercancías, los D que son deducciones personales de personas físicas —D01 honorarios médicos, D10 servicios educativos—, CP01 que es exclusivo de los CFDI tipo P con complemento de pagos, y S01, 'sin efectos fiscales', para operaciones con público en general o donativos no deducibles.

El ejemplo que más confunde: una persona física en régimen de sueldos y salarios, clave 605, NO puede recibir un CFDI con uso G03 'gastos en general'. ¿Por qué? Porque ese régimen no permite deducir gastos generales. El sistema lo rechaza en el timbrado. Si un asalariado les pide que le facturen su comida de negocios con uso G03, el comprobante no va a pasar, y aunque pasara, no le serviría. Esa congruencia régimen-uso es de las primeras validaciones que conviene configurar en el sistema."

---

## SLIDE 14: La Trampa de la Constancia

### Contenido Visual

El SAT **prohíbe** condicionar la emisión del CFDI a la entrega física de la Constancia de Situación Fiscal.

> Desde 2026 es **infracción de ley**: CFF **83-IX** (infracción) y **84-VI** (sanción) — multa **$21,420 a $122,440** y, en reincidencia, **clausura 3 a 15 días**.

Pero el emisor **necesita los datos**. La salida:

- Pedir los datos por escrito (correo, formulario), no exigir el documento
- Protocolo de actualización **anual** de clientes frecuentes

### Script

"Este punto genera fricción real en los mostradores, así que conviene aclararlo bien.

El SAT prohíbe expresamente condicionar la emisión de un CFDI a que el cliente entregue físicamente su Constancia de Situación Fiscal. Y ojo con esto, porque para 2026 dejó de ser solo un criterio administrativo: la reforma lo subió a infracción expresa del artículo 83, fracción IX del Código, sancionada por el 84, fracción VI, con multa de 21,420 a 122,440 pesos y, en reincidencia, clausura preventiva de 3 a 15 días. Antes vivía como el criterio 1/CFF del Anexo 3; hoy es de ley. O sea: el comercio que pone el letrero de 'sin constancia no facturamos' ya no comete solo una práctica indebida, comete una infracción con multa, y el cliente puede denunciarlo.

Pero —y aquí está la tensión— el emisor genuinamente necesita los datos correctos para timbrar: nombre, CP y régimen, que es justo lo que vimos. ¿Cómo se resuelve sin caer en la práctica indebida?

La práctica recomendada: soliciten los datos por escrito —un correo, un formulario web, una ficha de alta de cliente—, pero no exijan el documento físico como condición. Y para clientes frecuentes, monten un protocolo de actualización al menos anual, porque la gente cambia de régimen, se da de alta en RESICO, se sale, cambia de domicilio, y nadie avisa. El que tiene sus catálogos de clientes actualizados timbra a la primera; el que no, vive rechazando y reintentando. Con esto cerramos el bloque 2. Vamos al receso."

---

# RECESO (30 min) {icon: coffee}

---

## SLIDE 15: Receso

### Contenido Visual

**30 minutos.**

Regresamos con el bloque más operativo: **complementos**.

### Script

"Treinta minutos de receso. Estírense, tomen café, revisen el celular. Cuando regresemos entramos al bloque más largo y más útil de la clase: los complementos. Ahí vive el Recibo Electrónico de Pago y la Carta Porte, que son las dos cosas que más multas y cartas invitación generan en este país. No se me pierdan, porque empezamos puntuales."

---

# BLOQUE 3 — COMPLEMENTOS: PAGOS, CARTA PORTE, INE (60 min) {icon: puzzle}

---

## SLIDE 16: ¿Qué es un Complemento?

### Contenido Visual

Un **nodo XML adicional** anidado en el nodo Complemento, para información específica de un sector u operación.

Tres reglas que rigen a todos:

- **Obligatorios** por sector u operación — no opcionales
- **Validación adicional** del PAC antes de timbrar
- Nuevos complementos: obligatorios **30 días** tras su publicación

### Script

"Retomamos. Un complemento es, técnicamente, un nodo XML adicional que se anida dentro del nodo Complemento que vimos en el mapa del XML. El SAT los publica para capturar información que no cabe en el comprobante genérico: datos de transporte, datos electorales, datos de comercio exterior.

Tres reglas generales que aplican a TODOS los complementos, sin excepción.

Una: no son opcionales. Cada complemento tiene un supuesto de obligatoriedad. En el momento en que la operación cae en ese supuesto, el complemento se vuelve obligatorio. El error mental de 'es opcional' es carísimo.

Dos: cada complemento tiene sus propias reglas de validación, adicionales a las del CFDI, que el PAC debe verificar antes de timbrar. Por eso un complemento mal llenado rebota.

Tres, una regla de calendario que conviene tener presente: cuando el SAT publica un complemento nuevo, la Miscelánea 2026 establece que se vuelve obligatorio 30 días naturales después de su publicación en el portal. Eso les da una ventana corta para prepararse. Vamos con el complemento que más impacta el día a día: el de pagos."

---

## SLIDE 17: REP — Recepción de Pagos 2.0

### Contenido Visual

El complemento que más impacta al contador. También "Recibo Electrónico de Pago".

- Fundamento: **CFF 29-A fr. VII inc. b)**; RMF 2.7.1.32 y 2.7.1.35
- Versión **2.0 Rev. B** (desde 15-ene-2024), solo con CFDI 4.0
- Se emite cuando el CFDI original fue **PPD**, cada vez que se cobra
- Plazo: **5º día natural** del mes siguiente al cobro

> Cuidado: el plazo de "10 días" es de antes de 2022. Hoy son **5**.

### Script

"El Recibo Electrónico de Pago, el REP, es el complemento que más les va a tocar. Cada vez que un cliente factura PPD y luego cobra, hay que emitir un REP.

Su fundamento está en el 29-A fracción VII inciso b) del Código, y en las reglas 2.7.1.32 y 2.7.1.35 de la Miscelánea. La versión vigente es la 2.0 Revisión B, vigente desde el 15 de enero de 2024, compatible exclusivamente con CFDI 4.0.

¿Cuándo se emite? Cuando el CFDI original se emitió como PPD, y cada vez que se recibe un pago, sea total o parcial. Si hay tres parcialidades, hay tres REP.

Y el plazo, que es donde más gente se quema: a más tardar el quinto día natural del mes inmediato siguiente a aquel en que se recibió el pago. Subrayo esto porque hay guías viejas y hasta cursos que siguen diciendo 'diez días'. El plazo de diez días era el de antes de 2022. Hoy son cinco días naturales, regla 2.7.1.32. Si cobraron el 20 de marzo, el REP tiene que estar timbrado a más tardar el 5 de abril. Punto."

---

## SLIDE 18: Estructura del REP

### Contenido Visual

El CFDI tipo P es un **"cascarón"**: el pago va en el complemento.

**Comprobante (cascarón):**
- TipoDeComprobante **P** · SubTotal **0** · Total **0** · Moneda XXX
- **No** se registra MetodoPago ni FormaPago

**Complemento (Pagos 2.0):**
- Pago · DoctoRelacionado (UUID, parcialidad, saldos) · ImpuestosDR · ImpuestosP

### Script

"El REP tiene una estructura que descoloca al que lo ve por primera vez, porque parece que está vacío. Y es a propósito.

El nodo Comprobante del REP es un cascarón: tipo de comprobante P, SubTotal cero, Total cero, moneda XXX. Y aquí lo que más confunde: en el cascarón NO se registra método de pago ni forma de pago. La gente lo busca y no lo encuentra, y cree que está mal. No está mal: la información del pago no va arriba, va en el complemento.

En el nodo Complemento, el de Pagos 2.0, vive todo lo importante. El nodo Pago, con la fecha, la forma, la moneda, el monto y el tipo de cambio si aplica. El DoctoRelacionado, que liga este pago con la factura original: ahí va el UUID de la factura, el número de parcialidad, el saldo anterior, el importe pagado y el saldo insoluto. Y dos nodos de impuestos: ImpuestosDR, que desglosa los impuestos del documento relacionado, e ImpuestosP, que son los totales del pago.

Esa estructura cascarón-más-complemento es lo que tienen que tener clarísimo, porque cuando el PAC rechace un REP, el error casi siempre está en el DoctoRelacionado o en el desglose de impuestos."

---

## SLIDE 19: REP — Validaciones y Ejemplo

### Contenido Visual

La versión 2.0 trae **23 reglas** adicionales. Las que más rechazan:

- UUID relacionado debe existir, estar vigente y ser **PPD**
- Importe pagado **no excede** el saldo insoluto

| Evento | Fecha | CFDI | Saldo |
|---|---|---|---|
| Factura PPD | 15-feb | I · $58,000 | $58,000 |
| Pago 1 | 10-mar | P (REP #1) | Insoluto $28,000 |
| Pago 2 | 28-abr | P (REP #2) | Insoluto $0 |

> REP #1 → a más tardar **5-abr** · REP #2 → a más tardar **5-may**.

### Script

"La versión 2.0 del complemento incluye 23 reglas de validación adicionales. No las vamos a memorizar, pero sí las que más rechazos generan.

Una: el UUID que relacionan tiene que existir, estar vigente —no cancelado— y ser PPD. Si intentan relacionar un pago a una factura PUE, rebota, porque una PUE ya estaba pagada. Dos: el importe pagado no puede exceder el saldo insoluto del documento. Si la factura debía 28 mil y reportan un pago de 30 mil, truena. Tres y cuatro: consistencia de tipo de cambio cuando hay monedas distintas, y proporcionalidad de los impuestos desglosados respecto a la parte del pago aplicada.

Veamos el ejemplo de la tabla, que es el caso de la vida real. El 15 de febrero se emite una factura PPD por 58 mil pesos con IVA. El 10 de marzo el cliente abona 30 mil: se emite el REP número uno, queda un insoluto de 28 mil. El 28 de abril liquida los 28 mil restantes: REP número dos, saldo cero.

Ahora la parte crítica, los plazos. El pago de marzo obliga a timbrar el REP a más tardar el 5 de abril. El pago de abril, a más tardar el 5 de mayo. Si se les pasa cualquiera de esas fechas, llega carta invitación por discrepancia de IVA, porque el SAT ve el depósito en el banco pero no ve el REP que lo ampara."

---

## SLIDE 20: Carta Porte 3.1 — Quién está Obligado

### Contenido Visual

El complemento que más controversias y multas genera.

- Versión **3.1**, obligatoria desde **17-jul-2024**; catálogos act. 13-ene-2026

| Sujeto | CFDI | Cuándo |
|---|---|---|
| Dueño que mueve mercancía propia | **T** | Tramos de jurisdicción federal |
| Transportista (servicio a terceros) | **I** | Siempre que preste el servicio |
| Intermediario / agente | **T** | Cuando contrata el traslado |

### Script

"Carta Porte. Probablemente el complemento que más dolores de cabeza ha generado desde que existe. La versión vigente es la 3.1, obligatoria desde el 17 de julio de 2024. El SAT actualizó los catálogos al 13 de enero de 2026 —sin cambiar la estructura, pero sí los valores válidos: pedimentos del ejercicio 2026, la lista IATA de materiales peligrosos en su edición 67, ajustes de tasa de IEPS—.

¿Quién está obligado? Tres figuras. El dueño que mueve su propia mercancía emite un CFDI de Traslado, tipo T, con Carta Porte, siempre que el traslado implique tramos de jurisdicción federal. El transportista que presta servicio a terceros emite un CFDI de Ingreso, tipo I, con Carta Porte, siempre que preste el servicio de transporte de carga. Y el intermediario o agente de transporte emite Traslado cuando contrata el traslado para un tercero.

La pregunta que siempre surge: '¿y si solo muevo mercancía aquí cerquita?' Esa es la excepción del siguiente slide, y es donde está la trampa de la mayoría de las multas en retén."

---

## SLIDE 21: Carta Porte — Excepción Local e Info Mínima

### Contenido Visual

**Excepción local (regla 2.7.7.2.1):** mismo municipio o zona metropolitana, sin tramos federales, vehículo hasta **C2**.

> La circulación local NO exime si en algún punto se usa **carretera federal**.

Info mínima del 3.1: **IdCCP**, ubicaciones con CP/hora, mercancías con clave de catálogo y **peso**, autotransporte (permiso SICT, placa), figura de transporte (operador), régimen aduanero.

### Script

"La regla 2.7.7.2.1 establece la excepción de traslado local. No se requiere Carta Porte cuando se cumplen tres condiciones juntas: el traslado es dentro del mismo municipio o zona metropolitana, NO implica transitar por tramos de jurisdicción federal, y el vehículo no excede las características de un C2, que es un camión rígido de dos ejes.

Aquí está la trampa que llena los retenes de multas: la gente cree que por moverse 'dentro de la ciudad' está exenta. Falso. Si en cualquier punto del trayecto, aunque sea un tramo corto, se usa una carretera federal, la excepción se cae y se necesita Carta Porte. Esa interpretación errónea es la fuente de muchísimas sanciones.

Sobre la información mínima del complemento 3.1, sin agotarla: el IdCCP, que es el identificador único; las ubicaciones de origen y destino con código postal, fecha y hora estimadas; las mercancías con su clave de catálogo —ya no se acepta 'mercancía general'— y su peso en kilogramos; los datos del autotransporte, con permiso SICT, placa, año y peso bruto; la figura de transporte, que es el operador con su RFC, CURP y licencia; y desde la 3.1 el régimen aduanero para comercio exterior. La descripción genérica y el peso aproximado son dos de los errores que más multan."

---

## SLIDE 22: Carta Porte — Sanciones y Cancelación

### Contenido Visual

| Concepto | Sanción |
|---|---|
| No expedir CFDI con Carta Porte | **$19,700 a $112,650** |
| Reincidencia | Clausura **3 a 15 días** |
| Transportar sin Carta Porte | Presunción de **contrabando** (CFF 103) — prisión **3 a 6 años** |

**Cancelación:** requiere aceptación del receptor. Gasolina/diésel: solo **antes** de iniciar el traslado (2.7.7.1.6).

### Script

"Las sanciones de Carta Porte son las más severas de todo el universo CFDI, así que vale la pena que el grupo las dimensione.

No expedir el CFDI con Carta Porte, o expedirlo con errores, va de 19,700 a 112,650 pesos, montos del Anexo 5 que se actualizan cada año. La reincidencia escala a clausura preventiva de 3 a 15 días. Y la más grave, que mucha gente no sabe: transportar mercancía sin el CFDI con Carta Porte genera presunción de contrabando, artículo 103 del Código, con pena de prisión de 3 a 6 años conforme al 104. O sea, esto deja de ser una multa administrativa y se convierte en materia penal. Cuando un cliente transportista les diga 'al rato la saco', recuérdenle que está jugando con una presunción de contrabando.

Sobre la cancelación: la Carta Porte requiere aceptación expresa del receptor para cancelarse. Y hay un caso especial muy importante: para gasolina y diésel, regla 2.7.7.1.6, solo se puede cancelar sin aceptación antes de iniciar el traslado. Una vez que el viaje arrancó, ya no se puede cancelar. Punto. Eso obliga a una disciplina enorme en el sector combustibles."

---

## SLIDE 23: Complemento INE y Otros

### Contenido Visual

**INE** (Reglamento Fiscalización INE art. 46): quien venda a **partidos, coaliciones, candidatos independientes**.
- Precampaña y Campaña: **siempre**, sin importar monto · Ordinario: opcional

| Otros complementos | Cuándo |
|---|---|
| Comercio Exterior 2.0 | Exportaciones definitivas A1 |
| IEDU | Colegiaturas deducibles (uso D10) |
| Leyendas Fiscales | Estímulos, frontera |

### Script

"Cerramos complementos con un repaso rápido. El complemento INE: lo emiten todos los proveedores de bienes o servicios que le venden a partidos políticos, coaliciones, o asociaciones civiles que respaldan candidatos independientes. Su fundamento es el artículo 46 del Reglamento de Fiscalización del INE. La regla de oro: en procesos de precampaña y campaña es obligatorio siempre, sin importar el monto, para propaganda, espectáculos, eventos, publicidad. En proceso ordinario es opcional o cuando el receptor lo pida. Aunque las elecciones federales fuertes ya pasaron, hay procesos locales activos en varios estados en 2026, así que téngalo presente si tienen clientes con esa cartera.

Y en el radar, sin profundizar: Comercio Exterior 2.0 para exportaciones definitivas clave A1; el complemento IEDU para colegiaturas deducibles con uso D10, que les va a importar en la temporada de anual; Leyendas Fiscales para estímulos y zona fronteriza; Nómina 1.2, que verán a fondo en otro módulo; y dos que están pendientes de publicación —el de gastos por cuenta de terceros y el de hidrocarburos—, que serán obligatorios 30 días después de su publicación. Con esto cerramos el bloque de complementos y pasamos a los errores."

---

# BLOQUE 4 — ERRORES FRECUENTES Y CANCELACIÓN (30 min) {icon: triangle-alert}

---

## SLIDE 24: Top de Errores Recurrentes

### Contenido Visual

| Error | Consecuencia |
|---|---|
| Nombre/CP/régimen del receptor mal | No timbra |
| PUE cuando fue PPD | Cancelación motivo 01 + sustitución |
| No emitir REP en 5 días | Carta invitación IVA |
| "99 Por definir" en un PUE | Cruce inconsistente |
| Carta Porte "mercancía general" | Multa + retención en retén |
| No relacionar UUID al sustituir | Cancelación rechazada |

### Script

"Esta tabla es el resumen de todo lo que hemos visto, pero ordenado por frecuencia de aparición en la práctica. Es, básicamente, el catálogo de cómo se pierde dinero y se reciben cartas invitación.

El número uno, lejos: discrepancia entre nombre, CP o régimen del receptor y lo que tiene el SAT. Resultado: el CFDI no timbra. Se evita validando datos antes de emitir y manteniendo actualizados a los clientes frecuentes.

El dos: usar PUE cuando en realidad fue PPD. Ya lo vimos: obliga a cancelar con motivo 01 y sustituir. Se evita acordando la condición de pago por contrato antes de emitir.

El tres: no emitir el REP dentro de los cinco días del mes siguiente. Carta invitación por discrepancia de IVA. Se evita con calendario y alertas automatizadas, revisión semanal.

El cuatro: el '99 Por definir' en un PUE, esa contradicción que el SAT detecta en automático. El de Carta Porte con 'mercancía general' que multan en retén. Y el último, muy técnico pero muy común: no relacionar el UUID cuando sustituyen un CFDI. Eso nos lleva directo al procedimiento de cancelación, que es el siguiente slide."

---

## SLIDE 25: Los 4 Motivos de Cancelación

### Contenido Visual

| Clave | Motivo | ¿CFDI nuevo? |
|---|---|---|
| **01** | Errores **con** relación | Sí — se relaciona al sustituto |
| **02** | Errores **sin** relación | No |
| **03** | No se llevó a cabo la operación | No |
| **04** | Operación nominativa en factura global | Sí |

> El **01** es el más usado. Tiene un orden obligatorio.

### Script

"El tema que más se enreda en la práctica: la cancelación con motivos. Desde 2022 ya no se cancela 'porque sí'; hay que declarar por qué, con una de cuatro claves.

Motivo 01: comprobante emitido con errores CON relación. Es decir, hay un error en datos —RFC, importes, descripción— que obliga a reexpedir. Requiere emitir un CFDI sustituto y relacionarlo. Es el más usado, con diferencia.

Motivo 02: errores SIN relación. Errores que no ameritan sustituto, por ejemplo una factura duplicada al cliente correcto. No requiere CFDI nuevo.

Motivo 03: no se llevó a cabo la operación. El CFDI se emitió pero la operación nunca ocurrió. No requiere sustituto.

Motivo 04: operación nominativa que estaba incluida en una factura global. El cliente que estaba en la global pide su CFDI nominativo: se cancela la global y se emite el nominativo. Requiere CFDI nuevo.

El que tienen que dominar es el 01, porque tiene un orden obligatorio que si lo hacen al revés, rebota. Eso es el siguiente slide."

---

## SLIDE 26: Procedimiento Motivo 01 y Plazos

### Contenido Visual

**Orden correcto del motivo 01:**
1. Primero emites el **CFDI nuevo** (relación tipo **04 Sustitución**, con UUID del original)
2. Después cancelas el original (motivo **01**, con UUID del sustituto)

**Plazo de cancelación** (CFF 29-A):
- PM: hasta **31-mar** del año siguiente
- PF: hasta **30-abr** del año siguiente
- RESICO factura global: **mismo mes**

### Script

"El procedimiento del motivo 01 tiene un orden que la mayoría hace al revés, y por eso les rebota.

Primero se emite el CFDI nuevo, el corregido, usando tipo de relación 04 —sustitución de los CFDI previos— y registrando el UUID del comprobante que van a cancelar. Primero el nuevo. Después, y solo después, se solicita la cancelación del original, indicando motivo 01 y registrando el UUID del sustituto que acaban de crear. Si lo hacen al revés —cancelan primero y luego intentan sustituir— el sistema se confunde y queda como 'error sin relación'. Si el sistema de plano no permite la cancelación con motivo 01, el propio SAT acepta en sus preguntas frecuentes usar el motivo 02 como alternativa.

Y los plazos, que son críticos para el cierre del año. La regla general: se puede cancelar hasta el último día del mes en que se debe presentar la declaración anual del ISR del ejercicio en que se emitió. Aterrizado: personas morales, a más tardar el 31 de marzo del año siguiente; personas físicas, a más tardar el 30 de abril. Y un caso especial que se les escapa a muchos: RESICO personas físicas, la factura global solo se puede cancelar en el mismo mes en que se generó. Después, ya no."

---

## SLIDE 27: Cancelación sin Aceptación y Sanciones

### Contenido Visual

**Sin aceptación del receptor (regla 2.7.1.35):** dentro de **72 hrs**, monto ≤ **$1,000**, nómina, egreso/traslado, público en general. **El REP ya no entra** (RMF 2026).

> Plazo del receptor para responder: **3 días hábiles**. Si calla → **aceptación tácita**.

| Conducta | Sanción |
|---|---|
| No cancelar o fuera de plazo | **5% a 10%** del monto |
| Datos falsos en CFDI | Multa + posible delito (CFF 110) |

### Script

"Dos cosas para cerrar cancelación. La primera: no todas las cancelaciones requieren que el receptor diga que sí. La regla 2.7.1.35 mantiene los supuestos donde se puede cancelar sin aceptación: CFDI dentro de las 72 horas posteriores a su emisión, comprobantes con monto total hasta mil pesos con IVA incluido, los de nómina con ciertos límites, los tipo egreso y traslado, y los de público en general o residentes en el extranjero. Un cambio de 2026 que conviene marcar: el Complemento de Pago, el REP, ya no entra en esta facilidad aunque sea de monto chico; su cancelación siempre pide aceptación del receptor.

Fuera de esos casos, se necesita aceptación, y aquí el dato que más conviene saber: el receptor tiene 3 días hábiles para aceptar o rechazar la solicitud. Si no responde en ese plazo, el SAT da por aceptada la cancelación. Es la aceptación tácita. O sea, el silencio del receptor juega a favor de quien cancela.

Y las sanciones específicas: no cancelar, o cancelar fuera de plazo, cuesta entre 5% y 10% del monto del CFDI —fíjense que es porcentaje del comprobante, puede ser mucho dinero—. Y la más seria: asentar datos falsos en un CFDI no solo es multa, puede configurar el delito del artículo 110. Eso ya es cárcel. Con esto cerramos errores y entramos al bloque que conecta todo: deducciones."

---

# BLOQUE 5 — IMPACTO FISCAL EN DEDUCCIONES (25 min) {icon: receipt}

---

## SLIDE 28: CFDI: Constitutivo, no Probatorio

### Contenido Visual

La idea más importante de la sesión:

> Un gasto **NO es deducible** solo porque se pagó y existe comprobante.

La deducibilidad nace cuando concurren **TODOS** los requisitos del **Art. 27 LISR**.

El CFDI es **uno** de esos requisitos. No es la deducción en sí.

### Script

"Llegamos a la idea que quiero que se lleven grabada de toda la sesión. Si olvidan todo lo demás, recuerden esto.

Un gasto no es deducible simplemente porque se haya pagado y exista un comprobante. Lo repito porque va contra la intuición de muchos clientes y hasta de algunos colegas: tener la factura NO es tener la deducción.

La deducibilidad nace cuando concurren TODOS los requisitos del artículo 27 de la Ley del ISR, juntos. El CFDI es uno de esos requisitos —importantísimo, constitutivo, sin él no hay nada— pero es uno entre varios. Es condición necesaria, no suficiente.

¿Por qué insisto tanto? Porque el cliente típico llega con su carpeta de facturas y dice 'aquí está todo, dedúceme'. Y el trabajo del contador no es timbrar y restar; es verificar que cada gasto cumpla los siete u ocho filtros del 27. El que solo junta facturas es un capturista. El que verifica el 27 es un asesor. Vamos a ver cuáles son esos requisitos."

---

## SLIDE 29: Requisitos del Art. 27 LISR

### Contenido Visual

Los más relevantes para CFDI:

- **Fr. I** — Estrictamente **indispensable**
- **Fr. III** — Amparado con **CFDI**; pagos > **$2,000** por medio bancario
- **Fr. IV** — Registrado en **contabilidad**, una sola vez
- **Fr. V** — Cumplir **retención y entero** de impuestos
- **Fr. XVIII** — Fecha del CFDI en el **ejercicio** correcto

> Combustibles: medio bancario **sin importar el monto**.

### Script

"Estos son los requisitos del 27 que más se conectan con el CFDI. No los voy a leer como lista de súper; los voy a aterrizar.

Fracción I: estrictamente indispensable para la actividad. El clásico es el gasto personal disfrazado de gasto de empresa. Si no es indispensable para generar el ingreso, no entra, tenga o no factura.

Fracción III: dos cosas. Que esté amparado con un CFDI que cumpla los requisitos del Código —todo lo de hoy— y que cuando el monto exceda dos mil pesos, el pago se haga por medio bancario: transferencia, cheque nominativo, o tarjeta. El efectivo arriba de dos mil mata la deducción aunque tengan la factura perfecta. Y una excepción durísima: combustibles, el pago debe ser por medio electrónico sin importar el monto, aunque sean cien pesos de gasolina.

Fracción IV: registrado en contabilidad y restado una sola vez. Fracción V: cumplir las obligaciones de retención y entero, por ejemplo el ISR e IVA retenido a un honorario. Si no retuvieron, no deducen. Y fracción XVIII: la fecha del CFDI debe corresponder al ejercicio por el que se deduce. El caso típico: gasto pagado en diciembre de 2025 con factura de enero de 2026. Por regla general se deduce en el ejercicio que corresponda a la fecha del CFDI. Cuidado con eso en los cierres."

---

## SLIDE 30: Acreditamiento de IVA — Art. 5 LIVA

### Contenido Visual

| Fr. | Requisito |
|---|---|
| **I** | IVA de bienes/servicios **indispensables** |
| **II** | IVA **trasladado expresamente y por separado** en CFDI |
| **III** | IVA **efectivamente pagado** en el mes |
| **IV** | IVA retenido: que se haya **enterado** |

> Sin REP no hay constancia de pago efectivo → no procede el **acreditamiento** del mes.

### Script

"El espejo del ISR en materia de IVA es el artículo 5 de la Ley del IVA. Para acreditar el IVA que les trasladaron, necesitan cumplir estos requisitos.

Fracción I: que el IVA corresponda a bienes o servicios estrictamente indispensables, igual que en el ISR. Fracción II: que el IVA esté trasladado expresamente y por separado en un CFDI. Que venga desglosado, no escondido en el total. Fracción III, la clave: que el IVA haya sido efectivamente pagado en el mes de que se trate. Y fracción IV: tratándose de IVA retenido, que se haya enterado.

Ahora conecten esto con lo que vimos antes del receso. La fracción III dice 'efectivamente pagado'. ¿Y cómo demuestra el contribuyente que pagó, cuando la operación fue PPD? Con el REP. Por eso el Recibo Electrónico de Pago no es un trámite burocrático: es la constancia del pago efectivo que habilita el acreditamiento. Sin REP, técnicamente no hay constancia de pago, y técnicamente no procede acreditar el IVA del mes correspondiente al cobro. Todo se conecta: el REP del bloque 3 es el que sostiene el acreditamiento del bloque 5."

---

## SLIDE 31: Razón de Negocio y Listas 69-B

### Contenido Visual

Lo que viene **después** del CFDI:

- **CFF 5-A** — la autoridad puede recaracterizar operaciones sin **razón de negocio**
- **Anexo 3** — prácticas indebidas: uso de CFDI para inflar deducciones (EFOS/EDOS)
- **Listas 69 y 69-B** — emisores y receptores de comprobantes sin sustento

> Validar al proveedor en la **69-B** antes de deducir es control básico hoy.

### Script

"El CFDI perfecto no los blinda si la operación no tiene sustancia. Esto es lo que el SAT viene aplicando con más fuerza cada año.

El artículo 5-A del Código le da a la autoridad la facultad de recaracterizar operaciones que carecen de razón de negocio. Si una operación solo existe para generar un beneficio fiscal y no tiene lógica económica, el SAT puede tratarla según su verdadera naturaleza, o desconocerla.

Los criterios no vinculativos del Anexo 3 listan, entre las prácticas indebidas, el uso de CFDI para inflar deducciones. Ahí nace todo el universo EFOS y EDOS: los que emiten comprobantes de operaciones simuladas y los que se los compran.

Y la herramienta concreta que tienen que usar: las listas 69 y 69-B que el SAT publica en su portal. La 69-B lista a los contribuyentes que emiten comprobantes sin sustento, los EFOS, y a sus clientes, los EDOS. La recomendación es directa y práctica: validar a sus proveedores en la lista 69-B antes de aplicar sus deducciones es hoy control básico, no paranoia. Porque un CFDI de un EFOS puede ser declarado sin efectos fiscales de forma retroactiva, y entonces se les cae la deducción de años atrás, con recargos."

---

## SLIDE 32: "Tengo CFDI, Tengo Deducción" — El Filtro

### Contenido Visual

```
¿Estrictamente indispensable?  ── NO ──→ NO DEDUCIBLE
        │ SÍ
¿CFDI 4.0 con datos correctos? ── NO ──→ NO DEDUCIBLE
        │ SÍ
¿Pago > $2,000 por banco?      ── NO ──→ NO DEDUCIBLE
        │ SÍ
¿Se hicieron las retenciones?  ── NO ──→ NO DEDUCIBLE
        │ SÍ
¿Proveedor fuera de la 69-B?   ── NO ──→ Riesgo alto
        │ SÍ
¿Fecha del CFDI en el ejercicio? ─ NO ─→ NO DEDUCIBLE
        │ SÍ
            GASTO DEDUCIBLE
```

### Script

"Quiero que se lleven este esquema mental, porque es el que deberían correr —aunque sea en automático, en la cabeza— cada vez que un cliente les presenta una factura para deducir.

Primer filtro: ¿es estrictamente indispensable? Si no, se acabó, no deducible. Segundo: ¿hay CFDI 4.0 con los datos correctos del receptor? Si no, no deducible. Tercero: ¿el pago superó dos mil pesos y, si sí, fue por medio bancario? Si fue en efectivo arriba de dos mil, no deducible. Cuarto: ¿se efectuaron las retenciones que correspondían? Si no, no deducible. Quinto: ¿el proveedor está vigente y fuera de la lista 69-B? Si está en la lista, riesgo alto, alto. Y sexto: ¿la fecha del CFDI corresponde al ejercicio? Si no, no deducible.

Solo cuando un gasto pasa los seis filtros llega abajo, al recuadro que dice 'gasto deducible'. Cuéntenlos: son seis preguntas. El CFDI es apenas la segunda. Por eso la frase con la que abrí este bloque: el CFDI es necesario pero no suficiente. Quien internaliza este filtro deja de tener sorpresas en las auditorías. Con esto cerramos el contenido. Vamos a la síntesis."

---

# CIERRE DE LA CLASE {icon: flag}

---

## SLIDE 33: Síntesis — Tres Ideas

### Contenido Visual

1. El CFDI 4.0 está **consolidado**; lo que cambia son catálogos y validaciones. La **disciplina operativa** marca la diferencia.

2. Los complementos **no son opcionales**: cada uno tiene supuesto de obligatoriedad y sanción propia.

3. El CFDI es **condición necesaria pero insuficiente** para deducir. La única defensa: coherencia de datos y **materialidad**.

### Script

"Antes de cerrar, tres ideas para llevarse.

Primera: el CFDI 4.0 está consolidado y es estable. No esperen revoluciones; lo que cambia año con año son los catálogos y las reglas de validación. Entonces la ventaja competitiva de un despacho no es saber 'lo último', es la disciplina operativa. El despacho que reconcilia cada semana, que tiene a sus clientes actualizados, que vigila los plazos del REP, es el que no recibe cartas invitación. El que improvisa, las recibe cada mes.

Segunda: los complementos no son opcionales por defecto. Cada uno tiene un supuesto de obligatoriedad, y la mayoría traen sanciones específicas, algunas penales como Carta Porte. Tener el radar de qué cliente necesita qué complemento es parte del servicio.

Tercera, la que repetimos toda la tarde: el CFDI es condición necesaria pero insuficiente para la deducibilidad. La fiscalización del SAT cruza información en automático, sin que intervenga una persona. La única defensa real es la coherencia interna de los datos y la materialidad de las operaciones. Tengan eso y duermen tranquilos; no lo tengan y ninguna factura bonita los salva."

---

## SLIDE 34: Gracias · Próxima Clase

### Contenido Visual

**Clase 2 · Módulo 6** — Taller práctico: emisión, validación de XML y cancelaciones paso a paso.

Tarea para estas dos semanas:

- Elegir **2 clientes** y reconciliar CFDI emitidos vs cobros (REP)
- Validar **3 proveedores** clave en la lista **69-B**
- Traer un **XML real** para abrirlo nodo por nodo en clase

**LCP Israel Castro** — israel@todoconta.com

### Script

"Cerramos. Para estas dos semanas les dejo tarea concreta, de la que genera valor real en su despacho.

Una: tomen dos clientes y reconcilien sus CFDI emitidos contra los pagos efectivamente cobrados, vía REP. Es justo la pregunta que les hice antes del receso. Si encuentran descuadres, ahí hay un riesgo de IVA que conviene atender antes de que lo encuentre el SAT.

Dos: validen tres proveedores clave de algún cliente en la lista 69-B del portal del SAT. Es de cinco minutos y puede ahorrarles un dolor de cabeza de años.

Tres, y esta es para la próxima clase: traigan un XML real —anonimizado si quieren— porque la Clase 2 es taller. Vamos a abrirlo nodo por nodo, vamos a emitir con complementos, vamos a validar y vamos a cancelar paso a paso, con las herramientas del SAT: Mis Cuentas, Factura Fácil y los visores.

Hoy construimos el criterio. La próxima lo ponemos a trabajar. Gracias por su atención y por aguantar una clase densa. Nos vemos en dos semanas. Pasen buena tarde."

---

## Notas Técnicas para el Instructor

### Cronograma Detallado (9:00 am – 1:00 pm)

| Hora | Slides | Tema | Tipo | Minutos |
|---|---|---|---|---|
| 9:00 – 9:15 | 1–3 | Portada, ruta y diagnóstico | Apertura + sondeo | 15 |
| 9:15 – 10:00 | 4–10 | Bloque 1: Fundamentos CFDI 4.0 | Presentación + reflexión | 45 |
| 10:00 – 10:30 | 11–14 | Bloque 2: Campos del receptor | Presentación | 30 |
| **10:30 – 11:00** | 15 | **RECESO** | — | **30** |
| 11:00 – 12:00 | 16–23 | Bloque 3: Complementos | Presentación + ejemplo REP | 60 |
| 12:00 – 12:30 | 24–27 | Bloque 4: Errores y cancelación | Presentación + tablas | 30 |
| 12:30 – 12:55 | 28–32 | Bloque 5: Impacto en deducciones | Presentación + filtro | 25 |
| 12:55 – 13:00 | 33–34 | Síntesis y cierre | Q&A + tarea | 5 |

**TOTAL contenido activo:** 210 minutos
**Duración clock:** 240 minutos (4 horas) incluyendo receso
**Descanso:** 30 minutos

> **Nota de flexibilidad:** si el grupo se complica en complementos (Bloque 3) o cancelación (Bloque 4), reasignar minutos del Bloque 5, que puede convertirse en lectura comentada del filtro del slide 32. La Clase 2 retoma todos los casos prácticos, así que es válido cerrar la teoría aquí.

---

### Recursos Visuales Necesarios

- Diagrama del árbol del XML (slide 6) en grande / proyectable
- Tabla de tipos de CFDI (I/E/T/N/P) impresa para reparto
- Ejemplo numérico del REP (slide 19) en hoja de cálculo proyectable
- Mapa de los 4 motivos de cancelación (slide 25)
- Flujograma "Tengo CFDI, tengo deducción" (slide 32) en póster — es el cierre conceptual
- Captura de la herramienta de validación de RFC del SAT (para anticipar la Clase 2)

---

### Dinámica de Participación

- **Slide 3 (Diagnóstico):** contar manos en las 3 preguntas — calibra profundidad de bloques 4 y 5
- **Slide 9 (Reglas PUE/PPD):** preguntar quién ha emitido PUE y cobrado tarde — testimonio vivo
- **Slide 10 (Reflexión):** dejar pensar 2 min, no forzar respuestas en voz alta
- **Slide 19 (Ejemplo REP):** hacer el cálculo de plazos en vivo, no solo leerlo
- **Slide 22 (Sanciones Carta Porte):** enfatizar la parte penal (contrabando) — siempre engancha
- **Slide 32 (Filtro deducción):** correr el árbol con un gasto hipotético propuesto por el grupo

---

### Notas de Facilidad

- El Bloque 3 (complementos) es el núcleo: si el tiempo aprieta, sacrificar slides del Bloque 1 (4–7), no del 3
- REP (slides 17–19) y Carta Porte (20–22) son los que más consultas generan: no acelerarlos
- Evitar leer las tablas completas — señalar renglones clave y dar un ejemplo concreto por tabla
- El slide 32 (filtro) es el remate emocional de la clase: llegar con energía, no atropellarlo
- Recordar al grupo de forma recurrente la frase ancla: "el CFDI es necesario pero no suficiente"

---

### Materiales a Preparar

- ✅ Estos slides (uno por participante + proyectable)
- ✅ XML de muestra (anonimizado) para anticipar la Clase 2
- ✅ Impresión del flujograma del slide 32
- ✅ Liga directa a la consulta de listas 69 / 69-B del SAT
- ✅ `M6_C1_CFDI_4.0_Fundamentos_y_Complementos.md` como soporte para dudas detalladas
- ✅ Calendario de plazos REP y cancelación 2026 (proyectable)

---

### Puntos de Actualización Normativa 2026

- **RMF 2026:** DOF 28-dic-2025; anexos 3, 7, 10–14 y 16 publicados 9-ene-2026
- **Anexo 20:** estructura del CFDI 4.0 sin cambios; Guía de llenado actualizada 29-dic-2025
- **REP 2.0 Revisión B:** vigente desde 15-ene-2024 (plazo de timbrado: 5º día natural mes siguiente)
- **Carta Porte 3.1:** obligatoria desde 17-jul-2024; catálogos actualizados 13-ene-2026 (IATA 67ª ed., pedimentos 2026)
- **Anexo 5 (multas):** montos actualizados publicados 28-dic-2025
- **Listas 69 / 69-B:** consulta permanente en portal SAT
- **Complementos pendientes:** Gastos por cuenta de terceros e Hidrocarburos — obligatorios 30 días naturales tras su publicación

---

**Documento elaborado para fines educativos**
**Diplomado en Herramientas Prácticas ante la Autoridad Fiscal**
**Módulo 6 · Clase 1 — Enero 2026**