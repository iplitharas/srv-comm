"""
Service A pays the role of a client to Service B where
Service A can send a message to Service B using an HTTP client.
"""

from loguru import logger
from src.clients.http_client import HttpClient


class ServiceAException(Exception):
    pass


class ServiceA:
    def __init__(self, client: HttpClient | None = None):
        self.client = client or HttpClient()

    def send_message(self, url: str, data: dict) -> dict | None:
        try:
            resp = self.client.send(url, data)
            return resp.json()
        except Exception as e:
            logger.error(f"Failed to send message due to: {e}")
            raise ServiceAException(f"Failed to send message due to: {e}")
