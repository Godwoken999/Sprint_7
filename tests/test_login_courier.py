import pytest

from api_methods import CourierMethods
from helpers import generate_random_string


class TestLoginCourier:

    def test_login_courier_valid_credentials_returns_status_code_200(self, registered_courier):
        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }

        response = CourierMethods.login_courier(payload)

        assert response.status_code == 200

    def test_login_courier_valid_credentials_returns_id(self, registered_courier):
        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }

        response = CourierMethods.login_courier(payload)

        assert "id" in response.json()

    @pytest.mark.parametrize("required_field", ["login", "password"])
    def test_login_courier_with_empty_required_field_returns_status_code_400(self, registered_courier, required_field):
        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }
        payload[required_field] = ""

        response = CourierMethods.login_courier(payload)

        assert response.status_code == 400

    @pytest.mark.parametrize("required_field", ["login", "password"])
    def test_login_courier_with_empty_required_field_returns_error_message(self, registered_courier, required_field):
        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }
        payload[required_field] = ""

        response = CourierMethods.login_courier(payload)

        assert response.json()["message"] == "Недостаточно данных для входа"

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_courier_with_incorrect_credentials_returns_status_code_404(self, registered_courier, field):
        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }
        payload[field] = payload[field] + "_wrong"

        response = CourierMethods.login_courier(payload)

        assert response.status_code == 404

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_courier_with_incorrect_credentials_returns_account_not_found_message(self, registered_courier, field):
        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }
        payload[field] = payload[field] + "_wrong"

        response = CourierMethods.login_courier(payload)

        assert response.json()["message"] == "Учетная запись не найдена"

    def test_login_nonexistent_courier_returns_status_code_404(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }

        response = CourierMethods.login_courier(payload)

        assert response.status_code == 404

    def test_login_nonexistent_courier_returns_account_not_found_message(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }

        response = CourierMethods.login_courier(payload)

        assert response.json()["message"] == "Учетная запись не найдена"
