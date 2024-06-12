import pytest
import os
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from generators.user_generator import get_random_user
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()


@pytest.fixture
def register_page(chrome_browser):
    chrome_browser.get(os.getenv("FRONTEND_URL") + "/register")
    return RegisterPage(chrome_browser)


def test_successful_registration_and_login(register_page: RegisterPage):
    user = get_random_user()
    register_page.register_user(user, LoginPage).get_alert().verify_alert_success(
        "Registration successful"
    )

def test_cancel_registration_opens_login_page(register_page: RegisterPage):
    register_page.click_cancel_button()
    assert register_page.driver.current_url.endswith("/login"), "Should redirect to login page after cancel"
