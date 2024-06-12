from api.base_api import BaseAPI
from api.data.user_details import UserDetails


class GetUsers(BaseAPI):
    def api_call(self, token: str):
        response = self.make_request(
            "GET", "users", headers={"Authorization": f"Bearer {token}"}
        )
        response.raise_for_status()
        assert response.status_code == 200, "Failed to fetch users"
        users_data = response.json()
        users_details = [UserDetails(**user) for user in users_data]
        return users_details
    
    def api_call_no_header(self):
        response = self.make_request(
            "GET", "users"
        )
        return response

