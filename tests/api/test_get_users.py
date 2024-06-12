import pytest
import os
from api.data.user_details import UserDetails
from api.delete_user import DeleteUser
from api.get_users import GetUsers
from dotenv import load_dotenv
import requests


load_dotenv()

@pytest.fixture
def get_users_api_logged_in(api_logged_in: str):
    yield GetUsers(), api_logged_in

@pytest.fixture
def get_users_api():
    return GetUsers()

def test_successful_get_users(get_users_api_logged_in):
    get_users, token = get_users_api_logged_in
    users_details = get_users.api_call(token)
    assert len(users_details) > 0, "No users found"
    assert all(isinstance(user, UserDetails) for user in users_details), "Invalid user details type"

def test_failed_get_users_with_bad_token(get_users_api: GetUsers):
    get_users = get_users_api
    bad_token = "bad_token_value"
    try:
        get_users.api_call(bad_token)
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 403, "Expected status code 403"

def test_get_users_no_auth_header(get_users_api: GetUsers):
    get_users = get_users_api
    try:
        get_users.api_call_no_header()
    except requests.exceptions.HTTPError as e:
        assert e.response.status_code == 403, "Expected status code 403 for missing auth header"