from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    PRODUCT_LINK = (By.CSS_SELECTOR, '.image_container a')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    PASSWORD_FIELD_CONFIRM = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    ADD_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ALERT_TITLE = (By.CSS_SELECTOR, '.alertinner strong')
    ALERT_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    ADD_BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')


class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
