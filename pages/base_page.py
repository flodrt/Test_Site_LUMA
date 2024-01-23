from selenium.webdriver.common.alert import Alert

class BasePage():
    """ Base class, methods that all pages can use"""
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()
        self.alert = Alert(self.driver)

    def _verify_page(self):
        # Test page name if its correct
        # if all links are operating correctly, 
        # testing cookies, 
        # reviewing forms on webpage, 
        # evaluating database security, 
        # and validating CSS or HTML.
        pass
