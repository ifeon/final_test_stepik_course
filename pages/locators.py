from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ALERT_TITLE = (By.CSS_SELECTOR, '.alertinner strong')
    ALERT_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    ADD_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')
