from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from chrome_fixture import chrome_browser
from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_login(chrome_browser):
    chrome_browser.get('http://localhost:8081')
    login_page = LoginPage(chrome_browser)
    login_page.attempt_login("admin", "admin", HomePage).verify_header("Slawomir")

