import pytest 
from pages.login_page import LoginPage
from data.login_data import LOGIN_DATA
from playwright.sync_api import expect
from utils.logger import get_logger

logger = get_logger(__name__)

def test_successful_login(page, base_url):
    # Open page
    page.goto(base_url)
    
    #  Fill in credentials
    login_page = LoginPage(page)

    user = LOGIN_DATA["valid_user"]
    
    login_page.login(user["username"], user["password"])
    logger.info("Starting login test")

    expect(page.locator(".title")).to_have_text("Products")

    # Wait for redirect to inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    #  Assert that we have been redirected to the inventory page
    assert "saucedemo" in page.url
    logger.info("Login successful")

def test_invalid_login(page, base_url):
    # Open page
    page.goto(base_url)
    #  Fill in credentials
    login_page = LoginPage(page)

    user = LOGIN_DATA["invalid_user"]

    login_page.login(user["username"],user["password"] )
    logger.info("Starting login test")

    # Get error message
    error = login_page.get_error_message()

    # Assert that error message is present
    assert "Username and password do not match" in error
    logger.info("Login failuere")