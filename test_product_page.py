import pytest

from .pages.product_page import ProductPage


@pytest.mark.skip
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser,
                       f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}")
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_title = page.get_product_title()
    product_price = page.get_product_price()
    alert_title = page.alert_title()
    alert_price = page.alert_price()
    assert product_title == alert_title, 'the title doesnt match'
    assert product_price == alert_price, 'the price doesnt match'


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,
                       'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser,
                       'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    page.open()
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


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser,
                       'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    page.open()
    page.go_to_login_page()