import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_successful_login(page):
    # Open page
    page.goto("https://www.saucedemo.com")
    #  Fill in credentials
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    expect(page.locator(".title")).to_have_text("Products")

    # Wait for redirect to inventory page
    page.wait_for_url("**inventory**")
    
    #  Assert that we have been redirected to the inventory page
    assert "saucedemo" in page.url

def test_invalid_login(page):
    # Open page
    page.goto("https://www.saucedemo.com")
    #  Fill in credentials
    login_page = LoginPage(page)
    login_page.login("invalid_user", "wrong_password")
    # Get error message
    error = login_page.get_error_message()

    # Assert that error message is present
    assert "Username and password do not match" in error