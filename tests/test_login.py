import pytest
import os
from pages.home_page import HomePage
from pages.login_page import LoginPage
from .fixtures import chrome_browser  # used
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def login_page(chrome_browser):
    chrome_browser.get(os.getenv("FRONTEND_URL"))
    return LoginPage(chrome_browser)


def test_successful_login(login_page):
    login_page.attempt_login(
        os.getenv("ADMIN_USERNAME"), os.getenv("ADMIN_PASSWORD"), HomePage
    ).verify_header("Slawomir")


def test_failed_login(login_page):
    login_page.attempt_login("wrong", "wrong", LoginPage).verify_error_alert(
        "Invalid username/password supplied"
    )
