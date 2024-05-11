from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.abstract_base_page import AbstractBasePage
from selenium.webdriver.support import expected_conditions as EC
from api.data.register import User
from typing import Type, TypeVar

T = TypeVar('T', bound='AbstractBasePage')

class EditPage(AbstractBasePage):
    first_name_input = (By.NAME, "firstName")
    last_name_input = (By.NAME, "lastName")
    email_input = (By.NAME, "email")
    username_input = (By.NAME, "username")
    roles_input = (By.NAME, "roles")
    edit_button = (By.CLASS_NAME, "btn-primary")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def verify_user_autocomplete(self, user: User):
        self.wait.until(EC.visibility_of_element_located(self.first_name_input))
        assert self.driver.find_element(*self.first_name_input).get_attribute('value') == user.firstName
        assert self.driver.find_element(*self.last_name_input).get_attribute('value') == user.lastName
        assert self.driver.find_element(*self.email_input).get_attribute('value') == user.email
        assert self.driver.find_element(*self.username_input).get_attribute('value') == user.username
        assert self.driver.find_element(*self.roles_input).get_attribute('value') == ','.join(user.roles)
        
    def edit_user(self, newUser: User, expected_page: Type[T]) -> T:
        self.wait.until(EC.visibility_of_element_located(self.first_name_input))
        self.driver.find_element(*self.first_name_input).clear()
        self.driver.find_element(*self.first_name_input).send_keys(newUser.firstName)
        self.driver.find_element(*self.last_name_input).clear()
        self.driver.find_element(*self.last_name_input).send_keys(newUser.lastName)
        self.driver.find_element(*self.email_input).clear()
        self.driver.find_element(*self.email_input).send_keys(newUser.email)
        self.driver.find_element(*self.edit_button).click()
        return self.new_instance_of(expected_page)
