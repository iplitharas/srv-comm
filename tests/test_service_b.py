"""
Test cases for Service B
"""
from unittest.mock import patch

import pytest

from src.services.srv_b import ServiceB

SERVICE_B_MODULE_PATH = "src.services.srv_b"


@patch(f"{SERVICE_B_MODULE_PATH}.random")
@pytest.mark.parametrize(
    "fake_random,expected", [(0.6, True), (0.1, True), (0.91, False), (0.99, False)]
)
def test_service_b_accept_message_based_on_a_random_value(mocked_random, fake_random, expected):
    """
    Given a ServiceB instance and the random.random() method is mocked.
    When the `accept_message` method is called
    Then I expect the method to return the right value
    """
    # Given
    mocked_random.random.return_value = fake_random
    service_b = ServiceB()
    # When
    response = service_b.accept_message()
    # Then
    assert response is expected


@pytest.mark.parametrize("message", ["World", "hi there"])
def test_service_b_render_response(message):
    """
    Given a ServiceB instance
    When the `render_response` method is called
    Then I expect the method to return the right value
    """
    # Given
    service_b = ServiceB(message=message)
    # When
    response = service_b.render_response()
    # Then
    assert response == message
