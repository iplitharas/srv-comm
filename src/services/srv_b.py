"""
Services B pays the role of a server where at 90% of the time
it responses with the message `World` and at 10% of the time
with a failure message for example
`Service B is not available at the moment`
"""

import random


class ServiceB:
    def __init__(self, message: str = "World"):
        self.message = message

    @staticmethod
    def accept_message() -> bool:
        return True if random.random() <= 0.9 else False

    def render_response(self) -> str:
        return self.message
