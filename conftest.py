import os
import pytest
from playwright.sync_api import sync_playwright

from config.qa_config import QAConfig
from config.dev_config import DEVConfig
from config.prod_config import PRODConfig

def get_config():
    env = os.getenv("ENV", "prod")

    if env == "dev":
        return DEVConfig()
    elif env == "qa":
        return QAConfig()
    return PRODConfig()

@pytest.fixture(scope="session")
def config():
    return get_config()

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance, config):

    browser_type = config.BROWSER

    if browser_type == "chromium":
        browser = playwright_instance.chromium.launch(headless=config.HEADLESS)
    elif browser_type == "firefox":
        browser = playwright_instance.firefox.launch(headless=config.HEADLESS)
    elif browser_type == "webkit":
        browser = playwright_instance.webkit.launch(headless=config.HEADLESS)
    else:
        raise ValueError(f"Browser {browser_type} not supported")

    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def base_url(config):
    return config.BASE_URL