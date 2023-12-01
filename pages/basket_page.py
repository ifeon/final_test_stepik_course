from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), 'basket is not empty'
