import pytest
import requests

from urls import Urls
from helpers import generate_courier_payload, generate_random_string, delete_courier


class TestCreateCourier:

    @pytest.fixture
    def courier_cleanup(self):
        created_couriers = []

        yield created_couriers

        for courier in created_couriers:
            if "login" in courier and "password" in courier:
                delete_courier(courier["login"], courier["password"])

    def test_create_courier_success(self, courier_cleanup):
        payload = generate_courier_payload()

        response = requests.post(Urls.CREATE_COURIER, data=payload)
        courier_cleanup.append(payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_create_two_same_couriers_returns_error(self, courier_cleanup):
        payload = generate_courier_payload()

        first_response = requests.post(Urls.CREATE_COURIER, data=payload)
        courier_cleanup.append(payload)

        second_response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert first_response.status_code == 201
        assert second_response.status_code == 409
        assert second_response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @pytest.mark.parametrize("required_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_error(self, required_field, courier_cleanup):
        payload = generate_courier_payload()
        payload.pop(required_field)

        response = requests.post(Urls.CREATE_COURIER, data=payload)
        courier_cleanup.append(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    def test_create_courier_with_existing_login_returns_error(self, courier_cleanup):
        payload = generate_courier_payload()

        first_response = requests.post(Urls.CREATE_COURIER, data=payload)
        courier_cleanup.append(payload)

        payload_with_existing_login = {
            "login": payload["login"],
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        second_response = requests.post(Urls.CREATE_COURIER, data=payload_with_existing_login)

        assert first_response.status_code == 201
        assert second_response.status_code == 409
        assert second_response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
