from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.abstract_base_page import AbstractBasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(AbstractBasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.header_h1 = (By.CSS_SELECTOR, "h1")
        self.logout_link = (By.ID, "logout")
        self.add_more_users_link = (By.ID, "addmore")

    def verify_header(self, expected_header: str):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.header_h1)
        )
        actual_header = self.driver.find_element(*self.header_h1).text
        assert (
            expected_header in actual_header
        ), f"Expected header to be '{expected_header}' but found '{actual_header}'"
