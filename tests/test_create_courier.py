import allure
import requests
from urls import Urls
from data import CourierData

class TestCreateCourier:

    @allure.title("Проверка успешного создания курьера")
    def test_create_courier_success(self):
        payload = CourierData.valid_courier()

        with allure.step("Создание курьера"):
            response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}


    @allure.title("Проверка, что нельзя создать двух одинаковых курьеров")
    def test_create_two_same_couriers_error(self, courier):
        with allure.step("Создание курьера с уже существующими данными"):
            response = requests.post(Urls.CREATE_COURIER, data=courier)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."


    @allure.title("Проверка ошибки при создании курьера без логина")
    def test_create_courier_without_login_error(self):
        payload = CourierData.courier_without_login()

        with allure.step("Создание курьера без логина"):
            response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

        

    @allure.title("Проверка ошибки при создании курьера без пароля")
    def test_create_courier_without_password_error(self):
        payload = CourierData.courier_without_password()

        with allure.step("Создание курьера без пароля"):
            response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

        

    @allure.title("Проверка ошибки при создании курьера с уже существующим логином")
    def test_create_courier_with_existing_login_error(self, courier):
        payload = CourierData.valid_courier()
        payload["login"] = courier["login"]

        with allure.step("Создание курьера с уже существующим логином"):
            response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
