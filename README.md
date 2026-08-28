# despachos

Modulo de consolidacion de despachos. Calcula tarifas de envio, valida datos de
entrada y administra el ciclo de vida de un pedido.

## Estructura

```
src/despachos/          Codigo fuente
  pedidos.py            Modelo de pedido y transiciones de estado
  tarifas.py            Calculo de tarifas de despacho
  validaciones.py       Validaciones de formato de entrada
tests/                  Pruebas unitarias
docs/                   Documentacion y entregables
.github/workflows/      Definicion del pipeline
```

## Ejecutar en local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --cov=src --cov-report=term
```

## Pipeline

El pipeline esta definido en `.github/workflows/pipeline.yml` y tiene dos
trabajos:

- `validar`: instala dependencias, ejecuta las pruebas con reporte de cobertura
  y envia el resultado al servicio de analisis de calidad.
- `publicar`: construye el paquete distribuible y lo publica como artefacto de
  la ejecucion.

Se puede ejecutar manualmente desde la pestana **Actions**, con **Run workflow**.

## Configuracion requerida

| Elemento | Donde se configura |
|---|---|
| `SONAR_TOKEN` | Settings -> Secrets and variables -> Actions |
| `sonar.organization` | `sonar-project.properties` |
| `sonar.projectKey` | `sonar-project.properties` |

## Version

La version vigente esta en `VERSION` y en `pyproject.toml`.
