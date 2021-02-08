from .base_page import BasePage
from .locators import RegisterPageLocators


class LoginPage(BasePage):

    def register_new_user(self):
        email = self.generation_email()
        password = self.generation_password()
        input_email = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD)
        input_password.send_keys(password)
        input_password_confirm = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD_CONFIRM)
        input_password_confirm.send_keys(password)
        button_submit = self.browser.find_element(*RegisterPageLocators.REGISTER_BTN)
        button_submit.click()
