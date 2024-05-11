from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.abstract_base_page import AbstractBasePage


class LoginPage(AbstractBasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button.btn.btn-primary")

    def new_instance_of(self, expected_page):
        if issubclass(expected_page, AbstractBasePage) and '__init__' in dir(expected_page):
            return expected_page(self.driver)
        else:
            raise ValueError("Invalid page class provided")

    def attempt_login(self, username: str, password: str, expected_page):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return self.new_instance_of(expected_page)
