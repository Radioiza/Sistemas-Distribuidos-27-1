# Azure: reconstrucción del escenario de referencia

Consulta real en la [calculadora oficial Azure](https://azure.microsoft.com/en-us/pricing/calculator/) el 1 de octubre de 2026. Se conservaron capturas y una transcripción de los controles visibles. **No se recuperó un XLSX descargado**: pulsar Export no confirmó un archivo local y guardar/compartir requería iniciar sesión. Estos archivos son observaciones de la calculadora, no exports oficiales fabricados.

| Componente | México USD/mes | East US USD/mes |
|---|---:|---:|
| VM B2s Linux Ubuntu, 730 h, un disco E4 SSD LRS 32 GiB | 36.07 | 32.77 |
| PostgreSQL Flexible, B1MS, 730 h, Premium SSD 32 GiB | 17.70 | 16.09 |
| Blob Standard GPv2, Flat Namespace, Hot LRS, 50 GB | 1.24 | 1.13 |
| Application Gateway Standard V2, 730 h | 167.02 | 151.84 |
| **Total mensual mostrado por calculadora** | **222.04** | **201.82** |
| **Total anual mostrado por calculadora** | **2,664.43** | **2,421.89** |

Los subtotales redondeados suman 222.03 y 201.83; el total oficial usa mayor precisión interna. No sustituirlo por la suma redondeada. Diferencia entre los totales mensuales mostrados: USD 20.22, **10.02%** respecto a East US. El Gateway aporta USD 15.18 de diferencia.

## Parámetros adicionales

- VM: pago por uso; sin snapshots ni cifrado confidencial adicional; monitoreo extra no añadido. Disco 32 GiB por nivel disponible frente a 30 GB. Transacciones de disco no modeladas; se necesitaría una carga medida para cuantificarlas.
- Salida de VM: Internet Egress, 100 GB, vía Microsoft Global Network, misma región que cómputo. La calculadora muestra USD 0 aplicando la franquicia que anuncia; no repetirla en Gateway.
- PostgreSQL: 1 B1MS, 1 vCore, nivel Burstable, 32 GiB por mínimo de servicio, 0 GiB de respaldo adicional, LRS, sin Extended Support. La selección se propone sin HA; no se configuró una cuenta ni un servidor real.
- Blob: 1 × 10,000 escrituras; 0 listados/creación de contenedores; 9 × 10,000 lecturas; 0 otras operaciones. Data Retrieval ajustado a 100 GB antes de cambiar de región. SFTP y replicación de objetos desactivados.
- **Incidencia de Blob:** el resumen conserva `1,000 GB Data Write`, pero East US no ofrece un control editable para esa cantidad y señala escritura por GB gratuita. En México, Data Retrieval y Data Write muestran “Pricing is not available for your selection in this region”. No significa transferencia de salida de 1,000 GB y no permite concluir por sí solo que ambos conceptos son gratuitos allí. Resolver con tarifas oficiales o soporte antes de cerrar la estimación mexicana.
- Gateway: 730 horas fijas; 1 unidad de cómputo; 1,000 conexiones persistentes; 1 mb/s; salida 0 para evitar duplicar los 100 GB de VM. La unidad de capacidad Azure y la LCU de AWS son diferentes; comparar funciones similares no implica equivalencia de rendimiento.
- Support Basic incluido, Microsoft Customer Agreement, USD, sin Dev/Test. No se aplicaron créditos educativos.

## Archivos que respaldan los valores

- [East US, captura original](P01_A3_azure_equipo_eeuu_original.jpg).
- [East US, controles visibles transcritos](P01_A3_azure_eeuu_observacion.txt).
- [México, captura original](P01_A3_azure_equipo_mexico_original.jpg).
- [México, controles visibles transcritos](P01_A3_azure_mexico_observacion.txt).

No se desplegó esta infraestructura. El costo excluye impuestos, dominio, IPv4 adicional, NAT, carga de logs, transacciones de disco y otros servicios no añadidos.
