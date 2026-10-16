# Práctica 1 · Consolas, costos y alertas

**IPN · ESCOM · Sistemas Distribuidos · 7CV1 · Semestre 27/1**

Docente: MBA. Rodrigo Ojeda Santillán. Fecha de elaboración: 1 de octubre de 2026. Revisión documental: 16 de octubre de 2026.

Integrantes: Escalona Zuñiga Juan Carlos; Henáro Sánchez Julissa Ischel; Bernal Ramírez Brian Ricardo.

**Estado: entrega en elaboración.** Las alertas y capturas originales AWS de Julissa están disponibles; quedan pendientes otros integrantes, inventario global y evidencias finales. La investigación documental y los cálculos no acreditan estas actividades. Las fechas de septiembre solicitadas por la práctica ya transcurrieron; no se dispone de evidencia original ni autorización docente de recepción tardía.

**Continuación actual:** Julissa, usuario GitHub `IxchelHenaro`, confirmado por el usuario. AWS verificado el 15/10: dos presupuestos creados, gasto cero con alerta > USD 0.01 y mensual USD 5 con 50/80/100% real y 100% previsto. El correo está Verified (1/1 verificado) en ambos presupuestos, comprobado el 15/10; hay capturas originales y una segunda revisión del presupuesto mensual el 16/10. Free Tier habilitado; factura estimada USD 0.00 el 15/10. Inventario global y formato final pendientes. Azure: la usuaria informa créditos agotados y solicita trabajar solo con AWS. [Bitácora actual](../../bitacora/2026-10-15.md).

Proyecto seleccionado: [EnlaceCorto, acortador de URLs con estadísticas](../../proyecto/PROPUESTA.md). Candidato provisional: Azure for Students, sujeto a comprobar elegibilidad, saldo y disponibilidad. [Índice de evidencias](../../evidencias/P01/README.md).

## 1. Cuentas y presupuestos — A1 y A2

### Tabla 1. Cuentas del equipo

| Integrante | Proveedor | Identificador de cuenta | Unidad de facturación | Región México | Créditos y vencimiento | Correo de alertas |
|---|---|---|---|---|---|---|
| Juan Carlos | Por verificar | Pendiente | Según proveedor | Pendiente en consola | Pendiente | Pendiente |
| Julissa | AWS | Ixchel Henaro (cuenta verificada en consola) | Cuenta AWS | México (Central), mx-central-1 | USD 120 restantes; crédito vence 14/10/2027; plan gratuito hasta 13/04/2027 o agotar crédito | jhenaros1900@alumno.ipn.mx, Verified el 15/10/2026 |
| Brian | Azure | Acceso iniciado; suscripción pendiente | Suscripción | Mexico Central, pendiente en cuenta | Pendiente | Pendiente de confirmar |
| Brian | AWS | Acceso confirmado verbalmente; sesión pendiente | Cuenta AWS | mx-central-1, pendiente en cuenta | Pendiente | Pendiente de confirmar |

Cada integrante añadirá una fila por cuenta real. El uso de una calculadora pública no confirma que una cuenta exista ni que la región esté habilitada. No copiar saldos comerciales como si fueran créditos concedidos.

### Configuración requerida y situación

| Proveedor | Presupuesto mensual | Umbrales reales | Pronóstico | Configuración adicional | Verificación |
|---|---|---|---|---|---|
| AWS | USD 5, `P1-<usuario>-aws` | 50%, 80%, 100% | 100% | Gasto cero `P1-<usuario>-aws-cero` al superar USD 0.01; Free Tier al 85% cuando aplique | Pendiente |
| Azure | USD 5, `P1-<usuario>-azure` | 50%, 80%, 100% | 100% | Ámbito suscripción; periodo mensual; vencimiento 31/12/2026 | Pendiente |

Los umbrales equivalen a USD 2.50, 4.00 y 5.00. El correo debe pertenecer al titular y revisarse diariamente. Conservar listado y detalle que muestren cuenta, monto, periodo, umbrales y destinatario. No modificar presupuestos ajenos ni crear duplicados sin revisar los existentes. [Procedimiento oficial Azure](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html).

**La alerta no detiene recursos.** La facturación puede tener retrasos. En una suscripción nueva de Azure, Cost Management puede tardar hasta 48 horas en estar disponible; si ocurre, se debe registrar el mensaje real y volver a verificar. No marcar la actividad como completada por tener solo un formulario preparado.

## 2. Estimaciones — A3

### Escenario y método

VM Linux de 2 vCPU/4 GB, 730 h/mes, SSD 30 GB; BD relacional administrada de 1–2 vCPU y 2–4 GB, 20 GB; objetos 50 GB y 100,000 solicitudes; un balanceador de aplicación; salida a Internet 100 GB/mes. Pago por uso, sin reservas ni compromisos. Valores en USD, sin impuestos. El total anual multiplica por 12 el mensual con la precisión interna de cada calculadora; no es una reserva ni una predicción de factura.

Solicitudes de objetos: 10,000 escrituras y 90,000 lecturas. AWS: t3.medium, EBS gp3; RDS PostgreSQL db.t3.small (2 vCPU/2 GiB), Single-AZ, gp2 20 GB; S3 Standard. Se excluyen RDS Proxy, Database Insights avanzado y Extended Support; se requiere una versión de PostgreSQL con soporte ordinario. Los créditos de CPU por uso sostenido de instancias burstable no se incluyen; deben medirse en un despliegue real.

ALB: 730 horas, 100 GB procesados al mes (100/730 GB/h), una conexión nueva/s, 60 s de duración, una solicitud/s y una evaluación de regla por solicitud. Estas son hipótesis adicionales para poder calcular capacidad; no son mediciones ni requisitos textuales de la práctica. La dimensión dominante resulta de 0.13698630137 LCU. El escenario de referencia no incluye dominio, NAT, soporte de pago ni IPv4 públicas. Si se despliega con IPv4 pública, debe añadirse su costo por hora; no usar este cálculo como precio total de una arquitectura pública productiva.

### Tabla 2A. AWS

| Recurso | Unidad de cobro | Cantidad | México USD/mes | EEUU USD/mes | ¿Capa gratuita? |
|---|---|---|---:|---:|---|
| EC2 + EBS | Instancia-hora + GB-mes | 730 h + 30 GB | 34.42 | 32.77 | No se supone cubierta; depende de plan/créditos |
| RDS PostgreSQL + disco | Instancia-hora + GB-mes | 730 h + 20 GB | 30.16 | 28.58 | No se supone cubierta |
| S3 + operaciones | GB-mes + solicitud | 50 GB + 100,000 | 1.30 | 1.24 | No se supone cubierta |
| ALB | Balanceador-hora + LCU-hora | 730 h + 100 LCU-h aprox. | 18.09 | 17.23 | No se supone cubierta |
| Salida bruta a Internet | GB | 100 | 9.00 | 9.00 | Franquicia general condicionada |
| **Total mensual bruto** | USD/mes | | **92.97** | **88.82** | Antes de créditos y franquicia |
| **Total anual bruto** | USD/año | 12 meses | **1,115.64** | **1,065.84** | Proyección aritmética |

[Estimación oficial EEUU y enlace de recuperación](../../evidencias/P01/costos/P01_A3_aws_eeuu.md). La calculadora incluye los USD 9 de salida dentro del componente EC2; aquí se separan sin duplicarlos. Según la [página oficial de EC2](https://aws.amazon.com/ec2/pricing/on-demand/), hay 100 GB mensuales de salida gratuita agregados entre servicios y regiones elegibles. Si toda esa franquicia está disponible, este escenario estadounidense queda en USD 79.82/mes (957.84/año), antes de otros créditos y costos omitidos. No asignar la franquicia completa varias veces a cargas que coexisten en la misma cuenta.

[Estimación oficial México](../../evidencias/P01/costos/P01_A3_aws_mexico.md). Diferencia bruta: USD 4.15/mes, equivalente a **4.67%** respecto a EEUU. El mayor incremento por renglón es EC2+EBS (USD 1.65), seguido de RDS (USD 1.58). Con los 100 GB gratuitos íntegros disponibles, México sería USD 83.97/mes y 1007.64/año; la diferencia relativa neta sería 5.20%.

### Comparación con salida neta bajo el mismo supuesto

Comparación aritmética de estimaciones históricas, sin actualizar tarifas: cada escenario se considera aislado y con la franquicia completa de 100 GB disponible. AWS resta USD 9 una sola vez; Azure ya muestra USD 0 por salida. No se descuentan créditos educativos.

| Región | AWS neto condicionado USD/mes | Azure USD/mes | Diferencia Azure menos AWS |
|---|---:|---:|---:|
| EEUU | 79.82 | 201.82 | 122.00 |
| México | 83.97 | 222.04 (provisional) | 138.07 (provisional) |

No implica igualdad de capacidad ni una factura real: Gateway y ALB difieren, los discos tienen mínimos distintos y faltan componentes como IPv4. La incidencia de Blob México sigue abierta. Si la franquicia ya se consume con otras cargas, hay que recalcular ambos proveedores. [Export oficial AWS EEUU](../../evidencias/P01/costos/P01_A3_aws_eeuu_oficial.json), recuperado el 15 de octubre con precios históricos del 1 de octubre.

### Tabla 2B. Azure: cálculo reconstruido el 1 de octubre

Se reconstruyeron ambos escenarios en la calculadora oficial. Se guardaron capturas y parámetros visibles; **no se recuperaron los XLSX oficiales**. El detalle, los archivos y la incidencia de Blob están en [la reconstrucción documentada](../../evidencias/P01/costos/P01_A3_azure_reconstruccion.md).

| Recurso | Unidad | Cantidad | México USD/mes | East US USD/mes | Capa gratuita |
|---|---|---|---:|---:|---|
| VM B2s + SSD E4 | VM-hora + disco-mes | 730 h + 32 GiB | 36.07 | 32.77 | Elegibilidad pendiente |
| PostgreSQL B1MS + SSD | Instancia-hora + almacenamiento | 730 h + 32 GiB | 17.70 | 16.09 | Elegibilidad pendiente |
| Blob Hot LRS | GB-mes + operaciones | 50 GB + 100,000 | 1.24 | 1.13 | Elegibilidad pendiente |
| Application Gateway Standard V2 | Gateway-hora + capacidad-hora | 730 h + 1 unidad dominante | 167.02 | 151.84 | No asumir gratuidad |
| Salida a Internet | GB | 100 GB en componente VM | 0.00 | 0.00 | Franquicia aplicada por calculadora |
| **Total mensual de calculadora** | USD/mes | | **222.04** | **201.82** | Sin créditos educativos |
| **Total anual de calculadora** | USD/año | | **2,664.43** | **2,421.89** | Calculado con precisión interna |

Los subtotales redondeados no siempre suman el total mostrado. Se conserva el total de calculadora: diferencia mensual USD 20.22, **10.02%** respecto a East US. El Gateway explica USD 15.18 del sobrecosto. La anualización de Azure usa importes internos sin redondear, por eso difiere unos centavos de multiplicar el total visible por 12.

El disco de 32 GiB responde a niveles o mínimos del servicio frente a los 30/20 GB pedidos. Blob conserva un campo descriptivo no editable de 1,000 GB Data Write: en East US se indica gratuidad por GB; en México Data Write y Data Retrieval señalan precio no disponible. **El total mexicano es provisional hasta resolver esos campos.** No interpretar ese dato como 1,000 GB adicionales de salida a Internet. AWS ALB y Azure Gateway tienen dimensiones de capacidad distintas; esta comparación no demuestra equivalencia de rendimiento.

### Estimación preliminar de EnlaceCorto

Hipótesis: 100 enlaces nuevos, 10,000 redirecciones/mes, 1 GB de datos, 1 GB de exportaciones y 1 GB de salida. Se cotizará el prototipo inicial por separado de Kubernetes final. Un GB lógico de datos no permite contratar menos del mínimo de almacenamiento del servicio. Se configuraron B1ms Ubuntu, PostgreSQL B1MS y Blob en East US: suma parcial USD 33.62/mes antes de IPv4 y otros extras. Falta completar IPv4, guardar el total y exportar. Ver [estimación preliminar e hipótesis detalladas](../../evidencias/P01/costos/P01_A3_proyecto_preliminar.md). No se afirma costo cero ni viabilidad dentro de USD 5.

**Recursos creados durante esta continuación: ninguno.** Esto no confirma que las cuentas carezcan de recursos anteriores.

## 3. Modelos de servicio y características NIST — B1 y B2

### Tabla 3. Investigación de servicios

La tabla clasifica servicios con documentación pública. Faltan las 14 capturas de identificación y la comprobación por región en consola. “Pendiente” no significa que un servicio sea inexistente; requiere verificar SKU, modalidad y permisos. Los siete renglones de cada proveedor son categorías de la práctica: FaaS y servicios administrados se relacionan con PaaS, y no constituyen siete modelos distintos en la taxonomía original de NIST.

| Proveedor y servicio | Modelo | Administra proveedor | Administra equipo | Unidad de cobro | Beneficio gratuito | México |
|---|---|---|---|---|---|---|
| [AWS EC2](https://aws.amazon.com/ec2/pricing/on-demand/) | IaaS | Hardware y virtualización | SO, parches, aplicación, red lógica, datos | Instancia-segundo/hora; GB-mes; GB salida | Depende de plan y tipo | Cotizable t3.medium; cuenta pendiente |
| [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) | PaaS | Aprovisionamiento, despliegue, plataforma | Código, datos, configuración | Recursos EC2/EKS, discos y balanceo subyacentes | Sin tarifa propia; recursos sí se cobran | No listado en endpoints mexicanos consultados |
| [AWS Lambda](https://aws.amazon.com/lambda/pricing/) | FaaS | Entorno de ejecución y escalado | Función, dependencias, permisos | Solicitudes + GB-segundo | 1 millón solicitudes y 400,000 GB-s/mes, según condiciones | Pendiente en cuenta |
| [Amazon EKS](https://aws.amazon.com/eks/pricing/) | Contenedores gestionados | Plano de control Kubernetes | Imágenes, manifiestos, nodos según modalidad | Clúster-hora + nodos/capacidad | No asumir plano de control gratuito | Pendiente |
| [RDS PostgreSQL](https://aws.amazon.com/rds/postgresql/) | BD gestionada | Motor, mantenimiento, respaldos configurados | Esquema, consultas, acceso, retención | Instancia-hora + GB-mes + extras | Depende de plan y clase | Cotizable en México; cuenta pendiente |
| [Amazon S3](https://aws.amazon.com/s3/) | Objetos | Infraestructura y durabilidad por clase | Objetos, permisos y ciclo de vida | GB-mes + solicitudes + salida | Depende de plan | Cotizable en México; cuenta pendiente |
| [Amazon Bedrock](https://aws.amazon.com/bedrock/pricing/) | IA gestionada | Infraestructura y servicio de modelos | Prompts, datos, modelo y controles | Tokens de entrada/salida; otras modalidades según modelo | No asumir cuota universal | Verificar modelo y ruta de inferencia |
| [Azure VM](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/) | IaaS | Hardware y virtualización | SO, aplicación y red lógica | VM-hora + discos + salida | Créditos/servicios elegibles; verificar cuenta | Pendiente SKU B2s |
| [Azure App Service](https://azure.microsoft.com/en-us/pricing/details/app-service/linux/) | PaaS | Plataforma y host | Aplicación, datos y plan | Instancia del plan por tiempo | Nivel Free limitado; no equivale a todos los planes | Pendiente plan y SO |
| [Azure Functions](https://azure.microsoft.com/en-us/pricing/details/functions/) | FaaS | Ejecución y escalado por plan | Función y dependencias | Ejecuciones + GB-s en Consumption | Depende de plan y suscripción | Pendiente modalidad |
| [Azure AKS](https://azure.microsoft.com/en-us/pricing/details/kubernetes-service/) | Contenedores gestionados | Plano de control | Cargas, manifiestos, nodos | Nivel de administración + VM/discos/red | Nivel Free de gestión no elimina nodos | Pendiente |
| [Azure PostgreSQL](https://azure.microsoft.com/en-us/pricing/details/postgresql/flexible-server/) | BD gestionada | Motor y mantenimiento | Datos, acceso y configuración | Cómputo-hora + almacenamiento + respaldos extra | Verificar elegibilidad B1ms | Pendiente |
| [Azure Blob Storage](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/) | Objetos | Servicio de almacenamiento | Objetos, permisos y nivel | GB-mes + operaciones + transferencia | Depende de oferta | Pendiente redundancia y nivel |
| Azure AI Foundry / Azure OpenAI | IA gestionada | Servicio de inferencia y modelos | Prompts, datos, despliegue y acceso | Tokens o capacidad aprovisionada | No asumir gratuidad | Pendiente modelo/tipo de despliegue |

La [tabla oficial de endpoints de Beanstalk](https://docs.aws.amazon.com/general/latest/gr/elasticbeanstalk.html) consultada no incluye `mx-central-1`. No sustituir una región por otra sin registrarlo. En IA, disponer de acceso al catálogo no garantiza que la inferencia ocurra en México: revisar [regiones/modelos de Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) y disponibilidad de Azure por producto.

**SaaS: GitHub.** Se consume la aplicación de colaboración, sin administrar su infraestructura. Los planes comerciales se expresan por usuario/mes; el plan Free no convierte todas las funciones en gratuitas. Su facturación se consulta en GitHub, independientemente de la consola AWS/Azure del usuario. [Precios oficiales](https://github.com/pricing). Captura pendiente.

### NIST: explicación y evidencia que falta

| Característica | Justificación | Captura necesaria | Estado |
|---|---|---|---|
| Autoservicio bajo demanda | Un usuario autorizado solicita capacidad mediante un asistente o API. El aprovisionamiento ordinario no requiere intervención humana del proveedor. | Asistente de VM listo para crear; cancelar antes de confirmar | Pendiente |
| Amplio acceso a la red | El mismo servicio puede usarse por interfaces de red desde distintos clientes. La identidad consultada en Cloud Shell debe corresponder a la cuenta del portal. | `aws sts get-caller-identity` o `az account show`, sin secretos | Pendiente |
| Agrupación de recursos | El proveedor asigna capacidad de un conjunto compartido a múltiples clientes. Regiones, zonas y familias ilustran opciones de ubicación/capacidad, aunque no prueban por sí solas la implementación física. | Selector regional y familias compartidas | Pendiente |
| Elasticidad rápida | La capacidad puede ajustarse con la demanda. Ver un menú de tamaños acredita opciones; demostrar escalado automático requeriría una prueba adicional. | Selector de tamaños o configuración de autoescalado sin crear recursos | Pendiente |
| Servicio medido | El proveedor registra consumo por unidades y lo presenta al usuario. La factura y el presupuesto permiten observar y gestionar ese consumo. | Uso por servicio y presupuesto de la misma cuenta | Pendiente |

Marco: [NIST SP 800-145](https://doi.org/10.6028/NIST.SP.800-145). Las explicaciones anteriores son conceptuales y no sustituyen las cinco evidencias.

## 4. Preguntas de análisis

### 1. ¿Cuenta compartida o cuentas individuales?

Para la práctica corresponden cuentas personales y alertas por integrante. Para un despliegue común conviene un ámbito de proyecto con titular responsable y accesos individuales con permisos mínimos: centraliza el gasto y evita duplicar entornos. Compartir una contraseña impide atribuir cambios, dificulta retirar accesos y expone toda la cuenta. Separar cuentas mejora aislamiento, pero dispersa presupuestos e inventarios. Aún no se ha configurado acceso colaborativo; la elección final depende de las ofertas educativas y de quién asuma la facturación. No juntar cuentas solo para acumular créditos: la [FAQ de AWS](https://aws.amazon.com/free/free-tier-faqs/) establece restricciones para transferirlos y para ciertos cambios de plan.

### 2. Diferencia México/EEUU y residencia de datos

La reconstrucción Azure muestra un sobrecosto mexicano provisional de 10.02% y un sobrecosto de Gateway de USD 15.18/mes. AWS ya tiene dos estimaciones oficiales guardadas: México USD 92.97 y EEUU USD 88.82 (4.67% más en México). Azure queda pendiente de exportar y de resolver los campos de Blob sin tarifa. Los totales AWS son brutos de salida; Azure aplica su franquicia, por lo que una comparación entre proveedores debe usar supuestos netos homogéneos. Elegiríamos México cuando una medición de latencia desde los usuarios o una obligación contractual de residencia lo justifique. La ubicación mexicana por sí sola no demuestra cumplimiento de la LFPDPPP: deben revisarse finalidades, aviso de privacidad, seguridad y transferencias aplicables. Para el prototipo se proponen conteos agregados y evitar IPs persistentes. La decisión jurídica debe basarse en el tratamiento concreto y en la [ley vigente, en particular sus reglas sobre transferencias](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf).

### 3. ¿Qué sigue cobrando con la VM detenida?

Siguen existiendo discos y snapshots (GB-mes), objetos (GB-mes y solicitudes), la BD administrada que continúe ejecutándose (instancia-hora más almacenamiento), balanceador (hora y capacidad) e IPv4 públicas reservadas/uso aplicable (IP-hora). NAT, si se incorpora, añade hora y procesamiento. La salida se factura por los GB que realmente se transfieran; no es una cuota inevitable por apagar la VM. En Azure hay que distinguir “detenida” de “desasignada”: apagar desde el SO puede conservar el cobro del cómputo. En nuestra estimación AWS EEUU, mantener RDS, S3 y ALB suma USD 47.05/mes, más USD 2.40 de EBS, aun sin utilizar EC2; no incluye tráfico ni IPv4 adicional. [EC2](https://aws.amazon.com/ec2/pricing/on-demand/), [VM Linux Azure](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/).

### 4. Modelo de cómputo para EnlaceCorto

Se propone contenedores para el proyecto final porque el alcance guardado exige separar enlaces y estadísticas y evolucionar a Kubernetes. El equipo administrará imágenes, API y manifiestos; con AKS administrado el proveedor opera el plano de control y el costo principal sigue incluyendo VM-hora de nodos, discos y red. Para el prototipo inicial, una VM con contenedores simplifica las pruebas antes de pagar un clúster. Serverless sería atractivo por las 10,000 redirecciones mensuales supuestas, pero no reemplaza por sí solo la demostración de Kubernetes. Es una elección de diseño pendiente de verificación en consola, no un despliegue realizado. [Tarifas AKS](https://azure.microsoft.com/en-us/pricing/details/kubernetes-service/).

### 5. ¿Cómo contener gasto automáticamente?

AWS Budgets permite asociar acciones a umbrales, como detener EC2 o RDS compatibles mediante un rol con permisos suficientes. Proponemos probar primero un presupuesto de laboratorio con umbral conservador, destinatario confirmado y acción sobre identificadores explícitos del proyecto; después verificar la detención y los costos residuales de discos, respaldos y red. Debe preverse el retraso de la medición y que otros recursos sigan cobrando. No es un límite transaccional exacto de USD 5, ni está configurado aún. En Azure for Students conviene conservar el límite de gasto de la oferta, que depende del crédito y no de un monto mensual personalizado. [Acciones AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html), [límite Azure](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit).

### 6. Dependencia de las capas gratuitas

Una oferta puede cambiar en capacidad, elegibilidad y vigencia; la continuidad debe planearse con el costo bruto y no solo con el descuento. AWS documenta que el plan gratuito termina al cumplirse seis meses o agotar créditos; el vencimiento de los créditos es un concepto distinto, verificable en Billing. Para EnlaceCorto proponemos revisar el saldo semanalmente, anotar el vencimiento real, conservar respaldos exportables de PostgreSQL e imágenes portables y probar restauración local antes de las exposiciones. Si los créditos no cubren el semestre, se debe reducir el tiempo encendido y acordar proveedor alternativo o presupuesto antes de migrar. Las afirmaciones de la práctica sobre cambios de Oracle deben contrastarse con sus [límites actuales](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm); no se atribuye una cuenta OCI al equipo. [FAQ AWS](https://aws.amazon.com/free/free-tier-faqs/).

## 5. Seguridad, costos e inventario — B3

- [ ] Inventario real de cada cuenta y regiones requeridas, con recursos existentes justificados.
- [ ] Gasto del mes, créditos y vencimiento consultados y capturados.
- [ ] Presupuestos activos con ámbito, monto, umbrales y correo correctos.
- [ ] Capturas históricas auténticas de septiembre, si existen; ausencia declarada en otro caso.
- [x] Revisión de las cuatro capturas de calculadora guardadas; no muestran credenciales ni tarjetas. Faltan las capturas de cuentas.
- [x] Verificación de texto y enlaces ejecutada sin incidencias; volver a ejecutar al incorporar evidencias nuevas.
- [x] Publicación y GitHub Actions verificados en verde el 2 de octubre de 2026: [ejecución comprobada](https://github.com/Radioiza/Sistemas-Distribuidos-27-1/actions/runs/37101184322).
- [ ] Commits auténticos de los tres integrantes.

No se ejecutarán acciones de limpieza destructivas sobre recursos preexistentes sin identificar propietario, función y consecuencias. La ausencia de despliegues durante esta sesión no acredita inventario cero.

## 6. Conclusiones

El escenario mínimo incluye costos persistentes más allá de la VM. La estimación AWS EEUU de USD 88.82/mes rebasa ampliamente el umbral de alerta de USD 5; se elaboró únicamente en la calculadora. Las ofertas educativas pueden reducir la factura temporalmente, pero requieren verificar cuenta, saldo, elegibilidad y vencimiento. La práctica no puede considerarse completa hasta que los tres integrantes acrediten sus presupuestos y se integren los cálculos y capturas faltantes.

## 7. Uso de IA y contribuciones

Codex apoyó la lectura de requisitos, navegación de calculadoras, consulta de fuentes oficiales, redacción y revisión de archivos. Los integrantes deben revisar y poder explicar cifras, decisiones y evidencias. No se generaron capturas ficticias ni se retrofecharon actividades.

| Integrante | Contribución comprobable en esta continuación | Pendiente individual |
|---|---|---|
| Brian Ricardo | Proporcionó el espacio de trabajo y confirmó acceso a cuentas; trabajo documental asistido en su sesión | Completar/verificar cuentas, presupuestos y revisión de entrega |
| Juan Carlos | Nombre y proyecto registrados en contexto previo; sin nueva actividad verificada | Evidencias propias y commit |
| Julissa Ischel | Integrante confirmada; sin nueva actividad verificada | Evidencias propias y commit |

## 8. Referencias y trazabilidad

Fuente principal: `Practica1_ConsolasCostosAlertas_SD_2026.pdf`, proporcionado en la carpeta P1, páginas 4–11 para actividades y entregables. La convocatoria original del proyecto no está disponible en este equipo; el alcance se conserva desde la propuesta y el contexto anterior. Fuentes web enlazadas junto a cada afirmación, consultadas el 1 de octubre de 2026. Las páginas de precios no acreditan condiciones de una cuenta concreta.

- [Calculadora AWS](https://calculator.aws/).
- [Calculadora Azure](https://azure.microsoft.com/en-us/pricing/calculator/).
- [Productos Azure por región](https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/).
- [Bitácora de esta continuación](../../bitacora/2026-10-01.md).


