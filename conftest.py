import pytest

from api_methods import CourierMethods
from helpers import generate_courier_payload


@pytest.fixture
def courier_payload():
    payload = generate_courier_payload()

    yield payload

    if payload.get("login") and payload.get("password"):
        CourierMethods.delete_courier(payload["login"], payload["password"])


@pytest.fixture
def registered_courier():
    payload = generate_courier_payload()

    CourierMethods.create_courier(payload)

    yield payload

    CourierMethods.delete_courier(payload["login"], payload["password"])
