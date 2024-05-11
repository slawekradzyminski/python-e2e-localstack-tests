from selenium import webdriver
from selenium.webdriver.common.by import By
from api.data.register import User
from components.alert import AlertComponent
from pages.abstract_base_page import AbstractBasePage
from selenium.webdriver.support import expected_conditions as EC

from pages.edit_page import EditPage


class HomePage(AbstractBasePage):
    header_h1 = (By.CSS_SELECTOR, "h1")
    logout_link = (By.ID, "logout")
    add_more_users_link = (By.ID, "addmore")
    alert_success = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def verify_header(self, expected_header: str):
        self.wait.until(EC.visibility_of_element_located(self.header_h1))
        actual_header = self.driver.find_element(*self.header_h1).text
        assert (
            expected_header in actual_header
        ), f"Expected header to be '{expected_header}' but found '{actual_header}'"

    def click_edit_on(self, user: User):
        row_with_my_user = self._find_row_with_user(user)
        edit_button = row_with_my_user.find_element(By.CLASS_NAME, "edit")
        edit_button.click()
        return EditPage(self.driver)
    
    def get_alert(self):
        return AlertComponent(self.driver)
    
    def verify_user_displayed(self, user: User):
        try:
            self._find_row_with_user(user)
        except ValueError:
            assert False, f"User {user.firstName} {user.lastName} should be displayed but is not."
        return self

    def verify_user_not_displayed(self, user: User):
        try:
            self._find_row_with_user(user)
            assert False, f"User {user.firstName} {user.lastName} should not be displayed but is."
        except ValueError:
            pass # expected
        return self

    def _find_row_with_user(self, user: User):
        users_list = self._get_users()
        for element in users_list:
            if f"{user.firstName} {user.lastName}" in element.text:
                return element
        raise ValueError("Could not find the user")

    def _get_users(self):
        self.wait.until(
            lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "ul > li")) >= 2
        )
        return self.driver.find_elements(By.CSS_SELECTOR, "ul > li")
