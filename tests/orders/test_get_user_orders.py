'''Тесты эндпоинта для получения заказов пользователя.'''
import allure
import pytest

from data import Orders


class TestGetUserOrders:

    @allure.title('Получение заказов пользователя')
    @pytest.mark.parametrize(
        'auth, expected',
        [pytest.param(True, Orders.ORDERS_OK, id='auth'),
         pytest.param(False, Orders.UNAUTHORIZED, id='no auth')]
    )
    def test_get_user_orders_success(self, orders_methods, test_user, auth, expected):
        _, token = test_user
        status_code, body = orders_methods.get_user_orders(token if auth else None)
        assert status_code == expected[0]  # and проверка тела
