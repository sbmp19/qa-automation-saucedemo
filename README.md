# 🧪 SauceDemo — Testing Automatizado con Playwright + Python

[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/TU_USUARIO/TU_REPO/actions)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![Playwright](https://img.shields.io/badge/Playwright-1.60-45ba4b?logo=playwright&logoColor=white)](https://playwright.dev/python)
[![pytest](https://img.shields.io/badge/pytest-8.4-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org)
[![Chromium](https://img.shields.io/badge/Chromium-148-4285F4?logo=googlechrome&logoColor=white)](https://www.chromium.org)

---

## 📌 Descripción

Suite de **tests funcionales automatizados** para [SauceDemo](https://www.saucedemo.com), un sitio e-commerce de práctica diseñado para entrenar habilidades de testing.

El proyecto cubre escenarios reales de un flujo de compra online:

- Login exitoso y fallido (distintos tipos de usuario)
- Agregar y quitar productos del carrito
- Checkout completo con confirmación de orden
- Validación de mensajes de error y navegación
- Ordenamiento de productos por precio
- Validación de campos obligatorios en checkout

> Proyecto creado con fines de portafolio para demostrar habilidades en **QA Automation**, **Playwright** y **Python**.

---

## 📋 Tests incluidos

| # | Archivo | Test | Escenario | Verificación |
|---|---------|------|-----------|-------------|
| 1 | `test_saucedemo.py` | `test_login[standard_user-exito]` | Login correcto con `standard_user` | Redirige a `/inventory.html` |
| 2 | `test_saucedemo.py` | `test_login[locked_out_user-bloqueado]` | Login con `locked_out_user` | Muestra error de usuario bloqueado |
| 3 | `test_saucedemo.py` | `test_login[performance_glitch_user-exito]` | Login correcto con `performance_glitch_user` (usuario lento) | Redirige a `/inventory.html` |
| 4 | `test_saucedemo.py` | `test_login_contrasena_incorrecta` | Login con contraseña errónea | Muestra error `"Username and password do not match"` |
| 5 | `test_saucedemo.py` | `test_agregar_producto_al_carrito` | Login → agregar producto al carrito | Badge del carrito muestra `1` |
| 6 | `test_saucedemo.py` | `test_compra_completa` | Login → agregar producto → checkout completo → confirmar | Muestra `"Thank you for your order"` |
| 7 | `test_ordenamiento.py` | `test_ordenar_precio_menor_a_mayor` | Ordenar productos por precio ascendente | Todos los precios están ordenados de menor a mayor |
| 8 | `test_ordenamiento.py` | `test_ordenar_precio_mayor_a_menor` | Ordenar productos por precio descendente | Todos los precios están ordenados de mayor a menor |
| 9 | `test_checkout_validacion.py` | `test_nombre_vacio` | Checkout con nombre vacío | Muestra error `"First Name is required"` |
| 10 | `test_checkout_validacion.py` | `test_apellido_vacio` | Checkout con apellido vacío | Muestra error `"Last Name is required"` |
| 11 | `test_checkout_validacion.py` | `test_codigo_postal_vacio` | Checkout con código postal vacío | Muestra error `"Postal Code is required"` |
| 12 | `test_carrito.py` | `test_agregar_tres_y_quitar_uno` | Agregar 3 productos, quitar 1 desde el carrito | Badge pasa de `3` a `2` |

> Los tests 1-3 usan `@pytest.mark.parametrize`: un mismo test ejecutado con 3 combinaciones distintas de datos.

---

## 🛠️ Tecnologías

| Herramienta | Propósito |
|-------------|-----------|
| **Python 3.9+** | Lenguaje de programación |
| **Playwright** | Automatización de navegador Chromium |
| **pytest** | Framework de testing y ejecutor |
| **pytest-html** | Generación de reportes HTML autocontenidos |
| **Chromium** | Navegador headless / headless-shell |
| **GitHub Actions** | Integración continua (CI) |

---

## 📁 Estructura del proyecto

```
.
├── .github/
│   └── workflows/
│       └── ci.yml                # Workflow de CI (push a main)
├── pages/                        # Page Object Model
│   ├── base_page.py              # Clase base con método texto_error()
│   ├── login_page.py             # LoginPage: selectores y acciones de login
│   ├── inventory_page.py         # InventoryPage: ordenamiento, carrito, precios
│   ├── cart_page.py              # CartPage: remover productos, ir a checkout
│   └── checkout_page.py          # CheckoutPage: formulario y confirmación
├── tests/
│   ├── conftest.py               # Fixture del navegador + screenshot en fallos
│   ├── test_saucedemo.py         # Tests de login, carrito y compra completa
│   ├── test_ordenamiento.py      # Tests de ordenamiento por precio
│   ├── test_checkout_validacion.py  # Tests de validación de checkout
│   └── test_carrito.py           # Tests de gestión del carrito
├── reports/                      # Reporte HTML generado (ignorado por git)
├── pytest.ini                    # Configuración por defecto de pytest
├── requirements.txt              # Dependencias del proyecto
├── run_tests.sh                  # Script para correr tests y abrir reporte
├── .gitignore
└── README.md
```

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO
```

### 2. Crear el entorno virtual e instalar dependencias

```bash
python3 -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Instalar el navegador

```bash
playwright install chromium
```

### 4. Ejecutar todos los tests

```bash
pytest -v
```

Esto genera automáticamente el reporte en `reports/report.html`.

### 5. (Opcional) Ver el reporte HTML

```bash
open reports/report.html        # macOS
# xdg-open reports/report.html  # Linux
# start reports/report.html     # Windows
```

O usar el script incluido:

```bash
./run_tests.sh
```

### Comandos útiles

```bash
# Ejecutar un test específico
pytest tests/test_saucedemo.py::test_compra_completa -v

# Ejecutar solo los tests parametrizados de login
pytest -k "test_login" -v

# Generar reporte con nombre personalizado
pytest --html=reporte.html --self-contained-html
```

---

## 🤖 Integración continua (CI)

El workflow de GitHub Actions (`.github/workflows/ci.yml`) ejecuta automáticamente todos los tests en cada `push` a la rama `main`:

1. Instala Python 3.11 y las dependencias
2. Descarga Chromium
3. Corre los tests en modo **headless**
4. Sube el reporte HTML como **artefacto descargable**

Para descargar el reporte desde GitHub: entrar al workflow run → sección **Artifacts** → `reporte-test`.

---

## ✅ Salida esperada

```
$ pytest -v

tests/test_carrito.py::TestCarrito::test_agregar_tres_y_quitar_uno             PASSED
tests/test_checkout_validacion.py::TestCheckoutValidacion::test_nombre_vacio   PASSED
tests/test_checkout_validacion.py::TestCheckoutValidacion::test_apellido_vacio PASSED
tests/test_checkout_validacion.py::TestCheckoutValidacion::test_codigo_postal_vacio PASSED
tests/test_ordenamiento.py::TestOrdenamiento::test_ordenar_precio_menor_a_mayor PASSED
tests/test_ordenamiento.py::TestOrdenamiento::test_ordenar_precio_mayor_a_menor PASSED
tests/test_saucedemo.py::test_login[standard_user-exito]                      PASSED
tests/test_saucedemo.py::test_login[locked_out_user-bloqueado]                PASSED
tests/test_saucedemo.py::test_login[performance_glitch_user-exito]            PASSED
tests/test_saucedemo.py::test_login_contrasena_incorrecta                     PASSED
tests/test_saucedemo.py::test_agregar_producto_al_carrito                     PASSED
tests/test_saucedemo.py::test_compra_completa                                 PASSED

============================== 12 passed in 19.45s ==============================
```

---

## 📸 Captura de pantalla en fallos

Si un test falla, el hook en `conftest.py` toma una captura de pantalla automática y la incrusta en el reporte HTML, permitiendo ver el estado exacto de la página al momento del error.

---

## 📄 Sobre este proyecto

Este proyecto fue creado como parte de mi portafolio de **QA Automation**. El objetivo es demostrar habilidades en:

- Automatización de pruebas end-to-end con **Playwright** y **Python**
- Diseño de tests **data-driven** con `@pytest.mark.parametrize`
- Patrón **Page Object Model (POM)** para mantener tests mantenibles y reutilizables
- Configuración de **CI/CD** con GitHub Actions
- Generación de reportes visuales con **pytest-html**
- Buenas prácticas: fixtures, hooks, page objects, y organización de proyecto

---

<p align="center">
  Hecho con ❤️ para la comunidad de QA <br>
  <a href="https://www.saucedemo.com">SauceDemo</a> ·
  <a href="https://playwright.dev/python">Playwright Python</a> ·
  <a href="https://docs.pytest.org">pytest</a>
</p>
