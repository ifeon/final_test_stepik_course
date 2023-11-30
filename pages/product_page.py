from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_to_basket.click()

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def alert_title(self):
        return self.browser.find_element(*ProductPageLocators.ALERT_TITLE).text

    def alert_price(self):
        return self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
