import pytest
from fastapi.testclient import TestClient

from src.server import app


@pytest.fixture(name="api_client")
def client_fixture():
    client = TestClient(app)
    yield client
