import json
from http.client import HTTPConnection


class CustomHTTPConnection(HTTPConnection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_send = self.send
        self.send = self.custom_send

    def custom_send(self, data):
        self._original_send(data)
        if isinstance(data, bytes):
            try:
                headers, body = data.decode().split("\r\n\r\n")
                print("Request Headers:\n", headers)
                if body:
                    print("Request Body:\n", json.dumps(json.loads(body), indent=4))
            except Exception as e:
                print("Could not log request:", e)


HTTPConnection.send = CustomHTTPConnection.send
