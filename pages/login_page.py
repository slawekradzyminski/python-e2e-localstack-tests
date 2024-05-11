from typing import Type, TypeVar
from selenium import webdriver
from components.alert import AlertComponent
from pages.abstract_base_page import AbstractBasePage
from selenium.webdriver.common.by import By

T = TypeVar('T', bound='AbstractBasePage')

class LoginPage(AbstractBasePage):
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button.btn.btn-primary")
    error_alert = (By.CSS_SELECTOR, ".alert.alert-danger")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def attempt_login(self, username: str, password: str, expected_page: Type[T]) -> T:
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return self.new_instance_of(expected_page)

    def get_alert(self):
        return AlertComponent(self.driver)
