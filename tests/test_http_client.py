"""
Test cases for the `http_client` module.
"""
from unittest.mock import MagicMock

import pytest

from src.clients.http_client import HttpClient

MODULE = "src.clients.http_client"


class FakeResponse:
    def __init__(self, data: dict = None, error: bool = True):
        self.data = data or {"message": "Hello"}
        self.error = error

    def json(self) -> dict:
        return self.data

    def raise_for_status(self):
        return self.error


def test_http_client_can_make_a_post_successfully():
    """
    Given a `HttpClient` instance and a mock version of requests.
    When I call the `sent` method with some url with some data,
    Then the request should be made successfully and the post method should be called once
    with the right arguments.
    """
    # Given
    mocked_requests = MagicMock()
    mocked_requests.post = MagicMock(return_value=FakeResponse())
    http_client = HttpClient(client=mocked_requests)
    url = "http://some_host:8000/some_endpoint"
    data = {"message:": "hi"}
    # When
    resp = http_client.send(url, data)
    # Then
    assert resp.json() == {"message": "Hello"}
    mocked_requests.post.assert_called_once_with(url, json=data)


def test_http_client_fails_to_make_a_post():
    """
    Given a `HttpClient` instance and a mock  version of requests
    When I call the `sent` method with some url with some data,
    Then the request should fail to be made and the exception should be raised.
    """
    # Given
    mocked_requests = MagicMock()
    mocked_requests.post = MagicMock(side_effect=Exception)
    http_client = HttpClient(client=mocked_requests)
    url = "http://some_host:8000/some_endpoint"
    data = {"message:": "hi"}
    # When/Then
    with pytest.raises(Exception):
        http_client.send(url, data)
