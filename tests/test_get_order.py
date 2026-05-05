import allure
import requests
from urls import Urls

class TestGetOrders:

    @allure.title("Проверка получения списка заказов")
    def test_get_orders_returns_orders_list(self):
        with allure.step("Получение списка заказов"):
            response = requests.get(Urls.GET_ORDERS)

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
