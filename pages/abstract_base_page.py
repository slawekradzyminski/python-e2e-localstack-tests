from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from typing import Type, TypeVar

T = TypeVar('T', bound='AbstractBasePage')

class AbstractBasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def new_instance_of(self, expected_page: Type[T]) -> T:
        if issubclass(expected_page, AbstractBasePage):
            return expected_page(self.driver)
        else:
            raise ValueError("Invalid page class provided")
