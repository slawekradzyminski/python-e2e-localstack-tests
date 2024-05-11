from .fixtures import logged_in_test, chrome_browser # used


def test_autocomplete(logged_in_test):
    home_page, token, user = logged_in_test
    home_page.click_edit_on(user).verify_user_autocomplete(user)
