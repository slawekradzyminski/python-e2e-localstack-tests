import requests
import os

from api.data.login import LoginRequestDto, LoginResponseDto
from dotenv import load_dotenv

from api.data.register import RegisterRequestDto

load_dotenv()


def register_user(user: RegisterRequestDto):
    response = requests.post(
        f"{os.getenv('BACKEND_URL')}/users/signup", json=user.to_dict()
    )
    response.raise_for_status()
    assert response.status_code == 201, "Failed register"
