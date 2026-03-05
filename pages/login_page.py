class LoginPage(BasePage):
    def __init__(self, page):        
        #Initialize the login page elements
        super().__init__(page)
        self.username_input = "luisamsotoa@gmail.com"
        self.password_input = "gvm-cjf6qzu6EWA!qyt"
        self.login_button = "#login"

    def login (self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)