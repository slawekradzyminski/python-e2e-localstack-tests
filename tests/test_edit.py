import time
from typing import Tuple
from api.data.register import User
from api.get_user import get_user_details
from generators.user_generator import get_random_user
from pages.home_page import HomePage
from .fixtures import logged_in_test, chrome_browser  # used


def test_autocomplete(logged_in_test: Tuple[HomePage, str, User]):
    home_page, token, user = logged_in_test
    home_page.click_edit_on(user).verify_user_autocomplete(user)


def test_edit(logged_in_test: Tuple[HomePage, str, User]):
    home_page, token, user = logged_in_test
    newUser = get_random_user()
    home_page.click_edit_on(user).edit_user(newUser, HomePage).verify_user_displayed(
        newUser
    ).verify_user_not_displayed(user).get_alert().verify_alert_success(
        "Updating user successful"
    )
    assert_user_via_api(user, newUser, token)


def assert_user_via_api(user, newUser, token):
    time.sleep(1)  # give server some time to process changes
    user_details = get_user_details(user.username, token)
    assert user_details.firstName == newUser.firstName
    assert user_details.lastName == newUser.lastName
    assert user_details.email == newUser.email
    assert user_details.roles == user.roles
    assert user_details.username == user.username
