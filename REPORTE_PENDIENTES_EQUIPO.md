# Reporte de cierre y pendientes para el equipo

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


> **Actualización del 2 de octubre de 2026:** el usuario pidió retomar la publicación. Los permisos funcionan, los commits se publicaron en `main` y GitHub Actions pasó para `3cbb12a`. Último commit publicado: `0785534`, con reporte y bitácora actualizados; su [verificación final también terminó correctamente](https://github.com/Radioiza/Sistemas-Distribuidos-27-1/actions/runs/37101232459). El bloqueo 403 descrito abajo es histórico y está resuelto. Copia local sincronizada: 21 archivos. Siguen pendientes las cuentas, presupuestos, cálculos/evidencias incompletos y contribuciones del resto del equipo.

**Actualizado: 15 de octubre de 2026.** Trabajo reanudado por petición del usuario, en la sesión de Julissa (`IxchelHenaro`). La práctica sigue incompleta. Estado actual y rutas en [CONTEXTO_Y_PENDIENTES.md](CONTEXTO_Y_PENDIENTES.md).

Azure está bloqueado por un permiso guardado del navegador; AWS está pendiente de inicio de sesión. Ya se recuperó el [JSON oficial AWS EEUU](evidencias/P01/costos/P01_A3_aws_eeuu_oficial.json). No se verificaron cuentas ni presupuestos. Los resultados de octubre 1–2 siguientes se conservan como antecedentes.

## Qué queda entregado

Se guardaron en esta carpeta P1 los 20 archivos del repositorio, con copia comprobada contra el original. El reporte académico está en [practicas/P01/README.md](practicas/P01/README.md), las evidencias en [evidencias/P01/README.md](evidencias/P01/README.md) y el detalle para retomar en [CONTEXTO_Y_PENDIENTES.md](CONTEXTO_Y_PENDIENTES.md).

- Reporte redactado: tablas, análisis, seis respuestas, clasificación documental de servicios, explicación NIST, conclusiones, referencias y uso de IA. Los campos pendientes están señalados.
- Dos estimaciones AWS guardadas en la calculadora oficial: EEUU **USD 88.82/mes** y México **USD 92.97/mes**, con enlaces y capturas.
- Dos estimaciones Azure reconstruidas: EEUU **USD 201.82/mes** y México **USD 222.04/mes**. México sigue provisional por campos Blob sin tarifa disponible. Hay capturas y notas; faltan archivos XLSX oficiales.
- Estimación preliminar de EnlaceCorto: **USD 33.62/mes parciales**, pendiente de IPv4 y cierre. No es un presupuesto final.
- Propuesta EnlaceCorto, bitácoras y comprobación local de archivos, enlaces y patrones de credenciales.
- Último commit local: `3cbb12a`. Verificación: **20 archivos, 21 objetos históricos, cero incidencias detectadas**. Las imágenes se revisaron visualmente; esto no verifica cuentas ni gastos.

**No se desplegó infraestructura. No se verificó ningún presupuesto activo ni la facturación de las cuentas.**

## Orden recomendado para continuar

| Prioridad | Pendiente | Quién debe atenderlo | Evidencia de cierre |
|---|---|---|---|
| 1 | Recuperar acceso operativo a las consolas Azure y AWS | Cada integrante con sus cuentas | Capturas de identidad, región México, créditos y vencimiento, ocultando datos sensibles |
| 1 | Crear y verificar presupuestos reales | Cada integrante | Presupuesto mensual USD 5 por cuenta; alertas reales 50%, 80%, 100% y previsión 100%; capturas de configuración |
| 1 | Revisar recursos y facturación existentes | Cada integrante | Inventario de regiones, servicios activos y costo; no asumir gasto cero |
| 2 | Publicar cambios actuales | Julissa con identidad IxchelHenaro y acceso autorizado | El bloqueo anterior está resuelto; main sigue en 0785534. Faltan publicar esta continuación y verificar su Actions |
| 2 | Cerrar los cálculos Azure y del proyecto | Responsable de costos que designe el equipo | Resolver Blob México, exportar XLSX de ambas regiones y completar IPv4, total y exportación del proyecto |
| 3 | Completar evidencias B1 y B2 | Repartir entre los tres integrantes | 14 capturas de servicios, SaaS, cinco características NIST y comando de identidad en la terminal de nube |
| 3 | Ajustar imágenes al formato de entrega | Responsable del reporte | PNG anotados según la práctica, con configuración y detalles legibles; las capturas originales actuales son JPG |
| 4 | Completar contribuciones y revisión final | Los tres integrantes | Evidencias propias, commits propios, tablas completas, enlaces válidos y todas las casillas justificadas |
| 4 | Validar proyecto y entrega con docente | Equipo | Registro/aceptación de EnlaceCorto, recuperación del PDF original del proyecto y confirmación de entrega tardía |

### Detalle de presupuestos

Usar nombres `P1-<usuario>-<provider>`, monto mensual USD 5 y destinatarios correctos. Azure: verificar suscripción y fecha final 31 de diciembre de 2026. AWS: añadir control de gasto cero con umbral USD 0.01 y alerta Free Tier al 85%, según la práctica. Comprobar los ajustes en la cuenta real. Las alertas por sí solas no detienen recursos ni garantizan un límite de gasto.

### Detalle de costos

Conservar la misma carga de referencia entre proveedores: VM Linux 2 vCPU/4 GB durante 730 h, disco 30 GB, base relacional 1–2 vCPU/2–4 GB y 20 GB, objetos 50 GB/100 mil solicitudes, balanceador de aplicación y 100 GB de salida. Documentar mínimos de capacidad distintos y franquicias. Las estimaciones no incluyen necesariamente impuestos ni todos los componentes de producción.

Los resúmenes AWS actuales muestran el total; añadir capturas con el detalle de los servicios. Azure tiene diferencias de centavos por precisión interna: usar el total mostrado por la calculadora, sin sustituirlo por la suma redondeada. La estimación del prototipo no cubre toda la fase final con Kubernetes.

## Bloqueos encontrados

1. **Navegador:** el usuario confirmó «ya inicie». Después, la herramienta de acceso al navegador dejó de responder. No se pudo localizar ni verificar la sesión final. El equipo puede continuar directamente en su navegador; no hace falta asumir que el acceso personal falló.
2. **GitHub:** el 403 es histórico, resuelto el 2 de octubre. Se confirmó main en 0785534 durante esta continuación; los nuevos cambios locales no se han publicado.
3. **Archivos previos:** no están disponibles aquí los XLSX Azure del equipo anterior ni `SD_7CV1_Proyecto_Integrador.pdf`. Recuperarlos de su propietario si existen.
4. **Fechas:** la práctica indicaba entrega el 8 de septiembre y límite tardío el 10 de septiembre de 2026. El trabajo presente es del 1 de octubre. Consultar al docente; no retrofechar capturas ni presentar las bitácoras retrospectivas como pruebas históricas.

## Dónde retomar

- Carpeta de entrega: esta carpeta P1.
- Repositorio de trabajo: `C:/Users/Ixchel/Documents/Gobierno TI/Pratica1/P1` (copia de entrega sin .git; requiere un clon para publicar).
- Remoto: https://github.com/Radioiza/Sistemas-Distribuidos-27-1
- Leer primero el contexto actualizado y después las casillas del reporte académico.
- Tras resolver permisos, publicar desde el repositorio de trabajo. Las copias de P1 no contienen la carpeta `.git`.
- Juan Carlos y Julissa deben realizar sus contribuciones con sus propias identidades. No se les atribuyeron commits ajenos.

**Estado actual:** continuación autorizada; faltan acceso efectivo a cuentas, evidencias y publicación de los cambios nuevos. No confundir el cierre histórico del 2 de octubre con una orden vigente de detenerse.
