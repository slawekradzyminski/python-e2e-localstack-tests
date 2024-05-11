from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.abstract_base_page import AbstractBasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.edit_page import EditPage


class HomePage(AbstractBasePage):
    header_h1 = (By.CSS_SELECTOR, "h1")
    logout_link = (By.ID, "logout")
    add_more_users_link = (By.ID, "addmore")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def verify_header(self, expected_header: str):
        self.wait.until(EC.visibility_of_element_located(self.header_h1))
        actual_header = self.driver.find_element(*self.header_h1).text
        assert (
            expected_header in actual_header
        ), f"Expected header to be '{expected_header}' but found '{actual_header}'"

    def click_edit_on(self, user):
        row_with_my_user = self._find_row_with_user(user)
        edit_button = row_with_my_user.find_element(By.CLASS_NAME, "edit")
        edit_button.click()
        return EditPage(self.driver)

    def _find_row_with_user(self, user):
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
