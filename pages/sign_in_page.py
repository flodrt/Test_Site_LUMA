from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    """Locators on Sign In Page"""
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'pass')
    SIGN_IN_BUTTON = (By.ID, 'send2')
    EMAIL_ERROR = (By.ID, "email-error")
    PASSWORD_ERROR = (By.ID, "pass-error")

class SignInPage(BasePage):
    
    def enter_email(self, email):
        """Enter email to sign in"""
        # Find emial field
        el_email = self.driver.find_element(*Locators.EMAIL_FIELD)
        # Enter email
        el_email.send_keys(email)

    def enter_pass(self, password):
        """Enter password to sign in"""
        # Find password field
        el_password = self.driver.find_element(*Locators.PASSWORD_FIELD)
        # Enter password
        el_password.send_keys(password)

    def click_sing_in_button(self):
        """Click button to sign in"""
        # Find button
        el_sign_in_button = self.driver.find_element(*Locators.SIGN_IN_BUTTON)
        # Do action - click
        el_sign_in_button.click()

