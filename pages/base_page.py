class BasePage:
    # Base class for all page classes to inherit from
    
    def __init__(self, page):
        # initialize the BasePage with a Playwright page object
        self.page = page

    def wait_for_element(self, selector):
        # wait for an element specified by the CSS selector to be present on the page
        return self.page.wait_for_selector(selector)

    def click(self, selector):
        # click on an element specified by the CSS selector        
        self.page.click(selector)

    def fill(self, selector, text):
        # fill an input field specified by the CSS selector with the provided text
        self.page.fill(selector, text)

    def get_text(self, selector):
        # get the text content of an element specified by the CSS selector
        return self.page.text_content(selector)
