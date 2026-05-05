import allure
import pytest
import requests
from helpers import register_new_courier_and_return_login_password
from urls import Urls


@pytest.fixture
def courier():
    with allure.step("Создание курьера"):
        courier_data = register_new_courier_and_return_login_password()

    yield courier_data

    with allure.step("Логин курьера для получения id"):
        response = requests.post(Urls.LOGIN_COURIER, data={
            "login": courier_data["login"],
            "password": courier_data["password"]
        })

        courier_id = response.json()["id"]

    with allure.step("Удаление курьера после теста"):
        requests.delete(Urls.delete_courier(courier_id))