# EnlaceCorto: acortador de URLs con estadísticas

**Tema 3 de la convocatoria del proyecto integrador.** Sistemas Distribuidos, 7CV1, semestre 27/1. Propuesta elaborada el 1 de octubre de 2026; pendiente de registro y validación docente.

## Equipo

- Escalona Zuñiga Juan Carlos.
- Henáro Sánchez Julissa Ischel.
- Bernal Ramírez Brian Ricardo.

## Problema y usuarios

Los estudiantes y docentes comparten enlaces extensos a materiales y actividades. Una dirección corta facilita su distribución; un conteo agregado de visitas permite conocer si el material se consulta. EnlaceCorto ofrecerá esas dos funciones en una aplicación pequeña cuyo comportamiento distribuido pueda medirse y demostrarse durante el curso.

Los administradores del prototipo crearán y consultarán sus enlaces desde un panel protegido. Los visitantes utilizarán las direcciones cortas para llegar al destino sin necesidad de una cuenta. Las estadísticas iniciales mostrarán conteos agregados, sin perfiles de visitantes.

## Alcance mínimo

El usuario administrador introducirá una URL HTTP/HTTPS válida y recibirá un código único. Al visitar ese código, el sistema buscará el destino y responderá con una redirección; un código inexistente producirá un error 404. El panel mostrará la URL original, el enlace corto, las visitas totales y las visitas por día. Permitirá desactivar enlaces. El prototipo no incluirá pagos, dominios personalizados, vista previa de sitios ni campañas de mercadotecnia.

La API expondrá operaciones de creación, consulta y desactivación de enlaces, redirección y consulta de estadísticas. Se documentará con OpenAPI. La validación de destinos aceptará exclusivamente los esquemas HTTP y HTTPS y no descargará automáticamente las páginas de destino. El panel requerirá autenticación y las escrituras tendrán límites de solicitudes.

## Arquitectura prevista y evolución

Un servicio de enlaces atenderá la administración y redirección, y otro procesará estadísticas. PostgreSQL almacenará los datos con responsabilidades separadas por servicio. Los eventos de visita se entregarán de forma asíncrona para que un fallo en las estadísticas no impida redirigir; sus identificadores permitirán evitar conteos duplicados al reintentar. La selección de la cola y del proveedor se justificará con disponibilidad, costos y acceso educativo comprobados.

La primera versión priorizará el flujo completo y las pruebas locales. En las fases siguientes se incorporarán réplicas, balanceo, autoescalado y contenedores. La demostración final se desplegará sobre Kubernetes e incluirá métricas de solicitudes, errores y latencia, junto con una prueba de carga o recuperación. Los datos persistentes sobrevivirán al reinicio de un contenedor.

## Criterios iniciales de evaluación

Como objetivos propuestos para las pruebas: al menos 99% de redirecciones correctas para códigos activos durante una ventana de prueba definida, latencia p95 menor de 500 ms con 20 solicitudes por segundo y actualización de estadísticas en menos de 60 segundos bajo esa carga. Son metas pendientes de validar; no representan resultados medidos ni un SLA comercial.

La estimación preliminar considerará 100 enlaces nuevos y 10,000 redirecciones al mes, 1 GB de datos, 1 GB de archivos de exportación y 1 GB de salida. Se cotizará la infraestructura real, incluidos tamaños mínimos y horas de cómputo, con presupuesto y alertas configurados antes de desplegar. La Práctica 1 conservará además su escenario de referencia obligatorio, que es distinto de esta carga propuesta.

## Reproducibilidad y contribuciones

El repositorio incluirá instrucciones de ejecución y despliegue, configuración de ejemplo sin secretos, diagramas por fase, evidencias, costos, bitácora y declaración de uso de IA. Cada integrante deberá realizar y poder explicar sus contribuciones, con commits propios. La distribución de responsabilidades está pendiente de acuerdo del equipo; no se atribuye trabajo realizado a ninguno de sus integrantes en esta propuesta.

## Uso de IA

Codex ayudó a comparar la complejidad de las opciones y redactar esta propuesta. El equipo deberá revisar el alcance, comprender las decisiones y registrar sus cambios y resultados reales.

Fuente de requisitos: `SD_7CV1_Proyecto_Integrador.pdf`, convocatoria proporcionada por el usuario. Este archivo es una propuesta; no acredita registro, implementación, despliegue ni cumplimiento de hitos anteriores.
