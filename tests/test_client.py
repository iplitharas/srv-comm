"""
Test cases for the `client` module.
"""

from unittest.mock import patch, call

from src.client import main
from src.services.srv_a import ServiceAException

CLIENT_MODULE_PATH = "src.client"
SERVER_MODULE_PATH = "src.server"


@patch(
    f"{CLIENT_MODULE_PATH}.ServiceA.send_message",
    side_effect=[{"message": "ok"}, ServiceAException, {"message": "ok"}],
)
def test_client_main_with_three_requests_at_the_server(mocked_service_a_send_message):
    """
    Given a client with a maximum of 3 requests
         and a mocked version of ServiceA for the `send_message` method
    When the client sends 3 requests to the server
    Then the client should receive 3 responses from the server.
    """
    # Given/When
    main(3)
    # Then
    expected_calls = [call("http://localhost:8000/greet", data={"message": "hi"})] * 3
    mocked_service_a_send_message.assert_has_calls(expected_calls)
    assert mocked_service_a_send_message.call_count == 3


@patch(f"{CLIENT_MODULE_PATH}.ServiceA.send_message", side_effect=[ServiceAException] * 10)
def test_client_main_with_service_b_down(mocked_service_a_send_message):
    """
    Given a client with a maximum of 10 requests
        and a mocked version of ServiceA for the `send_message` method that raises an exception
    When the client sends 10 requests to the server
    Then the client should receive 10 responses from the server.
    """
    # Given/When
    main(10)
    # Then
    expected_calls = [call("http://localhost:8000/greet", data={"message": "hi"})] * 10
    mocked_service_a_send_message.assert_has_calls(expected_calls)
    assert mocked_service_a_send_message.call_count == 10
