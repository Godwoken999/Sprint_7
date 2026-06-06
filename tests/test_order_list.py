from api_methods import OrderMethods


class TestOrderList:

    def test_get_order_list_returns_status_code_200(self):
        response = OrderMethods.get_order_list()

        assert response.status_code == 200

    def test_get_order_list_response_body_contains_orders_key(self):
        response = OrderMethods.get_order_list()

        assert "orders" in response.json()

    def test_get_order_list_orders_value_is_list(self):
        response = OrderMethods.get_order_list()

        assert type(response.json()["orders"]) == list
