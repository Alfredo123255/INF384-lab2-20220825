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
| `SONAR_TOKEN` | Settings -> Secrets and variables -> Actions -> **Secrets** |
| `SONAR_ORGANIZATION` | Settings -> Secrets and variables -> Actions -> **Variables** |
| Project key | Constante `INF384-lab2` en `.github/workflows/pipeline.yml` |

El proyecto en SonarQube Cloud debe crearse con la project key exacta
`INF384-lab2`. No hay que editar ningun archivo del repositorio para
configurar el analisis.

## Version

La version vigente esta en `VERSION` y en `pyproject.toml`.
