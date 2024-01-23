from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    """Locators on Create Account Page"""
    FIRST_NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.ID, "password")
    PASSWORD_CONFIRMATION_INPUT = (By.ID, "password-confirmation")
    CREATE_BUTTON = (By.XPATH, '//button[@title="Create an Account"]')
    NEWSLETTER_CHECKBOX = (By.XPATH, '//label[@for="is_subscribed"]')
    FIRST_NAME_ERROR = (By.XPATH, '//div[@id="firstname-error"]')
    LAST_NAME_ERROR = (By.XPATH, '//div[@id="lastname-error"]')
    EMAIL_ERROR = (By.XPATH, '//div[@id="email_address-error"]')
    PASSWORD_ERROR = (By.XPATH, '//div[@id="password-error"]')
    PASSWORD_CONF_ERROR = (By.XPATH, '//div[@id="password-confirmation-error"]')
    
class CreateAccountPage(BasePage):
    """Create Account Page"""
    def _verify_page(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located(Locators.FIRST_NAME_INPUT))
        wait.until(EC.visibility_of_element_located(Locators.LAST_NAME_INPUT))
        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
        wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
        wait.until(EC.visibility_of_element_located(Locators.PASSWORD_CONFIRMATION_INPUT))

    def enter_firstname(self, username):
        """Enter firstname"""
        el_first_name = self.driver.find_element(*Locators.FIRST_NAME_INPUT)
        el_first_name.send_keys(username)

    def enter_lastname(self, lastname):
        """Enter lastname"""
        el_last_name = self.driver.find_element(*Locators.LAST_NAME_INPUT)
        el_last_name.send_keys(lastname)

    def enter_email(self, email):
        """Enter email"""
        el_email = self.driver.find_element(*Locators.EMAIL_INPUT)
        el_email.send_keys(email)

    def enter_password(self, password):
        """Enter password"""
        el_password = self.driver.find_element(*Locators.PASSWORD_INPUT)
        el_password.send_keys(password)

    def enter_password_confirmation(self, password_con):
        """Enter password to confirm"""
        el_password_con = self.driver.find_element(*Locators.PASSWORD_CONFIRMATION_INPUT)
        el_password_con.send_keys(password_con)
    
    def click_create_button(self):
        """Click button to create account"""
        # Find create button
        el_create_button = self.driver.find_element(*Locators.CREATE_BUTTON)
        # Click it!
        el_create_button.click()
    
    def newsletter_accept(self):
        """Mark checkbox to sign email to newsletter"""
        # Find checkbox to accept newsletter
        el_newsletter = self.driver.find_element(*Locators.NEWSLETTER_CHECKBOX)
        # Click checkbox
        el_newsletter.click()
