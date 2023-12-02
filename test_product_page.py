import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,
                       'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser,
                       'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    page.open()
    page.add_to_basket()
    page.should_disappear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser,
                       'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/')
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser,
                       'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser,
                       'https://selenium1py.pythonanywhere.com/ru/catalogue/')
    page.open()
    page.product_link_click()
    page = BasketPage(browser,
                      browser.current_url)
    page.basket_button_click_quest()
    page.basket_empty_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture
    def setup(self, browser):
        page = ProductPage(browser,
                           'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser,
                         browser.current_url)
        email = page.email_generator()
        password = page.password_generator()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        page = ProductPage(browser,
                           'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        page = ProductPage(browser,
                           f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        page.open()
        page.add_to_basket()
        page.compare_product_title()
        page.compare_product_price()


class TestGuestAddToBasketFromProductPage:
    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser,
                           'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser,
                           f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}")
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.compare_product_title()
        page.compare_product_price()
