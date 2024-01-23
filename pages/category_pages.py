from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    """Locators on Category Pages"""
    PAGE_HEADER = (By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
    TOPS_CATEGORY = (By.CSS_SELECTOR, 'dd ol.items li.item a')
    BOTTOMS_CATEGORY = (By.CSS_SELECTOR, 'dd ol.items li.item a')
    JACKETS_CATEGORY = (By.XPATH, '//a[text()="Jackets"]/@href')
    LIMITER_ITEMS_ON_PAGE_SET_36 = (By.XPATH, '//select[@id="limiter"]//option[@value="36"]')
    ITEM_IMAGE_ON_PAGE = (By.XPATH, '//img[@class="product-image-photo"]')
    SORTER_BY_PRICE = (By.XPATH, '//select[@id="sorter"]//option[@value="price"]')
    PRICE_OF_PRODUCT_ON_LIST = (By.XPATH ,'//span[@class="price"]')

class CategoryPage(BasePage):
    
    def _verify_page(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located(Locators.TOPS_CATEGORY))
        wait.until(EC.visibility_of_element_located(Locators.BOTTOMS_CATEGORY))


    def open_tops_category(self):
        el_tops = self.driver.find_elements(*Locators.TOPS_CATEGORY)
        el_tops[0].click()

    def open_bottoms_category(self):
        el_bottoms = self.driver.find_elements(*Locators.BOTTOMS_CATEGORY)
        el_bottoms[1].click()

    def open_jackets_category(self):
        el_jackets = self.driver.find_element(*Locators.JACKETS_CATEGORY)
        el_jackets.click()   

    def change_item_amount_on_page_to_36(self):
        els_item_amount = self.driver.find_elements(*Locators.LIMITER_ITEMS_ON_PAGE_SET_36)
        el_item_amount = [i for i in els_item_amount if i.is_displayed()]
        el_item_amount[0].click()

    def amount_of_all_displayed_items_on_page(self):
        els_displayed_items_on_page = self.driver.find_elements(*Locators.ITEM_IMAGE_ON_PAGE)
        return len(els_displayed_items_on_page)
    
    def sort_items_by_price(self):
        el_sort_items = self.driver.find_element(*Locators.SORTER_BY_PRICE)
        el_sort_items.click()
    
    def all_products_sorted_by_price(self):
        els_items_prices = self.driver.find_elements(*Locators.PRICE_OF_PRODUCT_ON_LIST)
        els_items_prices = [i for i in els_items_prices if i.is_displayed()]
        products_order_after_sorting_by_price = [] 
        for price in els_items_prices:
            products_order_after_sorting_by_price.append(price.text)
        return products_order_after_sorting_by_price
    
    def properly_sorted_items_by_price_ascending(self):
        items_on_page = self.all_products_sorted_by_price()
        items_on_page.sort()
        return items_on_page

