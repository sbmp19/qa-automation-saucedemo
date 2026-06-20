"""Tests automatizados para saucedemo.com con Playwright + pytest."""


# ─── Helpers ────────────────────────────────────────────────────────────────────

def login(page, usuario, contrasena):
    page.fill("#user-name", usuario)
    page.fill("#password", contrasena)
    page.click("#login-button")


def texto_error(page):
    return page.text_content('[data-test="error"]')


# ─── Test 1: Producto al carrito ────────────────────────────────────────────────

def test_agregar_producto_al_carrito(pagina):
    login(pagina, "standard_user", "secret_sauce")
    pagina.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    contador = pagina.text_content(".shopping_cart_badge")
    assert contador == "1", f"Se esperaba '1' pero se obtuvo '{contador}'"
    print("✅ TEST 1 PASÓ — Producto agregado al carrito, badge muestra 1")


# ─── Test 2: Login con contraseña incorrecta ────────────────────────────────────

def test_login_contrasena_incorrecta(pagina):
    login(pagina, "standard_user", "wrong_pass")
    error = texto_error(pagina)
    assert error is not None, "No apareció el mensaje de error"
    assert "Username and password do not match" in error
    print("✅ TEST 2 PASÓ — Se muestra error de credenciales inválidas")


# ─── Test 3: Login con usuario bloqueado ────────────────────────────────────────

def test_login_usuario_bloqueado(pagina):
    login(pagina, "locked_out_user", "secret_sauce")
    error = texto_error(pagina)
    assert error is not None, "No apareció el mensaje de error"
    assert "locked out" in error.lower()
    print("✅ TEST 3 PASÓ — Se muestra error de usuario bloqueado")


# ─── Test 4: Compra completa hasta el "Thank you" ──────────────────────────────

def test_compra_completa(pagina):
    login(pagina, "standard_user", "secret_sauce")
    pagina.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    pagina.click(".shopping_cart_link")
    pagina.click("#checkout")
    pagina.fill("#first-name", "Silvia")
    pagina.fill("#last-name", "Meza")
    pagina.fill("#postal-code", "1234")
    pagina.click("#continue")
    pagina.click("#finish")
    mensaje = pagina.text_content(".complete-header")
    assert mensaje is not None, "No apareció el mensaje de confirmación"
    assert "Thank you for your order" in mensaje
    print("✅ TEST 4 PASÓ — Compra completada, aparece 'Thank you for your order'")
