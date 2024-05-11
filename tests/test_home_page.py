from .fixtures import logged_in_test, chrome_browser


def test_successful_login(logged_in_test):
    home_page, token = logged_in_test
    home_page.verify_header("Slawomir")
