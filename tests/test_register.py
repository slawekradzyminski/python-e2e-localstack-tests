import pytest
import os
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from generators.user_generator import get_random_user
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()


@pytest.fixture
def browser(chrome_browser):
    chrome_browser.get(os.getenv("FRONTEND_URL") + "/register")
    return chrome_browser


def test_successful_registration_and_login(browser: webdriver):
    user = get_random_user()
    RegisterPage(browser).register_user(user, LoginPage).get_alert().verify_alert_success(
        "Registration successful"
    )

def test_cancel_registration_opens_login_page(browser: webdriver):
    RegisterPage(browser).click_cancel_button()
    assert browser.current_url.endswith("/login"), "Should redirect to login page after cancel"
