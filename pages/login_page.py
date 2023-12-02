import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, 'Invalid login url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'Register form not found'

    def email_generator(self):
        email = f'email{time.time()}@fakemail.com'
        return email

    def password_generator(self):
        password = f'Pass{str(time.time())[:5]}word'
        return password

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_CONFIRM)
        email_field.send_keys(email)
        password_field1.send_keys(password)
        password_field2.send_keys(password)
        reg_submit_button = self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BUTTON)
        reg_submit_button.click()
