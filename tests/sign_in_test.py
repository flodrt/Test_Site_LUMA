import sys
sys.path.append(sys.path[0]+"/..")
import time

from tests.base_test import BaseTest
from pages.sign_in_page import Locators, SignInPage
from selenium.webdriver.common.by import By 
from tests.test_data import TestData

class SignInTest(BaseTest):
    """Sign In tests"""
    def setUp(self):
        super().setUp()
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/")
        self.sign_in_page = SignInPage(self.driver)
        self.test_data = TestData()

    def test_no_email_enter(self):
        self.sign_in_page.enter_pass(self.test_data.password)
        time.sleep(2)
        self.sign_in_page.click_sing_in_button()
        
        # EXPECTED RESULT
        # 1. User get an information "This is required field." under the email field.
        self.required_field_error(Locators.EMAIL_ERROR)

    def test_sign_in_no_password_entered(self):
        """Test sign in with no password entered"""
        self.sign_in_page.enter_email(self.test_data.email)
        time.sleep(1)
        self.sign_in_page.click_sing_in_button()
        
        # EXPECTED RESULT
        # 1. User get an information "This is required field." under the password field.
        self.required_field_error(Locators.PASSWORD_ERROR)

    def test_sign_in_wrong_format_email_entered(self):
        """Test sign in with no password entered"""
        self.sign_in_page.enter_email(self.test_data.firstname)
        time.sleep(2)
        self.sign_in_page.enter_pass(self.test_data.password)
        self.sign_in_page.click_sing_in_button()
        
        # EXPECTED RESULT
        # 1. User get an information "Please enter a valid email address (Ex: johndoe@domain.com)." under the email field.
        expected_msg = "Please enter a valid email address (Ex: johndoe@domain.com)."
        # a) Check if error appear by locator
        user_error_msg = self.driver.find_elements(*Locators.EMAIL_ERROR)
        # b) Check if error message is correct.
        self.assertEqual(expected_msg, user_error_msg[0].text)
    