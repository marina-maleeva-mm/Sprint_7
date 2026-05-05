from helpers import generate_random_string

class CourierData:

    @staticmethod
    def valid_courier():
        return {
            "login": generate_random_string(),
            "password": generate_random_string(),
            "firstName": generate_random_string()
        }

    @staticmethod
    def courier_without_login():
        return {
            "password": generate_random_string(),
            "firstName": generate_random_string()
        }

    @staticmethod
    def courier_without_password():
        return {
            "login": generate_random_string(),
            "firstName": generate_random_string()
        }

class OrderData:
    BASE_ORDER = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, Пушкина, 1",
        "metroStation": 5,
        "phone": "+79998887766",
        "rentTime": 5,
        "deliveryDate": "2026-05-10",
        "comment": "Позвонить заранее"
    }

    @staticmethod
    def order_with_color(color):
        order = OrderData.BASE_ORDER.copy()
        order["color"] = color
        return order
