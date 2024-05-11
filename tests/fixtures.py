import json
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api.post_sign_in import sign_in
from pages.home_page import HomePage


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
    chrome_browser.get("http://localhost:8081")
    login_response = sign_in("admin", "admin")
    token = login_response["token"]
    chrome_browser.execute_script(
        "window.localStorage.setItem(arguments[0], arguments[1])",
        "user",
        json.dumps(login_response),
    )
    chrome_browser.get("http://localhost:8081")
    return HomePage(chrome_browser), token
