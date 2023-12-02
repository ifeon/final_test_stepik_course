from .base_page import BasePage
from .locators import ProductPageLocators, MainPageLocators


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

    def compare_product_title(self):
        product_title = self.get_product_title()
        alert_title = self.alert_title()
        assert product_title == alert_title, 'The title doesnt match'

    def compare_product_price(self):
        product_price = self.get_product_price()
        alert_price = self.alert_price()
        assert product_price == alert_price, 'The price doesnt match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_BASKET_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_product_title(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_TITLE), \
            "Product title is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_BASKET_SUCCESS_MESSAGE), \
            "Success message didn't disappear"

    def product_link_click(self):
        product_link = self.browser.find_element(*MainPageLocators.PRODUCT_LINK)
        product_link.click()
