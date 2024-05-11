import requests

from api.data.login import LoginRequestDto


def sign_in(username, password):
    login_request = LoginRequestDto(username=username, password=password).to_dict()
    response = requests.post("http://localhost:4001/users/signin", json=login_request)
    response.raise_for_status()
    assert response.status_code == 200, "Failed to log in"
    return response.json()