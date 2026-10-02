# EnlaceCorto: estimación preliminar en curso

Calculadora utilizada: [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/), 1 de octubre de 2026. **No es un total final ni un export oficial.** La conexión con el navegador falló antes de guardar y verificar el escenario completo.

## Hipótesis del prototipo

- 100 enlaces nuevos y 10,000 redirecciones mensuales.
- 1 GB lógico de base de datos; se cotiza el mínimo físico de 32 GiB en PostgreSQL.
- 1 GB de archivos de exportación; hipótesis adicional de 100 escrituras y 100 lecturas de objetos al mes. Las redirecciones consultan PostgreSQL, no Blob.
- 1 GB de salida mensual, sin otros consumos concurrentes de franquicia.
- VM Ubuntu B1ms (1 vCPU, 2 GB) 730 h/mes, SSD E4 de 32 GiB para contenedores del prototipo. PostgreSQL administrado B1MS. Región East US.
- Proxy HTTP y servicios de enlaces/estadísticas en la VM durante el prototipo; cola local persistida en disco. Se requiere validar memoria y capacidad con pruebas. No se presenta como arquitectura de alta disponibilidad ni como Kubernetes final.

## Valores observados antes de interrumpirse

| Recurso | Importe mostrado USD/mes | Estado |
|---|---:|---|
| B1ms + SSD E4 + 1 GB salida | 17.51 | Observado en calculadora |
| PostgreSQL B1MS + 32 GiB | 16.09 | Observado en calculadora |
| Blob 1 GB + 100 PUT + 100 GET | 0.02 | Observado; campos de operaciones 0.01 × 10,000 |
| Dirección IPv4 pública | Pendiente | Se pulsó añadir IP Addresses; falta configurar y verificar |
| **Suma parcial de valores redondeados** | **33.62** | **No incluye IPv4 ni extras** |

La calculadora resumía las operaciones fraccionarias como `0 × 10,000`, aunque los controles visibles conservaban `0.01`; revisar el export al recuperarlo. También conservaba el campo no editable Data Write de 1,000 GB descrito en la reconstrucción de Azure. Ninguna cifra representa uso medido ni un cargo real.

## Para completar

1. Verificar persistencia de esta estimación en la calculadora; si se perdió, reconstruir los tres componentes con estos parámetros.
2. Añadir una IPv4 pública Standard estática de 730 h y registrar el subtotal. No crear la dirección en una cuenta real.
3. Revisar cuotas, elegibilidad y créditos de Azure for Students. La suma parcial supera USD 5, por lo que no debe confundirse presupuesto de alertas con capacidad financiada.
4. Guardar/exportar la estimación completa y capturar parámetros y total.
5. Cotizar Kubernetes, réplicas y observabilidad por separado para el proyecto final. Esos costos no están cubiertos por esta tabla.
