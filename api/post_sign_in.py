import requests
import os

from api.data.login import LoginRequestDto, LoginResponseDto
from dotenv import load_dotenv

load_dotenv()


def sign_in(username, password):
    login_request = LoginRequestDto(username=username, password=password).to_dict()
    response = requests.post(f"{os.getenv('BACKEND_URL')}/users/signin", json=login_request)
    response.raise_for_status()
    assert response.status_code == 200, "Failed to log in"
    return response.json()

