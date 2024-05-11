import json
import pytest
import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api.post_sign_in import sign_in
from api.post_sign_up import register_user
from generators.user_generator import get_random_user
from pages.home_page import HomePage
from dotenv import load_dotenv

load_dotenv()
frontend_url = os.getenv("FRONTEND_URL")


@pytest.fixture
def chrome_browser():
    options = Options()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service, options=options)
    yield browser
    browser.quit()


@pytest.fixture
def logged_in_test(chrome_browser):
    user = get_random_user()
    register_user(user)
    chrome_browser.get(frontend_url)
    login_response = sign_in(user.username, user.password)
    setup_user_local_storage(chrome_browser, login_response)
    chrome_browser.get(frontend_url)
    return HomePage(chrome_browser), login_response["token"], user


def setup_user_local_storage(browser, login_response):
    browser.execute_script(
        "window.localStorage.setItem(arguments[0], arguments[1])",
        "user",
        json.dumps(login_response),
    )
