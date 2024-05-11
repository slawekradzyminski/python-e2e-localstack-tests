import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def chrome_browser():
    options = Options()
    options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service, options=options)
    yield browser
    browser.quit()