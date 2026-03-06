from pages.base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self, page):        
        #Initialize the login page elements
        super().__init__(page)
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def login (self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
    
    def get_error_message(self):
        return self.get_text(self.error_message)