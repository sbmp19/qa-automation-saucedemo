# 🧪 Testing automatizado — SauceDemo con Playwright

Suite de **tests automatizados** para [SauceDemo](https://www.saucedemo.com), un sitio de práctica de comercio electrónico.  
Los tests cubren flujos críticos de login, carrito de compras y checkout. Ideal para mostrar en un portafolio de **QA Automation** o **Testing con Python**.

---

## 📋 Tests incluidos

| # | Test | Descripción |
|---|------|-------------|
| 1 | `test_agregar_producto_al_carrito` | Login con `standard_user`, agrega el primer producto al carrito y verifica que el badge muestre `1` |
| 2 | `test_login_contrasena_incorrecta` | Login con `standard_user` y contraseña errónea; verifica el mensaje de error `"Username and password do not match"` |
| 3 | `test_login_usuario_bloqueado` | Login con `locked_out_user`; verifica que aparezca el error de usuario bloqueado |
| 4 | `test_compra_completa` | Login, agrega producto, completa checkout con datos ficticios y confirma la compra; verifica el mensaje `"Thank you for your order"` |

---

## 🛠️ Tecnologías

| Herramienta | Versión |
|-------------|---------|
| **Python** | 3.9+ |
| **Playwright** | 1.60 |
| **pytest** | 8.4 |
| **Chromium** | headless / headless-shell |

---

## 🚀 Cómo ejecutar los tests

```bash
# 1. Crear el entorno virtual
python3 -m venv .venv

# 2. Instalar dependencias
.venv/bin/pip install -r requirements.txt

# 3. Instalar el navegador Chromium
.venv/bin/playwright install chromium

# 4. Ejecutar todos los tests
.venv/bin/pytest tests/ -v
```

### Ejecutar un test específico

```bash
.venv/bin/pytest tests/test_saucedemo.py::test_compra_completa -v
```

### Modo visual (con navegador visible)

Los tests abren el navegador por defecto (`headless=False`). Si preferís que se ejecuten en segundo plano, editá la fixture `pagina` en `tests/test_saucedemo.py` cambiando `headless=False` por `headless=True`.

---

## 📁 Estructura del proyecto

```
.
├── requirements.txt           # Dependencias
├── .gitignore
├── README.md
└── tests/
    └── test_saucedemo.py      # Los 4 tests
```

---

## ✅ Ejemplo de salida

```
$ .venv/bin/pytest tests/ -v

tests/test_saucedemo.py::test_agregar_producto_al_carrito PASSED
tests/test_saucedemo.py::test_login_contrasena_incorrecta PASSED
tests/test_saucedemo.py::test_login_usuario_bloqueado PASSED
tests/test_saucedemo.py::test_compra_completa PASSED

============================== 4 passed in 5.17s ===============================
```

---

## ✨ Mejoras futuras (ideas)

- Agregar tests con `problem_user` y `performance_glitch_user`
- Validar precios, descuentos y totales en el checkout
- Ejecutar en paralelo con pytest-xdist
- Integrar con GitHub Actions (CI/CD)
- Generar reportes HTML con `pytest-html` o Allure
