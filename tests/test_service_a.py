"""
Test cases for service A.
"""
from unittest.mock import MagicMock

import pytest

from src.clients.http_client import HttpClient
from src.services.srv_a import ServiceA


class FakeResponse:
    def __init__(self, data: dict = None):
        self.data = data or {"message": "Hello"}

    def json(self) -> dict:
        return self.data


def test_client_service_can_sent_a_message_successfully():
    """
    Given a `mocked HTTP client` with a `FakeResponse` and a `service A` instance.
    When a message is sent at some url with some data,
    Then the message should be sent successfully and the response
    should be the same as the `FakeResponse` data.
    """

    # Given
    mocked_http_client = MagicMock(HttpClient)
    mocked_http_client.send = MagicMock(return_value=FakeResponse())
    srv_a = ServiceA(mocked_http_client)
    # When
    fake_url = "http://some_host:8000/some_endpoint"
    fake_data = {"message:": "hi"}
    resp = srv_a.send_message(fake_url, data=fake_data)
    # Then
    assert resp == {"message": "Hello"}
    mocked_http_client.send.assert_called_once_with(fake_url, fake_data)


def test_client_service_fails_to_send_message():
    """
    Given a `mocked HTTP client` that raises an exception and a `service A` instance.
    When a message is `send` at some url with some data,
    Then the message should fail to be sent and the exception should be raised.
    """

    # Given
    mocked_http_client = MagicMock(HttpClient)
    mocked_http_client.send = MagicMock(side_effect=Exception)
    srv_a = ServiceA(mocked_http_client)
    # When
    fake_url = "http://some_host:8000/some_endpoint"
    fake_data = {"message:": "hi"}
    # Then
    with pytest.raises(Exception):
        srv_a.send_message(fake_url, data=fake_data)
    mocked_http_client.send.assert_called_once_with(fake_url, fake_data)
