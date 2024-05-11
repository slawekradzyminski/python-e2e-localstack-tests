import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def chrome_browser():
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    yield browser
    browser.quit()