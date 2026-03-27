# 🧪 Sauce Demo - Automation Framework

Framework de automatización de pruebas E2E para [Sauce Demo](https://www.saucedemo.com) usando **Playwright** con **Python** y **Pytest**.

## Estructura del proyecto

```
├── config/                 # Configuración por ambiente (dev, qa, prod)
│   ├── base_config.py
│   ├── dev_config.py
│   ├── qa_config.py
│   └── prod_config.py
├── data/                   # Datos de prueba
│   └── login_data.py
├── pages/                  # Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/                  # Tests
│   ├── test_login.py
│   └── test_homepage.py
├── utils/                  # Utilidades
│   └── logger.py
├── logs/                   # Logs generados
├── conftest.py             # Fixtures de Pytest
├── pytest.ini              # Configuración de Pytest
└── requirements.txt
```

## Requisitos previos

- Python 3.8+
- pip

## Instalación

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Instalar navegadores de Playwright
playwright install
```

## Ejecución de tests

```bash
# Ejecutar todos los tests
pytest

# Ejecutar por archivo
pytest tests/test_login.py

# Ejecutar por markers
pytest -m smoke
pytest -m regression

# Ejecutar con más detalle
pytest -v
```

## Ambientes

El framework soporta múltiples ambientes mediante la variable de entorno `ENV`:

| Ambiente | Comando | URL |
|----------|---------|-----|
| Dev      | `ENV=dev pytest`  | `https://dev.saucedemo.com` |
| QA       | `ENV=qa pytest`   | `https://qa.saucedemo.com` |
| Prod     | `ENV=prod pytest` (default) | `https://www.saucedemo.com` |

## Navegadores

Por defecto se usa Chromium. El navegador se configura en `config/base_config.py`:

- `chromium`
- `firefox`
- `webkit`

## Markers

| Marker       | Descripción |
|--------------|-------------|
| `smoke`      | Tests críticos rápidos |
| `regression` | Suite completa de tests |

## Logs

Los logs se generan automáticamente en `logs/test.log` y también se muestran en consola durante la ejecución.
