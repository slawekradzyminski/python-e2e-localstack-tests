import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from .chrome_fixture import chrome_browser


@pytest.fixture
def login_page(chrome_browser):
    chrome_browser.get("http://localhost:8081")
    return LoginPage(chrome_browser)


def test_successful_login(login_page):
    login_page.attempt_login("admin", "admin", HomePage).verify_header("Slawomir")


def test_failed_login(login_page):
    login_page.attempt_login("wrong", "wrong", LoginPage).verify_error_alert(
        "Invalid username/password supplied"
    )
