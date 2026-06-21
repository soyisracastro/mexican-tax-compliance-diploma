# Clase 02 — Módulo 6: Taller Práctico de CFDI 4.0
## Herramientas del SAT, XML, Validación y Cancelación
### Slides con Scripts para Teleprompter

**Duración**: 3 horas 30 minutos efectivos (9:00 am – 1:00 pm, hora centro, con receso 10:40–11:10)
**Contenido activo**: 210 minutos
**Actualización normativa**: Enero 2026 (CFF arts. 29 y 29-A; RMF 2026 DOF 28-dic-2025; Anexo 20 CFDI 4.0; herramientas SAT vigentes)

---

## SLIDE 1: Taller Práctico de CFDI 4.0

### Contenido Visual

De la teoría a la **operación**: emitir, leer XML, validar y cancelar.

Módulo 6 · Clase 2 de 2 · Enero 2026

Instructor — **LCP Israel Castro**

### Script

"Buenos días. Bienvenidos a la segunda y última clase del Módulo 6. La clase pasada construimos el marco: de dónde nace el CFDI, los campos del receptor, los complementos, los errores y la conexión con la deducibilidad. Hoy bajamos a la cancha.

Esta sesión es un taller. Le bajamos el nivel teórico a propósito y le subimos el operativo. Quiero que salgan de aquí sabiendo entrar a las herramientas gratuitas del SAT, emitir un CFDI bien hecho en cinco escenarios reales, abrir un XML y entenderlo nodo por nodo, validar si una factura que les mandaron es auténtica, y cancelar con el motivo correcto sin que el sistema les rebote.

Si pueden, sigan el flujo en su propia pantalla mientras avanzamos. Y si en algún momento un portal del SAT se cae —que pasa— no se preocupen: tengo capturas de respaldo. Lo importante es que se lleven el método, porque los portales cambian de aspecto pero la lógica es la misma.

Arrancamos con un repaso relámpago de la clase anterior."

---

## SLIDE 2: Hoja de Ruta

### Contenido Visual

**6 bloques** prácticos en 210 minutos.

| Bloque | Tema | Min |
|---|---|---|
| 0 | Apertura y repaso Clase 1 | 10 |
| 1 | Herramientas del SAT | 50 |
| 2 | Casos prácticos de emisión | 40 |
| — | **Receso** | 30 |
| 3 | Estructura del XML nodo por nodo | 50 |
| 4 | Validación y cancelaciones | 35 |
| 5 | Detección y corrección de errores | 15 |
| 6 | Cierre del módulo | 10 |

### Script

"Vean la ruta. Antes del receso: repaso corto, las herramientas gratuitas del SAT que todo contador debería usar como rutina, y cinco casos de emisión correcta. Esos cinco casos son oro: son los que más ven mal hechos en sus despachos.

Después del receso, la parte que a muchos les da miedo y que hoy van a perder el miedo: leer un XML nodo por nodo. Luego validación y cancelación paso a paso, la detección y corrección de errores con sus códigos crípticos, y el cierre del módulo completo.

Una advertencia honesta: esta clase tiene menos slides bonitos y más manos a la obra. Si en algún caso quieren que repita un paso, díganlo. Es taller, no conferencia. Empecemos."

---

# BLOQUE 0 — APERTURA Y REPASO (10 min) {icon: rotate-ccw}

---

## SLIDE 3: Repaso Flash de la Clase 1

### Contenido Visual

Tres ideas ancla antes de operar:

- **CFDI 4.0** es la única versión válida desde abril 2023
- **Tres campos del receptor** deben coincidir EXACTO: nombre, CP, régimen
- El CFDI es **necesario pero no suficiente** para deducir (Art. 27 LISR)

> Diagnóstico: ¿quién ha usado **Mis Cuentas** o **Factura Fácil** en los últimos 6 meses?

### Script

"Tres ideas para anclar lo de la clase pasada, porque hoy las vamos a aplicar.

Una: el CFDI 4.0 es la única versión válida desde abril de 2023 y sigue sin cambios estructurales en 2026. No hay debate de versiones.

Dos: tres campos del receptor son críticos y deben coincidir exactamente con lo que tiene el SAT —nombre o razón social, código postal del domicilio fiscal, y régimen fiscal—. Hoy vamos a ver exactamente qué error suelta el sistema cuando uno de estos falla.

Tres: tener CFDI no es tener deducción. El comprobante es uno de los requisitos del artículo 27, no la deducción completa. Esa frase la repetimos toda la clase pasada y hoy la van a ver materializada en el mini-caso del cierre.

Y una pregunta rápida para calibrar: levanten la mano quienes hayan entrado a Mis Cuentas o Factura Fácil del SAT en los últimos seis meses. … Perfecto, eso me dice a qué velocidad voy en el primer bloque. Vamos a las herramientas."

---

# BLOQUE 1 — HERRAMIENTAS DEL SAT (50 min) {icon: wrench}

---

## SLIDE 4: Mapa de Herramientas Gratuitas

### Contenido Visual

El SAT da herramientas gratis que el contador debe dominar, aunque use PAC.

| Herramienta | Para qué |
|---|---|
| **Factura Electrónica** | Emitir CFDI 4.0 con CSD/e.firma |
| **Factura Fácil** (Mis Cuentas) | Emisión simplificada |
| **Verifica tus facturas** | Validar autenticidad y estatus |
| **Cancela y recupera** | Cancelar y recuperar XML |
| **Visores** | Conciliar IVA, nómina, anual |
| **Validador masivo** | Validar muchos CFDI a la vez |

### Script

"Empecemos por el mapa. El SAT pone a disposición un set de herramientas gratuitas que muchos contadores ignoran porque trabajan con un PAC de paga. Error. Aunque tengan el mejor sistema del mercado, estas herramientas son su red de seguridad, y algunas no las sustituye ningún PAC.

La aplicación de Factura Electrónica es la general: emite CFDI 4.0 con su CSD o e.firma. Factura Fácil, dentro de Mis Cuentas, es la versión simplificada. 'Verifica tus facturas' valida si un CFDI es auténtico y si sigue vigente, y es pública, no necesita contraseña. 'Cancela y recupera' sirve para cancelar y para rescatar un XML que se perdió. Los Visores —que son la joya de la corona— concilian IVA, nómina y declaración anual. Y el validador masivo permite revisar muchos CFDI de un jalón.

Las direcciones exactas están en su material de apoyo. No se las van a memorizar; las van a tener a la mano. Vamos a entrar a las tres más importantes para el día a día, empezando por Factura Fácil."

---

## SLIDE 5: Mis Cuentas y Factura Fácil

### Contenido Visual

Portal simplificado del SAT. Nació para el RIF, hoy lo usan:

- Personas físicas con **actividad empresarial**
- **Arrendadores** y profesionales (honorarios)
- Algunas personas morales (donatarias, asoc. religiosas)

> Incluye un **Simulador** para practicar sin emitir CFDI reales — ideal para enseñarle a un cliente.

### Script

"Factura Fácil vive dentro de Mis Cuentas. Nació para el extinto Régimen de Incorporación Fiscal, el RIF, pero hoy la pueden usar varios perfiles: personas físicas con actividad empresarial, arrendadores, profesionales que cobran honorarios, e incluso algunas personas morales con actividades específicas como donatarias autorizadas o asociaciones religiosas.

¿Para quién es ideal? Para el cliente de bajo volumen que no tiene sistema y no quiere pagar un PAC. El que emite cinco, diez facturas al mes. Para ese perfil, Factura Fácil es suficiente y es gratis.

Y hay una función que poca gente usa y que a mí me encanta para capacitar: el Simulador. Permite practicar el flujo completo de emisión sin generar un CFDI real. Cuando tengan un cliente nuevo que quiere aprender a facturarse solo, siéntenlo en el Simulador. Practica, se equivoca, no pasa nada, y cuando ya le agarró la mano, emite de verdad. Es la mejor herramienta pedagógica gratuita que tiene el SAT. Ahora, esta herramienta tiene límites importantes, y eso es el siguiente slide."

---

## SLIDE 6: Factura Fácil — Qué Sí y Qué No

### Contenido Visual

| ✅ SÍ permite | ❌ NO permite |
|---|---|
| CFDI de Ingreso (I) | Logo / diseño propio |
| REP de pagos (P) | Volumen alto |
| Egreso (E) | Conexión por API |
| Factura global (público gral.) | Complementos especiales (Carta Porte, INE…) |
| Consultar, recuperar, cancelar | Nómina (en transición) |

### Script

"El cuadro es para que sepan cuándo Factura Fácil alcanza y cuándo tienen que mandar al cliente a un PAC.

Del lado bueno: emite CFDI de Ingreso, emite el Recibo Electrónico de Pago, emite Egresos para devoluciones y descuentos, emite factura global con público en general, y permite consultar, recuperar y cancelar. Para el 80% de las operaciones de un cliente pequeño, con eso basta.

Del lado de los límites: no permite personalizar la factura con logo ni diseño corporativo —sale el formato genérico del SAT—. No aguanta volumen alto porque la captura es manual, factura por factura. No se conecta por API con sistemas externos. Y aquí está el límite que más importa: no emite la mayoría de los complementos especializados. Si su cliente necesita Carta Porte, Comercio Exterior o INE, Factura Fácil no le sirve; necesita un PAC. La nómina está en transición, así que tampoco cuenten con ella.

Moraleja práctica: Factura Fácil es para el cliente sencillo. En el momento en que aparece un complemento especial o el volumen crece, toca PAC. Saber dónde está esa línea les ahorra muchas frustraciones."

---

## SLIDE 7: Cambio Clave para 2026

### Contenido Visual

La facilidad del **RIF** terminó.

> Quienes emitían en Mis Cuentas sin e.firma ni CSD podían hacerlo **solo hasta 31-dic-2025**.

A partir de **2026**: todos los emisores en Mis Cuentas requieren **CSD o e.firma vigente**.

- Avisar a clientes que aún operaban con la facilidad
- Verificar vigencia de la **e.firma** antes de facturar

### Script

"Este slide es una alerta concreta para enero de 2026, porque va a tomar a varios clientes por sorpresa.

Los contribuyentes del extinto RIF que venían emitiendo CFDI a través de Mis Cuentas en 2022, 2023 y 2024 tenían una facilidad muy cómoda: podían sellar sus comprobantes sin necesidad de e.firma ni Certificado de Sello Digital. Esa facilidad venció el 31 de diciembre de 2025.

¿Qué significa esto en la práctica? Que a partir de este 2026, todos los emisores en Mis Cuentas, sin excepción, necesitan CSD o e.firma vigente para timbrar. El cliente que llegaba, ponía su RFC y contraseña y facturaba, ahora va a toparse con que el sistema le pide su certificado.

Acción para ustedes: identifiquen en su cartera a quién le aplicaba esta facilidad —los exRIF que facturan por Mis Cuentas— y avísenle antes de que tenga la urgencia de emitir y no pueda. Y verifiquen que su e.firma esté vigente, porque renovarla a las prisas, en enero, con las oficinas saturadas, es un dolor. Mejor prevenir. Pasemos a la herramienta más importante de todas: el Visor."

---

## SLIDE 8: Visor de Facturas Emitidas y Recibidas

### Contenido Visual

La herramienta **más importante** de hoy: base del prellenado de IVA y anual.

- Concentra **todos** los CFDI emitidos y recibidos
- Es el **cruce primario** del SAT al mandar cartas invitación
- Detecta CFDI **cancelados** que no habías visto

> Si lo del Visor no coincide con lo que declaras → **carta invitación**.

### Script

"De todo lo que veamos hoy, si me tuviera que quedar con una sola herramienta, sería esta: el Visor de Facturas Emitidas y Recibidas. Y la mayoría de los contadores solo lo abren cuando ya les llegó la carta invitación. Llegan tarde.

¿Qué hace? Concentra absolutamente todos los CFDI que el contribuyente emitió y recibió, los clasifica, y los presenta como insumo de las declaraciones provisionales y de la anual. O sea: es la base con la que el SAT pre-llena. Cuando ustedes ven una declaración pre-llenada, lo que están viendo es el contenido del Visor.

Y aquí está el punto que tienen que entender: este Visor es el cruce primario que hace el SAT antes de mandar una carta invitación. Si lo que está en el Visor no coincide con lo que el contribuyente declaró, sale la carta de forma automática. Nadie la revisa a mano; es un algoritmo.

Por eso la recomendación es convertir el Visor en rutina mensual, no en herramienta de emergencia. Al cierre de cada mes, descargan el reporte, lo cruzan contra contabilidad, identifican cancelados, faltantes y duplicados, y concilian antes de declarar. El que hace esto no recibe cartas invitación de IVA. El que no, vive apagando incendios."

---

## SLIDE 9: Visor de Comprobantes de Nómina

### Contenido Visual

Dos versiones: **Patrón** y **Trabajador**.

**Patrón** — ISR retenido vs enterado, detalle por trabajador, alertas de timbrado.

- La acumulación se basa en **fecha de pago**, no de emisión
- Las correcciones **NO** se hacen en el Visor: se cancela y reemite

**Trabajador** — espejo del anterior; el cliente PF lo consulta para su anual.

### Script

"El Visor de Nómina tiene dos caras: la del Patrón y la del Trabajador. Las dos importan.

La del Patrón muestra los pagos por sueldos, asimilados y separación, con vista mensual y anual, el ISR retenido contra el enterado, y el detalle trabajador por trabajador. Dos datos clave: primero, la acumulación se basa en la fecha de pago del CFDI, no en la fecha de emisión —flujo de efectivo otra vez—. Y segundo, importantísimo: las correcciones NO se hacen en el Visor. El Visor solo muestra, es un espejo. Si hay un error, se corrige en el sistema de nómina cancelando y reemitiendo el CFDI. Mucha gente busca el botón de editar en el Visor y no existe.

La del Trabajador es el mismo espejo, pero desde el lado del empleado. ¿Por qué le importa al contador? Porque muchos clientes persona física lo consultan antes de su declaración anual y llegan con dudas. Ustedes tienen que poder explicárselo. Si aparece un patrón que el cliente no reconoce, puede ser robo de identidad fiscal. Si las cifras no cuadran con sus recibos, hay que avisar al patrón. Y las alertas amarillas —ojo con esto— indican comprobantes con errores de timbrado que no se computan en el prellenado. Justo de eso trata el caso del siguiente slide."

---

## SLIDE 10: Caso — La Alerta Amarilla

### Contenido Visual

Cliente PF: el SAT le pre-llenó un ingreso **menor** al real en su anual.

En el Visor del Trabajador: **3 CFDI** de nómina con **alerta amarilla** (patrón timbró con errores).

**¿Qué hacer?**
- Avisar al patrón → cancelar y reemitir los CFDI
- Declarar con los **registros reales** (recibos, estados de cuenta)
- Dejar **nota en papel de trabajo** justificando la diferencia

### Script

"Este caso lo van a ver tarde o temprano, así que conviene tenerlo resuelto de antemano.

Llega un cliente persona física con su Constancia de Sueldos y Salarios y les dice: 'el SAT me pre-llenó un ingreso menor al que realmente gané, ¿está mal el SAT?'. Ustedes entran al Visor del Trabajador y descubren que tres de sus CFDI de nómina aparecen con alerta amarilla, porque el patrón los timbró con errores en el complemento —códigos del Apéndice 6 mal aplicados, por ejemplo—. Esos tres comprobantes, al estar en amarillo, no se computaron en el prellenado. Por eso el ingreso pre-llenado salió más bajo.

¿Qué hacen? Tres pasos. Primero, comunican al patrón para que cancele y reemita esos CFDI correctamente; eso arregla el problema de raíz, aunque toma tiempo. Segundo, mientras el patrón corrige, ustedes presentan la declaración con base en los registros reales del cliente: sus recibos, sus estados de cuenta, lo que efectivamente cobró. No con el prellenado equivocado. Y tercero, y esto es lo que los blinda en una auditoría, dejan nota en el papel de trabajo justificando por qué la declaración difiere del prellenado.

La lección: el prellenado es una propuesta, no una verdad absoluta. Cuando hay alertas amarillas, manda la realidad documentada, no el algoritmo."

---

## SLIDE 11: ¿Cuándo Usar Cada Herramienta?

### Contenido Visual

| Necesidad | Herramienta |
|---|---|
| Cliente bajo volumen sin sistema | Factura Fácil |
| Volumen mediano/alto | PAC propio o integrado |
| ¿Es válido un CFDI recibido? | Verifica tus facturas |
| Validar 50 CFDI a la vez | Validador masivo |
| Conciliar IVA mensual | Visor Emitidas/Recibidas |
| Nómina vs ISR enterado | Visor Nómina (Patrón) |
| Recuperar XML perdido | Cancela y recupera |

### Script

"Cerramos el bloque de herramientas con esta tabla de decisión, que es la que quiero que tengan pegada en el monitor.

¿Cliente de bajo volumen sin sistema? Factura Fácil. ¿Volumen mediano o alto? PAC, con sistema propio o integrado. ¿Necesitan saber si un CFDI que les mandaron es válido? 'Verifica tus facturas'. ¿Tienen que validar cincuenta facturas de golpe? Validador masivo. ¿Conciliar el IVA del mes? El Visor de Emitidas y Recibidas. ¿Conciliar nómina contra el ISR enterado? El Visor de Nómina del Patrón. ¿Se perdió un XML? 'Cancela y recupera tus facturas' lo rescata.

La idea de fondo: no hay una sola herramienta para todo. Hay una herramienta correcta para cada necesidad, y el contador profesional las conoce todas y elige la adecuada. El que solo sabe usar el sistema de su PAC se queda corto el día que el cliente llega con un problema que el PAC no resuelve.

Con esto pasamos de las herramientas a los casos. Cinco escenarios reales de emisión correcta. Pongan atención porque estos son los que más se equivocan en la práctica."

---

# BLOQUE 2 — CASOS PRÁCTICOS DE EMISIÓN (40 min) {icon: file-check}

---

## SLIDE 12: Caso 1 — Honorarios con Retención

### Contenido Visual

PF (612) presta servicios contables a PM (601). Cobra **$10,000 + IVA**.

| Concepto | Monto |
|---|---|
| Subtotal | $10,000.00 |
| IVA trasladado 16% | $1,600.00 |
| Retención ISR 10% | −$1,000.00 |
| Retención IVA 10.67% | −$1,066.67 |
| **Total a pagar** | **$9,533.33** |

> Uso **G03** · ClaveProdServ **84111506** · ClaveUnidad **E48**.

### Script

"Caso uno, el pan de cada día de cualquier despacho. Persona física en régimen 612, actividades profesionales, le factura servicios contables a una persona moral en régimen 601, general. Cobra diez mil más IVA. Y como el receptor es persona moral, debe retenerle ISR e IVA. Esa retención la marca el artículo 1-A de la Ley del IVA y el artículo 106 de la de ISR.

Veamos el cálculo, que es donde tropieza la gente. Subtotal, diez mil. IVA trasladado al 16%, mil seiscientos. Hasta ahí el comprobante diría once mil seiscientos. Pero ahora las retenciones: ISR del 10% sobre el subtotal, mil pesos. Y la retención de IVA, que son dos terceras partes del IVA trasladado, es decir 10.67% sobre el subtotal, mil sesenta y seis con sesenta y siete. El total que efectivamente recibe el prestador es nueve mil quinientos treinta y tres con treinta y tres.

Los errores típicos: no incluir las retenciones en el CFDI cuando el receptor es persona moral —el más grave, porque rompe el acreditamiento del cliente—; confundir el régimen del emisor con el del receptor; y usar el uso G01, adquisición de mercancías, en lugar de G03, gastos en general. Para servicios va G03 siempre. Y los catálogos: clave de producto 84111506 servicios contables, clave de unidad E48 unidad de servicio."

---

## SLIDE 13: Caso 2 — Venta a Crédito con Parcialidades

### Contenido Visual

Venta **$50,000 + IVA** el 10-feb. Pago en dos parcialidades.

| CFDI | Fecha | Tipo | Clave |
|---|---|---|---|
| #1 Factura | 10-feb | **I** · PPD | FormaPago **99** |
| #2 REP $30,000 | 25-feb | **P** | timbrar ≤ **5-mar** |
| #3 REP $28,000 | 15-mar | **P** | timbrar ≤ **5-abr** |

> Emitir el #1 como PUE "para no hacer REP" = discrepancia de IVA garantizada.

### Script

"Caso dos, la secuencia del PPD que vimos en teoría, ahora aterrizada. Una empresa vende cincuenta mil más IVA el 10 de febrero. El cliente va a pagar en dos parcialidades: treinta mil el 25 de febrero, los veintiocho mil restantes el 15 de marzo.

Esto genera tres CFDI, no uno. El primero, la factura por la operación completa, el 10 de febrero: tipo Ingreso, método PPD, forma de pago 99 'Por definir', total cincuenta y ocho mil. El segundo, el REP por el primer pago: tipo P, con el complemento de pagos relacionando el UUID de la factura, parcialidad uno, saldo anterior cincuenta y ocho mil, pagado treinta mil, insoluto veintiocho mil. Y este REP tiene fecha límite: a más tardar el 5 de marzo. El tercero, el REP por la liquidación del 15 de marzo, parcialidad dos, insoluto cero, con fecha límite 5 de abril.

El error que les va a costar cartas invitación es la tentación de emitir la factura inicial como PUE para 'ahorrarse' los REP. No lo hagan. El SAT cruza la fecha de emisión contra la fecha del pago real que ve en el banco, y la discrepancia de IVA es automática. El otro error es pasarse del plazo de cinco días, y el tercero, calcular mal los impuestos proporcionales en el ImpuestosDR del REP. Disciplina de calendario: el REP no espera."

---

## SLIDE 14: Caso 3 — Factura Global RESICO PF

### Contenido Visual

Abarrotes, PF RESICO (626), ventas al público en marzo: **$80,000** (IVA incl.).

- RFC genérico **XAXX010101000**
- Nombre: **PUBLICO EN GENERAL**
- Uso **S01** (sin efectos fiscales)
- Nodo **InformacionGlobal**: periodicidad 04, mes 03, año 2026

> La global RESICO PF **solo se cancela en el mismo mes** en que se generó.

### Script

"Caso tres, la factura global, típica del comercio al menudeo. Una tienda de abarrotes, persona física en RESICO, régimen 626, vendió al público en general durante marzo ochenta mil pesos en total, IVA incluido. No le va a hacer factura a cada cliente que compró un refresco; emite una factura global del mes.

Los datos clave: el RFC genérico para público en general es XAXX010101000 —ojo, con A—; el nombre se registra literalmente como 'PUBLICO EN GENERAL'; el uso del CFDI es S01, sin efectos fiscales, porque esas ventas al menudeo no las va a deducir nadie; y se llena el nodo InformacionGlobal con la periodicidad —04 que es mensual—, el mes 03 y el año 2026.

Y la restricción que tienen que tener tatuada para RESICO personas físicas: la factura global solo se puede cancelar en el mismo mes en que se generó. Después, ya no. Esto conecta directo con el caso cuatro.

Errores típicos: usar XEXX010101000 en lugar de XAXX —el XEXX es para residentes en el extranjero, es otra cosa—; olvidar el nodo InformacionGlobal, sin el cual la global no es global; y pretender cancelar la global meses después, que es justo lo que el RESICO PF no permite."

---

## SLIDE 15: Caso 4 — De Global a Nominativa

### Contenido Visual

Tras la global de marzo, un cliente pide factura **nominativa** de una venta de $1,500 ya incluida.

**Procedimiento (motivo 04):**
1. Emitir el CFDI **nominativo** con datos reales del cliente
2. Cancelar la global con **motivo 04**
3. **Reemitir** la global SIN esa venta

> Olvidar el paso 3 = ingreso **duplicado**. Usar motivo 01/02 en vez del 04 = mal.

### Script

"Caso cuatro, la continuación natural del tres, y donde más se equivoca la gente. Ya emitieron la global de marzo. El 5 de abril llega un cliente y dice: 'oye, esa compra de mil quinientos que te hice el mes pasado, necesito factura a mi nombre para deducirla'. Esa venta ya está dentro de la global. ¿Qué hacen?

Tres pasos, en orden. Paso uno: emiten el CFDI nominativo al cliente, con sus datos reales, tipo Ingreso, el uso que él indique —normalmente G03—, con el detalle de la venta original. Paso dos: cancelan la factura global usando el motivo 04, que es el específico para 'operación nominativa relacionada en una factura global'. Paso tres, y este es el que todo el mundo olvida: reemiten la factura global, ahora SIN incluir esa venta de mil quinientos que ya facturaron por separado.

¿Qué pasa si se brincan el paso tres? Ingreso duplicado: la venta queda facturada dos veces, en la global vieja y en la nominativa nueva, y el SAT lo ve. ¿Y el otro error clásico? Usar motivo 01 o 02 en lugar del 04. Cada motivo tiene su escenario; este escenario es el 04, punto. Memoricen la tripleta: nominativa, cancelo con 04, reemito la global limpia."

---

## SLIDE 16: Caso 5 — Egreso por Devolución

### Contenido Visual

Venta $20,000 + IVA en feb. En marzo el cliente devuelve **$5,000 + IVA**.

Emitir **CFDI de Egreso (E)**, no cancelar:
- TipoRelacion **03** (devolución) + UUID de la venta original
- Subtotal $5,000 · IVA $800 · Total $5,800

> **Regla del millón:** error de captura → cancelación. Realidad de la operación (devolución, descuento) → **nota de crédito (E)**.

### Script

"Caso cinco, y la pregunta del millón que cierra el bloque. Una empresa vendió veinte mil más IVA en febrero. En marzo el cliente devuelve cinco mil más IVA de mercancía defectuosa. ¿Cancelo la factura de venta? No. La venta sí ocurrió; lo que pasó después es una devolución parcial.

Lo correcto es emitir un CFDI de Egreso, tipo E, una nota de crédito, por los cinco mil más IVA. Se relaciona con la venta original usando CfdiRelacionados con tipo de relación 03, que es 'devolución de mercancía sobre facturas previas', y el UUID de la factura de venta. Subtotal cinco mil, IVA ochocientos, total cinco mil ochocientos. La venta de veinte mil queda intacta y el egreso de cinco mil ochocientos la ajusta a la baja.

Y aquí la regla que resuelve la confusión eterna entre cancelar y emitir nota de crédito: si el ajuste viene de la realidad de la operación —una devolución, un descuento posterior, una bonificación— va por nota de crédito, CFDI de Egreso. Si el ajuste viene de un error en la captura del CFDI —puse mal el RFC, mal el importe— va por cancelación con sustitución. Realidad versus error. Esa es la divisoria.

Antes del receso, piensen: de estos cinco casos, ¿cuál ven peor hecho en su despacho? Lo comentamos al regresar. Treinta minutos. Nos vemos."

---

# RECESO (30 min) {icon: coffee}

---

## SLIDE 17: Receso

### Contenido Visual

**30 minutos.**

Al regresar: abrimos un **XML** y lo leemos nodo por nodo.

### Script

"Treinta minutos de receso. Cuando regresemos viene la parte que parece la más técnica y que en realidad es la más empoderante: vamos a abrir un XML de CFDI y a leerlo nodo por nodo, sin miedo. Van a salir de aquí sabiendo distinguir un comprobante bien hecho de uno que les va a dar problemas, con solo ver el archivo. Descansen y volvemos puntuales."

---

# BLOQUE 3 — ESTRUCTURA DEL XML NODO POR NODO (50 min) {icon: file-code}

---

## SLIDE 18: Por Qué Leer un XML

### Contenido Visual

Tres razones para que el contador lea XML:

- **Diagnosticar errores** con códigos crípticos (CFDI40143, CRP20246…)
- **Validar** lo que mandó el cliente o proveedor, sin depender del PDF
- **Entender** qué revisa el SAT en sus cruces automáticos

> El **XML es el documento fiscal verdadero**. El PDF es solo su representación impresa. Si difieren, manda el XML.

### Script

"Retomamos con la habilidad que separa al contador operativo del capturista: leer un XML.

Tres razones por las que tienen que poder hacerlo. Una: para diagnosticar errores. Cuando el sistema rechaza un timbrado, suelta un código críptico tipo CFDI40143 o CRP20246. Si saben leer el XML, ubican el nodo culpable en segundos en lugar de adivinar. Dos: para validar lo que les mandó un cliente o un proveedor sin depender de la versión impresa. Tres: para entender qué está revisando el SAT, porque sus cruces automáticos leen el XML, no el PDF bonito.

Y aquí la idea fuerza de todo el bloque, subráyenla: el XML es el documento fiscal verdadero. El PDF es solo una representación impresa, un dibujo. Cualquiera puede hacer un PDF que diga lo que sea. La verdad fiscal vive en el XML. Por eso, cuando un cliente les diga 'mi factura salió mal' o 'no me deja deducir', la primera respuesta siempre es: 'mándame el XML, no el PDF'. Si hay diferencia entre los dos, manda el XML. Siempre. Vamos a abrir uno."

---

## SLIDE 19: Anatomía de un CFDI 4.0

### Contenido Visual

```xml
<cfdi:Comprobante Version="4.0" Serie="A" Folio="12345"
   Fecha="2026-03-15T10:30:00" Sello="..." NoCertificado="..."
   SubTotal="10000.00" Moneda="MXN" Total="11600.00"
   TipoDeComprobante="I" Exportacion="01"
   MetodoPago="PUE" FormaPago="03" LugarExpedicion="58000">

  <cfdi:Emisor Rfc="..." Nombre="..." RegimenFiscal="612"/>
  <cfdi:Receptor Rfc="..." Nombre="..."
     DomicilioFiscalReceptor="06600"
     RegimenFiscalReceptor="601" UsoCFDI="G03"/>
  <cfdi:Conceptos> ... </cfdi:Conceptos>
  <cfdi:Impuestos TotalImpuestosTrasladados="1600.00"> ... </cfdi:Impuestos>
  <cfdi:Complemento>
     <tfd:TimbreFiscalDigital UUID="..." SelloSAT="..."/>
  </cfdi:Complemento>
</cfdi:Comprobante>
```

### Script

"Esto es un CFDI 4.0 de ingreso, simplificado para que quepa en pantalla. No se asusten con las comillas y las etiquetas; vamos por partes y van a ver que es muy lógico.

Arriba, la etiqueta Comprobante, que es el nodo raíz. Ahí viven los datos generales: versión 4.0, serie, folio, fecha, el sello digital del emisor, los importes —subtotal, moneda, total—, el tipo de comprobante, el método y la forma de pago, y el lugar de expedición.

Anidados dentro del Comprobante están los actores: el Emisor con su RFC, nombre y régimen; el Receptor con sus datos, incluyendo los tres campos críticos que vimos la clase pasada; los Conceptos, que es el detalle de lo facturado; los Impuestos totales; y al final el Complemento, donde vive el Timbre Fiscal Digital con el UUID y el sello del SAT.

Fíjense en la estructura de muñecas rusas: todo cuelga del Comprobante, y cada nodo tiene sus atributos entre comillas. Eso es leer XML. En los siguientes slides vamos atributo por atributo, empezando por el encabezado, que es donde se esconden la mitad de los errores de método y forma de pago."

---

## SLIDE 20: El Encabezado del Comprobante

### Contenido Visual

| Atributo | Cuidado |
|---|---|
| `Version` | Siempre **4.0** |
| `Fecha` | ISO 8601; dentro de **72 hrs** antes del timbrado |
| `MetodoPago` | PUE o PPD |
| `FormaPago` | **99 solo con PPD** |
| `Exportacion` | 01 No aplica · 02 Definitiva |
| `LugarExpedicion` | CP del **emisor** |

### Script

"El encabezado del Comprobante. Repaso los atributos donde más se equivoca la gente.

Versión: siempre 4.0, no hay otra vigente. Fecha: formato ISO 8601 —año, mes, día, T, hora— y tiene que estar dentro de las 72 horas anteriores al timbrado. Si intentan timbrar una factura con fecha de hace una semana, rebota. Es un control antifraude del SAT.

Método de pago y forma de pago: aquí está el clásico que arrastramos de la clase pasada. El método es PUE o PPD. La forma es del catálogo c_FormaPago, y la regla de oro: el 99 'Por definir' solo se usa con PPD. Si ven un XML con método PUE y forma 99, está mal, punto.

Exportación: atributo nuevo que muchos ignoran. 01 es 'no aplica', que es el 99% de los casos; 02 es exportación definitiva A1. Y LugarExpedicion: es el código postal del emisor, del establecimiento que factura. Cuidado, no lo confundan con el DomicilioFiscalReceptor, que es del cliente. Son dos CP distintos en dos nodos distintos, y mezclarlos es error común. Vamos a los actores."

---

## SLIDE 21: Emisor y Receptor

### Contenido Visual

**Emisor**: RFC activo con CSD vigente · Nombre exacto · Régimen vigente.

**Receptor** — los 3 campos críticos del 4.0 y su error:

| Campo | Error si falla |
|---|---|
| `Rfc` | **CFDI40143** (no existe en lista SAT) |
| `Nombre` | **CFDI40148** (no coincide) |
| `RegimenFiscalReceptor` + `UsoCFDI` | **CFDI40161** (uso incompatible) |

### Script

"Emisor y Receptor. El Emisor es relativamente sencillo: su RFC debe estar activo y con CSD vigente, su nombre exacto como en el SAT, su régimen vigente. Como es uno mismo o el cliente que factura, casi siempre está bien.

El Receptor es el campo de batalla, y aquí lo conecto con los códigos de error reales que van a ver al timbrar. Los tres campos críticos del 4.0, cada uno con su error característico.

El RFC del receptor: si no existe en la lista de RFC inscritos y no cancelados del SAT, el sistema suelta el error CFDI40143. Lo ven, ya saben: RFC mal o receptor con problemas en el SAT.

El Nombre: si no coincide exactamente con lo registrado, sale el CFDI40148. Acento, abreviatura, lo que sea que difiera, ese código.

Y la combinación de RegimenFiscalReceptor con UsoCFDI: si el uso no es compatible con el régimen —el clásico G03 con un asalariado en 605— sale el CFDI40161. Aprenderse estos tres códigos les ahorra horas de adivinar. Cuando vean 40143, van directo al RFC; 40148, al nombre; 40161, a la pareja régimen-uso. Sigamos con los conceptos."

---

## SLIDE 22: Conceptos y ObjetoImp

### Contenido Visual

Cada concepto = un bien o servicio:

- `ClaveProdServ` (8 dígitos) · `ClaveUnidad` · `Descripcion` específica
- `ValorUnitario` · `Importe` (= cantidad × valor, validación matemática)

> **`ObjetoImp` — nuevo en 4.0:** 01 No objeto · 02 Sí objeto · 03 Sí objeto, no obligado a desglose · 04 Sí objeto, no causa.

### Script

"El nodo Conceptos. Cada concepto representa un bien o un servicio facturado, y un CFDI puede tener varios.

Los atributos: ClaveProdServ, la clave de producto o servicio del catálogo del SAT, ocho dígitos. ClaveUnidad, la unidad de medida estandarizada. Descripción, que debe ser específica —ya lo dijimos para Carta Porte, pero aplica a todo: nada de 'mercancía general' o 'varios'—. ValorUnitario, el precio sin impuestos. E Importe, que es cantidad por valor unitario, y el SAT valida esa multiplicación matemáticamente: si no cuadra, rebota.

Y el atributo estrella que nació con el 4.0 y que mucha gente todavía pone mal: ObjetoImp, objeto de impuesto. Tiene cuatro valores. 01, no objeto del impuesto. 02, sí objeto —el caso normal de algo que causa IVA—. 03, sí objeto pero no obligado al desglose. Y 04, sí objeto pero no causa impuesto. Poner mal el ObjetoImp es de los errores nuevos más frecuentes, porque en la 3.3 no existía y la gente venía en automático. Si el concepto causa IVA, va 02 y se desglosa. Vamos al desglose de impuestos y al timbre, que cierra el recorrido."

---

## SLIDE 23: Impuestos y Timbre Fiscal Digital

### Contenido Visual

**Impuestos** — doble desglose (por concepto + total comprobante):
- `001` ISR · `002` IVA · `003` IEPS · TipoFactor Tasa/Cuota/Exento

**TimbreFiscalDigital** — el sello del SAT vía PAC:
- `UUID` (folio fiscal, 36 caracteres) · `SelloSAT` · `RfcProvCertif`

> Sin nodo Timbre, el CFDI **NO está timbrado** y **no tiene validez fiscal**.

### Script

"Dos nodos para cerrar la anatomía. Impuestos y el Timbre.

El nodo Impuestos tiene un doble desglose que conviene entender: aparece a nivel de cada concepto, y luego otra vez como total a nivel comprobante. Los impuestos se identifican con clave: 001 es ISR, 002 es IVA, 003 es IEPS. El TipoFactor puede ser Tasa, Cuota o Exento, y la TasaOCuota es el número aplicable —0.160000 para el IVA al 16%—. Cuando revisen un XML, verifiquen que el total de impuestos a nivel comprobante sea la suma de los de cada concepto. Si no cuadran, algo está mal armado.

Y el último nodo, el Timbre Fiscal Digital, que va dentro del Complemento. Este es el sello del SAT, puesto a través del PAC. Contiene el UUID —el folio fiscal único de 36 caracteres, la huella digital del comprobante—, el SelloSAT, y el RFC del PAC que timbró.

La regla absoluta: sin este nodo, el CFDI no está timbrado y no tiene ninguna validez fiscal. Es un borrador. Cuando alguien les muestre un 'comprobante' sin Timbre Fiscal Digital, no es un CFDI, es un papel. Lo primero que busco yo al abrir un XML es justo este nodo: si está, es real; si no está, no existe para el SAT. Veamos cómo abrir un XML en la práctica."

---

## SLIDE 24: Cómo Abrir un XML en la Práctica

### Contenido Visual

Tres opciones para el contador:

- **Notepad++** o editor de texto plano (gratis; con plugin XML queda legible)
- **Visualizadores XML web** (subes el archivo, lo ves estructurado)
- **El visor del propio PAC** (formato amigable)

> Cuando el cliente diga "mi factura salió mal", pide **siempre el XML**, no el PDF.

### Script

"Bien, ya saben qué tiene un XML por dentro. ¿Cómo lo abren en el día a día? Tres opciones, de la más simple a la más cómoda.

Una: Notepad++ o cualquier editor de texto plano. Gratis, está en todas las computadoras, nunca falla. Si le instalan un plugin de XML y activan el 'pretty print', el archivo se acomoda con sangrías y queda muy legible, casi como los slides que acabamos de ver. Para una revisión rápida, sobra.

Dos: visualizadores XML en web. Suben el archivo y se los muestra estructurado, con los nodos colapsables. Útiles, pero ojo: no suban a sitios random un XML con datos fiscales reales de un cliente. Usen herramientas confiables o trabajen local.

Tres: el visor del propio PAC. Casi todos los sistemas de facturación tienen una vista amigable del XML, que es la más cómoda si ya trabajan con uno.

Y el tip que cierra el bloque, el que más les va a servir: cuando un cliente les diga 'mi factura salió mal' o 'el SAT no me la reconoce', pídanle siempre el XML, nunca solo el PDF. El PDF puede tener cualquier diseño y ocultar el problema. El XML es la verdad. Con eso pasamos a validación y cancelación."

---

# BLOQUE 4 — VALIDACIÓN Y CANCELACIONES (35 min) {icon: badge-check}

---

## SLIDE 25: Verifica tus Facturas

### Contenido Visual

**verificacfdi.facturaelectronica.sat.gob.mx** — pública y gratuita.

Capturas UUID + RFC emisor + RFC receptor. Tres resultados:

- **Vigente** → válido para deducir
- **Cancelado** → NO sirve para deducir
- **No encontrado** → < 72 hrs, error de captura, o **apócrifa**

### Script

"Validación. La herramienta número uno es 'Verifica tus facturas', y lo mejor: es pública y gratuita, no necesita contraseña. Cualquiera puede verificar cualquier CFDI si tiene el folio fiscal y los dos RFC.

Capturan el UUID, el RFC del emisor, el RFC del receptor, el captcha, y el sistema les devuelve uno de tres resultados.

Vigente: el CFDI existe en los controles del SAT y no está cancelado. Es válido para fines fiscales. Pueden deducir con tranquilidad.

Cancelado: el comprobante fue cancelado. No sirve para deducir, aunque tengan el PDF en la mano. Este caso es traicionero, porque el proveedor pudo cancelar la factura sin avisarles, y ustedes la tienen registrada como gasto. Por eso conviene reverificar antes del cierre.

No encontrado: el CFDI no existe en los registros del SAT. Tres explicaciones posibles: una, que tenga menos de 72 horas desde el timbrado y todavía no se sincronice —esperan y reverifican—; dos, que se equivocaron al capturar el UUID o un RFC; o tres, la grave, que sea una factura apócrifa. Si pasaron las 72 horas y los datos están bien y sigue 'no encontrado', huele a apócrifo, y eso no se deduce y conviene documentar. Vamos a las otras dos vías de validación."

---

## SLIDE 26: Validador Masivo y Código QR

### Contenido Visual

**Validador masivo** — `tramitesdigitales.sat.gob.mx/Sicofi.ValidacionCFD`
- Carga muchos CFDI a la vez. Ideal para revisión mensual de recibidas.

**Código QR** — cada CFDI 4.0 lo trae en su representación impresa.
- Al escanearlo, abre la verificación con datos pre-cargados.

> Flujo eficiente: lector de QR + validación para revisar volúmenes de tickets.

### Script

"Validar una factura a la vez está bien para casos puntuales, pero ¿qué hacen cuando el cliente les entrega ochenta facturas recibidas del mes? Ahí entra el validador masivo.

El validador masivo permite cargar un archivo con muchos CFDI y verificarlos todos de una sola consulta. Es la herramienta para la revisión mensual de facturas recibidas, o para depurar una cartera grande. En lugar de capturar UUID por UUID, suben el lote y el sistema les regresa cuáles están vigentes y cuáles canceladas. Esto debería ser parte de su rutina de cierre mensual.

Y el código QR: cada CFDI 4.0 incluye un QR en su representación impresa. Al escanearlo con cualquier lector, abre directamente la URL de verificación con los datos ya pre-cargados. No tienen que teclear nada.

Un flujo que usan los despachos eficientes para gastos con muchos tickets: una app móvil que lee el QR y encadena con la verificación. El auxiliar va escaneando los tickets de gasolina, casetas, consumos, y en automático va validando cuáles son auténticos. Lo que antes tomaba una tarde de captura, hoy son minutos. La tecnología está ahí, gratis; el chiste es usarla. Pasemos a cancelación."

---

## SLIDE 27: Cancelación Paso a Paso

### Contenido Visual

Portal: **Cancela y recupera tus facturas** (RFC/contraseña o e.firma).

1. Localizar el CFDI (UUID, fecha, filtros)
2. Seleccionar **motivo** (01/02/03/04)
3. Si es 01 o 04 → capturar **UUID del sustituto**
4. Confirmar solicitud
5. Esperar aceptación (**3 días hábiles**) o tácita
6. Verificar estatus **"Cancelado"**

### Script

"Cancelación paso a paso, ya con la teoría de la clase pasada internalizada. Entran al portal 'Cancela y recupera tus facturas', se autentican con RFC y contraseña o con e.firma.

Paso uno, localizan el CFDI a cancelar: por UUID, por fecha, o con los filtros. Paso dos, seleccionan el motivo de cancelación —01, 02, 03 o 04—, y en un momento repaso cuándo va cada uno. Paso tres, si el motivo es 01, errores con relación, o 04, operación nominativa de una global, el sistema les va a pedir el UUID del CFDI sustituto, así que ese sustituto ya debe existir. Paso cuatro, confirman la solicitud.

Paso cinco, y aquí depende del caso: si la cancelación requiere aceptación del receptor, esperan su respuesta. Tiene tres días hábiles para aceptar o rechazar; si no responde, opera la aceptación tácita y se da por cancelado. Paso seis, verifican que el estatus final diga 'Cancelado'. No asuman que se canceló; confírmenlo, porque mientras el receptor no acepte y no pasen los tres días, sigue vigente.

Ese es el flujo general. Ahora el detalle de qué motivo usar en cada escenario, que es donde la gente se enreda."

---

## SLIDE 28: El Motivo Correcto

### Contenido Visual

| Motivo | Escenario | ¿Sustituto? |
|---|---|---|
| **01** | Error en datos (RFC, importe) | Sí — primero el nuevo, luego cancelar |
| **02** | Duplicado o cliente equivocado | No |
| **03** | La operación no se realizó | No |
| **04** | Nominativa de una factura global | Sí — emitir, cancelar, reemitir global |

> Motivo 01: **primero** el sustituto (relación 04), **después** la cancelación.

### Script

"Los cuatro motivos, con su escenario claro para que no duden.

Motivo 01: hubo un error en los datos —el RFC, el importe, la descripción— que obliga a reexpedir. Requiere sustituto, y el orden es sagrado: primero emiten el CFDI nuevo y correcto, con tipo de relación 04, sustitución, apuntando al UUID del viejo; después cancelan el viejo con motivo 01 apuntando al UUID del nuevo. Si lo hacen al revés, rebota. Y si el sistema de plano no deja con el 01, el propio SAT acepta usar el 02 como alternativa.

Motivo 02: errores que no ameritan sustituto. Una factura duplicada que le mandaron al cliente correcto, o una a un cliente equivocado que no van a reexpedir. No requiere UUID nuevo, no emiten sustituto.

Motivo 03: la operación no se llevó a cabo. Facturaron un anticipo y el negocio se cayó. No requiere sustituto.

Motivo 04: el escenario del caso cuatro de hoy. El cliente que estaba en la global pide nominativa. Emiten la nominativa, cancelan la global con 04, reemiten la global sin esa venta.

Lean el escenario, identifiquen el motivo. No es memoria; es lógica. Error de captura, 01 o 02. Operación que no pasó, 03. Global a nominativa, 04."

---

## SLIDE 29: Sin Aceptación y Plazos

### Contenido Visual

**Sin aceptación del receptor (regla 2.7.1.34):** dentro de **72 hrs**, monto ≤ **$1,000**, nómina, egreso/traslado/pago, público en general.

**Plazo límite de cancelación:**
- PM → **31-mar** del año siguiente
- PF → **30-abr** del año siguiente
- RESICO PF (global) → **mismo mes**

### Script

"Dos precisiones que cierran cancelación.

Primera, cuándo NO necesitan que el receptor acepte. La regla 2.7.1.34 mantiene los supuestos: si cancelan dentro de las 72 horas de emitido; si el monto total no pasa de mil pesos con IVA; los de nómina con sus límites; los tipo egreso, traslado y pago con matices; y los de público en general o residentes en el extranjero. En todos esos casos cancelan directo, sin pedir permiso. Fuera de esos casos, sí necesitan la aceptación o la tácita de tres días.

Segunda, los plazos límite, que son críticos para el cierre del año. Personas morales: pueden cancelar hasta el 31 de marzo del año siguiente al ejercicio en que emitieron. Personas físicas: hasta el 30 de abril. Y el caso especial, otra vez: RESICO personas físicas, la factura global solo en el mismo mes en que se generó.

¿Por qué importa tanto? Porque si descubren en el cierre de marzo que hay un CFDI mal de hace año y medio, ya no lo pueden cancelar. Quedó como ingreso o gasto definitivo. Por eso la revisión mensual del Visor, que vimos en el bloque 1, no es opcional: es lo que les permite cancelar a tiempo, dentro del plazo. Una cosa alimenta a la otra."

---

## SLIDE 30: Sanciones y Bitácora

### Contenido Visual

| Conducta | Sanción |
|---|---|
| No cancelar o fuera de plazo (CFF 81-XLVI, 82-XLII) | **5% a 10%** del monto |
| Cancelar sin justificación documental | Verificable en facultades de comprobación |

> **Bitácora de cancelaciones:** motivo + soporte (correo, contrato) + fecha. Es la mejor defensa en auditoría.

### Script

"Cerramos cancelación con las sanciones y una recomendación que vale oro.

Las sanciones: no cancelar cuando debían, o cancelar fuera de plazo, cuesta entre el 5% y el 10% del monto del CFDI. Fíjense que es porcentaje del comprobante, no una multa fija; en facturas grandes, puede ser muchísimo dinero. Y cancelar sin justificación documental no es delito por sí mismo, pero el SAT lo puede cuestionar en sus facultades de comprobación, y si no tienen con qué sustentarlo, quedan expuestos.

De ahí la recomendación operativa, y con esto les doy una herramienta concreta para el lunes: lleven una bitácora de cancelaciones. Una hoja de cálculo simple donde por cada CFDI cancelado registren el motivo real, el soporte —el correo del cliente que pidió la corrección, el contrato que se canceló, la nota de la devolución— y la fecha. Nada sofisticado.

¿Por qué? Porque cuando llegue una auditoría —y llegan— y el auditor pregunte 'por qué cancelaste estas cuarenta facturas', ustedes abren la bitácora y tienen la respuesta documentada, caso por caso. Esa bitácora es la diferencia entre una revisión que se resuelve en una tarde y una que se convierte en un crédito fiscal. La defensa fiscal se construye antes del problema, no después. Vamos al penúltimo bloque: errores y su corrección."

---

# BLOQUE 5 — DETECCIÓN Y CORRECCIÓN DE ERRORES (15 min) {icon: bug}

---

## SLIDE 31: Errores con Código y Solución

### Contenido Visual

| Código | Causa | Solución |
|---|---|---|
| **CFDI40143** | RFC del receptor no existe / CSD cancelado | Validar RFC en SAT |
| **CFDI40148** | CP no coincide con el receptor | Confirmar CP del domicilio fiscal |
| **CFDI40161** | Uso incompatible con régimen (G03 + 605) | Revisar uso vs régimen |
| **CRP20246** | Falta ImpuestosDR en el REP | Agregar desglose de impuestos |
| Cadena original | Sello no coincide / CSD vencido | Verificar CSD; regenerar sello |

### Script

"Esta tabla es su diccionario de urgencias. Cuando el timbrado truene, en lugar de entrar en pánico, buscan el código aquí y van directo a la causa.

CFDI40143: el RFC del receptor no existe en la lista del SAT, o el receptor tiene su CSD cancelado. Validan el RFC en línea. Es el mismo del nodo Receptor que vimos en el XML.

CFDI40148: el código postal no corresponde al receptor en el SAT. Confirman el CP del domicilio fiscal del cliente, no el de su sucursal.

CFDI40161: el uso del CFDI es incompatible con el régimen del receptor, el clásico G03 con un asalariado en 605. Revisan la pareja uso-régimen.

CRP20246: este es del REP. Falta el nodo ImpuestosDR, el desglose de impuestos del documento relacionado. Lo agregan y listo.

Y los errores de cadena original: el sello no coincide con la cadena, casi siempre porque el CSD está vencido, mal configurado, o porque el XML fue alterado después de sellarlo. Verifican vigencia del CSD y regeneran el sello.

Memorícense estos cinco. Son el 90% de lo que van a ver. Cada código apunta a un nodo específico que ya recorrimos en el bloque del XML. Todo se conecta."

---

## SLIDE 32: Mini-Caso Integrador

### Contenido Visual

Cliente PM entrega **30 facturas** para deducir. Al validar:

- **4 canceladas** → no deducibles; pedir reemisión o sustento
- **2 no encontradas** → ¿< 72 hrs? esperar. ¿Apócrifas? denunciar y no deducir
- **1 con fecha posterior al cierre** → se deduce el **ejercicio siguiente** (Art. 27-XVIII)

> Flujo: identificar error → ¿captura o estructural? → cancelar/corregir → **documentar**.

### Script

"Cerramos el bloque con un mini-caso que integra todo lo de hoy, y es exactamente lo que les va a pasar en una temporada de cierre.

Un cliente persona moral les entrega treinta facturas recibidas del mes para deducir. Su equipo las captura, y al validarlas —con el validador masivo, claro— el sistema reporta tres situaciones. Cuatro facturas están canceladas en el SAT. Dos no las encuentra. Y una tiene fecha posterior al cierre del ejercicio. ¿Qué hacen con cada grupo?

Las cuatro canceladas: no se pueden deducir, punto. Tienen el PDF, pero el XML está cancelado, y manda el XML. Comunican al cliente y le piden al proveedor que reemita o que les dé el sustento de por qué canceló.

Las dos no encontradas: investigan. Si tienen menos de 72 horas, esperan y revalidan, puede ser sincronización. Si ya pasó el plazo y siguen sin aparecer, son apócrifas: no se deducen y se documenta, incluso se valora denunciar.

La de fecha posterior al cierre: no se deduce en el ejercicio actual. Se deduce en el siguiente, conforme al artículo 27 fracción XVIII de la Ley del ISR, que vimos la clase pasada.

¿Ven cómo se conecta todo? Validación, lectura de XML, deducibilidad, plazos. El flujo de corrección siempre es el mismo: identifican el error, deciden si es de captura o estructural, cancelan o corrigen, y documentan. Esa última palabra, documentar, es la que los salva. Vamos al cierre."

---

# CIERRE DEL MÓDULO {icon: flag}

---

## SLIDE 33: Síntesis del Módulo 6

### Contenido Visual

Cuatro ideas para llevarse de las dos clases:

1. El CFDI 4.0 es la **espina dorsal** de la fiscalización electrónica 2026
2. Las herramientas gratuitas del SAT son la **red de seguridad**: úsalas como rutina
3. El **XML es la verdad fiscal**; el PDF es solo representación
4. Cancelar **bien y a tiempo** previene el 80% de los problemas

> Lo que viene: Módulo 7 (cierre fiscal) y Módulo 8 (planeación) se apoyan en todo esto.

### Script

"Cerramos el módulo completo. Cuatro ideas, una por cada pilar de las dos clases.

Una: el CFDI 4.0 es la espina dorsal de la fiscalización electrónica del SAT en 2026. No es un trámite; es el dato con el que el SAT los vigila. Quien lo entiende así, deja de improvisar.

Dos: las herramientas gratuitas del SAT —los Visores, la verificación, el validador masivo— son la red de seguridad del contador. Úsenlas como rutina mensual, no como herramienta de emergencia cuando ya llegó la carta. El que concilia cada mes no recibe sorpresas.

Tres: el XML es la verdad fiscal; el PDF es solo la representación impresa. Aprender a leer XML, que hoy practicamos nodo por nodo, es una habilidad de defensa profesional que los distingue.

Cuatro: cancelar bien y a tiempo, con el motivo correcto y dentro del plazo, previene el 80% de los problemas de deducibilidad y acreditamiento.

Y miren hacia adelante: el Módulo 7, el taller de declaraciones y cierre fiscal, va a usar todo esto —la validación es insumo del cierre, los Visores alimentan el prellenado, los REP arman el IVA mensual—. Y el Módulo 8, planeación y defensa, se construye sobre el dominio del CFDI. Lo que aprendieron aquí es la base de lo que viene."

---

## SLIDE 34: Gracias · Compromiso de Aplicación

### Contenido Visual

> **De todo lo que vimos, ¿qué es lo PRIMERO que vas a implementar el lunes en tu despacho?**

Tres candidatos de alto impacto:

- Conciliación **mensual** con el Visor de Emitidas y Recibidas
- **Bitácora** de cancelaciones con soporte documental
- Validación **masiva** de facturas recibidas antes de deducir

**LCP Israel Castro** — israel@todoconta.com

### Script

"Cerramos con una pregunta, no con una despedida, porque lo que importa no es lo que vieron hoy sino lo que van a hacer con ello.

De todo lo que recorrimos en este módulo —las dos clases—, ¿qué es lo primero que van a implementar el lunes en su despacho? No me digan 'todo', porque 'todo' es 'nada'. Una cosa, concreta, que arranque la próxima semana.

Les dejo tres candidatos de alto impacto y bajo esfuerzo. Uno: montar la conciliación mensual con el Visor de Emitidas y Recibidas, para dejar de recibir cartas invitación de IVA. Dos: empezar la bitácora de cancelaciones con su soporte, que es su mejor defensa en auditoría. Tres: validar masivamente las facturas recibidas antes de deducirlas, para no cargar con canceladas o apócrifas.

Me encantaría escuchar a dos o tres de ustedes: ¿cuál eligen y por qué? … 

Gracias por estas dos clases y por el trabajo. El CFDI parece un tema árido, pero es, literalmente, el lenguaje en que hablan con la autoridad todos los días. Dominarlo es dominar la conversación. Cualquier duda que les surja al aplicarlo, ahí tienen mi correo. Mucho éxito, y nos vemos en el siguiente módulo. Buena tarde."

---

## Notas Técnicas para el Instructor

### Cronograma Detallado (9:00 am – 1:00 pm)

| Hora | Slides | Tema | Tipo | Minutos |
|---|---|---|---|---|
| 9:00 – 9:10 | 1–3 | Portada, ruta y repaso | Apertura + sondeo | 10 |
| 9:10 – 10:00 | 4–11 | Bloque 1: Herramientas del SAT | Demo + tablas | 50 |
| 10:00 – 10:40 | 12–16 | Bloque 2: Casos de emisión | Casos paso a paso | 40 |
| **10:40 – 11:10** | 17 | **RECESO** | — | **30** |
| 11:10 – 12:00 | 18–24 | Bloque 3: XML nodo por nodo | Recorrido en vivo | 50 |
| 12:00 – 12:35 | 25–30 | Bloque 4: Validación y cancelación | Demo + procedimiento | 35 |
| 12:35 – 12:50 | 31–32 | Bloque 5: Errores y corrección | Tabla + mini-caso | 15 |
| 12:50 – 13:00 | 33–34 | Síntesis y cierre del módulo | Q&A + compromiso | 10 |

**TOTAL contenido activo:** 210 minutos
**Duración clock:** 240 minutos (4 horas) incluyendo receso
**Descanso:** 30 minutos

> **Nota sobre tiempos:** se ajustaron los minutos de los bloques del material fuente para llenar el formato de 4 horas (9:00–13:00), igual que la Clase 1, dando más aire a los bloques prácticos (casos, XML, validación). Si el grupo es muy operativo, el Bloque 1 puede comprimirse y trasladar minutos al Bloque 3 (XML), que es el de mayor valor diferencial.

---

### Recursos Visuales / Técnicos Necesarios

- **Acceso en vivo a los portales del SAT** con un RFC de prueba o datos ficticios (idealmente)
- Capturas de respaldo de cada flujo, por si los portales fallan
- Un **XML real anonimizado** abierto en Notepad++ con plugin XML (Pretty Print activado)
- El **Simulador** de Factura Fácil abierto para demostrar emisión sin timbrar
- Tabla de códigos de error (slide 31) impresa/proyectable
- Plantilla de **bitácora de cancelaciones** (Excel) para repartir como entregable

---

### Dinámica de Participación

- **Slide 3 (Repaso):** sondeo de manos sobre uso de Mis Cuentas — calibra velocidad del Bloque 1
- **Slide 8 (Visor):** preguntar quién hace conciliación mensual hoy — casi nadie levanta la mano, ese es el gancho
- **Slide 16 (Caso 5):** dejar la pregunta "¿cuál ven peor hecho?" abierta hacia el receso
- **Slides 19–23 (XML):** recorrer un XML REAL en pantalla, no solo el del slide; pedir que ubiquen el nodo Timbre
- **Slide 28 (Motivos):** lanzar 2-3 mini-escenarios y que el grupo grite el motivo correcto
- **Slide 32 (Mini-caso):** resolverlo en plenaria, grupo por grupo de facturas
- **Slide 34 (Compromiso):** invitar a 2-3 participantes a comprometerse en voz alta

---

### Notas de Facilidad

- Esta clase es taller: si un portal del SAT se cae, pasar a capturas sin perder ritmo — no improvisar troubleshooting en vivo
- El Bloque 3 (XML) es el de mayor valor diferencial: si el tiempo aprieta, sacrificar slides del Bloque 1, no del 3
- No leer las tablas completas — señalar el renglón y dar el ejemplo concreto
- Los cinco casos del Bloque 2 son lo más aplicable: hacer los cálculos en vivo, sobre todo el Caso 1 (retenciones) y el Caso 2 (secuencia REP)
- Reforzar de forma recurrente la frase ancla: "el XML es la verdad; el PDF es el dibujo"
- Recordar que la Clase 1 dejó la teoría; aquí se trata de operar, no de volver a teorizar

---

### Materiales a Preparar / Entregables

- ✅ Estos slides (uno por participante + proyectable)
- ✅ XML de muestra anonimizado (el del slide 19 o uno propio)
- ✅ Plantilla de bitácora de cancelaciones (Excel)
- ✅ Liga directa a: Verifica tus facturas, Validador masivo, Mis Cuentas
- ✅ Tabla de códigos de error CFDI imprimible
- ✅ `0602-contenido.md` como soporte para dudas detalladas
- ✅ Calendario de plazos REP y cancelación 2026

---

### Puntos de Actualización Normativa 2026

- **Facilidad RIF en Mis Cuentas:** terminó el 31-dic-2025; desde 2026 se requiere CSD o e.firma vigente
- **RMF 2026:** reglas 2.7.1.4, 2.7.1.7, 2.7.1.29, 2.7.1.32, 2.7.1.34, 2.7.1.35 (DOF 28-dic-2025)
- **Anexo 20:** estándar técnico del CFDI 4.0 sin cambios estructurales
- **Plazo REP:** 5º día natural del mes siguiente al cobro
- **Plazos de cancelación:** PM 31-mar / PF 30-abr / RESICO PF global solo mismo mes
- **Portales SAT:** verificar URLs vigentes antes de la clase (cambian de aspecto periódicamente)

---

**Documento elaborado para fines educativos**
**Diplomado en Herramientas Prácticas ante la Autoridad Fiscal**
**Módulo 6 · Clase 2 — Enero 2026**
