from typing import Type, TypeVar
from selenium import webdriver
from selenium.webdriver.common.by import By
from api.data.register import User
from pages.abstract_base_page import AbstractBasePage
from pages.login_page import LoginPage

T = TypeVar('T', bound='AbstractBasePage')

class RegisterPage(AbstractBasePage):
    first_name_input = (By.NAME, "firstName")
    last_name_input = (By.NAME, "lastName")
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    email_input = (By.NAME, "email")
    register_button = (By.CSS_SELECTOR, "button.btn.btn-primary")
    cancel_button = (By.CSS_SELECTOR, ".btn-link")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def register_user(self, user: User, expected_page: Type[T]) -> T:
        self.driver.find_element(*self.first_name_input).send_keys(user.firstName)
        self.driver.find_element(*self.last_name_input).send_keys(user.lastName)
        self.driver.find_element(*self.username_input).send_keys(user.username)
        self.driver.find_element(*self.password_input).send_keys(user.password)
        self.driver.find_element(*self.email_input).send_keys(user.email)
        self.driver.find_element(*self.register_button).click()
        return self.new_instance_of(expected_page)

    def click_cancel_button(self):
        self.driver.find_element(*self.cancel_button).click()
        return LoginPage(self.driver)
