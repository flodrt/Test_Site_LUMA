from selenium import webdriver
from pages.base_page import BasePage
from pages.sign_in_page import SignInPage
from pages.create_account_page import CreateAccountPage
from pages.category_pages import CategoryPage
from selenium.webdriver.common.by import By

class Locators:
    """Locators on Home Page"""
    SIGN_IN_LINK = (By.PARTIAL_LINK_TEXT, "Sign In")
    CREATE_ACCOUNT_LINK = (By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/customer/account/create/"]')
    WHATS_NEW_PAGE = (By.ID, "ui-id-3")
    WOMEN_PAGE = (By.ID, "ui-id-4")
    MAN_PAGE = (By.ID, "ui-id-5")
    GEAR_PAGE = (By.ID, "ui-id-6")
    TRAINING_PAGE = (By.ID, "ui-id-7")
    SALE_PAGE = (By.ID, "ui-id-8")

class HomePage(BasePage):
    """Main Page"""
    
    def click_sign_in(self):
        """Click link to sing in page"""
        el_sign_in = self.driver.find_element(*Locators.SIGN_IN_LINK)
        el_sign_in.click()
        return SignInPage(self.driver)
    
    def click_create_account(self):
        """Click link to create account page"""
        el_crea_acc = self.driver.find_element(*Locators.CREATE_ACCOUNT_LINK)
        el_crea_acc.click()
        return CreateAccountPage(self.driver)
    
    def category_page(self):
        el_women_category = self.driver.find_element(*Locators.WOMEN_PAGE)
        el_women_category.click()
        return CategoryPage(self.driver)
    