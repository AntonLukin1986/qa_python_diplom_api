'''Тесты эндпоинта для создания заказов.'''
import random

import allure
import pytest

from data import Common, Orders
from helpers import code_and_body_are_expected


class TestMakeOrders:

    @allure.title('Успешное создание нового заказа')
    @pytest.mark.parametrize(
        'auth', [pytest.param(False, id='no auth'),
                 pytest.param(True, id='auth')]
    )
    def test_make_order_success(self, orders_methods, test_user, auth):
        response_body = orders_methods.get_ingredients().json()
        ingredients = random.sample(
            response_body['data'], k=random.randint(1, 5)
        )
        ingredients_ids = [ingredient['_id'] for ingredient in ingredients]
        _, token = test_user
        response = orders_methods.make_order(
            ingredients_ids, token if auth else None
        )
        result, message = code_and_body_are_expected(response, *Orders.CREATED)
        assert result, message

    @allure.title(
        'Невозможно создать заказ без или с неверным хешем ингредиентов'
    )
    @pytest.mark.parametrize(
        'ids, expected',
        [pytest.param([], Orders.NO_IDS, id='no ids'),
         pytest.param([Common.ADD], Orders.WRONG_IDS, id='wrong ids')]
    )
    def test_make_order_incorrect_ingredients_error(
        self, orders_methods, ids, expected
    ):
        response = orders_methods.make_order(ids, token=None)
        result, message = code_and_body_are_expected(response, *expected)
        assert result, message
