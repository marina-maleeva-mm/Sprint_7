import pytest
import requests
from helpers import register_new_courier_and_return_login_password
from urls import Urls


@pytest.fixture
def courier():
    courier_data = register_new_courier_and_return_login_password()

    assert courier_data, "Не удалось создать курьера"

    yield courier_data

    response = requests.post(Urls.LOGIN_COURIER, data={
        "login": courier_data["login"],
        "password": courier_data["password"]
    })

    response_json = response.json()

    assert "id" in response_json

    courier_id = response_json["id"]
    requests.delete(Urls.delete_courier(courier_id))