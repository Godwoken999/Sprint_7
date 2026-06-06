import allure
import requests

from urls import Urls


class CourierMethods:

    @staticmethod
    @allure.step("Создать курьера")
    def create_courier(payload):
        return requests.post(Urls.CREATE_COURIER, data=payload)

    @staticmethod
    @allure.step("Авторизовать курьера")
    def login_courier(payload):
        return requests.post(Urls.LOGIN_COURIER, data=payload)

    @staticmethod
    @allure.step("Удалить курьера")
    def delete_courier(login, password):
        login_payload = {
            "login": login,
            "password": password
        }

        login_response = CourierMethods.login_courier(login_payload)

        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            return requests.delete(f'{Urls.CREATE_COURIER}/{courier_id}')

        return login_response


class OrderMethods:

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload):
        return requests.post(Urls.CREATE_ORDER, json=payload)

    @staticmethod
    @allure.step("Получить список заказов")
    def get_order_list():
        return requests.get(Urls.ORDER_LIST)
