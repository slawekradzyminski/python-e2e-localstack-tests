import requests
import os

from dotenv import load_dotenv

from api.data.user_details import UserDetails

load_dotenv()


def get_user_details(username, token):
    response = requests.get(
        f"{os.getenv('BACKEND_URL')}/users/{username}",
        headers={"Authorization": f"Bearer {token}"},
    )
    response.raise_for_status()
    assert response.status_code == 200, "Failed to fetch user details"
    user_data = response.json()
    user_details = UserDetails(**user_data)
    return user_details
