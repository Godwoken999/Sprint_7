import pytest

from api_methods import OrderMethods
from helpers import generate_order_payload


class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None
    ])
    def test_create_order_with_different_colors_returns_status_code_201(self, color):
        payload = generate_order_payload(color)

        response = OrderMethods.create_order(payload)

        assert response.status_code == 201

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None
    ])
    def test_create_order_with_different_colors_returns_track(self, color):
        payload = generate_order_payload(color)

        response = OrderMethods.create_order(payload)

        assert "track" in response.json()
