import requests
import os

from api.data.login import LoginRequestDto, LoginResponseDto
from dotenv import load_dotenv

load_dotenv()


def delete_user(username, token):
    response = requests.delete(
        f"{os.getenv('BACKEND_URL')}/users/{username}",
        headers={"Authorization": f"Bearer {token}"},
    )
    response.raise_for_status()
    assert response.status_code == 204, "Failed to delete user"
