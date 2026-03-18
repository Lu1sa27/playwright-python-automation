from data.login_data import LOGIN_DATA

def test_homepage(page, base_url):
    page.goto(base_url)
    assert page.title() == "Swag Labs"   
