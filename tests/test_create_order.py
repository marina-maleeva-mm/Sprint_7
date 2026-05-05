import allure
import pytest
import requests
from urls import Urls
from data import OrderData

class TestCreateOrder:

    @allure.title("Проверка создания заказа с разными вариантами цвета")
    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]
    )
    def test_create_order_with_different_colors_success(self, color):
        payload = OrderData.order_with_color(color)

        response = requests.post(Urls.CREATE_ORDER, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()
