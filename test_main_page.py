import pytest

from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser,
                        'https://selenium1py.pythonanywhere.com/')
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser,
                        'https://selenium1py.pythonanywhere.com/')
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser,
                    'https://selenium1py.pythonanywhere.com/ru/catalogue/')
    page.open()
    page.basket_button_click_quest()
    page = BasketPage(browser,
                      browser.current_url)
    page.basket_empty_message()
