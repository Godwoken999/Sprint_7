import pytest
import requests

from urls import Urls
from helpers import generate_order_payload


class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None
    ])
    def test_create_order_with_different_colors_returns_track(self, color):
        payload = generate_order_payload(color)

        response = requests.post(Urls.CREATE_ORDER, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()
        assert type(response.json()["track"]) == int
