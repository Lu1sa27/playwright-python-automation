import pytest 
from pages.login_page import LoginPage
from data.login_data import LOGIN_DATA
from playwright.sync_api import expect

def test_successful_login(page, base_url):
    # Open page
    page.goto(base_url)
    #  Fill in credentials
    login_page = LoginPage(page)

    user = LOGIN_DATA["valid_user"]
    
    login_page.login(user["username"], user["password"])

    expect(page.locator(".title")).to_have_text("Products")

    # Wait for redirect to inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    #  Assert that we have been redirected to the inventory page
    assert "saucedemo" in page.url

def test_invalid_login(page, base_url):
    # Open page
    page.goto(base_url)
    #  Fill in credentials
    login_page = LoginPage(page)

    user = LOGIN_DATA["invalid_user"]

    login_page.login(user["username"],user["password"] )
    # Get error message
    error = login_page.get_error_message()

    # Assert that error message is present
    assert "Username and password do not match" in error