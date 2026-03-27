from data.login_data import LOGIN_DATA
from utils.logger import get_logger

logger = get_logger(__name__)

def test_homepage(page, base_url):
    page.goto(base_url)
    logger.info("Open URL")
    assert page.title() == "Swag Labs"   
