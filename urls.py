class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

    CREATE_COURIER = f"{BASE_URL}/api/v1/courier"
    LOGIN_COURIER = f"{BASE_URL}/api/v1/courier/login"
    CREATE_ORDER = f"{BASE_URL}/api/v1/orders"
    GET_ORDERS = f"{BASE_URL}/api/v1/orders"

    @staticmethod
    def delete_courier(courier_id):
        return f"{Urls.BASE_URL}/api/v1/courier/{courier_id}"
