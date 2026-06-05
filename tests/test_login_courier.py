import pytest
import requests

from urls import Urls
from helpers import register_new_courier_and_return_login_password, generate_random_string, delete_courier


class TestLoginCourier:

    @pytest.fixture
    def courier(self):
        courier_data = register_new_courier_and_return_login_password()

        yield courier_data

        if courier_data:
            delete_courier(courier_data[0], courier_data[1])

    def test_login_courier_success_returns_id(self, courier):
        payload = {
            "login": courier[0],
            "password": courier[1]
        }

        response = requests.post(Urls.LOGIN_COURIER, data=payload)

        assert response.status_code == 200
        assert "id" in response.json()
        assert type(response.json()["id"]) == int

    @pytest.mark.parametrize("required_field", ["login", "password"])
    def test_login_courier_with_empty_required_field_returns_error(self, courier, required_field):
        payload = {
            "login": courier[0],
            "password": courier[1]
        }
        payload[required_field] = ""

        response = requests.post(Urls.LOGIN_COURIER, data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_courier_with_incorrect_credentials_returns_error(self, courier, field):
        payload = {
            "login": courier[0],
            "password": courier[1]
        }
        payload[field] = payload[field] + "_wrong"

        response = requests.post(Urls.LOGIN_COURIER, data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    def test_login_nonexistent_courier_returns_error(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }

        response = requests.post(Urls.LOGIN_COURIER, data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
