"""
Test cases for the server module.
"""
import http
from unittest.mock import patch

import pytest

SERVER_MODULE_PATH = "src.server"


@patch(f"{SERVER_MODULE_PATH}.ServiceB.accept_message", return_value=True)
def test_a_client_can_greet_the_server_successfully(mocked_accept_message, api_client):
    """
    Given a `test client` and a service B which is available.
    When a client sends a POST request to "/greet/" with a valid payload
    Then it should receive a 202 status code and a message from the server.
    """
    # Given/When
    response = api_client.post("/greet/", json={"message": "Hello"})
    # Then
    assert response.status_code == http.HTTPStatus.ACCEPTED
    assert response.json() == {"message": "Hello World"}


@patch(f"{SERVER_MODULE_PATH}.ServiceB.accept_message", return_value=False)
def test_a_client_cannot_greet_the_server_because_it_is_unavailable(
    mocked_accept_message, api_client
):
    """
    Given a `test client` and a service B which is unavailable.
    When a client sends a POST request to "/greet/" with a valid payload
    Then it should receive a 503 status code and a message from the server.
    """
    # Given/When
    response = api_client.post("/greet/", json={"message": "Hello"})
    # Then
    assert response.status_code == http.HTTPStatus.SERVICE_UNAVAILABLE
    assert response.json() == {"message": "Service B is not available at the moment"}


def test_a_client_should_receive_422_status_code_when_sending_invalid_payload(api_client):
    """
    Given a `test client`
    When a client sends a POST request to "/greet/" with an invalid payload
    Then it should receive a `UNPROCESSABLE_ENTITY` status code.
    """
    # Given/When
    response = api_client.post("/greet/", json={"invalid_key": "Hello"})
    # Then
    assert response.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY


@pytest.mark.parametrize("non_valid_methods", ["get", "put", "delete", "patch", "head", "options"])
def test_a_client_should_receive_405_status_code_when_sending_other_methods(
    non_valid_methods, api_client
):
    """
    Given a `test client`
    When a client sends a non-valid request to "/greet/"
    Then it should receive a `METHOD_NOT_ALLOWED` status code.
    """
    # Given/When
    response = getattr(api_client, non_valid_methods)("/greet/")
    # Then
    assert response.status_code == http.HTTPStatus.METHOD_NOT_ALLOWED
