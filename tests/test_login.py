import pytest
from pages.login_page import LoginPage

def test_successful_login(page):
    # Open page
    page.goto("https://www.saucedemo.com")

    login_page = LoginPage(page)
    
    login_page.login("standard_user", "secret_sauce")
    
    # Validación
    assert "saucedemo" in page.url

def test_invalid_login(page):
    # Abrir página
    page.goto("https://www.saucedemo.com")

    login_page = LoginPage(page)

    # Ejecutar login inválido
    login_page.login("invalid_user", "wrong_password")

    # Validación del mensaje de error
    error = login_page.get_error_message()

    assert "Username and password do not match" in error