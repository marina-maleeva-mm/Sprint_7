import requests
import random
import string
from urls import Urls

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_courier_and_return_login_password():
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Urls.CREATE_COURIER, data=payload)

    if response.status_code == 201:
        return payload

    return {}
