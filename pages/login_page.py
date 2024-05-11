from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.abstract_base_page import AbstractBasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(AbstractBasePage):
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button.btn.btn-primary")
    error_alert = (By.CSS_SELECTOR, ".alert.alert-danger")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def attempt_login(self, username: str, password: str, expected_page):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return self.new_instance_of(expected_page)
    
    def verify_error_alert(self, error_message: str):
        self.wait.until(EC.visibility_of_element_located(self.error_alert))
        assert self.driver.find_element(*self.error_alert).text == error_message
