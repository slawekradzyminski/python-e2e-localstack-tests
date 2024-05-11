from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class AbstractBasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def new_instance_of(self, expected_page):
        if issubclass(expected_page, AbstractBasePage) and "__init__" in dir(
            expected_page
        ):
            return expected_page(self.driver)
        else:
            raise ValueError("Invalid page class provided")
