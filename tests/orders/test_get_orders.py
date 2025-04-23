'''Тесты эндпоинта для получения заказов пользователя.'''
import allure
import pytest

from data import Orders, Common
from helpers import code_and_body_are_expected


class TestGetOrders:

    @allure.title('Получение заказов пользователя')
    @pytest.mark.parametrize(
        'auth, expected',
        [pytest.param(True, Orders.ORDERS_OK, id='auth'),
         pytest.param(False, Common.UNAUTHORIZED, id='no auth')]
    )
    def test_get_user_orders_success(
        self, orders_methods, test_user, auth, expected
    ):
        _, token = test_user
        response = orders_methods.get_user_orders(token if auth else None)
        result, message = code_and_body_are_expected(response, *expected)
        assert result, message

    @allure.title('Получение всех заказов')
    def test_get_all_orders_success(self, orders_methods):
        response = orders_methods.get_all_orders()
        total_orders = len(response.json()['orders'])
        result, message = code_and_body_are_expected(response, *Orders.ORDERS_OK)
        assert result and total_orders == Orders.TOTAL_ORDERS, message
