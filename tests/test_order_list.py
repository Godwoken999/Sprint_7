import requests

from urls import Urls


class TestOrderList:

    def test_get_order_list_returns_orders_list(self):
        response = requests.get(Urls.ORDER_LIST)

        response_body = response.json()

        assert response.status_code == 200
        assert "orders" in response_body
        assert type(response_body["orders"]) == list
