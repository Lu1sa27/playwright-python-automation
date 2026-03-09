from pages.base_page import BasePage

class LoginPage(BasePage):
    #  Login page elements and methods
    def __init__(self, page):        
        #Initialize the login page elements
        super().__init__(page)
        self.username_input = "[data-test='username']"
        self.password_input = "[data-test='password']"
        self.login_button = "[data-test='login-button']"
        self.error_message = "[data-test='error']"

    def login (self, username, password):
        # Perform login with given credentials
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
    
    def get_error_message(self):
        # Get the error message text after failed login attempt
        return self.get_text(self.error_message)