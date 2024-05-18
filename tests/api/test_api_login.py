import pytest
import os
from api.post_sign_in import SignIn
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def sign_in_api():
    return SignIn()

def test_successful_api_login(sign_in_api: SignIn):
    response = sign_in_api.api_call(os.getenv("ADMIN_USERNAME"), os.getenv("ADMIN_PASSWORD"))
    assert response.status_code == 200, "Expected status code 200"
    assert response.json()['token'] is not None, "Token should not be None"
