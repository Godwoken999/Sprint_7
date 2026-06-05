import random
import string
import requests

from urls import Urls


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_courier_payload():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload


# метод регистрации нового курьера возвращает список из логина, пароля и имени
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Urls.CREATE_COURIER, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


def get_courier_id(login, password):
    payload = {
        "login": login,
        "password": password
    }

    response = requests.post(Urls.LOGIN_COURIER, data=payload)

    if response.status_code == 200:
        return response.json()["id"]

    return None


def delete_courier(login, password):
    courier_id = get_courier_id(login, password)

    if courier_id is not None:
        requests.delete(f'{Urls.CREATE_COURIER}/{courier_id}')


def generate_order_payload(color=None):
    payload = {
        "firstName": "Eren",
        "lastName": "Yeager",
        "address": "Shiganshin, Wall Maria, 1",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2026-06-06",
        "comment": "Test order"
    }

    if color is not None:
        payload["color"] = color

    return payload
