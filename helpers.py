import random
import string


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
