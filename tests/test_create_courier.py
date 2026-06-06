import pytest

from api_methods import CourierMethods
from helpers import generate_courier_payload, generate_random_string


class TestCreateCourier:

    def test_create_courier_valid_data_returns_status_code_201(self, courier_payload):
        response = CourierMethods.create_courier(courier_payload)

        assert response.status_code == 201

    def test_create_courier_valid_data_returns_ok_true(self, courier_payload):
        response = CourierMethods.create_courier(courier_payload)

        assert response.json() == {"ok": True}

    def test_create_same_courier_returns_status_code_409(self, registered_courier):
        response = CourierMethods.create_courier(registered_courier)

        assert response.status_code == 409

    def test_create_same_courier_returns_login_already_used_message(self, registered_courier):
        response = CourierMethods.create_courier(registered_courier)

        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @pytest.mark.parametrize("required_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_status_code_400(self, required_field):
        payload = generate_courier_payload()
        payload.pop(required_field)

        response = CourierMethods.create_courier(payload)

        assert response.status_code == 400

    @pytest.mark.parametrize("required_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_error_message(self, required_field):
        payload = generate_courier_payload()
        payload.pop(required_field)

        response = CourierMethods.create_courier(payload)

        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    def test_create_courier_with_existing_login_returns_status_code_409(self, registered_courier):
        payload = {
            "login": registered_courier["login"],
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = CourierMethods.create_courier(payload)

        assert response.status_code == 409

    def test_create_courier_with_existing_login_returns_login_already_used_message(self, registered_courier):
        payload = {
            "login": registered_courier["login"],
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = CourierMethods.create_courier(payload)

        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
