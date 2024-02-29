"""
Simple HTTP client wrapper to send POST requests to a given URL.
"""

import requests


class HttpClient:
    def __init__(self, client=requests):
        self.client = client

    def send(self, url: str, data: dict) -> requests.Response | None:
        response = self.client.post(url, json=data)
        response.raise_for_status()
        return response
