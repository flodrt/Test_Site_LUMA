import sys
sys.path.append(sys.path[0]+"/..")

import unittest
from tests.base_test import BaseTest
from pages.create_account_page import Locators, CreateAccountPage
from selenium.webdriver.common.by import By 
from tests.test_data import TestData


class CreateAccountTest(BaseTest):
    """Create Account tests"""
    def setUp(self):
        super().setUp()
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
        self.create_account_page = CreateAccountPage(self.driver)
        self.test_data = TestData()
    

    def test_Create_an_account_no_firstname_enter(self):
        """Test create account with no first name entered"""
        self.create_account_page.enter_lastname(self.test_data.lastname)
        self.create_account_page.enter_email(self.test_data.email)
        self.create_account_page.enter_password(self.test_data.password)
        self.create_account_page.enter_password_confirmation(self.test_data.password)
        self.create_account_page.click_create_button()
        
        # EXPECTED RESULT
        # 1. User get an information "This is required field." under the first name field.
        self.required_field_error(Locators.FIRST_NAME_ERROR)

    def test_Create_an_account_no_lastname_entered(self):
        self.create_account_page.enter_firstname(self.test_data.firstname)
        self.create_account_page.enter_email(self.test_data.email)
        self.create_account_page.enter_password(self.test_data.password)
        self.create_account_page.enter_password_confirmation(self.test_data.password)
        self.create_account_page.click_create_button()
        
        self.required_field_error(Locators.LAST_NAME_ERROR)

    def test_Create_an_account_no_email_entered(self):
        self.create_account_page.enter_firstname(self.test_data.firstname)
        self.create_account_page.enter_lastname(self.test_data.lastname)
        self.create_account_page.enter_password(self.test_data.password)
        self.create_account_page.enter_password_confirmation(self.test_data.password)
        self.create_account_page.click_create_button()
        
        self.required_field_error(Locators.EMAIL_ERROR)

    def test_Create_an_account_no_password_entered(self):
        self.create_account_page.enter_firstname(self.test_data.firstname)
        self.create_account_page.enter_lastname(self.test_data.lastname)
        self.create_account_page.enter_email(self.test_data.email)
        self.create_account_page.enter_password_confirmation(self.test_data.password)
        self.create_account_page.click_create_button()
        
        self.required_field_error(Locators.PASSWORD_ERROR)

    def test_Create_an_account_no_password_confirmation_entered(self):
        self.create_account_page.enter_firstname(self.test_data.firstname)
        self.create_account_page.enter_lastname(self.test_data.lastname)
        self.create_account_page.enter_email(self.test_data.email)
        self.create_account_page.enter_password(self.test_data.password)
        self.create_account_page.click_create_button()
        
        self.required_field_error(Locators.PASSWORD_CONF_ERROR)

    def test_Create_an_account_wrong_email_format(self):
        self.create_account_page.enter_firstname(self.test_data.firstname)
        self.create_account_page.enter_lastname(self.test_data.lastname)
        self.create_account_page.enter_email(self.test_data.firstname)
        self.create_account_page.enter_password(self.test_data.password)
        self.create_account_page.enter_password_confirmation(self.test_data.password)
        self.create_account_page.click_create_button()
    
        # EXPECTED RESULT
        # 1. User get an information "Please enter a valid email address (Ex: johndoe@domain.com)."
        expected_msg = "Please enter a valid email address (Ex: johndoe@domain.com)."
        # a) Check if error appear by locator
        user_error_msg = self.driver.find_elements(*Locators.EMAIL_ERROR)
        # b) Check if error message is correct.
        self.assertEqual(expected_msg, user_error_msg[0].text)

    def test_Create_an_account_too_short_password_entered(self):
        self.create_account_page.enter_firstname(self.test_data.firstname)
        self.create_account_page.enter_lastname(self.test_data.lastname)
        self.create_account_page.enter_email(self.test_data.email)
        self.create_account_page.enter_password(self.test_data.too_short_password)
        self.create_account_page.enter_password_confirmation(self.test_data.too_short_password)
        self.create_account_page.click_create_button()
    
        # EXPECTED RESULT
        # 1. User get an information "Minimum length of this field must be equal or 
        # greater than 8 symbols. Leading and trailing spaces will be ignored." under the password field.
        expected_msg = "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored."
        # a) Check if error appear by locator
        user_error_msg = self.driver.find_elements(*Locators.PASSWORD_ERROR)
        # b) Check if error message is correct.
        self.assertEqual(expected_msg, user_error_msg[0].text)

    def test_Create_an_account_con_passwd_notequal_to_passwd(self):
        self.create_account_page.enter_firstname(self.test_data.firstname)
        self.create_account_page.enter_lastname(self.test_data.lastname)
        self.create_account_page.enter_email(self.test_data.email)
        self.create_account_page.enter_password(self.test_data.password)
        self.create_account_page.enter_password_confirmation(self.test_data.password+"1")
        self.create_account_page.click_create_button()
    
        # EXPECTED RESULT
        # 1. User get an information "Please enter the same value again." under the confirmation password field.
        expected_msg = "Please enter the same value again."
        # a) Check if error appear by locator
        user_error_msg = self.driver.find_elements(*Locators.PASSWORD_CONF_ERROR)
        # b) Check if error message is correct.
        self.assertEqual(expected_msg, user_error_msg[0].text)