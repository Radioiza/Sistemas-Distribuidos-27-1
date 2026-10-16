# Práctica 1 — Contexto y pendientes actualizados

## Estado vigente — 16 de octubre de 2026

Julissa (`IxchelHenaro`) solicita continuar solo con AWS: informa que agotó sus créditos gratuitos de Azure. Esta aclaración sustituye su declaración anterior de no tener cuenta; el saldo Azure no se comprobó en consola. Azure queda fuera del trabajo operativo por petición expresa. La práctica exige dos proveedores: esta limitación no equivale a cumplir ese requisito.

### AWS comprobado el 15 de octubre

- Cuenta Ixchel Henaro y región México (Central), `mx-central-1`.
- Presupuesto mensual `P1-IxchelHenaro-aws`: USD 5, alertas reales 50/80/100% y prevista 100%; destinatario verificado.
- Presupuesto `P1-IxchelHenaro-aws-cero`: plantilla nominal USD 1, alerta por gasto real superior a USD 0.01; destinatario verificado.
- Preferencia Free Tier habilitada y guardada para el correo indicado por Julissa.
- Créditos restantes USD 120: crédito inicial USD 100 y bonificación USD 20 por configurar presupuesto. Vencimiento de créditos 14/10/2027; fin del plan gratuito 13/04/2027 o agotamiento previo.
- Factura estimada de octubre: USD 0.00, sin datos de uso. No es una factura definitiva.
- EC2 México: ninguna instancia; panel con cero volúmenes, instantáneas, IP elásticas y balanceadores; un grupo de seguridad. No se desplegó infraestructura.
- Inventario global incompleto: Tag Editor presentó errores de permisos y carga sin terminar; no demuestra ausencia de recursos en toda la cuenta.

### Segunda revisión del 16 de octubre

Ambos presupuestos continúan en buen estado y muestran USD 0.00 gastados y destinatario Verified. El mensual mantiene USD 5 y cuatro alertas; gasto cero mantiene el umbral > USD 0.01. Se guardaron capturas nuevas de ambos. El historial sigue mostrando DataUnavailableException. La captura nueva conserva su fecha real; no sustituye las verificaciones de septiembre faltantes.

### Entrega y pendientes

Publicado en main el commit [63eeb87](https://github.com/Radioiza/Sistemas-Distribuidos-27-1/commit/63eeb87bcfac9c1c43a8fd435a1fe9680185069c) con la identidad Git IxchelHenaro. [GitHub Actions correcto](https://github.com/Radioiza/Sistemas-Distribuidos-27-1/actions/runs/38859744523). Comprobación local: 37 archivos, 23 objetos históricos, cero incidencias antes de publicar. Esta validación comprueba integridad documental, no cumplimiento académico completo. El clon con historial está en la carpeta hermana `publicacion`; P1 conserva la copia de entrega. No incluir archivos temporales ni códigos de acceso.

La práctica sigue incompleta: faltan evidencias B1/B2, inventario global completo, PNG finales anotados, export oficial AWS México, cierre del costo del proyecto, aportaciones de otros integrantes y aceptación docente fuera de plazo. Azure y sus exportaciones quedan pendientes por la limitación indicada. No afirmar cumplimiento total.

Evidencias: [índice de cuentas](evidencias/P01/cuentas/README.md). El registro siguiente es histórico; ante contradicciones prevalece este estado.

---

## Estado histórico — 15 de octubre de 2026 (America/Mexico_City)

La continuación comenzó el 14 de octubre y la exportación AWS terminó el 15. **La práctica sigue incompleta.** El usuario autorizó retomar los pendientes y confirmó: integrante **Julissa**, usuario GitHub **IxchelHenaro**. No se han verificado sus cuentas, identidad en nube, créditos, gastos ni presupuestos. No se crearon recursos.

### Ubicación actual y continuidad

- Carpeta de trabajo: `C:/Users/Ixchel/Documents/Gobierno TI/Pratica1/P1`.
- Se extrajo `P1.zip` sin modificar el ZIP original. Esta carpeta es una copia de entrega **sin historial .git**; las rutas del equipo de Brian que aparecen en el registro histórico no son rutas de este equipo.
- Remoto existente: https://github.com/Radioiza/Sistemas-Distribuidos-27-1, rama `main`.
- Consulta remota realizada en esta continuación: HEAD y main apuntan a `0785534b229c3463daa9083f1a7d8e28e78d65dc`. El rechazo 403 del 1 de octubre quedó resuelto el 2; no volver a tratarlo como bloqueo vigente. Actions en verde es una comprobación histórica del 2 de octubre, no una ejecución de los cambios locales actuales.
- No se han publicado ni creado commits con la identidad de Julissa. Confirmar su acceso autenticado antes de publicar; no atribuirle los commits de Brian.
- Respaldo íntegro del contexto recibido: `tmp/CONTEXTO_ANTES_CONTINUACION_2026-10-14.md`.

### Avances comprobados

- [x] Extraer y leer contexto, reporte, índice, bitácora y los requisitos de las 11 páginas del PDF de la práctica.
- [x] Confirmar el commit remoto actual y separar los bloqueos históricos de los actuales.
- [x] Recuperar la estimación AWS EEUU: USD 88.82/mes y USD 1065.84/año. La pantalla indicó precios del 1 de octubre; no se pulsó Update estimate.
- [x] Descargar y guardar el JSON oficial `evidencias/P01/costos/P01_A3_aws_eeuu_oficial.json`, exportado el 15 de octubre. Contiene cuatro servicios, parámetros y totales. Nuevo enlace generado por AWS: https://calculator.aws/#/estimate?id=8f51df13da36d17a3f717c777ef6d562f638c6c3. La fecha de exportación no convierte los precios en una cotización actualizada.
- [x] Registrar a Julissa / IxchelHenaro para las nuevas evidencias, sin atribuirle verificaciones no realizadas.
- [x] Preparar comparación aritmética homogénea con los importes históricos, manteniendo la provisionalidad de Azure México.
- [x] Añadir al verificador un modo explícito `--solo-archivos` para esta copia sin Git. El modo normal conserva la comprobación obligatoria de historial para CI.

### Aclaración de Julissa — 15 de octubre de 2026

Julissa confirmó que NO tiene cuenta de Azure. No confundir los accesos históricos de Brian con los de ella. Falta crear y verificar su cuenta/oferta educativa, además de habilitar el permiso de navegación. Se volvió a mostrar AWS para iniciar sesión; Azure volvió a rechazar el acceso por un permiso guardado. No se creó ninguna cuenta.

### Bloqueos actuales y siguiente acción

1. **Azure:** abrir `https://portal.azure.com/` fue rechazado; el usuario autorizó habilitar acceso, pero el segundo intento informó un permiso guardado que sigue bloqueándolo. El usuario debe cambiar ese permiso. No intentar otras vías para eludirlo.
2. **AWS:** se abrió la consola y llegó a la pantalla de inicio de sesión. Se solicitó al usuario iniciar sesión directamente; último estado observado: formulario IAM, sin sesión autenticada comprobada. No pedir ni guardar contraseñas o códigos en archivos/chat.
3. **Datos personales necesarios tras el acceso:** confirmar titular, cuentas/suscripciones y correo destinatario de alertas. Los nombres propuestos para Julissa son `P1-IxchelHenaro-azure`, `P1-IxchelHenaro-aws` y `P1-IxchelHenaro-aws-cero`. Revisar primero presupuestos existentes.
4. **Archivos faltantes:** exports Azure y PDF original del proyecto; no están en el ZIP. El JSON AWS EEUU ya no está pendiente; el de México sí.
5. **Dependencias humanas/temporales:** cuentas y evidencias propias de los tres integrantes; commits auténticos; verificación al día siguiente de configurar presupuestos; aceptación docente fuera del plazo original. No se pueden sustituir con documentación generada.

### Pendientes activos

- [ ] A1/A2: entrar a cada cuenta real, verificar suscripción/plan y créditos; crear o corregir presupuestos USD 5 (50/80/100% real y 100% previsto), gasto cero AWS y Free Tier aplicable; capturar listado y detalle.
- [ ] A1/B3: región México, facturación, créditos/vencimiento e inventario por cuenta; justificar recursos existentes. No declarar gasto cero sin evidencia.
- [ ] A2: segunda verificación al día siguiente de la configuración efectiva. Las fechas de septiembre siguen sin pruebas auténticas.
- [ ] A3 AWS: export México y capturas detalladas de ambos escenarios. EEUU ya tiene export oficial validado.
- [ ] A3 Azure: resolver Blob México, exportar ambas regiones, terminar IPv4 y total del proyecto con export y captura.
- [ ] B1: 14 capturas de servicios con cobro, gratuidad y disponibilidad mexicana, más SaaS. El PDF permite páginas públicas de precios; no todas requieren login, aunque la disponibilidad debe verificarse.
- [ ] B2: cinco capturas NIST y comando de identidad en cuenta real.
- [ ] Convertir evidencias finales a PNG anotados y legibles, conservando originales y fecha real.
- [ ] Recuperar convocatoria original del proyecto, confirmar registro y autorización docente de entrega tardía.
- [ ] Publicar los cambios nuevos desde un clon con historial e identidad autenticada de Julissa; revisar Actions de ese nuevo commit. Incorporar aportaciones auténticas de cada integrante.

Ver [reporte del equipo](REPORTE_PENDIENTES_EQUIPO.md) y [bitácora actual](bitacora/2026-10-15.md). Los detalles técnicos históricos se conservan a continuación; ante contradicciones, prevalece este estado vigente.

---

## Registro histórico recibido (1–2 de octubre; no es el estado actual)


> **Actualización del 2 de octubre de 2026:** el usuario pidió retomar la publicación. Los permisos funcionan, los commits se publicaron en `main` y GitHub Actions pasó para `3cbb12a`. Último commit publicado: `0785534`, con reporte y bitácora actualizados; su [verificación final también terminó correctamente](https://github.com/Radioiza/Sistemas-Distribuidos-27-1/actions/runs/37101232459). El bloqueo 403 descrito abajo es histórico y está resuelto. Copia local sincronizada: 21 archivos. Siguen pendientes las cuentas, presupuestos, cálculos/evidencias incompletos y contribuciones del resto del equipo.

Actualizado: 1 de octubre de 2026, después de continuar en el equipo de Brian. **Leer este estado antes de actuar.** Sustituye el inventario de la sesión del equipo de Carlo. El contexto anterior se conserva localmente en `tmp/CONTEXTO_ANTES_CONTINUACION_2026-10-01.md`.

## Objetivo y estado honesto

Completar la Práctica 1 de Sistemas Distribuidos, 7CV1, semestre 27/1: cuentas reales en al menos dos nubes, presupuestos individuales, cuatro estimaciones regionales y una del proyecto, evidencias, reporte, bitácora y repositorio público. El usuario pidió avanzar con todo lo pendiente y guardar este documento antes de agotar los recursos de la sesión.

**La práctica sigue incompleta.** Se avanzó en cálculos y documentación, pero no se verificó ningún presupuesto activo ni el inventario/facturación de las cuentas. No se desplegó infraestructura. No afirmar que la factura sea cero. La prioridad al retomar son las cuentas y alertas reales.

## Equipo y proyecto, ya decididos

- Escalona Zuñiga Juan Carlos.
- Henáro Sánchez Julissa Ischel.
- Bernal Ramírez Brian Ricardo.

Proyecto: **opción 3, EnlaceCorto, acortador de URLs con estadísticas**. Registro y validación docente pendientes. Alcance y arquitectura en `proyecto/PROPUESTA.md`, copia original `PROPUESTA_PROYECTO.md`. No volver a preguntar nombres ni tema.

Prototipo: creación de URLs HTTP/HTTPS, redirección por código, desactivación, estadísticas agregadas y panel protegido. Evolución a servicios separados de enlaces y estadísticas, eventos con deduplicación, contenedores, Kubernetes, métricas, balanceo, autoescalado y prueba de carga/recuperación. No implementado. No confundir elegir un tema con acreditar hitos.

## Rutas y archivos reales

- **Entrega actual:** `C:\Users\Brian Ricardo\OneDrive - sales.stratacache.com\Escritorio\P1\P1`.
- **Repositorio Git fuera de OneDrive:** `C:\Users\Brian Ricardo\source\sistemas-distribuidos-27-1`.
- **Remoto:** https://github.com/Radioiza/Sistemas-Distribuidos-27-1 (origin, rama main).
- **Fuente de requisitos:** `Practica1_ConsolasCostosAlertas_SD_2026.pdf` en P1, leído completo (11 páginas).
- **Reporte:** `practicas/P01/README.md`.
- **Índice:** `evidencias/P01/README.md`.
- **Costos:** `evidencias/P01/costos/`.
- **Bitácoras:** `bitacora/2026-09-01.md`, `2026-09-08.md`, `2026-10-01.md`.
- **Seguridad/CI:** `.gitignore`, `scripts/verificar_repositorio.py`, `.github/workflows/verificacion.yml`.

El repositorio público estaba vacío al iniciar. Se clonó aquí y se reconstruyó el contenido. Los XLSX Azure y los JPG citados en el contexto anterior NO se encontraron en este equipo ni en el remoto. No asumir que existen todavía en otra carpeta local. El PDF original `SD_7CV1_Proyecto_Integrador.pdf` tampoco está aquí: la propuesta y el contexto anterior conservan sus requisitos, pero debe recuperarse antes de validar el proyecto completo.

## Bloqueos reales detectados

### Acceso a consolas

Se abrieron Azure y AWS en el navegador integrado. Azure llegó a la pantalla «Estamos actualizando nuestros términos» de Microsoft; AWS mostraba inicio de sesión. El usuario confirmó que tiene acceso y después dijo **«ya inicie»**. Al buscar las sesiones iniciadas, la conexión del navegador dejó de responder. Una consulta de estado terminó con timeout; no se verificó la consola final. No concluir que el usuario no inició sesión: puede haberlo hecho en otra pestaña o navegador.

Al retomar, inspeccionar las pestañas disponibles con las herramientas documentadas y localizar la cuenta real. Si se requiere SMS, identidad, términos o autenticación personal, dejar que el usuario lo complete. Nunca guardar contraseñas ni códigos. No crear una cuenta duplicada ni pasar a un plan de pago para evitar un bloqueo de acceso.

### Publicación GitHub

Primer commit documental: `c2d5c13`. Último commit de cierre: `3cbb12a`. El verificador final revisó 20 archivos y 21 objetos históricos sin incidencias. Se corrigió un espacio final señalado por la comprobación de formato.

**Push rechazado con HTTP 403:** `Permission to Radioiza/Sistemas-Distribuidos-27-1.git denied to zahirobrian`.

La identidad Git local es Brian Bernal y la credencial GitHub disponible pertenece a `zahirobrian`. Falta permiso de escritura de esa cuenta en el repositorio de Radioiza o autenticación de un titular autorizado. No cambiar de repositorio ni publicar bajo otro propietario sin indicación del usuario. No se verificó GitHub Actions en verde porque no hubo publicación. Los commits de Juan Carlos y Julissa siguen pendientes; no suplantarlos.

## Trabajo completado en esta continuación

- [x] Leer contexto, propuesta y práctica completa; corregir rutas e inventario.
- [x] Clonar repositorio vacío fuera de OneDrive y configurar origin.
- [x] Reconstruir y guardar oficialmente dos estimaciones AWS con enlaces recuperables.
- [x] Guardar dos capturas originales de resumen AWS (solo muestran total; falta detalle gráfico).
- [x] Reconstruir Azure México y East US, guardar capturas y transcripción de controles visibles.
- [x] Revisar visualmente las cuatro capturas públicas; sin credenciales ni tarjetas visibles.
- [x] Redactar reporte con tablas de cuentas/costos/modelos, NIST, seis respuestas, conclusiones, fuentes, uso de IA y contribuciones honestas.
- [x] Preparar bitácoras retrospectivas que declaran ausencia de pruebas históricas, y bitácora real del 1 de octubre.
- [x] Preparar y ejecutar verificación local de archivos, enlaces y patrones de secretos; revisar historial.
- [x] Crear commit local con identidad configurada de Brian e intentar publicación.

El reporte tiene secciones redactadas, pero sus casillas pendientes son reales. Una clasificación documental de servicios no equivale a 14 capturas en consola.

## A3 — AWS: resultados guardados

### Enlaces oficiales

- EEUU: https://calculator.aws/#/estimate?id=04afdcc60391888f9172f113fae935df22d5a2b0
- México: https://calculator.aws/#/estimate?id=a16c4de12b7ba4ca2ae2230bd42675e57376ee9f

En `P01_A3_aws_eeuu.md` y `P01_A3_aws_mexico.md` se conservan enlaces y resultados. El proveedor indica vigencia del enlace de un año. Se intentó JSON, pero no se recuperó un archivo local verificable. No inventar un JSON con apariencia de export oficial: los enlaces guardados son la evidencia recuperable actual.

| Recurso | México USD/mes | us-east-1 USD/mes |
|---|---:|---:|
| EC2 Linux t3.medium 730 h + EBS gp3 30 GB | 34.42 | 32.77 |
| RDS PostgreSQL db.t3.small 730 h + gp2 20 GB | 30.16 | 28.58 |
| S3 Standard 50 GB + solicitudes | 1.30 | 1.24 |
| ALB | 18.09 | 17.23 |
| Salida Internet bruta 100 GB | 9.00 | 9.00 |
| **Mensual bruto** | **92.97** | **88.82** |
| **Anual bruto** | **1115.64** | **1065.84** |

Diferencia bruta: USD 4.15, **4.67%**. EC2+EBS explica USD 1.65 de diferencia, RDS USD 1.58. La salida ya está incluida en la fila EC2 del resumen del proveedor (43.42 México, 41.77 EEUU); el reporte la separa sin duplicarla.

Configuración: pago por uso, VM 2 vCPU/4 GiB; RDS 2 vCPU/2 GiB, Single-AZ, sin Proxy, sin Database Insights avanzado ni Extended Support. S3 10,000 escrituras y 90,000 lecturas. ALB 730 horas, 100/730 GB/h procesados, 1 conexión nueva/s, duración 60 s, 1 solicitud/s y 1 regla por solicitud; dimensión dominante 0.13698630137 LCU.

No se incluyen IPv4, dominio, NAT, logs adicionales, snapshots ni créditos excedentes de CPU burstable. Si la franquicia general de los primeros 100 GB de salida está íntegra, restar USD 9 una sola vez por escenario independiente: 83.97 México y 79.82 EEUU al mes, antes de créditos y otros cargos. No aplicar la franquicia completa a varias cargas simultáneas de la misma cuenta.

## A3 — Azure: valores reconstruidos, exportación pendiente

Leer `evidencias/P01/costos/P01_A3_azure_reconstruccion.md` y los dos archivos `_observacion.txt` (transcripciones de controles, no exports). Capturas `_original.jpg` guardadas.

| Componente | Mexico Central USD/mes | East US USD/mes |
|---|---:|---:|
| VM B2s Ubuntu + E4 32 GiB | 36.07 | 32.77 |
| PostgreSQL Flexible B1MS + 32 GiB | 17.70 | 16.09 |
| Blob GPv2 Hot LRS 50 GB + operaciones | 1.24 | 1.13 |
| Application Gateway Standard V2 | 167.02 | 151.84 |
| **Total mensual de calculadora** | **222.04** | **201.82** |
| **Total anual de calculadora** | **2664.43** | **2421.89** |

**Corrección importante:** los apuntes anteriores sumaban subtotales redondeados (222.03 y 201.83). Los totales oficiales observados usan precisión interna. Conservar 222.04 y 201.82 y los anuales mostrados; diferencia visible USD 20.22, 10.02%.

VM y BD 730 h. Disco 32 GiB por nivel/mínimo frente a 30/20 GB. VM tiene Internet Egress 100 GB vía Microsoft Global Network, región correspondiente; USD 0 por franquicia indicada en la calculadora. PostgreSQL Burstable B1MS, 0 respaldo adicional, LRS, sin Extended Support. Blob 1 × 10,000 escrituras, 9 × 10,000 lecturas, cero listados y otras operaciones; Data Retrieval 100 GB. Gateway 730 h, 1 compute unit, 1,000 conexiones persistentes, 1 mb/s y 0 GB de salida para evitar duplicar VM.

**Incidencia pendiente de Blob:** descripción conserva «1,000 GB Data Write», campo sin entrada editable en East US, donde se indica gratuidad por GB. En México Data Retrieval y Data Write dicen que no hay precio para esa selección. No equivale a 1,000 GB de salida; no afirmar gratuidad mexicana por ausencia de tarifa. Resolver antes de dar el total por definitivo.

El botón Export no produjo un XLSX recuperable en esta sesión. Save/Share requerían login. Volver a exportar y verificar el archivo descargado. La LCU de AWS no equivale a la unidad de capacidad de Gateway: no presentar comparación de rendimiento.

## A3 — Proyecto: parcial guardado en notas

Leer `evidencias/P01/costos/P01_A3_proyecto_preliminar.md`.

Hipótesis: 100 enlaces nuevos y 10,000 redirecciones/mes; 1 GB lógico BD; 1 GB exportaciones; 1 GB salida. Prototipo East US con VM Ubuntu B1ms 1 vCPU/2 GB, SSD E4 32 GiB, PostgreSQL B1MS con mínimo 32 GiB y Blob 1 GB. Se proponen 100 PUT y 100 GET de exportaciones (0.01 × 10,000 cada uno); redirecciones consultan BD.

Valores observados: VM+disco+salida 17.51, BD 16.09, Blob 0.02; **suma parcial USD 33.62/mes**. No es total final. Se retiró Gateway solo de la simulación del prototipo y se pulsó añadir IP Addresses. Falta configurar una IPv4 Standard 730 h, revisar costo total, guardar/exportar y capturar. El navegador falló antes de verificar ese componente. No hay captura/export del proyecto finalizado.

Kubernetes, réplicas y observabilidad de la fase final necesitan otra estimación. No atribuir disponibilidad o rendimiento al prototipo sin pruebas. El umbral USD 5 no financia esta infraestructura: no desplegar sin créditos y presupuestos verificados.

## Pendientes prioritarios al retomar

### 1. A1/A2: todas las cuentas reales de cada integrante

- [ ] Localizar las sesiones que el usuario dijo haber iniciado; confirmar identidad, suscripción/plan, regiones y permisos.
- [ ] Azure: verificar oferta educativa, créditos y vencimiento; presupuesto `P1-<usuario>-azure`, USD 5 mensual, expiración 31/12/2026, ámbito de suscripción. Actual 50/80/100%, Forecast 100%, correo confirmado del titular. Revisar Cost alerts y listado/detalle.
- [ ] AWS: USD 5 `P1-<usuario>-aws`, umbrales exactos 50/80/100% actual y 100% forecast. Gasto cero `P1-<usuario>-aws-cero` con USD 0.01 y alertas Free Tier 85% aplicables al plan. Revisar presupuestos existentes para no duplicar.
- [ ] Capturar por cuenta inicio/identidad, selector México y facturación/créditos/vencimiento. Completar tabla de cuentas y destinatarios con datos reales.
- [ ] Juan Carlos y Julissa deben configurar/aportar sus cuentas y capturas personales. No usar una cuenta compartida como sustituto.
- [ ] Segunda verificación real al día siguiente de la configuración actual, fechada correctamente. No sustituye pruebas de septiembre.

### 2. A3: cerrar y exportar

- [ ] Recuperar exports JSON/CSV de los enlaces AWS y capturar el detalle de servicios, además del resumen ya guardado.
- [ ] Exportar Azure México y EEUU a XLSX; resolver campos Blob sin tarifa; cotejar precisión, salida y cantidades.
- [ ] Terminar IPv4 y total del proyecto, exportar y guardar evidencia.
- [ ] Homogeneizar la comparación entre proveedores: AWS incluye USD 9 de salida bruta, Azure aplica franquicia. Mantener bruto y neto condicionados claramente identificados.

### 3. B1/B2: pruebas de modelos y NIST

- [ ] 14 capturas de modelos: IaaS, PaaS, FaaS, contenedores, BD, objetos e IA por cada proveedor; unidad de cobro, gratuidad y disponibilidad mexicana reales.
- [ ] Captura SaaS de GitHub Pricing.
- [ ] Cinco capturas NIST: asistente VM sin crear, identidad en Cloud Shell, selector región/zonas/familias, menú tamaños o autoescalado, facturación y presupuesto.
- [ ] Consultar `aws sts get-caller-identity` o `az account show` en la cuenta correspondiente; evitar secretos y costos de almacenamiento no previstos al abrir Cloud Shell.
- [ ] Verificar SKU/región por servicio. El listado oficial consultado de Elastic Beanstalk no incluía mx-central-1. Bedrock requiere revisar modelo y ubicación de inferencia; no asumir disponibilidad mexicana general.

### 4. B3 y evidencia final

- [ ] Inventariar cada cuenta y todas las regiones requeridas; justificar recursos previos. No borrar recursos preexistentes sin conocer su función/propietario.
- [ ] Capturar gasto, créditos y presupuestos actuales; no afirmar factura cero sin consulta.
- [ ] Preparar PNG anotados `P01_<actividad>_<proveedor>_<usuario>_<n>.png`. Los cuatro archivos actuales son JPG originales sin anotación gráfica y se conservaron como fuentes; todavía no cumplen el formato final.
- [ ] Revisar legibilidad y cada imagen antes de publicar. AWS actual solo muestra total, no detalle de recursos.

### 5. Publicación y cierre

- [ ] Resolver permiso de escritura del usuario GitHub `zahirobrian` en el repositorio de `Radioiza`, o autenticar un titular autorizado.
- [ ] Publicar main y verificar GitHub Actions en verde. No recrear el repositorio ni inventar acceso.
- [ ] Incorporar commits propios de Juan Carlos y Julissa, sus usuarios GitHub y evidencias.
- [ ] Revisar las secciones provisionales del reporte y marcar casillas solo al verificar pruebas.
- [ ] Mantener sincronizada la copia de entrega P1 sin `.git`; el repositorio operativo debe seguir fuera de OneDrive.

## Fechas y limitaciones históricas

La práctica pidió sesiones del 1 y 8 de septiembre de 2026, evidencia adicional del 2, entrega el 8 antes de 16:30 y tardía hasta el 10 con penalización; después indica que no se recibe. No consta permiso docente posterior. Las bitácoras creadas ahora declaran ausencia de evidencia histórica. No cambiar fechas ni fabricar capturas/commits.

Según contexto previo del proyecto: registro 14 de septiembre, F1–F2 29 de septiembre, F3–F4 3 de noviembre, F5 19, F6 24, F7 8 de diciembre y exposición 10 de diciembre. Recuperar convocatoria original para cotejar; no consta registro ni entregas pasadas.

## Fuentes y herramientas para continuar

- Práctica PDF local, autoridad principal de requisitos.
- https://calculator.aws/ y https://azure.microsoft.com/en-us/pricing/calculator/
- https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets
- https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit
- https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html
- https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html
- https://aws.amazon.com/free/free-tier-faqs/
- https://aws.amazon.com/ec2/pricing/on-demand/
- https://doi.org/10.6028/NIST.SP.800-145
- https://github.com/pricing

Más referencias junto a las afirmaciones en el reporte. La verificación local usa Python 3; el `python` global del equipo es 2.7, por lo que se utilizó el intérprete empaquetado de Codex:
`C:\Users\Brian Ricardo\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`.

Última consulta de capacidad durante esta continuación: 72% de uso de la ventana semanal, antes de guardar el cierre. No es un saldo de dólares ni un contador de tokens y puede cambiar. Guardar resultados de forma incremental, sin esperar a agotar el acceso.

## Cierre a solicitud del usuario — 2 de octubre de 2026

El usuario pidió terminar el trabajo actual y detenerse. Se guardó `REPORTE_PENDIENTES_EQUIPO.md` con el orden de continuación, responsables sugeridos y pruebas necesarias. Se copiaron los 20 archivos versionados desde el repositorio externo a P1 y se comprobó que sus contenidos coinciden. Último commit: `3cbb12a`; sin publicación remota por el bloqueo 403 ya descrito. No reanudar operaciones de nube ni publicación sin una nueva petición del usuario.

## Resultado de validación de la continuación del 15 de octubre

27 archivos revisados en modo --solo-archivos, cero incidencias. Historial Git no revisado; no hay publicación de estos cambios. JSON oficial AWS EEUU analizado: cuatro servicios, suma mensual 88.82 y anual 1065.84 USD. Los demás cierres requieren las evidencias señaladas en el estado vigente al inicio de este documento.


## Avance de AWS — 15 de octubre de 2026 (prevalece sobre el estado anterior)

Se confirmó sesión de Julissa en la cuenta Ixchel Henaro, región México (Central), mx-central-1. Panel de créditos: USD 100 restantes y USD 0 utilizados; inicio 14/10/2026, vencimiento del crédito 14/10/2027. El menú del plan gratuito indica fin de acceso 13/04/2027 o al agotar créditos; son fechas distintas.

Correo destinatario confirmado expresamente por el usuario: jhenaros1900@alumno.ipn.mx.

Se crearon P1-IxchelHenaro-aws-cero con la plantilla oficial (presupuesto nominal USD 1, alerta real por gasto > USD 0.01) y P1-IxchelHenaro-aws mensual recurrente de USD 5, desde octubre de 2026, todos los servicios, con alertas reales 50/80/100% y prevista 100%, sin acciones sobre recursos. El listado confirmó ambos en buen estado. El de gasto cero mostró USD 0 utilizado; el mensual recién creado mostró importe utilizado no disponible. No declarar factura cero ni inventario vacío. La previsualización de Cost Explorer indicó DataUnavailableException.

AWS requiere verificar los destinatarios nuevos por correo; se avisó al usuario. Falta comprobar verificación, recepción, preferencias Free Tier, inventario, factura, capturas finales y segunda revisión real el 16/10/2026. La configuración de presupuestos no despliega infraestructura.

Permiso Azure: la documentación oficial ubica sitios permitidos/bloqueados en Configuración de la aplicación > Navegador. Se explicó cómo cambiar portal.azure.com y se solicitó captura de Configuración si la opción no aparece. Julissa aún no tiene cuenta Azure.


Comprobación posterior en detalle: presupuesto mensual USD 5, periodo mensual desde 2026-10-01, estado En buen estado, importe gastado mostrado USD 0.00; historial/gráfico aún sin datos. Destinatario con estado Pending, 0/1 email verified y cuatro alertas asociadas. Debe verificar el correo antes de recibir alertas.


### Incidencia de verificación de correo — 15/10/2026

El usuario aportó una captura con error HTTP 400: el código de activación del enlace no coincide con el registrado por AWS (Input token did not match stored Activation Token). Se consultó el presupuesto: destinatario aún Pending, 0/1 verificado. Se pulsó una vez Resend verification; AWS respondió Failed to send verification al destinatario confirmado. No se confirmó envío nuevo ni activación. No repetir enlaces anteriores ni marcar las alertas como operativas hasta verificar destinatario. La documentación de ActivateEmailContact indica códigos con vigencia de 12 horas y máximo de cinco intentos; no se conoce la causa concreta del fallo actual. Pendiente comprobar si el usuario abrió el mensaje más reciente y, de persistir el fallo de reenvío, resolverlo con soporte AWS. No se guardaron códigos ni enlaces de activación.

### Verificación de correo resuelta — 15/10/2026

Tras confirmar el usuario que verificó el mensaje, se recargó AWS y se comprobó en ambos presupuestos: jhenaros1900@alumno.ipn.mx con estado Verified y 1/1 email verified. En P1-IxchelHenaro-aws figuran cuatro alertas asociadas; en P1-IxchelHenaro-aws-cero figura Costo real > 0.01 USD. Ambos en buen estado. El bloqueo de activación y el fallo de reenvío anteriores quedan como antecedentes resueltos. No se comprobó recepción de una alerta disparada. Faltan la segunda revisión del 16/10, capturas finales, Free Tier e inventario/facturación completos; Azure sigue pendiente.
