import allure
import requests
from urls import Urls

class TestLoginCourier:

    @allure.title("Проверка успешной авторизации курьера")
    def test_login_courier_success(self, courier):
        response = requests.post(Urls.LOGIN_COURIER, data={
            "login": courier["login"],
            "password": courier["password"]
        })

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Проверка ошибки авторизации без логина")
    def test_login_courier_without_login_error(self, courier):
        response = requests.post(Urls.LOGIN_COURIER, data={
            "password": courier["password"]
        })

        response_json = response.json()
        
        assert response.status_code == 400
        assert response_json["message"] == "Недостаточно данных для входа"

    @allure.title("Проверка ошибки авторизации без пароля")
    def test_login_courier_without_password_error(self, courier):
        response = requests.post(Urls.LOGIN_COURIER, data={
            "login": courier["login"],
            "password": ""
        })
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"    

    @allure.title("Проверка ошибки авторизации с неверным логином")
    def test_login_courier_with_wrong_login_error(self, courier):
        response = requests.post(Urls.LOGIN_COURIER, data={
            "login": courier["login"] + "wrong",
            "password": courier["password"]
        })

        response_json = response.json()
        
        assert response.status_code == 404
        assert response_json["message"] == "Учетная запись не найдена"

    @allure.title("Проверка ошибки авторизации с неверным паролем")
    def test_login_courier_with_wrong_password_error(self, courier):
        response = requests.post(Urls.LOGIN_COURIER, data={
            "login": courier["login"],
            "password": courier["password"] + "wrong"
        })

        response_json = response.json()
        
        assert response.status_code == 404
        assert response_json["message"] == "Учетная запись не найдена"
        

    @allure.title("Проверка ошибки авторизации несуществующего пользователя")
    def test_login_nonexistent_courier_error(self):
        response = requests.post(Urls.LOGIN_COURIER, data={
            "login": "nonexistent_login_12345",
            "password": "nonexistent_password_12345"
        })

        response_json = response.json()
        
        assert response.status_code == 404
        assert response_json["message"] == "Учетная запись не найдена"
