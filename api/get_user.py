from api.base_api import BaseAPI
from api.data.user_details import UserDetails


class GetUser(BaseAPI):
    def api_call(self, username, token):
        response = self.make_request(
            "GET", f"users/{username}", headers={"Authorization": f"Bearer {token}"}
        )
        response.raise_for_status()
        assert response.status_code == 200, "Failed to fetch user details"
        user_data = response.json()
        user_details = UserDetails(**user_data)
        return user_details
