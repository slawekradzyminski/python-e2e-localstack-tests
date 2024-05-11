from api.base_api import BaseAPI

class DeleteUser(BaseAPI):
    def api_call(self, username, token):
        response = self.make_request(
            "DELETE",
            f"users/{username}",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 204, "Failed to delete user"