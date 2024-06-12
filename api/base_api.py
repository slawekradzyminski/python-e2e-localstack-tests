import requests
import os
import logging
import json
from dotenv import load_dotenv

load_dotenv()


class BaseAPI:
    def __init__(self):
        self.base_url = os.getenv("BACKEND_URL")
        self.logger = logging.getLogger("http.client")

    def make_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        self.logger.info(f"Making {method} request to URL: {url}")
        
        # Log request headers
        if kwargs.get("headers"):
            self.logger.info(
                "Request Headers:\n" + json.dumps(kwargs["headers"], indent=4)
            )
        
        # Log request body if present
        if kwargs.get("json"):
            self.logger.info(
                "Request JSON Body:\n" + json.dumps(kwargs["json"], indent=4)
            )
        if kwargs.get("data"):
            self.logger.info(
                "Request Form Data:\n" + json.dumps(kwargs["data"], indent=4)
            )
        
        response = requests.request(method, url, **kwargs)
        
        # Log response status code
        self.logger.info(f"Response Status Code: {response.status_code}")
        
        # Log response headers
        self.logger.info(
            "Response Headers:\n" + json.dumps(dict(response.headers), indent=4)
        )
        
        # Log response body for all responses
        try:
            response.raise_for_status()
            if "application/json" in response.headers.get("Content-Type", ""):
                self.logger.info("Response Body:\n" + json.dumps(response.json(), indent=4))
        except requests.exceptions.HTTPError as e:
            # Log error response body
            if "application/json" in response.headers.get("Content-Type", ""):
                self.logger.error("Error Response Body:\n" + json.dumps(response.json(), indent=4))
            raise
        
        return response
