'''Тесты эндпоинта для создания заказов.'''
import random

import allure
import pytest

from data import ADD, Orders


class TestMakeOrders:

    @allure.title('Успешное создание нового заказа')
    @pytest.mark.parametrize(
        'auth', [pytest.param(False, id='no auth'),
                 pytest.param(True, id='auth')]
    )
    def test_make_order_success(self, orders_methods, test_user, auth):
        _, json = orders_methods.get_ingredients()
        ingredients = random.sample(json['data'], k=random.randint(1, 5))
        ingredients_ids = [ingredient['_id'] for ingredient in ingredients]
        _, token = test_user
        status_code, body = orders_methods.make_order(ingredients_ids, token if auth else None)
        assert status_code == 200  # and проверка тела

    @allure.title(
        'Невозможно создать заказ без или с неверным хешем ингредиентов'
    )
    @pytest.mark.parametrize(
        'ids, expected',
        [pytest.param([], Orders.NO_IDS, id='no ids'),
         pytest.param([ADD], Orders.WRONG_IDS, id='wrong ids')]
    )
    def test_make_order_incorrect_ingredients_error(self, orders_methods, ids, expected):
        status_code, response = orders_methods.make_order(ids, token=None)
        assert status_code == expected[0]  # and проверка тела
