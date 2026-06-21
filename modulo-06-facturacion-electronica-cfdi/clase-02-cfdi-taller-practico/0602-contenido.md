# Módulo 6 — Clase 2: Taller práctico de CFDI 4.0

**Diplomado en Herramientas Prácticas ante la Autoridad Fiscal**
**Duración efectiva:** 3 horas 30 minutos (4 horas con 30 min de descanso)
**Modalidad:** 100% online
**Público objetivo:** Contadores en ejercicio que requieren actualización profesional
**Docente:** C.P. Israel Castro Urieta (Isca)

---

## 🎯 Objetivos de aprendizaje

Al finalizar la sesión, el participante será capaz de:

1. Operar las herramientas gratuitas del SAT (Mis Cuentas, Factura Fácil, Visores) y conocer sus límites y casos de uso.
2. Resolver casos prácticos típicos de emisión correcta de CFDI 4.0 en escenarios reales que enfrenta un despacho.
3. Leer y entender la estructura básica de un XML de CFDI, identificando los nodos y atributos críticos.
4. Validar la autenticidad y vigencia de un CFDI usando las herramientas oficiales del SAT.
5. Cancelar un CFDI siguiendo el procedimiento correcto según el motivo de cancelación.
6. Diagnosticar y corregir los errores fiscales más comunes en la práctica diaria.

---

## 🗺️ Mapa de la sesión y tiempos sugeridos

| Bloque | Tema | Tiempo | Acumulado |
|---|---|---|---|
| 0 | Apertura, repaso de Clase 1 y enmarque del taller | 10 min | 0:10 |
| 1 | Herramientas del SAT: Mis Cuentas, Factura Fácil y Visores | 50 min | 1:00 |
| 2 | Casos prácticos de emisión correcta de CFDI | 35 min | 1:35 |
| ☕ | **DESCANSO** | **30 min** | — |
| 3 | Estructura del XML — recorrido nodo por nodo | 45 min | 2:50 |
| 4 | Validación de CFDI y cancelaciones paso a paso | 30 min | 3:20 |
| 5 | Detección y corrección de errores fiscales | 8 min | 3:28 |
| 6 | Cierre y siguientes pasos | 2 min | 3:30 |

> **Nota didáctica para el docente:** Esta clase está diseñada para ser eminentemente práctica. Si es posible, compartir pantalla y entrar en vivo a los portales del SAT (con un RFC de prueba o con datos ficticios). Los XML de ejemplo pueden mostrarse en cualquier editor de texto plano (Notepad++, VS Code, Sublime). Como advertimos en la Clase 1, el nivel se bajó intencionalmente: aquí se trata de operar, no de teorizar.

---

## Bloque 0 — Apertura y repaso *(10 min)*

### 0.1 Repaso flash de Clase 1

Tres ideas fuerza para anclar:

1. **CFDI 4.0 es la única versión válida** desde abril de 2023 y se mantiene en 2026 sin cambios estructurales.
2. **Tres campos del receptor son críticos:** nombre/razón social, código postal y régimen fiscal — deben coincidir EXACTAMENTE con el SAT.
3. **El CFDI es necesario pero no suficiente** para deducir: deben cumplirse los demás requisitos del artículo 27 LISR.

### 0.2 Diagnóstico breve

Pregunta abierta al grupo:

> ¿Quiénes han usado alguna vez Mis Cuentas o Factura Fácil del SAT en los últimos 6 meses? ¿Para qué tipo de operación?

Esta pregunta calibra qué tan operativos son los participantes con las herramientas oficiales y permite ajustar el nivel del bloque 1.

---

## Bloque 1 — Herramientas del SAT: Mis Cuentas, Factura Fácil y Visores *(50 min)*

### 1.1 Mapa de herramientas gratuitas del SAT *(5 min)*

El SAT pone a disposición varias herramientas gratuitas que el contador debe conocer aunque trabaje habitualmente con un PAC:

| Herramienta | URL/Acceso | Para qué sirve |
|---|---|---|
| **Aplicación de Factura Electrónica** | sat.gob.mx → Factura Electrónica → Genera tu factura | Emitir CFDI 4.0 con CSD o e.firma. Es la herramienta general. |
| **Mis Cuentas — Factura Fácil** | rfs.siat.sat.gob.mx | Emisión simplificada (originalmente para RIF; hoy abierta a otros regímenes con limitaciones). |
| **Verifica tus facturas (CFDI)** | verificacfdi.facturaelectronica.sat.gob.mx | Validar autenticidad y estatus de un CFDI. No requiere autenticación. |
| **Cancela y recupera tus facturas** | sat.gob.mx → Factura Electrónica → Cancela | Cancelación de CFDI emitidos y recuperación de XML. |
| **Visor de comprobantes de Nómina (Patrón)** | sat.gob.mx → Declaraciones → Visores | Conciliación de CFDI nómina vs ISR retenido vs enterado. |
| **Visor de comprobantes de Nómina (Trabajador)** | sat.gob.mx → Declaraciones → Visores | Consulta del trabajador de sus ingresos y retenciones. |
| **Visor de Facturas Emitidas y Recibidas** | sat.gob.mx → Declaraciones → Visores | Insumo del prellenado de IVA y declaración anual. |
| **Validador masivo de CFDI** | tramitesdigitales.sat.gob.mx/Sicofi.ValidacionCFD | Validación de múltiples CFDI en una sola consulta. |

### 1.2 Mis Cuentas y Factura Fácil *(15 min)*

#### ¿Qué es y para quién?

Mis Cuentas es el portal simplificado del SAT y dentro de él vive **Factura Fácil**. Originalmente diseñada para el desaparecido Régimen de Incorporación Fiscal (RIF), hoy puede ser utilizada por:
- Personas físicas con actividad empresarial.
- Arrendadores.
- Profesionales independientes (honorarios).
- Personas morales con actividades específicas (asociaciones religiosas, donatarias autorizadas, entre otras).

#### Lo que SÍ permite

- Emitir CFDI 4.0 de Ingreso (I).
- Emitir CFDI con Complemento de Recepción de Pagos (P).
- Emitir CFDI de Egreso (E) para devoluciones, descuentos o bonificaciones.
- Emitir factura global con público en general (RFC genérico XAXX010101000).
- Consultar, recuperar y cancelar facturas.
- Acceder al **Simulador** para practicar sin emitir CFDI reales (útil para enseñar a un cliente).

#### Lo que NO permite

- Personalizar las facturas con logo o diseño corporativo.
- Manejar volumen alto (la velocidad de captura es manual).
- Conectarse vía API con sistemas externos.
- Emitir muchos complementos especializados (Carta Porte, Comercio Exterior, INE, etc.) — para esto se requiere PAC.
- Emitir CFDI de Nómina (existe la opción “Mis Cuentas — Recibo de Nómina” pero está en transición).

#### Facilidades vigentes hasta el 31 de diciembre de 2025

Los contribuyentes del extinto RIF que hayan emitido CFDI a través de Mis Cuentas en 2022, 2023 o 2024 podían sellar el CFDI sin necesidad de e.firma o CSD hasta el 31 de diciembre de 2025. **A partir de 2026 ya se requiere CSD o e.firma vigente** para todos los emisores en Mis Cuentas. Punto importante para clientes que aún operan con esta facilidad.

#### Demostración sugerida (en vivo si es posible)

> **Para el docente:** mostrar el flujo en Factura Fácil:
> 1. Ingreso a sat.gob.mx con RFC y contraseña.
> 2. Mis Cuentas → Factura Fácil → Generar Factura.
> 3. Captura de receptor (RFC, nombre, CP, régimen fiscal, uso).
> 4. Captura de concepto (clave del producto, descripción, cantidad, valor).
> 5. Selección de método y forma de pago.
> 6. Vista previa y emisión.
> 7. Descarga de XML y PDF.
>
> Si no se puede mostrar en vivo, usar capturas o el Simulador como respaldo.

### 1.3 Visor de Facturas Emitidas y Recibidas *(10 min)*

Esta es probablemente la herramienta más importante de las que veremos hoy, porque es la base del prellenado de IVA y de la declaración anual.

#### ¿Qué hace?

Concentra TODOS los CFDI emitidos y recibidos por el contribuyente, los clasifica y los presenta como insumo de las declaraciones provisionales y anual.

#### Por qué importa al contador

- Es el cruce primario que realiza el SAT cuando envía cartas invitación.
- Si lo que está aquí no coincide con lo que se declara, llega la carta invitación.
- Permite identificar CFDI cancelados que el contribuyente no había detectado.
- Ayuda a reconciliar el IVA acreditable y trasladado mes a mes.

#### Flujo de trabajo recomendado para el contador

1. Al cierre de cada mes, descargar el reporte del Visor.
2. Cruzar contra los CFDI registrados en contabilidad.
3. Identificar discrepancias (CFDI cancelados, faltantes, duplicados).
4. Antes de presentar la declaración, conciliar los totales del Visor con el papel de trabajo.
5. Documentar las diferencias justificadas.

> **Pregunta de reflexión:** ¿En tu despacho hay un proceso mensual de conciliación con el Visor o solo lo revisan cuando llega una carta invitación? Si es lo segundo, llegan tarde.

### 1.4 Visor de Comprobantes de Nómina *(15 min)*

Existen dos versiones complementarias: la del **Patrón** y la del **Trabajador**. Ambas con accesos diferenciados en sat.gob.mx → Declaraciones → Visores.

#### Visor de Nómina del Patrón

**¿Qué muestra?**
- Pagos por sueldos y salarios, asimilados a salarios y pagos por separación.
- Información acumulada anual y vista mensual.
- ISR retenido vs enterado.
- Detalle por trabajador (RFC, percepciones, deducciones, subsidios).
- Errores de timbrado identificados (alertas amarillas/rojas).

**Datos clave para el contador:**
- La acumulación de ingresos se basa en la **fecha de pago**, no en la fecha de emisión del CFDI.
- Contiene información desde el ejercicio 2018 en adelante.
- Sirve como insumo para el prellenado del prellenado de pagos provisionales de ISR retenciones por salarios y asimilados (a partir de 2022).
- Sirve como insumo para el prellenado de la deducibilidad de la nómina en la declaración anual.

**Las correcciones NO se hacen en el Visor.** El Visor solo muestra; las correcciones se hacen en el sistema de nómina del patrón (cancelando y reemitiendo el CFDI).

#### Visor de Nómina del Trabajador

Es el espejo del anterior, desde la perspectiva del empleado. Útil para el contador porque muchos clientes lo consultan antes de su declaración anual y el contador debe poder explicarles lo que ven.

**Tres puntos para entender al cliente persona física:**
- Si aparece un patrón que no reconoce → posible robo de identidad fiscal.
- Si las cifras no coinciden con sus recibos → alertar al patrón para corregir CFDI.
- Las alertas amarillas indican comprobantes con errores de timbrado que NO se computan automáticamente para el prellenado.

#### Caso típico para presentar al grupo

> Un cliente persona física llega con su Constancia de Sueldos y Salarios y le indica al contador que en su declaración anual el SAT le pre-llenó un ingreso menor al que realmente percibió. El contador entra al Visor del Trabajador y descubre que tres CFDI de nómina aparecen con alerta amarilla porque el patrón los timbró con errores en el complemento (códigos del Apéndice 6 mal aplicados). ¿Qué hacer?
>
> **Respuesta:** comunicar al patrón para que cancele y reemita los CFDI. Mientras tanto, presentar la declaración con base en los registros reales (recibos, estados de cuenta) y dejar nota en papel de trabajo justificando la diferencia con el prellenado.

### 1.5 Tabla resumen: cuándo usar cada herramienta *(5 min)*

| Necesidad | Herramienta recomendada |
|---|---|
| Cliente con bajo volumen sin sistema | Factura Fácil (Mis Cuentas) |
| Cliente con volumen mediano/alto | PAC con sistema propio o integrado |
| Verificar si un CFDI recibido es válido | Verifica tus facturas (verificacfdi…) |
| Validar 50 CFDI a la vez | Validador masivo |
| Conciliar IVA mensual | Visor de Facturas Emitidas y Recibidas |
| Conciliar nómina vs ISR enterado | Visor de Comprobantes de Nómina (Patrón) |
| Cliente persona física revisando su anual | Visor de Comprobantes de Nómina (Trabajador) |
| Recuperar XML que se perdió | Cancela y recupera tus facturas |
| Cancelar un CFDI | Sistema PAC o portal del SAT (Cancela y recupera) |

---

## Bloque 2 — Casos prácticos de emisión correcta de CFDI *(35 min)*

Cinco casos representativos que verán los participantes en su despacho. Para cada uno: planteamiento, decisiones clave y resolución.

### 2.1 Caso 1: Honorarios profesionales con retención *(7 min)*

#### Planteamiento

Persona física, régimen 612 (Actividades Empresariales y Profesionales), presta servicios contables a una persona moral en régimen 601 (General). Cobra $10,000 + IVA. La persona moral debe retenerle ISR e IVA.

#### Decisiones clave

| Campo | Valor correcto |
|---|---|
| TipoDeComprobante | I |
| Emisor — RégimenFiscal | 612 |
| Receptor — RegimenFiscalReceptor | 601 |
| UsoCFDI del receptor | G03 (Gastos en general) |
| MetodoPago | PUE si paga en el momento; PPD si pagará después |
| FormaPago | 03 (Transferencia) si PUE; 99 si PPD |
| Concepto — ClaveProdServ | 84111506 (Servicios contables) |
| Concepto — ClaveUnidad | E48 (Unidad de servicio) |

#### Cálculo de impuestos

| Concepto | Monto |
|---|---|
| Subtotal | $10,000.00 |
| IVA trasladado (16%) | $1,600.00 |
| Retención ISR (10%) | $1,000.00 |
| Retención IVA (2/3 de IVA = 10.67%) | $1,066.67 |
| **Total a pagar al prestador** | **$9,533.33** |

#### Errores típicos a evitar

- No incluir las retenciones en el CFDI cuando el receptor es persona moral (LIVA art. 1-A).
- Confundir el régimen del emisor con el del receptor.
- Usar uso CFDI G01 (Adquisición de mercancías) en lugar de G03 (Gastos en general).

### 2.2 Caso 2: Venta a crédito con pagos parciales *(7 min)*

#### Planteamiento

Empresa vende mercancía por $50,000 + IVA el 10 de febrero de 2026. El cliente pagará en dos parcialidades: $30,000 el 25 de febrero y el resto el 15 de marzo.

#### Secuencia de CFDI a emitir

**CFDI #1 — 10 de febrero (factura por la operación)**

| Campo | Valor |
|---|---|
| TipoDeComprobante | I |
| MetodoPago | **PPD** |
| FormaPago | **99** (Por definir) |
| Subtotal | $50,000.00 |
| IVA | $8,000.00 |
| Total | $58,000.00 |

**CFDI #2 — 25 de febrero (REP por primer pago)**

Se debe emitir a más tardar el **5 de marzo de 2026**.

| Campo | Valor |
|---|---|
| TipoDeComprobante | P |
| Subtotal del comprobante | 0 |
| Total del comprobante | 0 |
| Moneda del comprobante | XXX |
| Pago — FechaPago | 2026-02-25 |
| Pago — FormaDePagoP | 03 (Transferencia) |
| Pago — Monto | 30,000.00 |
| DoctoRelacionado — UUID | UUID del CFDI #1 |
| DoctoRelacionado — NumParcialidad | 1 |
| DoctoRelacionado — ImpSaldoAnt | 58,000.00 |
| DoctoRelacionado — ImpPagado | 30,000.00 |
| DoctoRelacionado — ImpSaldoInsoluto | 28,000.00 |

**CFDI #3 — 15 de marzo (REP por segundo pago)**

Se debe emitir a más tardar el **5 de abril de 2026**. Misma estructura que el #2 pero con NumParcialidad=2, ImpSaldoAnt=28,000, ImpPagado=28,000, ImpSaldoInsoluto=0.

#### Errores típicos a evitar

- Emitir el CFDI #1 como PUE para "evitar" emitir REP. Esto causará discrepancia de IVA porque el SAT cruza fecha de emisión con fecha de pago real.
- Olvidar emitir el REP dentro del plazo de 5 días del mes siguiente.
- Calcular mal los impuestos proporcionales en el ImpuestosDR del REP.

### 2.3 Caso 3: Factura global RESICO PF *(7 min)*

#### Planteamiento

Tienda de abarrotes, persona física en RESICO (régimen 626), realiza ventas con público en general durante el mes de marzo de 2026 por $80,000.00 totales (IVA incluido).

#### Decisiones clave

- El RFC genérico para público en general es **XAXX010101000**.
- El nombre se registra como **PUBLICO EN GENERAL**.
- El uso del CFDI debe ser **S01** (Sin efectos fiscales).
- La periodicidad se registra mediante el nodo **InformacionGlobal** con periodicidad “04” (Mensual), Mes “03”, Año “2026”.

#### Plazo y restricciones especiales para RESICO PF

- **La factura global del RESICO PF solo se puede cancelar en el mismo mes en que se generó.**
- Debe emitirse a más tardar el día 17 del mes siguiente (según calendario RESICO; verificar contra la regla aplicable).

#### Errores típicos a evitar

- Usar XEXX010101000 en lugar de XAXX010101000 (XEXX es para residentes en el extranjero).
- No registrar el nodo InformacionGlobal.
- Pretender cancelar la global meses después.

### 2.4 Caso 4: Cliente que estaba en factura global pide nominativa *(7 min)*

#### Planteamiento

Después de emitir la factura global de marzo (Caso 3), el 5 de abril llega un cliente y solicita factura nominativa por una venta de $1,500 IVA incluido que estaba incluida en la global.

#### Procedimiento correcto

**Paso 1:** Emitir el CFDI nominativo al cliente con sus datos correctos:
- TipoDeComprobante: I
- Receptor: datos reales del cliente
- UsoCFDI: el que indique el cliente (típicamente G03)
- Conceptos: detalle de la venta original

**Paso 2:** Cancelar la factura global usando motivo de cancelación **04** (Operación nominativa relacionada en una factura global).

**Paso 3:** Reemitir la factura global, ahora SIN incluir la venta de $1,500 que ya se facturó nominativamente.

#### Errores típicos a evitar

- Olvidar el paso 3 (queda como ingreso duplicado: en la global cancelada y en la nominativa nueva si la global no se reemite correctamente).
- Usar motivo de cancelación 01 o 02 en lugar del 04 (que es el específico para este escenario).

### 2.5 Caso 5: CFDI de egreso por devolución *(7 min)*

#### Planteamiento

Empresa vendió mercancía por $20,000 + IVA en febrero. En marzo, el cliente devuelve $5,000 + IVA de mercancía defectuosa.

#### Procedimiento correcto

Emitir un **CFDI de Egreso (E)** por la devolución:

| Campo | Valor |
|---|---|
| TipoDeComprobante | **E** |
| Subtotal | $5,000.00 |
| IVA | $800.00 |
| Total | $5,800.00 |
| CfdiRelacionados — TipoRelacion | **03** (Devolución de mercancía sobre facturas o traslados previos) |
| CfdiRelacionados — UUID | UUID del CFDI de venta original |
| Receptor | Datos del cliente (mismo que la venta original) |
| UsoCFDI | El que el cliente indique para la nota de crédito |

#### ¿Cancelación o nota de crédito? — La pregunta del millón

Este es un tema que conviene discutir con el grupo:

- **Cancelación (motivo 01 + sustitución):** se usa cuando hay un error en el CFDI original.
- **CFDI de Egreso (E):** se usa cuando la operación SÍ ocurrió pero después se modifica (devolución, descuento, bonificación).

> **Regla práctica:** si el ajuste deriva de la realidad de la operación (devolución, descuento posterior), va por nota de crédito (CFDI E). Si el ajuste deriva de un error en la captura del CFDI, va por cancelación con sustitución.

### 🤔 Pregunta de reflexión

> En estos cinco casos, ¿cuál es el que con más frecuencia ven mal hecho en su despacho? ¿Por qué creen que se repite?

---

## ☕ DESCANSO *(30 min)*

---

## Bloque 3 — Estructura del XML: recorrido nodo por nodo *(45 min)*

### 3.1 Por qué el contador debe poder leer un XML *(5 min)*

Tres razones prácticas:

1. **Para diagnosticar errores** que el sistema reporta con códigos crípticos (CFDI40143, CRP20246, etc.).
2. **Para validar lo que el cliente o el proveedor le mandó** sin depender solo de la representación impresa (PDF).
3. **Para entender qué está revisando el SAT** cuando hace cruces y validaciones automáticas.

> **Idea fuerza:** el XML es el documento fiscal verdadero; el PDF es solo una representación impresa. Si hay diferencia entre ambos, manda el XML.

### 3.2 Anatomía de un CFDI 4.0 — recorrido por capas *(15 min)*

Vamos a recorrer un CFDI 4.0 de tipo Ingreso, simplificado:

```xml
<?xml version="1.0" encoding="utf-8"?>
<cfdi:Comprobante
    xmlns:cfdi="http://www.sat.gob.mx/cfd/4"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.sat.gob.mx/cfd/4 http://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd"
    Version="4.0"
    Serie="A"
    Folio="12345"
    Fecha="2026-03-15T10:30:00"
    Sello="AMifipYnPS5FuNW...[sello digital del emisor]"
    NoCertificado="30001000000500003416"
    Certificado="MIIFsDCCA5igAwIB...[certificado del emisor]"
    SubTotal="10000.00"
    Moneda="MXN"
    Total="11600.00"
    TipoDeComprobante="I"
    Exportacion="01"
    MetodoPago="PUE"
    FormaPago="03"
    LugarExpedicion="58000">

    <cfdi:Emisor
        Rfc="CACS890101AB1"
        Nombre="ISRAEL CASTRO URIETA"
        RegimenFiscal="612"/>

    <cfdi:Receptor
        Rfc="EMP010101AB2"
        Nombre="EMPRESA EJEMPLO SA DE CV"
        DomicilioFiscalReceptor="06600"
        RegimenFiscalReceptor="601"
        UsoCFDI="G03"/>

    <cfdi:Conceptos>
        <cfdi:Concepto
            ClaveProdServ="84111506"
            Cantidad="1"
            ClaveUnidad="E48"
            Descripcion="Servicios contables del mes de febrero 2026"
            ValorUnitario="10000.00"
            Importe="10000.00"
            ObjetoImp="02">

            <cfdi:Impuestos>
                <cfdi:Traslados>
                    <cfdi:Traslado
                        Base="10000.00"
                        Impuesto="002"
                        TipoFactor="Tasa"
                        TasaOCuota="0.160000"
                        Importe="1600.00"/>
                </cfdi:Traslados>
            </cfdi:Impuestos>
        </cfdi:Concepto>
    </cfdi:Conceptos>

    <cfdi:Impuestos TotalImpuestosTrasladados="1600.00">
        <cfdi:Traslados>
            <cfdi:Traslado
                Base="10000.00"
                Impuesto="002"
                TipoFactor="Tasa"
                TasaOCuota="0.160000"
                Importe="1600.00"/>
        </cfdi:Traslados>
    </cfdi:Impuestos>

    <cfdi:Complemento>
        <tfd:TimbreFiscalDigital
            xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital"
            Version="1.1"
            UUID="A1B2C3D4-E5F6-G7H8-I9J0-K1L2M3N4O5P6"
            FechaTimbrado="2026-03-15T10:30:15"
            RfcProvCertif="PAC850101XX1"
            SelloCFD="[sello del emisor]"
            NoCertificadoSAT="30001000000400000001"
            SelloSAT="[sello del SAT a través del PAC]"/>
    </cfdi:Complemento>
</cfdi:Comprobante>
```

### 3.3 Análisis nodo por nodo *(20 min)*

#### Encabezado del Comprobante

| Atributo | Significado | Cuidados |
|---|---|---|
| `Version="4.0"` | Versión del estándar | Debe ser 4.0 (única vigente) |
| `Serie` y `Folio` | Identificadores internos del emisor | Libre, pero recomendable mantener consecutividad |
| `Fecha="2026-03-15T10:30:00"` | Momento de emisión | Formato ISO 8601 (AAAA-MM-DDThh:mm:ss). Debe estar dentro de las 72 horas anteriores al timbrado. |
| `Sello` | Firma digital del emisor | Generada con la llave privada del CSD |
| `NoCertificado` | Número de serie del CSD | 20 dígitos |
| `Certificado` | Cadena del CSD en base64 | Permite al SAT validar el sello |
| `SubTotal` | Suma de importes antes de impuestos | Sin descuentos |
| `Moneda="MXN"` | Catálogo c_Moneda | Si no es MXN, requiere TipoCambio |
| `Total` | Suma final | Subtotal + traslados − retenciones (con redondeo) |
| `TipoDeComprobante` | I, E, T, N, P | Define qué validaciones aplican |
| `Exportacion="01"` | Catálogo c_Exportacion | "01" = No aplica; "02" = Definitiva A1; "03" = Temporal |
| `MetodoPago` | PUE o PPD | Debe ser consistente con FormaPago |
| `FormaPago` | Catálogo c_FormaPago | "99 Por definir" SOLO con PPD |
| `LugarExpedicion` | CP del lugar de expedición | Es el CP del establecimiento del emisor |

#### Nodo Emisor

| Atributo | Significado | Cuidados |
|---|---|---|
| `Rfc` | RFC del emisor | Debe estar activo y con CSD vigente |
| `Nombre` | Razón social o nombre completo | Sin abreviaturas, exactamente como en SAT |
| `RegimenFiscal` | Catálogo c_RegimenFiscal | Régimen vigente del emisor |

#### Nodo Receptor (los tres campos críticos del 4.0)

| Atributo | Significado | Cuidados |
|---|---|---|
| `Rfc` | RFC del receptor | Debe existir en lista del SAT (error CFDI40143 si no) |
| `Nombre` | Nombre/Razón social | Debe coincidir con SAT (error CFDI40148 si no) |
| `DomicilioFiscalReceptor` | CP del receptor | Debe ser el CP del domicilio fiscal en el SAT |
| `RegimenFiscalReceptor` | Régimen del receptor | Debe corresponder a un régimen vigente |
| `UsoCFDI` | Catálogo c_UsoCFDI | Debe ser compatible con el régimen del receptor (error CFDI40161 si no) |

#### Nodo Conceptos

Cada concepto representa un bien o servicio facturado:

| Atributo | Significado | Cuidados |
|---|---|---|
| `ClaveProdServ` | Catálogo c_ClaveProdServ | 8 dígitos; clave del SAT |
| `Cantidad` | Cantidad del bien o servicio | Hasta 6 decimales |
| `ClaveUnidad` | Catálogo c_ClaveUnidad | Unidad de medida estandarizada |
| `Descripcion` | Descripción libre | Específica; no “mercancía general” |
| `ValorUnitario` | Precio unitario | Sin impuestos |
| `Importe` | Cantidad × ValorUnitario | Validación matemática |
| **`ObjetoImp`** | **Catálogo c_ObjetoImp** | **Nuevo en 4.0:** 01=No objeto, 02=Sí objeto, 03=Sí objeto y no obligado al desglose, 04=Sí objeto y no causa impuesto |

#### Nodo Impuestos a nivel concepto y a nivel comprobante

Doble desglose: por cada concepto y luego un total a nivel comprobante.

- `Impuesto="001"` = ISR
- `Impuesto="002"` = IVA
- `Impuesto="003"` = IEPS
- `TipoFactor` = Tasa, Cuota o Exento
- `TasaOCuota` = la tasa aplicable (0.160000 para IVA 16%)

#### Nodo Complemento → TimbreFiscalDigital

Es el “sello” del SAT a través del PAC. Sin este nodo, el CFDI NO está timbrado y NO tiene validez fiscal.

| Atributo | Significado |
|---|---|
| `UUID` | Folio Fiscal único (36 caracteres) |
| `FechaTimbrado` | Momento del timbrado por el PAC |
| `RfcProvCertif` | RFC del PAC que timbró |
| `SelloCFD` | El sello del emisor (referencia) |
| `NoCertificadoSAT` | Certificado del SAT |
| `SelloSAT` | Sello del SAT que valida todo el comprobante |

### 3.4 Cómo abrir y leer un XML en la práctica *(5 min)*

Tres opciones para el contador:

1. **Notepad++ o cualquier editor de texto plano.** Gratis, funciona siempre. Si activas el “Pretty Print” con un plugin XML queda muy legible.
2. **Visualizadores XML web.** Hay varios gratuitos que permiten subir el XML y verlo estructurado.
3. **El propio sistema del PAC.** Casi todos tienen un visor que muestra el XML en formato amigable.

> **Tip:** cuando un cliente diga “mi factura no salió bien”, pedirle SIEMPRE el XML, no solo el PDF. El PDF puede ser cualquier diseño; el XML es la verdad.

---

## Bloque 4 — Validación de CFDI y cancelaciones paso a paso *(30 min)*

### 4.1 Validación de CFDI: las tres herramientas oficiales *(10 min)*

#### Herramienta 1: Verifica tus facturas (CFDI)

**URL:** verificacfdi.facturaelectronica.sat.gob.mx

**Datos requeridos:**
- Folio Fiscal (UUID).
- RFC del emisor.
- RFC del receptor.
- Captcha.

**Resultados posibles:**
- **Vigente:** el CFDI existe en los controles del SAT y no está cancelado. Es válido para fines fiscales.
- **Cancelado:** el CFDI fue cancelado. NO sirve para deducir.
- **No encontrado:** el CFDI no existe en los registros del SAT. Puede ser por: (a) menos de 72 horas desde el timbrado (todavía no se sincroniza), (b) error de captura del UUID/RFC, (c) factura apócrifa.

> **Importante:** la verificación es PÚBLICA y gratuita. No requiere autenticación. Cualquier persona puede verificar cualquier CFDI si tiene el UUID y los RFC.

#### Herramienta 2: Validador masivo

**URL:** tramitesdigitales.sat.gob.mx/Sicofi.ValidacionCFD

Permite cargar un archivo con múltiples CFDI a verificar simultáneamente. Útil para revisión mensual de facturas recibidas o para validación de carteras grandes.

#### Herramienta 3: Lectura de código QR

Cada CFDI 4.0 incluye un código QR en su representación impresa. Al escanearlo con cualquier lector se obtiene la URL de verificación con los datos pre-cargados.

**Tip operativo:** algunos contadores usan apps móviles de lectura de QR + verificación masiva como flujo eficiente para revisar grandes volúmenes de tickets de gastos.

### 4.2 Cancelación paso a paso *(15 min)*

Repasamos el procedimiento práctico de cancelación, ya con la teoría de la Clase 1 internalizada.

#### Procedimiento general en el portal del SAT

**Paso 1:** Ingresar a sat.gob.mx → Factura Electrónica → Cancela y recupera tus facturas. Autenticación con RFC y contraseña o e.firma.

**Paso 2:** Localizar el CFDI a cancelar (por UUID, fecha o filtros).

**Paso 3:** Seleccionar el motivo de cancelación (01, 02, 03 o 04).

**Paso 4:** Si el motivo es 01 (errores con relación) o 04 (operación nominativa de factura global), capturar el UUID del CFDI sustituto.

**Paso 5:** Confirmar la solicitud de cancelación.

**Paso 6:** Si requiere aceptación del receptor, esperar la respuesta (3 días hábiles) o la aceptación tácita.

**Paso 7:** Verificar el estatus final como “Cancelado”.

#### Procedimiento detallado por motivo

##### Motivo 01 — Comprobante emitido con errores con relación

> Caso típico: te equivocaste en el RFC, el importe, la descripción o cualquier dato que requiere reexpedición.

1. **Primero** emite el nuevo CFDI con los datos correctos.
2. En el nuevo CFDI, registra `CfdiRelacionados` con `TipoRelacion="04"` (Sustitución de los CFDI previos) y `UUID` del CFDI a cancelar.
3. **Después** solicita la cancelación del CFDI original con motivo **01** y captura el UUID del nuevo CFDI sustituto.
4. Si el sistema rechaza la cancelación con motivo 01, se puede usar motivo 02 como alternativa (criterio del SAT).

##### Motivo 02 — Comprobante emitido con errores sin relación

> Caso típico: emitiste un CFDI duplicado por accidente al cliente correcto, o un CFDI a un cliente equivocado y no necesitas reexpedirlo.

1. Solicita la cancelación con motivo 02.
2. NO se requiere registrar UUID sustituto.
3. NO emites un CFDI nuevo (a menos que sea otro caso).

##### Motivo 03 — No se llevó a cabo la operación

> Caso típico: facturaste anticipadamente y la operación se cayó.

1. Solicita la cancelación con motivo 03.
2. NO se requiere UUID sustituto.

##### Motivo 04 — Operación nominativa relacionada en una factura global

> Caso típico: el cliente que estaba en tu factura global ahora pide CFDI nominativo (Caso 4 del Bloque 2).

1. Emite el CFDI nominativo al cliente.
2. Cancela la factura global con motivo 04.
3. Reemite la factura global SIN la operación que ya está nominativa.

#### Cancelación sin aceptación del receptor

La regla **2.7.1.34** RMF 2026 mantiene los supuestos en los que NO se requiere aceptación del receptor:

- CFDI cancelado dentro de las **72 horas** posteriores a su emisión.
- CFDI con monto total hasta **$1,000.00** MXN (IVA incluido).
- CFDI por concepto de nómina (con limitaciones).
- CFDI a contribuyentes del extinto RIF.
- CFDI tipo Egreso, Traslado y Pago (con matices).
- CFDI con público en general (factura global) y emitidos a residentes en el extranjero.

#### Plazo límite de cancelación

- **Personas morales:** hasta el 31 de marzo del año siguiente al ejercicio en que se emitió el CFDI.
- **Personas físicas:** hasta el 30 de abril del año siguiente.
- **RESICO PF:** la factura global solo puede cancelarse en el mismo mes en que se generó.

### 4.3 Sanciones por cancelación incorrecta *(5 min)*

| Conducta | Sanción |
|---|---|
| No cancelar o cancelar fuera de plazo (CFF art. 81 fracc. XLVI y 82 fracc. XLII) | 5% a 10% del monto del CFDI |
| Cancelar sin justificación documental | El SAT puede verificarlo en facultades de comprobación |

> **Recomendación operativa:** llevar bitácora de cancelaciones donde se documente el motivo, soporte (correo del cliente, contrato cancelado, etc.) y fecha. Esta bitácora es la mejor defensa en una auditoría.

---

## Bloque 5 — Detección y corrección de errores fiscales *(8 min)*

### 5.1 Errores frecuentes con su código y solución

Tabla rápida de los errores que aparecen al timbrar y cómo resolverlos:

| Código | Mensaje | Causa común | Solución |
|---|---|---|---|
| **CFDI40143** | El RFC del receptor no existe en la lista de RFC inscritos no cancelados del SAT | RFC incorrecto, o receptor con CSD cancelado | Validar RFC en SAT; pedir Constancia (sin exigirla) o validar en línea |
| **CFDI40148** | El campo DomicilioFiscalReceptor debe pertenecer al nombre asociado al RFC | CP no coincide con el del receptor en SAT | Confirmar el CP del domicilio fiscal del receptor |
| **CFDI40161** | La clave del campo UsoCFDI debe corresponder con el tipo de persona y el régimen | Combinación inválida (ej.: G03 con régimen 605) | Revisar catálogo c_UsoCFDI vs régimen del receptor |
| **CRP20246** | El nodo hijo ImpuestosDR del nodo DoctoRelacionado debe existir | Falta desglose de impuestos en el REP | Agregar nodo ImpuestosDR con los impuestos del documento relacionado |
| Errores de cadena original | Discrepancia entre el sello y la cadena | CSD vencido, mal configurado o el XML fue alterado | Verificar vigencia del CSD; regenerar el sello |

### 5.2 Flujo recomendado de corrección

1. **Identificar el error** (código, mensaje, nodo afectado).
2. **Determinar si es estructural o de captura.**
3. **Si es de captura:** cancelar el CFDI defectuoso (motivo 01) y emitir uno nuevo con los datos correctos.
4. **Si es estructural** (CSD vencido, sistema mal configurado): primero corregir la causa raíz, luego reemitir.
5. **Documentar** en bitácora interna para evitar repetición.

### 5.3 Mini-caso integrador para el cierre

> **Escenario:** un cliente persona moral te entrega 30 facturas recibidas durante el mes para deducir. Tu equipo las captura y al cierre el sistema reporta que 4 de ellas tienen estatus “Cancelado” en el SAT, 2 no las encuentra (NO existen) y 1 tiene fecha posterior al cierre del ejercicio. ¿Qué haces con cada una?

**Respuesta esperada:**
- Las 4 canceladas: NO se pueden deducir. Comunicar al cliente y solicitar al proveedor reemisión o sustento de la cancelación.
- Las 2 no encontradas: investigar si tienen menos de 72 horas (esperar) o si son apócrifas (denunciar y NO deducir).
- La 1 con fecha posterior al cierre: NO se deduce en el ejercicio actual; se deduce en el ejercicio siguiente conforme al art. 27 fracc. XVIII LISR.

---

## Bloque 6 — Cierre y siguientes pasos *(2 min)*

### 6.1 Síntesis del módulo completo

Cerrando los dos bloques del Módulo 6:

1. El CFDI 4.0 es la espina dorsal de la fiscalización electrónica del SAT en 2026.
2. Las herramientas gratuitas del SAT son la red de seguridad del contador: úsalas como rutina, no solo cuando llega una carta.
3. El XML es la verdad fiscal; el PDF es solo la representación. Aprender a leer XML es una habilidad de defensa profesional.
4. Cancelar bien y a tiempo previene el 80% de los problemas con la deducibilidad y el acreditamiento.

### 6.2 Compromiso de aplicación

Pregunta abierta para el cierre:

> **De todo lo que vimos en este módulo, ¿qué es lo PRIMERO que vas a implementar el lunes en tu despacho?**

Invitar a 2 o 3 participantes a compartir antes de cerrar.

### 6.3 Enlace con los siguientes módulos del diplomado

Lo que viene en el Módulo 7 (Taller de Declaraciones y Cierre Fiscal) usará todo lo visto aquí:

- La validación de CFDI emitidos y recibidos será insumo para el cierre fiscal.
- Los Visores son insumo directo del prellenado de declaraciones anuales.
- Los REP son insumo del cálculo de IVA mensual.

Y en el Módulo 8 (Estrategias y Planeación Fiscal), el dominio del CFDI será la base para entender la fiscalización electrónica y la defensa del contribuyente.

---

## 📚 Referencias normativas y herramientas

### Leyes y reglamentos
- Código Fiscal de la Federación, arts. 29 y 29-A.
- Reglamento del CFF, art. 39.
- LISR art. 27 (requisitos de las deducciones).

### Resolución Miscelánea Fiscal 2026
- Reglas 2.7.1.4 (validación de CFDI), 2.7.1.7 (representación impresa), 2.7.1.29, 2.7.1.32, 2.7.1.34, 2.7.1.35.

### Anexos RMF 2026
- Anexo 20 — Estándar técnico del CFDI 4.0.

### Portales y herramientas oficiales del SAT
| Servicio | URL |
|---|---|
| Portal principal SAT | sat.gob.mx |
| Verificación de CFDI | verificacfdi.facturaelectronica.sat.gob.mx |
| Mis Cuentas / Factura Fácil | rfs.siat.sat.gob.mx |
| Validador masivo | tramitesdigitales.sat.gob.mx/Sicofi.ValidacionCFD |
| Verificación de Retenciones | prodretencionverificacion.clouda.sat.gob.mx |

### Documentos técnicos del SAT
- Guía de llenado del CFDI 4.0 (Anexo 20).
- Guía de llenado del Complemento para Recepción de Pagos 2.0 Revisión B.
- Guía de usuario del Visor de Comprobantes de Nómina (Patrón y Trabajador).
- Preguntas frecuentes y escenarios de cancelación conforme a la Reforma Fiscal 2022.

---

*Última actualización: mayo de 2026. Documento elaborado con base en la normativa fiscal vigente para el ejercicio 2026 y las herramientas operativas del SAT vigentes a la fecha de elaboración.*
