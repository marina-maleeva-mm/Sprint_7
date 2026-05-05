import allure
import requests
from urls import Urls
from data import CourierData

class TestCreateCourier:

    @allure.title("Проверка успешного создания курьера")
    def test_create_courier_success(self):
        payload = CourierData.valid_courier()

        response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        login_response = requests.post(Urls.LOGIN_COURIER, data={
            "login": payload["login"],
            "password": payload["password"]
        })

        courier_id = login_response.json()["id"]
        requests.delete(Urls.delete_courier(courier_id))

    @allure.title("Проверка, что нельзя создать двух одинаковых курьеров")
    def test_create_two_same_couriers_error(self, courier):
        response = requests.post(Urls.CREATE_COURIER, data=courier)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Проверка ошибки при создании курьера без логина")
    def test_create_courier_without_login_error(self):
        payload = CourierData.courier_without_login()

        response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
        

    @allure.title("Проверка ошибки при создании курьера без пароля")
    def test_create_courier_without_password_error(self):
        payload = CourierData.courier_without_password()

        response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
        

    @allure.title("Проверка ошибки при создании курьера с уже существующим логином")
    def test_create_courier_with_existing_login_error(self, courier):
        payload = CourierData.valid_courier()
        payload["login"] = courier["login"]

        response = requests.post(Urls.CREATE_COURIER, data=payload)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
